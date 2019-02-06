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
OVER = 9

class Apocalypse(poc_grid.Grid):
    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []  
        self._grid_height = grid_height
        self._grid_width = grid_width
        
    def clear(self):
        self._human_list = []
        self._zombie_list = []
        poc_grid.Grid.clear(self)
        
    def add_zombie(self, row, col):
        self._zombie_list.append((row,col))
                
    def num_zombies(self):
        return len(self._zombie_list)       
          
    def zombies(self):
        for item in self._zombie_list:
            yield item

    def add_human(self, row, col):
        self._human_list.append((row,col))
        
    def num_humans(self): 
        return len(self._human_list) 
    
    def humans(self):  
        for item in self._human_list:
            yield item
        
    def compute_distance_field(self, entity_type):
        visited  = poc_grid.Grid(self._grid_height,self._grid_width)
        distance_field  = [[(self._grid_height*self._grid_width) for dummy_col in range(self._grid_width)] 
                       for dummy_row in range(self._grid_height)]
        boundary = poc_queue.Queue()
        if (entity_type==HUMAN):
            enum_l  = self._human_list[:]
        elif(entity_type==ZOMBIE):
            enum_l  = self._zombie_list[:]
        for row in (enum_l):
            visited.set_full(row[0],row[1])
            distance_field[row[0]][row[1]] = 0
            boundary.enqueue((row[0],row[1]))
        while len(boundary):
            cell = boundary.dequeue()
            neighbors = self.four_neighbors(cell[0], cell[1])
            for neighbor in neighbors:
                if visited.is_empty(neighbor[0], neighbor[1]) and self.is_empty(neighbor[0], neighbor[1]):
                    visited.set_full(neighbor[0], neighbor[1])
                    boundary.enqueue(neighbor)
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[cell[0]][cell[1]]+1
                
                
        
        return distance_field
    
    def move_humans(self, zombie_distance_field):
       
        index = 0
        value = []

        for hu_idx,human in enumerate(self._human_list):
            max_dist_from_zombie = 0
            coord_of_cell = ()
            neighbors = self.eight_neighbors(human[0],human[1])
            
            for neighbor in neighbors:
                if self.is_empty(neighbor[0], neighbor[1]):
                    if(zombie_distance_field[neighbor[0]][neighbor[1]] > max_dist_from_zombie) and (zombie_distance_field[neighbor[0]][neighbor[1]] > zombie_distance_field[human[0]][human[1]]):
                        max_dist_from_zombie = zombie_distance_field[neighbor[0]][neighbor[1]]
                        coord_of_cell = (neighbor[0],neighbor[1])
            if (len(coord_of_cell) != 0):
                human = (coord_of_cell[0],coord_of_cell[1])
                value = human
                index = hu_idx
                self._human_list[index] = value   

    def move_zombies(self, human_distance_field):
        
        index = 0
        value = []
        for zo_idx,zombie in enumerate(self._zombie_list):
            min_dist_to_hu = OVER
            coord_of_cell = ()
            neighbors = self.four_neighbors(zombie[0],zombie[1])
            
            for neighbor in neighbors:
                if self.is_empty(neighbor[0], neighbor[1]):
                    if(human_distance_field[neighbor[0]][neighbor[1]] < min_dist_to_hu) and (human_distance_field[neighbor[0]][neighbor[1]] < human_distance_field[zombie[0]][zombie[1]]):
                        min_dist_to_hu = human_distance_field[neighbor[0]][neighbor[1]]
                        coord_of_cell = (neighbor[0],neighbor[1])
            if (len(coord_of_cell) != 0):
                zombie = (coord_of_cell[0],coord_of_cell[1])
                value = zombie
                index = zo_idx
                self._zombie_list[index] = value   

    def __str__(self):
       
        ans = "Grid:"+"\n"
        for row in range(self._grid_height):
            ans += str(self._cells[row])
            ans += "\n"
        ans += "Humans: "+str(self._human_list)+"\n"
        ans += "Zombies: "+str(self._zombie_list)+"\n"
 
        return ans

poc_zombie_gui.run_gui(Apocalypse(25, 25))
