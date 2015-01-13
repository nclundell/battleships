CXXFLAGS = -g -Wall -O2
CXX = g++

MAIN = main.cpp main.h globals.h

MATCH = runners/match.cpp runners/match.h globals.h

PLACER = runners/placer.cpp runners/placer.h globals.h

clean:
	rm -rf *.o battleships bin/*
	ls --group-directories-first --color=auto -F



#Make Main ONLY
match: ${MATCH}
	g++ -o bin/match ${MATCH}
	ls --group-directories-first --color=auto -F

#Make Placer ONLY
placer: ${PLACER}
	g++ -o bin/placer ${PLACER}
	ls --group-directories-first --color=auto -F

#Make Main ONLY
main: ${MAIN}
	g++ -o battleships ${MAIN}
	ls --group-directories-first --color=auto -F

#Make All Binaries
battleships:
	g++ -o bin/match ${MATCH}
	g++ -o bin/placer ${PLACER}
	g++ -o battleships ${MAIN}
	ls --group-directories-first --color=auto -F
