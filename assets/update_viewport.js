document.addEventListener('DOMContentLoaded', function() {
    function updateViewportSize() {
        const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0);
        const vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0);
        
        const event = new CustomEvent('sendViewportSize', {
            detail: { vh: vh, vw: vw }
        });
        window.dispatchEvent(event);
        
        // Update an element with ID 'viewport-data-input'
        const inputElement = document.getElementById('viewport-data-input');
        if (inputElement) {
            inputElement.value = JSON.stringify({vh: vh, vw: vw});
            inputElement.dispatchEvent(new Event('change'));  // Trigger change event to notify Dash
        }
    }
    window.addEventListener('resize', updateViewportSize);
    updateViewportSize();  // Also update on initial load
});
