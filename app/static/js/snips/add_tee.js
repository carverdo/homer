/* Simple Simple */

// var cur_tees = [];

$(document).ready(function(){
    // some pretty boxes
    $('input, email').focus(function(){
        $(this).css("background-color", "#cccccc");
    });
    // $("#add_tee").click(function(){
    $('input, email').blur(function(){
        $(this).css("background-color", "#ffffff");
    });
    $('input, email').keyup(function() {
        var cur_text = $(this)[0].value;
        // if we like the text, pass it and clear the box
        if ($(this)[0].validationMessage == "" && $(this)[0].value.slice(-3, cur_text.length) == 'com') {
            delay(function() {
                $.getJSON("./_add_tee", $("form").serialize(), function(data, status) {
                    /* add raw text
                    cur_tees.push(data.result[0]);
                    $("#result").text(cur_tees); */
                    // add new ele
                    el = addEmailEle(data.result[0]);
                    // append, then clear the input box
                    $("#ems_cont").append(el);
                    $('input, email').val('');
                });
            }
            , 1200);
        };
    });
})

// FUNCTIONS
function addEmailEle(text) {
    el = $('<button>');
    el.attr('class', 'myButton');
    el.text(text);
    el.click(function(e) {
        $(e.target).remove();
    });
    return el;
};
// creates a delay function which we can drop into a keyup event
var delay = (function(){
    var timer = 0;
    return function(callback, ms){
        clearTimeout (timer);
        timer = setTimeout(callback, ms);
    };
})();
