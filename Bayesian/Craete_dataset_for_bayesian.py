import pandas as pd
import csv

file = pd.read_csv('weather.csv')
file2 = pd.read_csv('bayesian_dataset.csv')

with open('bayesian_dataset.csv', 'w') as myCsvFile:
    columns = ['Date', 'Parameters', 'Age_Group']
    writer = csv.DictWriter(myCsvFile, fieldnames=columns)
    for i in range(0, 290):

        if file.Age_Group_1[i] != 0:
            for j in range(0, int(file.Age_Group_1[i])):
                print(i)
                writer.writerow({'Date': file.Date[i], 'Parameters': file.Parameters[i], 'Age_Group': 1})

        if file.Age_Group_2[i] != 0:
            for j in range(0, int(file.Age_Group_2[i])):
                writer.writerow({'Date': file.Date[i], 'Parameters': file.Parameters[i], 'Age_Group': 2})

        if file.Age_Group_3[i] != 0:
            for j in range(0, int(file.Age_Group_3[i])):
                writer.writerow({'Date': file.Date[i], 'Parameters': file.Parameters[i], 'Age_Group': 3})

        if file.Age_Group_4[i] != 0:
            for j in range(0, int(file.Age_Group_4[i])):
                writer.writerow({'Date': file.Date[i], 'Parameters': file.Parameters[i], 'Age_Group': 4})

        if file.Age_Group_5[i] != 0:
            for j in range(0, int(file.Age_Group_5[i])):
                writer.writerow({'Date': file.Date[i], 'Parameters': file.Parameters[i], 'Age_Group': 5})

        if file.Age_Group_6[i] != 0:
            for j in range(0, int(file.Age_Group_6[i])):
                writer.writerow({'Date': file.Date[i], 'Parameters': file.Parameters[i], 'Age_Group': 6})

        # myCsvFile.to_csv("bayesian_dataset.csv",index=False)

# file2.to_csv("bayesian_dataset.csv",index=False)