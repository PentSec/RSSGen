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

#librerias necesarias
import datetime
import os
import sys
from copy import copy
from copy import deepcopy
#mira el README.MD y mira lo que falta.
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup, Tag, NavigableString, CData

#esto pondra la hora en el RSS.
datos = datetime.datetime.now()
dato = str(datos)[:10]

#configura la url por la tuya justo donde se guardan los post. a post me refiero al python-gen-xml-post.html .
url="https://pentsec.github.com/blog/post/"

#Puedes editarlo aqui o simplemente lo editas despues de que se cree el archivo. :D.
config = \
    '''
<?xml version="1.0" encoding="ISO-8859-1" ?> 
<rss version="2.0">
<channel>
<title>PentSecBLOG</title> 
<link>https://pentsec.github.io/blog</link> 
<description>En este Blog podras encontrar varia informacion importante
</description> 
<language>es-ES</language>

<item>
<title>My primer RSS</title>
<link>https://pentsec.github.com/blog/asd</link>
<guid>TEST</guid>
<pubdate>TEST</pubdate>
<description><![CDATA[My desc]]></description>
</item>

</channel></rss>
'''
#De aqui en adelante es preferible que no edites nada si no sabes lo que haras.
def logo():
    print """
--------------------------------------------------
  _____   _____ _____        _____            
 |  __ \ / ____/ ____|      / ____|           
 | |__) | (___| (___ ______| |  __  ___ _ __  
 |  _  / \___ \\___ \______| | |_ |/ _ \ '_ \ 
 | | \ \ ____) |___) |     | |__| |  __/ | | |
 |_|  \_\_____/_____/       \_____|\___|_| |_|
                                              
                                              
   Este codigo esta hecho por PentSec.
        Email: pentsec@cock.li
     web: https://pentsec.github.io   
--------------------------------------------------                        
"""

def genxml():
    print "Este Programa te Generara Autamaticamente tus RRS y te creara un archivo en estara en la misma direccion.\n"

def checkxml():
    try:
        xmlf=("feed.xml")
        isxmlf=os.path.isfile(xmlf)
        if isxmlf:
            return xmlf
        else:
            print "no tienes el archivo RSS. Desea crearlo? s:para continuar  n:para cancelar"
            pregunta=raw_input("S/N: ")
            if pregunta == "s":
                xmlfile = open('feed.xml', 'w')
                xmlfile.write(config)
                xmlfile.close()
                print "Su Archivo fue creado."
            elif pregunta == "n":
                print "Esperemos que busque su archivo y lo renombre :D"
                sys.exit(0)
            else:
               print "Hasta luego, Necesito una Opcion Valida para continuar. Vuelve a ejecutarme"
               sys.exit(0)
    except KeyboardInterrupt:
        print "Saliendo."
        pass
            
try:
    logo()
    print ""
    checkxml()
    print ""
    genxml()
    def pagetitu():
        global titulo
        print "Escribe el titulo de tu Feed"
        titulo=raw_input("Titulo: ")
        if titulo=="":
            print "El campo no puede estar vacio."
            pagetitu()
        else:
           postitulo()
    def postitulo():
        global postitu
        print "Escribe el archivo de tu post ejemplo: xml-gen.html"
        postitu=raw_input("archivo.html: ")
        if postitu=="":
            print "El campo no puede estar vacio."
            postitulo()
        else:
            descript()
    def descript():
        global desc
        print "Escribe aqui la Descripcion de tu Feed"
        desc=raw_input("Descripcion: ")
        if desc=="":
            print "El campo no puede estar vacio."
            descript()
        else:
            seguroxd()
    def seguroxd():
        global seguro
        print "ESTAS SEGURO QUE QUIERES AÑADIR ESTE FEED? s:continuar n:cancelar (y comenzar de nuevo xd)"
        seguro=raw_input("s/n: ")
        if seguro=="s":
            pass
        elif seguro=="n":
            print "Ok tienes otra oportunidad para mejorar tu Feed"
            pagetitu()
        else:
            print "SIEMPRE tienes que meter la opcion correcta.!! Adios"
            sys.exit(0)
    pagetitu()
except (KeyboardInterrupt):
    print "Saliendo."
    pass

def gen_xml(record):

    descrip = \
    '''
    <item>
    <title>feed titulo</title>
    <link>link para entrar</link>
    <pubDate>2016-11-09 22:41:24.776136</pubDate>
    <description>[CDATA[ Esta es la descripcion. ]]</description>
    </item>
    '''
    descripxml = BeautifulStoneSoup(descrip)

    keylocal = \
    [
        ("title", lambda x: x.name == u"title"),
        ("link", lambda x: x.name == u"link"),
        ("pubDate", lambda x: x.name == u"pubdate"),
        ("description", lambda x: x.name == u"description")
    ]

    tmpdescriphandle = deepcopy(descripxml)

    for (key, location) in keylocal:
        slist = tmpdescriphandle.findAll(location)
        if(not slist):
            continue
        tag_handle = slist[0]
        tag_handle.clear()
        if(key == "description"):
            tag_handle.insert(0, CData(record[key]))
        else:
            tag_handle.insert(0, record[key])

    return tmpdescriphandle

test_dict = \
{
    "title" : titulo,
    "link" : url +postitu,
    "pubDate" : dato,
    "description" : desc
}
ch = ("</channel>")
rs = ("</rss>")
f = str(gen_xml(test_dict))
impr = open('feed.xml', 'r')
algo = impr.read()
impr.close()
inicia = algo.find("</channel>")
finaliza = algo.find("</rss>")
algo = algo.replace(algo[inicia:finaliza+6], f)
kasd = open('feed.xml', 'w')
kasd.write(algo)
kasd.close()
asd = open('feed.xml', 'a+')
asd.write(ch)
asd.write(rs)
asd.seek(0)
asd.close()
print "Se añadio el Feed satisfactoriamente puedes ver el archivo feed.xml para confirmarlo"
