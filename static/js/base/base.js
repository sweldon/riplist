/**
 * Created by weldos01 on 9/1/16.
 */

$(document).ready(function(){

  $( function() {
    $( "#progressbar" ).progressbar({
      value: 37
    });
  } );
    $("#loginForm").keyup(
        function(event){
            if(event.keyCode === 13) {
                $(".loginbtn").click();
            }})


    $("#directripval").keyup(
    function(event){
        if(event.keyCode === 13) {
            $(".ripbtn").click();
        }})

    $( "#ripbtn" ).click(function() {

        alert('rip')

        });


});