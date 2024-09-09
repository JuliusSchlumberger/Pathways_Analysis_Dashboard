
UPDATE_LEGEND = '''
document.addEventListener('DOMContentLoaded', function () {
    var myPlot = document.getElementsByClassName('plotly-graph-div')[0];
    myPlot.on('plotly_legendclick', function(data) {
        var index = data.curveNumber;
        var legendItem = data.data[index];
        var currentName = legendItem.name;

        // Check if the legend item is currently toggled on or off
        if (currentName.includes("Click to show effective robustness (with interactions)")) {
            legendItem.name = currentName.replace("Click to show effective robustness (with interactions)", "Click to show interaction effects compared to robustness without interactions");
        } else {
            // Add "(hidden)" suffix
            legendItem.name = "Click to show effective robustness (with interactions)";
        }

        // Update the plot with the new legend name
        Plotly.update(myPlot, {}, {}, [index]);
    });
});
'''
