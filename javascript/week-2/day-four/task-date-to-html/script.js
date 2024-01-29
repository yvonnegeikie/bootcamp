//!Add a date to HTML

let divDate = document.getElementById("date");

//Get current date 
const d = new Date();

//set the current date in the d variable to the following format 
const date = d.toLocaleString('default', //time zone eg. en-gb
    {
        day: "2-digit",
        month: "numeric",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hourCycle: "h24"
    }
);

divDate.innerText = date;
console.log(date);


