function displayPage(data){
    let pic = $("<img class='quiz-image'>");
    $(pic).attr("src", data["image"][0]);
    $(pic).attr("alt", "quiz"+ data["id"] + " image");
    $("#quiz-image").append(pic);

    $.each(data["audio"], function (i, datum) {
        // console.log("hello");
        // // <button onclick="playSound()">Play</button>
        // let audio = new Audio(datum);
        let item = $("<div>");
        let button = $("<button>");
        button.text(i);

        let audio = $("<audio controls>");
        // let playSound = () => new Audio(datum).play();
        let source = $("<source type='audio/mpeg' preload='auto'> ")
        $(source).attr("src", datum); 
        let embed = $("<embed height='50' width='100'>");
        $(embed).attr("src", datum);
        let object = $("<object height='50' width='100' data='horse.mp3'></object>")
        $(item).append(button); 
        $(audio).append(source);
        $(audio).append(embed);
        $(audio).append(object);
        $(item).append(audio);

        $("#quiz-content").append(item);
      });
    }
$(document).ready(function(){
    //when the page loads, display all the names
    displayPage(data)  
    // $("#edit-button").click(function(){
    //     console.log("id:" + data["id"]);
    //     window.location.href = "/edit/" + data["id"];
    // })   
    
    $("#nxt").click(function(){
        if (data["id"] === "3"){
            console.log("here");
            window.location.href = '/quiz/result';
        }else{
            console.log("wrong");
            window.location.href = '/quiz/' + data["next"] + '/fingering'
        }
    })
    $("#prev").click(function(){
        if (data["id"] === "1"){
            window.location.href = '/quiz/3';
        }else{
            window.location.href = '/quiz/' + data["previous"] +'/fingering'
        }
    })            

})