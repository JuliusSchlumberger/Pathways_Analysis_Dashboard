from scripts.main_central_path_directions import ROH_LIST
from scripts.map_system_parameters import SECTOR_OBJECTIVES

def get_table_for_plot(df, risk_owner_hazard):

    pivot_df = df.pivot_table(
        index=risk_owner_hazard,
        columns='objective_parameter',
        values='normalized_values',
        aggfunc='sum'  # or 'mean', 'max', etc., depending on the required aggregation
    )
    reset_pivot = pivot_df.reset_index()
    reset_pivot.index = reset_pivot[risk_owner_hazard]
    # print(reset_pivot)
    pivot_text_df = df.pivot_table(
        index=risk_owner_hazard,
        columns='objective_parameter',
        values='Value',
        aggfunc='sum'  # or 'mean', 'max', etc., depending on the required aggregation
    )

    text_reset_pivot = pivot_text_df.reset_index()
    text_reset_pivot.index = text_reset_pivot[risk_owner_hazard]
    return reset_pivot, text_reset_pivot

def make_table_and_adjustments(df, index, values, objective_parameters):
    pivot_df = df.pivot_table(
        index=index,
        columns='objective_parameter',
        values=values,
        # aggfunc='sum'  # or 'mean', 'max', etc., depending on the required aggregation
    )
    reset_pivot = pivot_df.reset_index()

    result = []
    [result.append(x) for x in objective_parameters if x not in result]

    new_order = [index, *result]
    reset_pivot = reset_pivot[new_order]

    reset_pivot[ROH_LIST] = reset_pivot.pw_combi.str.split('_', expand=True)

    # Split 'pw_combi' column and expand into separate columns
    reset_pivot.loc[:, ROH_LIST] = reset_pivot[ROH_LIST].astype(int)

    # Assume reset_pivot is your DataFrame and ROH_LIST contains the column names to check

    # Find columns where not all values are zero
    # non_zero_columns = [col for col in ROH_LIST if not (reset_pivot[col] == 0).all()]
    reset_pivot[index] = reset_pivot[ROH_LIST].apply(
        lambda row: ', '.join(row.astype(str)), axis=1
    )
    # print(non_zero_columns)  # This will contain the column names with non-zero values
    # print(error)
    reset_pivot.index = reset_pivot[index]
    reset_pivot = reset_pivot.drop(ROH_LIST, axis=1)
    return reset_pivot

def get_table_for_plot_multi_risk(df, sectors_of_interest_list):
    objective_parameters = [item for s in sectors_of_interest_list for item in SECTOR_OBJECTIVES[s]]
    values = 'normalized_values'
    reset_pivot = make_table_and_adjustments(df, 'pw_combi', values, objective_parameters)
    pivot_text_df = make_table_and_adjustments(df, 'pw_combi', 'Value', objective_parameters)

    return reset_pivot, pivot_text_df