# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col):
        ''' (Rat, str, int, int) -> NoneType
        '''
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0
    
    def eat_sprout(self):
        self.num_sprouts_eaten += 1

    def __str__(self):
        return print(self.symbol + ' at (' + str(self.row) + ', ' + str(self.col) + ') ate ' + str(self.num_sprouts_eaten) + ' sprouts.')

class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        
        self.num_sprouts_left = 0
        for row in maze:
            for item in row:
                if item == SPROUT:
                    self.num_sprouts_left += 1

        rat_1_name = self.rat_1.symbol
        rat_1_row = self.rat_1.row
        rat_1_col = self.rat_1.col
        rat_2_name = self.rat_2.symbol
        rat_2_row = self.rat_2.row
        rat_2_col = self.rat_2.col
        self.maze[rat_1_row][rat_1_col] = rat_1_name
        self.maze[rat_2_row][rat_2_col] = rat_2_name
        
    def is_wall(self, row, col):
        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        return self.maze[row][col]

    def move(self, rat, ver, hor):
        ''' get rat 1/2,
        a number indicate verticle move,
        a number indicate horizontal move.
        '''
        # get current location of rat 1.
        rat_hor_pos = self.rat_1.row
        rat_ver_pos = self.rat_1.col
        # get current location of the rat passed.
        rat_2_hor_pos = self.rat_2.row
        rat_2_ver_pos = self.rat_2.col
        
        # find out what rat is passed:
        # if rat_1 is passed:
        if rat == self.rat_1:
            
            # check the spot the rat is going to:
            # where the rat is going to? : hor or ver?
            if ver == 0: # this mean the rat is not going verticle, hor has a value
                if hor == 1: # this mean the rat is going right
                    # check if right is a wall
                    if self.maze[rat_hor_pos][rat_ver_pos + 1] == WALL:
                        return False
                    elif self.maze[rat_hor_pos][rat_ver_pos + 1] == SPROUT:
                        #eat it
                        self.rat_1.num_sprouts_eaten += 1
                        #replace it with HALL
                        self.maze[rat_hor_pos][rat_ver_pos + 1] = HALL
                        # lower number of sprouts
                        self.num_sprouts_left -= 1
                        if rat_hor_pos == rat_2_hor_pos and rat_ver_pos == rat_2_ver_pos: #if rat1 on rat2
                            # change rat position
                            self.maze[rat_hor_pos][rat_ver_pos + 1] = RAT_1_CHAR
                            # change instance varible (rat's current location)
                            self.rat_1.col += 1
                            # reveal rat 2 back
                            self.maze[rat_hor_pos][rat_ver_pos] = RAT_2_CHAR
                            return True
                        else:
                            # delete rat's old position
                            self.maze[rat_hor_pos][rat_ver_pos] = HALL
                            # change rat position
                            self.maze[rat_hor_pos][rat_ver_pos + 1] = RAT_1_CHAR
                            # change instance varible (rat's current location)
                            self.rat_1.col += 1
                            return True       
                    else:
                        if rat_hor_pos == rat_2_hor_pos and rat_ver_pos == rat_2_ver_pos: #if rat1 on rat2
                            # change rat position
                            self.maze[rat_hor_pos][rat_ver_pos + 1] = RAT_1_CHAR
                            # change instance varible (rat's current location)
                            self.rat_1.col += 1
                            # reveal rat 2 back
                            self.maze[rat_hor_pos][rat_ver_pos] = RAT_2_CHAR
                            return True
                        else: 
                            # delete rat's old position
                            self.maze[rat_hor_pos][rat_ver_pos] = HALL
                            # change rat position
                            self.maze[rat_hor_pos][rat_ver_pos + 1] = RAT_1_CHAR
                            # change instance varible (rat's current location)
                            self.rat_1.col += 1
                            return True       
                else:
                    if self.maze[rat_hor_pos][rat_ver_pos - 1] == WALL: # check if left is a wall
                        return False
                    elif self.maze[rat_hor_pos][rat_ver_pos - 1] == SPROUT:
                        #eat it
                        self.rat_1.num_sprouts_eaten += 1
                        #replace it with HALL
                        self.maze[rat_hor_pos][rat_ver_pos - 1] = HALL
                        # lower number of sprouts
                        self.num_sprouts_left -= 1
                        if rat_hor_pos == rat_2_hor_pos and rat_ver_pos == rat_2_ver_pos: #if rat1 on rat2
                            # change rat position
                            self.maze[rat_hor_pos][rat_ver_pos - 1] = RAT_1_CHAR
                            # change instance varible (rat's current location)
                            self.rat_1.col -= 1
                            # reveal rat 2 back
                            self.maze[rat_hor_pos][rat_ver_pos] = RAT_2_CHAR
                            return True
                        else:     
                            # delete rat's old position
                            self.maze[rat_hor_pos][rat_ver_pos] = HALL
                            # change rat position
                            self.maze[rat_hor_pos][rat_ver_pos - 1] = RAT_1_CHAR
                            # change instance varible (rat's current location)
                            self.rat_1.col -= 1
                            return True
                    else:
                        if rat_hor_pos == rat_2_hor_pos and rat_ver_pos == rat_2_ver_pos: #if rat1 on rat2
                            # change rat position
                            self.maze[rat_hor_pos][rat_ver_pos - 1] = RAT_1_CHAR
                            # change instance varible (rat's current location)
                            self.rat_1.col -= 1
                            # reveal rat 2 back
                            self.maze[rat_hor_pos][rat_ver_pos] = RAT_2_CHAR
                            return True
                        else: 
                            # delete rat's old position
                            self.maze[rat_hor_pos][rat_ver_pos] = HALL
                            # change rat position
                            self.maze[rat_hor_pos][rat_ver_pos - 1] = RAT_1_CHAR
                            # change instance varible (rat's current location)
                            self.rat_1.col -= 1
                            return True
                        
            else:
                if ver == 1: #this mean the rat is going down
                    # check if down is a wall
                    if self.maze[rat_hor_pos + 1][rat_ver_pos] == WALL:
                        return False
                    elif self.maze[rat_hor_pos + 1][rat_ver_pos] == SPROUT:
                        #eat it
                        self.rat_1.num_sprouts_eaten += 1
                        #replace it with HALL
                        self.maze[rat_hor_pos + 1][rat_ver_pos] = HALL
                        # lower number of sprouts
                        self.num_sprouts_left -= 1
                        if rat_hor_pos == rat_2_hor_pos and rat_ver_pos == rat_2_ver_pos: #if rat1 on rat2
                            # change rat's position
                            self.maze[rat_hor_pos + 1][rat_ver_pos] = RAT_1_CHAR
                            # change instance varible (rat's current location)
                            self.rat_1.row += 1
                            # reveal rat 2 back
                            self.maze[rat_hor_pos][rat_ver_pos] = RAT_2_CHAR
                            return True
                        else:
                            # delete rat's old position
                            self.maze[rat_hor_pos][rat_ver_pos] = HALL
                            # change rat position
                            self.maze[rat_hor_pos + 1][rat_ver_pos] = RAT_1_CHAR
                            # change instance varible (rat's current location)
                            self.rat_1.row += 1
                            return True
                    else:
                        if rat_hor_pos == rat_2_hor_pos and rat_ver_pos == rat_2_ver_pos: #if rat1 on rat2
                            # change rat's position
                            self.maze[rat_hor_pos + 1][rat_ver_pos] = RAT_1_CHAR
                            # change instance varible (rat's current location)
                            self.rat_1.row += 1
                            # reveal rat 2 back
                            self.maze[rat_hor_pos][rat_ver_pos] = RAT_2_CHAR
                            return True
                        else: 
                            # delete rat's old position
                            self.maze[rat_hor_pos][rat_ver_pos] = HALL
                            # change rat position
                            self.maze[rat_hor_pos + 1][rat_ver_pos] = RAT_1_CHAR
                            # change instance varible (rat's current location)
                            self.rat_1.row += 1
                            return True
                else:
                    if self.maze[rat_hor_pos - 1][rat_ver_pos] == WALL: # check if up is a wall
                        return False
                    elif self.maze[rat_hor_pos - 1][rat_ver_pos] == SPROUT:
                        #eat it
                        self.rat_1.num_sprouts_eaten += 1
                        #replace it with HALL
                        self.maze[rat_hor_pos - 1][rat_ver_pos] = HALL
                        # lower number of sprouts
                        self.num_sprouts_left -= 1
                        if rat_hor_pos == rat_2_hor_pos and rat_ver_pos == rat_2_ver_pos: #if rat1 on rat2
                            # change rat position
                            self.maze[rat_hor_pos - 1][rat_ver_pos] = RAT_1_CHAR
                            # change instance varible (rat's current location)
                            self.rat_1.row -= 1
                            # reveal rat 2 back
                            self.maze[rat_hor_pos][rat_ver_pos] = RAT_2_CHAR
                            return True
                        else:
                            # delete rat's old position
                            self.maze[rat_hor_pos][rat_ver_pos] = HALL
                            # change rat position
                            self.maze[rat_hor_pos - 1][rat_ver_pos] = RAT_1_CHAR
                            # change instance varible (rat's current location)
                            self.rat_1.row -= 1
                            return True
                    else:
                        if rat_hor_pos == rat_2_hor_pos and rat_ver_pos == rat_2_ver_pos: #if rat1 on rat2
                            # change rat position
                            self.maze[rat_hor_pos - 1][rat_ver_pos] = RAT_1_CHAR
                            # change instance varible (rat's current location)
                            self.rat_1.row -= 1
                            # reveal rat 2 back
                            self.maze[rat_hor_pos][rat_ver_pos] = RAT_2_CHAR
                            return True
                        else: 
                            # delete rat's old position
                            self.maze[rat_hor_pos][rat_ver_pos] = HALL
                            # change rat position
                            self.maze[rat_hor_pos - 1][rat_ver_pos] = RAT_1_CHAR
                            # change instance varible (rat's current location)
                            self.rat_1.row -= 1
                            return True
                        
        else: # do for rat 2
            
            # check the spot the rat is going to:
            # where the rat is going to? : hor or ver?
            if ver == 0: # this mean the rat is not going verticle, hor has a value
                if hor == 1: # this mean the rat is going right
                    # check if right is a wall
                    if self.maze[rat_2_hor_pos][rat_2_ver_pos + 1] == WALL:
                        return False
                    elif self.maze[rat_2_hor_pos][rat_2_ver_pos + 1] == SPROUT:
                        #eat it
                        self.rat_2.num_sprouts_eaten += 1
                        #replace it with HALL
                        self.maze[rat_2_hor_pos][rat_2_ver_pos + 1] = HALL
                        # lower number of sprouts
                        self.num_sprouts_left -= 1
                        if rat_2_hor_pos == rat_hor_pos and rat_2_ver_pos == rat_ver_pos: 
                            # change rat position
                            self.maze[rat_2_hor_pos][rat_2_ver_pos + 1] = RAT_2_CHAR
                            # change instance varible (rat's current location)
                            self.rat_2.col += 1
                            # reveal rat 1 back
                            self.maze[rat_2_hor_pos][rat_2_ver_pos] = RAT_1_CHAR
                            return True
                        else:  
                            # delete rat's old position
                            self.maze[rat_2_hor_pos][rat_2_ver_pos] = HALL
                            # change rat position
                            self.maze[rat_2_hor_pos][rat_2_ver_pos + 1] = RAT_2_CHAR
                            # change instance varible (rat's current location)
                            self.rat_2.col += 1
                            return True   
                    else:
                        if rat_2_hor_pos == rat_hor_pos and rat_2_ver_pos == rat_ver_pos:
                            # change rat position
                            self.maze[rat_2_hor_pos][rat_2_ver_pos + 1] = RAT_2_CHAR
                            # change instance varible (rat's current location)
                            self.rat_2.col += 1
                            # reveal rat 1 back
                            self.maze[rat_2_hor_pos][rat_2_ver_pos] = RAT_1_CHAR
                            return True
                        else:    
                            # delete rat's old position
                            self.maze[rat_2_hor_pos][rat_2_ver_pos] = HALL
                            # change rat position
                            self.maze[rat_2_hor_pos][rat_2_ver_pos + 1] = RAT_2_CHAR
                            # change instance varible (rat's current location)
                            self.rat_2.col += 1
                            return True       
                else:
                    if self.maze[rat_2_hor_pos][rat_2_ver_pos - 1] == WALL: # check if left is a wall
                        return False
                    elif self.maze[rat_2_hor_pos][rat_2_ver_pos - 1] == SPROUT:
                        #eat it
                        self.rat_2.num_sprouts_eaten += 1
                        #replace it with HALL
                        self.maze[rat_2_hor_pos][rat_2_ver_pos - 1] = HALL
                        # lower number of sprouts
                        self.num_sprouts_left -= 1
                        
                        if rat_2_hor_pos == rat_hor_pos and rat_2_ver_pos == rat_ver_pos:
                            # change rat position
                            self.maze[rat_2_hor_pos][rat_2_ver_pos - 1] = RAT_2_CHAR
                            # change instance varible (rat's current location)
                            self.rat_2.col -= 1
                            # reveal rat 1 back
                            self.maze[rat_2_hor_pos][rat_2_ver_pos] = RAT_1_CHAR
                            return True
                        else:    
                            # delete rat's old position
                            self.maze[rat_2_hor_pos][rat_2_ver_pos] = HALL
                            # change rat position
                            self.maze[rat_2_hor_pos][rat_2_ver_pos - 1] = RAT_2_CHAR
                            # change instance varible (rat's current location)
                            self.rat_2.col -= 1
                            return True
                    else:
                        if rat_2_hor_pos == rat_hor_pos and rat_2_ver_pos == rat_ver_pos:
                            # change rat position
                            self.maze[rat_2_hor_pos][rat_2_ver_pos - 1] = RAT_2_CHAR
                            # change instance varible (rat's current location)
                            self.rat_2.col -= 1
                            # reveal rat 1 back
                            self.maze[rat_2_hor_pos][rat_2_ver_pos] = RAT_1_CHAR
                            return True
                        else:
                            # delete rat's old position
                            self.maze[rat_2_hor_pos][rat_2_ver_pos] = HALL
                            # change rat position
                            self.maze[rat_2_hor_pos][rat_2_ver_pos - 1] = RAT_2_CHAR
                            # change instance varible (rat's current location)
                            self.rat_2.col -= 1
                            return True
                        
            else:
                if ver == 1: #this mean the rat is going down
                    # check if down is a wall
                    if self.maze[rat_2_hor_pos + 1][rat_2_ver_pos] == WALL:
                        return False
                    elif self.maze[rat_2_hor_pos + 1][rat_2_ver_pos] == SPROUT:
                        #eat it
                        self.rat_2.num_sprouts_eaten += 1
                        #replace it with HALL
                        self.maze[rat_2_hor_pos + 1][rat_2_ver_pos] = HALL
                        # lower number of sprouts
                        self.num_sprouts_left -= 1
                        
                        if rat_2_hor_pos == rat_hor_pos and rat_2_ver_pos == rat_ver_pos:
                            # change rat position
                            self.maze[rat_2_hor_pos + 1][rat_2_ver_pos] = RAT_2_CHAR
                            # change instance varible (rat's current location)
                            self.rat_2.row += 1
                            # reveal rat 1 back
                            self.maze[rat_2_hor_pos][rat_2_ver_pos] = RAT_1_CHAR
                            return True
                        else:
                            
                            # delete rat's old position
                            self.maze[rat_2_hor_pos][rat_2_ver_pos] = HALL
                            # change rat position
                            self.maze[rat_2_hor_pos + 1][rat_2_ver_pos] = RAT_2_CHAR
                            # change instance varible (rat's current location)
                            self.rat_2.row += 1
                            return True
                    else:
                        if rat_2_hor_pos == rat_hor_pos and rat_2_ver_pos == rat_ver_pos:
                            # change rat position
                            self.maze[rat_2_hor_pos + 1][rat_2_ver_pos] = RAT_2_CHAR
                            # change instance varible (rat's current location)
                            self.rat_2.row += 1
                            # reveal rat 1 back
                            self.maze[rat_2_hor_pos][rat_2_ver_pos] = RAT_1_CHAR
                            return True
                        else:  
                            # delete rat's old position
                            self.maze[rat_2_hor_pos][rat_2_ver_pos] = HALL
                            # change rat position
                            self.maze[rat_2_hor_pos + 1][rat_2_ver_pos] = RAT_2_CHAR
                            # change instance varible (rat's current location)
                            self.rat_2.row += 1
                            return True
                else:
                    if self.maze[rat_2_hor_pos - 1][rat_2_ver_pos] == WALL: # check if up is a wall
                        return False
                    elif self.maze[rat_2_hor_pos - 1][rat_2_ver_pos] == SPROUT:
                        #eat it
                        self.rat_2.num_sprouts_eaten += 1
                        #replace it with HALL
                        self.maze[rat_2_hor_pos - 1][rat_2_ver_pos] = HALL
                        # lower number of sprouts
                        self.num_sprouts_left -= 1

                        if rat_2_hor_pos == rat_hor_pos and rat_2_ver_pos == rat_ver_pos:
                            # change rat position
                            self.maze[rat_2_hor_pos - 1][rat_2_ver_pos] = RAT_2_CHAR
                            # change instance varible (rat's current location)
                            self.rat_2.row -= 1
                            # reveal rat 1 back
                            self.maze[rat_2_hor_pos][rat_2_ver_pos] = RAT_1_CHAR
                            return True
                        else:
                            # delete rat's old position
                            self.maze[rat_2_hor_pos][rat_2_ver_pos] = HALL
                            # change rat position
                            self.maze[rat_2_hor_pos - 1][rat_2_ver_pos] = RAT_2_CHAR
                            # change instance varible (rat's current location)
                            self.rat_2.row -= 1
                            return True
                    else:
                        if rat_2_hor_pos == rat_hor_pos and rat_2_ver_pos == rat_ver_pos:
                            # change rat position
                            self.maze[rat_2_hor_pos - 1][rat_2_ver_pos] = RAT_2_CHAR
                            # change instance varible (rat's current location)
                            self.rat_2.row -= 1
                            # reveal rat 1 back
                            self.maze[rat_2_hor_pos][rat_2_ver_pos] = RAT_1_CHAR
                            return True
                        else:    
                            # delete rat's old position
                            self.maze[rat_2_hor_pos][rat_2_ver_pos] = HALL
                            # change rat position
                            self.maze[rat_2_hor_pos - 1][rat_2_ver_pos] = RAT_2_CHAR
                            # change instance varible (rat's current location)
                            self.rat_2.row -= 1
                            return True
                   
        
    def __str__(self):
        accu = ""
        repre_J = 'J at (' + str(self.rat_1.row) + ', ' + str(self.rat_1.col) + ') ate ' + str(self.rat_1.num_sprouts_eaten) + ' sprouts.'
        repre_P = 'P at (' + str(self.rat_2.row) + ', ' + str(self.rat_2.col) + ') ate ' + str(self.rat_2.num_sprouts_eaten) + ' sprouts.'
        for row in self.maze:
            for item in row:
                accu += item
            accu += '\n'
        accu += repre_J
        accu += '\n'
        accu += repre_P
        return accu

