import pymysql

host= inst-db-15.c9i8cw4265h0.us-east-2.rds.amazonaws.com
user= yale
passw= Yaleaws2024
db_name=db_user

def connection_SQL()
    try
        connection= pymysql.connect(
            host=host,
            user=user,
            password=passw,
            database=db_name
        )   
        print (Succesfull connection to database)
        return connection
    except Exception  as err
         print (Error, err)
         return None
