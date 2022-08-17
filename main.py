#plotting of data on graph.
import Data_fetcher
import matplotlib.pyplot as plt
import months_from_dates as months

plt.ylabel('Volume')
plt.xlabel('months', )

y= Data_fetcher.volume
x = months.month_list

font = {'size': 1}
plt.xticks(rotation=90)
plt.rc('font', **font)
plt.plot(x, y)
#plt.ticklabel_format(style='plain')
#plt.ticklabel_format(style = 'plain')

manager = plt.get_current_fig_manager()

plt.show()
