
var lat;
var lng;
var VAlat = 36.8508;
var VAlng = -76.2859;
function getLat(){
    return lat;
}
function getLng(){
    return lng;
}
function setLat(input){
    lat = input;
}
function setLng(input){
    lng = input;
}


function getLocation() {

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {

    var lat = position.coords.latitude;
    var lng = position.coords.longitude;

    setLat(lat);
    setLng(lng);

    initMap();

}

function showError(error) {
    // If no location, show a mobile friendly modal asking to enable location

    switch(error.code) {
        case error.PERMISSION_DENIED:
            setLat(VAlat);
            setLng(VAlng);
            initMap();
        case error.POSITION_UNAVAILABLE:
            setLat(VAlat);
            setLng(VAlng);
            initMap();
        case error.TIMEOUT:
            setLat(VAlat);
            setLng(VAlng);
            initMap();
        case error.UNKNOWN_ERROR:
            setLat(VAlat);
            setLng(VAlng);
            initMap();
    }
}

getLocation();



function addmarker(latilongi) {
    var marker = new google.maps.Marker({
        position: latilongi,
        url: 'http://www.google.com/',
        title: 'new marker',
        draggable: false,
        map: map
    });
    map.setCenter(marker.getPosition())
}
var map;
function initMap() {
    var userLatLng = new google.maps.LatLng(getLat(), getLng());
    map = new google.maps.Map(document.getElementById('listing_map'), {
        center: userLatLng,
        zoom: 12,
        disableDefaultUI: true,
    });

    addmarker(new google.maps.LatLng(getLat(), getLng()))

}

function comingSoon(){


jQuery("#createListingModal").find("[name='mdhd']").html("<center>Image Upload</center>");
jQuery("#createListingModal").find("[name='mdbd']").html("<center>Image uploads for your listing is in development and will be available very soon!</center>");
jQuery("#createListingModal").modal('toggle');


}

