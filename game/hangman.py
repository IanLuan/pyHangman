class Hangman:
	
	def __init__(self):
		self.__posts = 0
		self.__head = 0
		self.__arms = 0
		self.__legs = 0
		self.__body = 0
		self.__lives = 8


	# Removes parts of the body in order
	def remove(self):

		if self.__lives == 8 or self.__lives == 7:
			self.__posts += 1

		elif self.__lives == 6:
			self.__head += 1	

		elif self.__lives == 5:
			self.__body += 1

		elif self.__lives == 4 or self.__lives == 3:
			self.__arms += 1
			
		elif self.__lives == 2 or self.__lives == 1:
			self.__legs += 1

	
		
		self.__lives -= 1
	
	
	""" 
		Draws the man
		Defines what will be drawn 
	"""
	def draw(self):

		if self.__posts == 1:
			post1 = "°°°°°"
			post2 = ""
		elif self.__posts == 2:
			post1 = "°°°°°"
			post2 = "|"
		else:
			post1 = ""
			post2 = ""

		if self.__head == 1:
			head = "O"
		else:
			head = ""

		if self.__arms == 1:
			armL = "/"
			armR = ""
		elif self.__arms == 2:
			armL = "/"
			armR = "\ "
		else:
			armL = " "
			armR = ""
			
		if self.__body == 1:
			body = "|"
		else:
			body = ""
		
		if self.__legs == 1:
			legL = "/"
			legR = ""
		elif self.__legs == 2:
			legL = "/"
			legR = "\ "
		else:
			legL = ""
			legR = ""
		
		print("|"+post1+post2)
		print("|     "+ head + " ")
		print("|    "+armL + body + armR)
		print("|    "+legL + " " + legR)
		

	# Get the amount of lives
	def getLives(self):
		return self.__lives