import pygame
from pygame.draw import circle, rect
from random import randint, uniform
from math import hypot, cos, sin, pi


class Target:
    """Describes a target"""

    def __init__(self, position, velocity, r, color, type1):
        """Initialization"""

        self.position = list(position)
        self.velocity = list(velocity)
        self.r = r
        self.color = color
        self.type = type1

    def draw(self, screen):
        """Draws target on screen"""
        if self.type == "circle":
            circle(screen, self.color, self.position, self.r)
        if self.type == "square":
            rect(screen, self.color, (self.position[0] - self.r, self.position[1] - self.r, 2 * self.r, 2 * self.r))

    def is_inside(self, point):
        """Returns if point is inside target"""
        if self.type == "circle":
            return hypot(point[0] - self.position[0], point[1] - self.position[1]) <= self.r
        if self.type == "square":
            return abs(point[0] - self.position[0]) <= self.r and abs(point[1] - self.position[1]) <= self.r


class Counter:
    """Counter"""

    def __init__(self):
        """Initialization"""

        self.value = 0

    def increase(self):
        """Increases value of counter"""

        self.value += 1

    def value(self):
        """Counter's value"""

        return self.value


# Max fps
FPS = 30
# Colors in RGB
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
# Resolution
WIDTH = 1280
HEIGHT = 960
RESOLUTION = (WIDTH, HEIGHT)
# New balls appearing per second
TARGETS_PER_SECOND = 1 / 4
# Maximum number of targets
MAX_TARGETS = 5
# Types of targets
TYPES = ["circle", "square"]
# Time interval
TIME = 1

pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
points = []
score_counter = Counter()
frame_counter = Counter()


def new_ball():
    """Appends a new ball to list"""
    points.append(Target((randint(100, 700), randint(100, 500)), (randint(-40, 40), randint(-40, 40)), randint(30, 50),
                         COLORS[randint(0, 5)], TYPES[randint(0, 1)]))


def draw_balls():
    """Draws all balls"""
    for point in points:
        point.draw(screen)


def quit_event_handler():
    """Handles a quit event"""
    pass


def click_event_handler(event1):
    """Handles click event"""

    def process_point(point):
        """If mouse pointer is in shape, increases score and removes point"""
        if point.is_inside(event1.pos):
            score_counter.increase()
            points.remove(point)

    for point in points:
        process_point(point)


def move_points(time):
    """Changes points' positions, takes time interval"""

    def move_point(point, time):
        """Changes point position, takes point and time interval"""

        # Different movement for squares
        if point.type == "square":
            point.velocity[0] -= int(time * 5 * (point.position[0] - RESOLUTION[0] / 2) / RESOLUTION[0])
            point.velocity[1] -= int(time * 5 * (point.position[1] - RESOLUTION[1] / 2) / RESOLUTION[1])

            if point.velocity[0] > RESOLUTION[0] / 10:
                point.velocity[0] = RESOLUTION[0] / 10
            if point.velocity[1] > RESOLUTION[1] / 10:
                point.velocity[1] = RESOLUTION[1] / 10

        # Compute time to achieve borders
        tx = ((RESOLUTION[0] - point.r - point.position[0]) / point.velocity[0] if point.velocity[0] > 0 else
              -(point.position[0] - point.r) / point.velocity[0]) if point.velocity[0] != 0 else RESOLUTION[0]
        ty = ((RESOLUTION[1] - point.r - point.position[1]) / point.velocity[1] if point.velocity[1] > 0 else
              -(point.position[1] - point.r) / point.velocity[1]) if point.velocity[1] != 0 else RESOLUTION[1]

        # If target won't achieve borders, compute and return
        if tx > time and ty > time:
            for i in range(2):
                point.position[i] += time * point.velocity[i]
            return
        # Change position to achieve border
        t = tx if tx - ty < 0 else ty  # min(tx, ty)
        for i in range(2):
            point.position[i] += (time - t) * point.velocity[i]

        # Get random angle
        phi = uniform(0.1, pi - 0.1)
        # Change velocity
        vel = hypot(*point.velocity)

        # Reflect
        if tx == min(tx, ty):
            point.velocity[0] = (-1 if point.position[0] > RESOLUTION[0] / 2 else 1) * vel * sin(phi)
            point.velocity[1] = vel * cos(phi)
        else:
            point.velocity[1] = (-1 if point.position[1] > RESOLUTION[1] / 2 else 1) * vel * sin(phi)
            point.velocity[0] = vel * cos(phi)

        # Move for remaining time interval
        move_point(point, time - t)

    # Move all points
    for point in points:
        move_point(point, time)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    frame_counter.increase()
    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            quit_event_handler()
            finished = True
        # Mouse down
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_event_handler(event)
    # Move points
    move_points(TIME)
    # Create a new ball if it is necessary
    if frame_counter.value / FPS * TARGETS_PER_SECOND > len(points) and MAX_TARGETS > len(points):
        new_ball()
    # Update screen
    draw_balls()
    pygame.display.update()
    screen.fill(BLACK)

print(f"Score: {score_counter.value}")
pygame.quit()
