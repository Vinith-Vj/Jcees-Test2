document.addEventListener("DOMContentLoaded", () => {
    const menuIcon = document.getElementById('menuIcon');
    const closeIcon = document.getElementById('closeIcon');
    const menu = document.getElementById('menu');

    if (menuIcon && menu) { // ✅ Prevents errors if elements don't exist
        menuIcon.addEventListener('click', () => {
            menu.classList.toggle('-translate-y-full'); // Toggle the class
        });
        closeIcon.addEventListener('click', () => {
            menu.classList.toggle('-translate-y-full');
        });

        document.addEventListener('click', (event) => {
            if (!menu.contains(event.target) && !menuIcon.contains(event.target)) {
                menu.classList.add('-translate-y-full');
            }
        });
    }

    const dropdownButton = document.getElementById('dropdownButton');
    const dropdownMenu = document.getElementById('dropdownMenu');

    if (dropdownButton && dropdownMenu) { // ✅ Prevents errors if elements don't exist
        dropdownButton.addEventListener('click', () => {
            dropdownMenu.classList.toggle('hidden'); // Show/hide menu
        });

        document.addEventListener('click', (event) => {
            if (!dropdownButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
                dropdownMenu.classList.add('hidden');
            }
        });
    }
});


document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById("testimonialContainer");
    let index = 0;
    
    function nextSlide() {
        index = (index + 1) % 3; // Change 3 to the number of testimonials
        container.style.transform = `translateX(-${index * 100}%)`;
    }
    
    setInterval(nextSlide, 3000); // Change slide every 3 seconds
});

document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById("keralaCarousal");
    let index = 0;
    
    function nextSlide() {
        index = (index + 1) % 3; // Change 3 to the number of testimonials
        container.style.transform = `translateX(-${index * 100}%)`;
    }
    
    setInterval(nextSlide, 5000); // Change slide every 3 seconds
});
