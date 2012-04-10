"""
Student Cable Car Class        
Author: Adam Oest (amo9149@rit.edu)
    
This is where you will be able to define all the
methods that control the flow of execution of the game

Uses the singleton pattern for easy accessibility
"""
from Model.interface import PlayerMove
from engineData import EngineData

"""
Cable Car: Student Engine Data

A sample class you may use to hold your state data
Author: Adam Oest (amo9149@rit.edu)
Author: Anthony Sinisi (ars3197@rit.edu)
Author: YOUR NAME HERE (your email address)
Author: YOUR NAME HERE (your email address)
"""
  
def init_config(configDict, tileList, logger):
    """
        PART: 1 and 3
        This function handles the first part of engine initialization.
        It needs to process the configuration data and initialize your
        tile database based on the tile list provided, as well as initialize
        any other data structures you may need
        
        configDict: dictionary of configuration values keyed as they 
                    appear in cablecar.cfg.  Values may be numbers,
                    booleans, or lists
                    
        tileList:   a list of letters representing the tile stack.
                    The first item in the list represents the top of the
                    stack (don't worry about this until part 3)
                    
        logger:     an instance of the engine logger 
                    (use logger.write(text) for messages)
                    
        returns -   EngineData: your engine state
    """

    # Put your data in here.  
    # This will be permanently accessible by you in all functions.
    engineData = EngineData(logger, configDict, tileList)
    
    # This is how you write data to the log file
    engineData.logger.write("Student engine starting up")
    
    # This is how you print out your data to standard output (not logged)
    print(engineData)
    
    return engineData
    
def validate_move(engineData, playerMove, testOnly = False):
    """
        PART: 3 / 1-2
        (In parts 1-2 this function will be called, but only to 
        inform you of the moves being made in the game, which are 
        guaranteed to be valid.  You won't have to do anything
        other than update your own board state)
        
        Validates the playerMove based on the engine's own state (part 3),
        and updates your engine board state (all parts).
        
        engineData:  your engine data, as always
        
        playerMove: the playerMove returned by the current player
        
                    You cannot assume that playerMove is a valid instance 
                    of the playerMove class.  You must check to see that
                    it is, check the playerId, check the tile, and check
                    the correctness of that tile's placement
                    
        testOnly:   if True, do not update your board state or check 
                    for correctness of playerId or tile letter
                    
        returns -   A 2-tuple: your EngineData, and
                    True if the move is valid, else False
                    If returning False, you must also print an error message
                    out via logger.error() stating why the move was
                    invalidated
    """
    
    location = playerMove.position
    row = location[0]
    column = location[1]
    engineData.grid[row][column] = [playerMove.tileName, playerMove.rotation]
    return engineData, False

def tile_info_at_coordinates(engineData, row, column):
    """The engine calls this function during 
        part 1 to validate your board state.
    
    Parameters:
        engineData - your engine data, as always
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
        
    tileName = engineData.grid[row][column][0]
    tileRotation = engineData.grid[row][column][1]
    
    return tileName, tileRotation

def tile_tracks(engineData, row, column, entry):
    """The engine calls this function 
        during part 1 to validate your tile tracks
    
    Parameters:
        engine - your engine data as always
        row - the tile row (0-7)
        column - the tile column (0-7)
        entry - the point of entry on this time
                one of NL, NR, ET, EB, SR, SL, WB, WT
        
    You return:
        exit - where you end up if you follow the track from the entry point 
                one of NL, NR, ET, EB, SR, SL, WB, WT
                depending on where the tile track exists
    """
    
    tile = engineData.grid[row][column]
    if tile[0] == "a":
        routelist = [1,0,7,6,5,4,3,2]
    if tile[0] == "b":
        routelist = [3,4,7,0,1,6,5,2]
    if tile[0] == "c":
        routelist = [3,4,5,0,1,2,7,6]
    if tile[0] == "d":
        routelist = [1,0,7,4,3,6,5,2]
    if tile[0] == "e":
        routelist = [1,0,3,2,7,6,5,4]
    if tile[0] == "f":
        routelist = [5,4,7,6,1,0,3,2]
    if tile[0] == "g":    
        routelist = [1,0,3,2,5,4,7,6]
    if tile[0] == "h":    
        routelist = [7,2,1,4,3,6,5,0]
    if tile[0] == "i":   
        routelist = [3,6,5,0,7,2,1,4]
    if tile[0] == "j":   
        routelist = [7,6,5,4,3,2,1,0]
        
        
    mapping = ["NL", "NR", "ET", "EB", "SR", "SL", "WB", "WT"]         
    comingin = mapping.index(entry)          
    goingout = routelist[comingin]
        
            
    if tile[1] == 1:
        comingin = (mapping.index(entry) - 2) % 8
        goingout = (routelist[comingin] + 2) % 8
    if tile[1] == 2:
        comingin = (mapping.index(entry) - 4) % 8
        goingout = (routelist[comingin] + 4) % 8
    if tile[1] == 3:
        comingin = (mapping.index(entry) - 6) % 8
        goingout = (routelist[comingin] + 6) % 8
            
            
    exit = mapping[goingout]
    
    return exit

def route_complete(engineData, carId):
    """The engine calls this function 
        during part 2 to validate your route checking
    
    Parameters:
        engineData - your engine data as always
        carId - the id of the car where the route starts (1-32)
        
    You return:
        isComplete - true or false depending on whether or not this car
             connects to another car or power station"""
    
    isComplete = None
    
    return isComplete

def route_score(engineData, carId):
    """The engine calls this function 
        during part 2 to validate your route scoring
    
    Parameters:
        engineData - your engine data as always
        carId - the id of the car where the route starts (1-32)
        
    You return:
        score - score is the length of the current route from the carId.
                if it reaches the power station, 
                the score is equal to twice the length.
    """
    
    score = None
    
    return score

def init_players(engineData, playerRefs):
    """
        PART: 3
        This function initializes the player modules in the game. You
        need to call .init() for every player module in the game.
                                
        engineData:  your engine data, as always

        playerRef: a list of references to player modules 
                   you need to call init() on the module with the following
                   arguments -
                   playerId: the playerId of this module
                   numPlayers: the total number of players
                   startTiles: a list of each player's starting tile,
                               such that startTiles[playerId] is the current
                               player's tile
                   logger:     reference to the engine logger
                   arg:        player argument as specified in the config 
                               file. Defaults to "None" (a string) if
                               the config value is empty or invalid
                               
                   returns -   playerData for this player
        
        returns -  a 2-tuple: your EngineData and 
                   a list of the playerData objects the players returned,
                   indexed by player id
                   
                   remember to also store this
                   playerData in your own internal state as you will need to
                   pass it back to the player modules when move and 
                   move_info is called through your nextMove method
    """
    
    return engineData, []

def next_move(engineData, playerRefs):
    """
        PART: 4
        Processes the next move.  Needs to fetch the move from the
        current player, validate it, and then call move_info
        on all players.  Remember to also store the playerData   
        
        engineData:  your engine data, as always

        playerRefs: a list of references to all player modules,
                    keyed by playerId
                    you need to call .move(playerData) for the current
                    player, followed by .move_info(playerData, playerMove,
                    the next tile of the current player) for all players
                     
        returns:    a 4-tuple with your engine data, the returned playerMove, 
                    validity (True or False) and updated playerData 
                    (but don't call move_info if validity == False)
    """
    
    return engineData, None, False, []

def game_over(engineData, historyFileName = None):
    """
        PART: 1-3
        Called once the game is over.  Use it for unit testing.
    
        PART: 4
        Called once the game is over.  Returns scores, player validity,
        and the winner.
        
        engineData:  your engine data, as always
        historyFileName: the name of the current history file
        
        returns -    for part 4 only: 3-tuple with: engine data,winners 
                    (an ordered LIST of ids),scores (a LIST indexed by playerId)
    """
    
    # Test things here, changing the function calls...
    if historyFileName != None:
        print "History File: %s" % historyFileName
        print "If it says False below, you are doing something wrong"
        
        if historyFileName == "03-29-12_02-07-59_history.data":
            print tile_info_at_coordinates(engineData, 5, 2)
            print tile_tracks(engineData, 5, 2, 'NL')
        elif historyFileName == "03-29-12_02-08-37_history.data":
            print "Second history file test cases here..."
        elif historyFileName == "03-29-12_02-09-17":
            print "Third history file test cases here..."
            
    return engineData, [], []

# Dont't edit this class
class StudentEngine:
    __slots__ = ('EngineData')
    def initConfig(self, configDict, tileList, logger):
        self.EngineData = init_config(configDict, tileList, logger)
    def validateMove(self, playerMove, testOnly = False):
        self.EngineData, validity = validate_move(self.EngineData, playerMove, testOnly)
        return validity
    def initPlayers(self, playerRefs):
        self.EngineData, lst = init_players(self.EngineData, playerRefs)
        return lst
    def nextMove(self, playerRefs):        
        self.EngineData, move, validity, playerData = next_move(self.EngineData, playerRefs)
        return move, validity, playerData
    def gameOver(self, historyFileName):
        self.EngineData, winners, scores = game_over(self.EngineData, historyFileName)
        return winners, scores
    def tileInfoAtCoordinates(self, row, column):                    
        return tile_info_at_coordinates(self.EngineData, row, column)
    def tileTracks(self, row, column, entry):        
        return tile_tracks(self.EngineData, row, column, entry)
    def routeComplete(self, carId):        
        return route_complete(self.EngineData, carId)
    def routeScore(self, carId):        
        return route_score(self.EngineData, carId)
    instance = None
    class Singleton:
        def __call__(self, *args, **kw) :
            if StudentEngine.instance is None:
                StudentEngine.instance = StudentEngine()
            return StudentEngine.instance
    def __init__(self):
        if self.instance != None:
            raise Exception('ENGINE cannot be initialized directly')
    getInstance = Singleton()
