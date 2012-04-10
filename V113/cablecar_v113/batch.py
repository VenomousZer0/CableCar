"""
Batch program for the Cable Car game.  The program can be run with one
command line argument which is the name of the config file.    

Place this file in the same directory as cablecar.py

Author: Adam Oest (amo9149@rit.edu)
"""

import Engine
import time
import sys
from Engine.config import Config

def main():
    """Run the engine and start the game"""
    
    sys.setcheckinterval(500)
            
    if len(sys.argv) == 1:
        sys.argv.append("cablecar.cfg")
        
    wins = {}
    scores = {}
    
    games = abs(int(raw_input("Enter number of games: ")))
    
    # Get config
    cfg = Config(sys.argv[1])
    cfg.data['UI'] = False
    cfg.data['STDOUT_LOGGING'] = False
    tt = 0
    
    for game in xrange(1, games + 1):
        startTime = time.clock()
        winningPlayer, score, eliminated, moves = Engine.run(cfg)
        endTime = time.clock()
        if len(eliminated) > 0:
            print "Players errored: %s" % eliminated

        print "Game %s time: %s seconds" % (game, endTime - startTime)
        tt += (endTime - startTime)

        if winningPlayer != []:
            for player in winningPlayer:
                if player not in wins.keys():
                    wins[player] = 1
                    scores[player] = [score[player]]
                else:
                    wins[player] += 1
                    scores[player].append(score[player])        
            print "Player %s won the game with %s points!" % (winningPlayer, score) 
        else:
            print "No winner."

    for player,wins in wins.iteritems():
        print "Player %s won %s times" % (player, wins)
        score = 0
        for num in scores[player]:
            score += num
        print "Total Score: %s" % score
    print "Total Time: %s" % tt
                
if __name__ == "__main__":
    main()
    
#import profile
#profile.run("main()")