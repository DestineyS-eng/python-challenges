#input username 
username=input("enter your username")
#checks if its not empty or contains spaces 
#if it is an error message is outputed and program is exited 
if username.strip()=="" or " " in username:
    print("error:invalid username")
    exit()
#otherwise file is edited closed and confirmation of log is shown 
else:
    with open("security_log.txt","a") as file:
        file.write(f"{username} successfully logged in.\n")
    print("Log updated")
