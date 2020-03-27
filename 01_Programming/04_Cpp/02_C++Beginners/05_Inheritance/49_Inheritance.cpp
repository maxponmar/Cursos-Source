#include <iostream>
using namespace std;

class Animal{
public:
    void speak(){cout << "Grrr" << endl;}	
};

class Cat: public Animal{
public:
    void jump(){cout << "Cat jumping." << endl;}
};

int main(){
    Animal a;
    a.speak();
    
    Cat c;
    c.speak();
    c.jump();


    return 0;
}

