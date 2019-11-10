$(document).ready(function() {
    $.getJSON("/data", function(json) {
        document.getElementById("button1").value = json["button1"];
        document.getElementById("button2").value = json["button2"];
        document.getElementById("button3").value = json["button3"];
        document.getElementById("button4").value = json["button4"];
        document.getElementById("button5").value = json["button5"];
        document.getElementById("button6").value = json["button6"];
        document.getElementById("button7").value = json["button7"];
        document.getElementById("button8").value = json["button8"];
        document.getElementById("button9").value = json["button9"];
    });
});

$(function () {
    $("#button1").click(function (_) {
        $.get("/button1", {},
            function (data) {
            });
        return false;
    });
});
$(function() {
    $("#button2").click(function(_) {
        $.get("/button2", {},
            function(data) {});
        return false;
    });
});
$(function() {
    $("#button3").click(function(_) {
        $.get("/button3", {},
            function(data) {});
        return false;
    });
});
$(function() {
    $("#button4").click(function(_) {
        $.get("/button4", {},
            function(data) {});
        return false;
    });
});
$(function() {
    $("#button5").click(function(_) {
        $.get("/button5", {},
            function(data) {});
        return false;
    });
});
$(function() {
    $("#button6").click(function(_) {
        $.get("/button6", {},
            function(data) {});
        return false;
    });
});
$(function() {
    $("#button7").click(function(_) {
        $.get("/button7", {},
            function(data) {});
        return false;
    });
});
$(function() {
    $("#button8").click(function(_) {
        $.get("/button8", {},
            function(data) {});
        return false;
    })
});
$(function() {
    $("#button9").click(function(_) {
        $.get("/button9", {},
            function(data) {});
        return false;
    });
});
