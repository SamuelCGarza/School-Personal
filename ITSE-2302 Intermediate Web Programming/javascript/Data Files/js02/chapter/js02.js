/*  JavaScript 7th Edition
    Chapter 2
    Chapter case
    Fan Trick Fine Art Photography
    Variables and functions
    Author: Samuel Garza
    Date: 02/18/2024
    Filename: js02.js
 */

// Declare golbal constants for the application
const EMP_COST = 100;       // Photographer hourly rate
const BOOK_COST = 350;      // Cost of memory book
const REPRO_COST = 1250;    // Cost of reproduction rights
const TRAVEL_COST = 2;      // Trabel cost per mile

// Setup the form when the page loads
window.addEventListener("load", setupForm);



// Set the form's default values
function setupForm () {
    document.getElementById("photoNum").value = 1;
    document.getElementById("photoHrs").value = 2;
    document.getElementById("makeBook").checked = false;
    document.getElementById("photoRights").checked = false;
    document.getElementById("photoDist").value = 0;
}

