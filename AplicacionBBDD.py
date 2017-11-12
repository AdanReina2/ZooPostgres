from bottle import *
from lxml import etree
import requests
from sys import argv
import psycopg2, psycopg2.extras

conn = psycopg2.connect(database='pepper',user='jarvis',password='jarvis', host='172.22.200.101')
cur = conn.cursor()
cur.execute("SELECT * FROM ESPECIES")
rows = cur.fetchall()

@route('/')
def consulta():
	return template('resultado.tpl',objeto=rows)

anisinrepe = []
for i in rows:
        if i[4] not in anisinrepe:
                anisinrepe.append(i[4])

@route('/filtroclase')
def filtroclase():
	return template('filtroclase.tpl',objeto=anisinrepe)

@route('/listarclase/<clase>')
def listarclase(clase):
	anienclase = []
	for i in rows:
		if i[4] == clase:
			anienclase.append(i)
	return template('listarclase.tpl',objeto=anienclase)

@route('/todosanimales')
def todosanimales():
        return template('todosanimales.tpl',objeto=rows)

@route('/todosanimales2/<animal>')
def todosanimales2(animal):
	return template('todosanimales2.tpl',objeto=rows,info=animal)

@route('/static/<filepath:path>')
def server_static(filepath):
   return static_file(filepath, root='static')

run(host='0.0.0.0',port=8081)

