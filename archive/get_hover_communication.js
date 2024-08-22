document.addEventListener('DOMContentLoaded', function() {
    window.addEventListener('message', function(event) {
        if (event.data.type === 'hoverData') {
            console.log('Message received in parent:', event.data.payload);  // Log the received data

            var hoverStore = document.getElementById('hover-store');
            if (hoverStore) {
                var hoverData = JSON.stringify(event.data.payload);  // Convert the hoverData to JSON string
                console.log('Storing data in hoverStore:', hoverData);  // Debugging line
                hoverStore.data = hoverData;  // Store the JSON string in the data property
                hoverStore.dispatchEvent(new Event('change'));  // Trigger a change event
                console.log('Change event dispatched');  // Debugging line
            } else {
                console.error('hoverStore is null or undefined.');
            }
        }
    });
});
