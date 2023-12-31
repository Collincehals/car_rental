var swiper = new Swiper(".mySwiper", {
    spaceBetween: 30,
    breakpoints: {
        1024: {
            slidesPerView: 3,
          },
          768: {
            slidesPerView: 2,
          },
          100: {
            slidesPerView: 1,
          },
    },
    centeredSlides: true,
    autoplay: {
    delay: 2500,
    disableOnInteraction: false,
    },
    pagination: {
    el: ".swiper-pagination",
    clickable: true,
    },
    navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
    },
});


