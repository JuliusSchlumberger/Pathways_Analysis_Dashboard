import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scripts.map_system_parameters import MEASURE_DICT
from scripts.Legends.insert_linebreaks import insert_linebreak
import matplotlib.patches as patches
from scripts.design_choices.main_dashboard_design_choices import FIG_DIMENSIONS, FONTS
from scripts.design_choices.main_dashboard_dropdowns import ROH_DICT_INV



def create_full_overview_legend(legend_dict, max_items_per_col, filepath="full_legend_overview.png"):
    num_cols = len(list(legend_dict.keys())) * 2    # logo, description per risk owner hazard
    num_rows = max_items_per_col

    # Assuming a DPI of 100
    DPI = 100

    # Convert pixel dimensions to inches
    fig_width = FIG_DIMENSIONS['width'] / DPI
    fig_height = FIG_DIMENSIONS['height'] / DPI

    # Assuming num_rows and num_cols are defined
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(num_cols + 2, num_rows-1),
                            gridspec_kw={'width_ratios': [1.2, 4] * int(num_cols / 2)})

    # Hide all axes
    for ax in axs.flat:
        ax.axis('off')

    for column, roh in enumerate(list(legend_dict.keys())):
        legend_items = legend_dict[roh]
        for row, item in enumerate(legend_items):
            img = mpimg.imread(item['image_path'])

            axs[row, column*2].imshow(img)
            text = insert_linebreak(f"{MEASURE_DICT[item['name']]}", 15)

            # Set the text for the item
            axs[row, 2 * column + 1].text(-0.05, 0.5, text, va='center', ha='left', size=FONTS['main'])  # Adjust text alignment as needed

            if row == 0:
                axs[row, 2 * column].set_title(f'{ROH_DICT_INV[roh]}', ha='left', fontsize=FONTS['main'], fontweight="bold")
    fig.text(0.5, 0.93, 'Relevant Actor - Risk pairs and their considered measures', ha='center', va='center', fontsize=FONTS['title'])
    # Draw a rectangle around the figure
    plt.subplots_adjust(left=0.05, bottom=0.05)
    rect = patches.Rectangle((0.03, 0.03), .95,.94, linewidth=2, edgecolor='grey', facecolor='none',
                             transform=fig.transFigure,
                             clip_on=False)
    fig.patches.append(rect)

    #
    # plt.tight_layout()

    plt.savefig(filepath, bbox_inches='tight', dpi=DPI)
    plt.close()
    pass