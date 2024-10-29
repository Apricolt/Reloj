from CircularList import CircularList
from datetime import datetime

# Clock class representing the clock using circular lists for hours, minutes, and seconds
class Clock:
    def __init__(self):
        # Initialize circular lists for hours, minutes, and seconds
        self.hours = CircularList()
        self.minutes = CircularList()
        self.seconds = CircularList()
        self.initialize_clock()

        # Set the current node for hours, minutes, and seconds
        now = datetime.now()
        self.current_hour = self.get_node_at_position(self.hours, now.hour % 12)
        self.current_minute = self.get_node_at_position(self.minutes, now.minute)
        self.current_second = self.get_node_at_position(self.seconds, now.second)

    # Initializes the values in the circular lists
    def initialize_clock(self):
        for i in range(12):
            self.hours.add(i + 1)
        for i in range(60):
            self.minutes.add(i)
            self.seconds.add(i)

    # Gets the node at a specific position within the circular list
    def get_node_at_position(self, circular_list, position):
        node = circular_list.get_head()
        for _ in range(position):
            node = node.next
        return node

    # Function that advances the seconds and updates minutes and hours as needed
    def tick(self):
        if self.current_second and self.current_second.next:
            self.current_second = self.current_second.next
        if self.current_second.data == 0 and self.current_minute and self.current_minute.next:
            self.current_minute = self.current_minute.next
        if self.current_minute.data == 0 and self.current_hour and self.current_hour.next:
            self.current_hour = self.current_hour.next

    # Returns the current time in text format
    def get_current_time(self):
        return f"{self.current_hour.data:02}:{self.current_minute.data:02}:{self.current_second.data:02}"
