from scripts.main_central_path_directions import LEGENDS_LOCATION
from scripts.helperfunctions.images_as_base64 import image_to_base64
def add_measure_buttons(fig, y_ticks, risk_owner_hazard, x_start=0.23, xref='paper', yref='y', xanchor='left'):
    for tick, y_tick in enumerate(y_ticks.values):
        img_path = f'{LEGENDS_LOCATION}/{risk_owner_hazard}/colorized/{risk_owner_hazard}_pathway_{str(y_tick)}_ylabel.png'

        base64_image = image_to_base64(img_path)
        fig.add_layout_image(
            dict(
                source=base64_image,
                xref=xref,  # Use "paper" for relative positioning
                yref=yref,  # Use axis ID for aligning with specific ticks
                x=x_start,  # Adjust this value to position the image on the x-axis
                y=tick,  # Align with a specific y-axis tick label
                sizex=.7,
                sizey=.7,
                xanchor=xanchor,
                yanchor="middle",
            ),
        )
    return fig

def add_measure_buttons_PCP(fig, y_ticks, risk_owner_hazard, x_start=0.23, xref='paper', yref='paper', xanchor='left'):
    for y_tick in y_ticks.keys():
        img_path = f'{LEGENDS_LOCATION}/{risk_owner_hazard}/colorized/{risk_owner_hazard}_pathway_{str(y_tick)}_ylabel.png'

        base64_image = image_to_base64(img_path)
        fig.add_layout_image(
            dict(
                source=base64_image,
                xref=xref,  # Use "paper" for relative positioning
                yref=yref,  # Use axis ID for aligning with specific ticks
                x=x_start,  # Adjust this value to position the image on the x-axis
                y=y_ticks[y_tick],  # Align with a specific y-axis tick label
                sizex=.15,
                sizey=.15,
                xanchor=xanchor,
                yanchor="middle",
            ),
        )
    return fig