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

$('#main_search').keyup(function(event)
{
    if(event.keyCode == 13)
    {


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