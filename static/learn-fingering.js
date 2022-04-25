$(document).ready(function(){
    $("#page-title").text("Fingering Learning")
    $("#nav-learn").addClass("active")

    $("#prev").click(function(){
        window.location.href = '/learn/' + data.prev
    })

    // Clear previous fingerings first
    for (let i = 1; i < 17; i++){
        $("#" + String(i)).empty()
    }

    let cells = data["fingerings"]
    for(let fingering in cells){
        console.log(fingering, cells[fingering])
        let newFing = $("<div>"+fingering+"</div>")
        newFing.addClass("circle")
        $("#" + cells[fingering]).append(newFing)
    }
    
    $(".next").click(function(){
        if (data.id ===3){
            console.log("correct");
            window.location.href = '/quiz/1';
        }else{
            window.location.href = '/learn/' + data.next
        }
    })
})
