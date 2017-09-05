import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError

#con = r.connect('localhost', 28015).repl()
con = r.connect(host='localhost', port=28015, db='test')

try:
 #r.db('test').table_create('shows').run(con)
 r.table('shows').insert({ 'name': 'StarTrek' }).run(con)
except RqlRuntimeError as err:
 print(err.message)
finally:
 con.close()
