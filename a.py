import os,time,json

os.system("cls")


def cargar_json(url_archivo):
    with open(url_archivo, 'r') as archivo:
        return json.load(archivo)

def iniciar_programa():
    empleados = cargar_json('empleado.json')
    print(empleados)

iniciar_programa()