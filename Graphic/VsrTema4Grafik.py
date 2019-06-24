import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

data = pd.read_csv('web_traffic.tsv', sep='\t', header=None)

x, y = data[0], data[1]
list_x, list_y = list(x), list(y)

for i in range(len(list_y)):
    if math.isnan(list_y[i]) or math.isnan(list_x[i]):
        list_y[i] = 0
        list_x[i] = 0
list_y.remove(0), list_x.remove(0)

np_x, np_y = np.array(list_x), np.array(list_y)

x2 = list(range(743))

plt.scatter(list_x, list_y, label = u'Исходные данные', color='black')

f1 = sp.poly1d(sp.polyfit(np_x, np_y, 1))
plt.plot(x2, f1(x2), '--', linewidth = 2, label = u'полином 1-ой степени (линейный график)', color='b')
f2 = sp.poly1d(sp.polyfit(np_x, np_y, 2))
plt.plot(x2, f2(x2), ':', linewidth = 2, label = u'полином 2-ой степени (квадратичный)', color='r')

plt.title('Линейная регрессия.')
plt.legend()
plt.ylabel('y')
plt.xlabel('x')
plt.show()

