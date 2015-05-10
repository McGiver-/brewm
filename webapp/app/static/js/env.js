var countdown=null;
var isBrewing = true;
var specs = {};
var timeout = null;

var countdown=function(timeleft){
    console.log("countdown ", timeleft);
    if(!timeleft || timeleft < 0) {
        if(timeout != null) {
            console.log(timeout);
            clearTimeout(timeout);
        }
        console.log('done');
        $("#countdown").text("Done");
    } else {
        console.log('not done');
        $("#countdown").text(timeleft.toString());
        timeout = setTimeout(function() { countdown(timeleft - 1); }, 1000);
    }
}

function getBrewing(callback) {
	$.get("/api/status", function(response){
        console.log('status');
		isBrewing = response.brewing;
        countdown(response.time);
		callback(isBrewing);
	})
}

function postBrewing(state, callback) {
    console.log('post');
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
        console.log('lol');
        postBrewing(!isBrewing, setStatusText);
	});
});
