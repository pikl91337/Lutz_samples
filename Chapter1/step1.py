bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')

db = {}
db['bob'] = bob
db['sue'] = sue

db['sue']['pay'] # extract Sue's salary

[rec['name'] for rec in db.values() if rec['age'] >= 45]
# will print names of people whos age higher (or equal) than 45
