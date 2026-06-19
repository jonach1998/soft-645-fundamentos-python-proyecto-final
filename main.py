from app.menu import display_menu


def main():
    while True:
        display_menu()
        option = input("Select an option: ")

        if option == "0":
            print("Goodbye.")
            break
        else:
            print("This option has not been implemented yet.")


if __name__ == "__main__":
    main()
