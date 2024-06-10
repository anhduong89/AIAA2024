#!/bin/bash
for nb_drone in 5 10 20 40
do
    for nb_request in 15 30 45
    do
        echo "nb_drone: $nb_drone, nb_request: $nb_request\n" >> log.txt
        for run in {1..5}
        do
            echo "Run $run :" >> log.txt
            python3 gen_init.py nb_drone
            python3 gen_request.py nb_request 5
            python3 8.0.1-planning.py

