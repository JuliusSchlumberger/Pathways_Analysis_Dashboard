from scripts.map_system_parameters import AXIS_LABELS
from scripts.design_choices.main_dashboard_design_choices import COLORSCALE_PCP,COLORSCALE_NAMES, FIG_DIMENSIONS, FONTS
from scripts.design_choices.main_dashboard_dropdowns import ROH_DICT_INV,ROH_DICT, RANGE
from scripts.ParallelCoordinates.make_thicker_lines import make_thicker_lines
from scripts.helperfunctions.add_line_breaks_axis_labels import add_line_breaks
from scripts.ParallelCoordinates.create_custom_colorscale import create_custom_colorscale
from scripts.ParallelCoordinates.generate_ticks import generate_ticks
from scripts.helperfunctions.add_measure_buttons import add_measure_buttons_PCP
from scripts.helperfunctions.images_as_base64 import image_to_base64
from scripts.main_central_path_directions import LEGENDS_LOCATION

import plotly.graph_objects as go
import pandas as pd
import json

def Parallel_Coordinates_Plot(df, risk_owner_hazard, figure_title, robustness_metric, df_interaction=None):
    ## Rename pathways in sequential order
    # Load the dictionary from the JSON file
    with open(f'dynamic_data/data/renamed_pathways/renamed_pathways_{risk_owner_hazard}.json', 'r') as json_file:
        replace_dict = json.load(json_file)
    invert_replace_dict = {v: int(k) for k, v in replace_dict.items()}


    if df_interaction is None:
        new_df = df.copy()
        pivot_df = new_df.pivot_table(
            index=[risk_owner_hazard],
            columns='objective_parameter',
            values='Value',
            aggfunc='sum'
        )
        reset_pivot = pivot_df.reset_index()
        # Replace old values with new values in the 'risk_owner_hazard' column
        reset_pivot[risk_owner_hazard] = reset_pivot[risk_owner_hazard].replace(invert_replace_dict)
        reset_pivot['Color'] = reset_pivot[risk_owner_hazard] + 1
    else:
        new_df = df.copy()
        df_interaction_new = df_interaction.copy()
        pivot_df1 = new_df.pivot_table(
            index=[risk_owner_hazard],
            columns='objective_parameter',
            values='Value',
            aggfunc='sum'
        )
        reset_pivot1 = pivot_df1.reset_index()
        # Replace old values with new values in the 'risk_owner_hazard' column
        reset_pivot1[risk_owner_hazard] = reset_pivot1[risk_owner_hazard].replace(invert_replace_dict)
        reset_pivot1['Color'] = 1000

        pivot_df2 = df_interaction_new.pivot_table(
            index=[risk_owner_hazard],
            columns='objective_parameter',
            values='Value',
            aggfunc='sum'
        )
        reset_pivot2 = pivot_df2.reset_index()
        reset_pivot2[risk_owner_hazard] = reset_pivot2[risk_owner_hazard].replace(invert_replace_dict)
        reset_pivot2['Color'] = reset_pivot2[risk_owner_hazard]

        reset_pivot = pd.concat([reset_pivot1, reset_pivot2], ignore_index=True)

    objective_parameters = df['objective_parameter'].unique()
    objective_parameters = sorted(objective_parameters, key=lambda x: 'Cost' not in x)

    new_order = [risk_owner_hazard, *objective_parameters, 'Color']
    reset_pivot = reset_pivot[new_order]

    reset_pivot = reset_pivot.rename(columns=AXIS_LABELS)
    reset_pivot = reset_pivot.rename(columns=ROH_DICT_INV)

    dimensions_to_modify = df.objective_parameter.unique()
    dimensions_to_modify = [ROH_DICT_INV[risk_owner_hazard]] + [AXIS_LABELS[dim] for dim in dimensions_to_modify]

    combined_data = make_thicker_lines(reset_pivot, dimensions_to_modify, 0.005, 50)

    labels = [col for col in combined_data.columns if col not in ['Color', 'robustness_metric']]
    labels_with_linebreaks = {v: add_line_breaks(v) for v in labels}

    combined_data_sorted = combined_data.sort_values(by=['Color'], ascending=False).reset_index(drop=True)

    dimensions = [
        dict(range=RANGE[col],
             label=labels_with_linebreaks[col],
             values=combined_data_sorted[col],
)
        for col in combined_data_sorted.columns if col not in ['Color', 'robustness_metric']
    ]

    color_values, custom_colorscale = create_custom_colorscale(combined_data_sorted, df_interaction)

    fig = go.Figure(data=go.Parcoords(
        line=dict(
            color=color_values,
            colorscale=custom_colorscale,
        ),
        dimensions=dimensions,
        unselected=dict(line=dict(color='lightgrey', opacity=0.0)),
        domain=dict(
            x=[0.2, 0.9],  # Adjust the horizontal domain (left, right)
            y=[0.25, 0.82]  # Adjust the vertical domain (bottom, top)
        )

    ))

    fig.update_traces(
        dimensions=[
            {**d,
             "tickvals": generate_ticks(
                 d['range'][0],
                 d['range'][1],
                 d['range'][1] + 1 if d['label'].replace('<br>', '') in list(ROH_DICT.keys()) else (
                     int(d['range'][1] / 10) + 1 if d['range'][1] <= 1000 else int(d['range'][1] / 100) + 1),
                 1 if d['label'].replace('<br>', '') in list(ROH_DICT.keys()) else (
                     int(d['range'][1]/1000) if d['range'][1] > 1000 else (
                     1 if d['range'][1] <= 100 else 10))
             )[0],
             "ticktext": generate_ticks(
                 0 if d['label'].replace('<br>', '') in list(ROH_DICT.keys()) else d['range'][0],
                 RANGE[d['label'].replace('<br>', '')][1] if d['label'].replace('<br>', '') in list(ROH_DICT.keys()) else d['range'][1],
                 RANGE[d['label'].replace('<br>', '')][1] + 1 if d['label'].replace('<br>', '') in list(ROH_DICT.keys()) else (
                     int(d['range'][1] / 10) + 1 if d['range'][1] <= 1000 else int(d['range'][1] / 100) + 1),
                 1 if d['label'].replace('<br>', '') in list(ROH_DICT.keys()) else (
                     int(d['range'][1]/1000) if d['range'][1] > 1000 else (
                     1 if d['range'][1] <= 100 else 10))
             )[1]
             }
            for i, d in enumerate(fig.to_dict()["data"][0]["dimensions"])
        ]
    )

    leftmost_dimension = fig.data[-1]['dimensions'][0]

    ytick_dict = {leftmost_dimension['ticktext'][i]: 0.57 * leftmost_dimension['tickvals'][i]/(len(leftmost_dimension['ticktext'])-1) + 0.25 for i in range(len(leftmost_dimension['ticktext']))}
    fig = add_measure_buttons_PCP(fig, ytick_dict,
                              risk_owner_hazard, x_start=0.03, xanchor='left')

    # Replace the label of the first axis (index 0)
    fig.update_traces(dimensions=[
        go.parcoords.Dimension(
            range=dim['range'],
            label=' ' if i == 0 else dim['label'],  # Replace label of the first dimension
            values=dim['values'],
            tickvals=dim['tickvals'],  # Optional: Include tickvals if they exist
            ticktext=dim['ticktext']  # Optional: Include ticktext if they exist
        )
        for i, dim in enumerate(fig.data[0]['dimensions'])
    ])

    # Add an annotation for the legend
    fig.add_annotation(
        x=.5,  # Position at the start
        y=.95,  # Slightly above the plot
        text=" " if df_interaction is None else "<i>Colored lines: with interactions; Grey lines: without interaction</i>",  # Custom text
        showarrow=False,  # No arrow needed
        xref="paper",
        yref="paper",
        font=dict(size=FONTS['main'], color="black"),  # Make the font bold
        xanchor="center",
        yanchor="top",
    )

    # Add an image under the legend to the left
    base64_image = image_to_base64(f'{LEGENDS_LOCATION}/{risk_owner_hazard}_full_legend.png')
    fig.add_layout_image(
        dict(
            source=base64_image,
            # Replace with your image URL or path
            x=.5,  # Adjust x position (slightly right of the legend)
            y=.225,  # Adjust y position
            xref="paper",
            yref="paper",
            sizex=.8,  # Adjust size of the image
            sizey=.8,
            xanchor="center",
            yanchor="top"
        )
    )

    fig.add_annotation(
        x=0.0,  # Adjust this value to move the label left or right
        y=0.5,  # Adjust this value to move the label up or down
        text=f'{ROH_DICT_INV[risk_owner_hazard]} pathway options',  # Your y-axis label text here
        showarrow=False,
        xref='paper',
        yref='paper',
        textangle=-90,  # Rotate text for vertical orientation
        font=dict(size=FONTS['annotations']),  # Adjust font size as needed
        align='center'
    )

    fig.update_layout(
        # Title and positioning
        title={'text': add_line_breaks(figure_title, 80), 'y': .95, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'bottom'},
        title_font_size=FONTS['title'],
        font_size=FONTS['main'],

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
    fig.show()
    print(error)
    return fig