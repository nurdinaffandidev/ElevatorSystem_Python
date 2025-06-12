from ElevatorSystem.Elevator import Elevator

def get_int_input(prompt, min_val=1):
    while True:
        try:
            input_value = int(input(prompt))
            if input_value < min_val:
                raise ValueError
            return input_value
        except ValueError:
            print(f"Please enter a valid integer >= {min_val}.")

def get_bool_input(prompt):
    while True:
        input_val = input(prompt).strip().lower()
        if input_val in ('yes', 'y'):
            return True
        elif input_val in ('no', 'n'):
            return False
        else:
            print("Please enter y/n: ")


def main():
    elevators = []
    num_floors = get_int_input("Please enter the number of floors: ")

    while True:
        name = input("Enter a new elevator name: ").strip()

        starting_floor = get_int_input(f"Enter starting floor for {name}: ", min_val=1)
        if starting_floor > num_floors:
            print(f"Starting floor cannot be higher than {num_floors}.")
            continue

        commands = input("Enter command string (e.g., USDUDSD): ").strip().upper()
        elevator = Elevator(name, starting_floor, num_floors, commands)
        elevators.append(elevator)

        continue_add = get_bool_input("Would you like to add more elevators? y/n: ")
        if not continue_add:
            run_simulation(elevators)
            break

def run_simulation(elevators):
    print("\nRunning simulation...\n")
    for elevator in elevators:
        elevator.process_commands()
        elevator.report()


if __name__ == "__main__":
    main()