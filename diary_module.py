from datetime import date
file_path = "diary.txt"



def add_notes():
    notes = (input("Subject: ")).title()
    entry = (input("\nDetails: ")).capitalize()
    today = date.today()
    with open(file_path,'a') as f:
        f.write(f"{today}\n{notes}\n{entry}\n")

def read_notes():
    with open(file_path,'r') as f:
        try:
            print(f.read())
        except FileNotFoundError:
            print("Diary not found!...Add notes")


def clear_notes():
    ans = (input("Are you sure you want to clear all your notes?(Y/N)")).upper()
    if ans == "Y":
        with open(file_path,'w') as f:
            f.write("")
            print("All notes Deleted!")

    
    
    
