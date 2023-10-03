$(document).ready(function () {

    //  Adding  smooth scrolling to all links
    $("a").on("click", function (event) {
        
        if (this.hash !== "") {
            
            event.preventDefault();

            // Storing hash
            var hash = this.hash;

           
            $("html, body").animate(
                {
                    scrollTop: $(hash).offset().top,
                },
                800,
                function () {
                    // Adding hash (#) to URL when done scrolling (default click behavior)
                    window.location.hash = hash;
                }
            );
        } 
    });
});

var swiper = new Swiper(".slide-container", {
    slidesPerView: 4,
    spaceBetween: 20,
    sliderPerGroup: 4,
    loop: true,
    centerSlide: "true",
    fade: "true",
    grabCursor: "true",
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      520: {
        slidesPerView: 2,
      },
      768: {
        slidesPerView: 3,
      },
      1000: {
        slidesPerView: 4,
      },
    },
});

// JS to change background on scrolling by adding the 'scrolled' class 
window.addEventListener('scroll', function() {
  var navbar = document.querySelector('.navbar');
  if (window.scrollY > 0) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

let subMenu = document.getElementById("profile-subMenu")

function toggleMenu() {
    subMenu.classList.toggle("open-menu")
}