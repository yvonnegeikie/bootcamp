
//instruments object. 
const instruments = {
    "guitar": {
        "title": "guitar title",
        "description": "guitar description",
        "image": "https://placehold.co/600x400/000000/FFF"
    },
    "drums": {
        "title": "drums title",
        "description": "drums description",
        "image": "https://placehold.co/600x400/000000/F00"
    },
    "keyboard": {
        "title": "keyboard title",
        "description": "keyboard description",
        "image": "https://placehold.co/600x400/000000/ff0"
    },
}
// console.log(instruments)
// console.log(instruments.guitar.title)

const instrumentTitle = document.getElementById('instrumentTitle');
console.log(instrumentTitle);
const instrumentDescription = document.getElementById('instrumentDescription');
const instrumentImage = document.getElementById('instrumentImage');
// set new const instrumentDescription to the HTML element ID 
//'instrumentDescription'


//instruments function.
const selectInstrument = (instrument) => {

    instrumentTitle.innerText = instruments[instrument].title;
    instrumentDescription.innerText = instruments[instrument].description;
    instrumentImage.src = instruments[instrument].image;
    // set the inner text of instrumentTitle
    // to instruments[instrument].title

    // set the inner text of instrumentDescription
    // to instruments[instrument].description

    // set the image source of instrumentImage
    // to instruments[instrument].image

    console.log(instruments[instrument].title);
    return instruments[instrument];
}
// const guitarDetails = selectInstrument("guitar");
// const drumsDetails = selectInstrument("drums");
// const keyboardDetails = selectInstrument("keyboard");

//Modal for video 
const modal = document.getElementById("myModal");
const button = document.getElementById("modalButton");
let span = document.getElementsByClassName("close")[0];
button.onclick = function () {
    modal.style.display = "block";
}
span.onclick = function () {
    modal.style.display = "none";
}
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


