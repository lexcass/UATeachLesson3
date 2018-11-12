def encipher(message, key):
	result = ""		# empty string we'll add to
	
	for character in message:
	
		if character.isalpha():		# if character is a letter ("alpha" as in alphabet)
			ascii = ord(character)	# get character's ASCII code with ord()
			shifted = ascii + key
			
			if shifted > ord('z'):
				shifted -= 26
				
			result += chr(shifted)	# turn integer to character with chr()
			
		else:
			result += character		# if character is not a letter, just add it to the result
			
	return result
	
	
def decipher(message, key):
	result = ""
	
	for character in message:
	
		if character.isalpha():
			ascii = ord(character)
			
			# What do we put here to make this function decipher our enciphered message?
				
			result += chr(shifted)
			
		else:
			result += character
			
	return result

	
	
	
	
	
	
	
	
	
	

	
# Don't worry about the code below. 

command = ""
while True:
	command = input()
	tokens = command.split(" ")
	
	if command == "exit":
		break
	
	func = tokens[0]
	message = tokens[1]
	key = int(tokens[2])
	
	if func == "encipher":
		print(encipher(message, key))
	elif func == "decipher":
		print(decipher(message, key))