# User Profile Management System

# Global variavle to control the state of the system
system_active = True

# Function to create and display user profiles
def create_user_profile():
    # Assigning multiple variables in one line
    user_name, user_age, user_email = "Daniel", 35, "williamsoligodaniel@gmail.com"
    
    # output variables to display user information
    print("User profile created")
    print("Name", user_name)
    print("Age", user_age)
    print("Email", user_email)
    
# Function to toggle the system status using a global vriable
def toggle_system_status():
    global system_active # Declare system_active as global
    system_active = not system_active # Toggle the value
    status = "active" if system_active else "inactive"
    print("The system is now", status)
    
# Main function to run the profile system
def main():
    print("Welcome to the User Profile Management System")
    # Call the function to create and display a user profile
    create_user_profile()
    
    # Toggle the system status to demonstrate the global variable
    toggle_system_status()

# Execute the main function only if this script is run directly
if __name__ == "__main__":
    main()