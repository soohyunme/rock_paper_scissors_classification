import random
import os

sample_path = 'static/cpu'
sample_file_list = os.listdir(sample_path)
sample_label_list = list(map(lambda x: x.split('.')[0], sample_file_list))
class_names = {'paper': 0, 'rock': 1, 'scissors': 2}

class_map = list(map(lambda x: class_names[x], sample_label_list))
result = {0: 'WIN', 1: 'LOSE', 2: 'DRAW'}


def checkWin(user):
    random_idx = random.randint(0, 2)
    com_path = sample_path + '/' + sample_file_list[random_idx]
    com = class_map[random_idx]
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

    return result[state], com_path, com

