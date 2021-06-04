#CLASS


'''
class dog:
	u_name='Class of the dog'	#Class variable
	def __init__(self):
		print('Class object created')
	def name(self):
		print('Rocky')
	def breed(self):
		print('German Shepherd')
	def colour(self):
		print('Black-Brown')

a=dog()						#Instance variable
							#At the time of object creation a default constructor is invoked
print(a.u_name)
a.name()

'''

# def __init__(): this is the format for constructor

# NOTE:

'''
Functions inside a class are called methods.
Methods of a class require a parameter for proper working.
That is why we use 'self' as a parameter for avoiding error
'''

# Parametrised constructor
class dog:
	u_name='Class of the dog'	
	def __init__(self,name,srn):	# Parametrised constructor
		print('Class object created',name,srn)
a=dog('Bruno',40)


#To access the variables inside a particular method
# self.<variable> makes the variables accessible to objects of the class