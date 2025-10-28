# Air Traffic Controller Simulation

A simple, console-based Python application that simulates an Air Traffic Control (ATC) system. This script allows a user to manage three separate flight queues:
* Landing Line
* Takeoff Line
* Waiting Area

## 🚀 Features

* **Initialize Queues:** Start the simulation by inputting an initial, comma-separated list of flights for each of the three areas.
* **Menu-Driven:** A simple text menu allows the user to perform different actions.
* **Queue Management:** Add flights to different queues (Takeoff, Waiting) and process the next event.
* **Status Updates:** After every action, the simulation prints the current status, showing how many planes are in each queue.

## 🏃‍♂️ How to Run

1.  Make sure you have Python 3 installed.
2.  Save the code as `Air-Traffic-Controller.py`.
3.  Run the script from your terminal:

    ```bash
    python Air-Traffic-Controller.py
    ```

4.  You will first be prompted to enter the initial flights for each line. You can press Enter to start with empty lines.

    ```
    Initial Flights in the Landing Line : AA123,UA456
    Initial Flights in the Take Off Line : DL789
    Initial Flights in the Waiting Area : WN111
    ```

5.  After initialization, use the menu to manage the flights:

    ```
    1. Land
    2. Take Off
    3. Start Waiting
    4. Move from Waiting to Takeoff
    5. Next
    6. Quit
    Choice :
    ```

## 📝 Menu Options

* **1. Land:** (Note: In the current logic, this prompts for a flight sign but does not add it to the landing queue. It only reports the status.)
* **2. Take Off:** Adds a flight to the takeoff queue and processes one landing if a plane is waiting.
* **3. Start Waiting:** Adds a flight to the waiting area and processes one takeoff if a plane is waiting.
* **4. Move from Waiting to Takeoff:** Moves a plane from the waiting area to the takeoff line.
* **5. Next:** Processes the next event in order of priority:
    1.  Lands the next plane from the `land` queue.
    2.  If no planes are landing, takes off the next plane from the `takeoff` queue.
    3.  If no planes are landing or taking off, moves a plane from `waiting` to `takeoff`.
* **6. Quit:** Exits the simulation.

## 🏛️ Code Structure

* **`Atc` class:** A class used to manage the **Landing** and **Takeoff** lines. It includes methods to `add` and `remove` flights.
* **`Parking` class:** A class used to manage the **Waiting Area**. It includes `add` and `remove` methods and a `__str__` method for formatted status printing.
* **`main()` function:** Contains the main application loop, initialization logic, and menu handling.

## 💡 Potential Improvements

This is a great starting project! Here are a few ideas for potential improvements:

* **Fix Class Variables:** The `flights = []` list in both `Atc` and `Parking` is a *class variable*. This means all instances (e.g., `land` and `takeoff`) share the *same list*, which can cause bugs. This should be changed to an *instance variable* by initializing it inside `__init__`: `self.flights = []`.
* **Clarify Menu Logic:** The logic for some menu items is mixed. For example, "Take Off" also triggers a "Land". These could be separated into distinct, single-purpose actions.
* **Implement "Land" (Option 1):** Update Option 1 to actually add the entered flight to the `land` queue.
* **Add Error Handling:** Add `try-except` blocks to handle invalid inputs, such as entering a non-numeric choice in the menu or trying to remove a flight from an empty list.
