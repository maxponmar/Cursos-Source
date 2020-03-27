//============================================================================
// Name        : 33_This.cpp
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
	Person person2("Max", 21);
	Person person3("Chios", 22);

	cout << person1.toString() << "; memory location: " << &person1 << endl;
	cout << person2.toString() << "; memory location: " << &person2 << endl;

	return 0;
}
