let slideIndex = 0;
showSlides();

function showSlides() {
    const slides = document.querySelectorAll('.slide');
    slides.forEach((slide, index) => {
        slide.style.display = index === slideIndex ? 'block' : 'none';
    });
    slideIndex = (slideIndex + 1) % slides.length;
    setTimeout(showSlides, 8000); // Change every 4 seconds
}

function plusSlides(n) {
    const slides = document.querySelectorAll('.slide');
    slideIndex = (slideIndex + n + slides.length) % slides.length;
    showSlides();
}
