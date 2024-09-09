import plotly.express as px
import numpy as np
import plotly.graph_objects as go  # Import Plotly's graph_objects module
from scripts.helperfunctions.add_measure_buttons import add_measure_buttons
from scripts.map_system_parameters import AXIS_LABELS
from scripts.design_choices.main_dashboard_design_choices import COLORSCALE_HEATMAP, FONTS, FIG_DIMENSIONS
from scripts.design_choices.main_dashboard_dropdowns import ROH_DICT_INV
from scripts.helperfunctions.get_table_for_plot import get_table_for_plot
from scripts.main_central_path_directions import LEGENDS_LOCATION
from scripts.helperfunctions.add_line_breaks_axis_labels import add_line_breaks
from scripts.helperfunctions.images_as_base64 import image_to_base64
import json

def Heatmap(df, risk_owner_hazard, sector_objectives, figure_title, df_interaction=None):
    with open(f'dynamic_data/data/renamed_pathways/renamed_pathways_{risk_owner_hazard}.json', 'r') as json_file:
        replace_dict = json.load(json_file)
    invert_replace_dict = {v: int(k) for k, v in replace_dict.items()}

    new_df = df.copy()

    # Replace old values with new values in the 'risk_owner_hazard' column
    new_df[risk_owner_hazard] = new_df[risk_owner_hazard].replace(invert_replace_dict)

    pivot_df, pivot_text_df = get_table_for_plot(new_df, risk_owner_hazard)
    pivot_df = pivot_df.iloc[:, 1:]
    pivot_text_df = pivot_text_df.iloc[:, 1:]

    y_axis_values = pivot_df.index.values

    if df_interaction is None:
        pivot_df = pivot_df.rename(columns=AXIS_LABELS)
        fig = go.Figure(data=go.Heatmap(
            z=pivot_df.round(1).values,  # Use normalized values for color
            x=[add_line_breaks(t, 12) for t in pivot_df.columns],  # Objective parameters
            y=y_axis_values.astype(str),  # Risk owner hazard
            text=pivot_text_df.astype(int).values,  # Original values for display
            texttemplate="%{text}",  # Display the text from 'text' in each cell
            hoverinfo="text",  # Show only the text on hover
            colorscale=COLORSCALE_HEATMAP,  # Use the custom colorscale
            zmin=0.0,
            zmax=1.0,
            colorbar=dict(tickvals=[0.1, 0.3, 0.5, 0.7, 0.9],
                          ticktext=['Highest', 'High', 'Medium', 'Low', 'Lowest'],
                          title='Robustness',
                          x=.9,
                          len=0.6,  # Length of the colorbar
                          y=0.25,  # Center the colorbar vertically
                          yanchor='bottom',  # Align the colorbar by its middle
                          )),
        )

    if df_interaction is not None:
        print(len(df_interaction))
        # Replace old values with new values in the 'risk_owner_hazard' column
        df_interaction_new = df_interaction.copy()
        df_interaction_new[risk_owner_hazard] = df_interaction_new[risk_owner_hazard].replace(invert_replace_dict)

        pivot_df_interactions, pivot_text_df_interactions = get_table_for_plot(df_interaction_new, risk_owner_hazard)
        pivot_df_interactions = pivot_df_interactions.iloc[:, 1:]
        pivot_text_df_interactions = pivot_text_df_interactions.iloc[:, 1:]

        pivot_df_interactions = pivot_df_interactions.rename(columns=AXIS_LABELS)
        updated_text = pivot_text_df_interactions.astype(int).astype(str) + ' (' + pivot_text_df.astype(int).astype(str) + ')\u002a'

        fig = go.Figure(data=go.Heatmap(
            z=pivot_df_interactions.round(1).values,  # Use normalized values for color
            x=[add_line_breaks(t, 12) for t in pivot_df_interactions.columns],  # Objective parameters
            y=y_axis_values.astype(str),  # Risk owner hazard
            # text=updated_text.values,  # Original values for display
            text=updated_text,
            texttemplate="%{text}",  # Display the text from 'text' in each cell
            hoverinfo="text",  # Show only the text on hover
            colorscale=COLORSCALE_HEATMAP,  # Use the custom colorscale
            zmin=0.0,
            zmax=1.0,
            colorbar=dict(tickvals=[0.1, 0.3, 0.5, 0.7, 0.9],
                          ticktext=['Highest','High', 'Medium', 'Low', 'Lowest'],
                          title='Robustness',
                          x=.9,
                          len=0.6,  # Length of the colorbar
                          y=0.25,  # Center the colorbar vertically
                          yanchor='bottom',  # Align the colorbar by its middle
                          )), # Adjusts the colorbar length to 70% of the figure heighy
        )


    # Update both axes and add annotations in a single update_layout call
    fig.update_layout(
        # X-Axis configuration
        xaxis=dict(
            domain=[0.2, .89]  # Adjust x-axis domain
        ),
        yaxis=dict(
            domain=[0.25, .85]  # Adjust x-axis domain
        ),
    )

    # Add cell borders by updating the trace
    fig.update_traces(
        xgap=3,  # horizontal gap between cells
        ygap=3  # vertical gap between cells
    )

    fig = add_measure_buttons(fig, pivot_df.index.astype(str), risk_owner_hazard, x_start=0.04)

    # Add an image under the legend to the left
    base64_image = image_to_base64(f'{LEGENDS_LOCATION}/{risk_owner_hazard}_full_legend.png')
    fig.add_layout_image(
        dict(
            source=base64_image,
            # Replace with your image URL or path
            x=.5,  # Adjust x position (slightly right of the legend)
            y=.2,  # Adjust y position
            xref="paper",
            yref="paper",
            sizex=.8,  # Adjust size of the image
            sizey=.8,
            xanchor="center",
            yanchor="top"
        )
    )

    fig.add_annotation(
        x=.0,  # Adjust this value to move the label left or right
        y=0.55,  # Adjust this value to move the label up or down
        text=f'{ROH_DICT_INV[risk_owner_hazard]} pathway options',  # Your y-axis label text here
        showarrow=False,
        xref='paper',
        yref='paper',
        textangle=-90,  # Rotate text for vertical orientation
        font=dict(size=FONTS['annotations']),  # Adjust font size as needed
        align='center'
    )

    if df_interaction is not None:
        fig.add_annotation(
            x=.5,  # Position at the start
            y=.249,  # Slightly above the plot
            text="<i>* Explanation: with interactions (without interactions)</i>",  # Custom text
            showarrow=False,  # No arrow needed
            xref="paper",
            yref="paper",
            font=dict(size=FONTS['main'], color="black"),  # Make the font bold
            xanchor="center",
            yanchor="top",
        )

    # fig.update_yaxes(domain=[0.2, 1])  # Adjusting the domain can change the plotting area's height
    fig.update_layout(
        # Title and positioning
        title={'text': add_line_breaks(figure_title, 80), 'y': .95, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'bottom'},
        title_font_size=FONTS['title'],
        font_size=FONTS['main'],
        xaxis=dict(side='top'),
        # Custom margins
        margin=dict(l=5, r=5, t=30, b=5),
        paper_bgcolor='rgba(0,0,0,0)',  # Make the plot background transparent
        plot_bgcolor='#f3f3f3',  # Make the plot area background transparent
        # Fixed dimensions for the plot
        width=FIG_DIMENSIONS['width'],  # Width set to 1300 pixels
        height=FIG_DIMENSIONS['height'],  # Height set to 600 pixels
        autosize=False,  # Disable autosizing to use the specified width and height
    )  # Adjust figure size

    return fig
