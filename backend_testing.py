from db_connector import createUser
import requests
import pymysql

schema_name = "mydb"
# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3307, user='user', passwd='password', db=schema_name)

async def addUser(user_id) :
    res = requests.post(f'http://127.0.0.1:5000/users/{user_id}',json={'username': 'ready made'})
    if res.ok:
        print(res.json())
    return 'my user'


async def getUser(user_id) :
    res = requests.get(f'http://127.0.0.1:5000/users/{user_id}')
    if res.ok:
        print(res.json()['user_name'])
        print(res.status_code)
        return {'status_code': res.status_code, 'username': res.json()['user_name']}


async def verifyUsername(user_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {schema_name}.users WHERE user_name = '{user_name}'")

    user = cursor.fetchone()
    cursor.close()

    return user[1]


print(verifyUsername(7))