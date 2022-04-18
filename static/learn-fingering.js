$(document).ready(function(){
    $("#page-title").text("Fingering Learning")
    $("#nav-learn").addClass("active")

    $(".prev").click(function(){
        window.location.href = '/learn/' + data.prev
    })

    $(".next").click(function(){
        window.location.href = '/learn/' + data.id + '/sound'
    })
})