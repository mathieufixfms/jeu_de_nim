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
TOTAL_MATCHES = 21
MIN_REMOVE = 1
MAX_REMOVE = 4

def get_player_move(player_name, matches):
	"""
	Demander à un joueur combien d'allumettes il souhaite retirer.

	:parameter
	player_name : str (Nom du joueur)
	matches : int (Nombre d'allumettes restantes)

	:return int (Nombre d'allumettes retirées)
	"""
	
	while True:
		try:
			move = int(
				input(f"{player_name}, remove between 1 and 4 matches: ")
			)
			
			if MIN_REMOVE <= move <= MAX_REMOVE and move <= matches:
				return move
			
			print("Invalid number.")
		
		except ValueError:
			print("Please enter an integer.")
			
def display_matches(matches):
	"""
	Affiche les allumettes restantes.

	Paramètres
	----------
	matches : int
		Nombre d'allumettes restantes.
	"""
	print("\nRemaining matches :", matches)
	print("| " * matches)
	print()

def human_vs_human():
	"""
	Play a Human vs Human game.
	"""
	player1 = input("Name of player 1: ")
	player2 = input("Name of player 2: ")
	
	while True:
		first = input(f"Who starts ({player1}/{player2})? ")
		
		if first == player1:
			current = player1
			other = player2
			break
		
		elif first == player2:
			current = player2
			other = player1
			break
		
		print("Unknown player.")
	
	matches = TOTAL_MATCHES
	
	while True:
		display_matches(matches)
		
		move = get_player_move(current, matches)
		
		matches -= move
		
		if matches == 0:
			print(f"\n{current} removed the last match.")
			print(f"{current} loses!")
			print(f"{other} wins!")
			break
		
		current, other = other, current


def human_vs_computer():
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