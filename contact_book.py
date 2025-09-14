import json
import os
CONTACTS_FILE = "contacts.json"
def load_contacts():
    global contacts
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE,"r") as f:
            contacts = json.load(f)
    else:
     contacts = {}

def save_contacts():
    with open(CONTACTS_FILE,"w") as f:
        json.dump(contacts,f,indent = 4)         

def add_contact(name,phone,email,address):
    global contacts
    contacts[name] = {"phone": phone,"email": email,"address":address}
    save_contacts()
    print(f"Contact {name} added Successfully!")

def view_contact(name):
    global contacts
    if name in contacts:
        contact = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
    else:
        print(f"Contact '{name}' not found!")

def update_contact(name,phone = None,email = None,address = None):
    global contacts
    if name in contacts:
        contact = contacts[name]
        if phone:
            contact["phone"] = phone
        if email:
            contact["email"] = email
        if address:
            contact["address"] = address
        save_contacts()    
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found!")

def delete_contact(name):
    global contacts
    if name in contacts:
        del contacts[name]
        save_contacts()
        print(f"Contact '{name} deleted successfully!")
    else:
         print(f"Contact '{name}' not found!")
load_contacts()



