//
function dropdown() {

    //
    let navbar = document.getElementById("navbar");

    //
    if (navbar.classList.contains("dropped")) {
        navbar.classList.remove("dropped");
        navlinks.style.maxHeight = "0px";
    }

    //
    else {
        navbar.classList.add("dropped");
        navlinks.style.maxHeight = "217px";
    };

};


//
var navlinks = document.getElementById("navlinks");
navlinks.style.maxHeight = "0px";


//
const route = window.location.pathname;


//
const navanchors = document.querySelectorAll(".navanchor");


//
navanchors.forEach(navanchor => {
    
    //
    if (navanchor.getAttribute("href") === route) {
        navanchor.classList.add("active");
    }
    
    //
    else {
        navanchor.classList.remove("active");
    };

});