import numpy as np
import matplotlib.pyplot as plt

f = open('v_factor_vs_yelp_factor.csv')
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
plt.title('Veggie factor vs Yelp factor')
plt.xlabel('Veggie factor')
plt.ylabel('Yelp factor')

plt.savefig('plots/v_factor_vs_yelp_factor.png')
