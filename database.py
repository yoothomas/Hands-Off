import psycopg2

conn = psycopg2.connect(

'postgresql://santiago:8uO6KQi4WDchNsGs@free-tier4.aws-us-west-2.cockroachlabs.cloud:26257/pythondb?sslmode=verify-full&sslrootcert=/home/aptaabye/.postgresql/root.crt&options=--cluster%3Djumbo-hare-2182'
)

conn.set_session(autocommit=True)

cur = conn.cursor()

def create_user(username: str, password: str):
    if get_user(username) is None:
        cur.execute("INSERT INTO users (username, password) VALUES ('"+username+"', '"+password+"')")
        return True
    return False

def get_user(username:str):
    result = None
    try:
        cur.execute("SELECT username, password FROM users WHERE username = '" + username + "'")
    except:
        print('excepted 1')
    try:
        result = cur.fetchall()
    except:
        print('excepted 2')
    if (result is not None):
        if(not (result == [])):
            return result[0]

def add_session(username: str, n: int):
    cur.execute("UPDATE users SET sessions = "+n+" WHERE username = "+username)
