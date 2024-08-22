// assets/viewport.js
document.addEventListener('DOMContentLoaded', function() {
    function updateViewportSize() {
        const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0);
        const vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0);

        fetch('/save_viewport_size', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ vh: vh, vw: vw })
        }).then(response => response.json())
          .then(data => console.log('Success:', data))
          .catch((error) => console.error('Error:', error));
    }
    window.addEventListener('resize', updateViewportSize);
    updateViewportSize();  // Run on initial load
});
