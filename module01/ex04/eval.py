# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 19:11:10 by sbo               #+#    #+#              #
#    Updated: 2024/06/11 19:34:09 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Evaluator :
	@staticmethod
	def zip_evaluate(words, coefs):
		s = 0
		if (len(words) != len(coefs)):
			return -1
		if (isinstance(words[0], str) and isinstance(coefs[0], float)):
			for i,j in zip(words, coefs):
				s = s + len(i) * j
		elif (isinstance(words[0], float) and isinstance(coefs[0], str)):
			for i,j in zip(coefs, words):
				s = s + len(i) * j
		return s

	@staticmethod
	def enumerate_evaluate(words, coefs):
		s = 0
		if (len(words) != len(coefs)):
			return -1
		if (isinstance(words[0], str) and isinstance(coefs[0], float)):
			for i,j in enumerate(words):
				s = s + len(j) * coefs[i]
		elif (isinstance(words[0], float) and isinstance(coefs[0], str)):
			for i,j in enumerate(coefs):
				s = s + len(j) * words[i]
		return s
	
words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 747.0, 0.5]
print (Evaluator.enumerate_evaluate( coefs, words))