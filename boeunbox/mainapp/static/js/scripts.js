// 메뉴 펼치기
const menuicon = document.querySelector('.menu-icon');
const menu = document.querySelector('.menu');

menuicon.addEventListener('click', () => {
    menu.classList.toggle('active');
});


// Scrolling Effect
$(document).ready(function () {
    $(window).scroll(function () {
        if ($(window).scrollTop() > 150) {
            $('.navbar').addClass('black');
        }
        else {
            $('.navbar').removeClass('black');
        }
    });
});