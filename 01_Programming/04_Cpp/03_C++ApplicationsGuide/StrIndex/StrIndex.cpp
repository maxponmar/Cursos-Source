#include "General.h"
#include <string.h>
#include <stdlib.h>

using namespace std;

int main() {
	system("clear");
	cout << "Press <Ctrl-C> to exit!\n\n";
	char S[101];
	unsigned i,L;
	for(;;){
		cout << "Enter string S : " << flush; cin.get(S,101);
		cout << "Your string is : " << S << "\n";
		cout << "strlen(S) = " << (L=strlen(S)) << "\n";
		cout << "Its last entry is " << *(S+L-1) << "\n";
		cout << "Enter index i : "; cin >> i;
		cout << "S[i] = " << S[i] << "\n\n"; }
		return 0;}
	
