import numpy as np
import matplotlib.pyplot as plt

f = open('v_factor_vs_average_tip.csv')
rawdata = list(f)
f.close()

l = len(rawdata)
for i in range(l):
    rawdata[i] = rawdata[i].strip()

x = np.empty(l)
y = np.empty(l)

for i in range(l):
    w = rawdata[i].split(',')
    x[i] = float(w[1])
    y[i] = float(w[2])

plt.plot(x,y,'o')
plt.title('Veggie factor vs average tip')
plt.xlabel('Veggie factor')
plt.ylabel('Average tip ($)')

plt.savefig('plots/v_factor_vs_average_tip.png')
