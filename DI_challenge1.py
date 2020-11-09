import pandas as pd

product_file='ulta.csv'
product_db=pd.read_csv(product_file)

nameA = product_db['name'].loc[0]
listA = product_db['ingredients'].loc[0].split(', ')

max_shared=0
match_index=None

print 'searching for products similar to {}...'.format(nameA)

for i in range(0,len(product_db)):
    nameB=product_db['name'].loc[i]
    try:
        listB = product_db['ingredients'].loc[i].split(', ')
    except:
        listB = [None]
    shared=(set(listA) & set(listB))
    num_shared=len(shared)
    if((num_shared>max_shared) and (nameA!=nameB)):
        max_shared=num_shared
        match_index=i
        
print 'best match: {}'.format(product_db['name'].loc[match_index])
print '{} shared ingredients'.format(max_shared)