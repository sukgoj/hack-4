import datetime

class Child:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.appointments = []

    def add_appointment(self, appointment_date):
        self.appointments.append(appointment_date)
        print(f"Appointment booked for {self.name} on {appointment_date}.")

    def view_appointments(self):
        if self.appointments:
            print(f"\nChild: {self.name}\nBirth Date: {self.birth_date}\nAppointments: {self.appointments}\n")
        else:
            print(f"\nChild: {self.name}\nBirth Date: {self.birth_date}\nNo appointments found.\n")

class VaccinationManagementSystem:
    def __init__(self):
        self.children = {}

    def add_child(self, name, birth_date):
        if name in self.children:
            print(f"Child {name} is already registered.")
        else:
            self.children[name] = Child(name, birth_date)
            print(f"Child {name} registered successfully.")

    def book_appointment(self, name, appointment_date):
        if name in self.children:
            self.children[name].add_appointment(appointment_date)
        else:
            print(f"No child found with the name {name}. Please register the child first.")

    def view_child(self, name):
        if name in self.children:
            self.children[name].view_appointments()
        else:
            print(f"No child found with the name {name}.")

    def check_reminders(self, days_before=1):
        today = datetime.date.today()
        for child in self.children.values():
            for appointment in child.appointments:
                appointment_date = datetime.datetime.strptime(appointment, "%Y-%m-%d").date()
                if (appointment_date - today).days == days_before:
                    print(f"Reminder: {child.name} has an appointment on {appointment_date}.")

if __name__ == "__main__":
    vms = VaccinationManagementSystem()

    while True:
        print("\nChild Vaccination Management System")
        print("1. Register a Child")
        print("2. Book an Appointment")
        print("3. View Child Information")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter child's name: ")
            birth_date = input("Enter child's birth date (YYYY-MM-DD): ")
            vms.add_child(name, birth_date)

        elif choice == '2':
            name = input("Enter child's name: ")
            appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
            vms.book_appointment(name, appointment_date)

        elif choice == '3':
            name = input("Enter child's name: ")
            vms.view_child(name)

        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
