import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from operator import itemgetter

RATINGS = os.path.join(os.path.dirname(__file__), 'campaigns.csv')


class Campaigns(object):
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



    def get_After_Work(self):
        return self.movies['After_Work'].sum()

    def get_Fall_Break(self):
        return self.movies['Fall_Break'].sum()

    def get_LandingPage(self):
        return self.movies['LandingPage'].sum()

    def get_Mothers_Day(self):
        return self.movies['Mothers_Day'].sum()

    def get_Search_Boats(self):
        return self.movies['Search_Boats'].sum()
    def get_Search_Brand(self):
        return self.movies['Search_Brand'].sum()

    def get_Search_Kanal_dk(self):
        return self.movies['Search_Kanal_dk'].sum()

    def get_Search_kanal_En(self):
        return self.movies['Search_kanal_En'].sum()

    def get_Sunbeams(self):
        return self.movies['Sunbeams'].sum()
    def get_Suntop(self):
        return self.movies['Suntop'].sum()

    def get_Turist_Copenhagen(self):
        return self.movies['Turist_Copenhagen'].sum()



    def top_campaigns(self, n=10):
        grid = pd.DataFrame({
            'After_Work': self.get_After_Work(),
            'Fall_Break': self.get_Fall_Break(),
            'LandingPage': self.get_LandingPage(),
            'Mothers_Day': self.get_Mothers_Day(),
            'Search_Boats': self.get_Search_Boats(),
            'Search_Brand': self.get_Search_Brand(),
            'Search_Kanal_dk': self.get_Search_Kanal_dk(),
            'Search_kanal_En': self.get_Search_kanal_En(),
            'Sunbeams': self.get_Sunbeams(),
            'SunTop': self.get_Suntop(),
            'Turist_Copenhagen': self.get_Turist_Copenhagen(),})
        return grid.ix[grid['Sunbeams'].argsort()[:n]]


if __name__ == "__main__":
    ratings = Campaigns()
    print(ratings)
    print(ratings.top_campaigns())
