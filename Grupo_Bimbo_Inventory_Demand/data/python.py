import csv

with open('train_store.txt') as f:
    train = set( x.strip() for x in f.readlines())
with open('test_uniq_store.txt') as f:
    test = set( x.strip() for x in f.readlines())
    
with open('town_state.csv') as f:
    r = csv.reader(f)
    head = r.next()
    aaa  =set()
    for line in r:
        aaa.add(line[0])
        
print train - aaa


with open('test.csv') as f:
    r = csv.reader(f)
    head = r.next()
    aaa  =set()
    for line in r:
        info = dict(zip(head, line))        
        aaa.add(info['Agencia_ID'])
        
fw = open('test_unique_Agencia_ID.txt', 'w')
for e in aaa:
    fw.write(e + '\n')
fw.close()