# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 11:53:18 by sbo               #+#    #+#              #
#    Updated: 2024/06/10 12:34:55 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def text_analyzer(string):
	"""
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text"""
	i = 0
	min = 0
	maj = 0
	space = 0
	punct = 0
	if (string and isinstance(string, str) == True):
		l = len(string)
		while (i < l):
			if (string[i] >= 'a' or string[i] >= 'z') :
				min = min + 1
			elif (string[i] >= 'A' or string[i] >= 'Z') :
				maj = maj + 1
			elif (string[i] == ' ') :
				space = space + 1
			elif (string[i] == '.' or string[i] == ',' or string[i] == '?' or string[i] == '!') :
				punct = punct + 1
			i = i + 1
		print("The text contains ", i," character(s)")
		print("-", maj,"upper letter(s)")
		print("-", min,"lower letter(s)")
		print("-", punct,"punctuation mark(s)")
		print("-", space,"space(s)")
	elif (string):
		print ("AssertionError: argument is not a string")
	else:
		print ("None Argument")

def main(argv):
	i = 0
	len_array = len(sys.argv[1:])
	if (len_array > 1):
		print ("AssertionError: more than one argument are provided")
	else :
		text_analyzer(sys.argv[1:][0])


if __name__ == "__main__" and sys.argv[1:]:
	main(sys.argv[1:])
	
