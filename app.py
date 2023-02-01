import mariadb
import dbcreds

# 1. Connecting to the DB
conn = mariadb.connect(
                        user = dbcreds.user,
                        password = dbcreds.password,
                        host = dbcreds.host,
                        port = dbcreds.port,
                        database = dbcreds.database,
                        autocommit = True
                        )
# 2.Creating a cursor object
cursor = conn.cursor()

# !Gets sales peoples names and id
def sales_people():
    cursor.execute("CALL select_names_id()")
    result = cursor.fetchall()
    print("Select from the following: ")
    for person in result:
        # print(person) - > this also prints, but with a 'string' around the names
        print("{}.{}".format(person[0], person[1]))   
    selection = input("Your selection: ")
    return selection

# !Gets items name, id, price
def get_items():
    cursor.execute("CALL items()")
    result = cursor.fetchall()
    print("Select from the following: ")
    for item in result:
        print("{}.{}. Price : {}".format(item[0], item[1], item[2]))
    selection = input("Your selection : ")
    return selection

# !lets user make a sale
def make_sale(person : int):
    item = get_items()
    cursor.execute("CALL make_sale(?,?)", [item, person])

# !.....................................................................................
# !Function that runs the script
def main():
    print("Welcome, select from the following:")
    while True:
        print("1. Buy new item")
        print("2. Exit the application")
        slection = input("Make a selection : ")
        if slection == "1":
            person = sales_people()
            make_sale(person)
        elif slection == "2":
            break
        else:
            print("Please choose 1 or 2")

# Calling the script function
main()