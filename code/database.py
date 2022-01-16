from tinydb import TinyDB, Query

db = TinyDB('db.json')
UserQuery = Query()

def create_user(username: str, password: str):
    if get_user(username) is None:
        db.insert({'username': username, 'password': password, 'sessions': []})
        return True
    return False

def get_user(username:str):
    result = db.search(UserQuery.username == username)
    if (len(result)):
        return result[0]

def add_session(username: str, n: int):
    sessionsArray = db.search(UserQuery.username == username)['sessions']
    sessionsArray = sessionsArray.append(n)
    db.update({'sessions': sessionsArray}, User.username == username)