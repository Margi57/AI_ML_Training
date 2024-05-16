import mysql.connector as cnt

db=cnt.connect(
    host='localhost',
    user='root',
    password='Root@1234',
    database='Employee'
)
mycursor=db.cursor()
table="CREATE table employee(e_id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),experiance INT)"
mycursor.execute(table)


def insert():
    name=input("Enter name:")
    experiance=int(input("Enter experiance:"))
    val=(name,experiance)
    sql="Insert INTO employee(name,experiance) VALUES(%s,%s)"
    mycursor.execute(sql,val)
    db.commit()


def update():
    id=int(input("select in wich id you want change data:"))
    show()
    name=input("Enter name:")
    experiance=int(input("Enter experiance:"))
    val=(name,experiance,id)
    sql="UPDATE employee SET name=%s,experiance=%s WHERE e_id=%s"
    mycursor.execute(sql,val)
    db.commit()
    show()


def delete():
    id=int(input("select in wich id you want delete data:"))
    val=(id,)
    sql="DELETE FROM employee WHERE e_id=%s"
    mycursor.execute(sql,val)
    db.commit()
    show()

def show():
    sql="SELECT * FROM employee"
    mycursor.execute(sql)
    for i in mycursor:
        print(i)




def main():
    while True:
        print("------------------------")
        print("1.Insert Data\n"
              "2.Update Date\n"
              "3.Delete Data\n"
              "4.Display Data\n"
              "5.Exit")
        choice=int(input("Choose any one opration:"))
        if choice==1:
            insert()
        elif choice==2:
            update()
        elif choice==3:
            delete()
        elif choice==4:
            show()
        elif choice==5:
            print("exit")
            break

        
        

if __name__=="__main__":
    main()

