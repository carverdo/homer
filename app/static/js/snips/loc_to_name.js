// Defines Function and Calls (producing return)
// ============================================================
var geocoder;
var latlngStr = '', lat = 0.0, lng = 0.0;
var latlng;

$(document).ready(function() {
    geocoder = new google.maps.Geocoder();
    // $("#test").text("bosh");
    // console.log($("#latlng").data('value'));
    from_LaLo_to_Place();
})

function from_LaLo_to_Place() {
    var input = $("#latlng").data('value');
    console.log(input);
    latlngStr = input.split(",", 2);
    lat = parseFloat(latlngStr[0]);
    lng = parseFloat(latlngStr[1]);
    latlng = google.maps.LatLng(lat, lng);
    geocoder.geocode({'latLng': latlng}, function(results, status) {
        console.log(results);
        $("#placeName").text('' + results[4].formatted_address + '');
    });
}
