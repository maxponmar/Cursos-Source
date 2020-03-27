#include <iostream>
using namespace std;

void manipulate(double* value){
    cout << "2. Value of double in manipulate: " << value << endl;
    *value = 10.0;
    cout << "3. Value of double in manipulate: " << value << endl;
}

int main() {
    
    int nValue = 8;
    
    int* pnValue = &nValue;

    cout << "nValue : " << nValue << endl;
    cout << "Pointer to nValue : " << pnValue << endl;
    cout << "nValue via pointer : " << *pnValue << endl;
    
    cout << "=======================" << endl;
    double dValue = 123.4;
    cout << "1. dValue : " << dValue << endl;
    manipulate(&dValue);
    cout << "4. dValue : " << dValue << endl;



    return 0;
}
