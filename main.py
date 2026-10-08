
from diary import (
    add_entry,
    search_entries,
    select_diary_file,
    view_entries,
)


def main():
    """Run the diary application."""
    diary_file = None

    while True:
        print("\n===== MY DIARY APPLICATION =====")
        print("1. Select or create a diary file")
        print("2. Add a diary entry")
        print("3. View all diary entries")
        print("4. Search entries by date")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            selected_file = select_diary_file()

            if selected_file is not None:
                diary_file = selected_file

        elif choice == "5":
            print("Goodbye!")
            break

        elif choice in ("2", "3", "4"):
            if diary_file is None:
                print("Please select a diary file first.")
                continue

            if choice == "2":
                add_entry(diary_file)
            elif choice == "3":
                view_entries(diary_file)
            else:
                search_entries(diary_file)

        else:
            print("Invalid choice. Select 1-5.")


if __name__ == "__main__":
    main()
  