//Task 1 
let food = document.getElementById("food");
let foodMenu = document.getElementById("foodMenu");
let drinkMenu = document.getElementById("drinkMenu");
let drink = document.getElementById("drink");
let button = document.getElementById("button");

button.addEventListener("click", () => {
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

//Task 3
let vacancy = document.getElementById("vacancy");
console.log(vacancy);
vacancy.addEventListener("mouseenter", (event) => {
    console.log(event.target);
    vacancy.style.fontSize = "60px";
    vacancy.style.marginLeft = "-10px";
})
vacancy.addEventListener("mouseleave", (event) => {
    vacancy.style.fontSize = "";
    vacancy.style.marginLeft = "";
})



//Task 2
let links = document.getElementsByClassName("link");

for (let link in links) {
    links[link].addEventListener("mouseover", (event) => {
        links[link].style.color = "pink";
        links[link].style.backgroundColor = "blue";
        links[link].style.fontWeight = "bold";
    })

    links[link].addEventListener("mouseout", (event) => {
        links[link].style.color = "";
        links[link].style.backgroundColor = "";
        links[link].style.fontWeight = "";
    })

}


