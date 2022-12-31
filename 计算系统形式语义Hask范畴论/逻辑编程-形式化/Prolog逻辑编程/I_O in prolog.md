# I_O in prolog


https://stackoverflow.com/questions/29537207/convert-same-function-concept-of-c-to-prolog 有写：





```prolog
main :-
    write('Please enter an integer value: '),
    read(N),
    integer(N),
    N > 0,
    length(L, N),
    maplist(read_n, L),
    write_list(L).

read_n(N) :-
    write('Enter id: '),
    read(N),
    integer(N).

write_list(L) :-
    write_list(L, 1).
write_list([], _) :- nl.
write_list([H|T], N) :-
    format('~nYou have entered id ~w: ~w', [N, H]),
    N1 is N + 1,
    write_list(T, N1).
```

test run

```prolog
| ?- main.
Please enter an integer value: 4.
Enter id: 5.
Enter id: 6.
Enter id: 3.
Enter id: 6.

You have entered id 1: 5
You have entered id 2: 6
You have entered id 3: 3
You have entered id 4: 6

yes
| ?-
```
















