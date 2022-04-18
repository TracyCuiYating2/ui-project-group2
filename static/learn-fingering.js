$(document).ready(function(){
    $("#page-title").text("Fingering Learning")
    $("#nav-learn").addClass("active")

    $("#nxt").click(function(){
        window.location.href = '/learn/2'
    })
    $("#prev").click(function(){
        window.location.href = '/learn/basic-contd'
    })
})