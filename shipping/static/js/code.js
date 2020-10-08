

function currentTime() {
    var date = new Date(); /* creating object of Date class */
    var hour = date.getHours();
    var min = date.getMinutes();
    var sec = date.getSeconds();
    hour = updateTime(hour);
    min = updateTime(min);
    sec = updateTime(sec);

    var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    var d = days[date.getDay()];
    var x = date.getDate();
    var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"];
    var m = months[date.getMonth()];
    var y = date.getFullYear() ;

    
    document.getElementById("date").innerHTML = d + " " + m + " " + x + ", " + y;
    document.getElementById("clock").innerText = hour + " : " + min + " : " + sec; /* adding time to the div */
      var t = setTimeout(function(){ currentTime(); }, 1000); /* setting timer */
  }
  
  function updateTime(k) {
    if (k < 10) {
      return "0" + k;
    }
    else {
      return k;
    }
  }
  
  currentTime(); /* calling currentTime() function to initiate the process */