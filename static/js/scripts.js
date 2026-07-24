document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.querySelector('form');
    const searchButton = document.querySelector('button[type="submit"]');
    const themeToggle = document.getElementById('theme-toggle');

    // Add event listener for form submission
    searchForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        // Show loading animation
        searchButton.classList.add('loading');
        setTimeout(() => {
            searchForm.submit(); // Proceed with the actual form submission after 1 second (simulating loading time)
        }, 1000);
    });

    // Add event listener for theme toggle button
    themeToggle.addEventListener('click', function() {
        const body = document.body;
        if (body.classList.contains('light-theme')) {
            body.classList.replace('light-theme', 'dark-theme');
        } else {
            body.classList.replace('dark-theme', 'light-theme');
        }
    });
});
