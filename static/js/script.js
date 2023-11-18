window.addEventListener("load", () => {
    document.querySelector(".loader").classList.add("loader--hidden")
});

$(document).ready(function () {
    $('.image-container').slick({
        infinite: true,   
        slidesToShow: 1,  
        slidesToScroll: 1,
        autoplay: true,   
        autoplaySpeed: 2000,
    });
});

$(document).ready(function(){
    $('.customer-logos').slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 1500,
        arrows: false,
        dots: false,
        pauseOnHover: false,
        responsive: [{
            breakpoint: 768,
            settings: {
                slidesToShow: 4
            }
        }, {
            breakpoint: 520,
            settings: {
                slidesToShow: 3
            }
        }]
    });
});

function menu_click() {
	if (document.getElementById("nav").style.display == "block"){
  		document.getElementById("nav").style.display = "none";
    }
    else{
    	document.getElementById("nav").style.display = "block";
    }
}