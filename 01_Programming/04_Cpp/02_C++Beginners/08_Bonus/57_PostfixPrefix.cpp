#include <iostream>
using namespace std;

int main() {

	int value = 8;

	cout << value++ << endl;
	cout << value << endl;

	int number = ++value;

	cout << "Number is: " << number << endl;
	cout << "Value is now: " << value << endl;

	return 0;
}

