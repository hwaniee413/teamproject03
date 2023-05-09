$(function(){	
	//document.getElementById('moreBt').click();
	showUnits();
});

var show_unit= 20;

function showUnits() {
	var champ= document.getElementsByClassName('champion_container');
	var container = document.getElementsByClassName('champion-list-wrapper');
	var moreBt = document.getElementsByClassName('controll_more');		
	if(show_unit <=champ.length) {
		container[0].style.setProperty('display', 'block');
		container[0].style.setProperty('overflow', 'hidden');
		for (var i=0; i<show_unit; i++){
			champ[i].style.setProperty('display','block');
			if (show_unit==160){
				champ[i+1].style.setProperty('display','block');
				champ[i+2].style.setProperty('display','block');
				moreBt[0].style.setProperty('display','none');
			}
		}
		show_unit *=2
	} 
}

function sortbyrole1() {
	var show_unit= 20;
	var rolename_x = document.getElementById("rolename1").value;
	var rolename_y = document.getElementsByClassName("card_content-role");	
	var container = document.getElementsByClassName('champion-list-wrapper');
	var moreBt = document.getElementsByClassName('controll_more');	
	var champ= document.getElementsByClassName('champion_container');

	for(var i=0; i<champ.length; i++){
		champ[i].style.setProperty('display','none');
	}
	if(show_unit <=champ.length) {
		container[0].style.setProperty('display', 'block');
		container[0].style.setProperty('overflow', 'hidden');
		for (var i=0; i<champ.length; i++){
			role = rolename_y[i].innerText.substring(3,6).trim();	
			if (rolename_x == role ) {
				champ[i].style.setProperty('display','block');
			} else {
				champ[i].style.setProperty('display','none');	
			}
		}
		show_unit *=2
		moreBt[0].style.setProperty('display','none');
	} 
}

function sortbyrole2() {
	var show_unit = 20;	
	var rolename_x = document.getElementById("rolename2").value;
	var rolename_y = document.getElementsByClassName("card_content-role");	
	var container = document.getElementsByClassName('champion-list-wrapper');
	var moreBt = document.getElementsByClassName('controll_more');	
	var champ= document.getElementsByClassName('champion_container');

	for(var i=0; i<champ.length; i++){
		champ[i].style.setProperty('display','none');
	}
	if(show_unit <=champ.length) {
		container[0].style.setProperty('display', 'block');
		container[0].style.setProperty('overflow', 'hidden');
		for (var i=0; i< champ.length; i++){
			role = rolename_y[i].innerText.substring(3,5).trim();	
			if (rolename_x == role ) {
				champ[i].style.setProperty('display','block');
				
			} else {
				champ[i].style.setProperty('display','none');	
			}
		}
		show_unit *=2
		moreBt[0].style.setProperty('display','none');
	} 
}
function sortbyrole3() {
	var show_unit= 20;
	var rolename_x = document.getElementById("rolename3").value;
	var rolename_y = document.getElementsByClassName("card_content-role");	
	var container = document.getElementsByClassName('champion-list-wrapper');
	var moreBt = document.getElementsByClassName('controll_more');	
	var champ= document.getElementsByClassName('champion_container');
	for(var i=0; i<champ.length; i++){
		champ[i].style.setProperty('display','none');
	}
	if(show_unit <=champ.length) {
		container[0].style.setProperty('display', 'block');
		container[0].style.setProperty('overflow', 'hidden');
		for (var i=0; i<champ.length; i++){
			role = rolename_y[i].innerText.substring(3,6).trim();	
			if (rolename_x == role ) {
				champ[i].style.setProperty('display','block');	
			} else {
				champ[i].style.setProperty('display','none');	
			}
		}				
		show_unit *=2
		moreBt[0].style.setProperty('display','none');
	} 
}
function sortbyrole4() {
	var show_unit= 20;
	var rolename_x = document.getElementById("rolename4").value;
	var rolename_y = document.getElementsByClassName("card_content-role");	
	var container = document.getElementsByClassName('champion-list-wrapper');
	var moreBt = document.getElementsByClassName('controll_more');	
	var champ= document.getElementsByClassName('champion_container');
	for(var i=0; i<champ.length; i++){
		champ[i].style.setProperty('display','none');
	}
	if(show_unit <=champ.length) {
		container[0].style.setProperty('display', 'block');
		container[0].style.setProperty('overflow', 'hidden');
		for (var i=0; i<champ.length; i++){
			role = rolename_y[i].innerText.substring(3,6).trim();	
			if (rolename_x == role ) {
				champ[i].style.setProperty('display','block');	
			} else {
				champ[i].style.setProperty('display','none');	
			}
		}				
		show_unit *=2
		moreBt[0].style.setProperty('display','none');
	} 
}
function sortbyrole5() {
	var show_unit= 20;
	var rolename_x = document.getElementById("rolename5").value;
	var rolename_y = document.getElementsByClassName("card_content-role");	
	var container = document.getElementsByClassName('champion-list-wrapper');
	var moreBt = document.getElementsByClassName('controll_more');	
	var champ= document.getElementsByClassName('champion_container');
	for(var i=0; i<champ.length; i++){
		champ[i].style.setProperty('display','none');
	}
	if(show_unit <=champ.length) {
		container[0].style.setProperty('display', 'block');
		container[0].style.setProperty('overflow', 'hidden');
		for (var i=0; i<champ.length; i++){
			role = rolename_y[i].innerText.substring(3,6).trim();	
			if (rolename_x == role ) {
				champ[i].style.setProperty('display','block');	
			} else {
				champ[i].style.setProperty('display','none');	
			}
		}				
		show_unit *=2
		moreBt[0].style.setProperty('display','none');
	} 
}
function sortbyrole6() {
	var show_unit= 20;
	var rolename_x = document.getElementById("rolename6").value;
	var rolename_y = document.getElementsByClassName("card_content-role");	
	var container = document.getElementsByClassName('champion-list-wrapper');
	var moreBt = document.getElementsByClassName('controll_more');	
	var champ= document.getElementsByClassName('champion_container');
	for(var i=0; i<champ.length; i++){
		champ[i].style.setProperty('display','none');
	}
	if(show_unit <=champ.length) {
		container[0].style.setProperty('display', 'block');
		container[0].style.setProperty('overflow', 'hidden');
		for (var i=0; i<champ.length; i++){
			role = rolename_y[i].innerText.substring(3,6).trim();	
			if (rolename_x == role ) {
				champ[i].style.setProperty('display','block');	
			} else {
				champ[i].style.setProperty('display','none');	
			}
		}				
		show_unit *=2
		moreBt[0].style.setProperty('display','none');
	} 
}