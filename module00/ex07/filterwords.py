# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 16:07:51 by sbo               #+#    #+#              #
#    Updated: 2024/06/10 16:49:38 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main(argv):
	i = 0
	len_array = len(sys.argv[1:])
	if (len_array != 2):
		print("ERROR")
		exit()
	if (sys.argv[1:][1].isnumeric()  == False):
		print("ERROR")
		exit()
	N = int (sys.argv[1:][1])
	S = sys.argv[1:][0]
	lst = []
	l = len (S)
	i = 0
	cpt = 0
	tmp = ""
	while (i < l):
		if (S[i] == ' ' or S[i] == '\n' or S[i] == '\t'):
			lst += [tmp] if cpt > N else []
			tmp = ""
			cpt = 0
		if (S[i] not in " ,.?[]():;!-\"'\n\t" ):
			cpt = cpt + 1
			tmp = tmp + S[i]
		i = i + 1
	print (lst)


if __name__ == "__main__" and sys.argv[1:]:
	main(sys.argv[1:])
else:
	print("ERROR")