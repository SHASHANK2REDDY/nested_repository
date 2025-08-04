import mysql.connector
var1=mysql.connector.connect(host="localhost",
user="root",
password="1309")
obj1=var1.cursor()
obj1.execute("create database siva")
var1.commit()
var1.close()