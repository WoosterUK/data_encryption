class SelectOne():
    def __init__(self, options):
        self.options = options

    def __str__(self):
        return "\n".join(f"{i+1}. {option}" for i, option in enumerate(self.options))

    def get_option(self, index):
        if 0 <= index < len(self.options):
            return self.options[index]
        else:
            raise IndexError("Option index out of range")
    
    def get_user_selection(self):
        while True:
            try:
                user_input = int(input("Please select an option: ")) - 1
                return self.get_option(user_input)
            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")

class YesNo():
    def __str__(self):
        return "1. Yes\n2. No"

    def get_user_selection(self):
        while True:
            user_input = input("Please select an option (Yes/No): ").strip().lower()
            if user_input in ['yes', 'y']:
                return True
            elif user_input in ['no', 'n']:
                return False
            else:
                print("Invalid selection. Please enter 'Yes' or 'No'.")

class KeyboardInput():
    def __init__(self, introduction, prompt, category="string"):
        self.introduction = introduction
        self.prompt = prompt
        self.validate_function = str
        self.category = category
    
    def __str__(self):
        return self.introduction

    def get_input(self):
        print(self)
        while True:
            user_input = input(self.prompt)
            try:
                return self.validate_function(user_input)
            except ValueError:
                print(f"Invalid input. Please enter a {self.category} value.")

class NumericInput(KeyboardInput):
    def __init__(self, introduction, prompt):
        super().__init__(introduction, prompt, "numeric")
        self.validate_function = lambda x: float(x)

class IntegerInput(KeyboardInput):
    def __init__(self, introduction, prompt):
        super().__init__(introduction, prompt, "integer")
        self.validate_function = lambda x: int(x)

class TerminalInterface():
    def __init__(self):
        pass

    def display_message(self, message):
        print(message)

    def get_user_input(self, prompt):
        return input(prompt)

    def select_option(self, options):
        selector = SelectOne(options)
        print(selector)
        return selector.get_user_selection()

    def yes_no_prompt(self, prompt):
        print(prompt)
        yes_no = YesNo()
        print(yes_no)
        return yes_no.get_user_selection()
    
    def get_keyboard_input(self, introduction, prompt):
        kb_input = KeyboardInput(introduction, prompt)
        return kb_input.get_input()
    
    def get_numeric_input(self, introduction, prompt):
        num_input = NumericInput(introduction, prompt)
        return num_input.get_input()
    
    def get_integer_input(self, introduction, prompt):
        int_input = IntegerInput(introduction, prompt)
        return int_input.get_input()

if __name__ == "__main__":
    interface = TerminalInterface()
    options = ["Yes / No", "String input", "Numeric input", "Integer input"]
    selected_option = interface.select_option(options)
    print(f"You selected: {selected_option}")

    if selected_option == "Yes / No":
        yes_no_result = interface.yes_no_prompt("Do you want to continue?")
        print(f"Your answer: {'Yes' if yes_no_result else 'No'}")
    elif selected_option == "String input":
        kb_input_result = interface.get_keyboard_input("Please enter a string:", "Input: ", "string")
        print(f"You entered: {kb_input_result}")
    elif selected_option == "Numeric input":
        num_input_result = interface.get_numeric_input("Please enter a numeric value:", "Input: ")
        print(f"You entered: {num_input_result}")
    elif selected_option == "Integer input":
        int_input_result = interface.get_integer_input("Please enter an integer value:", "Input: ")
        print(f"You entered: {int_input_result}")