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

    let user_result = {
        "1": "",
        "2": "",
        "3": "",
        "4": ""
    }

    $("#nxt").click(function(){
        // let response = {
        //     "id": data.id,
        //     "user": user
        // }
        console.log(data["id"]);
        if (data["id"] === "6"){
            window.location.href = '/quiz/result'; //quiz result
        }else{
            window.location.href = '/quiz/' + data["next"] 
        }
    })

               

    //The buttons for the fingering are made draggable

    $("#finger1").draggable({
        containment: 'document',
        cursor: 'move',
        revert: 'invalid',
        stop:function(){
        $(this).draggable('option','revert','invalid')
        },
        activate: function(){
            $(".table-w-border").css("border-style", "solid")
        }
    })

    
    $("#finger2").draggable({
        containment: 'document',
        cursor: 'move',
        revert: 'invalid',
        stop:function(){
        $(this).draggable('option','revert','invalid')
        }
    })

    $("#finger3").draggable({
        containment: 'document',
        cursor: 'move',
        revert: 'invalid',
        stop:function(){
        $(this).draggable('option','revert','invalid')
        }
    })

    $("#finger4").draggable({
        containment: 'document',
        cursor: 'move',
        revert: 'invalid',
        stop:function(){
        $(this).draggable('option','revert','invalid')
        }
    })

    // Hover -- hovering over the buttons will change the color 
    $("#finger1").hover(function(){
        $(this).css("background-color", "pink");
        }, function(){
        $(this).css("background-color", "yellow");
      });

      $("#finger2").hover(function(){
        $(this).css("background-color", "pink");
        }, function(){
        $(this).css("background-color", "yellow");
      });

      $("#finger3").hover(function(){
        $(this).css("background-color", "pink");
        }, function(){
        $(this).css("background-color", "yellow");
      });

      $("#finger4").hover(function(){
        $(this).css("background-color", "pink");
        }, function(){
        $(this).css("background-color", "yellow");
      });

      $(".table-w-border").droppable({
        drop: function(event, ui){
            console.log(ui.draggable.text())
            console.log(this.id)
            user_result[ui.draggable.text()] = this.id
            $(".table-w-border").removeClass("show-border")
        },

        over: function(){
            $(".table-w-border").addClass("show-border")
        } 
    })


    //where the dots can return to

    $("#dots-group").droppable({
        drop: function(event, ui){
            console.log(ui.draggable.text() + " is put back.")
            $(".table-w-border").removeClass("show-border")
        }
    })


    $("#cfm").click(function(){
        let user = $(this).html()

        let response = {
            "id": data.id,
            "user": user_result
        }
        save_user_response(response)
        
        $(this).attr("disabled", "true")
        $("#nxt").removeAttr("disabled")
    }) 
})

function save_user_response(selection) {
    $.ajax({
        type: "POST",
        url: "save_user_response",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(selection),
        success: function(result){
            quiz_data = result["quiz_results"]
            console.log(quiz_data)

            let url = window.location.href
            let curNum = url.charAt(url.length - 1) - 1
            let fb = $("#quiz_feedback")
            let flag = true
            let right = quiz_data[curNum]['correct']
            let answer = quiz_data[curNum]['user']
            for(let k in right){
                if(right[k] !== answer[k]){
                    flag = false
                    break
                }
            }
            if(flag){
                fb.text("Correct. Good job!")
                fb.addClass("correct")
            } else {
                let s = ""
                for(let k in right){
                    if(right[k] !== ""){
                        s = s + "dot " + k + " should be put at the " + right[k] + "th grid,"
                    }
                    
                }
                fb.text("Oho, the correct answer is " + s)
                fb.addClass("wrong")
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
