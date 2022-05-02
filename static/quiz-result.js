$(document).ready(function(){
    $.each(data["review"], function (i, datum) {
        console.log(datum);
        let container = $("<div class='review'>")
        let header = $("<a>").html(datum[1] + " Chord");
        $(header).attr("href", "http://127.0.0.1:5000/learn/" + datum[0])
        $(container).append(header)
        $("#result").append(container)
    })
})