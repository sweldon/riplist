/**
 * Created by weldos01 on 10/31/16.
*/
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

$( document ).ready(function(){
$( "#search_button" ).click(function() {

    input_val = $( "#main_search" ).val();

    materials = $( "#mat" ).is(':checked');
    laydown_yards = $( "#ly" ).is(':checked');
    equipment = $( "#eq" ).is(':checked');
    distance = $( "#dist" ).is(':checked');

//    $( "#results_container" ).text("");

    var csrftoken = getCookie('csrftoken');

    if(input_val != ''){
       jQuery.ajax({
    "headers" : {'X-CSRFToken': csrftoken},
    "url": "/browse/search_listings",
    "type": "POST",
    'data':{search:input_val, materials:materials, laydown_yards: laydown_yards, equipment:equipment, distance:distance},
    "dataType":"json",
    success: function(result){

        if( result.material_results != null){

        materials = result.material_results

            for (var listing in materials) {
                var newlisting = '<div class="result_item"><div class="type_item"></div><div class="thumbnail_item"><img src="/static/images/gravel.jpg"></img></div><div class="main_details"><div class="title_item">'+materials[listing]["volume"]+' cu yd Gravel</div><div class="price">$'+materials[listing]["price"]+'/cu yd</div></div><div class="details_container"><div class="distance">Distance: <b>4 mi.</b></div><div class="date_available">Date Available: <b>'+materials[listing]["date_available"]+'</b></div><div class="material_details">Loading: <b>Yes</b><br />Hauling: <b>Yes</b></div></div></div><br />'
                $( "#results_container" ).append(newlisting);
            }

        }
        else if( result.laydown_results != null){

        sites = result.laydown_results

            for (var listing in sites) {
                var newlisting = '<div class="result_item"><div class="type_item"></div><div class="thumbnail_item"><img src="/static/images/gravel.jpg"></img></div><div class="main_details"><div class="title_item">'+sites[listing]["volume"]+' cu yd Gravel</div><div class="price">$'+sites[listing]["price"]+'/cu yd</div></div><div class="details_container"><div class="distance">Distance: <b>4 mi.</b></div><div class="date_available">Date Available: <b>'+sites[listing]["date_available"]+'</b></div><div class="material_details">Loading: <b>Yes</b><br />Hauling: <b>Yes</b></div></div></div><br />'
                $( "#results_container" ).append(newlisting);
            }

        }



        //update map
        //add results to page
        //document.getElementById('results_container').scrollIntoView();
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