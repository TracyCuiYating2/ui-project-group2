$(document).ready(function(){
    $("#page-title").text("Fingering Learning")
    $("#nav-learn").addClass("active")

    //next learning page?
    $("#nxt").click(function(){
        window.location.href = '/learn/2'
    })
    $("#prev").click(function(){
        window.location.href = '/learn/basic-contd'
    })

    let id = pageID
    let chordID = learnData.id

    if(chordID = id)
    {
        let chordDisplay =$("<div class='chords'> ")
        chordDisplay.append("<div class='chordImage'>" + learnData.chordIMG + " </div>")
        chordDisplay.append("<div class='chordInfo'>  Here is the " + learnData.chord + " C chord, your fingers should pressing the yellow dots on the strings. </div>")

    }

    $("#chordLearning").append(chordDisplay)
    
    
})

