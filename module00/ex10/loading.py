# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbo <sbo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 18:21:55 by sbo               #+#    #+#              #
#    Updated: 2024/06/10 18:58:45 by sbo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import sleep
from time import time

from tqdm import tqdm

def ft_progress(lst):
	for i in tqdm(lst, bar_format=" ETA = {remaining_s:.2f}  {l_bar}{bar} {n_fmt}/{total_fmt} | elaspsed time {elapsed_s:.2f}s"):
		yield i

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
print()
print(ret)

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
	ret += elem
	sleep(0.005)
print()
print(ret)