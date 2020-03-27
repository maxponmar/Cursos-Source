/*
 * Person.cpp
 *
 *  Created on: Mar 20, 2020
 *      Author: max
 */

#include <sstream>
#include "Person.h"

string Person::toString(){
	stringstream ss;
	ss << "Name: ";
	ss << name;
	ss << "; Age: ";
	ss << age;

	return ss.str();
}

