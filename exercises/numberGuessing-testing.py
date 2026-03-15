import random

def game():
	difficulties = {
		1: {
			"name": "Easy mode - 10 attempts",
			"max_attempts": 10,
			"max_number": 10
		},
		2: {
			"max_attempts": 8,
			"max_number": 50
		},
		3: {
			"name": "Hard mode - 6 attempts",
			"max_attempts": 6,
			"max_number": 100
		}
	}
	
	# difficulty choice and validation loop
	while True:
		try:
			choice = int(input("Choose a difficulty: 1 - Easy (1-10)  2 - Medium (1-50)  3 - Hard (1-100)"))
			config = difficulties[choice]
			break
		except ValueError:
			print("Error: Please enter a number.")
			continue
				
		except KeyError:
			print("Error: Choose one of the listed difficulty numbers.")
			continue
			
	print(config["name"])
	max_attempts = config["max_attempts"]
	secret_number = random.randint(1, config["max_number"])
	
	# guessing loop
	while max_attempts > 0:
		try:
			guess = int(input(f"Enter your guess (1-{config['max_number']}): "))
			if guess > config["max_number"]:
				print("Please enter number within range.")
				continue
			elif guess < 1:
				print("Please enter a valid number.")
				continue
		except ValueError:
			print("Error: Please enter a number.")
			continue
		
		max_attempts -= 1		
		if guess < secret_number:
			print(f"Too low! You have {max_attempts} attempts left.")
	
		elif guess > secret_number:
			print(f"Too high! You have {max_attempts} attempts left.")
	
		else:
			# this means the guessed number equals the secret number
			remaining_attempts = config["max_number"] - max_attempts
			print(f"Correct! You guessed it in {remaining_attempts} attempts.")
			break
	


if max_attempts == 0:
	print("Game over. No more attempts left.")
	print("Secret number was:", secret_number)

	# replay = str(input("Do you want to play again? (y/n):"))
	# if replay == "y":
	# 	print("Game will be replayed.")
	# elif replay == "n":
	# 	print("Thank you for playing.")