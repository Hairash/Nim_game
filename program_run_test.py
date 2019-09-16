## TODO:
## . Check the good algorhithm
## . Tournament mode
## + Anti cheat
## + Kill process after time limit

import subprocess
import time

start_bot1 = 'run_nim.bat'
start_bot2 = 'GameAI.bat'
time_limit = 1
bot1 = start_bot1
bot2 = start_bot2
cur_bot = -1
cur_pos = [0, 0, 0]

game_positions = [
    [0, 0, 1, 2],
    [0, 1, 0, 2],
    [1, 0, 0, 2],
    [1, 1, 1, 4],
    [1, 2, 3, 6],
    [3, 4, 5, 10],
    [7, 8, 9, 10],
    [10, 10, 10, 10],
    [30, 10, 20, 10]
    ]


def wait_timeout(proc, seconds): # returns True on error
    """Wait for a process to finish, or raise exception after timeout"""
    start = time.time()
    end = start + seconds
    interval = min(seconds / 1000.0, .25)

    while True:
        result = proc.poll()
        if result is not None:
            return False
        if time.time() >= end:
            proc.terminate()
            print('\nTime limit! Bot', show_cur_bot(count_cur_bot(cur_bot)))
            return True
        time.sleep(interval)


def show_cur_bot(cur_bot):
    if cur_bot == 1:
        return(bot1)
    else:
        return(bot2)


def count_cur_bot(cur_bot):
    return (cur_bot + 1) % 2 + 1


def print_error(cur_bot):
    print('Error! Bot', show_cur_bot(count_cur_bot(cur_bot)))
    

def file_operations(): # returns error (True - error, False - ok)
    with open('result.txt', 'r') as res_file:
        res = list(map(int, res_file.readline().split()))
    print('Bot', count_cur_bot(cur_bot), 'turn:', res)

    idx = res[0] - 1
    if not 0 <= idx <= 2:
        print_error(cur_bot)
        return True
    val = res[1]
    if not 1 <= val <= cur_pos[idx]:
        print_error(cur_bot)
        return True
    cur_pos[idx] -= val
    print('Position:', cur_pos, end = ' ')

    with open('position.txt', 'w') as pos_file:
        pos_file.write(' '.join([str(x) for x in cur_pos]))
    return False


def pos_1_game(pos, bot_order):
    global cur_bot
    cur_bot = 0
    global cur_pos
    cur_pos = pos.copy()
    global bot1, bot2
    # order = 0 - norm order, order = 1 - reversed order
    if bot_order == 0:
        bot1 = start_bot1
        bot2 = start_bot2
    else:
        bot1 = start_bot2
        bot2 = start_bot1
    print('Bot1:', bot1)
    print('Bot2:', bot2)

##    with open('position.txt') as pos_file:
##        cur_pos = list(map(int, pos_file.readline().split()))
    with open('position.txt', 'w') as pos_file:
        pos_file.write(' '.join([str(x) for x in cur_pos]))
    print('Position:', cur_pos, end = ' ')

    while cur_pos != [0, 0, 0]:
        cur_bot = (cur_bot + 1) % 2
        process = subprocess.Popen(bot1, shell = False)
        if wait_timeout(process, time_limit):
            cur_bot = (cur_bot + 1) % 2
            break
        if file_operations():
            cur_bot = (cur_bot + 1) % 2
            break
        if cur_pos != [0, 0, 0]:
            cur_bot = (cur_bot + 1) % 2
            process = subprocess.Popen(bot2, shell = False)
            if wait_timeout(process, time_limit):
                cur_bot = (cur_bot + 1) % 2
                break
            if file_operations():
                cur_bot = (cur_bot + 1) % 2
                break
        
    print('\nBot', show_cur_bot(count_cur_bot(cur_bot)), 'wins')


def pos_tournament(pos, n_games):
    for i in range(n_games):
        pos_1_game(pos, i % 2)
        input()
    

def game_tournament():
    for game_pos in game_positions:
        pos = game_pos[:3]
        n = game_pos[-1]
        print('--------------------------------------------')
        print('Game', pos, 'started. Number of rounds:', n)
        pos_tournament(pos, n)
    










