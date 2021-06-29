import pandas as pd
import random
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Create a DataFrame for the 4 'bins'. For this purpose, I've used random numbers to fill in the dataframe.
d = {'SI':random.sample(range(10,25),6),'SA':random.sample(range(10,25),6),'PD':random.sample(range(10,25),6),'LS':random.sample(range(10,25),6)}
years = ['2016','2017','2018','2019','2020','2021']
df= pd.DataFrame(data=d, index=years)
print(df)

# Create a line plot
rcParams['figure.figsize'] = 10, 4
plt.plot(df)
plt.legend(['SI','SA','PD','LS'],loc=4)
plt.grid(True, color='k', linestyle=':')
plt.title("TIPS Themes among the years 2016~2021")
plt.xlabel("Year")
plt.show()

# Create a Pie chart
width=0.35
fig, ax = plt.subplots()
ax.bar(years, df['SI'], width, label='SI')
ax.bar(years, df['SA'], width, label='SA', bottom=df['SI'])
ax.bar(years, df['PD'], width, label='PD', bottom=df['SA']+df['SI'])
ax.bar(years, df['LS'], width, label='LS', bottom=df['PD']+df['SA']+df['SI'])
ax.set_ylabel('Number of TIPS')
ax.set_xlabel('Years')
ax.legend()
plt.title("Stacked bar chart")
plt.show()
