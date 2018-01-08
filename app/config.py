import os

class config():
    
    def __init__(self,app):   

        #app 
        app.debug = True
        app.secret_key = os.urandom(23)



        config = {

            # Config Mail 
            'MAIL_SERVER'   : 'smtp.gmail.com',
            'MAIL_PORT'     : 465,
            'MAIL_USERNAME' : 'youremail@gamil.com',
            'MAIL_PASSWORD' : 'passwordEmail',
            'MAIL_USE_TLS'  : False,
            'MAIL_USE_SSL'  : True,


            #JSON
            "token_file"         : "app/Json/token.json",

            #DB
            "DB:SQLite"     : "app/Databases/dbite/db.sql",

        }



        app.config.update(config)
        


