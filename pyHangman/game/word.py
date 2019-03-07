class Word:
	
	def __init__(self):
		self.word = ""
		self.newWord = ""
		self.tried = list()
	
	def setWord(self, word):

		word = word.upper()
		word = word.replace(" ", "_")
		self.word = word
			
		# Generates the word mask
		for x in word:
			self.newWord += "* "
		
		# return True if the word has blank spaces
		if "_" in word:
			return True
			
	def print(self):
		print(self.newWord)

	
	
	