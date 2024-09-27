import pandas as pd
from scripts.helperfunctions.add_measure_buttons import add_measure_buttons
from scripts.design_choices.main_dashboard_dropdowns import ROH_DICT_INV
from scripts.design_choices.main_dashboard_design_choices import FIG_DIMENSIONS, FONTS
from scripts.main_central_path_directions import LEGENDS_LOCATION
from scripts.map_system_parameters import NORMALIZATION_BENCHMARKS
from scripts.helperfunctions.get_table_for_plot import get_table_for_plot_multi_risk
from scripts.StackedBar.add_trace_one_bar import add_traces_oneBar_multi_risk
from scripts.StackedBar.add_custom_legend import add_custom_legend
from scripts.helperfunctions.images_as_base64 import image_to_base64
import plotly.graph_objects as go  # Import Plotly's graph_objects module
from scripts.helperfunctions.add_line_breaks_axis_labels import add_line_breaks
import json

# Permanently changes the pandas settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def Stacked_Bar_Plot(df, sectors_of_interest_list, figure_title):
    # Load the dictionary from the JSON file
    complete_replace_dict = {}
    for risk_owner_hazard in sectors_of_interest_list:
        complete_replace_dict[risk_owner_hazard] = {}
        with open(f'dynamic_data/data/renamed_pathways/renamed_pathways_{risk_owner_hazard}.json', 'r') as json_file:
            replace_dict = json.load(json_file)
        invert_replace_dict = {v: int(k) for k, v in replace_dict.items()}
        complete_replace_dict[risk_owner_hazard] = invert_replace_dict
    new_df = df.copy()

    # Replace old values with new values in the 'risk_owner_hazard' column
    # for risk_owner_hazard in sectors_of_interest_list:
    #     new_df[risk_owner_hazard] = new_df[risk_owner_hazard].replace(complete_replace_dict[risk_owner_hazard])


    pivot_df, pivot_text_df = get_table_for_plot_multi_risk(new_df, sectors_of_interest_list)

    fig = go.Figure()

    initial_traces, static_legend_entries = add_traces_oneBar_multi_risk(
        pivot_df, pivot_text_df,
        sectors_of_interest_list,
        offsetgroup=0, legend_entries={})
    for trace in initial_traces:
        fig.add_trace(trace)


    fig = add_custom_legend(fig, static_legend_entries, sectors_of_interest_list,  x_start=.66, y_start=.84, y_step=-0.04)
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
        ticktext=list(range(x_axis_range[0], x_axis_range[1]))
    )

    # Update both axes and add annotations in a single update_layout call
    fig.add_annotation(
        x=.5,  # Position at the start
        y=.049,  # Slightly above the plot
        text="<i>The shorter the bar(s), the better</i>",  # Custom text
        showarrow=False,  # No arrow needed
        xref="paper",
        yref="paper",
        font=dict(size=FONTS['main'], color="black"),  # Make the font bold
        xanchor="center",
        yanchor="top",
    )

    fig.update_layout(
        barmode='stack',
        # X-Axis configuration
        xaxis=dict(
            showticklabels=False,  # Hide x-tick labels
            # title_text='The shorter the bar(s), the better',  # Remove x-axis title
            range=x_axis_range,
            domain=[0.17, .65]  # Adjust x-axis domain
        ),
        yaxis=dict(
            domain=[0.1, .9]  # Adjust x-axis domain
        ),
    )

    fig.update_layout(
        showlegend=False
        )


    fig.update_layout(
        # Title and positioning
        title={'text': add_line_breaks(figure_title, 80), 'y': .95, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'bottom'},
        title_font_size=FONTS['title'],
        font_size=FONTS['main'],

        # Custom margins
        margin=dict(l=5, r=5, t=30, b=5),
        paper_bgcolor='rgba(0,0,0,0)',  # Make the plot background transparent
        plot_bgcolor='#f3f3f3',  # Make the plot area background transparent
        # xaxis=dict(
        #     showgrid=True,
        #     gridcolor='grey'  # Change x-axis grid line color to grey
        # ),
        # Fixed dimensions for the plot
        width=FIG_DIMENSIONS['width'],  # Width set to 1300 pixels
        height=FIG_DIMENSIONS['height'],  # Height set to 600 pixels
        autosize=False,  # Disable autosizing to use the specified width and height

    )
    # fig.show()
    # print(error)
    return fig