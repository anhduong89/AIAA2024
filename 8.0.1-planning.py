# Dec 9 2023
import clingo
from clingo.symbol import Function
from clingo.symbol import Number
from clingo import symbol
import sys
import tempfile
import time

# 

def on_model(model):
    print("Found solution:", model)
    
def get_atom(name, arg):
    atom_arg = []
    for i in arg:
        # if len(str(i)) > 1:
        #     atom_arg += .join(str(i))
        # else:
        # print(i)
        atom_arg += [str(i)]
        # if name == 'new_request':
        #     print('arg=', arg)

    atom_full = name +'(' + ','.join(atom_arg) +'). ' 

    return atom_full



#instance and program
input = 'rq.lp'
network = 'network.lp'
init = 'init.lp'    
program = '8.0.1-planning.lp'



#INIT
total_cost = 0
avai = ''
assignment = ''
request = " "
start_time = time.process_time()
#asp
stop = False
i = 0
while stop == False:
    
    atom = 'time(' + str(i) + ').'
    prog1 = clingo.Control(["0", "--opt-mode=optN"])
    prog1.add(request)
    request = ''
    prog1.add(atom)
    prog1.add(avai)
    prog1.add(assignment)
    prog1.load(program)
    prog1.load(input)
    prog1.load(network)
    prog1.load(init)
    #display
    # print('available agent round ', i, ':', avai)
    # print('incomplete_request :', request)
    lenAS = len(assignment)
    prog1.ground([("base", [])])
    with prog1.solve(yield_=True, async_=True) as models: # type: ignore
        models.wait(600)
        
        min_cost = float('inf')
        for model in models:
        # print(f'Optimal:{models.optimality_proven}\n')
            
            if model.cost[0] < min_cost:
                min_model = model
            
        for atom in model.symbols(atoms=True):
            if atom.name == "avai":
                avai += get_atom(atom.name, atom.arguments)
            if atom.name == "as":
                assignment += get_atom(atom.name, atom.arguments)
            if atom.name =='incomplete_request':
                request += get_atom("new_request", atom.arguments)
            if atom.name =='iteration_cost':
                total_cost += (atom.arguments[0].number)
            if atom.name =='complete':
                stop = True
        models.cancel()               
    i+=1
    # if len(assignment) == lenAS: break
    # if i ==11: break
# print('output:', avai)
end_time = time.process_time()
running_time = end_time - start_time
with open('log.txt', "a") as f:
    f.write(f'running_time: {running_time}\n')




