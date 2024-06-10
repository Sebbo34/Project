# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 11:17:21 by sbo               #+#    #+#              #
#    Updated: 2024/06/10 11:49:16 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys

def main(argv):
	i = 0
	len_array = len(sys.argv[1:])
	if (len_array > 1):
		print ("AssertionError: more than one argument are provided")
	elif (sys.argv[1:][0].isnumeric() == True):
		i = int (sys.argv[1:][0])
		if (i == 0) :
			print ("I'm Zero.")
		elif  i % 2 == 0 :
			print ("I'm Even.")
		elif i % 2 == 1 :
			print ("I'm Odd.")
	elif (sys.argv[1:][0][1:].isnumeric() == True and sys.argv[1:][0][0] == '-'):
		i = int (sys.argv[1:][0])
		if (i == 0) :
			print ("I'm Zero.")
		elif  i % 2 == 0 :
			print ("I'm Even.")
		elif i % 2 == 1 :
			print ("I'm Odd.")
	else :
		print("AssertionError: argument is not an integer")


if __name__ == "__main__" and sys.argv[1:]:
	main(sys.argv[1:])