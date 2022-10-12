
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.8.2/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.8.2/firebase-analytics.js";
  import { getDatabase, ref, child, get,set  } from "https://www.gstatic.com/firebasejs/9.8.2/firebase-database.js";
  import { getAuth } from "https://www.gstatic.com/firebasejs/9.8.2/firebase-auth.js";

  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyBiuYp3aVk7LmHV0wISACEBMKCvrWSYWeA",
    authDomain: "aly6080-nlp.firebaseapp.com",
    projectId: "aly6080-nlp",
    storageBucket: "aly6080-nlp.appspot.com",
    messagingSenderId: "723702609158",
    appId: "1:723702609158:web:3b25a97d4c7ddc11219a87",
    measurementId: "G-WFDSQG1FDC"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
  const database = getDatabase(app);
  const auth = getAuth();
  export const dbRef = ref(getDatabase());
  
  function loadExam(){
    get(child(dbRef, `examList`)).then((snapshot) => {
      if (snapshot.exists()) {
         snapshot.val();
      } else {
        console.log("No data available");
      }
    }).catch((error) => {
      console.error(error);
    });
  }
  export{loadExam}
