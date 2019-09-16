import random

print('bot1')

with open('position.txt') as pos_file:
    cur_pos = list(map(int, pos_file.readline().split()))

idx = int(random.random() * 3)
while cur_pos[idx] == 0:
    idx = int(random.random() * 3)

num = cur_pos[idx]
d_num = int(random.random() * num) + 1

with open('result.txt', 'w') as res_file:
    res_file.write(str(idx + 1) + ' ' + str(d_num))
##res_file.close()

##input()
