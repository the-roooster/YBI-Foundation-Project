import pandas as pd

# Global variables
guest_list = []  # List of tuples to store guest data
guest_set = set()  # Set to track unique guest-event combinations
valid_statuses = {'Attending', 'Not Attending', 'Pending'}

def add_guest():
    """Add a new guest to the guest list with validation"""
    print("\nAdd New Guest")
    
    while True:
        name = input("Enter guest name: ").strip()
        event = input("Enter event name: ").strip()
        
        # Create a unique identifier for the guest-event combination
        guest_key = f"{name.lower()}_{event.lower()}"
        
        if guest_key in guest_set:
            print("Error: This guest is already registered for this event.")
            continue
        else:
            break
    
    while True:
        status = input("Enter RSVP status (Attending/Not Attending/Pending): ").strip()
        if status in valid_statuses:
            break
        else:
            print("Invalid status. Please choose from: Attending, Not Attending, Pending")
    
    # Add to our data structures
    guest_list.append((name, event, status))
    guest_set.add(guest_key)
    print(f"Guest {name} added successfully for event {event}!")

def view_guests():
    """Display all guests in the system"""
    print("\nCurrent Guest List:")
    print("-" * 40)
    print(f"{'Name':<20}{'Event':<20}{'Status':<15}")
    print("-" * 40)
    
    if not guest_list:
        print("No guests in the system yet.")
    else:
        for guest in guest_list:
            print(f"{guest[0]:<20}{guest[1]:<20}{guest[2]:<15}")
    print("-" * 40)

def summarize_attendance():
    """Show counts of each RSVP status using Pandas"""
    if not guest_list:
        print("No guests to summarize.")
        return
    
    # Convert to DataFrame
    df = pd.DataFrame(guest_list, columns=['Name', 'Event', 'Status'])
    
    # Get status counts
    status_counts = df['Status'].value_counts()
    
    print("\nAttendance Summary:")
    print("-" * 30)
    print(status_counts.to_string())
    print("-" * 30)

def export_to_csv():
    """Export guest data to a CSV file"""
    if not guest_list:
        print("No guests to export.")
        return
    
    df = pd.DataFrame(guest_list, columns=['Name', 'Event', 'Status'])
    df.to_csv('guest_list.csv', index=False)
    print("Guest list successfully exported to guest_list.csv")

def main_menu():
    """Display the main menu and handle user input"""
    while True:
        print("\nEvent Guest List Manager")
        print("1. Add Guest")
        print("2. View Guests")
        print("3. Summarize Attendance")
        print("4. Export to CSV")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_guest()
        elif choice == '2':
            view_guests()
        elif choice == '3':
            summarize_attendance()
        elif choice == '4':
            export_to_csv()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    main_menu()
