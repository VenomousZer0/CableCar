from Model.interface import PlayerMove
from playerData import PlayerData

"""
Cable Car: Student Computer Player

Complete these function stubs in order to implement your AI.
Author: Adam Oest (amo9149@rit.edu)
Author: YOUR NAME HERE (your email address)
Author: YOUR NAME HERE (your email address)
Author: YOUR NAME HERE (your email address)
"""

def init(playerId, numPlayers, startTiles, logger, arg = "None"):
    """The engine calls this function at the start of the game in order to:
        -tell you your player id (0 through 5)
        -tell you how many players there are (1 through 6)
        -tell you what your start tile is (a letter a through i)
        -give you an instance of the logger (use logger.write("str") 
            to log a message) (use of this is optional)
        -inform you of an additional argument passed 
            via the config file (use of this is optional)
        
    Parameters:
        playerId - your player id (0-5)
        numPlayers - the number of players in the game (1-6)
        startTiles - a list of all players' tiles, 
                     yours is at startTiles[playerId]
        logger - and instance of the logger object
        arg - an extra argument as specified via the config file (optional)

    You return:
        playerData - your player data, which is any data structure
                     that contains whatever you need to keep track of.
                     Consider this your permanent state.
    """
    
    # Put your data in here.  
    # This will be permanently accessible by you in all functions.
    # It can be an object, list, or dictionary
    playerData = PlayerData(logger, playerId, startTiles[playerId], numPlayers)

    # This is how you write data to the log file
    playerData.logger.write("Player %s starting up" % playerId)
    
    # This is how you print out your data to standard output (not logged)
    print(playerData)
    
    return playerData

def move(playerData):  
    """The engine calls this function when it wants you to make a move.
    
    Parameters:
        playerData - your player data, 
            which contains whatever you need to keep track of
        
    You return:
        playerData - your player data, 
            which contains whatever you need to keep track of
        playerMove - your next move
    """
    
    playerData.logger.write("move() called")

    # Populate these values
    playerId = None # 0-5
    position = None # (row, column)
    tileName = None # a-j
    rotation = None # 0-3 (0 = north, 1 = east, 2 = south, 3 = west)
    
    return playerData, PlayerMove(playerId, position, tileName, rotation)

def move_info(playerData, playerMove, nextTile):
    """The engine calls this function to notify you of:
        -other players' moves
        -your and other players' next tiles
        
    The function is called with your player's data, as well as the valid move of
    the other player.  Your updated player data should be returned.
    
    Parameters:
        playerData - your player data, 
            which contains whatever you need to keep track of
        playerMove - the move just made 
                     or None if you've already made your planned
                     last move and some other player ends up crashing, leaving
                     you next in line: in this case, you will have to make 
                     one last move using the tile that's passed via nextTile
        nextTile - the next tile for the player specified in playerMove, 
                    or if playerMove is None, then it's your own next tile
    You return:
        playerData - your player data, 
            which contains whatever you need to keep track of
    """
    
    playerData.logger.write("move_info() called")
    
    return playerData


################################# PART ONE FUNCTIONS #######################
# These functions are called by the engine during part 1 to verify your board 
# data structure
# If logging is enabled, the engine will tell you exactly which tests failed
# , if any

def tile_info_at_coordinates(playerData, row, column):
    """The engine calls this function during 
        part 1 to validate your board state.
    
    Parameters:
        playerData - your player data as always
        row - the tile row (0-7)
        column - the tile column (0-7)
    
    You return:
        tileName - the letter of the tile at the given coordinates (a-j), 
            or 'ps' if power station or None if no tile
        tileRotation - the rotation of the tile 
            (0 is north, 1 is east, 2 is south, 3 is west.
            If the tile is a power station, it should be 0.  
            If there is no tile, it should be None.
    """      
        
    tileName = False
    tileRotation = False
    
    return tileName, tileRotation

def tile_tracks(playerData, row, column, entry):
    """The engine calls this function 
        during part 1 to validate your tile tracks
    
    Parameters:
        playerData - your player data as always
        row - the tile row (0-7)
        column - the tile column (0-7)
        entry - the point of entry on this time
                one of NL, NR, ET, EB, SR, SL, WB, WT
        
    You return:
        exit - where you end up if you follow the track from the entry point 
                one of NL, NR, ET, EB, SR, SL, WB, WT
                depending on where the tile track exists
    """
    
    exit = None
    
    return exit

def route_complete(playerData, carId):
    """The engine calls this function 
        during part 2 to validate your route checking
    
    Parameters:
        playerData - your player data as always
        carId - the id of the car where the route starts (1-32)
        
    You return:
        isComplete - true or false depending on whether or not this car
             connects to another car or power station"""
    
    isComplete = None
    
    return isComplete

def route_score(playerData, carId):
    """The engine calls this function 
        during part 2 to validate your route scoring
    
    Parameters:
        playerData - your player data as always
        carId - the id of the car where the route starts (1-32)
        
    You return:
        score - score is the length of the current route from the carId.
                if it reaches the power station, 
                the score is equal to twice the length.
    """
    
    score = None
    
    return score

def game_over(playerData, historyFileName = None):
    """The engine calls this function after the game is over 
        (regardless of whether or not you have been kicked out)

    You can use it for testing purposes or anything else you might need to do...
    
    Parameters:
        playerData - your player data as always       
        historyFileName - name of the current history file, 
            or None if not being used 
            
    Returns (part 3 and 4):
        scores: a LIST of scores indexed by player id
    """
    
    # Test things here, changing the function calls...
    print "History File: %s" % historyFileName
    print "If it says False below, you are doing something wrong"
    
    if historyFileName == "example_complete_start.data":
        print tile_info_at_coordinates(playerData, 5, 2) == ('e', 0)
        print tile_tracks(playerData, 5, 2, 'NL') == 'NR'
    elif historyFileName == "SECOND_HISTORY_FILE_NAME":
        print "Second history file test cases here..."
    elif historyFileName == "THIRD_HISTORY_FILE_NAME":
        print "Third history file test cases here..."
        
    return []
    
    