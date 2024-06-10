# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 16:56:53 by sbo               #+#    #+#              #
#    Updated: 2024/06/10 17:36:49 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main(argv):
	alphabet = dict(A='.-', B='-...', C='-.-.', D='-..', E='.', F='..-.', G='--.',
	                H='....', I='..', J='.---', K='-.-', L='.-..', M='--', N='-.',
	                O='---', P='.--.', Q='--.-', R='.-.', S='...', T='-', U='..-',
	                V='...-', W='.--', X='-..-', Y='-.--', Z='--..')
	alphabet.update({
	    '0': '-----', '1': '.----',
	    '2': '..---', '3': '...--',
	    '4': '....-', '5': '.....',
	    '6': '-....', '7': '--...',
	    '8': '---..', '9': '----.',
	})
	i = 0
	len_array = len(sys.argv[1:])
	lst = []
	while (i < len_array):
		l = len(sys.argv[1:][i])
		tmp = ''
		j = 0
		while  j < l :
			if (sys.argv[1:][i][j] >= 'a' and sys.argv[1:][i][j] <= 'z') :
				c = sys.argv[1:][i][j].upper()
			elif (sys.argv[1:][i][j] >= 'A' and sys.argv[1:][i][j] <= 'Z') :
				c = sys.argv[1:][i][j]
			elif (sys.argv[1:][i][j] >= '0' and sys.argv[1:][i][j] <= '9') :
				c = sys.argv[1:][i][j]
			elif (sys.argv[1:][i][j] == ' '):
				c = '/'
			else :
				print ("ERROR")
				exit()
			if (c == '/'):
				tmp = tmp + c
			else:
				tmp = tmp + alphabet[c]
			tmp = tmp + ' '
			j = j + 1
		i = i + 1
		lst.append(tmp)
	print(*lst)

if __name__ == "__main__" and sys.argv[1:]:
	main(sys.argv[1:])