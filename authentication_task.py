def Registration_Login():
    d={}
    while True:
        choice=input("What do yo want:")
        if choice=='signup':
            name=input("enter the name :")
            
            email=input("enter the email:")
            if email in [i.get('email',None) for i in d.values()]:
                print("gmail is already exist !!!!!!")
             
            else:
                
                password=int(input("enter the password:"))
                confirm_password=int(input("enter the confirm password:"))
                
                if password!=confirm_password:
                    print("your password and confirm password is not matched !!!!!")
                   
                else:
                    d[name]={}
                    d[name]['email']=email
                    d[name]['password']=password
                    d[name]['confirm_password']=confirm_password
                    print("Your Registraion is successfully done.......")
                    print(d)
               
        elif choice=='signin':
            email=input("enter the gmail :")
            password=int(input("enter the password:"))
        
            for key,values in d.items():
                if values['email'] == email: 
                    if values['password'] == password:
                    
                        print("Your Login is successfully done.......")
                        break
                    else:
                        print("password is wrong")
                if email not in d:
                    print("email is not exits")
                    break
               

    return d
registration=Registration_Login()

print(registration)







