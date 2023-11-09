$(document).ready(function () {
    $('.image-container').slick({
        infinite: true,   
        slidesToShow: 1,  
        slidesToScroll: 1,
        autoplay: true,   
        autoplaySpeed: 2000,
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