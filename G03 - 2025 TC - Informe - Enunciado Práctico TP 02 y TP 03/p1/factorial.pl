factorial(0, 1).
factorial(N, F) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, F1),
    F is N * F1.

:- initialization(main).

main :- 
    factorial(5, F),
    write('El factorial de 5 es: '), write(F), nl.