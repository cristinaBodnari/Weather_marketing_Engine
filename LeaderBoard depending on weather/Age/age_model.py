import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from operator import itemgetter

RATINGS = os.path.join(os.path.dirname(__file__), 'age.csv')


class Age(object):
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

    def get_Age_Group_1(self):
        return self.movies['Age_Group_1'].sum()

    def get_Age_Group_2(self):
        return self.movies['Age_Group_2'].sum()

    def get_Age_Group_3(self):
        return self.movies['Age_Group_3'].sum()

    def get_Age_Group_4(self):
        return self.movies['Age_Group_4'].sum()

    def get_Age_Group_5(self):
        return self.movies['Age_Group_5'].sum()

    def get_Age_Group_6(self):
        return self.movies['Age_Group_6'].sum()

    def top_Age(self, n=10):
        grid = pd.DataFrame({
            'Age_Group_1': self.get_Age_Group_1(),
            'Age_Group_2': self.get_Age_Group_2(),
            'Age_Group_3': self.get_Age_Group_3(),
            'Age_Group_4': self.get_Age_Group_4(),
            'Age_Group_5': self.get_Age_Group_5(),
            'Age_Group_6': self.get_Age_Group_6()

        })
        return grid.ix[grid['Age_Group_5'].argsort()[:n]]


if __name__ == "__main__":
    ratings = Age()
    print(ratings)
    print(ratings.top_Age())
