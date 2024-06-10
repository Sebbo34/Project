# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 17:41:57 by sbo               #+#    #+#              #
#    Updated: 2024/06/10 18:08:42 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randint

print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!""")

answer = randint(1, 99)
print (answer)
attempt = 0
while (1) :
	guess = input("What's your guess between 1 and 99?\n >>")
	if guess.isnumeric():
		n = int (guess)
		attempt = attempt + 1
		if (n > answer):
			print ("Too high!")
		elif (n < answer):
			print ("Too low!")
		else:
			if (answer == 42):
				print("The answer to the ultimate question of life, the universe and everything is 42.")
			if (attempt == 1):
				print ("Congratulations! You got it on your first try!")
			if (attempt != 1 and answer != 42):
				print (f"Congratulations, you've got it! \nYou won in {attempt} attempts!")
			break
			
	else :
		if (guess == "exit"):
			print ("exit")
			break
		print("That's not a number") 
