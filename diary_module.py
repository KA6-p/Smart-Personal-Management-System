from datetime import datetime
DIARY_FILE = "diary.txt"



def add_notes():
    while True:
        notes = input("Subject: ").title().strip()
        if notes:
            break
        print("Subject cannot be empty!")
    while True:
        entry = input("\nDetails: ").capitalize().strip()
        if entry:
            break
        print("Details cannot be empty!")
        today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DIARY_FILE,'a') as f:
        f.write(f"\n--- {today} ---\n")
        f.write(f"Subject: {notes}\n")
        f.write(f"Entry: {entry}\n")
        f.write("-" * 30 + "\n")

def read_notes():
    try:
        with open(DIARY_FILE,'r') as f:
            content = f.read()
            if content.strip():
                print(content)
            else:
                print("Your diary is empty. Add some notes!")
    except FileNotFoundError:
        print("Diary not found! Add some notes first.")
    except Exception as e:
         print(f"Error reading diary: {e} occured")
         

def clear_notes():
    ans = (input("Are you sure you want to clear all your notes?(Y/N)")).upper()
    if ans == "Y":
        with open(DIARY_FILE,'w') as f:
            f.write("")
            print("All notes Deleted!")

    
    
    
