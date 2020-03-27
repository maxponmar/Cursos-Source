//============================================================================
// Name        : 30_GettersSetters.cpp
// Author      : Maximiliano
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include "Person.h"
#include <iostream>
using namespace std;


int main() {

	Person max;

	max.setName("Ponce");

	cout << max.toString() << endl;
	cout << "Name with get method : " << max.getName() << endl;
	return 0;
}
