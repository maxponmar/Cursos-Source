/*
 * Cat.cpp
 *
 *  Created on: Mar 20, 2020
 *      Author: max
 */

#include <iostream>
#include "Cat.h"

using namespace std;

Cat::Cat(){
	happy = true;
	cout << "Cat created" << endl;
}

Cat::~Cat(){
	cout << "Cat destroyed" << endl;
}

void Cat::speak() {
	if (happy) {
		cout << "Meoww" << endl;
	} else {
		cout << "Sssss!!!" << endl;
	}
}


