from random import choice
lst = {'Tag':0,'JoJo Rabbit':0,'Dictator':0,'Schindler\'s list':0,'The Imitation game':0,'Bohemian Rhapsody':0,'Shawshank redemption':0,'Shutter island':0,'The Prestige':0,'The Matrix':0,'Forest Gump':0,'Shaun of the Dead':0,'Get out':0,'The Shinning':0}
final=['The Imitation game','Tag','The Matrix','Bohemian Rhapsody','JoJo Rabbit']
'''
i=0
while i<500:
	a=choice(list(lst.keys()))
	lst[a]+=1
	i+=1

for j in lst.items():
	print(j)
'''

print(choice(final))