#1. Create a file named mydata2.txt
#2. Open the file without with
#3. Catch FileNotFoundError
#4. In else print contents
#5. In finally 
#6. Open nonexistent file mydata3.txt

try:
    f = open("mydata2.txt", encoding="utf-8")

except FileNotFoundError as ex:
    print("File not found")
    print(ex.args)
else:
    print("File found:", f.read())
    f.close()
finally:
    print("Have a nice day")