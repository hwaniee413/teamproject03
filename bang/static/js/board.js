$(document).ready(function(){
	$("select[name=selc_category]").change(function () {
		$("#searchSelect").submit();
	});

});


function check() {
	var search_kw = document.getElementById('search_kw').value;
	alert(search_kw);
	if (search_kw.length == 0) {
		alert("검색어를 입력해주세요");
		return false;
	} else {
		input = checkByteLen(search_kw, 20)
		if (!input){
			alert("검색어가 너무 길어요");
		}
		return false;
	}
}
function checkByteLen(str, size){
	var byteLen = getByteLen(str);
	if(byteLen <= size){
		return true;
	}else{
		return false;
	}
}
function getByteLen(str){
   return str.replace(/[\0-\x7f]|([0-\u07ff]|(.))/g,"$&$1$2").length;
}

function enterCheck(elm) {
	if(event.keyCode==13) {
		var input = document.getElementById('search_kw')
		if (elm = input){
			check();
		}
	}
}
