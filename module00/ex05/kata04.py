# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 14:05:46 by sbo               #+#    #+#              #
#    Updated: 2024/06/10 14:14:06 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (0, 4, 132.42222, 10000, 12345.67)

print(f"module_0{kata[0]}, ex_0{kata[1]} : {format(kata[2],'.2f')}, {format(kata[3],'.2e')}, {format(kata[4],'.2e')}",end = "\n")