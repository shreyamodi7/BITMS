email="shreya@gmail.com"
pwd=123456
uemail=str(input("Enter the email"))
upwd=int(input("Enter pwd"))
if(email==uemail):
    if(pwd==upwd):
        print("login success")
    else:
        print("Login failed due to incorrect pwd")
else:
    print("login failed due to incorrect email")