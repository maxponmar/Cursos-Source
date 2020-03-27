/*
 * Person.h
 *
 *  Created on: Mar 20, 2020
 *      Author: max
 */

#ifndef PERSON_H_
#define PERSON_H_

#include <iostream>
using namespace std;

class Person {
private:
	string name;
	int age;
public:
	Person(): name("unnamed"), age(0) {};
	Person(string name, int age): name(name), age(age) {};
	string toString();
};
#endif /* PERSON_H_ */
