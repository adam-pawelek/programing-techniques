%insert the specification of a new system;

comp( bicycle, all, [frame, gear, opt(acessory),opt(tyy)]).
comp( bicycle, all, [frame, gear, opt(tak),opt(ojj)]).
comp(frame, one-of, [18, 24]).
comp(gear, one-of, [small, medium, big]).
comp(acessory, more-of, [ligth, bell]).



%count the number of ”one-of” specifications;
contar_specyfic(N) :-  comp(_,one-of,L), length(L,N1), write(N1).

contar_all(N) :-  findall(T, comp(_,one-of,T),S), write(S),nl, sum_listt(S,Sum), write(Sum).

sum_listt([], 0).
sum_listt([H|T], Sum) :-
   sum_listt(T, Rest),
   length(H,N1),
   Sum is N1 + Rest.



%. list the optional components of a system knowing that they are only possible inside ”all” specifications.



list_opt(N) :- comp(_,all,L),  member(opt(W), L), find_elem(opt(W),L), fail. 




find_elem(X,[]). 
find_elem(opt(X),[opt(X)|T]) :- write(X),find_optt(X),nl,find_elem(X,T) .

%find_elem(X,[X|T]) :- write(X),find_elem(X,T) .

find_elem(X, [_|T]) :- find_elem(X,T).


find_optt(OPTT) :- comp(OPTT,_,L), write(L).


%find_elemF(NN) :- findall(T,comp(_,all,T),S), write(S).



%find_listt(T) :- findall(T, member(opt(XX), T), S), write(S).




% count the maximum number of components of the system considering that it is possible to define more than one ”all” and ”more-of” specification for a system;


contar_number_more_of(Sum) :-   findall(T, comp(_,more-of,T),Sum).


contar_number_more_of_cc(Sum) :-  contar_number_more_of(N), sum_listt(N, Sum).



contar_number_all(Sum) :- findall(T, comp(_,all,T),Sum).


contar_number_all_cc(Sum) :- contar_number_all(N), sum_listt(N, Sum).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%

contar_more_of_to_substract(Sum) :-   findall(T, comp(_,more-of,T),WW), length(WW, Sum).


%%%%%%%%%%%%%

count_result(Sum) :- contar_number_more_of_cc(N1),  contar_number_all_cc(N2), contar_more_of_to_substract(N3), Sum is N1 + N2 - N3.



%contar_number_more_of(Sum) :-  findall(T, comp(_,more-of,T),S), write(S),nl,  sum_listt(S,Sum).














