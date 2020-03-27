#include <iostream>

// This code is written without using namespace std before
//int main() {
//	std::cout << "Outputting text program" << std::endl;
//	return 0;
//}

using namespace std;

int main() {
	// Flush doesn't create a new line
	cout << "Starting program..." << flush;

	cout << "This is some text" << endl;

	cout << "Banana. " << "Apple. " << "Orange." << endl;

	cout << "This is some more text" << endl;

	return 0;
}
