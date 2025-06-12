class Elevator:
    def __init__(self, name, starting_floor, num_floors, commands):
        self.name = name
        self.current_floor = starting_floor
        self.num_floors = num_floors
        self.commands = commands.upper()
        self.stops = 0
        self.history = []
        self.floors_travelled = 0

    def process_commands(self):
        for cmd in self.commands:
            self.history.append((self.current_floor, cmd))
            if cmd == 'U':
                if self.current_floor < self.num_floors:
                    self.current_floor += 1
                    self.floors_travelled +=1
            elif cmd == 'D':
                if self.current_floor > 1:
                    self.current_floor -= 1
                    self.floors_travelled += 1
            elif cmd == 'S':
                self.stops += 1
            else:
                print(f"Ignored invalid command '{cmd}' for {self.name}")

    def get_score(self):
        if self.stops == 0:
            return format(self.floors_travelled, ".1f")
        return round(self.floors_travelled / self.stops, 2)


    def report(self):
        print(f"Elevator {self.name} started on floor {self.history[0][0]} moving {self.commands}")
        print(f"Elevator {self.name} ended on floor {self.current_floor} with {self.stops} stops.")
        print(f"efficiency: {self.get_score()}\n")
        self.report_state_log()
        print()

    def report_state_log(self):
        print(f"Elevator {self.name} full logs:")
        for floor, next_action in self.history:
            print(f"(current floor:{floor}, next action:{next_action})")

