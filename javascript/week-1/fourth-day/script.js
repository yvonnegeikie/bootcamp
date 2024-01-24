//Array & Loop

// a single variable which hold more than one value
let numbers = [2, 4, 6, 7, 10, 11];
// each value has a number associated to it called - index number
// index number start from zero
let employees = [
    "Zak Pardis",
    "Mark",
    "Christian",
    "Timothy",
    "Abdul"
]
// first item =0
//last value =
console.log(employees[0]);
console.log(employees)
console.log(employees.length)
employees[2] = "Ender";
console.log(employees);

//add item
employees.push("Christain");
console.log(employees);
//remove last item
employees.pop();
console.log(employees);

let fruit = [
    "Banana",
    "Apple",
    "Kewi"
]
fruit.splice(1, 0, "Orange");
console.log(fruit)

//Search about loop in JS.
//10
//increment => ++
//decrement => --
//For loop

// use the for loop when the number of iteration is certain.
for (let i = 0; i < 6; i++) {
    console.log("Welcome to JavaScript");
}
let colours = [
    "Blue",
    "Green",
    "Red",
    "Yellow",
    "Orange",
    "Black",
    "Purple",
    "Pink",
    "Black",
    "Brown"
]
for (let i = 0; i < colours.length; i++) {
    if (colours[i] == "Black") {
        continue;
    }
    else {
        console.log(colours[i])
    }
}

//Display numbers starting from 0 till 20
for (let i = 0; i <= 20; i++) {
    console.log(i);
}

let upscaling = [
    `0`,
    `1`,
    `2`,
    `3`,
    `4`,
    `5`,
    `6`,
    `7`,
    `8`,
    `9`,
    `10`,
    `11`,
    `12`,
    `13`,
    `14`,
    `15`,
    `16`,
    `17`,
    `18`,
    `19`,
    `20`
]
for (let i = 0; i <= 20; i++) {
    console.log(i);
}

console.clear();
//While loop
//used when the number of iteration is uncertain
let number = 0;
while (number < 20) {
    console.log(number);
    number++;
}
//do While Loop
//It wil run the loop once even if th econdition is false as it will check the condition after 
let num = 1;
do {
    console.log(num)
    num++;
}
while (num < 5)

//Math

//Math.floor rounds down to nearest whole number 
console.log(Math.floor(20.9)); //20

//Math.ceil rounds up to nearest whole number 
console.log(Math.ceil(20.9)); //21

//Math.round rounds to nearest whole number 
console.log(Math.round(20.5)); //21

//Math.random will generate random number between 0-1
console.log(Math.random());//0.24922634731710036

//Generate a random number between 1 and 5 
console.log(Math.ceil(Math.random() * 6));
console.log(Math.floor(Math.random() * 5) + 1);