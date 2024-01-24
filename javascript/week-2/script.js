/*
Learning Objectives
 
Recap and apply using the DOM
 
Learn how to create events in JS
 
Create interactive elements on a webpage by using the DOM and events together.
*/

//Gathering the paragraphs 
let p1 = document.getElementById('p1');
let p2 = document.getElementById('p2');
let p3 = document.getElementById('p3');
let p4 = document.getElementById('p4');
let p5 = document.getElementById('p5');

/*Task// 
Use one of the event listeners we have looked at
 
8 mins --> until 9:45am
*/
p3Btn.addEventListener('click', function run() {
    if (p3.style.display != 'block') {
        p3.style.display = "block"
        console.log(p3 showing)
        p4.style.display = "none"
    }
})

