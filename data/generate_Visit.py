import numpy as np

def generate_tip(v_factor, veggie):
    if veggie:
        base = np.random.normal(3.0,1.0)
        tip = base + v_factor*10.0
    else:
        tip = np.random.normal(6.0,1.0)
    return np.around(tip,2)

p_file = open('Patron.csv')
r_file = open('v_factor.csv')

patrons = list(p_file)
restaurants = list(r_file)

p_file.close()
r_file.close()

p = len(patrons)
r = len(restaurants)

for i in range(p):
    patrons[i] = patrons[i].strip()
for i in range(r):
    restaurants[i] = restaurants[i].strip()

p_array = np.empty((p,3), dtype=object)
for i in range(p):
    w = patrons[i].split(',')
    p_array[i,0] = w[0]
    p_array[i,1] = w[1]
    p_array[i,2] = w[2]

r_dict = dict()
for i in range(r):
    w = restaurants[i].split(',')
    r_dict[w[0]] = float(w[1])
    
oid = 1

outfile = open('Visit.csv', 'w')
for i in range(p):
    veggie = (p_array[i,2] == 'Y')
    days = np.arange(1,31)
    np.random.shuffle(days)
    days = days[0:5]
    r_indices = np.arange(r)
    np.random.shuffle(r_indices)
    r_indices = r_indices[0:5]
    tips = np.empty(5)
    for j in range(5):
        date = '2014-11-'+str(days[j]).zfill(2)
        rest_name = restaurants[r_indices[j]].split(',')[0]
        v_factor = r_dict[rest_name]
        tips[j] = generate_tip(v_factor, veggie)
        outfile.write(str(oid)+','+p_array[i,0]+','+p_array[i,1]+','+rest_name+','
                +str(tips[j])+','+date+'\n')
        oid = oid+1

outfile.close()
