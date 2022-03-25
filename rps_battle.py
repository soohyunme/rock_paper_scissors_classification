import random
import os

sample_path = 'static/cpu'
sample_list = os.listdir(sample_path)

class_names = {0: 'paper', 1: 'rock', 2: 'scissor'}
result = {0: 'WIN', 1: 'LOSE', 2: 'DRAW'}


def checkWin(user):
    com = random.randint(0, 2)
    com_path = sample_path + '/' + sample_list[com]
    print(com, com_path)
    com_list = [com, com_path]
    if user == com:
        state = 2
    elif user == 2 and com == 1:
        state = 1
    elif user == 1 and com == 0:
        state = 1
    elif user == 0 and com == 2:
        state = 1
    else:
        state = 0

    return com, com_path, result[state], com_list

