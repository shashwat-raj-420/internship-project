        // Modal functionality
        function openModal() {
            document.getElementById('demoModal').classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeModal() {
            document.getElementById('demoModal').classList.remove('active');
            document.body.style.overflow = 'auto';
            // Clear form and messages
            document.getElementById('demoForm').reset();
            document.getElementById('messageContainer').innerHTML = '';
        }

        // Close modal when clicking outside
        document.getElementById('demoModal').addEventListener('click', function(e) {
            if (e.target === this) {
                closeModal();
            }
        });

        // Form submission
        function submitForm(event) {
            event.preventDefault();
            
            const submitBtn = document.getElementById('submitBtn');
            const messageContainer = document.getElementById('messageContainer');
            const formData = new FormData(event.target);
            
            // Show loading state
            submitBtn.innerHTML = '<span class="loading"></span> Reserving Your Spot...';
            submitBtn.disabled = true;
            
            // Clear previous messages
            messageContainer.innerHTML = '';
            
            // Simulate form submission (replace with actual API call)
            setTimeout(() => {
                // Simulate success (you can add actual form submission logic here)
                const success = Math.random() > 0.1; // 90% success rate for demo
                
                if (success) {
                    messageContainer.innerHTML = `
                        <div class="success-message">
                            <i class="fas fa-check-circle"></i> 
                            <strong>Success!</strong> Your spot has been reserved. Check your email for demo details.
                        </div>
                    `;
                    
                    // Reset form after successful submission
                    document.getElementById('demoForm').reset();
                    
                    // Auto-close modal after 3 seconds
                    setTimeout(() => {
                        closeModal();
                    }, 3000);
                } else {
                    messageContainer.innerHTML = `
                        <div class="error-message">
                            <i class="fas fa-exclamation-triangle"></i> 
                            <strong>Error!</strong> Something went wrong. Please try again.
                        </div>
                    `;
                }
                
                // Reset button
                submitBtn.innerHTML = 'Reserve My Spot Now';
                submitBtn.disabled = false;
            }, 2000);
        }

        // Smooth scrolling for navigation links
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

        // Header scroll effect
        window.addEventListener('scroll', function() {
            const header = document.querySelector('.header');
            if (window.scrollY > 100) {
                header.style.background = 'rgba(255, 255, 255, 0.98)';
                header.style.boxShadow = '0 5px 30px rgba(0,0,0,0.1)';
            } else {
                header.style.background = 'rgba(255, 255, 255, 0.95)';
                header.style.boxShadow = '0 2px 20px rgba(0,0,0,0.1)';
            }
        });

        // Intersection Observer for animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Observe elements for animation
        document.addEventListener('DOMContentLoaded', function() {
            const animateElements = document.querySelectorAll('.challenge-card, .testimonial, .stat');
            animateElements.forEach(el => {
                el.style.opacity = '0';
                el.style.transform = 'translateY(30px)';
                el.style.transition = 'all 0.6s ease';
                observer.observe(el);
            });
        });

        // Counter animation for stats
        function animateCounters() {
            const counters = document.querySelectorAll('.stat-number');
            counters.forEach(counter => {
                const target = counter.textContent;
                const numericValue = parseInt(target.replace(/[^\d]/g, ''));
                
                if (numericValue > 0) {
                    let current = 0;
                    const increment = numericValue / 100;
                    const timer = setInterval(() => {
                        current += increment;
                        if (current >= numericValue) {
                            counter.textContent = target;
                            clearInterval(timer);
                        } else {
                            if (target.includes('+')) {
                                counter.textContent = Math.floor(current).toLocaleString() + '+';
                            } else if (target.includes('⭐')) {
                                counter.textContent = '5.0 ⭐';
                            } else {
                                counter.textContent = Math.floor(current).toLocaleString();
                            }
                        }
                    }, 50);
                }
            });
        }

        // Trigger counter animation when stats section is visible
        const statsSection = document.querySelector('.community');
        const statsObserver = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounters();
                    statsObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        if (statsSection) {
            statsObserver.observe(statsSection);
        }

        // Form validation
        function validateForm() {
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const phone = document.getElementById('phone').value.trim();
            const goals = document.getElementById('goals').value.trim();
            
            if (!name || !email || !phone || !goals) {
                return false;
            }
            
            // Email validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                return false;
            }
            
            // Phone validation (basic)
            const phoneRegex = /^[\d\s\-\+\(\)]{10,}$/;
            if (!phoneRegex.test(phone)) {
                return false;
            }
            
            return true;
        }

        // Real-time form validation
        document.getElementById('email').addEventListener('blur', function() {
            const email = this.value.trim();
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            
            if (email && !emailRegex.test(email)) {
                this.style.borderColor = '#e74c3c';
                this.style.backgroundColor = '#ffeaea';
            } else {
                this.style.borderColor = '#27ae60';
                this.style.backgroundColor = '#eafaf1';
            }
        });

        document.getElementById('phone').addEventListener('blur', function() {
            const phone = this.value.trim();
            const phoneRegex = /^[\d\s\-\+\(\)]{10,}$/;
            
            if (phone && !phoneRegex.test(phone)) {
                this.style.borderColor = '#e74c3c';
                this.style.backgroundColor = '#ffeaea';
            } else {
                this.style.borderColor = '#27ae60';
                this.style.backgroundColor = '#eafaf1';
            }
        });

        // Keyboard shortcuts
        document.addEventListener('keydown', function(e) {
            // Escape key to close modal
            if (e.key === 'Escape' && document.getElementById('demoModal').classList.contains('active')) {
                closeModal();
            }
        });

        // Prevent form submission on Enter in input fields (except submit button)
        document.querySelectorAll('input').forEach(input => {
            input.addEventListener('keydown', function(e) {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    const form = this.closest('form');
                    const inputs = Array.from(form.querySelectorAll('input, textarea, select'));
                    const currentIndex = inputs.indexOf(this);
                    const nextInput = inputs[currentIndex + 1];
                    
                    if (nextInput) {
                        nextInput.focus();
                    } else {
                        form.querySelector('button[type="submit"]').focus();
                    }
                }
            });
        });