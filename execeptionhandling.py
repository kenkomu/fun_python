# try:
#     alist = [1,2,3]
#     print(alist[3])
# except IndexError:
#     print("Sorry that index doesn't exist")
# except:
#     print("An unknown error occurred")

  #CUSTOMS EXECPTIONS
# class DognameError(Exception):
#     def __init__(self,*args,**kwargs):
#         Exception.__init__(self,*args,**kwargs)
# try:
#     dogName = input("what is the dogs name:")
#     if any (char.isdigit() for char in dogName):
#         raise DognameError
# except DognameError:
#     print("name contains digits")


num1, num2 = input("Enter the 2 values to divide").split()
try:
    quotient = int(num1) / int(num2)
    print("{} / {} = {}".format(num1,num2,quotient))

except ZeroDivisionError:

    print("You can't divide by zero")

else:
    print("You didn't raise any execption")

finally:
    print("Thanks for attempting")