import numpy as np

def generate_price():
    return np.around(np.random.normal(20.0,4.0),2)

r_file = open('Restaurant.csv')
v_file = open('veggie_dishes.csv')
m_file = open('meat_dishes.csv')

restaurants = list(r_file)
veggie_dishes = list(v_file)
meat_dishes = list(m_file)

r_file.close()
v_file.close()
m_file.close()

for i in range(len(restaurants)):
    restaurants[i] = restaurants[i].strip()
for i in range(len(veggie_dishes)):
    veggie_dishes[i] = veggie_dishes[i].strip()
for i in range(len(meat_dishes)):
    meat_dishes[i] = meat_dishes[i].strip()

v_factors = np.empty(50)
v_factors[0:10] = np.full(10,100)
v_factors[10:20] = np.random.randint(60,80,10)
v_factors[20:30] = np.random.randint(40,60,10)
v_factors[30:40] = np.random.randint(20,40,10)
v_factors[40:50] = np.random.randint(0,20,10)

output = open('Serves.csv', 'w')
for i in range(50):
    restaurant_name = restaurants[i]
    vf = v_factors[i]
    m = 100-vf
    v_indices = np.random.randint(0,len(veggie_dishes),vf)
    m_indices = np.random.randint(0,len(meat_dishes),m)
    for j in np.arange(vf):
        output.write(restaurant_name+','+veggie_dishes[v_indices[j]]+','+str(generate_price())+'\n')
    for j in np.arange(m):
        output.write(restaurant_name+','+meat_dishes[m_indices[j]]+','+str(generate_price())+'\n')

output.close()
