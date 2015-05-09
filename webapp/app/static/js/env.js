var countdown=null;
var isBrewing = true;
function updateBrewing(callback){
	$.get("/api/status",function(response){
		isBrewing = response.brewing;
		callback(isBrewing);
	})
}

$( document ).ready(function() {
    
    updateBrewing(function(isBrewing){
   	 	$("amount").text("Are we brewing"+response.brewing);
    });
   
    var countdownDom = document.getElementById("countdown");
   
    $("#doit").click(function(){
    	$.post("/api/brew", {"brewing":true},function(response){
        $("#status").text("Brewing...");
   		});
	});

    $("#doit").click(function(){
   	 	$.get("/api/specs", function(response){
       		$("#cups").text("Number of Cups of Coffee"+reponse.cups+"Number of mL of fluid Max"+reponse.ml);
   	 	});
	});
    
    $("#doit").click(function(){
   		$.get("/api/status", function(response){
        	$("#amount").text("Are we brewing"+response.brewing);
   	 	});
	});
});
