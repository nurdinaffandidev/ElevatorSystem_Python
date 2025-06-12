import unittest
from ElevatorSystem.Elevator import Elevator

class TestElevator(unittest.TestCase):

    def test_basic_movement(self):
        elevator = Elevator("e1", 2, 5, "UUDD")
        elevator.process_commands()
        self.assertEqual(elevator.current_floor, 2)

    def test_ignore_invalid_moves(self):
        elevator = Elevator("e2", 1, 3, "DDUUU")
        elevator.process_commands()
        self.assertEqual(elevator.current_floor, 3)

    def test_stop_count(self):
        elevator = Elevator("e3", 1, 5, "SUSDS")
        elevator.process_commands()
        self.assertEqual(elevator.stops, 3)


    def test_invalid_commands(self):
        elevator = Elevator("e4", 1, 5, "UXSDZ")
        elevator.process_commands()
        self.assertEqual(elevator.current_floor, 1)  # Only valid commands count
        self.assertEqual(elevator.stops, 1)

    def test_get_score(self):
        elevator = Elevator("e5", 1, 5, "UUUSSD")
        elevator.process_commands()
        self.assertEqual(elevator.get_score(), 2)

    def test_get_score_no_stop(self):
        elevator = Elevator("e6", 1, 5, "UUU")
        elevator.process_commands()
        self.assertEqual(elevator.get_score(), 3)


if __name__ == '__main__':
    unittest.main()
