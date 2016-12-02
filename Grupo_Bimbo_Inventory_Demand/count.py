import csv

with open('test_unique_Agencia_ID.txt') as f:
    train = set( x.strip() for x in f.readlines())
with open('train_unique_Agencia_ID.txt') as f:
    test = set( x.strip() for x in f.readlines())
    
xxx = train | test
with open('town_state.csv') as f:
    r = csv.reader(f)
    head = r.next()
    
    fw = open('exist_town_state.csv', 'wb')
    w  = csv.writer(fw)
    w.writerow(head)
    for line in r:
        if line[0] in xxx:
	        
            w.writerow(line)
    fw.close()
        