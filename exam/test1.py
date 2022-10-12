# from encodings import utf_8
# import pandas as pd


# data = pd.read_csv("./exam/testpaper/TEST.csv")
# df_single=data[data['Category']=='single']
# df_fib=data[data['Category']=='fib']
# print(type(df_single))

# for i, row in df_single.iterrows():
#     print(type(row['ID']))
#     print(row['description'])
#     print(row['answer'])
#     print(row['A'])
#     print(row['B'])
#     print(row['C'])
#     print(row['D'])
from faker import Faker
fake = Faker()