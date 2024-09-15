from flask import Flask, render_template, request
from database.db import *
app = Flask(__name__)

@app.route('/register_page')
def register_page():
    return render_template("register.html")

@app.route('/register_user', methods =["post"]) 
def register_user():
    data = request.form
    id, nombre, apellido, documento, area, fecha, horai, horaf, descripcion = data["id"], data["nombre"],data["apellido"],data["documento"], data["area"], data["fecha"], data["horai"], data["horaf"], data["descripcion"]
    insert(id,nombre,apellido,documento,area,fecha,horai,horaf,descripcion)
    #return "User added"  
    alert ("Actividad Guardada con éxito");
    return render_template("register.html")

if __name__=="__main__":
    host ="0.0.0.0"
    port=80
    app.run (host,port,True)