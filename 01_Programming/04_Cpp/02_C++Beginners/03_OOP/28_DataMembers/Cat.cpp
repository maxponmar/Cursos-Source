/*
 * Cat.cpp
 *
 *  Created on: Mar 20, 2020
 *      Author: max
 */

#include <iostream>
#include "Cat.h"

using namespace std;

void Cat::speak() {
	if (happy) {
		cout << "Meoww" << endl;
	} else {
		cout << "Sssss!!!" << endl;
	}
}

void Cat::makeHappy() {
	happy = true;
}

void Cat::makeSad() {
	happy = false;
}

