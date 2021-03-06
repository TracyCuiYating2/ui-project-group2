function displayPage(data){
    let pic = $("<img id='quiz-image'>");
    $(pic).attr("src", data["image"][0]);
    $(pic).attr("alt", "quiz"+ data["id"] + " image");
    $("#quiz-image").append(pic);

    $.each(data["audio"], function (i, datum) {
        // console.log("hello");
        // // <button onclick="playSound()">Play</button>
        // let audio = new Audio(datum);
        let item = $("<div id='audio-option'>");
        let button = $("<button class='btn btn-primary option vertical' type='button'>");
        button.text(String.fromCharCode(i+65));
        button.attr('id', i)


        let audio = $("<audio id='quiz-audio' controls>");
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
    })
    
    $(".option").click(function(){
        let user = $(this).html()

        let response = {
            "id": data.id,
            "user": user
        }

        save_user_response(response)
        $("#nxt").removeAttr("disabled")
    })
}

function save_user_response(selection, seleID) {
    $.ajax({
        type: "POST",
        url: "save_user_response",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(selection),
        success: function(result){
            quiz_data = result["quiz_data"]
            
            console.log(quiz_data)
            
            let url = window.location.href
            let curNum = url.charAt(url.length - 1) - 1

            // console.log(seleID, quiz_data[curNum]['correct'])

            let fb = $("#quiz_feedback")
            if(quiz_data[curNum]['user'] === quiz_data[curNum]['correct']){
                fb.text("Correct. Good job!")
                fb.addClass("correct")
            } else {
                fb.text("Oho, the correct answer is " + quiz_data[curNum]['correct'])
                fb.addClass("wrong")
            }

            for(let i = 0; i < 3; i++){
                $("#" + String(i)).attr('disabled', true)
            }
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

$(document).ready(function(){
    displayPage(data)  

    $("#nxt").click(function(){
        window.location.href = '/quiz/' + data["next"]
    })
    $("#prev").click(function(){
        console.log("Should get feedbacks from server.")
        // if (data["id"] === "1"){
        //     window.location.href = '/learn/3';
        // }else{
        //     window.location.href = '/quiz/' + data["previous"]
        // }

    })   

})