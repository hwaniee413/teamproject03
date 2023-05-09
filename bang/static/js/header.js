var slideIndex = 0;
window.onload =function(){	
	showSlides();
}
function showSlides() {
	var i;
	var slides = document.getElementsByClassName("slides");
	for (i = 0; i < slides.length; i++) {
		slides[i].style.display='none';	 
		//slides[i].style.transition='2s';
		//slides[i].style.left="640px";
				 
	} 
	slideIndex++;
	if (slideIndex > slides.length) {slideIndex = 1}
		//alert(slideIndex)
	//slides[slideIndex-1].style.transition='0.5s';	
	//slides[slideIndex-1].style.left="0px";
	slides[slideIndex-1].style.display='flex';	
	setTimeout(showSlides, 3000); // Change image every 3 seconds

}

