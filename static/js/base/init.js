/**
 * Created by weldos01 on 10/31/16.
 */
$( document ).ready(function(){

$( "#dateneeded" ).datepicker();
$( "#dateavailable" ).datepicker();

$( "input#searchLocation" ).autocomplete({
                    source: "/browse/searchLocation/",
                    minLength: 2
});

$('#searchLocation').keyup(function(event)
{
    if(event.keyCode == 13)
    {
        // get lat and lng of city and update map with it
    jQuery("#alertModal").find("[name='mdhd']").html("Search near you");
    jQuery("#alertModal").find("[name='mdbd']").html("Searching coming soon")

    $("#alertModal").modal('show');

    }
    // if ( event.keyCode === 27 ) { // ESC
    //     $( "#close" ).click();
    // }
});

$("#buy").click(function() {

    // jQuery("#alertModal").find("[name='mdhd']").html("Purchase");
    // jQuery("#alertModal").find("[name='mdbd']").html("Purchasing options coming soon.")

    $("#buyModal").modal('show');

});

$("#user-link").click(function() {

    jQuery("#alertModal").find("[name='mdhd']").html("User profile");
    jQuery("#alertModal").find("[name='mdbd']").html("User profiles and ratings coming soon.")

    $("#alertModal").modal('show');

});


$("#sell").click(function() {

    // jQuery("#alertModal").find("[name='mdhd']").html("Sell");
    // jQuery("#alertModal").find("[name='mdbd']").html("Vendor options coming soon.")

    $("#sellModal").modal('show');

});

$("#menudropdown").click(function() {

   document.getElementById("home-dropdown").classList.toggle("show");

});



});

function dropdown() {

}

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