RIGHT_ROTATE = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N'
}

LEFT_ROTATE = {
    'N': 'W',
    'W': 'S',
    'S': 'E',
    'E': 'N'
}


class MarsRover:
    """
    class to simulate a Mars rover.
    """

    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading

    def rotate_right(self):
        """rotate rover 90 degees clockwise."""
        self.direction = RIGHT_ROTATE[self.direction]

    def rotate_left(self):
        """rotate rover 90 degees counter clockwise."""
        self.direction = LEFT_ROTATE[self.direction]

    def move(self):
        """ moves the rover 1 grid square along current heading."""

        if self.heading == 'N':
            self.y += 1
        elif self.heading == 'E':
            self.x += 1
        elif self.heading == 'S':
            self.y -= 1
        elif self.heading == 'W':
            self.x -= 1

    def execute(self, command_string):
        """parse and execute single letter commands in
        a command string.

        L/R - turn 90 degrees left/right
        M   - move one grid square in the current heading.
        """

        for command in command_string:
            if command == 'L':
                self.rotate_left()

            elif command == 'R':
                self.rotate_right()

            elif command == 'M':
                self.move()

            else:
                raise ValueError("Unrecognized command '{command}'.")

    def __str__(self):
        return f"{self.x} {self.y} {self.heading}"


def main():
    # this should have some error checking
    coords = input("Enter x and y coordinate (e.g., 3 11): ")
    x, y = (int(s) for s in coords.strip().split())
    heading = input("Enter initial heading: ")

    rover = MarsRover(x, y, heading)

    while True:

        command_string = input("Please input directions for rover.")
        if command_string == '':
            break

        rover.execute(command_string)

        print(str(rover))


if __name__ == '__main__':
    main()
