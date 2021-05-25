"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list=None,
                 zombie_list=None, human_list=None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list is not None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list is not None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list is not None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list, self._human_list = [], []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        return (zombie for zombie in self._zombie_list)

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        return (human for human in self._human_list)

    def _fill_creature_data_structures(self, creatures):
        visited = poc_grid.Grid(self._grid_height, self._grid_width)
        distance_field = [[-1 for dummy_col in range(self._grid_width)]
                          for dummy_row in range(self._grid_height)]
        boundary = poc_queue.Queue()

        for creature in creatures:
            boundary.enqueue(creature)
            visited.set_full(creature[0], creature[1])
            distance_field[creature[0]][creature[1]] = 0

        return visited, distance_field, boundary

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        if entity_type == HUMAN:
            creatures = self.humans()
        if entity_type == ZOMBIE:
            creatures = self.zombies()

        visited, distance_field, boundary = self._fill_creature_data_structures(creatures)

        while boundary:
            cell = boundary.dequeue()
            neighbors = visited.four_neighbors(cell[0], cell[1])
            for neighbor in neighbors:
                if visited.is_empty(neighbor[0], neighbor[1]):
                    visited.set_full(neighbor[0], neighbor[1])
                    boundary.enqueue(neighbor)
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[cell[0]][cell[1]] + 1

        return distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        for index_human in range(len(self._human_list)):
            human = self._human_list[index_human]
            distance = zombie_distance_field[human[0]][human[1]]
            movement_directions = [human]
            neighbors = self.eight_neighbors(human[0], human[1])

            for neighbor in neighbors:
                if self.is_empty(neighbor[0], neighbor[1]):
                    if zombie_distance_field[neighbor[0]][neighbor[1]] > distance:
                        distance = zombie_distance_field[neighbor[0]][neighbor[1]]
                        movement_directions = [neighbor]
                    elif zombie_distance_field[neighbor[0]][neighbor[1]] == distance:
                        movement_directions.append(neighbor)

            self._human_list[index_human] = random.choice(movement_directions)

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for index_zombie in range(len(self._zombie_list)):
            zombie = self._zombie_list[index_zombie]
            distance = human_distance_field[zombie[0]][zombie[1]]
            movement_directions = [zombie]
            neighbors = self.four_neighbors(zombie[0], zombie[1])

            for neighbor in neighbors:
                if self.is_empty(neighbor[0], neighbor[1]):
                    if human_distance_field[neighbor[0]][neighbor[1]] < distance:
                        distance = human_distance_field[neighbor[0]][neighbor[1]]
                        movement_directions = [neighbor]
                    elif human_distance_field[neighbor[0]][neighbor[1]] == distance:
                        movement_directions.append(neighbor)

            self._zombie_list[index_zombie] = random.choice(movement_directions)


poc_zombie_gui.run_gui(Apocalypse(30, 40))
