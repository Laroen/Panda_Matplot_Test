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
print()
graph_2 = my_list['Adult/Young'].value_counts().reset_index()
print(graph_2)

graph_3 = my_list.groupby(['city']).count()
graph_3.drop(columns='name', inplace=True)
graph_3.reset_index(inplace=True)
graph_3.rename(columns={'age':'Members'}, inplace=True)
#print(graph_3)



np_arr = my_list.values
np_graph_2= graph_2.values
np_graph_3= graph_3.values


x_plt1 = np_graph_3[:,0]
y_plt1 = np_graph_3[:,1]

x_plt2 = np_graph_2[:,0]
y_plt2 = np_graph_2[:,1]

x_plt3 = np_arr[:,0]
y_plt3 = np_arr[:,1]

plot1 = plt.subplot2grid((6, 4), (0, 0), colspan=3)
plt.xticks(np.arange(0, graph_3['Members'].max()+3, 1.0))

plot2 = plt.subplot2grid((6, 4), (0, 3), rowspan=5)
plt.yticks(np.arange(0, max(y_plt2)+3, 1.0))
plt.xticks(rotation=15)

plot3 = plt.subplot2grid((6, 4), (2, 0), rowspan=4, colspan=3)
plt.yticks(np.arange(0, max(y_plt3)+1, 1.0))
plt.xticks(rotation=35)

plot1.barh(x_plt1,y_plt1,xerr=0.2)
plot1.set_title("Ammount of Members from each city")
plot1.set_ylabel("City")
plot1.set_xlabel("Ammount of Members")

plot2.bar(x_plt2,y_plt2,xerr=0.2, width=0.3)
plot2.set_title("Type of age")
plot2.set_ylabel("Number of young or adult")
plot2.set_xlabel("Adult or Young")

plot3.bar(x_plt3,y_plt3,xerr=0.2, width=0.3, align='center')
plot3.set_title("Members's Age")
plot3.set_ylabel("Age")
plot3.set_xlabel("Name")


plt.show()
