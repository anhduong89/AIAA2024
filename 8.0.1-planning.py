# Dec 9 2023
import argparse
import sys
import tempfile
import time
import copy
import subprocess
import re
import os
import pdb
#instance and program
input = 'rq.lp'
network = 'network.lp'
init = 'init.lp'    
program = '8.0.1-planning.lp'

# parser = argparse.ArgumentParser(description='Process input and optional files.')
# parser.add_argument('nb_drone', type=str, help='number of drones')
# parser.add_argument('nb_request', type=str, help='number of requests')
# parser.add_argument('run_for_request', type=str, help='run for request')
# parser.add_argument('run_for_drone', type=str, help='run for drone')

# args = parser.parse_args()
#INIT
total_cost = 0
avai = ''
assignment = ''
request = " "

start_time = time.time()
#asp
stop = False
i = 0
atom_pattern = re.compile(r'\b[a-zA-Z_]\w*\([^\)]*\)\.')
assignment_pattern = re.compile(r'as\(\d+(?:,\s*\d+)*\)')
iterationCost_pattern = re.compile(r'iteration_cost\((\d+),\s*\d+\)')
with open('auxilary.lp', 'w') as f:
    pass
optimum = True
totalCost = 0
while stop == False:
    # print(f'round {i}:')
    
    # command = f"clingo rq.lp network.lp init.lp 8.0.1-planning.lp auxilary.lp --time-limit=30 --outf=1 -V0 --quiet=1 -s2 -c timeConstant={i}"
    command = f"clingo example2.lp 8.0.1-planning.lp auxilary.lp --time-limit=30 --outf=1 -V0 --quiet=1 -c timeConstant={i}"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    
    atoms = atom_pattern.findall(result.stdout)
    
    if "OPTIMUM" not in result.stdout:
        optimum = False
     
    # with open(f'/home/anhd/Git/AIAA2024/log/{args.nb_request}_{args.run_for_request}_{args.nb_drone}_{args.run_for_drone}.txt', 'a') as f:
    #     f.write(result.stdout)
    print(result.stdout)
    # Process the extracted atoms as needed
    with open('auxilary.lp', 'w') as f:
        for atom in atoms:
            f.write(atom + '\n')
    # if "complete" in result.stdout:
    #     stop = True
    if i == 5: stop = True
        # print("number of time step:", i)
    # print(f'atom to next iteration:{atoms}')
    i+=1
    # if i > 6: break

iterationCost = iterationCost_pattern.findall(result.stdout)
iterationCost = [int(i) for i in iterationCost]
totalCost = sum(iterationCost)

end_time = time.time()
runTime = end_time - start_time
# with open('log.txt', "a") as f:
#     f.write(f' {args.nb_request}, {args.run_for_request}, {args.nb_drone}, {args.run_for_drone}, run_time: {runTime}, total_cost: {totalCost}, number of time step: {i}, optimum: {optimum}\n')



