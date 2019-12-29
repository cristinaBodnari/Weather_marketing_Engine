import os

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


PATH = os.path.join(os.path.dirname(__file__), 'Age_bayesian.csv')


PRIOR = [2, 2, 2, 2, 2]


class Age(object):

    def __init__(self, path=PATH, m=3.75, c=1):
        self.path = path
        self.prior = m
        self.confidence = c
        self.load()

    def bayesian_mean(self, arr):
        if not self.prior or not self.confidence:
            raise TypeError("Bayesian mean must be computed with m and C")
        return ((self.confidence * self.prior + arr.sum()) /
                (self.confidence + arr.count()))

    def load(self):
        self.data = pd.read_csv(self.path)

    def __str__(self):
        return str(self.data.head())


    @property
    def Age_Range(self):
        """
        Returns the data grouped by
        """
        return self.data.groupby('Parameters')

    def get_means(self):
        return self.Age_Range['Age_range'].mean()

    def get_counts(self):
        return self.Age_Range['Age_range'].count()



    def plot_mean_frequency(self):
        grid = pd.DataFrame({
            'Mean Range': self.Age_Range['Age_Group_1'].mean() + self.Age_Range['Age_Group_2'].mean() +
                          self.Age_Range['Age_Group_3'].mean() + self.Age_Range['Age_Group_4'].mean() +
                          self.Age_Range['Age_Group_5'].mean() + self.Age_Range['Age_Group_6'].mean(),

            'Number of Sessions': self.Age_Range['Age_Group_1'].count() + self.Age_Range['Age_Group_2'].count() +
                                  self.Age_Range['Age_Group_3'].count() + self.Age_Range['Age_Group_4'].count() +
                                  self.Age_Range['Age_Group_5'].count() + self.Age_Range['Age_Group_6'].count()
        })
        grid.plot(x='Number of Sessions', y='Mean Range', kind='hexbin',
                  xscale='log', cmap='YlGnBu', gridsize=12, mincnt=1,
                  title="Age ranges by Simple Mean")
        plt.show()

    def get_bayesian_estimates(self):
        return self.Age_Range['Age_range'].agg(self.bayesian_mean)


    def dirichlet_mean(self, arr, prior=PRIOR):
        """
        Computes the Dirichlet mean with a prior
        """
        counter = Counter(arr)
        votes = [counter.get(n, 0) for n in range(1, 6)]
        posterior =list(map(sum, zip(votes, prior)))
        N = sum(posterior)
        weights = map(lambda i: (i[0] + 1) * i[1], enumerate(posterior))
        return float(sum(weights)) / N

    def get_dirichlet_estimates(self):
        return self.Age_Range['Age_range'].agg(self.dirichlet_mean)

    def top_Age_Range(self, n=10):
        grid = pd.DataFrame({
            'mean': self.get_means(),
            'count': self.get_counts(),
            'bayes': self.get_bayesian_estimates(),
            'dirichlet': self.get_dirichlet_estimates()
        })
        return grid.iloc[grid['dirichlet'].argsort()[-n:]]


if __name__ == "__main__":
    ratings = Age()
    print(ratings.top_Age_Range())
    print(ratings.plot_mean_frequency())


