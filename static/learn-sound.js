$(document).ready(function(){
    $("#page-title").text("Sound Learning")
    $("#nav-learn").addClass("active")

    //goes to correct lerning page -- based on data id from learnData
    $(".prev").click(function(){
        window.location.href = '/learn/' + data.id
    })

    //next -- 
    $(".next").click(function(){
        if (data.id ===3){ //reaches the end of what we have to teach, goes to quiz
            console.log("correct");
            window.location.href = '/quiz/1'; //hard coded :\
        }else{
            window.location.href = '/learn/' + data.next //go to the next data to learn
        }
    })
})