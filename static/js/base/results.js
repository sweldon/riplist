function postResults(result, summary_search){

        $( "#results_container" ).html("");

        if( Object.keys(result.materials_results).length > 0){

        materials = result.materials_results

            for (var listing in materials) {
                var newlisting = '<a href="/browse/materials/?id='+materials[listing]["id"]+'"><div class="result_item"><div class="type_material"></div><div class="thumbnail_item"><img src="/media/'+materials[listing]["images"][0]+'" width="125" height="125"/></div><div class="main_details"><div class="title_item">'+materials[listing]["volume"]+' '+materials[listing]["rate"]+' '+materials[listing]["type"]+'</div><div class="price">$'+materials[listing]["price"]+'/'+materials[listing]["rate"]+'</div></div><div class="details_container"><div class="distance">Distance: <b>'+materials[listing]["distance"]+' mi.</b></div><div class="date_available">Date Available: <b>'+materials[listing]["date_available"]+'</b></div><div class="material_details">Loading: <b>Yes</b><br />Hauling: <b>Yes</b></div></div></div></a><br />'
                $( "#results_container" ).append(newlisting);
            }

        }
        else if(Object.keys(result.laydown_results).length > 0){

        sites = result.laydown_results

            for (var listing in sites) {
                var newlisting = '<a href="/browse/sites/?id='+sites[listing]["id"]+'"><div class="result_item"><div class="type_laydown"></div><div class="thumbnail_item"><img src="/static/images/dirt.jpg"></img></div><div class="main_details"><div class="title_item">'+sites[listing]["size"]+' '+sites[listing]["surface"]+' - '+sites[listing]["city"]+'</div><div class="price">$'+sites[listing]["price"]+'/'+sites[listing]["rate"]+'</div></div><div class="details_container"><div class="distance">Distance: <b>'+sites[listing]["distance"]+' mi.</b></div><div class="date_available">Date Available: <b>'+sites[listing]["date_available"]+'</b></div><div class="material_details">Loading: <b>Yes</b><br />Hauling: <b>Yes</b></div></div></div></a><br />'
                $( "#results_container" ).append(newlisting);
            }

        }

        else if(Object.keys(result.equipment_results).length > 0){
        equipment = result.equipment_results

            for (var listing in equipment) {
                var newlisting = '<a href="/browse/equipment/?id='+equipment[listing]["id"]+'"><div class="result_item"><div class="type_equipment"></div><div class="thumbnail_item"><img src="/static/images/tcrane.jpg"></img></div><div class="main_details"><div class="title_item">'+equipment[listing]["year"]+' '+equipment[listing]["make"]+' '+equipment[listing]["model"]+' '+equipment[listing]["type"]+'</div><div class="price">$'+equipment[listing]["price"]+'/'+equipment[listing]["rate"]+'</div></div><div class="details_container"><div class="distance">Distance: <b>'+equipment[listing]["distance"]+' mi.</b></div><div class="date_available">Date Available: <b>'+equipment[listing]["date_available"]+'</b></div><div class="material_details">Loading: <b>Yes</b><br />Hauling: <b>Yes</b></div></div></div></a><br />'
                $( "#results_container" ).append(newlisting);
            }

        }
        else{
         $( "#results_container" ).html("<div id='loading_results'><span class='glyphicon glyphicon-alert'></span> <span style='margin-left:15px;  opacity: .5;'>No results</span><br /><br /></div>");
        }


        //update map
        //add results to page
        //document.getElementById('results_container').scrollIntoView();
        if(!summary_search) {
            for (var i = 0; i < result.markers.length; i++) {
                addmarker(new google.maps.LatLng(result.markers[i][0], result.markers[i][1]))
            }

            $('html, body').animate({
            scrollTop: $("#mapholder").offset().top
            }, 500);
        }

        $( "#results_container" ).append('<div id="pages"></div>');
        $("#pages").html(result.total_pages);



}