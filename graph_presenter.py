import matplotlib.pyplot as plt
import numpy as np
open_file = open('CupcakeInvoices.csv')

total_choco = 0
total_vanilla = 0
total_strawberry = 0
for line in open_file:
    line = line.rstrip('\n').split(',')
    for item in line:
        if item == 'Chocolate':
            total=float(line[3])*float(line[4])
            total_choco+=total
        elif item == 'Vanilla':
            total=float(line[3])*float(line[4])
            total_vanilla+=total
        elif item == 'Strawberry':
            total=float(line[3])*float(line[4])
            total_strawberry+=total
    

print(total_choco)
print(total_vanilla)
print(total_strawberry)


total_value=[total_choco, total_vanilla, total_strawberry]
cup_cakes=['Chocolate', 'Vanilla', 'Strawberry']

ypos= np.arange(len(cup_cakes))
print(ypos)

plt.xticks(ypos, cup_cakes)
plt.ylabel("revenue($)")
plt.title('Cup Cakes Income')
plt.bar(ypos, total_value)


plt.show()


open_file.close()