// Login page validation
$(document).ready(function(){
    $("#logsubmit").click(function(){
      if ($("#id_username").val()==""){
        alert("Enter Username")
        return false;
     }
    
     if ($("#id_password").val()==""){
        alert("Enter Password")
        return false;
     }
    })
})

// Add staff page validation
$(document).ready(function(){
   $("#sub").click(function(){
      
      if($("#id_name").val()==""){
         alert("Enter Username")
         return false;
      }
      if($("#id_email").val()==""){
         alert("Enter Email")
         return false;
      }
      if(!$("#id_email").val().match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')){
         alert("Enter Email")
         return false;
      }
      if($("#id_password").val()==""){
         alert("Enter Password")
         return false;
      }
      if($("#id_contact").val()==""){
         alert("Enter Contact")
         return false;
      }
      if ($("#id_contact").val().length != 10) {
         alert("Contact length should be equal to 10 Digits");
         return false;
     }
      if($("#id_address").val()==""){
         alert("Enter Address")
         return false;
      }
      if($("#id_gender").val()==""){
         alert("Select Gender")
         return false;
      }
      if($("#id_experience").val()==""){
         alert("Enter Experince")
         return false;
      }
      if($("#id_qualification").val()==""){
         alert("Enter Qualification")
         return false;
      }
      if($("#id_department").val()==""){
         alert("Enter Department")
         return false;
      }
   })
})

// Add student page validation

$(document).ready(function(){
   $("#sub1").click(function(){
      
      if($("#id_name").val()==""){
         alert("Enter Username")
         return false;
      }
      if($("#id_email").val()==""){
         alert("Enter Email")
         return false;
      }
      if(!$("#id_email").val().match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')){
         alert("Enter Email Format")
         return false;
      }
      if($("#id_password").val()==""){
         alert("Enter Password")
         return false;
      }
      
      if($("#id_gender").val()==""){
         alert("Select Gender")
         return false;
      }
      if($("#id_department").val()==""){
         alert("Enter Department")
         return false;
      }
      if($("#id_dob").val()==""){
         alert("Enter Date of Birth")
         return false;
      }
      var dob = new Date($("#id_dob").val());

      if (isNaN(dob) || dob > new Date()) {
      alert("Enter a valid date of birth");
      return false;
      }

      {
      if($("#id_address").val()==""){
         alert("Enter Address")
         return false;
      }  
      if($("#id_contact").val()==""){
         alert("Enter Contact")
         return false;
      }
      }
   })
})

// Add admin notification page validation
var date    = new Date(),
yr      = date.getFullYear(),
month   = date.getMonth(),
day     = date.getDate(),
newDate = yr + '-' + month + '-' + day;

$(document).ready(function(){
   $("#subnot").click(function(){
      
     if ($("#id_title").val()==""){
       alert("Enter Title")
       return false;
    }
    if ($("#id_description").val()==""){
       alert("Enter Description")
       return false;
    }
   //  if ($("#id_start_date").val()==""){
   //     alert("Select Start Date")
   //     return false;
   //  } 
   //  if($("#id_end_date").val()==""){
   //     alert("Select Ending Date")
   //     return false;
   //  }
    if ($("#id_start_date").val()>$("#id_end_date").val()){
      alert("End date choose correctly")
      return false;
   }
    
   })
})

// add work page validation

$(document).ready(function(){
   $("#subwork").click(function(){
      
     if ($("#id_title").val()==""){
       alert("Enter Title")
       return false;
    }
    if ($("#id_description").val()==""){
       alert("Enter Description")
       return false;
    }
   //  if ($("#id_start_date").val()==""){
   //     alert("Select Start Date")
   //     return false;
   //  } 
   //  if($("#id_end_date").val()==""){
   //     alert("Select Ending Date")
   //     return false;
   //  }
    if ($("#id_start_date").val()>$("#id_end_date").val()){
      alert("End date choose correctly")
      return false;
   }
    if ($("#id_staffid").val()==""){
      alert("Select Staff")
      return false;
   }
    
   })
})
// add department page validation

$(document).ready(function(){
   $("#subdep").click(function(){
      
     if ($("#id_departmentname").val()==""){
       alert("Enter Department")
       return false;
    }
    if ($("#id_description").val()==""){
       alert("Enter Description")
       return false;
    }
  
    
   })
})
// add update status page validation

$(document).ready(function(){
   $("#subupdate").click(function(){
      
     if ($("#id_update_status").val()==""){
       alert("Enter Update status")
       return false;
    }
    if ($("#id_message").val()==""){
       alert("Enter Message")
       return false;
    }
  
    
   })
})
// add complaint page validation

$(document).ready(function(){
   $("#subcomp").click(function(){
      
     if ($("#id_subject").val()==""){
       alert("Enter Complaint Subject")
       return false;
    }
    if ($("#id_message").val()==""){
       alert("Enter Message")
       return false;
    }
  
    
   })
})
// add semester page validation

$(document).ready(function(){
   $("#subsem").click(function(){
      
     if ($("#id_departmentname").val()==""){
       alert("Enter Department")
       return false;
    }
    if ($("#id_semestername").val()==""){
       alert("Enter Semester")
       return false;
    }
  
    
   })
})
// add class page validation

$(document).ready(function(){
   $("#subclass").click(function(){
      
     if ($("#id_classname").val()==""){
       alert("Enter Class")
       return false;
    }
    if ($("#id_seatrows").val()=="0"){
      alert("Enter Class Rows :- using only digits not included 0")
      return false;
    }
    if (!$.isNumeric($("#id_seatrows").val())){
       alert("Enter Class Rows :- using only digits")
       return false;
    }
    if ($("#id_seatcolumns").val()=="0"){
      alert("Enter Class Columns :- using only digits not included 0")
      return false;
    }
    if (!$.isNumeric($("#id_seatcolumns").val())){
       alert("Enter Class Columns :- using only digits")
       return false;
    }
   })
})

// add subject page validation

$(document).ready(function(){
   $("#subsubject").click(function(){
      
     if ($("#id_subject").val()==""){
       alert("Enter Subject name")
       return false;
    }
     if ($('[name="description"]').val()==""){
       alert("Enter Description")
       return false;
    }
     if ($('[name="department"]').val()==""){
       alert("Select Department")
       return false;
    }
    if ($('[name="semester"]').val()==""){
      alert("Select Semester")
       return false;
    }
   })
})
// add Exam page validation



$(document).ready(function(){
   $("#subexam").click(function(){
      if ($("#id_exam").val()==""){
       alert("Enter Exam name")
       return false;
    }
     if ($("#id_department").val()==""){
       alert("Select Department name")
       return false;
    }
     if ($("#id_semester").val()==""){
       alert("Select Semester name")
       return false;
    }
     if ($("#id_subject").val()==""){
       alert("Enter Subject name")
       return false;
    }
   var selectedDate = new Date($("#id_date").val());
   var today = new Date();
   var yesterday = new Date(today);
    if ($("#id_date").val() == ""){
      alert("Enter date ")
      return false;
   }
  
  if (selectedDate < yesterday) {
      alert("Selected date must be greater than today date");
      return false;
  }
   
   // if ($("#id_start_time").val()==""){
   //    alert("Select Start Time")
   //    return false;
   // }
   // if ($("#id_end_time").val()==""){
   //    alert("Select End Time")
   //    return false;
   // }
   if ($("#id_end_time").val()>=$("#id_start_time").val()==""){
      alert("Select valid Time")
      return false;
   }
   })
})
// add Classallotment page validation


$(document).ready(function(){
   $("#suballot").click(function(){
      if ($("#id_department").val()==""){
         alert("Select Department name")
         return false;
      }
      if ($("#id_semester").val()==""){
         alert("Select Semester name")
         return false;
      }
     if ($("#id_subject").val()==""){
       alert("Select Subject name")
       return false;
    }
   
     if ($("#id_exam").val()==""){
       alert("Select Exam name")
       return false;
    }
     if ($("#id_classname").val()==""){
       alert("Select Classroom ")
       return false;
    }
     if ($("#id_name").val()==""){
       alert("Select Staff ")
       return false;
    }
   
   })
})