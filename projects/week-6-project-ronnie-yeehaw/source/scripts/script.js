
//instruments object. 
const instruments = {
    "guitar": {
        "title": "Guitar",
        "description": "In the dusty attic of Ronnie’s great aunt, nestled amongst cobwebs and forgotten dreams, lay Clementine, an acoustic guitar with a heart full of forgotten melodies. Crafted from the finest mahogany, her wood gleamed in the dim light, whispering tales of smoky jazz bars and moonlit serenades. ",
        "image": "/source/images/ronnie-guitar.jpg"
    },
    "drums": {
        "title": "Drums",
        "description": "Thumper the drumkit came to Ronnie on ‘loan’ after Ronnie’s friend decided to move back home to Korea. Ronnie didnt know much Korean prior to jamming with Thumper but has had to learn quickly!",
        "image": "/source/images/ronnie-drums.jpg"
    },
    "keyboard": {
        "title": "Bass",
        "description": "Ronnie found Bruno in the dimly lit corner of a dusty pawn shop, nestled between a chipped violin and a tarnished trumpet. His strings, once vibrant red, were now faded, his body bore the nicks and scratches of countless journeys. Yet, beneath the wear and tear, Bruno thrummed with a quiet melody, waiting for the right touch to awaken it.",
        "image": "/source/images/ronnie-bass.jpg"
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
selectInstrument("guitar");
// const drumsDetails = selectInstrument("drums");
// const keyboardDetails = selectInstrument("keyboard");


//Add Active Class to buttons 
const buttons = document.querySelectorAll('.button');

buttons.forEach(button => {
    button.addEventListener('click', handleClick);
});

function handleClick(e) {
    // Remove active class from all buttons:
    buttons.forEach(button => button.classList.remove('active'));

    // Add active class to the clicked button:
    e.target.classList.add('active');
}



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


