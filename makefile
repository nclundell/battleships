CXXFLAGS = -g -Wall -O2
CXX = g++

MAIN = main.cpp main.h globals.h

CHECKPLACER = runners/checkPlacer.cpp runners/checkPlacer.h globals.h

BATTLESHIPS = ${MAIN} ${CHECKPLACER}

clean:
	rm -rf *.o battleships main checkPlacer
	ls --group-directories-first --color=auto -F

#Make Main ONLY
main: ${MAIN}
	g++ -o main ${MAIN}
	ls --group-directories-first --color=auto -F

#Make checkPlacer Runner ONLY
checkPlacer: ${CHECKPLACER}
	g++ -o checkPlacer ${CHECKPLACER}
	ls --group-directories-first --color=auto -F

#Make Full Binary
battleships: ${BATTLESHIPS}
	g++ -o battleships ${BATTLESHIPS}
	ls --group-directories-first --color=auto -F
