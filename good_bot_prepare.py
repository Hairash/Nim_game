a = 1000
b = 1000
c = 1000

max_val = max(a, b, c)

def show_positions():
    for x in range(a + 1):
        for y in range(b + 1):
            print(*positions[x][y])
        print()

# 'W' - win, 'L' - lose, 0 - unknown
positions =  [[[0] * (c + 1) for x in range(b + 1)] for y in range(a + 1)]
positions[0][0][0] = 'L'

for i in range(1, a + 1):
    positions[i][0][0] = 'W'
for i in range(1, b + 1):
    positions[0][i][0] = 'W'
for i in range(1, c + 1):
    positions[0][0][i] = 'W'
for i in range(1, min(a, b) + 1):
    positions[i][i][0] = 'L'
    for j in range(1, c + 1):
        positions[i][i][j] = 'W'
for i in range(1, min(b, c) + 1):
    positions[0][i][i] = 'L'
    for j in range(1, a + 1):
        positions[j][i][i] = 'W'
for i in range(1, min(a, c) + 1):
    positions[i][0][i] = 'L'
    for j in range(1, b + 1):
        positions[i][j][i] = 'W'

for x in range(1, a + 1):
    for y in range(1, b + 1):
        if x != y:
            positions[x][y][0] = 'W'
for x in range(1, a + 1):
    for z in range(1, c + 1):
        if x != z:
            positions[x][0][z] = 'W'
for y in range(1, b + 1):
    for z in range(1, c + 1):
        if z != y:
            positions[0][y][z] = 'W'



print('go')
show_positions()


def check_pos(a, b, c):
    if (a, b, c) in positions:
        return positions[(a, b, c)]
    
    ans = []
    for i in range(a - 1, -1, -1):
        ans.append([i, b, c])
    for i in range(b - 1, -1, -1):
        ans.append([a, i, c])
    for i in range(c - 1, -1, -1):
        ans.append([a, b, i])
##    print((a, b, c), ans)

    for x in ans:
        x.sort()
        x = tuple(x)
        if not check_pos(*x):
            positions[(a, b, c)] = True
            return True
    positions[(a, b, c)] = False
    return False


##def main():
##    from time import time
##    
##    start_time = time.now()
##    check_pos(200, 300, 400)
##    end_time = time.now()
##
##    print(end_time - start_time)
##
##main()
