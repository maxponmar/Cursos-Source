//============================================================================
// Name        : 06_IntegerTypes.cpp
// Author      : Maximiliano
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <climits>

using namespace std;

int main() {

	int value = 777;
	cout << value << endl;

	cout << "Max int value: " << INT_MAX << endl;
	cout << "Min int value: " << INT_MIN << endl;


	//long lValue2 = 2345323531354; also works
	long int lValue = 2345323531354;
	cout << lValue << endl;

	short sValue = 23432;
	cout << sValue << endl;

	cout << "Size of int: " << sizeof(int) << endl;
	cout << "Size of long int: " << sizeof(long int) << " bytes" << endl;
	cout << "Size of short int: " << sizeof(short int) << " bytes" << endl;

	// Positive numbers only
	unsigned int uValue = 321324;
	cout << uValue << endl;

	return 0;
}
