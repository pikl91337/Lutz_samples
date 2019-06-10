from initdata import tom
import shelve
db = shelve.open('people-shelve')
sue = db['sue'] # extract object sue
sue['pay'] *= 1.50
db['sue'] = sue # change object sue
db['tom'] = tom # add new record
db.close()
