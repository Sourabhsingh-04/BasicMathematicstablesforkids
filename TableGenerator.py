print("Welcome to Mathematics Table Generator".center(50))
while True:
    a = int(input("Enter the number: "))
    for i in range (10):
      print(a,"x",i+1,"=",a*(i+1))

    w = input("You want to proceed [yes/no]: ")
    if w == "yes":
       continue
    else:
       print("Thanks for using .......")
       break