console.log("Hello world");
document.write("Hello");

// Outputs - DOM (Document Object Model)
// Alert statements
//alert('Statement');

// Use strict - ES5 specification 2009 - latest modifications, modern javascript
// classes & modules - stric mode automaticly activated
'use strict';

//========================================
// Variables, data types, type conversions
//========================================

let variableName;
variableName = "Maximiliano"; // <- string

// var - before ES6 (2015)
// it has function scope and not block scope like let
var variable1 = 10;
variabl2 = 20;  // <- bad practice
let isBoolean = true;


//======================
// Constants
//======================
const PI = 3.14159; // Capitalize constants y common practice
// pi = 4; <- error

//======================
// Javascript is Dynamic
//======================
let varName = "Name";
varName = 3123;
varName = false;
// infinity, NaN <- not a number
let a = 1/0;
console.log(a);
a = "string"/1;
console.log(a);

a = "orange"
console.log(`This is an ${a}`);
let bool = 1<2;
console.log(bool);

//======================
// Arrays and objects
//======================
let array = [1,2,3,"Hello", false, 3.14159];
console.log(array[3]);
let obj = {name:"Maximiliano", age:21, hair:"black"}
console.log(obj.name)

//======================
// Typeof operator
//======================
console.log("=================");
console.log(typeof(obj));
console.log(typeof(array));
console.log(typeof(bool));
console.log(typeof(a));
console.log(typeof(PI));

//======================
// Undefined and Null
//======================
console.log("=================");
let z;
console.log(typeof z);
z = undefined;
console.log(typeof z);
z = null;
console.log(typeof z);
// Null & Undefined are equals in value but different in type
console.log(typeof undefined);
console.log(typeof null);
console.log(null == undefined);

//======================
// Type conversions
//======================
console.log("=================");

let m = 1;
console.log(typeof m);
let mString = String(m);
console.log(typeof mString)

let mystring = "32";
console.log(mystring);
let mynumber = Number(mystring);
console.log(mynumber);
mystring = " 3 2  ";
console.log(mystring);
mynumber = Number(mystring);
console.log(mynumber);

//======================
// Outputs
//======================
a = "Hello there!"
alert(a + " " + "Have a nice day!, 1+2=" + (1+2) );
let age = prompt("What is your age");
alert(`You are ${age} years old`);
let agebool = confirm("Are you less than 18 years old?");
alert(agebool);

a = 1 + "Hello" + 2;
console.log(a);
// Ternary operator
// if (1<2) is true, then variable=10 else variable="no"
let variable = (1<2) ? 10 : "no";

// Creating strings and objects
a = new String("Hello");    // <- Object
b = "Hello"                 // <- string
console.log(typeof a);
console.log(typeof b);
a = new Number(5);
b = 4;
console.log(typeof a);
console.log(typeof b);

// Conditional statements and loops
if (a>3){
    //code
} else {
    // code
}

if (a>3){
    //code
} else if(a>4){
    // code
}

switch (b){
    case 1: //code
            //break;
    case 2: // code
            //break;
    default: // code
}

for(let i=1;i<=5;i++){
    console.log(i);
}

while(a==1){
    // code
}

do{
    // code
}while(a==4);

// Arrays
let myArray = []; // empty array
myArray = new Array("orange",1,2,false,3.25,-3);
// they have push, pop

// Date object
let d = new Date();
console.log(d);

// random
console.log(Math.random());


// Functions
function funName(){
    alert("Hello from funName");
}
function sum(n1, n2){
    let s = n1 + n2;
    return s;
}
funName();
let result = sum(10,20);
console.log(result);

// Anonymous functions
let varName = function(par1, par2){
    return par1*par2;
}
varName();

// self-invoking function
(function functionName(){
    alert("self-invoking function");
})();

let helloWorld = () => alert("Hello world");


// Objects
let person1 = {
    name:"Max",
    age:50,
    height=170,
    wave: function() {alert(`Hi im ${this.name}`)}
};

person1.wave();