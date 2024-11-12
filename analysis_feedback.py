import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
import math
from scripts.Legends.insert_linebreaks import insert_linebreak
import ast
import seaborn as sns
from wordcloud import WordCloud

# Permanently changes the pandas settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Define the list of IDs you want to filter by
filter_ids = [1,2,3,4,5,6,34,67,71,73,74,75,102,104,105, 108, 109,110, 111,166, 232,233,265,332,333,334, 364,464,496,529,597, 602, 607,619,620, 621, 630, 661
              ]
fname = 'survey_table_september_responses.csv'

all_columns = ['id', 'user_id', 'existing_id', 'current_url', 'completed_introduction',
       'impairment', 'work', 'expertise', 'use_frequency', 'viztype_barchart',
       'viztype_pcp', 'viztype_heatmap', 'viztype_pathways',
       'risk_owner_hazard', 'interactions', 'pathway_number',
       'f_resilient_crops', 'long_term', 'flexibility', 'easy', 'confidence',
       'enough_information', 'scalability', 'alternative_challenge',
       'alternative_advantage', 'completed_alternative_pathways',
       'completed_pathways_robustness', 'timehorizon', 'scenarios',
       'robustness_metric', 'robustness_plot',
       'interacting_sectors_robustness', 'coding_correct', 'crop_loss', 'robustness',
       'tradeoff', 'general_interactions',
       'interaction_least_productivity_loss', 'likkert_use-robustness_easy',
       'likkert_use-robustness_confidence',
       'likkert_use-robustness_enough_information',
       'likkert_use-robustness_scalability', 'robustness_challenge',
       'robustness_advantage', 'sectoral_interactions_maps', 'first_measure',
       'number_measures', 'most_flexible15', 'most_flexible4', 'timing_shifts',
       'ditch_shift', 'likkert_use-pathways_maps_easy',
       'likkert_use-pathways_maps_confidence',
       'likkert_use-pathways_maps_enough_information',
       'likkert_use-pathways_maps_scalability', 'pathways_challenge',
       'pathways_advantage', 'completed_pathways_maps', 'viewport_size.width',
       'viewport_size.height', 'viewport_size', 'alternatives_easy',
       'alternatives_confidence', 'alternatives_enough_information',
       'alternatives_scalability', 'interacting_sectors', 'robustness_easy',
       'robustness_enough_information', 'robustness_enough_informationn',
       'robustness_scalability', 'pathways_maps_easy',
       'pathways_maps_confidence', 'pathways_maps_enough_information',
       'pathways_maps_scalability', 'pathway_flood_agr', 'pathway_drought_agr',
       'pathway_flood_urb', 'pathway_drought_shp', 'system_analysis_focus',
       'system_analysis_pathways_1560', 'system_analysis_pathways_1530',
       'system_analysis_pathways_which_better',
       'system_analysis_performance_1560', 'system_analysis_performance_1530',
       'system_analysis_performance_which_better',
       'system_analysis_pathways_easy', 'system_analysis_performance_easy',
       'system_analysis_pathways_confidence',
       'system_analysis_performance_confidence',
       'system_analysis_pathways_enough_information',
       'system_analysis_performance_enough_information',
       'system_analysis_pathways_scalability',
       'system_analysis_performance_scalability', 'system_analysis_challenge',
       'system_analysis_advantage', 'completed_system_analysis',
       'drop_down_option.Heatmap']

context_ids = ['impairment', 'work', 'expertise', 'use_frequency', 'viztype_barchart',
       'viztype_pcp', 'viztype_heatmap', 'viztype_pathways',]
qualitative_feedback = ['alternative_challenge', 'alternative_advantage',
                        'robustness_challenge', 'robustness_advantage',
                        'pathways_challenge', 'pathways_advantage',
                        'system_analysis_challenge', 'system_analysis_advantage'
                        ]
not_sure_what_they_are = ['interactions', ]
likkert_feedback = [
'alternatives_easy',  'alternatives_confidence',  'alternatives_enough_information',  'alternatives_scalability',
'likkert_use-robustness_easy',
       'likkert_use-robustness_confidence',
       'likkert_use-robustness_enough_information',
       'likkert_use-robustness_scalability',
'likkert_use-pathways_maps_easy',
       'likkert_use-pathways_maps_confidence',
       'likkert_use-pathways_maps_enough_information',
       'likkert_use-pathways_maps_scalability',
'system_analysis_pathways_easy', 'system_analysis_performance_easy',
       'system_analysis_pathways_confidence',
       'system_analysis_performance_confidence',
       'system_analysis_pathways_enough_information',
       'system_analysis_performance_enough_information',
       'system_analysis_pathways_scalability',
       'system_analysis_performance_scalability',
]


subjective_fit_steps = {
    'alternatives': ['alternatives_easy',  'alternatives_confidence',  'alternatives_enough_information',  'alternatives_scalability'],
    'robustness': ['viztype_barchart',
       'viztype_pcp', 'viztype_heatmap', 'robustness_easy',
       'robustness_confidence',
       'robustness_enough_information',
       'robustness_scalability', 'robustness_plot'],
    'timing': ['viztype_pathways', 'pathways_maps_easy',
       'pathways_maps_confidence',
       'pathways_maps_enough_information',
       'pathways_maps_scalability'],
    'system_analysis_performance': ['system_analysis_performance_easy',
       'system_analysis_performance_confidence',
       'system_analysis_performance_enough_information',
       'system_analysis_performance_scalability',  'robustness_plot'],
    'system_analysis_pathways': ['system_analysis_pathways_easy',
                                    'system_analysis_pathways_confidence',
                                    'system_analysis_pathways_enough_information',
                                    'system_analysis_pathways_scalability',
                                 ]
}
quantitative_answers = {
    'alternatives': ['pathway_number', 'f_resilient_crops', 'long_term', 'flexibility',],
    'robustness': ['coding_correct', 'crop_loss', 'robustness', 'tradeoff', 'general_interactions', 'interaction_least_productivity_loss'],   # 'coding' is missing becuase i need to manually add that.
    'timing': ['first_measure', 'number_measures', 'most_flexible15', 'most_flexible4', 'timing_shifts', 'ditch_shift'],
    'system_analysis_performance': ['system_analysis_performance_1560', 'system_analysis_performance_1530', 'system_analysis_performance_which_better',],
'system_analysis_pathways': ['system_analysis_pathways_1560', 'system_analysis_pathways_1530', 'system_analysis_pathways_which_better']

}

questions = {
'alternatives': [
       'How many pathway alternatives do you have?',
       'How many alternative pathways start with measure "flood resilient crops"?',
       'Which measure is considered most often as the long-term measure (being implemented at a later stage)?',
       'Which first implemented measure offers the most flexibility with regards to future options?',
       ],
    'robustness': [
        'What do the colors represent in the figure?',
       'How much Crop Productivity Loss [%] do we expect for Pathway 5 over a time horizon of 60 years in the 4 \u2103 climate scenario  with no pathway interactions considered?',
       'In the 4 \u2103 climate change scenario, which pathway(s) is most robust at the time horizon of 60 years  with no pathway interactions considered?',
       'Which pathway(s) results in the highest Impacted Lifestock after 100 years in a 1.5 \u2103 climate scenario with no pathway interactions considered?',
       'When accounting for the presence of Farmer - Drought interactions, do we experience more synergy or more trade-off effects in a 1.5 \u2103 climate scenario over the next 60 years?',
       'When accounting for the presence of Farmer - Drought strategies, which pathway(s) show the best robustness regarding Crop Productivity Loss in a 4 \u2103 climate scenario over the next 60 years?'
       ],
    'timing': ['In which year is the first measure needed in a 1.5 \u2103 climate scenario with no pathway interactions considered?',
       'What is the maximum number of measures that need to be implemented in one pathway in a 1.5 \u2103 climate scenario over the 100 years with no pathway interactions considered?',
       'In a 1.5 \u2103 climate scenario, which first implemented measure offers the most flexibility with regards to future options?',
       'In a 4 \u2103 climate scenario, which first implemented measure offers the most flexibility with regards to future options?',
       'When accounting for the presence of Farmer - Drought interactions, what is the general effect on the timing of measure implementation compared to the case without interactions in a 4 \u2103 climate scenario?',
       'When accounting for the presence of Farmer - Drought interactions, by how many years does the implementation of "Large Dike elevation increase" in pathway 6 shift in a 4 \u2103 climate scenario compared to the case without interactions (use negative values if implementation takes place earlier, otherwise positive values)?',
        ],
    'system_analysis_performance': [
       'Looking at Pathways Performance with the pathway combination Farmer Flood - Pathway 1, Farmer - Drought Pathway 5, Municipality - Flood Pathway 6 and Shipping - Drought Pathway 0: what are the expected Farmer - Flood Costs in a 4 \u2103 climate scenario?',
       'Looking at Pathways Performance with the pathway combination Farmer Flood - Pathway 1, Farmer - Drought Pathway 5, Municipality - Flood Pathway 3 and Shipping - Drought Pathway 0: what are the expected Farmer - Flood Costs in a 4 \u2103 climate scenario?',
       'Which of the two considered Municipality Flood Pathways is more attractive from a Farmer - Flood perspective in a 4 \u2103 climate scenario?',],
'system_analysis_pathways': [
       'Looking at Pathways Maps with the pathway combination Farmer Flood - Pathway 1, Farmer - Drought Pathway 5, Municipality - Flood Pathway 6 and Shipping - Drought Pathway 0: how many measures  are implemented for Farmer - Flood Pathway 1 in a 4 \u2103 climate scenario?',
       'Looking at Pathways Maps with the pathway combination Farmer Flood - Pathway 1, Farmer - Drought Pathway 5, Municipality - Flood Pathway 3 and Shipping - Drought Pathway 0: how many measures  are implemented for Farmer - Flood Pathway 1 in a 4 \u2103 climate scenario?',
       'Which of the two considered Municipality Flood Pathways is more attractive from a Farmer - Flood perspective in a 4 \u2103 climate scenario?',]

}

correct_answers = {
    'alternatives': [7, 2, 'large_dikes', 'Flood_Resilient_Crops', ],
    'robustness': ['y', 60, [3,4], [0], 'synergies', [0,1,2,3,4,5,6,7], ],
    'timing': [2052, 2, 'Flood_Resilient_Crops', 'Flood_Resilient_Crops', 'earlier', 3],
    'system_analysis_performance': [[10, 110, 150],
                        [0, 20, 30 ], 3, ],
'system_analysis_pathways': [2, 1,
                        3]

}


# Function to convert the string in 'data' column to a dictionary
def convert_to_dict(data_str):
    try:
        # Convert the string to a valid JSON object (dictionary)
        return json.loads(data_str)
    except json.JSONDecodeError:
        return {}

def convert_str_to_list(df):
    # Iterate through all rows and columns of the DataFrame
    for col in df.columns:
        for idx, val in df[col].items():
            # Check if the value is a string that looks like a list (starts with [ and ends with ])
            if isinstance(val, str) and val.startswith('[') and val.endswith(']'):
                try:
                    # Convert string representation of list to an actual list
                    df.at[idx, col] = ast.literal_eval(val)
                except (ValueError, SyntaxError):
                    print(f"Error converting {val} to a list at index {idx}, column {col}")
    return df

def load_relevant_data(fname, filter_ids):
    # Load CSV data into a DataFrame
    df = pd.read_csv(fname)

    # Filter the DataFrame by the 'id' column
    filtered_df = df.copy()
    # filtered_df = df[~df['id'].isin(filter_ids)]

    # Display the filtered DataFrame
    # Apply the function to convert the 'data' column into dictionaries
    filtered_df['data_dict'] = filtered_df['data'].apply(convert_to_dict)

    # Expand the dictionary into separate columns
    data_expanded = pd.json_normalize(filtered_df['data_dict'])

    # Merge the expanded data with the original DataFrame (excluding the 'data' and 'data_dict' columns)
    final_df = pd.concat([filtered_df.drop(columns=['data', 'data_dict']), data_expanded], axis=1)
    final_df_filtered = final_df[~final_df['id'].isin(filter_ids)].reset_index()
    final_df_filtered = final_df_filtered.rename(columns={'robustness_enough_information': 'robustness_confidence'})
    final_df_filtered = final_df_filtered.rename(columns={'robustness_enough_informationn': 'robustness_enough_information'})

    final_df_filtered.to_excel('survey_results_table_clean(3).xlsx')



def create_pie_charts(df, relevant_questions):
    # Calculate the number of rows and columns needed
    max_cols = 4  # Max subplots per row
    num_cols = len(df.columns)
    num_rows = math.ceil(num_cols / max_cols)  # Automatically calculate the rows

    # Create subplots
    fig, axes = plt.subplots(nrows=num_rows, ncols=max_cols, figsize=(12, 6 * num_rows))

    # Flatten axes for easy iteration (handles cases where nrows > 1)
    axes = axes.flatten()

    # Plot pie charts in each subplot
    for i, (col, ax, q) in enumerate(zip(df.columns, axes, relevant_questions)):
        df[col].plot.pie(ax=ax, autopct='%1.1f%%', startangle=90)
        ax.set_title(f'{insert_linebreak(q,20)} (n={df[col].sum()})')
        ax.set_ylabel('')  # Remove y-label for better appearance

    # Remove any unused subplots (if columns < max_cols * num_rows)
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])


def create_heatmap(df_dict, questions, quantitative_answers, expertise):
    for key in quantitative_answers:
        relevant_questions = questions[key]
        # create all plot no distinction between viztypes
        all_df = df_dict['all'][key]
        # # Ensure df and relevant_questions have the same length
        # if len(df) != len(relevant_questions):
        #     raise ValueError("The number of relevant questions should match the number of columns in the dataframe.")

        all_df['sum'] = all_df.sum(axis=1)
        number_entries = all_df['sum'].values[0]
        print(number_entries)
        # Divide all columns except 'sum' by 'sum'
        df_normalized = all_df.drop(columns=['sum']).div(all_df['sum'], axis=0).astype(float)

        # Create a heatmap
        plt.figure(figsize=(12, 6))  # Adjust the figure size based on the data
        print(df_normalized)

        # Use seaborn heatmap, set relevant_questions as y labels
        sns.heatmap(df_normalized, annot=True, fmt=".1f", cmap="Blues", cbar=False,
                    xticklabels=df_normalized.columns, yticklabels=[insert_linebreak(q, 80) for q in relevant_questions])
        # Move x-axis labels to the top
        plt.tick_params(axis='x', which='both', top=True, bottom=False, labeltop=True, labelbottom=False)
        plt.subplots_adjust(left=0.6)  # Increase left margin

        title_dict = {
            'alternatives': 'pathways options analysis',
            'robustness': 'performance robustness analysis' ,
            'timing': 'decision-timing analysis',
            'system_analysis_pathways': 'system pathways analysis',
            'system_analysis_performance': 'system performance robustness analysis',
        }

        plt.title(f'Objective fit evaluation for {title_dict[key]} (n={number_entries})')
        plt.tight_layout()
        plt.savefig(f'figures/output_analysis/{expertise}/analysis_step_{key}_objective_fit.png', dpi=300)
        plt.close()
        plt.clf()
        if key == 'robustness' or key == 'system_analysis_performance':
            different_types = ['PCP', 'StackedBar', 'Heatmap']
            fig, axes = plt.subplots(figsize=(12, 6), nrows=1, ncols=len(different_types), sharey=True)
            for i, type in enumerate(different_types):
                all_df = df_dict[type][key]

                all_df['sum'] = all_df.sum(axis=1)
                number_entries = all_df['sum'].values[0]
                print(number_entries)
                # Divide all columns except 'sum' by 'sum'
                df_normalized = all_df.drop(columns=['sum']).div(all_df['sum'], axis=0).astype(float)

                # Use seaborn heatmap, set relevant_questions as y labels
                sns.heatmap(df_normalized, ax=axes[i], annot=True, fmt=".1f", cmap="Blues", cbar=False,
                            xticklabels=df_normalized.columns,
                            yticklabels=[insert_linebreak(q, 60) for q in relevant_questions],
                            linewidth=.5,
                            vmin=0, vmax=1)
                # Move x-axis labels to the top
                axes[i].tick_params(axis='x', which='both', top=True, bottom=False, labeltop=True, labelbottom=False)
                axes[i].set_title(f'{type} (n={number_entries})')
            # sns.set()
            plt.subplots_adjust(left=0.47)  # Increase left margin

            fig.suptitle(f'Objective fit evaluation for {title_dict[key]}')
            plt.tight_layout()
            plt.savefig(f'figures/output_analysis/{expertise}/analysis_step_{key}_objective_fit.png', dpi=300)
            plt.close()
            plt.clf()

def analysis_step_pie_charts(final_df, quantitative_answers, correct_answers, questions, expertise):

    all_data = {}
    # Iterate over the keys of the dictionaries
    for viztype in ['all', 'PCP', 'StackedBar', 'Heatmap']:
        # Dictionary to store the data for pie chart values
        pie_data = {}
        if viztype == 'all':
            considered_df = final_df.copy()
        else:
            considered_df = final_df[final_df['robustness_plot'] == viztype]
        for key in quantitative_answers:
            # Get the columns to subset for the current key
            columns = quantitative_answers[key]
            correct_vals = correct_answers[key]
            relevant_questions = questions[key]
            # Ensure correct_vals and columns have the same length
            if len(columns) != len(correct_vals):
                raise ValueError(f"Mismatch between columns and correct answers for key '{key}'")

            # Initialize a DataFrame to store the counts for this key
            pie_df = pd.DataFrame(columns=['Correct', 'Part. Correct', 'Wrong'], index=columns)

            # Iterate over each column
            for idx, (col, correct_val) in enumerate(zip(columns, correct_vals)):
                correct_count = 0
                partial_count = 0
                wrong_count = 0

                # Iterate over each row in the DataFrame
                for row_idx, row in considered_df.iterrows():
                    val = row[col]

                    # Skip if the value is NaN, but only for scalar values, not lists or arrays
                    if not isinstance(val, (list, np.ndarray)) and pd.isna(val):
                        continue

                    # Check the correctness
                    if isinstance(correct_val, str):
                        if val == correct_val:
                            correct_count += 1
                        else:
                            wrong_count += 1

                    elif isinstance(correct_val, int):
                        if np.abs(int(val)) == np.abs(correct_val):
                            correct_count += 1
                        else:
                            wrong_count += 1

                    elif isinstance(correct_val, list):
                        if isinstance(val, list):
                            if set(val) == set(correct_val):
                                correct_count += 1
                            elif len(set(val) & set(correct_val)) > 0:
                                partial_count += 1
                            else:
                                wrong_count += 1
                        else:
                            if val in correct_val:
                                correct_count += 1
                            else:
                                wrong_count += 1

                # Store the results for this column in the pie_df DataFrame
                pie_df.loc[col] = [correct_count, partial_count, wrong_count]

            # Store the pie_df in the pie_data dictionary
            pie_data[key] = pie_df
        all_data[viztype] = pie_data
    create_heatmap(all_data,questions, quantitative_answers, expertise)



def calculate_correct_answer_ratios(final_df, quantitative_answers, correct_answers):
    # Initialize an empty DataFrame to store the results
    results = pd.DataFrame(index=final_df.index)

    # Iterate over the keys of the dictionaries
    for key in quantitative_answers:
        # Get the columns to subset for the current key
        columns = quantitative_answers[key]
        correct_vals = correct_answers[key]

        # Ensure correct_vals and columns have the same length
        if len(columns) != len(correct_vals):
            raise ValueError(f"Mismatch between columns and correct answers for key '{key}'")

        # List to store the correct answer ratios for each row
        ratios = []
        expert_types = []

        # Iterate over each row in the DataFrame
        for idx, row in final_df.iterrows():
            expert_type = row.expert_group
            correct_count = 0
            total_columns = len(columns)
            not_completed = False
            # Iterate over each column and its corresponding correct answer
            for col, correct_val in zip(columns, correct_vals):
                val = row[col]
                # Skip if the value is NaN, but only for scalar values, not lists or arrays
                if not isinstance(val, (list, np.ndarray)) and pd.isna(val):
                    not_completed = True
                    continue
                else:
                    # If the correct answer is a string, compare directly
                    if isinstance(correct_val, str):
                        if val == correct_val:
                            print(idx, col, val, correct_val, 'string correct')
                            correct_count += 1
                        else:
                            print(idx, col, val, correct_val, 'string not correct')

                    # If the correct answer is an integer, check if the absolute values are the same
                    elif isinstance(correct_val, int):
                        if np.abs(int(val)) == np.abs(correct_val):
                            print(idx, col, val, correct_val, 'int correct')
                            correct_count += 1
                        else:
                            print(idx, col, val, correct_val, 'int not correct')

                    # If the correct answer is a list, check for full or partial correctness
                    elif isinstance(correct_val, list):
                        if isinstance(val, list):
                            # Check for full match
                            if set(val) == set(correct_val):
                                print(idx, col, val, correct_val, 'list correct')
                                correct_count += 1
                            # Check for partial match (intersection is not empty)
                            elif len(set(val) & set(correct_val)) > 0:
                                print(idx, col, val, correct_val, 'partially correct')
                                correct_count += 0.5
                            else:
                                print(idx, col, val, correct_val, 'list not correct')
                        else:
                            # only the case for question where i did not specify which time horizon is of interest
                            if val in correct_val:
                                correct_count += 1
                                print(idx, col, val, correct_val, 'special correct')
                            else:
                                print(idx, col, val, type(val), correct_val, 'special not correct')
                    else:
                        print(idx, col, val, correct_val, 'not correct')
            if not_completed:
                ratio = np.NaN
            else:
                # Calculate the ratio of correct answers for the current row
                ratio = correct_count / total_columns
            ratios.append(ratio)
            expert_types.append(expert_type)

        # Add the ratios as a new column in the results DataFrame
        results[key] = ratios
    results['system_analysis'] = (results['system_analysis_performance'] + results['system_analysis_pathways'])/2
    results = results.drop(['system_analysis_performance', 'system_analysis_pathways'], axis=1)
    results['expert_group'] = expert_types
    return results

def violinplots(results_df, quantitative_answers, expertise):

    fig = plt.figure()
    plt.grid()
    results_df = results_df.rename(
        columns={'alternatives': 'pathways options', 'robustness': 'performance', 'system_analysis':'system analysis'})
    df_all = results_df.drop('expert_group', axis=1)
    df_long = pd.melt(df_all, var_name='analysis', value_name='value')

    df_long['value'] = df_long['value'] * 100
    sns.swarmplot(data=df_long, x="analysis", y="value", color='tab:gray', zorder=0)

    # Plot the average row with distinct color and thicker line
    axis_labels = ['pathways options', 'performance', 'timing', 'system analysis']
    if expertise == 'all':
        for expert in results_df.expert_group.unique():
            results_subgroup = results_df[results_df.expert_group == expert].drop('expert_group', axis=1)
            label_dict = {'dmdu': f'Avg. for DMDU experts (n={len(results_subgroup)})',
                          'ccadrr': f'Avg. for Adaptation/DRM experts (n={len(results_subgroup)})',
                          'other': f'Avg. for non-experts  (n={len(results_subgroup)})'}
            marker_dict = {'dmdu': f'D',
                           'ccadrr': 's',
                           'other': 'v'}
            color_dict = {'dmdu': f'tab:blue',
                          'ccadrr': 'tab:orange',
                          'other': 'tab:green',
                          'all': 'tab:red'}

            avg_row = results_subgroup.mean(axis=0) * 100
            print(avg_row)
            plt.plot(axis_labels, avg_row, linewidth=2, label=label_dict[expert], marker=marker_dict[expert],color=color_dict[expert], zorder=10)
    else:
        label_dict = {'dmdu': f'Avg. for DMDU experts (n={len(results_df)})',
                      'ccadrr': f'Avg. for Adaptation/DRM experts (n={len(results_df)})',
                      'other': f'Avg. for non-experts  (n={len(results_df)})'}
        marker_dict = {'dmdu': f'D',
                       'ccadrr': 's',
                       'other': 'v'}
        color_dict = {'dmdu': f'tab:blue',
                      'ccadrr': 'tab:orange',
                      'other': 'tab:green',
                      'all': 'tab:red'}
        avg_row = df_all.mean(axis=0) * 100
        print(avg_row)
        plt.plot(axis_labels, avg_row, linewidth=2, label=label_dict[expertise], color=color_dict[expertise], marker=marker_dict[expertise], zorder=10)
    # Set y-axis ticks to be every 0.1
    plt.yticks(np.arange(0, 110, 10))
    plt.ylabel('Percentage of correct answers [%]')
    plt.xlabel('Analysis step')


    plt.legend()
    # Show the plot
    plt.title('Objective fit of Dashboard')
    plt.tight_layout()
    plt.savefig(f'figures/output_analysis/{expertise}/overview_objective_fit.png', dpi=300)
    plt.close()
    plt.clf()


def create_swarm_one_plot(signal_words, cols, results_df, key, expertise):
    all_columns = []
    # Loop through the likkert_feedback to extract columns related to signal words
    for signal in signal_words:
        # Find columns from results_df that contain the signal word
        relevant_columns = [col for col in cols if signal in col.lower()]
        all_columns.append(relevant_columns)

    relevant_cols = [col[0] for col in all_columns]
    simplified_df = results_df[relevant_cols]

    simplified_df.columns = ['easy', 'confident', 'enough information', 'use again']
    simplified_df = simplified_df.dropna()
    df_long = pd.melt(simplified_df, var_name='analysis', value_name='value')
    fig = plt.figure()
    sns.swarmplot(data=df_long, x="analysis", y="value", color='tab:gray', zorder=0)
    avg_row = simplified_df.mean(axis=0)
    number_inputs = len(simplified_df)
    # Plot the average row with distinct color and thicker line
    label_dict = {'dmdu': f'Avg. for DMDU experts',
                  'ccadrr': f'Avg. for Adaptation/DRM experts',
                  'other': f'Avg. for non-experts',
                  'all': 'Avg. for all participants'}
    marker_dict = {'dmdu': f'D',
                   'ccadrr': 's',
                   'other': 'v',
                   'all': 'o'}
    color_dict = {'dmdu': f'tab:blue',
                   'ccadrr': 'tab:orange',
                   'other': 'tab:green',
                  'all': 'tab:red'}
    title_dict = {
        'alternatives': 'Subjective fit for analysis of pathways options',
        'robustness': 'Subjective fit for analysis of pathways performance robustness',
        'timing': 'Subjective fit for analysis of pathway maps',
        'system_analysis_pathways': 'Subjective fit for analysis of system pathways options',
        'system_analysis_performance': 'Subjective fit for analysis of system performance robustness',
    }
    
    plt.plot(['easy', 'confident', 'enough information', 'use again'], avg_row, color=color_dict[expertise], linewidth=2, label=label_dict[expertise], marker=marker_dict[expertise], zorder=10)
    plt.title(f'{title_dict[key]} (n= {number_inputs})')
    plt.grid()
    plt.ylabel('Scores')
    plt.xlabel('Categories')
    plt.legend()
    plt.tight_layout()

    return fig

def create_swarm_with_subplots(signal_words, cols, results_df, key, expertise ):
    all_columns = []
    # Loop through the likkert_feedback to extract columns related to signal words
    for signal in signal_words:
        # Find columns from results_df that contain the signal word
        relevant_columns = [col for col in cols if signal in col.lower()]
        all_columns.append(relevant_columns)

    relevant_cols = [col[0] for col in all_columns if col]
    print(relevant_cols)
    simplified_df = results_df[relevant_cols]
    simplified_df.columns = ['easy', 'confident', 'enough information', 'use again', 'plot_type']
    # Melt the dataframe, keeping 'plot_type' separate and combining the other four columns into 'analysis'
    df_long = pd.melt(simplified_df, id_vars=['plot_type'], var_name='analysis', value_name='value')
    fig = plt.figure()

    unique_plot_types = ['PCP', 'StackedBar', 'Heatmap']
    # Create a figure and subplots
    fig, axes = plt.subplots(nrows=1, ncols=len(unique_plot_types), figsize=(15, 5), sharey=True, sharex=True)

    label_dict = {'dmdu': f'Avg. for DMDU experts',
                  'ccadrr': f'Avg. for Adaptation/DRM experts',
                  'other': f'Avg. for non-experts',
                  'all': 'Avg. for all participants'}
    marker_dict = {'dmdu': f'D',
                   'ccadrr': 's',
                   'other': 'v',
                   'all': 'o'}
    color_dict = {'dmdu': f'tab:blue',
                  'ccadrr': 'tab:orange',
                  'other': 'tab:green',
                  'all': 'tab:red'}
    title_dict = {
        'alternatives': 'Subjective fit for analysis of pathways options',
        'robustness': 'Subjective fit for analysis of pathways performance robustness',
        'timing': 'Subjective fit for analysis of pathway maps',
        'system_analysis_pathways': 'Subjective fit for analysis of system pathways options',
        'system_analysis_performance': 'Subjective fit for analysis of system performance robustness',
    }

    # Loop through each unique 'plot_type' and create a subplot
    for i, plot_type in enumerate(unique_plot_types):
        # Subset the dataframe for the current 'plot_type'
        subset_df = df_long[df_long['plot_type'] == plot_type]

        # Create a swarmplot for the current subset
        sns.swarmplot(data=subset_df, x="analysis", y="value", ax=axes[i], color='tab:gray', zorder=0)

        avg_row = simplified_df[simplified_df.plot_type == plot_type]
        avg_row = avg_row.dropna()
        number_inputs = len(avg_row)
        avg_row = avg_row.drop(columns=['plot_type']).mean(axis=0)

        # Plot the average row with distinct color and thicker line
        axes[i].plot(['easy', 'confident', 'enough information', 'use again'], avg_row, color=color_dict[expertise], linewidth=2, label=label_dict[expertise], marker=marker_dict[expertise], zorder=10)

        # Set title for each subplot
        axes[i].set_title(f'{plot_type} (n= {number_inputs})')
        axes[i].grid()
        axes[i].set_ylabel('Scores')
        axes[i].set_xlabel('Categories')
    plt.legend()
    plt.suptitle(title_dict[key])
    plt.tight_layout()

    return fig

def create_subjective_fit_boxplots(results_df, columns_of_interest, expertise):
    for key in columns_of_interest:
        print(key)
        cols = columns_of_interest[key]
        # Step 1: Create a simplified DataFrame with signal words as columns
        if key == "robustness" or key == "system_analysis_performance":
            if key == 'system_analysis_performance':
                signal_words = ['performance_easy', 'performance_confidence', 'performance_enough_information', 'performance_scalability', 'robustness_plot']
            else:
                signal_words = ['easy', 'confidence', 'information', 'scalability', 'robustness_plot']
            fig = create_swarm_with_subplots(signal_words, cols, results_df, key, expertise)
        else:
            if key == 'system_analysis_pathways':
                signal_words = ['pathways_easy', 'pathways_confidence', 'pathways_enough_information',
                                'pathways_scalability']
            else:
                signal_words = ['easy', 'confidence', 'information', 'scalability']
            fig = create_swarm_one_plot(signal_words, cols, results_df, key, expertise)

        # Show the plot
        plt.savefig(f'figures/output_analysis/{expertise}/subjective_fit_{key}.png', dpi=300)
        plt.close()
        plt.clf()


def make_word_cloud(expertise_text_updated, expertise):
    # Generate a word cloud with the updated text
    wordcloud_updated = WordCloud(width=800, height=400, background_color='white').generate(expertise_text_updated)

    # Display the word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud_updated, interpolation='bilinear')
    plt.axis('off')
    # plt.show()
    plt.tight_layout()
    plt.savefig(f'figures/output_analysis/{expertise}/word_cloud_expertise.png', dpi=300)

def create_subjective_fit_overview(results_df, expertise):

    # Step 1: Create a simplified DataFrame with signal words as columns
    signal_words = ['easy', 'confidence', 'information', 'scalability']
    simplified_df = pd.DataFrame(index=results_df.index)

    # Loop through the likkert_feedback to extract columns related to signal words
    for signal in signal_words:
        # Find columns from results_df that contain the signal word
        relevant_columns = [col for col in results_df.columns if signal in col.lower()]

        # If any columns were found, average them and add as a new column
        if relevant_columns:
            simplified_df[signal] = results_df[relevant_columns].mean(axis=1)
        simplified_df['expert_group'] = results_df['expert_group']
    simplified_df = simplified_df.rename(columns={'confidence': 'confident', 'information': 'enough information', 'scalability': 'use again'})
    signal_words = ['easy', 'confident', 'enough information', 'use again']
    # Step 2: Create a box-whisker plot from the simplified DataFrame
    fig = plt.figure()
    df_all = simplified_df.drop('expert_group', axis=1)
    df_long = pd.melt(df_all, var_name='analysis', value_name='value')
    sns.swarmplot(data=df_long, x="analysis", y="value", color='tab:gray', zorder=0)

    if expertise == 'all':
        print(simplified_df)
        for expert in results_df.expert_group.unique():
            print(expert)
            results_subgroup = simplified_df[simplified_df.expert_group == expert].drop('expert_group', axis=1)
            print(results_subgroup)
            label_dict = {'dmdu': f'Avg. for DMDU experts (n={len(results_subgroup)})',
                          'ccadrr': f'Avg. for Adaptation/DRM experts (n={len(results_subgroup)})',
                          'other': f'Avg. for non-experts  (n={len(results_subgroup)})'}
            marker_dict = {'dmdu': f'D',
                          'ccadrr': 's',
                          'other': 'v'}
            color_dict = {'dmdu': f'tab:blue',
                          'ccadrr': 'tab:orange',
                          'other': 'tab:green',
                          'all': 'tab:red'}

            mean_values = results_subgroup.mean()
            print(mean_values)
            plt.plot(signal_words, mean_values, linewidth=2, label=label_dict[expert], marker=marker_dict[expert], color=color_dict[expert], zorder=10)
    else:
        label_dict = {'dmdu': f'Avg. for DMDU experts (n={len(results_df)})',
                      'ccadrr': f'Avg. for Adaptation/DRM experts (n={len(results_df)})',
                      'other': f'Avg. for non-experts  (n={len(results_df)})'}
        mean_values = df_all.mean()
        print(mean_values)
        plt.plot(signal_words, mean_values, color='red', linewidth=2, label=label_dict[expertise], zorder=10)

    plt.xlabel('Categories')
    plt.ylabel('Scores')

    # Add a legend for the mean line
    plt.legend()
    plt.grid()
    # Show the plot
    plt.title('Subjective fit of Dashboard')
    plt.tight_layout()

    # Show the plot
    plt.savefig(f'figures/output_analysis/{expertise}/overview_subjective_fit.png', dpi=300)
    plt.close()

    # # Step 3: Create the correlation matrix
    # correlation_matrix = simplified_df.corr('spearman')
    #
    # # Step 4: Visualize the correlation matrix using Matplotlib
    # plt.figure(figsize=(8, 6))
    #
    # # Create the heatmap using imshow
    # heatmap = plt.imshow(correlation_matrix, interpolation='nearest', cmap='coolwarm', vmin=-1, vmax=1)
    #
    # # Add color bar
    # plt.colorbar(heatmap)
    #
    # # Add labels for the axes
    # plt.xticks(np.arange(len(signal_words)), signal_words, rotation=45)
    # plt.yticks(np.arange(len(signal_words)), signal_words)
    #
    # # Add correlation coefficients as text on the heatmap
    # for i in range(len(signal_words)):
    #     for j in range(len(signal_words)):
    #         plt.text(j, i, f"{correlation_matrix.iloc[i, j]:.2f}",
    #                  ha='center', va='center', color='black')
    #
    # # Add a title to the heatmap
    # plt.title('Correlation Matrix')
    #
    # # Show the plot
    # plt.tight_layout()
    # plt.savefig(f'figures/output_analysis/{expertise}/overview_subjective_fit_correlation.png', dpi=300)

fname = 'survey_table_september_responses(3).csv'
# load_relevant_data(fname, filter_ids)
# print(error)
for expertise in ['all', 'dmdu', 'ccadrr', 'other']:
    print("expertse", expertise)
    df = pd.read_excel('survey_results_table_clean_evaluated(3).xlsx')
    df = convert_str_to_list(df)
    if expertise != 'all':
        df = df[df.expert_group == expertise]

    # Split the column on ',' or ';', flatten the resulting lists into a single list of strings
    split_strings = df['expertise'].replace('"', '').replace("'", '').str.split('[,;]', expand=False).apply(lambda x: [item.strip() for item in x]).sum()
    multiline_string = '"""\n' + '\n'.join(split_strings) + '\n"""'
    # print(multiline_string)

    make_word_cloud(multiline_string, expertise)

    results = calculate_correct_answer_ratios(df, quantitative_answers, correct_answers)

    violinplots(results, quantitative_answers, expertise)
    create_subjective_fit_overview(df, expertise)

    # Individual steps analysis
    analysis_step_pie_charts(df, quantitative_answers, correct_answers, questions, expertise)
    create_subjective_fit_boxplots(df, columns_of_interest=subjective_fit_steps, expertise=expertise)