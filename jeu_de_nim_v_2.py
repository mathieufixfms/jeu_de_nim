# /usr/bin/env python
# -*-coding: utf-8-*-
"""
Jeu de Nim
Deux joueurs s’affrontent dans ce jeu en se partageant un tas d’allumettes composé au départ de 21
allumettes.
Chaque joueur à son tour enlève entre une et quatre allumettes du tas. Celui qui enlève la dernière
allumette a perdu.
Le programme doit arbitrer une partie se déroulant entre deux joueurs humains, dont leur nom est
demandé au démarrage, ainsi que le joueur qui commence.
"""

def human_vs_human():
# print("\nHUMAN VS HUMAN")
	"""
	Play a Human vs Human game.
	"""
	player1 = input("Name of player 1: ")
	player2 = input("Name of player 2: ")
	

	first = input(f"Who starts ({player1}/{player2})? ")
	
	
def human_vs_computer():
	#print("\nHUMAN VS COMPUTER")
	"""
	Play Human vs Computer.
	"""
	human = input("Your name: ")
	
	
	first = input("Who starts ("+human+"/computer)? ").lower()
		
	

def main():
	"""
	Main function. Choisir le mode de jeu
	"""
	print("        GAME OF NIM")
	
	while True:
		print("\n1 - Human vs Human")
		print("2 - Human vs Computer")
		print("3 - Quit")
		
		choice = input("Choice: ")
		
		if choice == "1":
			human_vs_human()
		
		elif choice == "2":
			human_vs_computer()
		
		elif choice == "3":
			print("Goodbye!")
			break
		
		else:
			print("Invalid choice.")


if __name__ == "__main__":
	main()