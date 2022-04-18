$(document).ready(function(){
    $("#page-title").text("Sound Learning")
    $("#nav-learn").addClass("active")

    $(".prev").click(function(){
        window.location.href = '/learn/' + data.id
    })

    $(".next").click(function(){
        window.location.href = '/learn/' + data.next
    })
})