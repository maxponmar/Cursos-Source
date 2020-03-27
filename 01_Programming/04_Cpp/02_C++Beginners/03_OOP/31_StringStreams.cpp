//============================================================================
// Name        : 31_StringStreams.cpp
// Author      : Maximiliano
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <sstream>

using namespace std;

int main() {

	string name = "Max";

	int age = 32;

	//string info = "Name: " + name + "; age: " + age;
	//cout << info << endl;

	stringstream ss;

	ss << "Name: ";
	ss << name;
	ss << "; Age: ";
	ss << age;

	cout << ss.str() << endl;

	return 0;
}
