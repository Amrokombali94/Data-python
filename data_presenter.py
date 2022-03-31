open_file = open('CupcakeInvoices.csv')



for line in open_file:
    print(line)

open_file.seek(0)


print('-------------------------------------')
print('-------------------------------------')


for line in open_file:
    line = line.rstrip('\n').split(',')
    print(line[2])

open_file.seek(0)

print('-------------------------------------')
print('-------------------------------------')


for line in open_file:
    line = line.rstrip('\n').split(',')
    print(float(line[3])*float(line[4]))

print('-------------------------------------')
print('-------------------------------------')

open_file.seek(0)


totals = 0
for line in open_file:
    line = line.rstrip('\n').split(',')
    total=float(line[3])*float(line[4])
    totals+=total

print(totals)

open_file.close()