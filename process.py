import pandas as pandas
import xml.etree.cElementTree as et
import numpy as np

def createCSV(folder_name, left_avg, right_avg, left_std, right_std) :
    Pupil_df = pandas.DataFrame(
        list(zip(left_avg, right_avg, left_std, right_std)), 
        columns=['left_avg', 'right_avg', 'left_std', 'right_std']
    )
    Pupil_df.to_csv('./result/'+folder_name+ '.csv', index=False)


def addData (path, left_avg, right_avg, left_std, right_std) :
    tree=et.parse(path)
    root=tree.getroot()

    LeftPupilDiameter = []
    RightPupilDiameter = []

    i = 1

    for pupil in root.iter('Pupil'):
        pd = pupil.attrib.get('PupilDiameter')
        if (pd != 'NaN'):
            if (i % 2 == 0):
                RightPupilDiameter.append(float(pd))
            else:
                LeftPupilDiameter.append(float(pd)) 
        i += 1

    npRight = np.array(RightPupilDiameter)
    right_avg.append(np.average(npRight))
    right_std.append(np.std(npRight))

    npLeft = np.array(LeftPupilDiameter)
    left_avg.append(np.average(npLeft))
    left_std.append(np.std(npLeft))