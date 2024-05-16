// In your assets/clientside.js
if (!window.dash_clientside) {
    window.dash_clientside = {};
}

window.dash_clientside.clientside = {
    updateViewportStore: function(event) {
        return event.detail;
    }
}