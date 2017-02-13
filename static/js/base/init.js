/**
 * Created by weldos01 on 10/31/16.
*/



function createListing(){



$('#listing_dropdown option').prop('selected', function() {
    return this.defaultSelected;
});

$("#noselection").select();

$("#listing_dropdown").show();

$("#buysell").hide();

jQuery("#createListingModal").find("[name='mdhd']").html("<center>What type of listing?</center>");

jQuery("#createListingModal").modal('toggle');


}

function checkType(){

$('#listing_dropdown').fadeOut('fast', function() {
    $('#buysell').fadeIn('fast');

});

}





function getCookie(name) {
var cookieValue = null;
if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }
}
return cookieValue;
}

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

function checkAddress(){

if($("#address_dropdown").val() == "account"){
$("#optional_address").hide()
}else if($("#address_dropdown").val() == "other"){
    $("#optional_address").show()
}
}

function checkMaterialOther(){

if($("#type_dropdown").val() == "other"){
    $("#other_explain_material").show()
}else{
$("#other_explain_material").hide()
}}

function checkHauling(){

if($("#hauling_dropdown").val() == "yes"){
    $("#hauling_options").show()
}else{
$("#hauling_options").hide()
}}

function checkLoading(){

if($("#loading_dropdown").val() == "yes"){
    $("#loading_options").show()
}else{
$("#loading_options").hide()
}}


$( document ).ready(function(){

$('#material_price').on('input', function() {

if($('#material_price').val() != "" && $('#material_price').val() != "")
{
$('#total_price').text( (parseFloat($('#material_price').val()) * parseFloat($('#material_amount').val())).toFixed(2));
}

});

$( "#datepicker_available" ).datepicker();

$( "#datepicker_expiration" ).datepicker();


search_data = {}

$.get("https://ipinfo.io", function (response) {

search_data["user_location"] = response.loc;

}, "jsonp")

$( "#search_button" ).click(function() {

    input_val = $( "#main_search" ).val();
    distance_val = $( "#distance_dropdown" ).val();

    materials = $( "#mat" ).is(':checked');
    laydown_yards = $( "#ly" ).is(':checked');
    equipment = $( "#eq" ).is(':checked');

    var csrftoken = getCookie('csrftoken');

    if(input_val != ''){

    search_data["search"]=input_val
    search_data["materials"]=materials
    search_data["laydown_yards"]= laydown_yards
    search_data["equipment"]=equipment
    search_data["distance"]= distance_val

    $( "#results_container" ).html("<div id='loading_results'><img src='/static/images/loading_gears.gif'></img><br /><br /></div>");

    jQuery.ajax({
    headers : {'X-CSRFToken': csrftoken},
    url: "/browse/search_listings",
    type: "POST",
    data: search_data,
    dataType:"json",
    success: function(result){

        $( "#results_container" ).html("");

        if( Object.keys(result.materials_results).length > 0){

        materials = result.materials_results

            for (var listing in materials) {
                var newlisting = '<a href="/browse/m/?id='+materials[listing]["id"]+'"><div class="result_item"><div class="type_material"></div><div class="thumbnail_item"><img src="/static/images/gravel.jpg"></img></div><div class="main_details"><div class="title_item">'+materials[listing]["volume"]+' '+materials[listing]["rate"]+' '+materials[listing]["type"]+'</div><div class="price">$'+materials[listing]["price"]+'/'+materials[listing]["rate"]+'</div></div><div class="details_container"><div class="distance">Distance: <b>'+materials[listing]["distance"]+' mi.</b></div><div class="date_available">Date Available: <b>'+materials[listing]["date_available"]+'</b></div><div class="material_details">Loading: <b>Yes</b><br />Hauling: <b>Yes</b></div></div></div></a><br />'
                $( "#results_container" ).append(newlisting);
            }

        }
        else if(Object.keys(result.laydown_results).length > 0){

        sites = result.laydown_results

            for (var listing in sites) {
                var newlisting = '<a href="/browse/s/?id='+sites[listing]["id"]+'"><div class="result_item"><div class="type_laydown"></div><div class="thumbnail_item"><img src="/static/images/dirt.jpg"></img></div><div class="main_details"><div class="title_item">'+sites[listing]["size"]+' '+sites[listing]["surface"]+' - '+sites[listing]["city"]+'</div><div class="price">$'+sites[listing]["price"]+'/'+sites[listing]["rate"]+'</div></div><div class="details_container"><div class="distance">Distance: <b>'+sites[listing]["distance"]+' mi.</b></div><div class="date_available">Date Available: <b>'+sites[listing]["date_available"]+'</b></div><div class="material_details">Loading: <b>Yes</b><br />Hauling: <b>Yes</b></div></div></div></a><br />'
                $( "#results_container" ).append(newlisting);
            }

        }

        else if(Object.keys(result.equipment_results).length > 0){
        equipment = result.equipment_results

            for (var listing in equipment) {
                var newlisting = '<a href="/browse/e/?id='+equipment[listing]["id"]+'"><div class="result_item"><div class="type_equipment"></div><div class="thumbnail_item"><img src="/static/images/tcrane.jpg"></img></div><div class="main_details"><div class="title_item">'+equipment[listing]["year"]+' '+equipment[listing]["make"]+' '+equipment[listing]["model"]+' '+equipment[listing]["type"]+'</div><div class="price">$'+equipment[listing]["price"]+'/'+equipment[listing]["rate"]+'</div></div><div class="details_container"><div class="distance">Distance: <b>'+equipment[listing]["distance"]+' mi.</b></div><div class="date_available">Date Available: <b>'+equipment[listing]["date_available"]+'</b></div><div class="material_details">Loading: <b>Yes</b><br />Hauling: <b>Yes</b></div></div></div></a><br />'
                $( "#results_container" ).append(newlisting);
            }

        }
        else{
         $( "#results_container" ).html("<div id='loading_results'><span class='glyphicon glyphicon-alert'></span> <span style='margin-left:15px;  opacity: .5;'>No results</span><br /><br /></div>");
        }


        //update map
        //add results to page
        //document.getElementById('results_container').scrollIntoView();
        for(var i=0; i< result.markers.length; i++){
        addmarker(new google.maps.LatLng(result.markers[i][0], result.markers[i][1]))
        }

        $('html, body').animate({
        scrollTop: $("#mapholder").offset().top
        }, 500);




    },error:function(result){
        alert("search error")
    }
});
    }


});

$( "#dateneeded" ).datepicker();
$( "#dateavailable" ).datepicker();

$( "input#searchLocation" ).autocomplete({
                    source: "/browse/searchLocation/",
                    minLength: 2
});

$('#main_search').keyup(function(event)
{
    if(event.keyCode == 13)
    {

        $('#search_button').click();

    }

});


$("#menudropdown").click(function() {

   document.getElementById("home-dropdown").classList.toggle("show");

});


});


// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('#menudropdown')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}