// 메뉴 펼치기
const menuicon = document.querySelector('.menu-icon');
const menu = document.querySelector('.menu');

menuicon.addEventListener('click', () => {
    menu.classList.toggle('active');
});


// Scrolling Effect
// $(document).ready(function(){
// $(window).on("scroll", function () {
//     if ($(this).scrollTop()) {
//         $(".navbar").addClass("black");
//     }
//     else {
//         $(".navbar").removeClass("black");

//     });
// });
