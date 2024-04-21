/*    JavaScript 7th Edition
      Chapter 3
      Project 03-01

      Application to calculate total order cost
      Author: Samuel Garza
      Date: 02/25/2024   

      Filename: project03-01.js
*/

// Variable containing items in menuItem class
var menuItems = document.getElementsByClassName('menuItem');



// Loop through menuItems adding event event listener, running calcTotal() when clicked
for (var i = 0; i < menuItems.length; i++) {
      menuItems[i].addEventListener('click', calcTotal);
}



// Function to calculate sum of all clicked menu items
function calcTotal() {
      var orderTotal = 0;
      for (var i = 0; i < menuItems.length; i++) {
            if (menuItems[i].checked) {
            orderTotal += Number(menuItems[i].value);
            }
      }
      document.getElementById('billTotal').innerHTML = formatCurrency(orderTotal);
}
    


 // Function to display a numeric value as a text string in the format $##.## 
 function formatCurrency(value) {
    return "$" + value.toFixed(2);
 }