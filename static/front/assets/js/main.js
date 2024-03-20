(function() {
	"use strict";

    // Navbar Sticky JS
    try {
        const nav = document.querySelector('.wile-navbar');
        let navTop = nav.offsetTop;
        
        function fixedNav() {
        if (window.scrollY >= navTop) {
            nav.classList.add('sticky');
        } else {
            nav.classList.remove('sticky');
        }
        }
        window.addEventListener('scroll', fixedNav);
    } catch (err) {}

    // Services Slider JS
    var swiper = new Swiper(".mySwiperServices", {
        spaceBetween: 20,
        loop: true,
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        breakpoints: {
            0: {
                slidesPerView: 1
            },
            576: {
                slidesPerView: 1
            },
            768: {
                slidesPerView: 2
            },
            992: {
                slidesPerView: 3
            },
            1200: {
                slidesPerView: 4
            }
        }
    });

    // Product Slider JS
    var swiper = new Swiper(".mySwiperProduct", {
        spaceBetween: 25,
        loop: true,
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        breakpoints: {
            0: {
                slidesPerView: 1
            },
            576: {
                slidesPerView: 1
            },
            768: {
                slidesPerView: 2
            },
            992: {
                slidesPerView: 3
            },
            1200: {
                slidesPerView: 4
            }
        }
    });

    // Customer Slider JS
    var swiper = new Swiper(".mySwiperOne", {
        loop: true,
        spaceBetween: 10,
        slidesPerView: 3,
        freeMode: true,
        watchSlidesProgress: true,
        breakpoints: {
            0: {
                slidesPerView: 1
            },
            576: {
                slidesPerView: 0
            },
            768: {
                slidesPerView: 2
            },
            992: {
                slidesPerView: 3
            },
            1200: {
                slidesPerView: 3
            }
        }
    });
    var swiper2 = new Swiper(".mySwiperTwo", {
        loop: true,
        spaceBetween: 10,
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        thumbs: {
            swiper: swiper,
        },
    });
    
    // My Swiper Partner Slider JS
	var swiper = new Swiper(".mySwiperPartner", {
        slidesPerView: 6,
        spaceBetween: 50,
        centeredSlides: true,
        loop: true,
        autoplay: {
            delay: 2000,
            disableOnInteraction: false,
        },
        breakpoints: {
            0: {
                slidesPerView: 2
            },
            576: {
                slidesPerView: 3
            },
            768: {
                slidesPerView: 5
            },
            992: {
                slidesPerView: 6
            },
            1200: {
                slidesPerView: 6
            }
        }
    });

    // Project Slider JS
    var swiper = new Swiper(".mySwiperProject", {
        spaceBetween: 25,
        loop: true,
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        breakpoints: {
            0: {
                slidesPerView: 1
            },
            576: {
                slidesPerView: 1
            },
            768: {
                slidesPerView: 2
            },
            992: {
                slidesPerView: 3
            },
            1200: {
                slidesPerView: 4
            }
        }
    });

    // My Swiper Testimonial Slider JS
    var swiper = new Swiper(".mySwiperFeedback", {
        spaceBetween: 20,
        loop: true,
        navigation: {
            prevEl: ".swiper-button-prev",
            nextEl: ".swiper-button-next",
        },
        breakpoints: {
            0: {
                slidesPerView: 1
            },
            576: {
                slidesPerView: 1
            },
            768: {
                slidesPerView: 2
            },
            992: {
                slidesPerView: 2
            },
            1200: {
                slidesPerView: 2
            }
        }
    });

    // My Swiper Testimonials Slider JS
    var swiper = new Swiper(".mySwiper", {
        spaceBetween: 25,
        loop: true,
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        breakpoints: {
            0: {
                slidesPerView: 1
            },
            576: {
                slidesPerView: 1
            },
            768: {
                slidesPerView: 2
            },
            992: {
                slidesPerView: 2
            },
            1200: {
                slidesPerView: 2
            }
        }
    });

    // My Swiper Team Slider JS
    var swiper = new Swiper(".mySwiperTeam", {
        spaceBetween: 20,
        loop: true,
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        breakpoints: {
            0: {
                slidesPerView: 1
            },
            576: {
                slidesPerView: 1
            },
            768: {
                slidesPerView: 2
            },
            992: {
                slidesPerView: 3
            },
            1200: {
                slidesPerView: 4
            }
        }
    });

    // Go Top Button JS
    try {
        var btnTop = document.querySelector('#scrolltop-arrow');

        var btnReveal = function () { 
            if (window.scrollY > 300) {
            btnTop.classList.add('visible');
            } else {
            btnTop.classList.remove('visible');
            }
        }
    } catch (err) {}

    // For Live Projects
    window.addEventListener('load',function(){
        document.querySelector('body').classList.add("loaded")  
    });

    // ===================== js for pre loader =================
    var loader = document.querySelector(".cssload-preloader");
        window.addEventListener("load", function () {
        loader.style.display = "none";
    });
    // ++++++++++++ end pre loader   __________________

    //
    scrollCue.init();

})()