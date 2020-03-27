#include <iostream> 
#include <stdlib.h>
#include "General.h"

using namespace std;

int main()
{
	system("clear");
	
	cout << "Press <Ctrl-C> to exit!\n\n" << endl; // <Ctrl-C> 
												   // is ASCII 3
    char Ch;
    do {
		cout << "Enter a character: " << flush; cin >> Ch;
		cout << "It's ASCII " << unsigned(Ch) % 256 << ".\n\n"; 
	} while (Ch != 3 && !cin.eof());						
	
	return 0;
}
