$(document).ready(function(){
    $("#page-title").text("Fingering Learning")
    $("#nav-learn").addClass("active")

    //next learning page?
    $("#nxt").click(function(){
        window.location.href = '/learn/' + data.id + '/sound'
    })
    $("#prev").click(function(){
        window.location.href = '/learn/' + data.prev
    })

    // let id = pageID
    // let chordID = learnData.id

    // if(chordID = id)
    // {
    //     let chordDisplay =$("<div class='chords'> ")
    //     chordDisplay.append("<div class='chordImage'>" + learnData.chordIMG + " </div>")
    //     chordDisplay.append("<div class='chordInfo'>  Here is the " + learnData.chord + " C chord, your fingers should pressing the yellow dots on the strings. </div>")

    // }

    // $("#chordLearning").append(chordDisplay)

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
    
})

