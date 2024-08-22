if (!window.dash_clientside) {
    window.dash_clientside = {};
}

if (!window.dash_clientside.clientside) {
    window.dash_clientside.clientside = {};
}

//window.dash_clientside.clientside = {
//    updateViewportStore: function(data) {
//        return data || {};
//    }
//}

window.dash_clientside.clientside.receiveHoverData = function(event) {
    if (event.data.type === 'hoverData') {
        return event.data.payload;  // Return the payload to Dash
    }
    return window.dash_clientside.no_update;  // Use no_update to avoid unnecessary updates
};