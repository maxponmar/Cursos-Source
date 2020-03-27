//============================================================================
// Name        : 28_DataMembers.cpp
// Author      : Maximiliano
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include "Cat.h"
using namespace std;

int main() {

	Cat myCat;
	//myCat.happy = false;
	myCat.makeHappy();
	myCat.speak();

	Cat otherCat;
	otherCat.makeSad();
	otherCat.speak();
	return 0;
}
