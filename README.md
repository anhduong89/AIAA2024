## requirement
- clingo-dl
- python
## content
gen_init.py             : generate random initial location of agent

gen_rq.py               : generate trip request (random origin and destination)

init.lp                 : initial location instance

network.lp              : network instance (vertiport, arc)

rq.lp                   : request instance

solver_all.sh           : reproduce all experiments

8.0.1-planning.lp       : single-step planning program (pi)

8.0.1-planning.py       : iterative caller(Algorithm 1)

timeSchedule.lp         : time schedule program (pi_dl)
## hyper-parameter

8.0.1-planning.py:
                    nb_drone : number of drone
                    nb_request: number of request
                    run_for_request: how many times you want to sampling the request
                    run_for_drone: how many times you want to sampling the initial location of agent

## usage
TO reproduce all experiments:
```bash
./solver.sh
```

TO run solely experiment
```bash
python 8.0.1-planning.py nb_drone=X nb_request=Y run_for_request=Z run_for_drone=W
```

replace X, Y, Z, W by your choice.
