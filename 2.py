# Function to validate the length of first and last names
def validate_name_length(first_name, last_name):
    # Check if both first name and last name are at least 2 characters long
    if len(first_name) < 2:
        print("Error: The first name must be at least 2 characters long.")
    elif len(last_name) < 2:
        print("Error: The last name must be at least 2 characters long.")
    else:
        print("Both names are valid.")

# Main function to run the script
def main():
    # Ask for user input
    first_name = input("Please enter your first name: ").strip()
    last_name = input("Please enter your last name: ").strip()
    
    # Validate the names
    validate_name_length(first_name, last_name)

# Ensure the script runs if executed directly
if __name__ == "__main__":
    main()
