$(document).ready(function(){
    $("#page-title").text("Sound Learning")
    $("#nav-basic").addClass("active")

    $("#nxt").click(function(){
        window.location.href = '/learn/1'
    })
    $("#prev").click(function(){
        window.location.href = '/learn/basic'
    })
})