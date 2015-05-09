var countdown=null;
$( document ).ready(function() {
    var countdownDom = document.getElementById("countdown");

	$("#doit").click(function() {
		var currentNum =document.getElementById("time").value;

		function innerCountdown() {
			if(currentNum!=-1){
				countdownDom.innerHTML=currentNum;
				currentNum--;
				setTimeout(innerCountdown,1000);
			}
			return false;
		}

		innerCountdown();
		return false;
	});
});
