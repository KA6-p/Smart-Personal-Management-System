file_path = "users.txt"

def register(username,password):
        
        with open(file_path,'r') as file:
            users = file.readlines()
            for user in users:
                if ":" not in user:
                    continue
                saved_name,saved_password = user.strip().split(":")
                if saved_name == username and saved_password == password:
                    print(f"User Already registered!")
                    return True
            with open(file_path,'a') as file:
                file.write(f"{username}:{password}\n")  
                print(f"{username} successfully registered!")
                return True 
            
    
def login(username,password):
    try:
        with open(file_path,'r') as file:
            users = file.readlines()
            for user in users:
                if ":" not in user:
                    continue
                saved_name,saved_password = user.strip().split(":")
                if saved_name == username and saved_password == password:
                      print(f"Welcome {username}")
                      return True
            print("Invalid username or password")
            return False
        
    except FileNotFoundError:
        print("User not registered. Sign Up!")



