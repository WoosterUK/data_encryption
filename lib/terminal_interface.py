class __SelectOne():
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

class __YesNo():
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

class __KeyboardInput():
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

class __NumericInput(__KeyboardInput):
    def __init__(self, introduction, prompt):
        super().__init__(introduction, prompt, "numeric")
        self.validate_function = lambda x: float(x)

class __IntegerInput(__KeyboardInput):
    def __init__(self, introduction, prompt):
        super().__init__(introduction, prompt, "integer")
        self.validate_function = lambda x: int(x)

def display_message(message):
    print(message)

def get_user_input(prompt):
    return input(prompt)

def select_option(options):
    selector = __SelectOne(options)
    print(selector)
    return selector.get_user_selection()

def yes_no_prompt(prompt):
    print(prompt)
    yes_no = __YesNo()
    print(yes_no)
    return yes_no.get_user_selection()

def get_keyboard_input(introduction, prompt):
    kb_input = __KeyboardInput(introduction, prompt)
    return kb_input.get_input()

def get_numeric_input(introduction, prompt):
    num_input = __NumericInput(introduction, prompt)
    return num_input.get_input()

def get_integer_input(introduction, prompt):
    int_input = __IntegerInput(introduction, prompt)
    return int_input.get_input()

if __name__ == "__main__":
    options = ["Yes / No", "String input", "Numeric input", "Integer input"]
    selected_option = select_option(options)
    print(f"You selected: {selected_option}")

    if selected_option == "Yes / No":
        yes_no_result = yes_no_prompt("Do you want to continue?")
        print(f"Your answer: {'Yes' if yes_no_result else 'No'}")
    elif selected_option == "String input":
        kb_input_result = get_keyboard_input("Please enter a string:", "Input: ", "string")
        print(f"You entered: {kb_input_result}")
    elif selected_option == "Numeric input":
        num_input_result = get_numeric_input("Please enter a numeric value:", "Input: ")
        print(f"You entered: {num_input_result}")
    elif selected_option == "Integer input":
        int_input_result = get_integer_input("Please enter an integer value:", "Input: ")
        print(f"You entered: {int_input_result}")