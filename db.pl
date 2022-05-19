%Adam Pawelek - Third practical work (Prolog) Programming Technologies

:- dynamic(comp/3).

%comp( bicycle, all, [frame, gear, opt(acessory,test)]).
comp( bicycle, all, [frame, gear, opt(acessory)]).
comp(frame, one-of, [18, 24]).
comp(gear, one-of, [small, medium, big]).
comp(acessory, more-of, [ligth, bell]).




% Exercise. 01 - . insert the specification of a new system;
% predicate - insert_the_specification

insert_the_specification:- 
	write('Name: '), read(Name),
	write('all or more-of or one-of: '), read(Type),
	write('Elements in list[]: '), read(Elements),
	assertz(comp(Name,Type, Elements)).


% Exercise 02. - count the number of ”one-of” specifications;
% Working example len([small, medium, big]) + len( [18, 24]) = 3 + 2 = 5
% predicate - count_all_one_of



count_all_one_of :-  
	findall(T, comp(_,one-of,T),S), 
	%write(S),
	sum_length_of_lists(S,Sum), 
	write(Sum).

sum_length_of_lists([], 0).
sum_length_of_lists([H|T], Sum) :-
   sum_length_of_lists(T, Rest),
   length(H,N1),
   Sum is N1 + Rest.



%. Exercise 03. - list the optional components of a system knowing that they are only possible inside ”all” specifications.
% predicate - list_opt

list_opt :- 
	comp(_,all,L),  
	member(opt(W), L), 
	find_elem(opt(W),L), 
	fail. 


find_elem(X,[]). 
find_elem(opt(X),[opt(X)|T]) :- 
	write(X),write(' '),
	find_optt(X),
	nl,
	find_elem(X,T) .


find_elem(X, [_|T]) :- find_elem(X,T).

find_optt(OPTT) :- comp(OPTT,_,L), write(L).






% Exercise 04. - count the maximum number of components of the system considering that it is possible to define more than one ”all” and ”more-of” specification for a system;
%predicate - count_result(Sum)

find_more_of_lists(Sum) :-   findall(T, comp(_,more-of,T),Sum).


count_length_of_more_of_lists(Sum) :-  
	find_more_of_lists(N), 
	sum_length_of_lists(N, Sum).



find_all_lists(Sum) :- findall(T, comp(_,all,T),Sum).


count_length_of_all_lists(Sum) :- 
	find_all_lists(N), 
	sum_length_of_lists(N, Sum).




number_of_more_of_specyfication(Sum) :-   
	findall(T, comp(_,more-of,T),WW), 
	length(WW, Sum).



count_result(Sum) :- 
	count_length_of_more_of_lists(N1),  
	count_length_of_all_lists(N2), 
	number_of_more_of_specyfication(N3), 
	Sum is N1 + N2 - N3.



%find_more_of_lists(Sum) :-  findall(T, comp(_,more-of,T),S), write(S),nl,  sum_length_of_lists(S,Sum).



%Exercise 05. - generate dot code in order to visualize the graph representing thesystem
%predicate save_file


write_all:- 
	findall(X, comp(X,all,_), S),
	write_all_shape_box(S), fail.
	

write_one_of:- 
	findall(X, comp(X,one-of,_), S),
	write_one_of_shape_box_style_diagonals(S), fail.


write_more_of:- 
	findall(X, comp(X,more-of,_), S),
	write_more_of_shape_septagon(S), fail.


write_all_shape_box([]).
write_all_shape_box([X|Y]):- 
	write('\t'),
	write(X), 
	write(' ') ,
	write('[shape=Mdiamond]'),
	nl, 
	write_all_shape_box(Y).


write_one_of_shape_box_style_diagonals([]).
write_one_of_shape_box_style_diagonals([X|Y]) :-
	write('\t'),
	write(X), 
	write(' '),
	write([shape = box, style = diagonals]), 
	nl, 
	write_one_of_shape_box_style_diagonals(Y).


write_more_of_shape_septagon([]).
write_more_of_shape_septagon([X|Y]) :-
	write('\t'),
	write(' '),
	write(X), 
	write([shape = septagon]), 
	nl, 
	write_one_of_shape_box_style_diagonals(Y).
	
	
write_elem_all_info :-
	comp(N,all,S),
	write_elem_arrow_dot(N,S), fail. 
	

write_elem_one_of_info :-
	comp(N,one-of,S),
	write_elem_arrow_dot(N,S), fail. 
	
	
write_elem_more_of_info :-
	comp(N,more-of,S),
	write_elem_arrow_dot(N,S), fail. 






% get (X) from opt(X)
write_optional(opt(X)):-
	write(X).
		

write_elem_arrow_dot(_,[]). 	

write_elem_arrow_dot(N,[X|Y]) :-
	( X \= opt(_) -> 
		write('\t'),
		write(N),
		write(' -> '), 
		write(X), 
		write(' '), 
		write([arrowhead = box]), 
		nl, 
		write_elem_arrow_dot(N,Y)


	;	write('\t'),
		write(N),write(' -> '), 
		write_optional(X),
		write(' ') , 
		write([arrowhead = diamond, color = red]), 
		nl,
		write_elem_arrow_dot(N,Y)
	).





	
write_graph:- 
	write('digraph G {'),
	not(write_elem_all_info),
	not(write_elem_one_of_info),
	not(write_elem_more_of_info),
	not(write_all),
	not(write_one_of),
	not(write_more_of),
	write('}').


save_file :-
	tell('fil.txt'),
	write_graph,
	told.
	
	













