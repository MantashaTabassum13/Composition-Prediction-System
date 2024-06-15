import pandas as pd
df=pd.read_csv('D:\\DataModel\\jo.csv')
# df['num_mission_success'] = pd.Series(dtype='object')
sum_safe=df.Location.value_counts().sum()
print(sum_safe)
area=input('enter location :  ')
city_safe=df.loc[(df['Location'] == area)].value_counts().sum()
print(city_safe)
danger_percent=sum_safe/city_safe
print(danger_percent)