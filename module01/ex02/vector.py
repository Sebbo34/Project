# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 14:35:06 by sbo               #+#    #+#              #
#    Updated: 2024/06/11 17:07:26 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector :


	def __init__(self,vect):
		if (isinstance(vect, list)):
			self.values = vect
			if (len(vect) == 1):
				self.shape =(1, len(vect[0]))
			else:
				self.shape =(len(vect), 1)
		elif (isinstance(vect, int)):
			lst = []
			for i in range (vect):
				lst.append([float(i)])
			self.values = lst	
			self.shape = (vect, 1)
		elif (isinstance(vect, tuple)):
			lst = []
			for i in range (vect[0], vect[1]):
				lst.append([float (i)])
			self.values = lst
			self.shape = (vect[1] - vect[0], 1)

	def __repr__(self):
		if (self.shape[0] < self.shape[1]):
			return f"{self.values}"
		else :
			txt = "[["
			for i in self.values:
				txt = txt + str (i[0])
				if ( i != self.values[len(self.values) - 1]):
					txt = txt + ", "
			txt= txt + "]]"
			return txt
		

	def __str__(self):
		if (self.shape[0] < self.shape[1]):
			return f"{self.values}"
		else :
			txt = "[["
			for i in self.values:
				txt = txt + str (i[0])
				if ( i != self.values[len(self.values) - 1]):
					txt = txt + ", "
			txt= txt + "]]"
			return txt

	def __add__(self, other):
		if isinstance(other, Vector):
			if (self.shape != other.shape):
				print ("Error + need 2 vector with same shape")
				exit()
			else:
				if (self.shape[0] < self.shape[1]):
					lst = [[]]
					for i,j in zip (self.values[0], other.values[0]):
						tmp = i + j
						lst[0].append(tmp)
				else :
					lst = []
					for i,j in zip (self.values, other.values):
						tmp = i[0] + j[0]
						lst.append([tmp])
				return Vector(lst)
		else:
			raise TypeError("unsupported operand type for +")

	def __radd__(self, other):
		return self.__add__(other)




	def __mul__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			if (self.shape[0] < self.shape[1]):
				lst = [[]]
				for i in self.values[0]:
					tmp = i * other
					lst[0].append(tmp)
			else :
				lst = []
				for i in self.values:
					tmp = i[0] * other
					lst.append([tmp])
			return Vector(lst)
		else:
			raise TypeError("unsupported operand type for *")
		

	def __rmul__(self, other):
		return self.__mul__(other)


	def __truediv__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			if (self.shape[0] < self.shape[1]):
				lst = [[]]
				for i in self.values[0]:
					tmp = i / other
					lst[0].append(tmp)
			else :
				lst = []
				for i in self.values:
					tmp = i[0] / other
					lst.append([tmp])
			return Vector(lst)
		else:
			raise TypeError("unsupported operand type for /")
		

	def __rtruediv__(self, other):
		raise TypeError("Division of a scalar by a Vector is not defined here.")




	def __sub__(self, other):
		if isinstance(other, Vector):
			if (self.shape != other.shape):
				print ("Error + need 2 vector with same shape")
				exit()
			else:
				if (self.shape[0] < self.shape[1]):
					lst = [[]]
					for i,j in zip (self.values[0], other.values[0]):
						tmp = i - j
						lst[0].append(tmp)
				else :
					lst = []
					for i,j in zip (self.values, other.values):
						tmp = i[0] - j[0]
						lst.append([tmp])
				print (lst)
				return Vector(lst)
		else:
			raise TypeError("unsupported operand type for +")

	def __rsub__(self, other):
		return self.__sub__(other)


	def dot(self, v2):
		if (isinstance(v2, Vector) == False):
			print ("Error dot need 2 vector")
			exit()
		if (self.shape != v2.shape):
			print ("Error dot need 2 vector with same shape")
			exit()
		s = 0
		if (self.shape[0] < self.shape[1]):
			for i,j in zip (self.values[0], v2.values[0]):
				s = s + i * j
		else :
			for i,j in zip (self.values, v2.values):
				s = s + i[0] * j[0]
		return s

	def T(self):
		if (self.shape[0] < self.shape[1]):
			lst = []
			for i in self.values[0]:
				lst.append([i])
		else :
			lst = [[]]
			for i in self.values:
				lst[0].append(i[0])
		vect = Vector(lst)
		return vect

