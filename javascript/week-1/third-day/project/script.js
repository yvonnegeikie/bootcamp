
/*Tasks:

1:  Write a conditional statement to check a customer’s age at a bar. If the customer is under 18 log a message advising they are too young, otherwise ask what they would like to drink.*/
const yourAge = 7;
if (yourAge >= 18) {
    console.log("What do you want to drink?")
}
else {
    console.log("You are too young, get out!")
}


/*
2: Declare a variable called "Password". Write an if statement that checks how many characters are in the password, if the password has more than 8 characters log the password to the console, if the password has less than 8 characters log to the console that the password is too short.*/
const password = "11111111111";
if (password.length >= 8) {
    console.log("Winner winner chicken dinner!")
}
else {
    console.log("Make your password longer!")
}


/*3: Create a variable that stores a number. Check whether the number is divisible by 3 or 5, if so log "This number is divisible by 3 or 5" to the console. Otherwise log an alternate message to the console.*/
const a = 13;
let isDivByFive;

if (a % 5 === 0) {
    isDivByFive = true;
    console.log("isDivByFive = true")
} else {
    isDivByFive = false;
    console.log("isDivByFive = false")
}

let isDivByThree;

if (a % 3 === 0) {
    isDivByThree = true;
    console.log("isDivByThree = true")
} else {
    isDivByThree = false;
    console.log("isDivByThree = false")
}

if (isDivByFive || isDivByThree) {
    console.log("This number is divisible by 3 or 5")
}
else {
    console.log("Not divisible")
}


/*4: Create a variable that stores a number. If the number is divisible by 3, log "fizz" to the console. If the number is divisible by 5 log "buzz" to the console. If the number is divisible by both 3 and 5, log "fizz buzz" to the console. Otherwise log the number to the console.*/

const number = 30;
if (number % 3 === 0) {
    console.log("fizz")
}

if (number % 5 === 0) {
    console.log("buzz")
}

if (number % 3 === 0 && number % 5 === 0) {
    console.log(" fizz buzz")
} else { console.log(number) }

