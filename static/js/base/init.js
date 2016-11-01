/**
 * Created by weldos01 on 10/31/16.
 */
$( document ).ready(function(){


$("#buy").click(function() {

    jQuery("#alertModal").find("[name='mdhd']").html("Purchase");
    jQuery("#alertModal").find("[name='mdbd']").html("Purchasing options coming soon.")

    $("#alertModal").modal('show');

});

$("#sell").click(function() {

    jQuery("#alertModal").find("[name='mdhd']").html("Sell");
    jQuery("#alertModal").find("[name='mdbd']").html("Vendor options coming soon.")

    $("#alertModal").modal('show');

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