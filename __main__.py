from src.data import Data
from src.interview import Interview
from src.utils_interview import Utils

class Main:
    @staticmethod
    def main():
        name = input('Qual é o seu nome? ').capitalize().strip()
        print('')
        interview = Interview(name)
        interview.interview()
        results = interview.get_results()
        Data().export(results)
if __name__ == "__main__":
    Main.main()
