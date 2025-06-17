# Elevator System Simulation

This project simulates a smart elevator system that processes movement commands and tracks elevator state. It includes a command-line interface and unit tests.

---

## 🚀 Setup Instructions

1. **Clone the repository**:
   ```
   git clone https://github.com/nurdinaffandidev/elevator-system.git
   ```
   ```
   cd ElevatorSystem
   ```
   
2. **Run the program:**
   ```
   python elevator_simulator.py
   ```

3. **Run the unit test:**

   with **'pytest'**:
   ```
   pytest pytest_elevator_test.py   
   ```
   or python unit test:
   ```
   python -m unittest ElevatorSystemTests/unittest_elevator_test.py
   ```

## 🧑‍💻 Running the program

1. **Input number of floors**:
   ```
   Please enter the number of floors: _
   ```

2. **Input elevator name**:
   ```
   Enter a new elevator name: _
   ```

3. **Input starting floor of elevator name previously entered**:
   ```
   Enter starting floor for {name}: _
   ```
4. **Input elevator commands**:
   
   U: up

   D: down

   S: stop
   ```
   Enter command string (e.g., USDUDSD): _
   ```
5. **Add more elevators if needed**:
   ```
   Would you like to add more elevators? y/n: _
   ```

### 💻️ Sample:
  Input:
  
  ```
  Please enter the number of floors: 20
  Enter a new elevator name: e1
  Enter starting floor for e1: 2 
  Enter command string (e.g., USDUDSD): DDDD 
  Would you like to add more elevators? y/n: y
  Enter a new elevator name: e2
  Enter starting floor for e2: 5
  Enter command string (e.g., USDUDSD): UUUSDDD
  Would you like to add more elevators? y/n: n
  ```
  Output:
  ```
  Running simulation...
    
  Elevator e1 started on floor 2 moving DDDD
  Elevator e1 ended on floor 1 with 0 stops.
  efficiency: 1.0
  
  Elevator e1 full logs:
  (current floor:2, next action:D)
  (current floor:1, next action:D)
  (current floor:1, next action:D)
  (current floor:1, next action:D)

  Elevator e2 started on floor 5 moving UUUSDDD
  Elevator e2 ended on floor 5 with 1 stops.
  efficiency: 6.0

  Elevator e2 full logs:
  (current floor:5, next action:U)
  (current floor:6, next action:U)
  (current floor:7, next action:U)
  (current floor:8, next action:S)
  (current floor:8, next action:D)
  (current floor:7, next action:D)
  (current floor:6, next action:D)
  ```