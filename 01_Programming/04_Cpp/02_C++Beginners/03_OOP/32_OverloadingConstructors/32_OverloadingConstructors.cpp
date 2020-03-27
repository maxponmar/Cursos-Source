//============================================================================
// Name        : 32_OverloadingConstructors.cpp
// Author      : Maximiliano
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
#include "Person.h"


int main() {
	Person person1;

	Person person2("Max");

	Person person3("Chios", 40);

	cout << person1.toString() << endl;
	cout << person2.toString() << endl;
	cout << person3.toString() << endl;
	return 0;
}
