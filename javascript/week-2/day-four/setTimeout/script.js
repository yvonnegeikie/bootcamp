// adds a 1 second delay in 'Hello' showing on console 
// function hello() {
//     console.log('Hello');
// }
// hello();
// setTimeout(hello, 1000);


// const name = '';
// const byeText = '';
// function greet(name, byeText) {
//     console.log('Good morning', ' ', name, byeText);
// }


// greet('Fred', 'SeeYa');
// let timeOutID = setTimeout(greet, 5000, 'Rob', 'Goodbye');


// SCENARIO - you have a website where there are some articles/posts.
// You want to ask the user to SIGN-UP after 20 seconds.
// However, if the user has already clicked on the
// subscribe button WITHIN 20 seconds,
// then there is NO point in running the logic (asking them to subscribe).

// TASK - BUILD THE FOLLOWING INSIDE A FUNCTION:
// if (time>=20 seconds) and the user has subscribed (boolean) && (&& = and operator)
// clearTimeOut
// else the user has NOT subscribed
// setTimeOut (20000) //20 seconds

/*function textChange() {
    let p = document.getElementById("hello")
    p.style.fontFamily = "Impact"
}

let para = setTimeout(textChange, 5000)

let pBtn = document.getElementById("pBtn")
pBtn.addEventListener('click', function run() {
    clearTimeout(para);
})*/

// let subT = false
// let subBtn = document.getElementById('subscribe')

// subscribe1 = setTimeout(subscribe, 1000)

// subBtn.addEventListener('click', function run() {
//     subT = true
//     console.log('Event Listener Working')
//     if (subT == true) {
//         clearTimeout(subscribe1)
//         console.log('timeoutCleared')
//     }
// })

// function subscribe() {
//     if (subT == false) {
//         console.log('You are not subscribed')
//     } else {
//         console.log('You are subscribed')
//         clearTimeout(subscribe1)
//     }
// }

const modal = document.querySelector("#test");
const subBtn = document.querySelector("#subscribe");

const subTimer = setTimeout(() => {
    modal.showModal();
}, 20000);

subBtn.addEventListener("click", () => {
    clearTimeout(subTimer);
});


// Creating Date Objects
// There are four ways to create a date object.

// new Date()
// new Date(milliseconds)
// new Date(Date string)
// new Date(year, month, day, hours, minutes, seconds, milliseconds)

const timeNow = new Date();
console.log(timeNow); // shows current date and time /Thu Jan 25 2024 11:30:45 GMT+0000 (Greenwich Mean Time)


const time1 = new Date(2020, 1, 20, 4);
console.log(time1); // Thu Feb 20 2020 04:00:00 GMT+0000 (Greenwich Mean Time)