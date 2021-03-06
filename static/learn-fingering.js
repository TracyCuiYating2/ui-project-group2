
$(document).ready(function(){
    $("#page-title").text("Fingering Learning")
    $("#nav-learn").addClass("active")

    $("#prev").click(function(){
        if (data.prev===""){
            window.location.href = '/learn/basic-contd';
        }else{
            window.location.href = '/learn/' + data.prev
        }
    })

    $("#next").click(function(){
        if (data.next===""){
            window.location.href = '/learn/check';
        }else{
            window.location.href = '/learn/' + data.next
        }
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
    
    for (let i = 1; i <= 5; i++) {
       if (parseInt(data.id) == i) {
            $("#learn" + i).css("background-color", "#e0e0e0");
        }
    }
})
