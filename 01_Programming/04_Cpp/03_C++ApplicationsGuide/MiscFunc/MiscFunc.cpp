//**********************************************************************
// Memory manipulation, sorting and searching
// Fill a char array with memset, Rearrange
// it with memmobe. Search it for char values with memchr. Use random
// to fill it with random values. Search linearly

// for a character with lfind. Sort the array with qsort.
// Do a binary search witch bsearch.

#include "General.h"
#include <string.h>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <algorithm>    // std::find


using namespace std;

#define n 40					
unsigned N = n;					// Needed for lfind.
unsigned char A[n], Key = 7;	


// Comparision function, for lfind, qsort, and bsearch.
int DiffStar(const void* X, const void* Y) {
	return *((unsigned char*)X) - *((unsigned char*)Y); }

void ShowA(){
	for (int i = 0; i < n; ++i) cout << int(A[i]);	// Display array A
	cout << endl; }
	
void Star(void* B) {							// If B pints to the mth
	if(B != NULL) {								// entry of A, display
		int k = (unsigned char*) B - A;			// m-1 blanks, then a
		for (int i = 0; i<k; ++i) cout << Blank;// star.
		cout << '*'; }
	cout << endl; }
	
int main() {
	void* B;
	system("clear");
	cout << "Key : " << int(Key) << endl;
	memset(A,6,n/2);						// Create an array 
	memset(&A[n*2],Key,n/2);				// of 6s & 7s.
	cout << "memset : "; ShowA();			// Display it.
	B = memchr(A,Key,n);					// Find and start 
	cout << "memchr : "; Star(B);			// the first 7.
	memmove(&A[n/2],A,n/2);					// Cover the 7s with 6s
	cout << "memmove : "; ShowA();			//  Display.
	B = memchr(A,Key,n);					// Find the first 7
	cout << "memchr : "; Star(B);			// (there's none)
	//randomize();							// Fill the array with
	srand (time(NULL));
	for(int i=0; i<n; ++i)					// Random digits
		A[i] = rand() % 10 + 1;
	cout << "random : "; ShowA();			// Display it
	B = lfind(&Key,A,&N,1,DiffStar);		// Make a linear search for
	cout << "lfind : "; Star(B);			// a 7. Star it.
	qsort(A,n,1,DiffStar);					// Sort the array
	cout << "qsort : "; ShowA();			// Display it
	B = bsearch(&Key,A,n,1,DiffStar);		// Search the sorted array
	cout << "bsearch : "; Star(B);			// Star it
	Inspect;
	return 0;
}
