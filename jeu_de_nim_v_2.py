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


def computer_move(matches, human_move=None, computer_started=False):
	"""
    Calcule le coup de l'ordinateur en utilisant la stratégie optimale.

    :parameter
    matches : int (Nombre d'allumettes restantes)
    human_move : int, optionnel (Dernier coup joué par l'humain)
    computer_started : bool (True si l'ordinateur a commencé la partie)

  	:return int (Nombre d'allumettes retirées)
    """
	
	# Human started
	if not computer_started:
		move = 5 - human_move
	
	# Computer started
	else:
		# First move
		if matches == TOTAL_MATCHES:
			move = 1
		else:
			target = (matches - 1) % 5
			
			if target == 0:
				move = 1
			else:
				move = target
	
	move = max(1, min(move, 4))
	move = min(move, matches)
	
	print(f"Computer removes {move} match(es).")
	
	return move
	
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
	
	while True:
		first = input(f"Who starts ({human}/computer)? ").lower()
		
		if first in (f"{human}", "computer"):
			break
		
		print("Please enter 'human' or 'computer'.")
	
	matches = TOTAL_MATCHES
	human_starts = first == "human"
	
	if human_starts:
		turn = "human"
	else:
		turn = "computer"
	
	last_human_move = None
	
	while True:
		display_matches(matches)
		
		if turn == "human":
			
			move = get_player_move(human, matches)
			last_human_move = move
			
			matches -= move
			
			if matches == 0:
				print(f"\n{human} removed the last match.")
				print("You lose!")
				print("Computer wins!")
				break
			
			turn = "computer"
		
		else:
			
			move = computer_move(
				matches,
				last_human_move,
				computer_started=not human_starts
			)
			
			matches -= move
			
			if matches == 0:
				print("\nComputer removed the last match.")
				print("Computer loses!")
				print(f"{human} wins!")
				break
			
			turn = "human"
	

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