import lib.file_handler as file_handler
import lib.terminal_interface as interface
from lib.encrypt import generate_key
import os

def show_help():
    interface.display_message("================")
    interface.display_message("User information")
    interface.display_message("----------------")
    interface.display_message("This program is designed to help you encrypt the first column of a CSV file.")
    interface.display_message("It requires a key formatted in a particular way; you can generate this key using this program.")
    interface.display_message("To use the program, simply follow the prompts to select a CSV file and enter your encryption key.")
    interface.display_message("It will ignore the header row. All other values in the first column will be encrypted and saved to a new file.")
    interface.display_message("The new file will have the same name as the original, but with '_encrypted' appended before the file extension.")
    interface.get_keyboard_input(None, "Press Enter to return to the main menu:")

def encrypt_csv():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    finder = file_handler.FileFinder(current_dir)
    files = finder.filter_files_by_extension(".csv")
    if not files:
        interface.display_message("No CSV files found in the current directory.")
    else:
        encryption_key = interface.get_keyboard_input(
            "Please enter the encryption key:",
            "Encryption Key: "
        )
        selected_file = interface.select_option(None, files)
        interface.display_message(f"You selected: {selected_file}")
        file_path = os.path.join(current_dir, selected_file)
        file_handler.encrypt_csv_column(file_path, encryption_key)

def get_key():
    interface.display_message("Generating a new encryption key...")
    key = generate_key()
    interface.display_message(f"Your new encryption key is: {key}")

if __name__ == "__main__":
    interface.display_message("Data Encryption Program")
    interface.display_message("=======================")
    interface.display_message("Welcome to the data encryption program")
    options = {
        "Encrypt a CSV file": encrypt_csv,
        "Generate a new encryption key": get_key,
        "Help": show_help,
        "Quit": exit
    }
    while True:
        selected_option = interface.select_option(
            "=" * 9 + "\nMain menu\n" + "-" * 9,
            list(options.keys())
        )
        options[selected_option]()
    