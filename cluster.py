import random
import os, sys
import numpy as np
from tqdm import tqdm 
from matplotlib import pyplot as plt, animation




def create_mas(mas):
    mas = np.zeros((size, size))
    for k in occupied_list:
##        distance = ((k[0] - root[0]) ** 2 + (k[1] - root[1]) ** 2) ** 0.5
        mas[k[0]][k[1]] = 1
    mas[root[0]][root[1]] = 5
    return mas


def animate(i):
    sctr = plt.pcolormesh(results[i], cmap="binary", edgecolors='w', linewidth=1)
    filename = f'Итерация №{i + 1}\nd = {np.log(np.count_nonzero(results[i])) / np.log(1 / l)}'
    plt.title(filename)
    return sctr,


results = []
mcs_max = 150
size = 50
l = 1 / size


s = (random.randint(size // 2 - 1, size // 2), random.randint(size // 2 - 1, size // 2))
root = s
occupied_list = set()
occupied_list.add(s)
perimeter_list = [s]

mcs = 0
while mcs < mcs_max:
    s = random.choice(perimeter_list)
    rnd = random.randint(0, 3)        
    if rnd == 0:
        if s[1] - 1 < 0 or (s[0], s[1] - 1) in occupied_list:
            continue
        sn = (s[0], s[1] - 1)
    elif rnd == 1:
        if s[1] + 1 >= size or (s[0], s[1] + 1) in occupied_list:
            continue
        sn = (s[0], s[1] + 1)
    elif rnd == 2:
        if s[0] - 1 < 0 or (s[0] - 1, s[1]) in occupied_list:
            continue
        sn = (s[0] - 1, s[1])
    elif rnd == 3:
        if s[0] + 1 >= size or (s[0] + 1, s[1]) in occupied_list:
            continue
        sn = (s[0] + 1, s[1])

    occupied_list.add(sn)

    tmp = create_mas(occupied_list)
    results.append(tmp)

    
    perimeter_list = [(i, j) for i in range(size) for j in range(size) if tmp[i][j] != 0 and 0 in tmp[max(0, i-1):i+2, max(0, j-1):j+2]]
    mcs += 1
    

fig, ax = plt.subplots()
plt.style.use("ggplot")
plt.xlim(0, size)
plt.ylim(0, size)
plt.gca().invert_yaxis()
ax.set_aspect('equal')
##plt.pcolormesh(tmp, cmap="binary", edgecolors='w', linewidth=1)
##plt.show()


animation = animation.FuncAnimation(fig=fig,
                                    func=animate, 
                                    frames=tqdm(range(len(results)), ncols=100, initial=1, total=len(results)),
                                    interval=10,
                                    blit=True,
                                    repeat=True)
animation.save('моя анимация 2.gif', writer='pillow', fps=30)
