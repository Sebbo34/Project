# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 14:21:15 by sbo               #+#    #+#              #
#    Updated: 2024/06/10 16:07:17 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

recipeSand = {"ingredients":["ham", "bread", "cheese", "tomato"], "meal":"lunch", "prep_time":10}
recipeCake = {"ingredients":["flour", "sugar", "eggs"], "meal":"dessert", "prep_time":60}
recipeSalad = {"ingredients":["avocado", "arugula", "tomatoes", "spinach"], "meal":"lunch", "prep_time":15}

cookbook = {"Sandwich":recipeSand, "Cake":recipeCake, "Salad":recipeSalad}

def print_cookbook(cookbook):
	for i in cookbook :
		print(i)

def print_recipe(cookbook, recipe):
	check = 0
	for i in cookbook :
		if i == recipe :
			check = 1
	if (check == 1):
		tmp = cookbook[recipe]
		print("Recipe for cake:")
		print("Ingredient list:", tmp["ingredients"])
		print("To be eaten for",tmp["meal"], end='.\n')
		print("Takes ",tmp["prep_time"] , "minutes for cooking.")
	else :
		print("This recipe is not in the cookbook")

def delete_recipe(cookbook, recipe):
	check = 0
	for i in cookbook :
		if i == recipe :
			check = 1
	if (check == 1):
		del cookbook[recipe]

def add_recipe(cookbook):
	while (1) :
		recipe = input(">> Enter a name\n")
		if recipe:
			break
	print ("Enter ingredients")
	lst = []
	while (1) :
		ing = input("")
		if (ing == ''):
			break
		lst.append(ing)
	while (1) :
		meal_type = input(">> Enter a meal type\n")
		if meal_type:
			break
	while (1) :
		prep_time = input(">> Enter a preparation time\n")
		if prep_time.isnumeric():
			break
	new_recipe = {"ingredients":lst, "meal":meal_type, "prep_time":prep_time}
	tmp = {recipe : new_recipe}
	cookbook.update(tmp)


print("Welcome to the Python Cookbook!")
print("\tList of available options:")
print("\t1: Add a recipe")
print("\t2: Delete a recipe")
print("\t3: Print a recipe")
print("\t4: Print the cookbook")
print("\t5: Quit")

while (1) :
	print("Please select an option")
	opt = input(">>")
	if (opt.isnumeric()):
		i = int (opt)
	else :
		i = 6
	if (i == 1):
		add_recipe(cookbook)
	elif (i == 2):
		tmp = input("Select a recipe to delete: ")
		if (tmp in cookbook):
			delete_recipe(cookbook, tmp)
		else:
			print ("This recipe is not in the cookbook")
	elif (i == 3):
		tmp = input("Please enter a recipe name to get its details:")
		if (tmp in cookbook):
			print_recipe(cookbook, tmp)
		else:
			print ("This recipe is not in the cookbook")
	elif (i == 4):
		print_cookbook(cookbook)
	elif (i == 5):
		print("Cookbook closed. Goodbye !")
		break
	else:
		print("Sorry, this option does not exist.")
		print("List of available options:")
		print("\t1: Add a recipe")
		print("\t2: Delete a recipe")
		print("\t3: Print a recipe")
		print("\t4: Print the cookbook")
		print("\t5: Quit")
