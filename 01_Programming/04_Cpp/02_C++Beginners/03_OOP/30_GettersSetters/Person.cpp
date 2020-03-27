/*
 * Person.cpp
 *
 *  Created on: Mar 20, 2020
 *      Author: max
 */

#include "Person.h"

Person::Person() {
	name = "Maximiliano";

}

string Person::toString() {
	return name;
}

void Person::setName(string newName){
	name = newName;
}

string Person::getName(){
	return name;
}
