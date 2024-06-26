"use strict";
/*    JavaScript 7th Edition
      Chapter 7
      Project 07-01

      Project to validate a form used for setting up a new account
      Author: Samuel Garza
      Date: 04007/2024

      Filename: project07-01.js
*/

let signupForm = document.getElementById("signup");

signupForm.addEventListener("submit", function(e) { 
    
   e.preventDefault(); // prevent form from submitting by default

   let pwd = document.getElementById("pwd").value;
   let feedback = document.getElementById("feedback");

   // create regular expressions
   let regex1 = /[A-Z]/; // matches any uppercase letter A through Z
   let regex2 = /\d/; // matches any single digit
   let regex3 = /[!$#%]/; // matches any of the symbols !$#%

   // validate password
   if (pwd.length < 8) {
      feedback.textContent = "Your password must be at least 8 characters.";
   } else if (!regex1.test(pwd)) {
      feedback.textContent = "Your password must include an uppercase letter.";
   } else if (!regex2.test(pwd)) {
      feedback.textContent = "Your password must include a number.";
   } else if (!regex3.test(pwd)) {
      feedback.textContent = "Your password must include one of the following: !$#%";
   } else {
      // if password is valid, submit form
      signupForm.submit();
   }
});