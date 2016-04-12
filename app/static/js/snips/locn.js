// Defines Function and Calls (producing return)
// ============================================================
var crd;
var geocoder;
var latlngStr = '', lat = 0.0, lng = 0.0;
var latlng;
var placeName='';

var id, target = {};
var options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
};


$(document).ready(function() {
    target = {
        'latitude': $("#targLat").text(),
        'longitude': $("#targLong").text()
    };
    geocoder = new google.maps.Geocoder();
    // setInterval("getLocation()", 5000);
    getLocation();
});


function getLocation() {
    if (navigator.geolocation) {
        // navigator.geolocation.getCurrentPosition(success, error, options);
        id = navigator.geolocation.watchPosition(success, error, options);
    } else {
        $("#lalo").text('Geolocation switched off or not supported.');
    }
}
function success(pos) {
    var crd = pos.coords;
    $("#accuracy").text(crd.accuracy + ' m');
    // are we there yet?
    // parseInt is ROUGH!
    if (parseInt(target.latitude) === parseInt(crd.latitude) &&
            parseInt(target.longitude) === parseInt(crd.longitude)) {
        console.log('Congratulations, you reached the target');
        navigator.geolocation.clearWatch(id);
    }
    // adding layers of data
    latlng = new google.maps.LatLng(crd.latitude, crd.longitude);
    geocoder.geocode({'latLng': latlng}, function(results, status) {
        placeName = results[0].formatted_address;
        $("#placeName").text(placeName);

        res = {'lat': crd.latitude, 'long': crd.longitude, 'place': placeName,
            'target': target
        };
        // $("#lalo").text(JSON.stringify(res) + $.now());

        // sends it back for database handling
        $.getJSON('./_multilocs', res, function(data) {
            $("#result").text(data.dists + ' km');
        });
    });
}
function error(err) {
    console.warn('ERROR(' + err.code + '): ' + err.message);
    /*
    switch(err.code) {
        case err.PERMISSION_DENIED:
            console.log("permission denied");
            break;
        case err.POSITION_UNAVAILABLE:
            console.log("Location information is unavailable.");
            break;
        case err.TIMEOUT:
            console.log("The request to get user location timed out.");
            break;
        case err.UNKNOWN_ERROR:
            console.log("An unknown error occurred.");
            break;
    }
    */
}
/*
function from_LaLo_to_Place(pos) {
    var crd = pos.coords;
    console.log('More or less ' + crd.accuracy + ' meters.');
    latlng = new google.maps.LatLng(crd.latitude, crd.longitude);
    geocoder.geocode({'latLng': latlng}, function(results, status) {
        placeName = results[0].formatted_address;
        $("#placeName").text(placeName);

        res = {'lat': crd.latitude, 'long': crd.longitude, 'place': placeName};
        $("#lalo").text(JSON.stringify(res) + $.now());

        // sends it back for database handling
        $.getJSON('./_multilocs', res, function(data) {
            $("#result").text(data.result);
        });
    });
}
*/