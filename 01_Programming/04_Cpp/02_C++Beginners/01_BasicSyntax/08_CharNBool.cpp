//============================================================================
// Name        : 08_CharNBool.cpp
// Author      : Maximiliano
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {

	bool bValue = true;
	cout << bValue << endl;

	char cValue = 'l';
	cout << (int)cValue << endl;

	cout << sizeof(char) << endl;


	wchar_t wValue = 'i';
	cout << wValue << endl;
	cout << sizeof(wchar_t) << endl;

	return 0;
}
