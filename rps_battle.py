import random
import os

sample_path = 'static/cpu'
sample_list = os.listdir(sample_path)

class_names = {0: 'paper', 1: 'rock', 2: 'scissor'}
result = {0: 'WIN', 1: 'LOSE', 2: 'DRAW'}


def checkWin(user):
    cpu = random.randint(0, 2)
    cpu_path = sample_path + '/' + sample_list[cpu]

    if user == cpu:
        state = 2
    elif user == 2 and cpu == 1:
        state = 1
    elif user == 1 and cpu == 0:
        state = 1
    elif user == 0 and cpu == 2:
        state = 1
    else:
        state = 0

    return cpu, cpu_path, result[state]

