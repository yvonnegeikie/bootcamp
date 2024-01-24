let food = document.getElementById("food");
let foodMenu = document.getElementById("foodMenu");
let drinkMenu = document.getElementById("drinkMenu");
let drink = document.getElementById("drink");
let button = document.getElementById("button");

button.addEventListener("click", () => {
    console.log("click");
    if (food.style.display === "block") {
        food.style.display = "none"
        foodMenu.style.display = "none"
        drink.style.display = "block"
        drinkMenu.style.display = "block"
        button.innerText = "Food Menu"
    }
    else {
        food.style.display = "block"
        foodMenu.style.display = "block"
        drink.style.display = "none"
        drinkMenu.style.display = "none"
        button.innerText = "Drink Menu"
    }

});

//Task 2 - TIm 
let links = document.querySelectorAll("nav a");// create an array 


// for (let link in links) {
//     links[link].addEventListener("mouseover", function run() {
//         links[link].style.backgroundcolor = "pink"
//         links[link].style.fontFamily = "Impact"
//     }
//     )
// }

// for (let link in links) {
//     links[link].addEventListener("mouseout", function run() {
//         links[link].style.backgroundcolor = "White"
//         links[link].style.fontFamily = "fantasy"
//     }
//     )
// }
