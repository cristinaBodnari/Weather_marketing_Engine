import pandas as pd
import datetime

# file = pd.read_csv("dates.csv")
# file1 = pd.read_csv("35-44.csv")
# file2 = pd.read_csv("a.csv")
# file3 = pd.read_csv("dataset.csv")
# data = file.drop(columns="High")


def change_data(file):
    # change date format
    a = []
    for i in range(0, 297):
        date = datetime.datetime.strptime(file.Date[i], '%m.%d.%y').strftime('%d.%m.%y')
        a.append(date)

    file.Date = a

    file.to_csv("dates.csv", index=False)


def reform_file(file1,file):
    # Add the Session to new dates file
    for i in range(0, 236):
        for j in range(0, 297):
            if file1.Date[i] == file.Date[j]:
                file.Sessions[j] = file1.Sessions[i]
                break

    print(file)
    file.to_csv("35-44.csv", index=False)


def test(file1):
    # Test
    k = 0
    for i in range(0, 297):
        if file1.Sessions[i] != 0:
            k += 1
            print(file1.Sessions[i])

    print(k)


# Combine data
def combination(filename1, filename2):
    # load the different files in the Dataframe
    filee1 = pd.read_csv(filename1)
    filee2 = pd.read_csv(filename2)

    # combine the two files into one
    # also save the Dataframe as a CSV file
    result = pd.merge(filee1, filee2, on='Date')

    result.to_csv('campaigns.csv', index=False)


# combination('After Work.csv', 'Fall Break 2019.csv')




