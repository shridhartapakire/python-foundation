# Advanced File Manager System 📁
# Created as part of Python learning journey

from pathlib import Path
import os


def list_items():
    print("\n📂 Available Files & Folders:")
    items = list(Path('.').glob('*'))

    if not items:
        print("No files found")
        return

    for i, item in enumerate(items):
        print(f"{i+1}. {item}")


def create_file():
    try:
        name = input("\nEnter new file name: ")
        p = Path(name)

        if p.exists():
            print("❌ File already exists")
            return

        content = input("Enter content: ")
        p.write_text(content)

        print("✅ File created successfully")

    except Exception as e:
        print(f"Error: {e}")


def read_file():
    try:
        list_items()
        name = input("\nEnter file name to read: ")
        p = Path(name)

        if not p.exists() or not p.is_file():
            print("❌ File not found")
            return

        print("\n📄 File Content:\n")
        print(p.read_text())

    except Exception as e:
        print(f"Error: {e}")


def update_file():
    try:
        list_items()
        name = input("\nEnter file name to update: ")
        p = Path(name)

        if not p.exists() or not p.is_file():
            print("❌ File not found")
            return

        print("\n1. Rename File")
        print("2. Overwrite Content")
        print("3. Append Content")

        choice = input("Enter choice: ")

        if choice == '1':
            new_name = input("Enter new file name: ")
            p.rename(new_name)
            print("✅ File renamed")

        elif choice == '2':
            new_content = input("Enter new content: ")
            p.write_text(new_content)
            print("✅ File overwritten")

        elif choice == '3':
            extra = input("Enter content to append: ")
            with open(p, 'a') as f:
                f.write("\n" + extra)
            print("✅ Content appended")

        else:
            print("❌ Invalid choice")

    except Exception as e:
        print(f"Error: {e}")


def delete_file():
    try:
        list_items()
        name = input("\nEnter file name to delete: ")
        p = Path(name)

        if not p.exists() or not p.is_file():
            print("❌ File not found")
            return

        confirm = input("Are you sure? (y/n): ")

        if confirm.lower() == 'y':
            os.remove(p)
            print("✅ File deleted")
        else:
            print("Cancelled")

    except Exception as e:
        print(f"Error: {e}")


def menu():
    print("\n===== ADVANCED FILE MANAGER 📁 =====")
    print("1. Create File")
    print("2. Read File")
    print("3. Update File")
    print("4. Delete File")
    print("5. Exit")


def main():
    print("\nWelcome to Advanced File Manager 📁")

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            create_file()

        elif choice == '2':
            read_file()

        elif choice == '3':
            update_file()

        elif choice == '4':
            delete_file()

        elif choice == '5':
            print("👋 Exiting File Manager")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
