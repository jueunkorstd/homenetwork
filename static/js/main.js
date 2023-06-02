function setClock() {
  var dateInfo = new Date();
  var hour = modifyNumber(dateInfo.getHours());
  var min = modifyNumber(dateInfo.getMinutes());
  var sec = modifyNumber(dateInfo.getSeconds());
  var year = dateInfo.getFullYear();
  var month = dateInfo.getMonth() + 1; //monthIndex를 반환해주기 때문에 1을 더해준다.
  var date = dateInfo.getDate();
  document.getElementById("nowtime").innerHTML = hour + ":" + min + ":" + sec;
  document.getElementById("nowdate").innerHTML = year + "년 " + month + "월 " + date + "일";
}
function modifyNumber(time) {
  if (parseInt(time) < 10) {
    return "0" + time;
  }
  else
    return time;
}
window.onload = function () {
  setClock();
  setInterval(setClock, 1000);
}


// // 모달 창 열기
// function openModal() {
//   var modal = document.getElementById("myModal");
//   modal.style.display = "block";
// }

// // 모달 창 닫기
// function closeModal() {
//   var modal = document.getElementById("myModal");
//   modal.style.display = "none";
// }

// 알람 설정
// function setAlarm() {
//   var time = document.getElementById("time").value;
//   alert("알람이 " + time + "에 설정되었습니다!");
//   closeModal();
// }

