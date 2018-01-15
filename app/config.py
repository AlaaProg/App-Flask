# -*- coding: utf-8 -*-

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
            'MAIL_USERNAME' : 'mail@gmail.com',
            'MAIL_PASSWORD' : 'password',
            'MAIL_USE_TLS'  : False,
            'MAIL_USE_SSL'  : True,


            #JSON
            "token_file"         : "app/DB/Json/token.json",
            "DB:Json"            : "app/DB/Json/data.json",

            #DB
            "DB:SQLite"     : "app/DB/dbite/db.sql",
            "DB:MySQL"      : { 

                                "user"      :"root",
                                "host"      :"localhost",
                                "database"  :"test",
                                "password"  :"" 

                            }

        }


        app.config.update(config)
