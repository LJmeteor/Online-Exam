import{loadExam , dbRef} from './connect.js';
import { getDatabase, ref, child, get,set  } from "https://www.gstatic.com/firebasejs/9.8.2/firebase-database.js";

$(function(){
    queryExams();
    $("#create_subject").click(function () {
        $("#createSubjectModal").modal("show");
    });
    $("#saveCreateSubjectBtn").click(function(){
        const subjectName=$("#subjectName").val();
        const subKey=subjectName;
        const db = getDatabase();
        console.log(ref(db,"examList"));
        console.log(subjectName);
        set(ref(db, "examList/"+subKey), {
          subjectName:subjectName
        });
        $("#createSubjectModal").modal("hide");
        queryExams();
    });

});

function queryExams(){
    get(child(dbRef, `examList`)).then((snapshot) => {
        if (snapshot.exists()) {
           var exams= snapshot.val();
           console.log(exams);
        var htmlString="";
        $.each(exams, function (index, obj) {
            console.log(obj.subjectName)
         htmlString += "<div class='col-xs-12 col-sm-4'>";
         htmlString += "<div class='card'>";
         htmlString +="<a class='img-card' href='index.html'>";
         htmlString +="<img src='{% static 'image/nguyen-dang-hoang-nhu-Wp3sgCHoawg-unsplash.jpg' %}' />";
         htmlString +="</a>";
         htmlString +="<div class='card-content'>";
         htmlString +="<h4 class='card-title'>"
         htmlString +="<a href='http://www.fostrap.com/2016/03/bootstrap-3-carousel-fade-effect.html'>"+ obj.subjectName;
         htmlString +="</a>";
         htmlString +="</h4>";
         // htmlString +="<p class=''>";
         // htmlString +=obj +" exam description";
         // htmlString +="</p>";
         htmlString +=" </div>";
         htmlString +="</div>";
         htmlString +="</div>";
     $("#examsList").html(htmlString);
 });
        } else {
          console.log("No data available");
        }
      }).catch((error) => {
        console.error(error);
      });
     
}
