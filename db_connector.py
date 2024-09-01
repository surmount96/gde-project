import pymysql
from datetime import datetime

schema_name = "mydb"
# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3307, user='user', passwd='password', db=schema_name)

def fetchUser(user_id):
    user = {}

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {schema_name}.users WHERE user_id = '{user_id}'")

    user = cursor.fetchone()
    cursor.close()

    if user is None:
        return {"status": "error", "reason": "no such id"},  500
    else:
        return {"status": "ok", "user_name": user[1]}, 200


def createUser(username,user_id):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")

    try:
        cursor = conn.cursor()
        conn.autocommit(True)

        cursor.execute(f"INSERT INTO {schema_name}.users (user_id, user_name, creation_date) VALUES ('{user_id}','{username}','{date}');")
        cursor.close()
        conn.close()
        return {"status": "ok", "user_added": username}, 200

    except pymysql.DatabaseError as e:
        error = {}

        error_code,error_message = e.args

        if error_code == 1062 :
            error = {"status": "error", "reason": "id already exists"}
        return error,  500


def updateUser(username,user_id):

    try:
        cursor = conn.cursor()

        conn.autocommit(True)
        cursor.execute(f"UPDATE {schema_name}.users SET user_name = '{username}' WHERE user_id = '{user_id}'")

        cursor.close()
        conn.close()
        return {"status": "ok", "user_updated": username}, 200
    except Exception as e:
        error_code,error_message = e.args
        if error_code == 0:
            return {"status": "error", "reason": "no such id"},  500



def deleteUser(user_id):
    try:
        cursor = conn.cursor()
        conn.autocommit(True)
        cursor.execute(f"DELETE FROM {schema_name}.users WHERE user_id = '{user_id}'")

        cursor.close()
        conn.close()

        return {"status": "ok", "user_deleted": user_id}, 200
    except Exception as e:
        error_code, error_message = e.args
        print(error_code)
        if error_code == 0:
            return {"status": "error", "reason": "no such id"}, 500
