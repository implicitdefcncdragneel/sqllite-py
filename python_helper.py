import  sqlite3 as lite




class DatabaseManage(object):

    def __init__(self):
        global con
        try:
            con=lite.connect('databse.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXITS customer(Id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,description TEXT,price TEXT,is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create a DB !")


    # TODO create data
    def insert_data(self,data):
        try:
            with con:
                cur =con.cursor()
                cur.execute(
                    "INSERT INTO customer(name,add,age,gender) VALUES (?,?,?,?)" ,data
                )
                return True
        except Exception:
            return False
    # TODO read data
    def fetch_data(self):
        try:
            with con:
                cur=con.cursor()
                cur.execute("SELECT * FROM courses")
                return cur.fetchall()
        except Exception:
            return False

    # TODO delete data
    def delete_data(self,id):
        try:
            with con:
                cur=con.cursor()
                sql = "DELETE FROM customer where id = ?"
                cur.execute(sql,[id])
                return True
        except Exception:
            return False



#TODO provide user interface
def main():
    print("*"*40)
    print("\n:: CUSTOMER MANAGEMENT ::\n")
    print("*"*40)
    print("\n")

    db=DatabaseManage()
    
    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)


    print('\nPress 1. Insert a new customer')
    print('\nPress 2. Show all customer')
    print('\nPress 3. Delete a customer( NEED ID OF COURSE )\n')
    print('#'*40)
    print('\n')

    choice =input("\n Enter a choice:")

    if choice == "1":
        name =input("\n Enter custome name:")
        add =input("\n Enter address of the customer:")
        age =input("\nEnter customer age:")
        gen=input("\n Gender (M/F):")

        if db.insert_data([name,add,age,gen]):
            print("Customer was inserted successfully ")
        else:
            print("OOPS Something Went Wrong")
        
    elif choice == "2":
        print("\n :: Customer List ::")

        for index,item in enumerate(db.fetch_data()):
            print("\n SL no:"+str(index+1))
            print("\n ID no:"+str(item[0]))
            print("\n Customer Name:"+str(item[1]))
            print("\n Customer Address"+str(item[2]))
            print("\n Customer Age"+str(item[3]))
            private="Male" if item[4] else "Female"
            print("Gender :"+ private)
            print("\n")

    elif choice =="3":
        customer_id= input("Enter the customer ID:")

        if db.delete_data(customer_id):
            print("Customer record was deleeted ")
        else:
            print("Invalid Option")

    else:
        print("Invalid Option")



if __name__ == '__main__':
    main()
