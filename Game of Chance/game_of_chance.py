import random

money = 100

#Menu Function
def menu():
	print("1. Flip a Coin!")
	print("2. Cho-Han!")
	print("3. Card Drawing!")
	print(". Exit")
	print("You have $" + str(money))

#Coin Toss Function
def flip_coin():
	print("Welcome to coin flip!")
	bet = int(input("How much would you like to bet? "))

	if money <= 0:
		print("Sorry, you are out of money")
		return 0

	while bet <= 0 or bet > money:
		bet = int(input("Sorry, that is an invalid bet. Try again! "))
		

	player_guess = int(input("Awesome, would you like to bet heads or tails? Enter 1 for heads and 2 for tails: "))

	while player_guess < 1 or player_guess > 2:
		player_guess = int(input("Sorry, invalid guess. Try again! "))


	coin_toss = random.randint(1, 2)

	if coin_toss == 1:
		if player_guess == 1:
			print("Awesome! It's heads! You win!")
			return bet * 2
		else:
			print("Sorry, it's heads! You lost!")
			return 0 - bet

	if coin_toss == 2:
		if player_guess == 2:
			print("Awesome! It's tails! You Win!")
			return bet * 2
		else:
			print("Sorry, it's tails! You lost!")
			return 0 - bet

#Cho-Han Function
def cho_han():
	print("Welcome to Cho-Han!")
	bet = int(input("How much would you like to bet? "))

	if money <= 0:
		print("Sorry, you are out of money")
		return 0

	while bet <= 0 or bet > money:
		bet = int(input("Sorry, that is an invalid bet. Try again! "))

	die_1 = random.randint(1, 6)
	die_2 = random.randint(1, 6)
	dice_sum = die_1 + die_2

	player_guess = int(input("Would you like to bet that the sum of the dice is odd or even? Enter 1 for odd and 2 for even: "))

	while player_guess < 1 or player_guess > 2:
		player_guess = int(input("Sorry, invalid guess. Try again! "))

	print("Die one rolled: " + str(die_1))
	print("Die two rolled: " + str(die_2))
	print("The sum of the dice is: " + str(dice_sum))

	if dice_sum % 2 != 0:
		if player_guess == 1:
			print("Awesome! The sum is odd! You win!")
			return bet * 2
		else:
			print("Sorry, the sum is odd! You lose!")
			return 0 - bet

	if dice_sum % 2 == 0:
		if player_guess == 2:
			print("Awesome! The sum is even! You win!")
			return bet * 2
		else:
			print("Sorry, the sum is even! You lose!")
			return 0 - bet

#Card Drawing Function
def cards():
	print("Welcome to the card drawing game! The player with highest numbered card wins!")
	bet = int(input("How much would you like to bet? "))

	if money <= 0:
		print("Sorry, you are out of money")
		return 0

	while bet <= 0 or bet > money:
		bet = int(input("Sorry, that is an invalid bet. Try again! "))

	input("Are you ready to draw your card? (Press ENTER to continue...)")

	player_card_suit_generator = random.randint(1, 4) 
	player_card_number_generator = random.randint(1, 13)
	player_card_suit = ""
	player_card_number = ""

	if (player_card_suit_generator == 1):
		player_card_suit = "Spades"
	elif (player_card_suit_generator == 2):
		player_card_suit = "Hearts"
	elif (player_card_suit_generator == 3):
		player_card_suit = "Diamonds"
	else:
		player_card_suit = "Clubs"

	computer_card_suit_generator = random.randint(1, 4) 
	computer_card_number_generator = random.randint(1, 13)
	computer_card_suit = ""
	computer_card_number = ""
	player_wins = 0

	if (computer_card_suit_generator == 1):
		computer_card_suit = "Spades"
	elif (computer_card_suit_generator == 2):
		computer_card_suit = "Hearts"
	elif (computer_card_suit_generator == 3):
		computer_card_suit = "Diamonds"
	else:
		computer_card_suit = "Clubs"

	while (player_card_suit == computer_card_suit and player_card_number == computer_card_number):
		computer_card_number = random.randint(1, 13)

	if (player_card_number_generator == 1):
		player_card_number = "Ace"
	elif (player_card_number_generator == 11):
		player_card_number = "Jack"
	elif (player_card_number_generator == 12):
		player_card_number = "Queen"
	elif (player_card_number_generator == 13):
		player_card_number = "King"
	else:
		player_card_number = str(player_card_number_generator)

	if (computer_card_number_generator == 1):
		computer_card_number = "Ace"
	elif (computer_card_number_generator == 11):
		computer_card_number = "Jack"
	elif (computer_card_number_generator == 12):
		computer_card_number = "Queen"
	elif (computer_card_number_generator == 13):
		computer_card_number = "King"
	else:
		computer_card_number = str(computer_card_number_generator) 

	if (player_card_number_generator == 1 and computer_card_number_generator > 1):
		player_wins = 1
	elif (computer_card_number_generator == 1 and player_card_number_generator > 1):
		player_wins = 2
	elif (player_card_number_generator > computer_card_number_generator):
		player_wins = 1
	elif (player_card_number_generator < computer_card_number_generator):
		player_wins = 2
	else:
		player_wins = 0

	print("You drew a " + player_card_number + " of " + player_card_suit + "!")
	print("The computer drew a " + computer_card_number + " of " + computer_card_suit + "!")

	if (player_wins == 1):
		print("You drew higher! You win!")
		return bet * 2
	elif (player_wins == 2):
		print("Sorry, you drew lower! You lose!")
		return 0 - bet
	else:
		print("It's a draw! Your bet has been refunded!")
		return 0


print("Welcome to Games of Chance!")
print("Select your game!")
menu()


while (menu_input != 4):
	menu()
	if (menu_input == 1):
		money += flip_coin()
	elif (menu_input == 2):
		money += cho_han()
	elif (menu_input == 3):
		money += cards()
	else:
		print("Invalid Selection! Please try again!")


