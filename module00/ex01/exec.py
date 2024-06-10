# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:12:27 by sbo               #+#    #+#              #
#    Updated: 2024/06/10 17:11:41 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main(argv):
	i = 0
	len_array = len(sys.argv[1:])
	while (i < len_array):
		le = len(sys.argv[1:][i])
		while le > 0 :
			if (sys.argv[1:][i][le - 1] >= 'a' and sys.argv[1:][i][le - 1] <= 'z') :
				print(sys.argv[1:][i][le - 1].upper(), end='')
			elif (sys.argv[1:][i][le - 1] >= 'A' and sys.argv[1:][i][le - 1] >= 'Z') :
				print(sys.argv[1:][i][le - 1].lower(), end='')
			else :
				print(sys.argv[1:][i][le - 1], end='')
			le = le - 1
		i = i + 1
		if (i != len_array):
			print(end=' ')
	print(end='\n')

if __name__ == "__main__" and sys.argv[1:]:
	main(sys.argv[1:])