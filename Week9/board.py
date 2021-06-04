
def create_board_ui():
    global lbl_status, top_frame, list_labels
    top_frame = tk.Frame(window_main)
    for x in range(3):
        for y in range(3):
            lbl = tk.Label(top_frame, text=" ", font="Helvetica 45 bold", height=2, width=5, highlightbackground="grey",
                           highlightcolor="grey", highlightthickness=1)
            lbl.bind("<Button-1>", lambda e, xy=[x, y]: get_coordinate(xy))
            lbl.grid(row=x, column=y)

            dict_labels = {"xy": [x, y], "symbol": "", "label": lbl, "ticked": False}
            list_labels.append(dict_labels)

    lbl_status = tk.Label(top_frame, text="Status: Not connected to server", font="Helvetica 14 bold")
    lbl_status.grid(row=3, columnspan=3)

    top_frame.pack_forget()

def get_coordinate(xy):
    global client, your_turn
    # convert 2D to 1D cordinate i.e. index = x * num_cols + y
    label_index = xy[0] * num_cols + xy[1]
    label = list_labels[label_index]

    if your_turn:
        if label["ticked"] is False:
            label["label"].config(foreground=your_details["color"])
            label["label"]["text"] = your_details["symbol"]
            label["ticked"] = True
            label["symbol"] = your_details["symbol"]
            # send xy cordinate to server
            client.send("$xy$" + str(xy[0]) + "$" + str(xy[1]))
            your_turn = False

            # Does this play leads to a win or a draw
            result = game_logic()
            if result[0] is True and result[1] != "":  # a win
                your_details["score"] = your_details["score"] + 1
                lbl_status["text"] = "Game over, You won! You(" + str(your_details["score"]) + ") - " \
                    "" + opponent_details["name"] + "(" + str(opponent_details["score"]) + ")"
                lbl_status.config(foreground="green")
                threading._start_new_thread(init, ("", ""))

            elif result[0] is True and result[1] == "":  # a draw
                lbl_status["text"] = "Game over, Draw! You(" + str(your_details["score"]) + ") - " \
                    "" + opponent_details["name"] + "(" + str(opponent_details["score"]) + ")"
                lbl_status.config(foreground="blue")
                threading._start_new_thread(init, ("", ""))

            else:
                lbl_status["text"] = "STATUS: " + opponent_details["name"] + "'s turn!"
    else:
        lbl_status["text"] = "STATUS: Wait for your turn!"
        lbl_status.config(foreground="red")

def receive_message_from_server(sck, m):
    global your_details, opponent_details, your_turn, you_started
    while True:
        from_server = sck.recv(4096)

        if not from_server: break

        if from_server.startswith("welcome"):
            if from_server == "welcome1":
                your_details["color"] = "purple"
                opponent_details["color"] = "orange"
                lbl_status["text"] = "Server: Welcome " + your_details["name"] + "! Waiting for player 2"
            elif from_server == "welcome2":
                lbl_status["text"] = "Server: Welcome " + your_details["name"] + "! Game will start soon"
                your_details["color"] = "orange"
                opponent_details["color"] = "purple"

        elif from_server.startswith("opponent_name$"):
            temp = from_server.replace("opponent_name$", "")
            temp = temp.replace("symbol", "")
            name_index = temp.find("$")
            symbol_index = temp.rfind("$")
            opponent_details["name"] = temp[0:name_index]
            your_details["symbol"] = temp[symbol_index:len(temp)]

            # set opponent symbol
            if your_details["symbol"] == "O":
                opponent_details["symbol"] = "X"
            else:
                opponent_details["symbol"] = "O"

            lbl_status["text"] = "STATUS: " + opponent_details["name"] + " is connected!"
            sleep(3)
            # is it your turn to play? hey! 'O' comes before 'X'
            if your_details["symbol"] == "O":
                lbl_status["text"] = "STATUS: Your turn!"
                your_turn = True
                you_started = True
            else:
                lbl_status["text"] = "STATUS: " + opponent_details["name"] + "'s turn!"
                you_started = False
                your_turn = False
        elif from_server.startswith("$xy$"):
            temp = from_server.replace("$xy$", "")
            _x = temp[0:temp.find("$")]
            _y = temp[temp.find("$") + 1:len(temp)]

            # update board
            label_index = int(_x) * num_cols + int(_y)
            label = list_labels[label_index]
            label["symbol"] = opponent_details["symbol"]
            label["label"]["text"] = opponent_details["symbol"]
            label["label"].config(foreground=opponent_details["color"])
            label["ticked"] = True

            # Does this coordinate leads to a win or a draw
            result = game_logic()
            if result[0] is True and result[1] != "":  # opponent win
                opponent_details["score"] = opponent_details["score"] + 1
                if result[1] == opponent_details["symbol"]:  #
                    lbl_status["text"] = "Game over, You Lost! You(" + str(your_details["score"]) + ") - " \
                        "" + opponent_details["name"] + "(" + str(opponent_details["score"]) + ")"
                    lbl_status.config(foreground="red")
                    threading._start_new_thread(init, ("", ""))
            elif result[0] is True and result[1] == "":  # a draw
                lbl_status["text"] = "Game over, Draw! You(" + str(your_details["score"]) + ") - " \
                    "" + opponent_details["name"] + "(" + str(opponent_details["score"]) + ")"
                lbl_status.config(foreground="blue")
                threading._start_new_thread(init, ("", ""))
            else:
                your_turn = True
                lbl_status["text"] = "STATUS: Your turn!"
                lbl_status.config(foreground="black")
    sck.close()
def send_receive_client_message(client_connection, client_ip_addr):
    global server, client_name, clients, player_data, player0, player1
    # send welcome message to client
    client_name = client_connection.recv(4096)
    
    if len(clients) < 2:
        client_connection.send("welcome1")
    else:
        client_connection.send("welcome2")

    if len(clients) > 1:
        sleep(1)
        symbols = ["O", "X"]
        # send opponent name and symbol
        clients[0].send("opponent_name$" + clients_names[1] + "symbol" + symbols[0])
        clients[1].send("opponent_name$" + clients_names[0] + "symbol" + symbols[1])

    while True:
        # get the player choice from received data
        data = client_connection.recv(4096)
        if not data: break
        # player x,y coordinate data. forward to the other player
        if data.startswith("$xy$"):
            # is the message from client1 or client2?
            if client_connection == clients[0]:
                # send the data from this player (client) to the other player (client)
                clients[1].send(data)
            else:
                # send the data from this player (client) to the other player (client)
                clients[0].send(data)