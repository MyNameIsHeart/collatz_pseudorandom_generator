def get_positive_integer(prompt, default_value=None):
    """
    Asks the user for a positive integer.
    - Enter -> returns default value (if provided).
    - Non-positive number -> converts it to a positive value.
    - Invalid input -> prompts again.
    """
    while True:
        try:
            user_input = input(f"{prompt} " + 
                               (f"(press enter for default value, {default_value})" if default_value is not None else "") + 
                               ": ").strip()
            if user_input == "":  # Default value
                if default_value is not None:
                    return default_value
            value = int(user_input)
            if value > 0:
                return value
            print("Invalid input - must be a positive integer.")
            # Convert negative or zero values to positive
            value = abs(value) or 1
            print(f"Using {value} instead.")
            return value
        except ValueError:
            print("Invalid input - must be an integer.")