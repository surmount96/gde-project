from flask import Flask, request, render_template
from web_app import webUserUI
from db_connector import createUser, fetchUser,deleteUser,updateUser

app = Flask(__name__)

@app.route('/users/<user_id>', methods=['GET','POST','PUT','DELETE'])
def user(user_id):
    if request.method == 'GET':
        response = fetchUser(user_id)
        return response

    elif request.method == 'POST':
        response = createUser(request.json.get('username'),user_id)
        return response

    elif request.method == 'PUT':
        response = updateUser(request.json.get('username'),user_id)
        return response

    elif request.method == 'DELETE':
        response = deleteUser(user_id)
        return response



@app.route('/users/get_user_data/<user_id>')
def getUser(user_id):
    return webUserUI(user_id)
    # return render_template('index.html', content ='Hello world')

app.run('127.0.0.1',port=5000)