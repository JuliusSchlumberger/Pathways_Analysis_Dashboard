import numpy as np
import pandas as pd
from scripts.design_choices.main_dashboard_dropdowns import ROH_DICT_INV,ROH_DICT, RANGE


# Define a function to thicken lines by creating variations of the data
def make_thicker_lines(df, dimensions_to_modify, max_adjustment, num_adjustment):
    combined_data = df.copy()
    for adjustment_factor in np.linspace(0, max_adjustment, num_adjustment):
        reset_pivot_modified_up = df.copy()
        reset_pivot_modified_down = df.copy()
        for dim in dimensions_to_modify:
            if df[dim].max() >= 1000:
                adjustment_factor_specific = adjustment_factor * 1.5
            elif df[dim].max() > 100:
                adjustment_factor_specific = adjustment_factor * 2
            elif df[dim].max() > 10:
                adjustment_factor_specific = adjustment_factor * 7
            else:
                adjustment_factor_specific = adjustment_factor

            range_adjustment = (df[dim].max() - df[dim].min()) * adjustment_factor_specific
            # range_adjustment = adjustment_factor_specific
            reset_pivot_modified_up[dim] += range_adjustment
            reset_pivot_modified_down[dim] -= range_adjustment

        combined_data = pd.concat([combined_data, reset_pivot_modified_up, reset_pivot_modified_down])
    return combined_data
