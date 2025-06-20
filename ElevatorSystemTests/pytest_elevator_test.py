from ElevatorSystem.Elevator import Elevator

def test_basic_movement():
    elevator = Elevator("e1", 2, 5, "UUDD")
    elevator.process_commands()
    assert elevator.current_floor == 2

def test_ignore_invalid_moves():
    elevator = Elevator("e2", 1, 3, "DDUUU")
    elevator.process_commands()
    assert elevator.current_floor == 3

def test_stop_count():
    elevator = Elevator("e3", 1, 5, "SUSDS")
    elevator.process_commands()
    assert elevator.stops == 3

def test_invalid_commands():
    elevator = Elevator("e4", 1, 5, "UXSDZ")
    elevator.process_commands()
    assert elevator.current_floor == 1
    assert elevator.stops == 1

def test_get_score():
    elevator = Elevator("e5", 1, 5, "UUUSSD")
    elevator.process_commands()
    assert elevator.get_score() == 2

def test_get_score_no_stop():
    elevator = Elevator("e6", 1, 5, "UUU")
    elevator.process_commands()
    assert elevator.get_score() == 3