import pandas as pd

file = pd.read_csv('Age.csv')

a= []
for i in range(0,290):
    max = 0
    if file.Age_Group_1[i] > max:
        max = 1

    if file.Age_Group_2[i] > max:
        max = 2

    if file.Age_Group_3[i] > max:
        max = 3

    if file.Age_Group_4[i] > max:
        max = 4

    if file.Age_Group_5[i] > max:
        max = 5

    if file.Age_Group_6[i] > max:
        max = 6

    a.append(max)

file['Age_range'] = a

file.to_csv('Age_bayesian.csv', index=False)

