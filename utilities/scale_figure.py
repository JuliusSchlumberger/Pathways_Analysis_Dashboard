import json
from utilities.design_choices import FIGURE_WIDTH
from assets.static_inputs import FONTS
from PIL import Image

# def scale_figure(fig, viewport_data):
#     current_width = fig.layout.width
#     current_height = fig.layout.height
#
#     scaled_height = current_height
#     scaled_width = current_width
#
#     if current_height != None and current_width != None:
#         size = json.loads(viewport_data)
#         width, height = size['width'], size['height']
#         scale_factor = round(min(FIGURE_WIDTH / 12 * width / current_width, height * .8 / current_height),2) * 0.9  # Assuming 1920px is the standard width for full scale
#         # print(f'fig: {current_width}/{current_height}')
#         # print(f'screen: {width}/{height} - {FIGURE_WIDTH / 12 * width}/{height * .8}')
#         # print(f'scale_factor: {scale_factor} - {FIGURE_WIDTH / 12 * width / current_width}/{height * .8 / current_height}')
#         # print('scale_factor', FIGURE_WIDTH / 12 / 1280, height * .8, scale_factor, current_width, scaled_width, current_height, scaled_height)
#         # Scale the dimensions
#         scaled_width = current_width * scale_factor
#         scaled_height = current_height * scale_factor
#         fig.update_layout(
#             width=scaled_width,
#             height=scaled_height,
#             autosize=False,  # Ensure that the size is set explicitly based on scaled dimensions
#             title_font_size=FONTS['title'] * scale_factor,
#             font_size=FONTS['main'] * scale_factor,
#         )
#         # Scale annotation font sizes
#         if 'annotations' in fig.layout:
#             new_annotations = []
#             for annotation in fig.layout.annotations:
#                 if annotation.font:
#                     new_size = annotation.font.size * scale_factor if annotation.font.size else FONTS['annotations']
#                 else:
#                     new_size = FONTS['annotations'] * scale_factor  # Default font size if not set
#
#                 new_annotations.append(
#                     annotation.update(
#                         font=dict(
#                             size=new_size
#                         )
#                     )
#                 )
#             fig.update_layout(annotations=new_annotations)
#     return fig, scaled_height, scaled_width

def scale_figure(fig, storage):
    current_width = fig.layout.width
    current_height = fig.layout.height

    scaled_height = current_height
    scaled_width = current_width

    if current_height is not None and current_width is not None:
        size = storage['viewport_size']
        width, height = size['width'], size['height']
        scale_factor = round(min(FIGURE_WIDTH / 12 * width / current_width, height * 0.8 / current_height), 2) * 0.9

        # Scale the dimensions
        if scale_factor < 10.2:
            scaled_width = current_width * scale_factor
            scaled_height = current_height * scale_factor
            fig.update_layout(
                width=scaled_width,
                height=scaled_height,
                autosize=False,
                title_font_size=FONTS['title'] * scale_factor,
                font_size=FONTS['main'] * scale_factor,
            )

            # Scale annotation font sizes
            if 'annotations' in fig.layout:
                new_annotations = []
                for annotation in fig.layout.annotations:
                    if annotation.font:
                        new_size = annotation.font.size * scale_factor if annotation.font.size else FONTS['annotations']
                    else:
                        new_size = FONTS['annotations'] * scale_factor

                    new_annotations.append(
                        annotation.update(
                            font=dict(
                                size=new_size
                            )
                        )
                    )
                fig.update_layout(annotations=new_annotations)


    return fig, scaled_height, scaled_width

