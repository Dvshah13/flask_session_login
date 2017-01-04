import pg

db = pg.DB(host="localhost", user="postgres", passwd="rockets", dbname="users")
db.debug = True


# db.insert('users', id = 3, username = 'Deepak', password = 'test')
db.insert('users', username = 'Hello', password = 'hello')
db.insert('users', username = 'Paul', password = 'paul123')
db.insert('users', username = 'Test', password = 'work')
# db.update('users', id = 1, username = 'Deepak', password = 'test')
# db.update('users', id = 2, username = 'Get', password = 'get')
