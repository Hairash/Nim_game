a = 3
b = 4
c = 5

max_val = max(a, b, c)

positions = dict() # True - win pos, False - lose
positions[(0, 0, 0)] = False


def show_positions(positions):
    for x in positions:
        print(x, positions[x])


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


def main():
    from time import time
    
    start_time = time.now()
    check_pos(200, 300, 400)
    end_time = time.now()

    print(end_time - start_time)

main()
