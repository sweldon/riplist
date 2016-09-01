/**
 * Created by weldos01 on 9/1/16.
 */

$(document).ready(function(){


    $("#loginForm").keyup(
        function(event){
            if(event.keyCode === 13) {
                $(".loginbtn").click();
            }})


});