temp_year=temp.groupby(['Year']).mean()
rain_year=rain.groupby(['Year']).mean()

fig, ax1 = plt.subplots(figsize=(9,5))

color = 'tab:blue'
ax1.bar(rain_year.index, rain_year['Rainfall - (MM)'].values, color=color,alpha=0.8)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(120,170)
ax1.set_ylabel('Rainfall - (MM)', color=color,alpha=0.8)

ax2=ax1.twinx()

color = 'tab:red'
ax2.plot(temp_year.index,temp_year['Temperature - (Celsius)'].values,color=color)
ax2.set_ylabel('Temperature - (Celsius)', color=color,alpha=0.8)
ax2.tick_params(axis='y', labelcolor=color)

ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['right'].set_visible(False)

ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)

plt.title("Brazil's Climate data (1991-2016)",alpha=0.8)