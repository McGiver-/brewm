var countdown=null;
var isBrewing = true;
var specs = {};

var countdown=function(timeleft){
    if(timeleft==undefined){

    }else if(timeleft<=0){
        document.getElementById("countdown").innerHtml="Done"
    }else{
        document.getElementById("countdown").innerHtml=timeleft;
        setTimeout(countdown,1000);
        countdown(timeleft - 1);
    }
}
function getBrewing(callback) {
	$.get("/api/status", function(response){
		isBrewing = response.brewing;
        countdown(response.time);
		callback(isBrewing);
	})
}

function postBrewing(state, callback) {
    $.post("/api/brew", JSON.stringify({ "brewing": state }), function(response) {
        isBrewing = response.brewing;
        countdown(response.time);
        callback(isBrewing);
    });
}

function getSpecs(callback) {
    $.get("/api/specs", function(response) {
        specs = response;
        callback(specs);
    });
}

function setStatusText(state) {
    if(state) {
        $("#status").text("Brewing...");
        $("#doit").text("Stop brewing");
    }
    else {
        $("#status").text("Ready");
        $("#doit").text("Brew");
    }
}

$( document ).ready(function() {
    getBrewing(setStatusText);

    getSpecs(function(response){
        $("#cups").text(
                "Number of Cups of Coffee " + response.cups 
                + " Number of mL of fluid Max"+response.ml);
    });

    $("#doit").click(function(){
        postBrewing(!isBrewing, setStatusText);
	});
});
