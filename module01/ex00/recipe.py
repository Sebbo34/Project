# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 11:14:44 by sbo               #+#    #+#              #
#    Updated: 2024/06/11 18:54:30 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe :
	def __init__(self,name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		if (name and isinstance(name, str)) :
			self.name = name
		else :
			print("Error please enter a correct name")
			exit()
		if (cooking_lvl and isinstance(cooking_lvl, int) and cooking_lvl <= 5 and cooking_lvl >= 1):
			self.cooking_lvl = cooking_lvl
		else :
			print("Error please enter a correct cooking lvl")
			exit()
		if (cooking_time and isinstance(cooking_time, int) and cooking_time >= 0):
			self.cooking_time = cooking_time
		else :
			print("Error please enter a correct cooking time,")
			exit()
		if (ingredients and isinstance(ingredients, list)) :
			error = 0
			for i in ingredients :
				if (isinstance(i, str) == False) :
					error = 1
					break
			if error == 0 :
				self.ingredients = ingredients 
			else :
				print("Error please enter a correct list of ingredients")
				exit()
		else :
			print("Error please enter a correct list of ingredients")
			exit()
		if (isinstance(description, str)) :
			self.description = description
		else :
			print("Error please enter a correct  description")
			exit()
		if (recipe_type and isinstance(recipe_type, str) and (recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert")) :
			self.recipe_type = recipe_type
		else :
			print("Error please enter a correct recipe_type")
			exit()
	def debug(self):
		print (f"debug {self.name}")
	
	def __str__(self) :
		txt = f"{self.name} : \n{self.description} \nThis recipe is a level {self.cooking_lvl} and takes {self.cooking_time} min\nThis recipe is a {self.recipe_type} and you need {self.ingredients}"
		return txt
