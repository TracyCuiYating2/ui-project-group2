$(document).ready(function(){
    $("#page-title").text("Fingering Learning")
    $("#nav-learn").addClass("active")

    $("#prev").click(function(){
        window.location.href = '/learn/1';
        }
    })

    $("#next").click(function(){
        window.location.href = '/learn/check';
    })


})
