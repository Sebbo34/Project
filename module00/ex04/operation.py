# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operation.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 13:16:05 by sbo               #+#    #+#              #
#    Updated: 2024/06/10 13:31:52 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys

def main(argv):
	i = 0
	len_array = len(sys.argv[1:])
	if (len_array != 2):
		print ("AssertionError: more than one argument are provided")
	elif ((sys.argv[1:][0].isnumeric() == True and sys.argv[1:][1].isnumeric() == True) or
		(sys.argv[1:][0][1:].isnumeric() == True and sys.argv[1:][0][0] == '-') and 
		(sys.argv[1:][1][1:].isnumeric() == True and sys.argv[1:][1][0] == '-') 
		or (sys.argv[1:][0][1:].isnumeric() == True and sys.argv[1:][0][0] == '-' and  sys.argv[1:][1].isnumeric() == True
		) or (sys.argv[1:][0].isnumeric() == True and (sys.argv[1:][0][1:].isnumeric() == True and sys.argv[1:][0][0] == '-')) ):
		i = int (sys.argv[1:][0])
		j = int (sys.argv[1:][1])
		print ("Sum:\t\t",i + j)
		print ("Difference:\t", i - j)
		print ("Product:\t",i * j)
		if (j != 0) :
			print ("Quotient:\t", i / j)
			print ("Remainer:\t", i % j)
		else :
			print ("Quotient:\t ERROR(division by zero)")
			print ("Remainer:\t ERROR(modulo by zero)")
	else :
		print("AssertionError: only integer")


if __name__ == "__main__" and sys.argv[1:]:
	main(sys.argv[1:])