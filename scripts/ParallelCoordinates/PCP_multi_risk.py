from scripts.map_system_parameters import AXIS_LABELS
from scripts.design_choices.main_dashboard_design_choices import COLORSCALE_PCP,COLORSCALE_NAMES, FIG_DIMENSIONS, FONTS
from scripts.design_choices.main_dashboard_dropdowns import ROH_DICT_INV,ROH_DICT, RANGE
from scripts.ParallelCoordinates.make_thicker_lines import make_thicker_lines
from scripts.helperfunctions.add_line_breaks_axis_labels import add_line_breaks
from scripts.ParallelCoordinates.create_custom_colorscale import create_custom_colorscale
from scripts.ParallelCoordinates.update_traces import update_traces_with_ticks

from scripts.helperfunctions.add_measure_buttons import add_measure_buttons_PCP
from scripts.helperfunctions.images_as_base64 import image_to_base64
from scripts.main_central_path_directions import LEGENDS_LOCATION

import plotly.graph_objects as go
import pandas as pd
import json

def Parallel_Coordinates_Plot(df, sectors_of_interest_list, figure_title, robustness_metric):
    ## Rename pathways in sequential order
    # Load the dictionary from the JSON file
    complete_replace_dict = {}
    for risk_owner_hazard in sectors_of_interest_list:
        complete_replace_dict[risk_owner_hazard] = {}
        with open(f'dynamic_data/data/renamed_pathways/renamed_pathways_{risk_owner_hazard}.json', 'r') as json_file:
            replace_dict = json.load(json_file)
        invert_replace_dict = {v: int(k) for k, v in replace_dict.items()}
        complete_replace_dict[risk_owner_hazard] = invert_replace_dict

    new_df = df.copy()
    pivot_df = new_df.pivot_table(
        index=sectors_of_interest_list,
        columns='objective_parameter',
        values='Value',
        # aggfunc='sum'
    )

    reset_pivot = pivot_df.reset_index()
    # for risk_owner_hazard in sectors_of_interest_list:
    #     # Replace old values with new values in the 'risk_owner_hazard' column
    #     reset_pivot[risk_owner_hazard] = reset_pivot[risk_owner_hazard].replace(complete_replace_dict[risk_owner_hazard])
    reset_pivot['Color'] = reset_pivot.index + 1


    objective_parameters = df['objective_parameter'].unique()
    objective_parameters = sorted(objective_parameters, key=lambda x: 'Cost' not in x)

    new_order = [*sectors_of_interest_list, *objective_parameters, 'Color']
    reset_pivot = reset_pivot[new_order]

    reset_pivot = reset_pivot.rename(columns=AXIS_LABELS)
    reset_pivot = reset_pivot.rename(columns=ROH_DICT_INV)

    dimensions_to_modify = df.objective_parameter.unique()
    dimensions_to_modify_renamed = [AXIS_LABELS[dim] for dim in dimensions_to_modify]
    dimensions_to_modify_combined = [ROH_DICT_INV[s] for s in sectors_of_interest_list] + dimensions_to_modify_renamed

    combined_data = make_thicker_lines(reset_pivot, dimensions_to_modify_combined, 0.005, 50)

    labels = [col for col in combined_data.columns if col not in ['Color', 'robustness_metric']]

    labels_with_linebreaks = {v: add_line_breaks(v, 5) for v in [ROH_DICT_INV[s] for s in sectors_of_interest_list]}
    labels_with_linebreaks_II = {v: add_line_breaks(v, 8) for v in dimensions_to_modify_renamed}
    labels_with_linebreaks.update(labels_with_linebreaks_II)

    combined_data_sorted = combined_data.sort_values(by=['Color'], ascending=False).reset_index(drop=True)

    dimensions = [
        dict(range=RANGE[col],
             label=labels_with_linebreaks[col],
             values=combined_data_sorted[col],
)
        for col in combined_data_sorted.columns if col not in ['Color', 'robustness_metric']
    ]

    color_values, custom_colorscale = create_custom_colorscale(combined_data_sorted, None)

    fig = go.Figure(data=go.Parcoords(
        line=dict(
            color=color_values,
            colorscale=custom_colorscale,
        ),
        dimensions=dimensions,
        unselected=dict(line=dict(color='lightgrey', opacity=0.0)),
        domain=dict(
            x=[0.02, .95],  # Adjust the horizontal domain (left, right)
            y=[0.1, 0.86]  # Adjust the vertical domain (bottom, top)
        )

    ))


    update_traces_with_ticks(fig, ROH_DICT, RANGE)

    fig.update_layout(
        # Title and positioning
        title={'text': add_line_breaks(figure_title, 80), 'y': .95, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'bottom'},
        title_font_size=FONTS['title'],
        font_size=FONTS['main']-4,

        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        xaxis2=dict(visible=False),
        yaxis2=dict(visible=False),
        paper_bgcolor='rgba(0,0,0,0)',  # Make the plot background transparent
        plot_bgcolor='rgba(0,0,0,0)',  # Make the plot area background transparent

        # Custom margins
        # margin=dict(t=50, b=50),  # Final margin settings as it appears you've adjusted them
        margin=dict(l=5, r=5, t=30, b=5),
        # Fixed dimensions for the plot
        width=FIG_DIMENSIONS['width'],  # Width set to 1300 pixels
        height=FIG_DIMENSIONS['height'],
        autosize=False,  # Disable autosizing to use the specified width and height

    )

    return fig