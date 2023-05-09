function check() {
	var titleval = document.getElementById('editor_title_ta').value;
	titleval = trim(titleval);
	if (titleval.length==0) {
		alert("제목을 꼭 입력해주세요.");
		return false;
	} 
	
	var contentsval = f.contents.value;
	contentsval = trim(contentsval);
	if (contentsval.length==0) {
		alert("작성된 내용이 없습니다.");
		f.contents.focus();
		return false;
	} 	
		f.submit;
}
