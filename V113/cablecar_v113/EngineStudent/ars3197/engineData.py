"""
Cable Car: Student Computer Player

A sample class you may use to hold your state data
Author: Adam Oest (amo9149@rit.edu)
Author: YOUR NAME HERE (your email address)
Author: YOUR NAME HERE (your email address)
Author: YOUR NAME HERE (your email address)
"""


class EngineData(object):
    """A sample class for your engine data"""
    
    # Add other slots as needed
    __slots__ = ('logger', 'configDict', 'tileList', 'grid')
    
    def __init__(self, logger, configDict, tileList):
        """
        __init__: PlayerData * Engine.Logger * int * NoneType * int -> None
        Constructs and returns an instance of PlayerData.
            self - new instance
            logger - the engine logger
            configDict - dictionary of configuration values keyed as they 
                        appear in cablecar.cfg.  Values may be numbers,
                        booleans, or lists
            tileList: a list of letters representing the tile stack.
                    The first item in the list represents the top of the
                    stack (don't worry about this until part 3)
        """
        
        self.logger = logger
        self.configDict = configDict
        self.tileList = tileList
        
        # initialize any other slots you require here
        self.grid = [[None for col in range(8)] for row in range(8)]
        self.grid[3][3] = ["ps", 0]
        self.grid[3][4] = ["ps", 0]
        self.grid[4][3] = ["ps", 0]
        self.grid[4][4] = ["ps", 0]
        
        
    def __str__(self):
        """
        __str__: EngineData -> string
        Returns a string representation of the EngineData object.
            self - the EngineData object
        """
        result = "EngineData= " \
                    + "logger: " + str(self.logger) \
                    + ", configDict: " + str(self.configDict) \
                    + ", tileList: " + str(self.tileList)
                
        # add any more string concatenation for your other slots here
                
        return result