import webbrowser

# Objeto 'Cliente'

class cliente():       #DEBE SER UNA CLASE, NO UN MÉTODO
    
    def __init__(self, nombre, edad, activo, saldo):    
        self.nombre=nombre
        self.edad=edad
        self.activo=activo
        self.saldo=saldo


# Lista de clientes

clientes=[]

clientes.append(cliente("Pedro Gonzales",45,True,560))
clientes.append(cliente("Nicolas Uriel",35,False,140))
clientes.append(cliente("Sara Gonzo",66,True,5))
clientes.append(cliente("Nehemias Urquizu",27,True,560))
clientes.append(cliente("Sofia Lara",45,False,1200))
clientes.append(cliente("Tomas Wayne",21,False,40))
clientes.append(cliente("Paola Solola",40,True,112))
clientes.append(cliente("Fernando Xicay",42,True,989))
clientes.append(cliente("Rodrigo Hernan",21,False,105))
clientes.append(cliente("Pablo Cabrera",19,True,35))


# Archivo HTML

html_file=open('index.html','w')

html_file.write("""<!DOCTYPE html>
<html>
    <head>
        <title>Pagina HTML</title>
        <style>
            body{
                background-color:darkslategray;
            }
            div{
                background-color:black;
            }
            h2{
                color:white;
            }
            p{
                color:lightblue;
            }
        </style>
    <head>

    <body>

""")

for cliente in clientes:
    html_file.write("""       <div>
            <h2>Nombre: """+cliente.nombre+"""</h2>
            <p>Edad: """+str(cliente.edad)+"""</p>
            <p>Usuario activo: """+str(cliente.activo)+"""</p>
            <p>Saldo: """+str(cliente.saldo)+"""</p>
        </div>

""")

html_file.write("""    </body>
</html>""")


# Abrir el archivo HTML

webbrowser.open('index.html')