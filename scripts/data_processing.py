import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import re

path = 'C:/Users/cuong/pycharmProjects/Facebook_crawl/file_data/user_comments.csv'
path1 = r"C:\Users\cuong\pycharmProjects\Facebook_crawl\file_data\user.csv"
path2 = r"C:\Users\cuong\pycharmProjects\Facebook_crawl\file_data\comments.csv"
path3 = r"C:\Users\cuong\pycharmProjects\Facebook_crawl\file_data\filecomment.xlsx"
path4 = r"C:\Users\cuong\pycharmProjects\Facebook_crawl\file_data\data.csv"
path5 = r"C:\Users\cuong\pycharmProjects\Facebook_crawl\file_data\data1.csv"
path6 = r"C:\Users\cuong\pycharmProjects\Facebook_crawl\file_data\data2.csv"


df = pd.read_csv(path,encoding='utf-8')
df1 = pd.read_csv(path1,encoding='utf-8')
df2 = pd.read_csv(path2,encoding='utf-8')



# df1 = df1.drop(0,axis=0)
# df1['user'] = df1['user'].str.split('__cft').str[0]
# df1['user'] = df1['user'].str.replace('/?','')
# df1['user'] = df1['user'].str.replace('groups/165309862197524/user/','profile.php?id=')

# df = pd.concat([df1,df2],axis=1)




# pattern1 = r"(\w+\s\d+-\d+\s\w+)"
# pattern2 = r"(\d+-\d+\s\w+)"
# a[] = df2['comment'].str.extract(pattern1)
# b[] = df2['comment'].str.extract(pattern2)
#
a = pd.read_csv(path5)
b = pd.read_csv(path6)

# a.dropna(subset=['0'], inplace=True)
# b.dropna(subset=['0'], inplace=True)

# pattern1 = r"(\w+)"
# x = a['0'].str.extract(pattern1)
# for word in x.values.flatten():
#     if word is not None and word.casefold() != 'psg'and word.casefold() != 'paris' and word.casefold() != 'germain':
#         print(word)
#         a = a[~a['0'].str.contains(word)]

# pattern = r"(\d+-\d+)"
# a = a['0'].str.extract(pattern)


# pattern = r"(\d+-\d+)\s(\w+)"

# for index, row in b.iterrows():
#     match = re.match(pattern, row[0])
#     if match:
#         score = match.group(1)
#         team = match.group(2)
#
#         if team == "psg" or team == "mbape" or team == "Psg" or team == "m3p" or team == "PSG":
#             b.at[index, 'new_column'] = f"{team} {score}"
#         else:
#             b.at[index, 'new_column'] = f"{score} {team}"
#     else:
#         b.at[index, 'new_column'] = "-".join(row[0].split())
#
# b = b.drop('0', axis=1)


# pattern = r"(\d+-\d+)"
# b = b['0'].str.extract(pattern)

# x = pd.concat([a,b], axis=0)
x = pd.read_csv(path4)

value_counts = x['0'].value_counts()
ratios = value_counts / len(x['0']) * 100
plt.figure(figsize=(10,6), dpi=600)
plt.pie(ratios, labels=value_counts.index, autopct='%1.1f%%')
plt.show()



x.to_csv(path4,index=False)
a.to_csv(path5,index=False)
b.to_csv(path6,index=False)
# df.to_csv(path,index=False)
# df1.to_csv(path1, index=False)
# df2.to_csv(path2, index=False)
# df.to_excel(path3, index=False)