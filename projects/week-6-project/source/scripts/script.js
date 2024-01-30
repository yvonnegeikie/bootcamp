const modal = document.getElementById("myModal");
const button = document.getElementById("modalButton");
const span = document.getElementsByClassName("close")[0];

button.onclick = function () {
    modal.style.display = "block";
}

span.onclick = function () {
    modal.style.display = "none";
}

span.onclick = function () {
    modal.style.display = "none";
}

const instruments = {
    "guitar": {
        "title": "guitar title",
        "description": "guitar description",
        "image": "https://placehold.co/600x400/000000/FFF"
    },
    "drums": {
        "title": "drums title",
        "descriptiom": "drums description",
        "image": "https://placehold.co/600x400/000000/000"
    },
    "keyboard": {
        "title": "keyboard title",
        "description": "keyboard description",
        "image": "https://placehold.co/600x400/000000/ff0"
    },
}
console.log(instruments)
console.log(instruments.guitar.title)