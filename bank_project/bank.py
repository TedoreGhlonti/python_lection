import json
import os

from getpass import getpass
DB_FILE = "db.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {"user": {}}
    with open(DB_FILE, "r") as file:
        return json.load(file)
    
def save_db(db):
    with open(DB_FILE, "w") as file:
        json.dump(db, file, indent=2)


def register():
    username = input("Choose username: ").strip()
    if not username:
        print("username can not be empty!")
        return
    db = load_db()
    if username in db["user"]:
        print("That username is already taken.")
        return
    password = getpass("Choose a password")
    if not password:
        print("Password can not be empty!")
        return
    db["user"][username] = {
        "password": password,
        "balance": 0.0,
        "transactions": []
    }
    save_db(db)
    print(f"Account created for '{username}'")

def main():
    while True:
        print("\n=== Simple bank ===")
        print("1. Register")
        print("2. Quit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            register()
        elif choice == "2":
            print("Goodbye!")
            return
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
    