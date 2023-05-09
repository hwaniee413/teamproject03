import pandas as pd

class ChampionsData:
    def read_data(self):
        path = "./champions.csv"
        df = pd.read_csv('/champions.csv')
        print(df)
