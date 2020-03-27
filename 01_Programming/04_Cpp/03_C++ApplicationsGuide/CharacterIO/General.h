//**********************************************************************
//                                GENERAL.H
#ifndef General_H
#define General_H

//#include <conio.h>
#include <iostream>
#include <iomanip>
#include <limits>
#include <stdlib.h>
//#include <DOS.h>

//**********************************************************************
// General programming aids
#define This (*this)			// Showthand for the target of a class'
								// self-pointer.
								
#define Boolean		int			// These constitute an approximation of
								// the two valued Boolean data type.
								
#define StrEmpty(S)	(*(S)==0)	// Us string S empty?
#define EmptyStr 	""			// Empty string.
#define Blank		' '			// Blank character.								

#define UpperCase 	"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#define LowerCase 	"abcdefghijklmnopqrstuvwxyz"
#define WhiteSpace 	"\t\n\v\f\r "

void Pause(const char* Prompt = EmptyStr);	// Display a prompt, then
											// await and discard a
											// keyboard character.

#define Inspect 	Pause("\nPress any key...\n\n")

#define cinFlush cin.seekg(ios::end)	// Flush the input stream.

int Digits(int x);						// Number of characters in the 
										// shortest numeral for x
										
int Sing(double x);						// Return -1, 0, or 1
										// when x <, =, or > 0
										
//**********************************************************************										
// Maxima and minima

#undef max
#undef min
int		max(int x, int y);			// Return the larger of x,y.
int 	min(int x, int y);			// Return the smaller of x,y.
double	fmax(double x, double y);	// Return the larger of x,y.
double  fmin(double x, double y);	// Return the smaller of x,y.

//**********************************************************************
// Error reporting facilities

typedef enum ErrorType				// Error signal codes.
{ 	NoError,		BadFormat,
	IndexError,		OutOfMemory,
	DivideError } ErrorType;
	
void SetError(ErrorType E);	// Set error signal.
ErrorType GetError();		// Return error signal.
const char* ErrorName();			// Return error name, turn off error signal

// Included here are some miscellaneous features detailed in Sections
// 2.9 and 2.10.
	
	
#endif										
