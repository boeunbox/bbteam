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
    var navButton = document.getElementById("myCollapsed")
    if (navButton.classList.contains('active')) {
        navButton.classList.remove('active');
    } else {
        navButton.classList.add("active");
    }
}