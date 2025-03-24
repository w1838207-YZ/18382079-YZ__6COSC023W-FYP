//
function dropdown() {
    //
    var navbar = document.getElementById("navbar");
    //
    if (navbar.classList.contains("responsive")) {
        navbar.classList.remove("responsive");
    }
    //
    else {
        navbar.classList.add("responsive");
    }
}


//
const route = window.location.pathname;
//
const links = document.querySelectorAll(".link");
//
links.forEach(link => {
    //
    if (link.getAttribute("href") === route) {
        link.classList.add("active");
    }
    //
    else {
        link.classList.remove("active");
    }
})