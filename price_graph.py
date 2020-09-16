import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

price_data = pd.read_csv('lisbon_prices.csv',names=['price','area','date'])
price_data.loc[price_data.area.isnull(),'area'] = 'lisboa'
price_data['area'] = price_data['area'].str.replace(r'/$', '')

# Normalize to one at first observed date
price_data['price'] = price_data.groupby('area')['price'].transform(lambda x: x / x.iloc[0])

plt.rc('xtick', labelsize=20)
plt.rc('ytick', labelsize=20)

plot_days = 1000
plticks = list(price_data.loc[price_data.area=='lisboa','date'].tail(plot_days))[0::max(1,int(len(list(price_data.loc[price_data.area=='lisboa','date'].tail(plot_days)))/20))]

fig, ax = plt.subplots(figsize=(15,12))
ax = sns.lineplot(x='date',y='price',hue='area',data=price_data,legend=None)
plt.xlabel('')
plt.ylabel('Preço por m2', fontsize=20)
lgd = ax.legend(price_data['area'], prop={'size': 20}, loc='upper left', bbox_to_anchor=(1, 1), frameon=False)
plt.xticks(plticks)
ax.tick_params(axis="both", which="both", bottom=False, top=False, left=False, right=False)
sns.despine(right=True, top=True, bottom=True, left=True)
fig.autofmt_xdate()
fig.savefig('docs/price_graph', bbox_extra_artists=(lgd,), bbox_inches='tight')
