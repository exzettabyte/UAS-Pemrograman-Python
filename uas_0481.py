import mysql.connector
import requests
import json
import os
from tabulate import tabulate


db = mysql.connector.connect(
	host="localhost",
	user="administrator",
	password="Admin123!@#",
	database="db_akademik_0481"
)

def fetchnstore():
	url = "https://api.abcfdab.cfd/students"
	res = requests.get(url)
	parsing =  json.loads(res.text)
	hasil = parsing['data']
	cursor = db.cursor()
	sql = "INSERT INTO tbl_students_0481 (id, nim, nama, jk, jurusan, alamat) VALUES (%s, %s, %s, %s, %s, %s)" 
	for row in hasil:
		data = (row['id'],row['nim'],row['nama'],row['jk'],row['jurusan'],row['alamat'])
		cursor.execute(sql,data)
	db.commit()
	print("[Successfully Stored]\n")

def show_all():
	cursor = db.cursor()
	sql = "SELECT * FROM tbl_students_0481"
	cursor.execute(sql)
	res = cursor.fetchall()
	print(tabulate(res,headers=["NO","NIM","Nama","JK","Jurusan","Alamat"],tablefmt='pretty'))

def with_limit():
	try:
		cursor = db.cursor()
		number = int(input("Masukkan Limit : "))
		sql = "SELECT * FROM tbl_students_0481 LIMIT %s" % (number)
		cursor.execute(sql)
		res = cursor.fetchall()
		print(tabulate(res,headers=["NO","NIM","Nama","JK","Jurusan","Alamat"],tablefmt='pretty'))
	except:
		print("\n[INVALID !]\n")

def with_nim():
	try:
		cursor = db.cursor()
		value = input("Masukkan NIM : ")
		sql = "SELECT * FROM tbl_students_0481 WHERE nim = '%s'" % (value)
		cursor.execute(sql)
		res = cursor.fetchall()
		if not res:
			print(f"Data {value} tidak ditemukan!")
			print(tabulate([["NA","NA","NA","NA","NA","NA"]], headers=["NO","NIM","Nama","JK","Jurusan","Alamat"],tablefmt='pretty'))
		else:
			print(f"Data {value} ditemukan!")
			print(tabulate(res,headers=["NO","NIM","Nama","JK","Jurusan","Alamat"],tablefmt='pretty'))
	except:
		print("\n[INVALID !]\n")
		

def menu():
	print("1. Tampilkan semua data")
	print("2. Tampilkan data berdasarkan limit")
	print("3. Cari data berdasarkan NIM")
	print("0. Keluar")

def main():
	#fetchnstore()
	while True:
		menu()
		pilihan = int(input("Pilih menu> "))
		if pilihan == 1:
			show_all()
		elif pilihan == 2:
			os.system('clear')
			with_limit()
		elif pilihan == 3:
			os.system('clear')
			with_nim()
		elif pilihan == 0:
			break
		else:
			print("\n[INVALID !]\n")
		

if __name__ == '__main__':
	main()