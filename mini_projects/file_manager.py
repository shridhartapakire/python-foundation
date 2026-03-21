# File Manager System
# Created as part of Python learning journey

from pathlib import Path
import os


def list_items():
    print("\n📂 Files & Folders:")
    path = Path('.')
    items = list(path.rglob('*'))

    if not items:
        print("No files found")
        return

    for i, item in enumerate(items):
        print(f"{i+1}. {item}")


def create_file():
    try:
        list_items()
        name = input("\nEnter file name: ")
        p = Path(name)

        if not p.exists():
            with open(p, "w") as fs:
                data = input("Enter content: ")
                fs.write(data)
            print("✅ File created successfully")
        else:
            print("❌ File already exists")

    except Exception as err:
        print(f"Error: {err}")


def read_file():
    try:
        list_items()
        name = input("\nEnter file name to read: ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                print("\n📄 File Content:\n")
                print(fs.read())
        else:
            print("❌ File does not exist")

    except Exception as err:
        print(f"Error: {err}")


def update_file():
    try:
        list_items()
        name = input("\nEnter file name to update: ")
        p = Path(name)

        if p.exists() and p.is_file():

            print("\n1. Rename File")
            print("2. Overwrite Content")
            print("3. Append Content")

            try:
                choice = int(input("Enter your choice: "))
            except:
                print("❌ Invalid input")
                return

            if choice == 1:
                new_name = input("Enter new file name: ")
                p.rename(new_name)
                print("✅ File renamed successfully")

            elif choice == 2:
                with open(p, 'w') as fs:
                    data = input("Enter new content: ")
                    fs.write(data)
                print("✅ File overwritten successfully")

            elif choice == 3:
                with open(p, 'a') as fs:
                    data = input("Enter content to append: ")
                    fs.write(" " + data)
                print("✅ Content appended")

            else:
                print("❌ Invalid choice")

        else:
            print("❌ File does not exist")

    except Exception as err:
        print(f"Error: {err}")


def delete_file():
    try:
        list_items()
        name = input("\nEnter file name to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("✅ File deleted successfully")
        else:
            print("❌ File not found")

    except Exception as err:
        print(f"Error: {err}")


def menu():
    print("\n===== FILE MANAGER SYSTEM 📁 =====")
    print("1. Create File")
    print("2. Read File")
    print("3. Update File")
    print("4. Delete File")
    print("5. Exit")


def main():
    print("\nWelcome to File Manager System 📁")

    while True:
        menu()

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("❌ Invalid input")
            continue

        if choice == 1:
            create_file()

        elif choice == 2:
            read_file()

        elif choice == 3:
            update_file()

        elif choice == 4:
            delete_file()

        elif choice == 5:
            print("🙏 Exiting File Manager")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
