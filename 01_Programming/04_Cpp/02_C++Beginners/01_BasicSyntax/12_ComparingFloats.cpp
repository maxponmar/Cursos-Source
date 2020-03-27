//============================================================================
// Name        : 12_ComparingFloats.cpp
// Author      : Maximiliano
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <iomanip>

using namespace std;

int main() {

	float value1 = 1.1;

	if (value1 == 1.1) {
		cout << "equals" << endl;
	} else {
		cout << "not equal" << endl;
	}

	cout << setprecision(10) << value1 << endl;

	// When comparing float number is better to compare them choosing an epsilon (small value)
	// and check if 2 numbers are separated by that value or less
	if (value1 < 1.1+0.001) {
		cout << "equals" << endl;
	} else {
		cout << "not equal" << endl;
	}

	return 0;
}
