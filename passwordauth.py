import getpass
database = {"clcoding": "976729", "pythoncloding": "2502"}
username = input ("Enter your Username:")
password = getpass.getpass("Enter Your Password: ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again: ")
        break
print("Verified")
