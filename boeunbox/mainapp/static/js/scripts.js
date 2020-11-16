// Scroll 내릴 때 효과
document.addEventListener("DOMContentLoaded", function () {
    window.addEventListener('scroll', function (e) {
        if (window.scrollY > 100) {
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