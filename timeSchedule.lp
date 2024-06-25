% as(D, N, T)
% operation_cost(V, V', C)
% flight time(V, V', T)
% request(N, V, V', W, T)
% time_window(T)
flight_time(V, V', T/2) :- operation_cost(V, V', T).
time_window(T) :- T = #max {T1, V, V': flight_time(V, V', T1)}.


% for each assignment, agent always start at the beginning of time step of assignment
&diff {departure(D, V, T) - 0} = T':- as(D, N, T), time_window(TW), avai(D, V, T), T' = T*TW.

% arrival time at destination when agent is available at origin of assignment
&diff {arrival(D, V', T+1) - departure(D, V, T)} = FT :- as(D, N, T), request(N, V, V', _, _), flight_time(V, V', FT), avai(D, V, T).

% arrival time at destination when agent is not available at origin of assignment
&diff {arrival(D, V'', T+2) - departure(D, V', T+1)} = FT :- as(D, N, T), request(N, V', V'', _, _), flight_time(V', V'', FT), avai(D, V, T), V!=V'.

% arrival time at origin when agent is not available at origin of assignment
&diff {arrival(D, V', T+1) - departure(D, V, T)} = FT :- as(D, N, T), request(N, V', V'', _, _), flight_time(V, V', FT), avai(D, V, T), V!=V'.

% departure time at origin when agent is not available at origin of assignment
&diff {departure(D, V', T+1) - arrival(D, V', T+1)} = 0 :- as(D, N, T), request(N, V', V'', _, _),  avai(D, V, T), V!=V'.

#show dl/2.
