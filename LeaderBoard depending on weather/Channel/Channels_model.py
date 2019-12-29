import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from operator import itemgetter

RATINGS = os.path.join(os.path.dirname(__file__), 'Channels.csv')


class Channels(object):
    def __init__(self, path=RATINGS):
        self.path = path
        self.load()

    def load(self):
        self.data = pd.read_csv(self.path)


    @property
    def movies(self):
        """
        Returns the data grouped by Movie
        """
        return self.data.groupby('Parameters')



    def get_Direct(self):
        return self.movies['Direct'].sum()

    def get_Email(self):
        return self.movies['Email'].sum()

    def get_Organic_Search(self):
        return self.movies['Organic_Search'].sum()

    def get_Referral(self):
        return self.movies['Referral'].sum()

    def get_Social(self):
        return self.movies['Social'].sum()

    def get_Paid_search(self):
        return self.movies['Paid_search'].sum()





    def top_Channels(self, n=10):
        grid = pd.DataFrame({
            'Direct': self.get_Direct(),
            'Email': self.get_Email(),
            'Organic Search': self.get_Organic_Search(),
            'Referral': self.get_Referral(),
            'Social':self.get_Social(),
            'Paid Search': self.get_Paid_search()})
        return grid.ix[grid['Direct'].argsort()[:n]]


if __name__ == "__main__":
    ratings = Channels()
    print(ratings)
    print(ratings.top_Channels())