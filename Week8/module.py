# Modules:
'''
A module is a file containing Python defintions and statements. 
The file name is module name with the suffix '.py' appended

-> It contains different functions variables, and classes in one file called LIBRARIES

-> Use of Module:
	Reduce redundancy in code.
	Maintain uniformity in coding style
	* Increase readability and increases productivity and bug reporting *

-> Why need a module:
	Share as a library
	Develop libraries in a domain
	Avoid name clashes


# Module Path:

The python interpreter locates them from three locations:
-> The directory from the program is getting executed
-> The directory specified in the PYTHONPATH variable (shell variable or an environment variable)
-> The default directory

#executing:
-> directly using python module.py
-> indirect using 'import' statement

# Syntax:
import <module_name>
To use functions inside module use,
[module].[function]

OR
from <module_name> import <name()>		--> To import a specific function from module

OR
import [module] as [another_name]		--> represent a module by another name

OR
from [module] import * 					--> import all classes and functions

''' 
