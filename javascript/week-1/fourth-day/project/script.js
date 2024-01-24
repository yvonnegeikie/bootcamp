//Tasks:

/*1: Create an array of your favourite films / TV shows, up to 5 items. Use an array method to add 2 more items to your array. Use a loop to cycle through the array and log each item to the console.*/

/*2: Generate 10 random numbers between 1-100 and log them to the console.*/
for (let i = 0; i < 10; i++) {
    console.log(Math.floor(Math.random() * 100)) + 1;
}

/*3: Create a loop that counts backwards from 20-0.*/

/*4: Generate 5 random numbers between 1-50. For each number generated, check if the number is divisible by 5 or not. Log whether it is divisible or not to the console.*/

for (let i = 0; i < 5; i++) {
    const randomNumber1 = Math.ceil(Math.random() * 51);

    if (randomNumber1 % 5 === 0) {
        console.log(`${randomNumber1} is divisible! Yay!`);
    }
    else {
        console.log(`${randomNumber1} is not divisible .. Boo!`);
    }
}

