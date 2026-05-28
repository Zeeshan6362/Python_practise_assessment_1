#Flow of the program:
#Create function check_password_strength(password)
#Check if password length is at least 8 characters
#Check if password contains both uppercase and lowercase letters
#Check if password contains at least one digit
#Check if password contains at least one special character
#Return True if all criteria are met, otherwise return False


import string

def check_password_strength(password):
    """
    Checks if a password meets the required DevOps security criteria.
    Returns True if strong, False otherwise.
    """
    # 1. Checking Minimum length: The password should be at least 8 characters long
    if len(password) < 8:
        return False
        
    # 2. Checking if password contains both uppercase and lowercase letters
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
        
    # 3. Checking if password contains at least one digit (0-9)
    if not any(char.isdigit() for char in password):
        return False
        
    # 4. Checking if password contains at least one special character
    # Using string.punctuation covers all standard special characters (!, @, #, $, %, etc.)
    if not any(char in string.punctuation for char in password):
        return False
        
    # If it passes all checks, it's a strong password
    return True

# --- Main Script Execution ---
if __name__ == "__main__":
    print("--- DevOps Password Strength Checker ---")
    
    # Take user input outside of the function
    user_password = input("Enter a password to evaluate: ")
    
    # Call the function to validate it
    is_strong = check_password_strength(user_password)
    
    # Provide appropriate feedback
    if is_strong:
        print("\nSuccess: Your password is strong and meets all security criteria.")
    else:
        print("\nWeak Password: Your password does not meet the requirements.")
        print("Please ensure your password:")
        print("- Is at least 8 characters long")
        print("- Contains both uppercase and lowercase letters")
        print("- Contains at least one number")
        print("- Contains at least one special character (e.g., !, @, #, $, %)")