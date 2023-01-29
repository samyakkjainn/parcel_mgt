import mysql.connector
from tabulate import tabulate
con=mysql.connector.connect(host="localhost",user="root",password="Admin@1234",database="pms")
cur=con.cursor()

def add():
    while True:
            cur.execute("select max(pid) from pinfo;")
            pid=cur.fetchone()[0]
            if pid:
                pid=pid+1;
            else:
                pid=301
            pamt=0
            radd=input("Enter Receiver's Address(with name):")
            rmob=input("Enter Receiver's Mobile No:")
            pweight=int(input("Enter the weight of the parcel(in kg):"))
            if (pweight>0 and pweight<=5):
                pamt=pamt+(pweight*50)
            elif (pweight>5 and pweight<=10):
                pamt=pamt+(pweight*70)
            elif pweight>10:
                pamt=pamt+(pweight*100)
            else:
                print("Invalid Input")
                break
            print("Total payable amount is",pamt)
            ch=input("You want to proceed(Y/N)")
            if ch in['Y', 'y']:
                sadd=input("Enter Sender's address(with name):")
                smob=input("Enter sender's Mobile No:")
                cur.execute("insert into pinfo values({},'{}','{}',curdate(),{},{},'{}','{}');".format(pid,radd,rmob,pweight,pamt,sadd,smob))
                con.commit()
                print("Parcel Information added successfully!")
            status=input("Do you want to proceed another records(Y/N):\t")
            if status in ['n','N']:
                break


def search():
        pid=int(input("Enter Packet Id whose information is to be searched:"))
        print()
        cur.execute("select * from pinfo where pid={};".format(pid))
        rec=cur.fetchall()
        if rec:
            print(tabulate(rec,headers=["pid","radd","rmob","dispatchd date","pweight","pamt","sadd","smob"],tablefmt="psql"))
            print()
        else:
            print("Record not found for the entered Packet Id!")
        print()


def edit():     
        pid=int(input("Enter Packet Id whose information is to be edited:"))
        print()
        cur.execute("select * from pinfo where pid={};".format(pid))
        rec=cur.fetchall()
        if rec:
            print(tabulate(rec,headers=["pid","radd","rmob","dispatchd date","pweight","pamt","sadd","smob"],tablefmt="psql"))
            print()
            smob=input("Enter updated Mobile No of Sender:")
            rmob=input("Enter updated Mobile No of receiver:")
            cur.execute("update pinfo set smob='{}',rmob='{}' where pid={};".format(smob,rmob,pid))
            con.commit()
            print()
            print("Information for entered Packet Id is edited successfully!")
            print()
        else:
            print("Record not found for the entered Packet Id!")
            print()


def dispall():
        cur.execute("select * from pinfo;")
        rec=cur.fetchall()
        if rec:
            print(tabulate(rec,headers=["pid","radd","rmob","dispatchd date","pweight","pamt","sadd","smob"],tablefmt="psql"))
            print()
        else:
            print("Table is empty:No record found!")
            print()

            
def delete():
        pid=int(input("Enter Packet Id whose information is to be deleted:"))
        print()
        cur.execute("select * from pinfo where pid={};".format(pid))
        rec=cur.fetchall()
        if rec:
            print(tabulate(rec,headers=["pid","radd","rmob","dispatchd date","pweight","pamt","sadd","smob"],tablefmt="psql"))
            print()
            cur.execute("delete from pinfo where pid={};".format(pid))
            con.commit()
            print("Information  for the entered Packet Id is deleted successfully!")
            print()
        else:
            print("Record not found for the entered Packet Id!")
            print()

def load():
    cur.execute("select * from ratelist;")
    rec=cur.fetchall()
    if rec:
        pass
    else:
        cur.execute("insert into ratelist(wf,wt,rate) values(1,5,50.00);")
        cur.execute("insert into ratelist(wf,wt,rate) values(6,10,70.00);")
        cur.execute("insert into ratelist(wf,wt,rate) values(11,100,100.00);")
        con.commit()
        print()
load()


def ratelist():
    cur.execute("select * from ratelist;")
    rec=cur.fetchall()
    if rec:
        print(tabulate(rec,headers=["S.No.","Weight From(in Kg)","Weight To(in Kg)","Price(Per Kg)"],tablefmt="psql"))
        print()
