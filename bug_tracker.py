import json
import os
from datetime import datetime

FILE_NAME = "bugs.json"

def load_bugs():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_bugs(bugs):
    with open(FILE_NAME, "w") as file:
        json.dump(bugs, file, indent=4)

def add_bug():
    bugs = load_bugs()

    title = input("Enter bug title: ")
    description = input("Enter bug description: ")
    priority = input("Enter priority (Low/Medium/High): ")

    bug = {
        "id": len(bugs) + 1,
        "title": title,
        "description": description,
        "priority": priority,
        "status": "Open",
        "date_created": datetime.now().strftime("%Y-%m-%d")
    }

    bugs.append(bug)
    save_bugs(bugs)

    print("Bug added!\n")

def view_bugs():
    bugs = load_bugs()

    if not bugs:
        print("No bugs found.\n")
        return

    for bug in bugs:
        print(f"{bug['id']}. {bug['title']} | {bug['status']} | {bug['priority']} | {bug['date_created']}")
        print(f"   {bug['description']}\n")

def fix_bug():
    bugs = load_bugs()

    if not bugs:
        print("No bugs to fix.\n")
        return

    view_bugs()
    index = int(input("Enter bug number: ")) - 1

    if 0 <= index < len(bugs):
        bugs[index]["status"] = "Fixed"
        save_bugs(bugs)
        print("Bug fixed!\n")
    else:
        print("Invalid choice.\n")

def main():
    while True:
        print("=== Bug Tracker ===")
        print("1. Add Bug")
        print("2. View Bugs")
        print("3. Fix Bug")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_bug()
        elif choice == "2":
            view_bugs()
        elif choice == "3":
            fix_bug()
        elif choice == "4":
            break
        else:
            print("Invalid option\n")

main()