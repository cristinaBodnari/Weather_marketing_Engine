import pandas as pd






def combination(filename1, filename2):
    # load the different files in the Dataframe
    file1 = pd.read_csv(filename1)
    file2 = pd.read_csv(filename2)

    # combine the two files into one
    # also save the Dataframe as a CSV file
    result = pd.merge(file1, file2, on='Date')


    result.to_csv('weather.csv',index=False)


combination( 'weather.csv', 'dda.csv')


