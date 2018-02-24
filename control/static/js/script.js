function onClick(element) {
  document.getElementById("imagen").src = element.src;
  document.getElementById("modal").style.display = "block";
  var captionText = document.getElementById("mostrar");
  captionText.innerHTML = element.alt;
}

function myMap() {
var myCenter = new google.maps.LatLng(8.211059, -72.253574);
var mapProp = {center:myCenter, zoom:12, scrollwheel:false, draggable:false, mapTypeId:google.maps.MapTypeId.ROADMAP};
var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
var marker = new google.maps.Marker({position:myCenter});
marker.setMap(map);
}
$(document).ready(function(){
  $("#carusel1").owlCarousel({
          nav: true,
          loop: true,
          autoplay:true,
          autoplayTimeout:5000,
          autoplayHoverPause:true,
          slideSpeed : 300,
          paginationSpeed : 400,
          navText : ["<img src='img/prev.png'>","<img src='img/next.png'>"],
          singleItem:true,
          responsiveClass:true,
    responsive:{
        0:{
            items:2,
            nav:false
        },
        600:{
            items:3,
            nav:false
        },
        1000:{
            items:6,
            nav:true,
            loop:true
        }
    }
    });

$(".animacion1").waypoint(function() {
$(".animacion1").toggleClass( 'animated slideInUp' );
},
{
offset: '95%',
triggerOnce: true
});
$(".animacion2").waypoint(function() {
$(".animacion2").toggleClass( 'animated slideInUp' );
},
{
offset: '95%',
triggerOnce: true
});
$(".animacion3").waypoint(function() {
$(".animacion3").toggleClass( 'animated slideInUp' );
},
{
offset: '95%',
triggerOnce: true
});
$(".animacion4").waypoint(function() {
$(".animacion4").toggleClass( 'animated slideInUp' );
},
{
offset: '95%',
triggerOnce: true
});
$("#porqueElegirnos").waypoint(function() {
$("#porqueElegirnos").toggleClass( 'animated slideInUp' );
},
{
offset: '95%',
triggerOnce: true
});
$("#carruselEfect").waypoint(function() {
$("#carruselEfect").toggleClass( 'animated slideInUp' );
},
{
offset: '95%',
triggerOnce: true
});
});

