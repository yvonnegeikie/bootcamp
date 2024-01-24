let num1 = 100; //number value 
let firstName = "Yvonne"; //string value 
console.log(typeof num1);
console.log(typeof firstName);
console.log(typeof 50);

let education = true;
console.log(typeof education);
let a = 10;
console.log(a == 10);

let b;
console.log(typeof b);
let c = null;
console.log(typeof c);
let bigInt = 9846534;
console.log(typeof bigInt);
let bigInt2 = 9846534n;
console.log(typeof bigInt2);

//Data type changes 
//Syntax = string value (ValueToConvert)

let f = 3;
console.log(typeof String(f));
let g = String(100);
console.log(typeof g);
let h = String(true);
console.log(typeof h);
console.log(h);

console.log(10 + "10");
//Need to convert datatype to number equal 20!
let i = "20";
console.log(Number(i));
let myName = 'Yvonne';
console.log(Number(myName));
//NaN = not a number 
//true=1, false=0;
console.log(Number(false));
console.log(Number(true));

console.log(Number("1"));


//!Convert number to Boolean 
console.log(Boolean(0)); //false
console.log(Boolean(1)); //true
console.log(Boolean("Javascript")); //true
console.log(Boolean("")); //false
console.log(Boolean(" ")); //space is a character = true

console.log(Number(Boolean(String(true)))); //console.log(Number(1);




//!TRY THESE IN YOUR JS FILE:
console.log('1' + 2); //12
console.log('1' + 2 + true); //12true
console.log('12' + undefined); //12undefined
console.log('12' + null); //12null
console.log(2 + '1'); //21
console.log(2 + true); //3

//!String in JavaScript
let firstMessage = "Welcome to JavaScript";
console.log(firstMessage);
let secondMessage = 'Welcome to JavaScript';
console.log(secondMessage);
let thirdMessage = `Welcome to JavaScript`;
console.log(thirdMessage);
let christianName = 'Yvonne';
let sureName = "Geikie";
console.log(`Hello ${christianName} ${sureName} you are a legend`)

console.log("5" + 3 + 3);
console.log("10" === 10);
console.log(String(Boolean(String(4 / false))));
console.log(Number(Boolean("5")));
console.log(Number(Boolean(null)));

let value = Number(false);
console.log(value);

let valuee = Boolean("0");
console.log(valuee);

console.log(Number(Boolean(null)));