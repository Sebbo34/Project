# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 11:14:53 by sbo               #+#    #+#              #
#    Updated: 2024/06/11 13:17:11 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from recipe import Recipe
from datetime import datetime

class Book :

	def __str__(self) :
		txt = "test"
		return txt
	
	def __init__ (self, name):
		self.name = name
		self.creation_date = datetime.now()
		self.lastupdate = self.creation_date
		self.recipes_list = {"starter" : [], "lunch" : [], "dessert": []} 
	
	def get_recipe_by_name(self, name):
		for i in self.recipes_list.values() :
			if (i == name):
				print(i)
				return i
		print ("This recipe is not in this Book")

	def get_recipes_by_types(self, recipe_type):
		for i in self.recipes_list[recipe_type] :
			print (i.name)

	def add_recipe(self, recipe):
		if (isinstance(recipe, Recipe) == False):
			print (f"{recipe} is not in Recipe type")
			exit()
		if (recipe.recipe_type ==  "starter"):
			self.recipes_list["starter"].append(recipe)
		elif (recipe.recipe_type ==  "lunch"):
			self.recipes_list["lunch"].append(recipe)
		elif (recipe.recipe_type ==  "dessert"):
			self.recipes_list["dessert"].append(recipe)
		self.lastupdate = datetime.now