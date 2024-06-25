#!/bin/bash
# fixed 40 request, increase agent 10 -> 60
# echo "fixed 40 request, increase agent" >> log.txt
# python gen_rq.py 60 5
# for nb_drone in 10 20 30 40 50 60 100 200
# do 
#     echo "nb_drone $nb_drone" >> log.txt
#     for run in {1..5}
#     do
#         echo "Run $run :" >> log.txt
#         python3 gen_init.py $nb_drone
#         python3 8.0.1-planning.py
#     done
# done


for nb_request in 15 40 60 100 160
do
    for run_rq in {1..5}
    do
        python gen_rq.py $nb_request 5
        for nb_drone in 10 20 40 80 120 160 
        do
            
            for run_drone in {1..5}
            do
            
                python gen_init.py $nb_drone
                
                python 8.0.1-planning.py nb_drone=$nb_drone nb_request=$nb_request run_for_request=$run_rq run_for_drone=$run_drone
            done
        done
    done
done
sudo shutdown -h now




