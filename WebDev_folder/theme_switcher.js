// theme_switcher.js

document.addEventListener("DOMContentLoaded", function() {
    const themeToggleButton = document.getElementById("theme-toggle");
    const body = document.body;
    const navbar = document.querySelector(".navbar");
    const navLinks = document.querySelectorAll(".nav-links a");
    const header = document.querySelector("header");

    themeToggleButton.addEventListener("click", function() {
        body.classList.toggle("dark-theme");
        navbar.classList.toggle("dark-theme");
        header.classList.toggle("dark-theme");
        navLinks.forEach(link => link.classList.toggle("dark-theme"));
    });
});