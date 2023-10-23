import pandas as pd
from os import path
from src.interview import Interview

class Data:
    def export(self, results):
            if not path.exists('C:\\Users\\codgibrazuca\\Documents\\PYTHON\\MatchJobs\\data\\dados.csv'):
                return pd.DataFrame(results).to_csv('data/dados.csv', index=False)            
            else:
                return pd.DataFrame(results).to_csv('data/dados.csv', mode='a', index=False, header=False)