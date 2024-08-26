

ROH_DICT = {
    'Farmer - Flood': 'flood_agr',
    'Farmer - Drought': 'drought_agr',
    'Municipality - Flood': 'flood_urb',
    'Ship company - Drought': 'drought_shp',
}

ROH_DICT_LIST = list(ROH_DICT.keys())


WHICH_OPTIONS = {
    'Parallel Coordinates Plot': 'PCP',
    'Stacked Bar': 'StackedBar',
    'Heatmap': 'Heatmap'
}

TIMEHORIZONS = {
    'next 20 years': 20,
    'next 60 years': 60,
    'next 100 years': 100
}


SCENARIOS = {
    'historic': 'D',
    '1.5 \u2103': 'G',
    '4 \u2103': 'Wp'
}

ROBUSTNESS_METRICS = {
    'mean across scenario': 'average',
    # 'any other metric preferred by stakeholder': 'whatever'
}

INTRO_TEXT = (
    'Please answer all questions before proceeding. You can also revisit and adjust your answers at a later stage.'
              )

INTERACTION_VIZ = {
    'Pathways Map': 'map',
    'Pathways Robustness': 'performance'
}

OPTION_DICT = {str(key): key for key in range(8)}

MEASURE_ALTERNATIVES = {
    ' Ditch System': 'Ditch_System',
    ' Dike Maintenance': 'Dike_Maintenance',
    ' Flood Resilient Crops': 'Flood_Resilient_Crops',
    "Local support conservation scheme": 'local_support',
    "Small dike elevation increase": 'small_dikes',
    "Large dike elevation increase": 'large_dikes',

}

LINE_WIDTH_MARKER = 2
SIZE_MARKER = 12
LINE_WIDTH_LINE = 2
MAX_LINE_OFFSET = 0.2
FONTS = {
    "annotations": 12,
    'main': 12,
    'title': 15
}

PAGES = [
    {"step": 0, "title": "Home", 'url': '/0-introduction', 'check': 'completed_introduction'},
    {"step": 1, "title": "1) Measure Sequences", 'url': '/1-measure-sequences', 'check': 'completed_alternative_pathways'},
    {"step": 2, "title": "2) Pathways Robustness", 'url': '/2-pathways-robustness', 'check': 'completed_pathways_robustness'},
    {"step": 3, "title": "3) Pathway Maps", 'url': '/3-pathways-maps', 'check': 'completed_pathways_maps'},
    # {"step": 4, "title": "4) Interaction Effects", 'url': '/4-interaction-effects'},
    # {"step": 5, "title": "[5) Multi-risk Pathways]", 'url': '/5-multi_risk-pathways'}
]

INTERACTIONS = {ROH_DICT[ROH_DICT_LIST[0]]: [
    {'No interactions': ['no_interactions']},
    {ROH_DICT_LIST[1]: [ROH_DICT[ROH_DICT_LIST[1]]]},
{ROH_DICT_LIST[2]: [ROH_DICT[ROH_DICT_LIST[2]]]},
{ROH_DICT_LIST[3]: [ROH_DICT[ROH_DICT_LIST[3]]]},
    {f'{ROH_DICT_LIST[1]} & {ROH_DICT_LIST[2]}': [ROH_DICT[ROH_DICT_LIST[1]],ROH_DICT[ROH_DICT_LIST[2]]]},
{f'{ROH_DICT_LIST[1]} & {ROH_DICT_LIST[3]}': [ROH_DICT[ROH_DICT_LIST[1]],ROH_DICT[ROH_DICT_LIST[3]]]},
{f'{ROH_DICT_LIST[2]} & {ROH_DICT_LIST[3]}': [ROH_DICT[ROH_DICT_LIST[2]],ROH_DICT[ROH_DICT_LIST[3]]]},
{f'{ROH_DICT_LIST[1]} & {ROH_DICT_LIST[2]} & {ROH_DICT_LIST[3]}': [ROH_DICT[ROH_DICT_LIST[1]], ROH_DICT[ROH_DICT_LIST[2]],ROH_DICT[ROH_DICT_LIST[3]]]},
],
ROH_DICT[ROH_DICT_LIST[1]]: [
{'No interactions': ['no_interactions']},
    {ROH_DICT_LIST[0]: [ROH_DICT[ROH_DICT_LIST[0]]]},
{ROH_DICT_LIST[2]: [ROH_DICT[ROH_DICT_LIST[2]]]},
{ROH_DICT_LIST[3]: [ROH_DICT[ROH_DICT_LIST[3]]]},
    {f'{ROH_DICT_LIST[0]} & {ROH_DICT_LIST[2]}': [ROH_DICT[ROH_DICT_LIST[0]],ROH_DICT[ROH_DICT_LIST[2]]]},
{f'{ROH_DICT_LIST[0]} & {ROH_DICT_LIST[3]}': [ROH_DICT[ROH_DICT_LIST[0]],ROH_DICT[ROH_DICT_LIST[3]]]},
{f'{ROH_DICT_LIST[2]} & {ROH_DICT_LIST[3]}': [ROH_DICT[ROH_DICT_LIST[2]],ROH_DICT[ROH_DICT_LIST[3]]]},
{f'{ROH_DICT_LIST[0]} & {ROH_DICT_LIST[2]} & {ROH_DICT_LIST[3]}': [ROH_DICT[ROH_DICT_LIST[0]], ROH_DICT[ROH_DICT_LIST[2]],ROH_DICT[ROH_DICT_LIST[3]]]},
],
ROH_DICT[ROH_DICT_LIST[2]]: [
{'No interactions': ['no_interactions']},
    {ROH_DICT_LIST[1]: [ROH_DICT[ROH_DICT_LIST[1]]]},
{ROH_DICT_LIST[0]: [ROH_DICT[ROH_DICT_LIST[0]]]},
{ROH_DICT_LIST[3]: [ROH_DICT[ROH_DICT_LIST[3]]]},
    {f'{ROH_DICT_LIST[1]} & {ROH_DICT_LIST[0]}': [ROH_DICT[ROH_DICT_LIST[1]],ROH_DICT[ROH_DICT_LIST[0]]]},
{f'{ROH_DICT_LIST[1]} & {ROH_DICT_LIST[3]}': [ROH_DICT[ROH_DICT_LIST[1]],ROH_DICT[ROH_DICT_LIST[3]]]},
{f'{ROH_DICT_LIST[0]} & {ROH_DICT_LIST[3]}': [ROH_DICT[ROH_DICT_LIST[0]],ROH_DICT[ROH_DICT_LIST[3]]]},
{f'{ROH_DICT_LIST[1]} & {ROH_DICT_LIST[0]} & {ROH_DICT_LIST[3]}': [ROH_DICT[ROH_DICT_LIST[1]], ROH_DICT[ROH_DICT_LIST[0]],ROH_DICT[ROH_DICT_LIST[3]]]},
],
ROH_DICT[ROH_DICT_LIST[3]]: [
{'No interactions': ['no_interactions']},
    {ROH_DICT_LIST[1]: [ROH_DICT[ROH_DICT_LIST[1]]]},
{ROH_DICT_LIST[2]: [ROH_DICT[ROH_DICT_LIST[2]]]},
{ROH_DICT_LIST[0]: [ROH_DICT[ROH_DICT_LIST[0]]]},
    {f'{ROH_DICT_LIST[1]} & {ROH_DICT_LIST[2]}': [ROH_DICT[ROH_DICT_LIST[1]],ROH_DICT[ROH_DICT_LIST[2]]]},
{f'{ROH_DICT_LIST[1]} & {ROH_DICT_LIST[0]}': [ROH_DICT[ROH_DICT_LIST[1]],ROH_DICT[ROH_DICT_LIST[0]]]},
{f'{ROH_DICT_LIST[2]} & {ROH_DICT_LIST[0]}': [ROH_DICT[ROH_DICT_LIST[2]],ROH_DICT[ROH_DICT_LIST[0]]]},
{f'{ROH_DICT_LIST[1]} & {ROH_DICT_LIST[2]} & {ROH_DICT_LIST[0]}': [ROH_DICT[ROH_DICT_LIST[1]], ROH_DICT[ROH_DICT_LIST[2]],ROH_DICT[ROH_DICT_LIST[0]]]},
],
}

CUSTOM_HOVER = '''
    document.addEventListener("DOMContentLoaded", function() {
        var myPlot = document.getElementsByClassName('plotly-graph-div')[0];

        if (!myPlot) {
            console.error('Plotly graph not found');
            return;
        }

        // Create a div for displaying hover information
        var hoverInfoDiv = document.createElement('div');
        hoverInfoDiv.id = 'hover-info';
        hoverInfoDiv.style.position = 'absolute';
        hoverInfoDiv.style.width = '90%';  
        hoverInfoDiv.style.top = '85%';  
        hoverInfoDiv.style.left = '50%';  
        hoverInfoDiv.style.transform = 'translate(-50%, 0)';  
        hoverInfoDiv.style.backgroundColor = '#f8f9fa';  
        hoverInfoDiv.style.color = '#212529';  
        hoverInfoDiv.style.padding = '10px';  
        hoverInfoDiv.style.border = '1px solid #ccc';  
        hoverInfoDiv.style.borderRadius = '5px';  
        hoverInfoDiv.style.boxShadow = '0px 2px 4px rgba(0, 0, 0, 0.1)';  
        hoverInfoDiv.style.zIndex = '1000';  
        hoverInfoDiv.style.fontSize = '14px';  
        hoverInfoDiv.style.fontFamily = '"Segoe UI", Tahoma, Geneva, Verdana, sans-serif';  
        hoverInfoDiv.style.textAlign = 'center';  
        hoverInfoDiv.style.wordWrap = 'break-word';  
        document.body.appendChild(hoverInfoDiv);

        var lastClickedTrace = null;  // To keep track of the last clicked trace

        // Default message for hoverInfoDiv
        var defaultMessage = 'Click on a marker to highlight the pathway or hover above the markers to get more information';

        // Function to handle hover event
        function handleHover(data) {
            if (!data || !data.points || !data.points[0] || !data.points[0].customdata) {
                // Update the hoverInfoDiv with the default message
                hoverInfoDiv.innerHTML = defaultMessage;
                return;
            }

            // Update the hoverInfoDiv with the hover data
            hoverInfoDiv.innerHTML = `${data.points[0].data.text}`;
        }

        // Function to handle click event
        function handleClick(data) {
            if (!data || !data.points || !data.points[0]) {
                return;
            }

            var clickedGroups = data.points[0].customdata;

            // Reset styling for all traces
            var defaultUpdate = {
                'line.width': 1,
                'marker.line.width': 1
            };
            Plotly.restyle(myPlot, defaultUpdate);

            var indices = [];
            for (var i = 0; i < myPlot.data.length; i++) {
                var traceGroups = myPlot.data[i].customdata;

                if (traceGroups) {
                    if (Array.isArray(traceGroups[0])) {
                        traceGroups = traceGroups.flat();
                    }
                    if (clickedGroups.some(group => traceGroups.includes(group))) {
                        indices.push(i);
                    }
                }
            }

            if (lastClickedTrace && lastClickedTrace === data.points[0].pointIndex) {
                // If the same trace is clicked again, reset the style
                lastClickedTrace = null;
                Plotly.restyle(myPlot, defaultUpdate, indices);
            } else {
                // Update the clicked traces
                lastClickedTrace = data.points[0].pointIndex;
                var updateHover = {
                    'line.width': 4,
                    'marker.line.width': 4
                };
                Plotly.restyle(myPlot, updateHover, indices);
            }
        }

        // Attach hover and click event listeners
        myPlot.on('plotly_hover', handleHover);
        myPlot.on('plotly_unhover', function() {
            // On unhover, reset to default message
            hoverInfoDiv.innerHTML = defaultMessage;
        });
        myPlot.on('plotly_click', handleClick);

        // Initialize with the default message
        hoverInfoDiv.innerHTML = defaultMessage;

    });
'''



CUSTOM_LEGEND_CHANGE = '''
document.addEventListener('DOMContentLoaded', function () {
    console.log('Document loaded');

    var myPlot = document.getElementsByClassName('plotly-graph-div')[0];
    console.log('myPlot:', myPlot);

    if (!myPlot) {
        console.error('Plotly graph not found');
        return;
    }

    // Create a div for displaying hover information
    var hoverInfoDiv = document.createElement('div');
    hoverInfoDiv.id = 'hover-info';
    hoverInfoDiv.style.position = 'absolute';
    hoverInfoDiv.style.width = '23%';
    hoverInfoDiv.style.top = '55%';
    hoverInfoDiv.style.left = '77%';
    hoverInfoDiv.style.transform = 'translate(-50%, 0)';
    hoverInfoDiv.style.backgroundColor = '#f8f9fa';
    hoverInfoDiv.style.color = '#212529';
    hoverInfoDiv.style.padding = '10px';
    hoverInfoDiv.style.border = '1px solid #ccc';
    hoverInfoDiv.style.borderRadius = '5px';
    hoverInfoDiv.style.boxShadow = '0px 2px 4px rgba(0, 0, 0, 0.1)';
    hoverInfoDiv.style.zIndex = '1000';
    hoverInfoDiv.style.fontSize = '14px';
    hoverInfoDiv.style.fontFamily = '"Segoe UI", Tahoma, Geneva, Verdana, sans-serif';
    hoverInfoDiv.style.textAlign = 'center';
    hoverInfoDiv.style.wordWrap = 'break-word';
    document.body.appendChild(hoverInfoDiv);
    console.log('Hover info div created and appended');

    // Default message for hoverInfoDiv
    var defaultMessage = 'Hover above the bars to see more information here';

    // Function to handle hover event
    function handleHover(data) {
        console.log('Hover event detected:', data);

        if (!data || !data.points || !data.points[0] || !data.points[0].data.customdata) {
            console.log('No customdata found, resetting to default message');
            hoverInfoDiv.innerHTML = defaultMessage;
            return;
        }

        // Update the hoverInfoDiv with the hover data
        hoverInfoDiv.innerHTML = `${data.points[0].data.customdata}`;
        console.log('Hover info updated:', hoverInfoDiv.innerHTML);
    }

    // Attach hover and unhover event listeners
    myPlot.on('plotly_hover', handleHover);
    myPlot.on('plotly_unhover', function () {
        console.log('Unhover event detected');
        hoverInfoDiv.innerHTML = defaultMessage;
    });

    // Initialize with the default message
    hoverInfoDiv.innerHTML = defaultMessage;
    console.log('Hover info div initialized with default message');

    // Custom legend click handling
    myPlot.on('plotly_legendclick', function (data) {
        console.log('Legend click detected:', data);

        var index = data.curveNumber;
        var legendItem = data.data[index];
        var currentName = legendItem.name;

        console.log('Legend item name before update:', currentName);

        // Check if the legend item is currently toggled on or off
        if (currentName.includes("Click to show effective robustness (with interactions)")) {
            legendItem.name = currentName.replace("Click to show effective robustness (with interactions)", "Click to show interaction effects compared to robustness without interactions");
        } else {
            legendItem.name = "Click to show effective robustness (with interactions)";
        }

        console.log('Legend item name after update:', legendItem.name);

        // Update the plot with the new legend name
        Plotly.update(myPlot, {}, {}, [index]);
        console.log('Plotly update called with new legend name');
    });
});
'''
