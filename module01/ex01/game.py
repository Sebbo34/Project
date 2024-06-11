# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 13:24:41 by sbo               #+#    #+#              #
#    Updated: 2024/06/11 13:40:41 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter :
	def __init__ (self, name):
		self.name = name
		self.is_alive = True

class Stark(GotCharacter):
	"""A class representing the Stark family. Or when bad things happen to good people."""
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"
	def print_house_words(self):
		print (self.house_words)
	def die(self):
		self.is_alive = False

arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
print(arya.is_alive)

arya.die()
print(arya.is_alive)
print(arya.__doc__)
