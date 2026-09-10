// Main JavaScript - Toolora

// Hamburger Menu
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        navMenu.classList.toggle('active');
    });
}

// Close menu when link is clicked
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
    });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add loading animation
function showLoading() {
    const loader = document.createElement('div');
    loader.className = 'loader';
    loader.innerHTML = '<p>درحال پردازش...</p>';
    document.body.appendChild(loader);
    return loader;
}

function removeLoading(loader) {
    if (loader) {
        loader.remove();
    }
}

// Format large numbers with commas
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

// Copy to clipboard helper
function copyToClipboard(text) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
}

// API Error Handler
function handleApiError(error) {
    console.error('API Error:', error);
    alert('خطای را روبرو شدیم. لطفاً دوباره امیاز کنید.');
}

// Add active state to nav links based on current page
window.addEventListener('load', () => {
    const currentPage = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        const href = link.getAttribute('href');
        if (currentPage === href || currentPage.includes(href)) {
            link.style.opacity = '0.7';
        }
    });
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all tool cards
document.querySelectorAll('.tool-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    observer.observe(card);
});

// Export utilities
window.TooloraUtils = {
    formatNumber,
    copyToClipboard,
    showLoading,
    removeLoading,
    handleApiError
};
