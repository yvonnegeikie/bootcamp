let subject = "JavaScript"; //global scope 

//Declaring or defiling a fuction 
function greeting() {
    console.log("Hello World!");
}

//Call or Invoke the function - shows in console 
greeting();

//Uder login // Log out function 
let userOnline = true;
function userStatus() {
    if (userOnline == true) {
        console.log("User is online")
        console.log(userOnline);
    }
    else {
        console.log("User is Not online")
        console.log(userOnline);

    }
}
userStatus();

//Functin with parameter // Argument 


//Parameter are defined when we declare the function. Data is that is expected.

//Auguments are the data we pass to the function when wew call it 

function atm(accountNumber, amount) {
    console.log(`Account Number: ${accountNumber}. Amount: ${amount}`);
}
atm(345463, 300);
atm(123, 23)
function sum(num1, num2) {
    return num1 + num2;
}
console.log(sum(20, 10)); //30
console.log(sum(50, 50)); //100

//Creat a function which will say Hello 'PersonName', How are you, that you pass as argument. 

function greeting(PersonName) {
    console.log(`Hello ${PersonName}, how are you?`);
}
greeting(`Yvonne`);


console.clear();
//!Scope in JavaScrip
//block scope
//let, const 
//local scope
// var, let, const 
//global scope 
//if you declare a variable outside a function, it has global scope. Can be declared anywhere in the doc, not just the top

let name = "Matt";
{
    const name = "John";
    //block scopeonly available inside the block 
    //Var does NOT have block scope so it would work 

}
console.log(`Hello ${name}`); //Matt 
function scope() {
    var firstName = "Yvonne";
    console.log(subject)
}
scope();
//Funcions that call other functions 
function double(num1) {
    return num1 * 2;
}
function quadruple(num2) {
    return double(num2) * 2;
}
console.log(quadruple(20)); //80

//Function can be hoisted - Called before they are declared 
//Arorun function
//omit the return statement //exlpicit return 
//omit the function keyword
//when there is only 1 parementer, brackets is optional
let add2 = (num) => num * 2;
console.log(add2(10)); //20

let multiply = (x, y) => x * y; //omit hte return keyword 
console.log(multiply(5, 7)); //35

function multiplication(number) {
    for (let i = 1; i <= 10; i++) {
        console.log(`${i} * ${number} = ${i * number}`);
    }
}
multiplication(5);

