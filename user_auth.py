import hashlib
USERS_FILE = "users.txt"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(username, password):
    hashed_password = hash_password(password)

    # Read existing users
    with open(USERS_FILE, 'r') as file:
        users = file.readlines()

    # Check if username already exists
    for user in users:
        if ":" not in user:
            continue
        saved_name, saved_password = user.strip().split(":")
        if saved_name == username:
            print("Username already taken!")
            return False

    # Register new user with hashed password
    with open(USERS_FILE, 'a') as file:
        file.write(f"{username}:{hashed_password}\n")

    print(f"{username} successfully registered!")
    return True
    
def login(username,password):
    hashed_password = hash_password(password)
    try:
        with open(USERS_FILE,'r') as file:
            users = file.readlines()
            for user in users:
                if ":" not in user:
                    continue
                saved_name,saved_password = user.strip().split(":")
                if saved_name == username and saved_password == hashed_password:
                      print(f"Welcome {username}")
                      return True
            print("Invalid username or password")
            return False
        
    except FileNotFoundError:
        print("User not registered. Sign Up!")



