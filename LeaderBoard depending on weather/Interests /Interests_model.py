import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from operator import itemgetter

RATINGS = os.path.join(os.path.dirname(__file__), 'interests.csv')


class Interests(object):
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

    def get_News_Readers(self):
        return self.movies['News_Readers'].sum()

    def get_Beauty_Welness(self):
        return self.movies['Beauty_Welness'].sum()

    def get_Art_Theater(self):
        return self.movies['Art_Theater'].sum()

    def get_Business_Professionals(self):
        return self.movies['Business_Professionals'].sum()

    def get_Luxury_Shoppers(self):
        return self.movies['Luxury_Shoppers'].sum()

    def get_Books_lovers(self):
        return self.movies['Books_lovers'].sum()

    def get_Music_lovers(self):
        return self.movies['Music_lovers'].sum()

    def get_Shppers(self):
        return self.movies['Shppers'].sum()

    def get_Health_Fitness(self):
        return self.movies['Health_Fitness'].sum()

    def get_Travel_Buffs(self):
        return self.movies['Travel_Buffs'].sum()



    def top_Interests(self, n=10):
        grid = pd.DataFrame({
            'News_Readers': self.get_News_Readers(),
            'Beauty_Welness': self.get_Beauty_Welness(),
            'Art_Theater': self.get_Art_Theater(),
            'Business_Professionals': self.get_Business_Professionals(),
            'Luxury_Shoppers': self.get_Luxury_Shoppers(),
            'Books_lovers': self.get_Books_lovers(),
            'Music_lovers': self.get_Music_lovers(),
            'Shppers':self.get_Shppers(),
            'Health_Fitness': self.get_Health_Fitness(),
            'Travel_Buffs': self.get_Travel_Buffs(),


        })
        return grid.ix[grid['Travel_Buffs'].argsort()[:n]]


if __name__ == "__main__":
    ratings = Interests()
    print(ratings)
    print(ratings.top_Interests())
