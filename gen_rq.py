import sys
import random
import os
nb_request = int(sys.argv[1])
nb_time_step = int(sys.argv[2])
vPort_id = [0, 1, 2, 3, 4]

with open('rq.lp',"w+") as f:
#gen total request
    f.write(f'total_request({nb_request}).\n')
    #gen horizon
    f.write(f'horizon({nb_time_step}).\n')
    #gen request

    for id in range(0, nb_request):
        origin, destination = random.sample(vPort_id, 2)
        time_step = random.choice(range(0, nb_time_step))
        f.write(f'request({id},{origin},{destination}, 20, {time_step}).\n')



