#include <iostream>
using namespace std;

int main(){
    
    const int NSTRINGS = 5;

    string texts[NSTRINGS] = {"one","two","three","four","five"};

    string *pTexts = texts;
    
    pTexts+=3;
    cout << *pTexts << endl;
   
    pTexts-=2;
    cout << *pTexts << endl;

    string *pEnd = &texts[NSTRINGS-1];
    pTexts = &texts[0];

    while(pTexts != pEnd){
        cout << *pTexts << endl;
        pTexts++;
    }
    cout << *pTexts << endl;
    
    // Set pTExts back to start
    pTexts = &texts[0];
    
    long elements = (long)(pEnd - pTexts)+1;
    cout << elements << endl;
    
    pTexts += NSTRINGS/2;

    cout << *pTexts << endl;

    return 0;
}

