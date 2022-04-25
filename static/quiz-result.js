$(document).ready(function(){
    
    if (data[0].user != data[0].correct) {
        let container = $("<div class='review'>")
        let header = $("<a>").html("C Chord")
        $(header).attr("href", "http://127.0.0.1:5000/learn/3")

        $(container).append(header)
        $("#result").append(container)
    }
    if (data[1].user != data[1].correct) {
        let container = $("<div class='review'>")
        let header = $("<a>").html("G Chord")
        $(header).attr("href", "http://127.0.0.1:5000/learn/1")

        $(container).append(header)
        $("#result").append(container)
    }
    if (data[2].user != data[2].correct) {
        let container = $("<div class='review'>")
        let header = $("<a>").html("F Chord")
        $(header).attr("href", "http://127.0.0.1:5000/learn/2")

        $(container).append(header)
        $("#result").append(container)
    }
})