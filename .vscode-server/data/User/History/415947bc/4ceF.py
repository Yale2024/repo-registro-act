import pymysql

host= "inst-db-registroact.c9i8cw4265h0.us-east-2.rds.amazonaws.com"
user= "registroact"
passw= "registroact123"
db_name="db_RegistrosAct"

def connection_SQL():
    try:
        connection= pymysql.connect(
            host=host,
            user=user,
            password=passw,
            database=db_name
        )   
        print ("Succesfull connection to database")
        return connection
    except Exception  as err
         print (Error, err)
         return None
