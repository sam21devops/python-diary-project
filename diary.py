
from datetime import datetime
from pathlib import Path


def select_diary_file():
    """Select an existing diary file or create a new one."""
    file_name = input("Enter diary file name (.txt): ").strip()

    if not file_name:
        print("File name cannot be empty.")
        return None

    file_path = Path(file_name)

    if file_path.suffix.lower() != ".txt":
        print("Please select a .txt file.")
        return None

    if not file_path.parent.is_dir():
        print("The folder does not exist.")
        return None

    try:
        file_path.touch(exist_ok=True)
    except OSError as error:
        print(f"File error: {error}")
        return None

    print(f"Selected diary: {file_path}")
    return file_path


def add_entry(file_path):
    """Save one dated diary entry."""
    date = input("Enter date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date.")
        return

    entry = input("Write your diary entry: ").strip()

    if not entry:
        print("Entry cannot be empty.")
        return

    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"{date} | {entry}\n")
        print("Entry saved successfully.")
    except OSError as error:
        print(f"File error: {error}")


def view_entries(file_path):
    """Display all diary entries."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            entries = file.readlines()
    except OSError as error:
        print(f"File error: {error}")
        return

    if not entries:
        print("No entries found.")
        return

    for entry in entries:
        print(entry.rstrip("\n"))


def search_entries(file_path):
    """Display diary entries matching a date."""
    date = input("Enter date to search (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date.")
        return

    found = False

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for entry in file:
                if entry.startswith(f"{date} | "):
                    print(entry.rstrip("\n"))
                    found = True
    except OSError as error:
        print(f"File error: {error}")
        return

    if not found:
        print("No entries found for that date.")
  