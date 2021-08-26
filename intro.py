#-----VARIABLES-----

#message = 'Hello World'

greeting = 'Hello'
name = 'Nikola'

#message = greeting + ', ' + name + '. Welcome!' 	 #-- Complex Way
#message = '{}, {}. Welcome!'.format(greeting, name) # -- Easier Way (string formatting)
message = f'{greeting},{name}. Welcome!' 			 #--New Way (f-string)

#------------EXAMPLES OF DIFFERENT PRINT METHODS------------

# message = message.replace('World','Universe') -- Replaces World with Universe

print(message)

#print('Hello World') -- Prints a string.
#print(len('Hello World')) -- Prints numerical length of a string.
#print(message[1]) -- Prints value at index of string. 
#print(message[0:5]) -- Allows for a range of indexes. i.e. ('Hello') 
#print(message.lower()) -- sets string to lowercase. Can also use 'upper'.
#print(message.count('Hello')) -- Counts occurences of argument ('Hello').
#print(message.find('World')) -- Finds starting index of argument ('World').

