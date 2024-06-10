import sys
import random
import os

atom = ''
part=[]
def get(val, default):
    return val if val != None else default


nAgents = int(sys.argv[1])


vPort_id = [0, 1, 2, 3, 4]

with open('init.lp',"w+") as f:

#gen agent
    f.write(f'agent(0..{nAgents}).\n')
    #gen init
    for id in range(0, nAgents):
        origin = random.choice(vPort_id)
        f.write(f'init_loc({id},{origin}).\n')




    
    