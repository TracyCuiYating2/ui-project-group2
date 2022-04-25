$(document).ready(function(){
    $("#page-title").text("Sound Learning")
    $("#nav-basic").addClass("active")

    //for basic continued page --> then moves into learning section
    $("#nxt").click(function(){
        window.location.href = '/learn/1'
    })
    //returns to original basic page
    $("#prev").click(function(){
        window.location.href = '/learn/basic'
    })
})