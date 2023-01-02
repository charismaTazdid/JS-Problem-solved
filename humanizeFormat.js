//Formats a number to a human-readable string
//given input: 1 => expected output: 1st
//given input: 2 => expected output: 1nd
//given input: 8 => expected output: 8th
//given input: 3 => expected output: 3rd

function humanizeFormat(num) {
    if(typeof(num) == "undefined") return;
   if(num % 100 >= 11 && num % 100 <= 13)
         return num + "th";
         
         switch(num % 10) {
             case 1: return num + "st";
             case 2: return num + "nd";
             case 3: return num + "rd";
         }
         return num + "th";
     }

 console.log(humanizeFormat(1));  
 console.log(humanizeFormat(11));  
 console.log(humanizeFormat(8));  
 console.log(humanizeFormat(3));  
 console.log(humanizeFormat(301));  
 console.log(humanizeFormat(402)); 
 console.log(humanizeFormat(403)); 
 console.log(humanizeFormat(408)); 
 console.log(humanizeFormat(411)); 
 console.log(humanizeFormat(412)); 
 console.log(humanizeFormat(414)); 