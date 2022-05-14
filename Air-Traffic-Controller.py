class Atc:
    flights = []  # flights number list

    def __init__(self, flight=None):
        if flight is not None:
            self.flights = list(flight.strip().split(','))  # convert into list and separate with comma
        else:
            pass

    def add(self, fnum):
        self.flights.append(fnum)  # add flight number to list

    def remove(self, fnum):
        self.flights.remove(fnum)  # Remove flight number to list


class Parking:
    flights = []  # waiting flight number list

    def __init__(self, waiting=None):
        if waiting is not None:
            self.flights = list(waiting.strip().split(','))  # convert into list and separate with comma
        else:
            pass

    def add(self, fnum):
        self.flights.append(fnum)  # Add flight number to list

    def remove(self, fnum):
        self.flights.remove(fnum)  # last in first out of the list

    def __str__(self):
        return "There are " + str(len(self.flights)) + " planes in the waiting area"


# main
def main():
    landing = input("Initial Flights in the Landing Line :")
    if landing != "":
        land = Atc(landing)
    else:
        land = Atc()
    takoff = input("Initial Flights in the Take Off Line : ")
    if takoff != "":
        takeoff = Atc(takoff)
    else:
        takeoff = Atc()
    wait = input("Initial Flights in the Waiting Area : ")
    if wait != "":
        waiting = Parking(wait)
    else:
        waiting = Parking()

    while True:  # Loop for menu
        print("1. Land")
        print("2. Take Off")
        print("3. Start Waiting")
        print("4. Move from Waiting to Takeoff")
        print("5. Next")
        print("6. Quit")
        choice = int(input("Choice : "))
        if choice == 1:
            flight = input("Please enter a flight sign : ")  # enter flight sign
            print("LAND " + str(flight))
            print("There are " + str(len(land.flights)) + " planes waiting to land")  # waiting to land
            print("There are " + str(len(takeoff.flights)) + " planes waiting to takeoff")  # waiting to takeoff
            print(waiting)  # planes in waiting area
        elif choice == 2:
            t = input("Please enter a flight sign:")
            takeoff.flights.append(t)
            if len(land.flights) != 0:
                print("LAND " + land.flights[0])
                land.remove(land.flights[0])

            else:
                pass

            print("There are " + str(len(land.flights)) + " planes waiting to land")
            print("There are " + str(len(takeoff.flights)) + " planes waiting to takeoff")
            print(waiting)

        elif choice == 3:
            flight = input("Please enter a flight sign : ")  # enter flight sign
            waiting.flights.append(flight)  # adds flight to flight list
            if len(takeoff.flights) != 0:
                print("TAKEOFF " + takeoff.flights[0])
                takeoff.remove(takeoff.flights[0])  # remove plane from list
            else:
                pass

            print("There are " + str(len(land.flights)) + " planes waiting to land")  # planes waiting to land
            print("There are " + str(len(takeoff.flights)) + " planes waiting to takeoff")  # planes waiting to takeoff
            print(waiting)  # planes in waiting area

        elif choice == 4:

            if len(waiting.flights) != 0:
                print("TAKEOFF " + takeoff.flights[0])
                takeoff.add(waiting.flights[0])
                waiting.flights.remove(waiting.flights[0])
                takeoff.flights.remove(takeoff.flights[0])
            else:
                pass

            print("There are " + str(len(land.flights)) + " planes waiting to land")  # planes waiting to land
            print("There are " + str(len(takeoff.flights)) + " planes waiting to takeoff")  # planes waiting to takeoff
            print(waiting)  # planes in waiting area
        elif choice == 5:
            if len(land.flights) == 0:
                if len(takeoff.flights) != 0:
                    print("TAKEOFF " + takeoff.flights[0])
                elif len(waiting.flights) != 0:
                    takeoff.add(waiting.flights[-1])
                    waiting.flights.remove(waiting.flights[-1])  # remove from waiting list
                else:
                    pass
            else:
                print("LAND " + land.flights[0])
                land.remove(land.flights[0])  # remove plane from list
            if len(takeoff.flights) != 0:
                takeoff.flights.remove(takeoff.flights[0])
            else:
                pass
            print("There are " + str(len(land.flights)) + " planes waiting to land")  # planes waiting to land
            print("There are " + str(len(takeoff.flights)) + " planes waiting to takeoff")  # planes waiting to takeoff
            print(waiting)  # print the number of planes of waiting area

        elif choice == 6:
            break  # break the while loop
        else:
            print("Unknown choice ! Try again...")  # error message


if __name__ == '__main__':
    main()
