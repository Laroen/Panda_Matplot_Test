import numpy as np
import pandas
import matplotlib.pyplot as plt


def Check_Age(df):
    df['Adult/Young'] = df['age'].apply(lambda x: 'Adult' if x >= 18 else 'Young')
    return df

dataList = [
    {'name':'Agárdi Pál', 'age':26, 'city':'Budapest'},
    {'name':'Aradi Márta', 'age':15, 'city':'Pécs'},
    {'name':'Balogh Edina', 'age':29, 'city':'Budapest'},
    {'name':'Bíró Zsolt', 'age':14, 'city':'Budapest'},
    {'name':'Budai Máté', 'age':19, 'city':'Debrecen'},
    {'name':'Fekete Géza', 'age':18, 'city':'Pécs'},
    {'name':'Horváth Ferenc', 'age':17, 'city':'Budapest'},
    {'name':'Karácsony Antal', 'age':20, 'city':'Budapest'},
    {'name':'Kiss Tibor', 'age':16, 'city':'Debrecen'},
    {'name':'Kovács Péter', 'age':27, 'city':'Budapest'},
    {'name':'Nagy Ibolya', 'age':23, 'city':'Pécs'},
    {'name':'Németh Kamilla', 'age':19, 'city':'Debrecen'},
    {'name':'Pálosi Richárd', 'age':23, 'city':'Budapest'},
    {'name':'Piros Adél', 'age':29, 'city':'Debrecen'},
    {'name':'Román Sarolta', 'age':17, 'city':'Budapest'},
    {'name':'Szabados Attila', 'age':25, 'city':'Debrecen'},
    {'name':'Szabó Erzsébet', 'age':21, 'city':'Budapest'},
    {'name':'Szilágyi Ede', 'age':18, 'city':'Pécs'},
    {'name':'Tóth Sándor', 'age':22, 'city':'Debrecen'},
    {'name':'Varga Imre', 'age':18, 'city':'Budapest'},
    {'name':'Virág Bertalan', 'age':17, 'city':'Pécs'}
]

my_list = pandas.DataFrame(dataList)

my_list_sorted = my_list.sort_values(by='age').reset_index(drop=True)
print(my_list_sorted)

'''
low = my_list['age'] == my_list['age'].min() # generate a Series with True and False
print(my_list.loc[low])                               # show the Series where low is True in DF
'''

lowest = my_list.loc[lambda x: x['age'] == min(my_list['age'])]
print(f'\n {lowest}')

print()
city_count = my_list['city'].value_counts()
print(city_count)

cities = my_list['city'].value_counts().count()
#cities_2 = my_list.groupby(by='city').agg({'city' : 'count'})
print(f'\nThe ammount of different cities: {cities}')

cities_all = my_list['city'].value_counts().sum()
print(f'\nThe whole ammount of cities, where members came from: {cities_all}')

my_avg = my_list['age'].mean()
print(f'\nAvg: {my_avg:.0f}')

Check_Age(my_list)
print(my_list)


# matplotlib

graph_2 = my_list.groupby(['city']).count()
graph_2.drop(columns='name', inplace=True)
graph_2.reset_index(inplace=True)
graph_2.rename(columns={'age':'Members'}, inplace=True)
#print(graph_2)


np_arr = my_list.values
np_graph_2= graph_2.values

x_plt1 = np_graph_2[:,0]
y_plt1 = np_graph_2[:,1]

x_plt3 = np_arr[:,0]
y_plt3 = np_arr[:,1]

plot1 = plt.subplot2grid((4, 3), (0, 0), colspan=3)
plt.xticks(np.arange(0, graph_2['Members'].max()+3, 1.0))
'''
plot2 = plt.subplot2grid((4, 3), (0, 2), rowspan=3, colspan=2)
plt.yticks(np.arange(0, max(y_plt1)+1, 1.0))
plt.xticks(rotation=30)
'''
plot3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2, colspan=3)
plt.yticks(np.arange(0, max(y_plt3)+1, 1.0))
plt.xticks(rotation=30)

plot1.barh(x_plt1,y_plt1,xerr=0.2)
plot1.set_title("Ammount for Members from each city")
plot1.set_ylabel("City")
plot1.set_xlabel("Ammount of Members")

plot3.bar(x_plt3,y_plt3,xerr=0.2, width=0.3)
plot3.set_title("Members's Age")
plot3.set_ylabel("Age")
plot3.set_xlabel("Name")


plt.show()
