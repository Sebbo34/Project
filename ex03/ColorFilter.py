# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ColorFilter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: seb <seb@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/14 22:31:34 by seb               #+#    #+#              #
#    Updated: 2024/06/14 23:33:55 by seb              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

class ColorFilter:
    def invert (self, array):
        matrice_rgb = image_array[:, :, :3]
        array_inver = 1 - matrice_rgb
        return array_inver
    
    def to_blue(self, array):
        array_B = image_array.copy()
        array_B[:,:,(0,1)] = 0
        return array_B
        
    def to_red(self, array):
          array_R = image_array.copy()
          array_R[:,:,(1,2)] = 0
          return array_R

    def to_green(self, array):
          array_G = image_array.copy()
          array_G[:,:,(0,2)] = 0
          return array_G


fltr = ColorFilter()
image = img.imread("elon.png")
image_array = np.array(image)


plt.imshow(fltr.to_red(image_array))
plt.show()

plt.imshow(fltr.to_green(image_array))
plt.show()

plt.imshow(fltr.to_blue(image_array))
plt.show()

alpha = matrice_rgba[:, :, 3]