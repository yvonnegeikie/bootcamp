/*
Syntax:

if(condition){task to do}
else if(condition){task to do}
else if(condition){task to do}
else if(condition){task to do}
else{task to do}
*/
/*
let weather = "Sunny";
if (weather == "Raining") {
    console.log("Take unmerella, if it's raining!")
}
else if (weather == "Sunny") {
    console.log("It's sunny, take your sunglasses!")
}
else {
    console.log("The weather would be foggy, wear jacket!")
}
*/


/* //!OPERATOR
+   addition
-   subtraction
/   devision
*   multiply
%   moduler
++  increment
--  decrement
=       assignment
==      equal too -> comparison
===     ->equal value and equal data type.
! in === both the data type and value should be equal
! in == only the value should be equal
> greater
< less than
>= greater or equal
<= less than equal
*/

let age = "Too young";
if (age == "Old enough") {
    console.log("You can vote!")
}

else if (age == "Too young") {
    console.log("Come back in the future!")
}

else if (age == "Not registered") {
    console.log("Go register!")
}

else { ("Suck!") }


//Switch statements 
let day = "Sunday"
switch (day) {
    case "Monday":
        console.log("Happy Monday!");
        break;
    case "Tuesday":
        console.log("Suicide Tuesday!");
        break;
    case "Wednesday":
        console.log("Hump day!");
        break;
    case "Thursday":
        console.log("Thirsty Thursday!");
        break;
    case "Friday":
        console.log("TGI!");
        break;
    case "Saturday":
        console.log("Weekend!");
        break;
    case "Sunday":
        console.log("Rest!");
        break;

}


//Switch Statement 2 - Grading example 
let testScore = 65;
switch (true) {
    case testScore >= 75:
        console.log(`Disctinction`);
        break;
    case testScore >= 60:
        console.log(`Merit`);
        break;
    case testScore >= 50:
        console.log(`Pass`);
        break;
    default:
        console.log(`Fail`);


}


/*?
Tasks:
1:  Write a conditional statement to check a customer’s age at a bar. If the customer is under 18 log a message advising they are too young, otherwise ask what they would like to drink.

2: Declare a variable called "Password". Write an if statement that checks how many characters are in the password, if the password has more than 8 characters log the password to the console, if the password has less than 8 characters log to the console that the password is too short.

3: Create a variable that stores a number. Check whether the number is divisible by 3 or 5, if so log "This number is divisible by 3 or 5" to the console. Otherwise log an alternate message to the console.

4: Create a variable that stores a number. If the number is divisible by 3, log "fizz" to the console. If the number is divisible by 5 log "buzz" to the console. If the number is divisible by both 3 and 5, log "fizz buzz" to the console. Otherwise log the number to the console.
*/

let yourAge = 18;
if (yourAge == 18) {
    console.log("What do you want to drink?")
}
else {
    (yourAge < 18)
    console.log("You are too young, get out")
}

let password = "1111111";
if (password.length >= 8) {
    console.log("winner winner chicken dinner!")
}
else {
    (password.length <= 8)
    console.log("Make your password longer!")
}

let a = 10;
if (a / 3) {
    console.log("This number is divisible by 3 or 5")
}
if (a / 5) {
    console.log("This number is divisible by 3 or 5")
}
switch (true) {
    case a >= a / 3:
        console.log("This number is divisible by 3 or 5");
        break;
    case a >= a / 5:
        console.log("This number is divisible by 3 or 5");
        break;
}