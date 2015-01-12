CXXFLAGS = -g -Wall -O2
CXX = g++

clean:
	rm -rf *.o battleships

battleships:
	g++ -o battleships main.cpp main.h globals.h
