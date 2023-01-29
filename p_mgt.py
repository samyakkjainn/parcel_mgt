import orderMgt
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Admin@1234")
cur=con.cursor()
cur.execute("create database if not exists pms;")
cur.execute('use pms')
cur.execute('''create table if not exists pinfo(pid int primary key,radd varchar(256),rmob char(10),dispatchd date,
pweight int,pamt decimal(10,2),sadd varchar(256),smob char(10));''')
cur.execute('''create table if not exists ratelist(sn int not null primary key auto_increment, wf int ,wt int,rate decimal(10,2)
);''')
while True:
    print('------------WELCOME TO INSTANT PARCEL SERVICES---------------')
    print('here is the list of operations:')
    print("1. ORDER MGT 2. RATE LIST 3. EXIT")
    op=input('enter your choice:  ')
    if op=='1':
        print("1.Placing order\n 2.Search order\n 3.Edit order details\n 4.Display all details\n 5.Delete order")
        cho=input("enter your choice:  ")
        if cho=='1':
            orderMgt.add()
        elif cho=='2':
            orderMgt.search()
        elif cho=='3':
            orderMgt.edit()
        elif cho=='4':
            orderMgt.dispall()
        elif cho=='5':
            orderMgt.delete()
        else:
            print("Wrong choice entered")
    elif op=='2':
        orderMgt.ratelist()
    elif op=="3":
        break
    else:
        print("Invalid Input")    
