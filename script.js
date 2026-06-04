// Smooth Scrolling for Navigation Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Handle Form Submission
const form = document.getElementById('membershipForm');
const successMessage = document.getElementById('successMessage');
const submitBtn = form.querySelector('button');

form.addEventListener('submit', function(e) {
    e.preventDefault(); // Stop page refresh
    
    // Simulate processing
    submitBtn.innerHTML = "Processing...";
    submitBtn.disabled = true;

    setTimeout(() => {
        // Hide form, show success message
        form.style.display = 'none';
        successMessage.style.display = 'block';
        
        // Reset button for next time (optional)
        submitBtn.innerHTML = "Become a Member";
        submitBtn.disabled = false;
    }, 1500);
});
