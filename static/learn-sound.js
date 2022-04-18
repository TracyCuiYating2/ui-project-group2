$(document).ready(function(){
    $("#page-title").text("Sound Learning")
    $("#nav-learn").addClass("active")

    $("#nxt").click(function(){
        window.location.href = '/quiz/1'
    })
    $("#prev").click(function(){
        window.location.href = '/learn/1'
    })
})