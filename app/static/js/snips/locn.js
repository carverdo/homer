// Defines Function and Calls (producing return)
// ============================================================
var crd;
var geocoder;
var latlngStr = '', lat = 0.0, lng = 0.0;
var latlng;
var placeName='xx';

$(document).ready(function() {
    geocoder = new google.maps.Geocoder();
    // setInterval("getLocation()", 5000);
    getLocation();
});


function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(success);
    } else {
        $("#lalo").text('Geolocation switched off or not supported.');
    }
}

function success(pos) {
    from_LaLo_to_Place(pos);
}

function from_LaLo_to_Place(pos) {
    latlng = new google.maps.LatLng(pos.coords.latitude, pos.coords.longitude);
    geocoder.geocode({'latLng': latlng}, function(results, status) {
        placeName = results[0].formatted_address;
        $("#placeName").text(placeName);

        res = {'lat': pos.coords.latitude, 'long': pos.coords.longitude, 'place': placeName};
        $("#lalo").text(JSON.stringify(res) + $.now());

        // sends it back for database handling
        $.getJSON('./_multilocs', res, function(data) {
            $("#result").text(data.result);
        });
    });
}
