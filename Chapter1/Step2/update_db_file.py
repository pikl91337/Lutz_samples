from make_db_file import loadDbase, storeDbase, dbfilename
db = loadDbase()
print(db['tom']['name'])
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
storeDbase(db)

# does not work
