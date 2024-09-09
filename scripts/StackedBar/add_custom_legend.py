from scripts.StackedBar.create_pattern_image import create_pattern_image
from scripts.main_central_path_directions import MARKERS_LOCATION
from scripts.helperfunctions.images_as_base64 import image_to_base64

def add_custom_legend(fig, marker_dict, risk_owner_hazard, x_start=1, y_start=1, y_step=-0.04):
    # Create and save images for each entry in marker_dict
    for name, (color, pattern) in marker_dict.items():
        if color is None and pattern is None:
            pass
        elif pattern is None:
            img = create_pattern_image(color, pattern)
            img.save(f"{MARKERS_LOCATION}/markers_{name}_{risk_owner_hazard}.png")
        else:
            pattern = pattern['shape']
            # print(color)
            # print('e', pattern)
            img = create_pattern_image(color, pattern)
            # img.show()
            img.save(f"{MARKERS_LOCATION}/markers_{name}_{risk_owner_hazard}.png")
    # Position for the custom legend

    # Add custom markers and text
    # Add custom markers and text using the saved images
    fig.add_annotation(
        x=x_start,  # Adjust this value to move the label left or right
        y=y_start,  # Adjust this value to move the label up or down
        text=f'Objectives',  # Your y-axis label text here
        showarrow=False,
        xref='paper',
        yref='paper',
        # textangle=-90,  # Rotate text for vertical orientation
        font=dict(size=14),  # Adjust font size as needed
        xanchor='left',
        yanchor='bottom'
    )
    # y_start = y_start + y_step

    for i, name in enumerate(marker_dict.keys()):
        y_position = y_start + i * y_step
        base64_image = image_to_base64(f"{MARKERS_LOCATION}/markers_{name}_{risk_owner_hazard}.png")
        fig.add_layout_image(
            dict(
                source=base64_image,
                xref="paper", yref="paper",
                x=x_start, y=y_position,
                sizex=0.03, sizey=0.03,
                xanchor="left", yanchor="top"
            )
        )
        fig.add_annotation(
            x=x_start + 0.02, y=y_position - 0.015,
            text=name.replace('_', ' '),
            showarrow=False,
            xanchor="left",
            yanchor="middle",
            xref="paper", yref="paper",
            font=dict(color="black", size=10)
        )
    return fig

def add_custom_legend_multi_risk(fig, marker_dict, sectors_of_interest_list, x_start=1, y_start=1, y_step=-0.04):
    # Create and save images for each entry in marker_dict
    for name, (color, pattern) in marker_dict.items():
        if color is None:
            pass
        else:
            img = create_pattern_image(color, None)
            img.save(f"{MARKERS_LOCATION}/markers_{name}.png")

    # Position for the custom legend

    # Add custom markers and text
    # Add custom markers and text using the saved images
    fig.add_annotation(
        x=x_start,  # Adjust this value to move the label left or right
        y=y_start,  # Adjust this value to move the label up or down
        text=f'Objectives',  # Your y-axis label text here
        showarrow=False,
        xref='paper',
        yref='paper',
        # textangle=-90,  # Rotate text for vertical orientation
        font=dict(size=14),  # Adjust font size as needed
        xanchor='left',
        yanchor='bottom'
    )
    # y_start = y_start + y_step

    for i, name in enumerate(marker_dict.keys()):
        y_position = y_start + i * y_step
        base64_image = image_to_base64(f"{MARKERS_LOCATION}/markers_{name}.png")
        fig.add_layout_image(
            dict(
                source=base64_image,
                xref="paper", yref="paper",
                x=x_start, y=y_position,
                sizex=0.03, sizey=0.03,
                xanchor="left", yanchor="top"
            )
        )
        fig.add_annotation(
            x=x_start + 0.02, y=y_position - 0.015,
            text=name.replace('_', ' '),
            showarrow=False,
            xanchor="left",
            yanchor="middle",
            xref="paper", yref="paper",
            font=dict(color="black", size=10)
        )
    return fig