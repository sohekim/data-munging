import pandas as pandas
import xml.etree.cElementTree as et


file_name = 'vr_data_20191010T171504'
# loop through all xml files
tree=et.parse('./'+file_name+'.xml')
root=tree.getroot()

TimeStamp = []
PupilDiameter = []
LeftPupilDiameter = []
RightPupilDiameter = []

i = 1

for time in root.iter('GazeData'):
    t = time.attrib.get('TimeStamp')
    TimeStamp.append(t)

for pupil in root.iter('Pupil'):
    pd = pupil.attrib.get('PupilDiameter')
    PupilDiameter.append(pd)
    if (i % 2 == 0) :
        RightPupilDiameter.append(pd)
    else :
        LeftPupilDiameter.append(pd)
    i += 1

# print('time:')
# print(TimeStamp)
# print('pupil diameter')
# print(PupilDiameter)
# print('right:')
# print(RightPupilDiameter)
# print('left:')
# print(LeftPupilDiameter)

Pupil_df = pandas.DataFrame(
    list(zip(TimeStamp, LeftPupilDiameter, RightPupilDiameter)), 
    columns=['TimeStamp', 'Left_Pupil_Diameter', 'Right_Pupil_Diameter']
)

print(Pupil_df)

# csv file should match with the file input
Pupil_df.to_csv(file_name+ '.csv', index=False)