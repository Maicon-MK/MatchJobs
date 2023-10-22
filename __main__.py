from src.data import Data
from src.interview import Interview

name = input('Qual é o seu nome? ').capitalize().strip()
print('')
interview = Interview(name)
results = interview.interview()
Data().export(results)
