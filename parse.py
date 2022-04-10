import os
from process import *

path = './EyeTrackingData'

for i in os.scandir(path):
    # one participant
    if i.is_dir():
        print('Participant: ' + i.path)
        left_avg = []
        right_avg = []
        left_std = []
        right_std = []
        for k in os.scandir(i.path):
            if not k.name.startswith('.'): 
                addData(k.path, left_avg, right_avg, left_std, right_std)
        createCSV(i.name, left_avg, right_avg, left_std, right_std)