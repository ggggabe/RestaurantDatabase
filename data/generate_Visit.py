import numpy as np

def generate_tip(v_factor, veggie):
    if veggie:
        base = np.random.normal(3.0,1.0)
        tip = base + v_factor*10.0
    else:
        tip = np.random.normal(6.0,1.0)
    return np.around(tip,2)

def generate_review(v_factor, veggie):
    if veggie:
        return np.random.binomial(1, v_factor)
    else:
        return np.random.binomial(1, .5)

p_file = open('Patron.csv')
r_file = open('v_factor.csv')
s_file = open('serves.csv')

patrons = list(p_file)
restaurants = list(r_file)
serves = list(s_file)

p_file.close()
r_file.close()

p = len(patrons)
r = len(restaurants)
s = len(serves)

vpp = 20

for i in range(p):
    patrons[i] = patrons[i].strip()
for i in range(r):
    restaurants[i] = restaurants[i].strip()
for i in range(r):
    serves[i] = serves[i].strip()

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

s_array = np.empty((s,3), dtype=object)
for i in range(s):
    w = serves[i].split(',')
    s_array[i,0] = w[0]
    s_array[i,1] = w[1]
    s_array[i,2] = w[2]
    
oid = 1

outfile = open('Visit.csv', 'w')
orderfile = open('Ordered.csv', 'w')
reviewfile = open('Reviewed.csv','w')

for i in range(p):
    veggie = (p_array[i,2] == 'Y')
    days = np.arange(1,31)
    np.random.shuffle(days)
    days = days[0:vpp]
    r_indices = np.arange(r)
    np.random.shuffle(r_indices)
    r_indices = r_indices[0:vpp]
    tips = np.empty(vpp)
    for j in range(vpp):
        date = '2014-11-'+str(days[j]).zfill(2)
        rest_name = restaurants[r_indices[j]].split(',')[0]
        v_factor = r_dict[rest_name]
        tips[j] = generate_tip(v_factor, veggie)
        outfile.write(str(oid)+','+p_array[i,0]+','+p_array[i,1]+','+rest_name+','
                +str(tips[j])+','+date+'\n')

        found = False
        for m in range(s):
            if found == False:
                if s_array[m,0] == rest_name:
                    first_index = m
                    found = True
            else:
                if m == s-1:
                    last_index = s
                    break
                if s_array[m,0] != rest_name:
                    last_index = m
                    break
        possible_items = s_array[first_index:last_index]
        num_items = last_index-first_index
        veggie_index = 0
        for m in range(num_items):
            if possible_items[m,2] == 'Y':
                veggie_index = m
                break
        veggie_items = possible_items[veggie_index:num_items]
        num_veggie_items = num_items-veggie_index
        if veggie:
            indices = np.random.randint(0,num_veggie_items,2)
            orderfile.write(str(oid)+','+veggie_items[indices[0],1]+'\n')
            orderfile.write(str(oid)+','+veggie_items[indices[1],1]+'\n')
        else:
            indices = np.random.randint(0,num_items,2)
            orderfile.write(str(oid)+','+possible_items[indices[0],1]+'\n')
            orderfile.write(str(oid)+','+possible_items[indices[1],1]+'\n')

        oid = oid+1
    if (veggie):
        num_review = vpp - np.random.randint(0,5)
    else:
        num_review = vpp/2 + 1 - np.random.randint(0,5)
    for j in range(num_review):
        rest_name = restaurants[r_indices[j]].split(',')[0]
        v_factor = r_dict[rest_name]
        review = generate_review(v_factor, veggie)
        reviewfile.write(rest_name+','+p_array[i,0]+','+p_array[i,1]+','+str(review)+'\n')

outfile.close()
orderfile.close()
reviewfile.close()
