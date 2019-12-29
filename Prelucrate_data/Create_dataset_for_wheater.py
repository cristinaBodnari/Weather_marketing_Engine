import pandas as pd
import csv


def replace_to_comma(data):
    text = open(data, "r")
    text = ''.join([i for i in text]) \
        .replace(";", ",")
    x = open(data, "w")
    x.writelines(text)
    x.close()


def combined(filename1, filename2):
    replace_to_comma(filename1)
    replace_to_comma(filename2)

    file1 = pd.read_csv(filename1)
    file2 = pd.read_csv(filename2)

    file = pd.concat([file1, file2], sort=False)
    file.to_csv("Weather_tempreatures_2017.csv", index=False)


# combined("data/Analytics All Web Site Data Al trafik 20190101-20191127.csv", "data/Analytics All Web Site Data Google Ads-budjusteringer 20190101-20191127.csv")

def combined_temperatures_rain(filename1, filename2):
    file1 = pd.read_csv(filename1)
    file2 = pd.read_csv(filename2)

    a = []

    for rainfall in file1.Rainfall:
        a.append(rainfall)

    file2['Rainfall'] = a
    file2.to_csv("Weather_2017.csv", index=False)


# combined_temperatures_rain("Weather_rain_2017.csv", "Weather_tempreatures_2017.csv")

def combined_google_analytics(filename1, filename2):
    file1 = pd.read_csv(filename1)
    file2 = pd.read_csv(filename2)

    file2.drop(["Low", "High"], axis=1, inplace=True)

    a = []
    for temperature in file2.Medium:
        a.append(temperature)

    b = []
    for rainfall in file2.Rainfall:
        b.append(rainfall)

    file1['Medium'] = a
    file1['Rainfall'] = b

    file1.to_csv("Dataset.csv", index=False)


def min_medium_max(filename):
    file = pd.read_csv(filename)
    a = []

    for i in range(0, 291):
        if file.Rainfall[i] <= 2:
            a.append("Low")

        if file.Rainfall[i] >= 2 and file.Rainfall[i] <= 4:
            a.append("Medium")

        if file.Rainfall[i] > 4:
            a.append("High")

    file.Rainfall=a
    file.to_csv("a.csv", index=False)


def combine_tempreature_with_Rainfall(filename):
    file = pd.read_csv(filename)

    b = []
    for i in range(0, 292):
        parameters = str(file.Temperature[i]) + ", " + file.Rainfall[i]
        b.append(parameters)

    file.Rainfall = b
    file.to_csv("a.csv")

file = pd.read_csv("a.csv")


data = file.drop(columns="Temperature", inplace = True)


data.to_csv("a.csv", index=False)



# combined_google_analytics("Analytics_data.csv", "Weather_2019.csv")
# combine_tempreature_with_Rainfall("Dataset.csv")
