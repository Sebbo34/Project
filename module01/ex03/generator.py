# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 17:41:59 by sbo               #+#    #+#              #
#    Updated: 2024/06/11 19:00:55 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randint

def generator(var, sep, option = None):
	if (isinstance(var, str) and option in ["shuffle", "ordered", None, "unique"]):
		chaine = ""
		if (option == None):
			for i in var:
				if (i != sep):
					chaine = chaine + i
				if (i == sep and chaine):
					yield chaine
					chaine = ""
			if (chaine != ""):
				yield chaine
		lst = []
		if (option == "unique"):
			for i in var:
				if (i != sep):
					chaine = chaine + i
				if (i == sep and chaine):
					if (chaine not in lst):
						lst.append(chaine)
						yield chaine
					chaine = ""
			if (chaine not in lst and chaine != ""):
				yield chaine
		if (option == "ordered"):
			for i in var:
				if (i != sep):
					chaine = chaine + i
				if (i == sep and chaine):
					lst.append(chaine)
					chaine = ""
			if (chaine != ""):
				lst.append(chaine)
			lst.sort()
			for i in lst:
				yield i
		if (option == "shuffle"):
			for i in var:
				if (i != sep):
					chaine = chaine + i
				if (i == sep and chaine):
					lst.append(chaine)
					chaine = ""
			if (chaine != ""):
				lst.append(chaine)
			ind = []
			while (len(ind) != len(lst)):
				n = randint(0, len(lst) - 1)
				if (n not in ind):
					ind.append(n)
			for i in ind:
				yield lst[i]
			print (ind)
				
	else :
		print ("ERROR")

text = "Lorem Ipsum Lorem Ipsum"
var = " Je suis un test "
text1 = " n m "
print (len(text))
for i in generator(var, " "):
	print (i)
print ("--------------------------------------")
for word in generator(text, sep=" ", option="unique"):
	print(word)
print ("--------------------------------------")

for word in generator(text1, sep=" ", option="ordered"):
	print (word)
print ("--------------------------------------")

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="shuffle"):
	print(word)

