#include "General.h"

using namespace std;

int main() {
	return 0;
}

void Pause(char* Prompt) {		// Display a prompt, then await and
	cout << Prompt << flush;	// discard a character from the
	getchar(); }				// keyboard.


int Digits(int x) {				// Return the number of characters
	int p = 1; long n = 10;		// 0,..,9 in the shortest numeral for x.
	while (abs(x) >= n) {
		++p; n*= 10; }
	if (x < 0) ++p;
	return p; }

int Sign(double x) {			// Return -1, 0, or -1 when
	if (x < 0) return -1;		// x <, =, or > 0.
	if (x == 0) return 0;
	else return 1; }

int max(int x, int y) {			// Return the larger of x and y
	return (x < y ? y : x); }

int min(int x, int y) {			// Return the smaller of x and y
	return (x < y ? x : y); }
	
double fmax(double x, double y) {	// Return the larger of x and y
	return (x < y ? y : x); }

double fmin(double x, double y) {	// Return the smaller of x and y
	return (x < y ? x : y); }
	
ErrorType ErrorSignal = NoError;	// Initial value.
const char* ErrorString[] =				// Error signal output names
{	"No Error",		"Bad Format",	
	"Index Error",	"Out of Memory",
	"Divide Error"	};
	
void SetError(ErrorType E) {		// Set errir signal
	ErrorSignal = E; }
	
ErrorType GetError() {				// Return error signal
	return ErrorSignal; }			
	
const char* ErrorName() {
	ErrorType E = ErrorSignal;		// Return error name and turn of
	ErrorSignal = NoError;			// error signal.
	return ErrorString[E]; }		

// Included here are some miscellaneous features detailed in Sections
// 2.9 and 2.10.














