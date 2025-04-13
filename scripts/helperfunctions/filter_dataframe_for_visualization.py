from scripts.main_central_path_directions import ROH_LIST
from scripts.map_system_parameters import SECTOR_OBJECTIVES
import pandas as pd
import json

def filter_dataframe_for_visualization(df, risk_owner_hazard, timehorizon, scenarios, robustness_metric, sector_focus=None):

    # Filter the dataframe based on selections
    if isinstance(scenarios,list):
        selected_scenarios = '&'.join(scenarios)
    else:
        selected_scenarios = scenarios
    if scenarios == 'Wp':
        print(df['scenario_of_interest'].unique(), selected_scenarios)
    if sector_focus is None:
        filtered_df = df[
            (df['year'].isin([int(timehorizon)])) &  # Assuming timehorizon is a single selection, not a list
            (df['scenario_of_interest'] == selected_scenarios) &
            (df['robustness_metric'].isin(robustness_metric)) &
            (df.objective_parameter.isin(SECTOR_OBJECTIVES[risk_owner_hazard]))
            ].copy()
        # print(ROH_LIST, filtered_df.pw_combi.str.split('_', expand=True))
        filtered_df[ROH_LIST] = filtered_df.pw_combi.str.split('_', expand=True)


        # Split 'pw_combi' column and expand into separate columns
        filtered_df.loc[:,ROH_LIST] = filtered_df[ROH_LIST].astype(int)

        # Identify columns in B not in A
        columns_to_drop = [column for column in ROH_LIST if column != risk_owner_hazard]

        # Drop these columns from the DataFrame
        filtered_df = filtered_df.drop(columns=columns_to_drop, errors='ignore')
    else:
        # print(timehorizon, selected_scenarios, robustness_metric, SECTOR_OBJECTIVES[risk_owner_hazard])
        # print(df[df['year'].isin([int(timehorizon)])].head())
        # print(df[df['scenario_of_interest'] == selected_scenarios].head())
        # print(df[df['robustness_metric'].isin(robustness_metric)].head())
        # print(df[df.objective_parameter.isin(SECTOR_OBJECTIVES[risk_owner_hazard])].head())
        filtered_df = df[
            (df['year'].isin([int(timehorizon)])) &  # Assuming timehorizon is a single selection, not a list
            (df['scenario_of_interest'] == selected_scenarios) &
            (df['robustness_metric'].isin(robustness_metric)) &
            (df.objective_parameter.isin(SECTOR_OBJECTIVES[risk_owner_hazard])
             # (pd.concat([df[key].isin(value) for key, value in sector_focus.items()], axis=1).all(axis=1))
             )
            ].copy()

    return filtered_df
