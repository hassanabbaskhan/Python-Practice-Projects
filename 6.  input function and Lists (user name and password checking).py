#make a form and ask the user to put username and password correctly so that the next procedure may be followed ahead.
#taking user inputs of username and password

username=input("Enter user name \n")
password=input("Enter password \n")
data=["hassan","abc123"]     #stored_user_info_name_password
if username==data[0] and password==data[1]:
    print("Qualified for next procedure")
elif username!=data[0] and password==data[1]:
    print("incorrect username, re-try")
elif username==data[0] and password !=data[1]:
    print("Forget password?")
else:
    print("username and password are incorrect")
