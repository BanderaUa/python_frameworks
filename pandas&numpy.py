import random
import json
import numpy as np
import pandas as pd
from pandas import MultiIndex

# a = np.array([1, 2, 3])
# print(a)
#
# odd_number_list = [1, 3, 5, 7]
#
# b = np.array(odd_number_list)
# print(b)
#
# two_dim_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# np.array(two_dim_list)
#
# print(two_dim_list)
#
# c = np.arange(0, 10, 2)
#
# print(c)
#
# d = np.zeros(9)  # all zeros
#
# e = np.zeros((2, 3))  # 2 - strings   3 - columns
#
# # e= [[0. 0. 0.]
# #    [0. 0. 0.]]
#
#
# print(e)
#
# f = np.ones(3)  # all ones
#
# g = np.ones((3, 2))
#
# h = np.linspace(0, 5, 5)  # h = [0.   1.25 2.5  3.75 5.  ]
# print(h)
#
# identity_matrix = np.eye(3)
# print(identity_matrix)
# # [1. 0. 0.]
# # [0. 1. 0.]
# # [0. 0. 1.]
# identity_matrix2 = np.eye(5, 5)
# print(identity_matrix2)
# #  [1. 0. 0. 0. 0.]
# #  [0. 1. 0. 0. 0.]
# #  [0. 0. 1. 0. 0.]
# #  [0. 0. 0. 1. 0.]
# #  [0. 0. 0. 0. 1.]
#
#
# i = np.random.rand(5)
# print(i)
# # i == [0.77852722 0.58589975 0.41297126 0.89823964 0.14914716]
#
# j = np.random.rand(5, 4)
# # print(j)
#
# # j ==[[0.30294612 0.74170679 0.3304596  0.6610522 ]
# #     [0.90217947 0.3128738  0.1369325  0.19218654]
# #     [0.11731189 0.10038098 0.70591828 0.92753398]
# #     [0.90770927 0.99256072 0.52596843 0.73744581]
# #     [0.29998815 0.94163771 0.38882186 0.74980668]]
#
# q = np.random.randint(0, 50, 20)
# print(q)
#
# two_dim_list2 = q.reshape(4, 5)
# # print(two_dim_list2)
#
# # two_dim_list2 == [[10 39  3 41 19]
# #                  [35 33 11 18 10]
# #                  [17 42 36 20 40]
# #                  [37  9 18 27 33]]
#
# max_int = q.max()  # the highest value in array "q"
# print(max_int)
#
# min_int = q.min()  # the lowest value in array "q"
# print(min_int)
#
# max_arg = q.argmax()  # index of the highest value in array "q"
# print(max_arg)
#
# min_arg = q.argmin()  # index of the lowest value in array "q"
# print(min_arg)
#
# shape_of_q = q.shape
# print(shape_of_q)  # shape_of_q == (20,)    20 - strings  '' -columns
#
# arr = np.arange(1, 11)
# # [1 2 3 4 5 6 7 8 9 10]
# arr_sum = arr + arr
# # [ 2  4  6  8 10 12 14 16 18 20]
# arr_sum2 = arr + 1
# # [2 3 4 5 6 7 8 9 10 11]
#
#
# print(arr ** 2)
#
# print(np.sqrt(arr))
# print(np.exp(arr))
#
# """""""""""""PANDAS INTRODUCTION"""""""""""""
#
# letters = ['a', 'b', 'c']
# numberss = [1, 2, 3]
# np_arr = np.array(numberss)
# dict1 = {'a': 1, 'b': 2, 'c': 3}
#
# pd1 = pd.Series(data=letters, index=numberss)
#
# print(pd1[1])
# print(pd1[2])
# print(pd1[3])
#
# dict_series = pd.Series(dict1)
# print(dict_series)
#
# life_long_average = pd.Series([84.7, 84.5, 83.7], ["Hong Kong", "Japan", "Singapoure"])
# print(life_long_average)
# life_long_average1 = pd.Series([84.7, 84.5, 83.7], ["USA", "Japan", "Singapoure"])
# print(life_long_average1 + life_long_average)
#
# """DATA FRAMES"""
#
# my_df = pd.DataFrame(np.random.randn(4, 5), [1, 2, 3, 4], ['red', 'orange', 'yellow', 'green', 'blue'])
# # print(my_df)
# # #         red    orange    yellow     green      blue
# # # 1  0.496975 -0.019885 -0.135683 -0.042995 -1.307545
# # # 2  0.464517 -0.574651  0.182221  1.064881  0.573066
# # # 3  1.144458 -0.597515  0.516692 -1.043327 -0.428518
# # # 4  1.405683  1.076329  0.459339  0.419842  0.445378
# #
# # print(my_df['orange'])
# #
# # print(my_df[['yellow', 'blue']])
# #
# # my_df['indigo'] = my_df['blue']
# # print(my_df)
# #
# # my_df["violet"] = my_df['blue'] + my_df['indigo']
# # print(my_df)
# #
# # print(my_df.loc[2])
# #
# # print(my_df.iloc[1])
# #
# # print(my_df.loc[3, 'orange'])
# #
# # print(my_df.loc[[1, 3], ['blue', 'violet']])
#
# df2 = pd.DataFrame(np.random.randn(4, 3), ['a', 'b', 'c', 'd'], ['X', 'Y', 'Z'])
# print(df2)
#
# #
# # bool_df = df2 > 0
# # print(bool_df)
# #
# # print(df2[bool_df])
# #
# #
# #
# # print(df2[df2>0])
# #
# # print(df2['Y']>1)
#
# # print(df2[df2['Y']>0])
#
#
# res_df = (df2[df2["X"] < 0])
# #       X          Y        Z
# # a  0.956396 -1.076052  1.686785
# # b  1.496200 -0.874279 -0.368235
# # c -0.891143 -1.875188 -0.298729
# # d -1.733999  0.270454 -1.233022
# print('this is res df:')
# print(res_df)
# print('this is res df[Z]')
# print(res_df[["Z", 'Y']])
#
# bool_res = df2 > 0
# print(bool_res)
#
# print(bool_res[["X", "Y"]])
#
# selection_df = df2[(df2["X"] > 0) | (df2["Z"] > 0)]  # '&' == and in numpy ,  '|' == or in numpy
# print('this is sel')
#
# print(selection_df)
#
# change_str = df2.reset_index()
#
# z1 = [2, 3, 5, 6]
#
# df2['Z1'] = z1
# print(df2)
#
# df2.set_index("Z1", inplace=False)
# print(df2)
#
# out_ind = ['T1', 'T1', 'T1', 'T2', 'T2', 'T2']
# ins_ind = [1, 2, 3, 1, 2, 3]
# ind_hier = list(zip(out_ind, ins_ind))
# print(ind_hier)
#
# mult_ind = pd.MultiIndex(levels=[['T1', 'T2'], [1, 2, 3]], codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]])
# mult_ind_df = pd.DataFrame(np.random.randn(6, 2), mult_ind, ['X', 'Y'])
# print(mult_ind_df)
#
# print(mult_ind_df.loc['T1'].loc[2])
#
# print('this is last print')
# print(mult_ind_df.index.names)
#
# mult_ind_df.index.names = ['Types', 'Numbers']
# print(mult_ind_df)
#
# print(mult_ind_df.loc['T1'].loc[3]['Y'])
#
# print(mult_ind_df.xs('T2'))
# print(mult_ind_df.xs(2, level="Numbers"))
#
# print(mult_ind)
#
# dict22 = {'one': [10, np.nan, 30], 'two': [np.nan, np.nan, 50], 'three': [10, 10, 10]}
#
# df_dict = pd.DataFrame(dict22)
# print(df_dict)
#
# print('frormated dict')
# drop_na_dict = df_dict.dropna(thresh=2)
# print(drop_na_dict)
# print('ffff')
# filll_na_dict = df_dict['one'].fillna(value=df_dict['two'].mean)
# print(filll_na_dict)
#
dict_of_dataframe = {'Company': ['COMP1', 'COMP1', 'COMP2', 'COMP2', 'COMP3', 'COMP3'],
                     'Months': ['MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG'],
                     'Salary': [2000, 1500, 3000, 5000, 2500, 3500]}
df = pd.DataFrame(dict_of_dataframe)
# print(df)
mean_salary = (df.groupby('Company')[['Salary']].mean())

sum_of_salary = df.groupby('Company')[['Salary']].sum()

sum_of_salary_3rd_company = df.groupby('Company')[['Salary']].sum().loc['COMP3']

# print(sum_of_salary_3rd_company)
#
#
# print(df.groupby('Company').count())
#
# print(df.groupby('Company').max())
#
# print(df.groupby('Company').min())
#
# print(df.groupby('Company').describe())
#
# print(df.groupby('Company').describe().transpose())
#
# print(df.groupby('Company').describe().transpose()['COMP2'])
#


# df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3'], 'C': ['C0', 'C1', 'C2', 'C3'],
#                     'D': ['D0', 'D1', 'D2', 'D3'], }, index=[0, 1, 2, 3])
#
# df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'], 'B': ['B4', 'B5', 'B6', 'B7'], 'C': ['C4', 'C5', 'C6', 'C7'],
#                     'D': ['D4', 'D5', 'D6', 'D7'], }, index=[4, 5, 6, 7])
#
# df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'], 'B': ['B8', 'B9', 'B10', 'B11'], 'C': ['C8', 'C9', 'C10', 'C11'],
#                     'D': ['D8', 'D9', 'D10', 'D11'], }, index=[8, 9, 10, 11])

# print(df1)
# print(df2)
# print(df3)
# concat_this = pd.concat([df1,df2,df3])
# print(concat_this)


#
# df1 = pd.DataFrame({'order_id': [114, 235, 432],
#                      'user_id': [1, 2, 3],
#                      'user_name': ['James Brown', 'Jack White',
#                                    'Jane Green'],
#                      'country': ['USA', 'USA',
#                                     'France']})
#
# df2 = pd.DataFrame({'order_id': [114, 235, 432],
#                      'user_id': [1, 2, 3],
#                      'order_date': ['2020-02-11', '2020-02-11',
#                                     '2020-02-15'],
#                      'OS': ['Android', 'iOS', 'Android']})
#
# df3 = pd.merge(df1,df2,on='order_id')
#
# print(df3)


# df1 = pd.DataFrame({'order_id': [114, 235, 432],
#                     'user_id': [1, 2, 3],
#                     'user_name': ['James Brown', 'Jack White',
#                                   'Jane Green'],
#                     'country': ['USA', 'USA',
#                                 'France']})
#
# df2 = pd.DataFrame({'order_id': [114, 235, 432],
#                     'user_id': [1, 2, 3],
#                     'order_date': ['2020-02-11', '2020-02-11',
#                                    '2020-02-15'],
#                     'OS': ['Android', 'iOS', 'Android']})
#
# df3 = pd.merge(df1, df2, on='user_id')
# print('this is df 1')
#
# print(df1)
#
# print('*' * 100)
#
# print('this is df 2')
# print(df2)
# print(
#     '*' * 100
# )
# print('this is merged df1 and df2')
# print(df3)
# # this is merged df1 and df2
# #    order_id_x  user_id    user_name country  order_id_y  order_date       OS
# # 0         114        1  James Brown     USA         114  2020-02-11  Android
# # 1         235        2   Jack White     USA         235  2020-02-11      iOS
# # 2         432        3   Jane Green  France         432  2020-02-15  Android
# print('*' * 100)


# df1 = pd.DataFrame({'order_id': [114, 235, 432],
#                     'user_id': [1, 2, 3],
#                     'user_name': ['James Brown', 'Jack White',
#                                   'Jane Green'],
#                     'country': ['USA', 'USA',
#                                 'France']})
#
# df2 = pd.DataFrame({'order_id': [114, 235, 432], 'user_id': [2, 4, 5], 'order_date': ['2020-02-11', '2020-02-11',
# '2020-02-15'], 'OS': ['Android', 'iOS', 'Android']}) df3 = pd.merge(df1, df2, on=['user_id', ]) print(df3)
# order_id_x         user_id   user_name      country  order_id_y     order_date       OS 0         235
# 2        Jack White     USA         114       2020-02-11    Android  - because only one user id is equal == 2


# df1 = pd.DataFrame({'order_id': [114, 235, 432],
#                     'user_id': [1, 2, 3],
#                     'user_name': ['James Brown', 'Jack White',
#                                   'Jane Green'],
#                     'country': ['USA', 'USA',
#                                 'France']})
#
# df2 = pd.DataFrame({'order_id': [114, 235, 432],
#                     'user_id': [2, 4, 3],
#                     'order_date': ['2020-02-11', '2020-02-11',
#                                    '2020-02-15'],
#                     'OS': ['Android', 'iOS', 'Android']})

# df3 = pd.merge(df1, df2, on=['user_id', ])
# print(df3)
#         order_id_x  user_id   user_name   country  order_id_y    order_date       OS
# 0         235        2        Jack White     USA         114     2020-02-11    Android
# 1         432        3        Jane Green   France         432    2020-02-15    Android


# df4 = pd.merge(df1, df2, on=['user_id', 'order_id'])
# print(df4)

#    order_id     user_id   user_name  country  order_date       OS
# 0       432        3     Jane Green  France  2020-02-15    Android


# df1 = pd.DataFrame({
#     'user_name': ['James Brown', 'Jack White',
#                   'Jane Green'],
#     'country': ['USA', 'USA',
#                 'France']},
#     index=['ind1', 'ind2', 'ind3'])
#
# df2 = pd.DataFrame({'order_id': [114, 235, 432],
#                     'user_id': [2, 4, 3],
#                     'order_date': ['2020-02-11', '2020-02-11',
#                                    '2020-02-15'],
#                     'OS': ['Android', 'iOS', 'Android']},
#                    index=['ind1', 'ind4', 'ind3'])


# print(df1)
# print('*'*100)
# print(df2)
# print('*'*100)

#
# df3 =df1.join(df2)
# print(df3)

"""     user_name     country    order_id  user_id   order_date          OS
ind1    James Brown     USA        114.0      2.0     2020-02-11        Android
ind2    Jack White      USA        NaN        NaN         NaN           NaN
ind3    Jane Green      France     432.0      3.0     2020-02-15        Android
"""

#
# df3 =df2.join(df1)
# print(df3)
"""      order_id  user_id   order_date         OS            user_name            country
ind1       114        2      2020-02-11       Android        James Brown             USA
ind4       235        4      2020-02-11         iOS             NaN                  NaN
ind3       432        3      2020-02-15       Android        Jane Green            France
"""

df1 = pd.DataFrame(
    {'A': [1, 2, 3, 4],
     'B': [123, 245, 321, 123],
     'C': ['aaa', 'bbb', 'ccc', 'ddd']}
)

print(df1)

df2 = df1['B'].unique()  # Уникальные символы в столбце "B"
print(df2)

df3 = len(df1['B'].unique())
print(df3)

df4 = df1['B'].nunique()  # .nunique() == len()
print(df4)

print(df1['B'].value_counts())

print(df1[df1['A'] < 3])

print(df1[(df1['A'] < 3) & (df1['B'] < 200)])

print('*' * 100)


def times3(x):
    return x * 3


print(df1["A"].apply(times3))

print(df1["A"].apply(times3).sum())

df1['A'].apply(lambda x: x * 3)

df1['C'].apply(len)

print(df1.columns)

print(df1.index)

print(df1.sort_values("B"))

print(df1.isnull())

df_new = pd.DataFrame(
    {'A': [1, 1, 1, 2, 2, 2],
     'B': [123, 222, 222, 123, 123, 222],
     'C': ['aaa', 'bbb', 'aaa', 'bbb', 'bbb', 'aaa'],
     'D': [1, 2, 4, 3, 1, 5]}
)
# print(df_new)

print(df_new.pivot_table(values='D', index=['A', "B"], columns=['C']))
