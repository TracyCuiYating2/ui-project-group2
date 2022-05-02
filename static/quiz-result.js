$(document).ready(function(){
    let correct_list = []
    let correct_number = 0
    
    $.each(data, function (i, datum) {
        console.log(data[i].user);
        console.log(data[i].correct);

        if(data[i].user === data[i].correct){
            correct_list.push(data[i].id);
            correct_number += 1;
            $("#correct_message").text("You got " + correct_number + "/6 questions right!");
            console.log(correct_list);
        } 
    });
    console.log("total "+correct_number);


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