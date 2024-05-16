document.addEventListener('DOMContentLoaded', function() {
    function sendViewportSize() {
        const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0);
        const vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0);

        const event = new CustomEvent('sendViewportSize', {
            detail: { vh: vh, vw: vw }
        });
        window.dispatchEvent(event);
    }

    window.addEventListener('resize', sendViewportSize);
    sendViewportSize(); // Also update on initial load
});
