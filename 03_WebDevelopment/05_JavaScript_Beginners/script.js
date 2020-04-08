// DOM - Document Object Model

let x = document.getElementById('para');

x.innerText = "Changing text from javascript using id";

console.log(x);

x = document.getElementsByTagName("p");
console.log(x);
console.log(x[1]);

x = document.getElementsByClassName("grp");
console.log(x);

x = document.querySelectorAll("p.grp");
console.log(x);

// changing css
x = document.getElementById("para");
x.style.color = "brown";

// events
function btn1Click(){
    alert("Tanks for clicking!");
    x = document.getElementById("para");
    x.style.color = "black";
}
let btn2 = document.getElementById("btn2");
btn2.addEventListener("click", btn1Click);

let mouseTest = document.getElementById("mousetest");
mouseTest.addEventListener("mousedown", downEvent);
mouseTest.addEventListener("mouseup", upEvent);
mouseTest.addEventListener("mousemove", moveEvent);


 function downEvent(){
     mouseTest.style.backgroundColor = "red";
 }
 function upEvent(){
    mouseTest.style.backgroundColor = "white";
 }
 function moveEvent(){
    mouseTest.style.backgroundColor = "green";

 }

