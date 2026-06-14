document.addEventListener('DOMContentLoaded', () => {
    // ---------------------------------------------------------
    // Mobile Navigation & Hamburger Toggle
    // ---------------------------------------------------------
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('nav-active');
            hamburger.classList.toggle('toggle');
        });
    }

    // ---------------------------------------------------------
    // Dynamic Copyright Year
    // ---------------------------------------------------------
    const yearSpan = document.getElementById('current-year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    // ---------------------------------------------------------
    // Interactive Mouse Animation (Parallax)
    // ---------------------------------------------------------
    // We listen on the document for mouse movement
    document.addEventListener('mousemove', (e) => {
        const floaters = document.querySelectorAll('.floater');

        if (floaters.length === 0) return;

        const x = e.clientX;
        const y = e.clientY;

        floaters.forEach((floater, index) => {
            // Calculate speed based on index (different layers move at different speeds)
            const speed = (index + 1) * 0.03;

            // Reverse direction for parallax effect (-x)
            const xOffset = (window.innerWidth - x * speed) / 25;
            const yOffset = (window.innerHeight - y * speed) / 25;

            // Apply transform smoothly
            floater.style.transform = `translate(${xOffset}px, ${yOffset}px)`;
        });
    });

    // ---------------------------------------------------------
    // Dynamic Greetings (Optional Sentiment)
    // ---------------------------------------------------------
    const heroText = document.querySelector('.hero p');
    if (heroText) {
        const hour = new Date().getHours();
        console.log(`Current hour: ${hour}. Theme loaded.`);
    }

    // ---------------------------------------------------------
    // Smooth Scroll for Anchor Links
    // ---------------------------------------------------------
    // FAQ Accordion Script yang sudah diperbaiki
    document.querySelectorAll('.faq-question').forEach(button => {
        button.addEventListener('click', () => {
            // Menggunakan .closest agar selalu tepat mendeteksi elemen .faq-item
            const faqItem = button.closest('.faq-item'); 

            // Menutup item FAQ lain yang sedang terbuka
            document.querySelectorAll('.faq-item').forEach(item => {
                if (item !== faqItem) {
                    item.classList.remove('active');
                }
            });

            // Buka/tutup item yang diklik
            faqItem.classList.toggle('active');
        });
    });
});
