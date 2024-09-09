import plotly.express as px
import numpy as np
import plotly.graph_objects as go  # Import Plotly's graph_objects module
from scripts.helperfunctions.add_measure_buttons import add_measure_buttons
from scripts.map_system_parameters import AXIS_LABELS
from scripts.design_choices.main_dashboard_design_choices import COLORSCALE_HEATMAP, FONTS, FIG_DIMENSIONS
from scripts.design_choices.main_dashboard_dropdowns import ROH_DICT_INV
from scripts.helperfunctions.get_table_for_plot import get_table_for_plot_multi_risk
from scripts.main_central_path_directions import LEGENDS_LOCATION
from scripts.helperfunctions.add_line_breaks_axis_labels import add_line_breaks
from scripts.helperfunctions.images_as_base64 import image_to_base64
import json

def Heatmap(df, sectors_of_interest_list, figure_title):
    complete_replace_dict = {}
    for risk_owner_hazard in sectors_of_interest_list:
        complete_replace_dict[risk_owner_hazard] = {}
        with open(f'dynamic_data/data/renamed_pathways/renamed_pathways_{risk_owner_hazard}.json', 'r') as json_file:
            replace_dict = json.load(json_file)
        invert_replace_dict = {v: int(k) for k, v in replace_dict.items()}
        complete_replace_dict[risk_owner_hazard] = invert_replace_dict

    new_df = df.copy()

    # # Replace old values with new values in the 'risk_owner_hazard' column
    # for risk_owner_hazard in sectors_of_interest_list:
    #     new_df[risk_owner_hazard] = new_df[risk_owner_hazard].replace(complete_replace_dict[risk_owner_hazard])

    pivot_df, pivot_text_df = get_table_for_plot_multi_risk(new_df, sectors_of_interest_list)
    pivot_df = pivot_df.iloc[:, 1:]
    pivot_text_df = pivot_text_df.iloc[:, 1:]

    y_axis_values = pivot_df.index.values

    pivot_df = pivot_df.rename(columns=AXIS_LABELS)
    fig = go.Figure(data=go.Heatmap(
        z=pivot_df.round(1).values,  # Use normalized values for color
        x=[t for t in pivot_df.columns],  # Objective parameters
        y=y_axis_values.astype(str),  # Risk owner hazard
        text=pivot_text_df.astype(int).values,  # Original values for display
        texttemplate="%{text}",  # Display the text from 'text' in each cell
        hovertemplate="<b>Pathways Combination: %{y}</b><br>%{x}: %{text}<extra></extra>",  # Custom hover template
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

    # Update both axes and add annotations in a single update_layout call
    fig.update_layout(
        # X-Axis configuration
        xaxis=dict(
            domain=[0.17, .90]  # Adjust x-axis domain
        ),
        yaxis=dict(
            domain=[0.05, .83]  # Adjust x-axis domain
        ),
    )

    # Add cell borders by updating the trace
    fig.update_traces(
        xgap=1,  # horizontal gap between cells
        ygap=1  # vertical gap between cells
    )

    fig.add_annotation(
        x=0.0,  # Adjust this value to move the label left or right
        y=0.5,  # Adjust this value to move the label up or down
        text=add_line_breaks(f'Pathways Combination ({", ".join([ROH_DICT_INV[s] for s in sectors_of_interest_list])})',40),  # Your y-axis label text here
        showarrow=False,
        xref='paper',
        yref='paper',
        textangle=-90,  # Rotate text for vertical orientation
        font=dict(size=FONTS['annotations']),  # Adjust font size as needed
        align='center'
    )
    x_axis_range = [0, len(pivot_df.columns) + 1]
    # # Customize the x-tick labels
    fig.update_xaxes(
        tickvals=list(range(x_axis_range[0], x_axis_range[1])),
        ticktext=[add_line_breaks(t, 12) for t in pivot_df.columns]
    )

    # fig.update_yaxes(domain=[0.2, 1])  # Adjusting the domain can change the plotting area's height
    fig.update_layout(
        # Title and positioning
        title={'text': add_line_breaks(figure_title, 80), 'y': .95, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'bottom'},
        title_font_size=FONTS['title'],
        font_size=FONTS['main']-2,
        xaxis=dict(side='top'),
        xaxis_tickangle=-20,  # Optional: Rotate x-axis labels if needed
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
