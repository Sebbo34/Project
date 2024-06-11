# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 11:14:38 by sbo               #+#    #+#              #
#    Updated: 2024/06/11 18:53:59 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from recipe import Recipe
from book import Book

tourte = Recipe("tourte", 2, 1, ["test", 'test'],"This a test", "starter")
test2 = Recipe("Test1", 2, 1, ["test", 'test'],"This a test", "lunch")
test3 = Recipe("Test2", 2, 1, ["test", 'test'],"This a test", "dessert")
test4 = Recipe("Test3", 2, 1, ["test", 'test'],"This a test", "starter")

print (tourte.__str__())
print (tourte)
to_print = str(tourte)
print (to_print)
""" book = Book("Livre")

book.add_recipe(tourte)
book.add_recipe(test2)
book.get_recipe_by_name("tourte")
book.add_recipe(test3)
book.add_recipe(test4)
book.get_recipes_by_types("starter")
print ("===")
book.get_recipes_by_types("lunch")
print ("25252")
book.get_recipes_by_types("dessert")
print ("48484")
for i in book.recipes_list["dessert"]:
	print (i) """