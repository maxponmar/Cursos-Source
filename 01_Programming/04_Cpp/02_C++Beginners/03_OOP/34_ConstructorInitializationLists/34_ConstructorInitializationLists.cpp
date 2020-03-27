//============================================================================
// Name        : 34_ConstructorInitializationLists.cpp
// Author      : Maximiliano
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
#include "Person.h"

int main() {
	Person person1("Max", 21);
	Person person2("Chios", 22);
	Person person3;

	cout << person1.toString() << endl;
	cout << person2.toString() << endl;
	cout << person3.toString() << endl;
	return 0;
}
