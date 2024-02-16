document.querySelectorAll('.features').forEach(item => {
    item.addEventListener('click', function() {
        // Toggle background color directly using JavaScript
        if (this.style.backgroundColor === 'black') {
            this.style.backgroundColor = 'white';
        } else {
            this.style.backgroundColor = 'black';
            this.style.borderRadius = '10px';
        }
    });
});