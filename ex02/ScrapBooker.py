# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ScrapBooker.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: seb <seb@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/14 13:10:45 by seb               #+#    #+#              #
#    Updated: 2024/06/14 20:52:50 by seb              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class ScrapBooker:
	def crop(self, array, dim, position = (0,0)):
		if (array.shape[0] >= position[0] + dim[0] and array.shape[1] >= position[1] + dim[1]):
			new_array = array[position[0]:position[0] + dim[0], position[1]:position[1] + dim[1]]
			return new_array
		else :
			return None
	def thin(self, array, n, axis):
		new_array = array
		if (axis == 0):
			for i in range (array.shape[0] -1, -1, -1):
				if ((i + 1) % n == 0):
					new_array = np.delete(new_array, i, axis)
		if (axis == 1):
			for i in range (array.shape[1] -1, -1, -1):
				if ((i + 1) % n == 0):
					new_array = np.delete(new_array, i, axis)
		return new_array

	def juxtapose(self, array, n, axis):
		new_array = array
		if (axis == 0):
			for i in range (n - 1):
				new_array = np.vstack((new_array, array))
		if (axis == 1):
			for i in range (n - 1):
				new_array = np.hstack((new_array, array))
		return new_array

	def mosaic(self, array,dim):
		if (dim[0] == 0 or dim[1] == 0):
			return None
		mosaic = self.juxtapose(array, dim[0], 0)
		mosaic = self.juxtapose(mosaic, dim[1],1)
		return mosaic	
spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5) 
arr1 = spb.crop(arr1, (5,5),(0,0))
#print (arr1)
#print (np.arange(0,25).reshape(5,5))
arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
arr2 = spb.thin(arr2,3,0)
print (arr2)

arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 9]]) 
print (spb.mosaic(arr3, (3, 2)))


