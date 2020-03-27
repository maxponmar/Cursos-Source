//============================================================================
// Name        : 07_FloatingPointTypes.cpp
// Author      : Maximiliano
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <iomanip>

using namespace std;

int main() {

	float fValue = 76.4;

	cout << sizeof(float) << endl;
	cout << fixed << fValue << endl;
	cout << scientific << fValue << endl;
	cout << setprecision(20) << fixed << fValue << endl;

	double dValue = 123.456789;
	cout << sizeof(double) << endl;
	cout << fixed << dValue << endl;
	cout << scientific << dValue << endl;
	cout << setprecision(20) << fixed << dValue << endl;

	long double ldValue = 123.4563214354789;
	cout << sizeof(long double) << endl;
	cout << fixed << ldValue << endl;
	cout << scientific << ldValue << endl;
	cout << setprecision(20) << fixed << ldValue << endl;

	return 0;
}
