import os
import pandas as pd

RATINGS = os.path.join(os.path.dirname(__file__), 'Language.csv')


class Languages(object):
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

    def get_Danish(self):
        return self.movies['Danish'].sum()

    def get_English_US(self):
        return self.movies['English_US'].sum()

    def get_English_GB(self):
        return self.movies['English_GB'].sum()

    def top_Languages(self, n=10):
        grid = pd.DataFrame({
            'Danish': self.get_Danish(),
            'English GB': self.get_English_GB(),
            'English US': self.get_English_US()})
        return grid.ix[grid['Danish'].argsort()[:n]]


if __name__ == "__main__":
    ratings = Languages()
    print(ratings)
    print(ratings.top_Languages())
