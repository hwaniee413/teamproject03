/////////////////////더보기 버튼눌러서 영상 추가로 로딩하기/////////////////////
document.addEventListener("DOMContentLoaded", function(){
  const button = document.getElementById("load"); // id=load인 버튼
  const videos = document.querySelectorAll(".video"); // 등록된 영상을 모두 읽음
  
  let videoindex = 0; // 화면에 보이는 영상갯수를 변수로
  for(let i=0; i<12; i++){
    if(videoindex < videos.length){ // 전체 영상갯수가 화면에 보이는 수보다 많을때
      videos[videoindex].style.display = "inline-block"; // hide 속성을 inline-block으로 변경
      videoindex++;
    }else{
      button.style.display = "none"; // 더이상 로드할 영상이 없을경우 버튼을 none으로 세팅
      break;
    }
  }

button.addEventListener("click", function(){ //버튼 이벤트
    for(let i=0; i<3; i++){ //버튼 한번 누를때 영상 가져오기를 3번까지 실행 
      if(videoindex < videos.length){
        videos[videoindex].style.display = "inline-block";
        videoindex++;
      }else{
        button.style.display = "none";
        break;
      }
    }
  });
});

/////////////////////영상에 커서를 올렸을때 미리보기 자동 재생 (가능할까...?)//////////////////////
