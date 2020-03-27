//============================================================================
// Name        : 04_Strings.cpp
// Author      : Maximiliano
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {

	// int is a primitive type, string is a class, so text1 is an object of string class

	string text1 = "Hello ";
	string text2 = "Max";

	string text3 = text1 + text2;

	cout << text1 << text2 << endl;

	cout << text3 << endl;



	return 0;
}
