from db_connector import fetchUser

def webUserUI(user_id):

    user_name = fetchUser(user_id)
    if user_name[1] == 200:

         return "<h1 id='user'> Hello " + user_name[0]['user_name'] + "</h1>"
    else:
         return "<h1 id='error' style='color:red'> No such user: " + user_id + "</h1>"