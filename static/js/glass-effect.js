// filepath: /c:/Users/ekari/OneDrive/Desktop/NEWFINAL/starmamas-4/static/js/glass-effects.js
document.addEventListener('DOMContentLoaded', () => {
    const glassCard = document.querySelector('.glass-card');
    const form = document.querySelector('form');
    const inputs = document.querySelectorAll('.form-control');

    // Mouse movement effect
    if (glassCard) {
        glassCard.addEventListener('mousemove', (e) => {
            const rect = glassCard.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            // Calculate rotation based on mouse position
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = (y - centerY) / 20;
            const rotateY = (centerX - x) / 20;

            // Apply the transform with perspective
            glassCard.style.transform = `
                perspective(1000px)
                rotateX(${rotateX}deg)
                rotateY(${rotateY}deg)
                scale(1.02)
            `;
        });

        // Reset transform on mouse leave
        glassCard.addEventListener('mouseleave', () => {
            glassCard.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale(1)';
        });
    }

    // Add focus effects for form inputs
    inputs.forEach(input => {
        // Create ripple effect on focus
        input.addEventListener('focus', function() {
            this.style.transition = 'all 0.3s ease';
            this.style.boxShadow = '0 0 15px rgba(70, 130, 180, 0.4)';
            this.style.transform = 'scale(1.02)';
        });

        // Remove effects on blur
        input.addEventListener('blur', function() {
            this.style.boxShadow = 'none';
            this.style.transform = 'scale(1)';
        });
    });

    // Add loading state to login button
    const loginButton = document.querySelector('button[type="submit"]');
    if (loginButton) {
        loginButton.addEventListener('click', function(e) {
            if (form.checkValidity()) {
                this.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Logging in...';
                this.disabled = true;
            }
        });
    }

    // Add subtle background animation
    const updateBackground = () => {
        const scrollPosition = window.scrollY;
        const hueRotation = (scrollPosition / window.innerHeight) * 360;
        document.body.style.filter = `hue-rotate(${hueRotation}deg)`;
    };

    // Throttle the scroll event for better performance
    let ticking = false;
    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                updateBackground();
                ticking = false;
            });
            ticking = true;
        }
    });

    // Add notification system
    window.showNotification = (message, type = 'success') => {
        const notification = document.getElementById('notification');
        if (notification) {
            notification.textContent = message;
            notification.className = `notification alert alert-${type} fade show`;
            notification.style.display = 'block';
            
            setTimeout(() => {
                notification.style.display = 'none';
            }, 3000);
        }
    };

    // Form validation enhancement
    if (form) {
        form.addEventListener('submit', (e) => {
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
                showNotification('Please fill in all required fields', 'danger');
            }
            form.classList.add('was-validated');
        });
    }
});