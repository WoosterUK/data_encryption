import sys

class __SelectDict():
    def __init__(self, introduction, options):
        self.introduction = introduction
        self.options = options
        self.validate_options()

    def __str__(self):
        return "\n".join(f"[{i}] {option}" for i, option in self.options.items())
    
    def validate_options(self):
        if not isinstance(self.options, dict):
            raise ValueError("Options must be a dictionary")
        if len(self.options) == 0:
            raise ValueError("Options dictionary cannot be empty")
        if len(set(self.options.keys())) != len(self.options):
            raise ValueError("Option keys must be unique")
        return True
    
    def get_option(self, user_input):
        if user_input in self.options.keys():
            return self.options[user_input]
        else:
            raise IndexError("Option index out of range")
    
    def run(self):
        if self.introduction is not None:
            print(self.introduction)
        print(self)
        return self.get_user_selection()
    
    def get_user_selection(self):
        while True:
            try:
                user_input = input("Please select an option: ")
                return self.get_option(user_input.lower())
            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")

class __SelectOne(__SelectDict):
    def __init__(self, introduction, options):
        options_dict = {str(i+1): option for i, option in enumerate(options)}
        super().__init__(introduction, options_dict)

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
    def __init__(self, introduction, prompt, category="string", validate_function=str):
        self.introduction = introduction
        self.prompt = prompt
        self.validate_function = validate_function
        self.category = category
    
    def __str__(self):
        return self.introduction

    def get_input(self):
        if self.introduction is not None:
            print(self)
        while True:
            user_input = input(self.prompt)
            try:
                return self.validate_function(user_input)
            except ValueError:
                print(f"Invalid input. Please enter a value of type: {self.category}.")

def display_message(message):
    print(message)

def display_hline(length=50, char="-"):
    print(char * length)

def display_heading(heading, level):
    dividers = {1: "=", 2: "-", 3: "~"}
    up_divider = dividers.get(level)
    do_divider = dividers.get(level+1, "")
    display_hline(length=len(heading), char=up_divider)
    display_message(heading)
    display_hline(length=len(heading), char=do_divider)

def get_user_input(prompt):
    return input(prompt)

def select_dict(introduction, options):
    selector = __SelectDict(introduction, options)
    return selector.run()

def select_option(introduction, options):
    selector = __SelectOne(introduction, options)
    return selector.run()

def yes_no_prompt(prompt):
    print(prompt)
    yes_no = __YesNo()
    return yes_no.get_user_selection()

def create_keyboard_input(category="string", validate_function=str):
    current_module = sys.modules[__name__]
    def input_function(introduction, prompt): 
        kb_input = __KeyboardInput(introduction, prompt, category, validate_function)
        return kb_input.get_input()
    setattr(current_module, f"get_{category}_input", input_function)
    return True

create_keyboard_input("string", str)
create_keyboard_input("float", float)
create_keyboard_input("integer", int)

if __name__ == "__main__":
    display_heading("Terminal Interface Test", 1)
    options = ["Dict select", "Yes / No", "String input", "Float input", "Integer input"]
    selected_option = select_option(None, options)
    print(f"You selected: {selected_option}")

    if selected_option == "Dict select":
        dict_options = {"a": "Option A", "b": "Option B", "c": "Option C"}
        dict_result = select_dict("Please select an option from the dictionary:", dict_options)
        print(f"You selected: {dict_result}")
    elif selected_option == "Yes / No":
        yes_no_result = yes_no_prompt("Do you want to continue?")
        print(f"Your answer: {'Yes' if yes_no_result else 'No'}")
    elif selected_option == "String input":
        kb_input_result = get_string_input("Please enter a string:", "Input: ")
        print(f"You entered: {kb_input_result}")
    elif selected_option == "Float input":
        num_input_result = get_float_input("Please enter a float value:", "Input: ")
        print(f"You entered: {num_input_result}")
    elif selected_option == "Integer input":
        int_input_result = get_integer_input("Please enter an integer value:", "Input: ")
        print(f"You entered: {int_input_result}")