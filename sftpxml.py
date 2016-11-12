#!/usr/bin/python2
# encoding: utf-8
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
import os
import sys
import pysftp as sftp
from getpass import getpass

def questin():
    try:
        print "Quiere subir Su archivo feed.xml a su Host via sftp s:continuar n:cancelar "
        respsftp=raw_input("s/n: ")
        if respsftp=="s":
            print "Quieres verificar tu archivo primero ? s:continuar n:cancelar"
            catarch=raw_input("s/n: ")
            if catarch=="s":
                os.system("cat feed.xml")
                print "quieres seguir con la subida del archivo a tu host? s:continuar n:cancelar"
                subida=raw_input("s/n: ")
                if subida=="s":
                   datohost() 
                elif subida=="n":
                    print "Bien nos vemos pronto.."
                    sys.exit(0)
            elif catarch=="n":
                print "Sigamos con la subida."
                datohost()
            else:
                print "Necesito una opcion valida para continuar"
                questin()    
        elif respsftp=="n":
            print "Su feed se añadio correctamente a su archivo .xml quiere confirmarlo? s:continuar n:cancelar "
            confirxml=raw_input("s/n: ")
            if confirxml=="s":
                os.system("cat feed.xml")
                sys.exit(0)
            elif confirxml=="n":
                print "Gracias por utilizar el RSSGen Contacteme para ayudarte."
                sys.exit(0)
            else:
                print "Necesito una opcion para continuar."
                questin()
        else:
            print "Necesito una opcion para continuar."
            questin()
    except (KeyboardInterrupt):
        print "Saliendo."
        sys.exit(0)

def datohost():
    try:
        print "Por seguridad Pedire tus datos de tu host sftp"
        print "Introduce El nombre/ip de tu Host sftp"
        global hostname
        hostname=str(raw_input("nombre/ip: "))
        if hostname=="":
            print "El host no puede estar vacio"
        else:
            datosuser()
    except KeyboardInterrupt:
        print "Saliendo."
        sys.exit(0)

def datosuser():
    try:
        print "Introduce el nombre de usuario de tu host para el sftp"
        global hostuser
        hostuser=str(raw_input("User: "))
        if hostuser=="":
            print "El host no puede estar vacio"
        else:
            datoport()
    except KeyboardInterrupt:
        print "Saliendo."
        sys.exit(0)

def datoport():
    try:
        print "Introduce el puerto de tu host sftp"
        global hostport
        hostport=int(raw_input("Puerto: "))
        if hostport=="":
            print "El host no puede estar vacio"
        else:
           datodir()
    except KeyboardInterrupt:
        print "Saliendo."
        sys.exit(0)

def datodir():
    try:
        print "Introduce la direccion del HOST done quieres que vaya el archivo ejemplo: /var/www/html/myweb/feed.xml"
        global hostdir
        hostdir=str(raw_input("Direccion: "))
        if hostdir=="":
            print "El host no puede estar vacio"
        else:
            localdir()
    except KeyboardInterrupt:
        print "Saliendo."
        sys.exit(0)

def localdir():
    try:
        print "Introduce la direccion de tu archivo local EJEMPLO: /home/feed.xml \n"
        print "Si tu archivo local esta en la misma dir que este script solo pon su nombre: feed.xml"
        global dirlocal
        dirlocal=str(raw_input("Direccion LOCAL: "))
        if dirlocal=="":
            print "El host no puede estar vacio"
        else:
            sftpex()
    except KeyboardInterrupt:
        print "Saliendo."
        sys.exit(0)

def sftpex():
    try:
        print "Necesito el password de tu host.(El password no se guardara en ningun lado gracias a la libreria Getpass)"
        hostpasswd = getpass('Password del Host: ')
        s = sftp.Connection(host=hostname, port=hostport, username=hostuser, password=hostpasswd)
        s.put(dirlocal, hostdir)
        s.close()
        print "Tu archivo se subio correctamente. felicidades"
    except Exception, e:
        print ("No se puedo conectar por el siguiente error", str(e))

