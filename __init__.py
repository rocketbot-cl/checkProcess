# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
base_path = tmp_global_obj["basepath"]
cur_path = os.path.join(base_path, 'modules', 'checkProcess', 'libs')

import psutil

global find_rocketbot_processes

import os
import platform
import psutil

def find_rocketbot_processes(bot_name=None):
    rocketbot_processes = []
    platform_ = platform.system().lower()
    for process in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        try:
           
            cmdline = process.info['cmdline']
            if bot_name and cmdline and any(bot_name in arg for arg in cmdline):
                rocketbot_processes.append({
                    "pid": process.info['pid'],
                    "name": process.info['name'],
                    "cmdline": cmdline
                })
            elif not bot_name:
                rocketbot_processes.append({
                    "pid": process.info['pid'],
                    "name": process.info['name'],
                    "cmdline": cmdline
                })

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            PrintException()
            continue

    return rocketbot_processes


"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")

if module == "checkProcess":

    try:
        bot_name = GetParams("bot")
        var_ = GetParams("var_")
        processes = find_rocketbot_processes(bot_name)

        if processes:
            SetVar(var_, True)
        else:
            SetVar(var_, False)

    except Exception as e:
        PrintException()
        raise (e)