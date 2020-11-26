// Scroll 내릴 때 효과
document.addEventListener("DOMContentLoaded", function () {
    window.addEventListener('scroll', function (e) {
        if (window.scrollY > 30) {
            document.getElementById("id_nav").classList.add("black")
        } else {
            document.getElementById("id_nav").classList.remove('black');
        }
    });
});


// Responsive Collapsed Navbar 효과
function myFunction() {
    var navButton = document.getElementById("mySidebar")
    var pageOverlay = document.getElementsByClassName("overlay")

    if (navButton.classList.contains('active')) {
        navButton.classList.remove('active');
        pageOverlay[0].style.display = "none";
    } else {
        navButton.classList.add("active");
        pageOverlay[0].style.display = "block";
    }
}


// Submenu - 나의 보은
function dropFunction() {
    var subContent = document.getElementsByClassName("submenu")
    var upButton = document.getElementsByClassName("fa-caret-up");
    var downButton = document.getElementsByClassName("fa-caret-down");

    if (subContent[0].style.display == "block") {
        subContent[0].style.display = "none";
        upButton[0].style.display = "none";
        downButton[0].style.display = "inline-block"
    } else {
        subContent[0].style.display = "block";
        upButton[0].style.display = "inline-block";
        downButton[0].style.display = "none";
    }
}