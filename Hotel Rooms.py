# room.py

class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people: int):
        if not self.is_taken and self.capacity >= people:
            self.is_taken = True
            self.guests = people
        else:
            return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0
        else:
            return f"Room number {self.number} is not taken"
# hotel.py



class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room:
            result = room.take_room(people)
            if result is None:  # Room was successfully taken
                self.guests += people
            return result

    def free_room(self, room_number: int):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room:
            result = room.free_room()
            if result is None:  # Room was successfully freed
                self.guests -= room.guests
            return result

    def print_status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]

        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {', '.join(free_rooms)}")
        print(f"Taken rooms: {', '.join(taken_rooms)}")



hotel = Hotel.from_stars(5)
first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)  # Attempt to take room 1 with 4 guests (should fail)
hotel.take_room(1, 2)  # Take room 1 with 2 guests (should succeed)
hotel.take_room(3, 1)  # Take room 3 with 1 guest (should succeed)
hotel.take_room(3, 1)  # Attempt to take room 3 again (should fail)

hotel.print_status()
