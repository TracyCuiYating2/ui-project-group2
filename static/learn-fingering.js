$(document).ready(function(){
    $("#page-title").text("Fingering Learning")
    $("#nav-learn").addClass("active")

    $(".prev").click(function(){
        window.location.href = '/learn/' + data.prev
    })

    $(".next").click(function(){
        if (data.id ===3){
            console.log("correct");
            window.location.href = '/quiz/1';
        }else{
            window.location.href = '/learn/' + data.next
        }
    })
})