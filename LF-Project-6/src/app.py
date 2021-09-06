import main
import pandas as pd

query = input("Enter your query : ")
data_frame = pd.read_csv('../data/yahoo_ques.csv')

similarity_frame = main.check_similarity(query, data_frame)
print(similarity_frame.head())