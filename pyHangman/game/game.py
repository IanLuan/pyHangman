"""
	Where the game works
	All the game system is here: terminal, options, plays, all.
"""

from game.word import Word
from game.hangman import Hangman
from tqdm import tqdm
import time
import os
import sys

class Game:

	def __init__(self):
		self.terminal()
	

	"""
		Simulates a terminal
		Creates the menu
	"""
	def terminal(self):
		
		print("type 'help' for info")
		
		# Menu loop
		while True:
			op = input("> ")
			
			if op == "help":
				print("- new (New Game) \n- how (How to play) \n- quit (Exit now) \n- help ")
				print()
				
			elif op == "how":
				print("2 or more players")
				print("A player chooses the word and the others try to guess it")
				print("Each can try a word in order. If the letter is in the word, it will be shown. Otherwise, a new part will be drawn and the guessers lose a life. ")
				print("If someone tries the full word and is wrong, he loses.")
				print("If players guess the word, they win.")
				print()

			elif op == "quit":
				sys.exit()
			
			elif op == "new":
				self.newGame()
		
	
	# Start New Game
	def newGame(self):

		# restart
		self.word = Word()
		self.hangman = Hangman()


		theword = input("> Word: ").upper()
		
		while len(theword) < 3:
			print("word too short!")
			theword = input("> Word: ").upper()
		
		if self.word.setWord(theword):
			self.play("_", True)
		
		# Cleans the terminal
		os.system("clear")

		# PROGRESS BAR
		print("LOADING".center(50))
		for i in tqdm(range(10)):
			time.sleep(0.2)

		# Cleans the terminal	
		os.system("clear")
		

		# Game Loop
		while self.word.newWord.replace(" ", "").replace("_", " ") != theword:
			letter = input("> Letter: ").upper()

			# Determines whether it is a letter or the whole word.
			if len(letter) > 1:
				finalGuess = input("You are trying the full word? (y/n) ")
				
				if finalGuess == "y":
					
					if letter == theword:
						self.win()
					else:
						self.lose()

			elif len(letter) == 1:	
				self.play(letter, False)
			else:
				pass
		
		
		# If it comes out of the loop, it wins.
		self.win()
			
	
	# Play Function
	def play(self, letter, spaceRemove):

		self.word.newWord = self.word.newWord.split(" ")
		
		# See if the letter is in the word and makes the decisions.
		if letter in self.word.word and letter not in self.word.tried:
			for i, a in enumerate(self.word.word):
				if a == letter:
					self.word.newWord[i] = letter

			self.word.tried.append(letter)

		elif letter not in self.word.word and letter not in self.word.tried:
			self.hangman.remove()
			if self.hangman.getLives() == 0:
				self.lose()
			
			self.word.tried.append(letter)

		else:
			print("\nYou've tried that letter!")
			
			
		self.word.newWord = " ".join(self.word.newWord)

		if not spaceRemove:
			self.hangman.draw()
			print()
			print(self.word.newWord)
			print()
				

	# Win
	def win(self):
		print("YOU WIN!!!!!! ")
		print()
		self.terminal()
	
	# Lose
	def lose(self):
		self.hangman.draw()
		print()
		print("YOU LOSE! :( ")
		print()
		self.terminal()
