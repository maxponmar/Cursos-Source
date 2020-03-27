//============================================================================
// Name        : 05_UserInput.cpp
// Author      : Maximiliano
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {

	cout << "Enter your name: " << flush;
	string input;
	cin >> input;
	cout << "Hello " << input << ", How are you doing?" << endl;


	cout << "Enter a number: " << flush;
	int value;
	cin >> value;
	cout << "You entered: " << value << endl;


	return 0;
}
