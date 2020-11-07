// 메뉴 펼치기
// const menuicon = document.querySelector('.menu-icon');
// const menu = document.querySelector('.menu');

// menuicon.addEventListener('click', () => {
//     menu.classList.toggle('active');
// });


document.addEventListener("DOMContentLoaded", function () {
    // Transition effect for navbar 
    window.addEventListener('scroll', function (e) {
        // checks if window is scrolled more than 500px, adds/removes solid class
        if (window.scrollY > 100) {
            document.getElementById("id_nav").classList.add("black")
        } else {
            document.getElementById("id_nav").classList.remove('black');
        }
    });
});

/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myCollapsed").classList.toggle("active");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
    if (!event.target.matches('.btn-collapse')) {
        var collapse = document.getElementsByClassName("collapsed-content");
        var i;
        for (i = 0; i < collapse.length; i++) {
            var collapseNav = collapse[i];
            if (collapseNav.classList.add('active')) {
                collapseNav.classList.remove('active');
            }
        }
    }
}