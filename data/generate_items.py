import numpy as np

verbs_file = open('cooking_verbs.csv', 'r')
meat_file = open('meat.csv', 'r')
veggie_file = open('veggies.csv', 'r')

verbs = list(verbs_file)
meats = list(meat_file)
veggies = list(veggie_file)

verbs_file.close()
meat_file.close()
veggie_file.close()

for i in range(len(verbs)):
    verbs[i] = verbs[i].strip()
for i in range(len(meats)):
    meats[i] = meats[i].strip()
for i in range(len(veggies)):
    veggies[i] = veggies[i].strip()

meat_number = 500
veggie_number = 500

veggie_dishes = np.empty(veggie_number, dtype=object)
meat_dishes = np.empty(meat_number, dtype=object)

veggie_verbs = np.random.randint(0, len(verbs), veggie_number)
veggie_first = np.random.randint(0, len(veggies), veggie_number)
veggie_second = np.random.randint(0, len(veggies), veggie_number)

meat_verbs = np.random.randint(0, len(verbs), meat_number)
meat_first = np.random.randint(0, len(meats), meat_number)
meat_second = np.random.randint(0, len(veggies), meat_number)

for i in range(veggie_number):
    veggie_dishes[i] = verbs[veggie_verbs[i]]+' '+veggies[veggie_first[i]]+' with '+veggies[veggie_second[i]]
for i in range(meat_number):
    meat_dishes[i] = verbs[meat_verbs[i]]+' '+meats[meat_first[i]]+' with '+veggies[meat_second[i]]

output = open('Item.csv', 'w')
for i in range(veggie_number):
    output.write(veggie_dishes[i]+',Y\n')
for i in range(meat_number):
    output.write(meat_dishes[i]+',N\n')

output.close()
