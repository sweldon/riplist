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

function updateListingMap(){

        $("#loading_div").html("<img src='/static/images/loading_gears.gif' />");

        var csrftoken = getCookie('csrftoken');

        custom_address = $("#custom_street").val() + " " + $("#custom_state").val() + " " + $("#custom_zip").val();

        jQuery.ajax({
        "headers" : {'X-CSRFToken': csrftoken},
        "url": "/browse/get_address",
        "type": "POST",
        "dataType": "json",
        'data': {"custom_address": custom_address},
        success: function (result) {
            $("#loading_div").html("");
            if(result.success){
                addmarker(new google.maps.LatLng(result.lat, result.lng))
            }else{
                $("#loading_div").html("<font color='red'><span class='glyphicon glyphicon-exclamation-sign'></span> Couldn't find address!</font>");
            }

        }
    });

}

function checkAddress(){

    if($("#address_dropdown").val() == "account"){

        $("#loading_div").html("<img src='/static/images/loading_gears.gif' width='58' height='58'/>");

        var csrftoken = getCookie('csrftoken');

        jQuery.ajax({
            "headers" : {'X-CSRFToken': csrftoken},
            "url": "/browse/get_address",
            "type": "POST",
            "dataType": "json",
            success: function (result) {
                $("#loading_div").html("");
                var street = result.street;
                var zip = result.zipcode;
                var state = result.state;
                $("#account_address").html("<b>"+street+", "+state+", "+zip+"</b><br /><br />");
                addmarker(new google.maps.LatLng(result.lat, result.lng))
            }
        });

        $("#optional_address").hide()
        $("#account_address").show()

    }else if($("#address_dropdown").val() == "other"){

        $("#account_address").hide()
        $("#optional_address").show()
    }else{
        $("#optional_address").hide()
        $("#account_address").hide()
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

$("#purchase_btn").click(function() {

    $("#createListingModal").find("[name='mdhd']").html("<center>Coming Soon!</center>");
    $("#createListingModal").find("[name='mdbd']").html("<center>Purchasing in development, please check back soon.</center>");
    $("#createListingModal").modal('toggle');

});
$("#contact_btn").click(function() {

    $("#createListingModal").find("[name='mdhd']").html("<center>Coming Soon!</center>");
    $("#createListingModal").find("[name='mdbd']").html("<center>Contact seller in development, please check back soon.</center>");
    $("#createListingModal").modal('toggle');

});
$("#user_link").click(function() {

    $("#createListingModal").find("[name='mdhd']").html("<center>Coming Soon!</center>");
    $("#createListingModal").find("[name='mdbd']").html("<center>This will link to the user's profile page. The score in parentheses is the user's feedback score. The colors will be representative of their trustworthiness.</center>");
    $("#createListingModal").modal('toggle');

});
$( "#search_button" ).click(function() {


    input_val = $( "#main_search" ).val();
    if(input_val != '') {
        search_data={}
        input_val = $("#main_search").val();
        distance_val = $("#distance_dropdown").val();

        materials = $("#mat").is(':checked');
        laydown_yards = $("#ly").is(':checked');
        equipment = $("#eq").is(':checked');

        search_data["search"] = input_val
        search_data["materials"] = materials
        search_data["laydown_yards"] = laydown_yards
        search_data["equipment"] = equipment
        search_data["distance"] = distance_val
        search_data["summary"] = "false"

        query(search_data);
    }

});
function query(search_data) {

     $("#results_container").html("<div id='loading_results'><img src='/static/images/loading_gears.gif'></img><br /><br /></div>");

    var csrftoken = getCookie('csrftoken');

    jQuery.ajax({
    headers : {'X-CSRFToken': csrftoken},
    url: "/browse/search_listings",
    type: "POST",
    data: search_data,
    dataType:"json",
    success: function(result){

        postResults(result, false);

    },error:function(result){
        alert("search error")
    }
});
    }


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