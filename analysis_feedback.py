import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
import math
from scripts.Legends.insert_linebreaks import insert_linebreak

# Permanently changes the pandas settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Define the list of IDs you want to filter by
filter_ids = [2,3,6,34,67,71,73,74,102]
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
       'interacting_sectors_robustness', 'coding', 'crop_loss', 'robustness',
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
'easy', 'confidence',
       'enough_information', 'scalability',
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



# quantitative_answers = {
#     'alternatives': ['pathway_number', 'f_resilient_crops', 'long_term', 'flexibility',],
#     'robustness': ['robustness_plot', 'coding', 'crop_loss', 'robustness', 'tradeoff', 'general_interactions', 'interaction_least_productivity_loss'],
#     'timing': ['first_measure', 'number_measures', 'most_flexible15', 'most_flexible4', 'timing_shifts', 'ditch_shift'],
#     'system_analysis': ['robustness_plot','system_analysis_pathways_1560', 'system_analysis_pathways_1530', 'system_analysis_pathways_which_better','system_analysis_performance_1560', 'system_analysis_performance_1530', 'system_analysis_performance_which_better',]
# }
#
# correct_answers = {
#     'alternatives': [7, 2, 'large_dikes', 'Flood_Resilient_Crops', ],
#     'robustness': ['robustness_plot', 'chaos', 60, [3,4], [0], 'synergies', [0,1,2,3,4,5,6], ],
#     'timing': [2052, 2, 'Flood_Resilient_Crops', 'Flood_Resilient_Crops', 'earlier', 3],
#     'system_analysis': ['robustness_plot', 2, 1,
#                         3, [10, 110, 150],
#                         [0, 20, 30 ], 3, ]
#
# }
subjective_fit_steps = {
    'alternatives': ['easy', 'confidence', 'enough_information', 'scalability'],
    'robustness': ['viztype_barchart',
       'viztype_pcp', 'viztype_heatmap', 'likkert_use-robustness_easy',
       'likkert_use-robustness_confidence',
       'likkert_use-robustness_enough_information',
       'likkert_use-robustness_scalability'],   # 'coding' is missing becuase i need to manually add that.
    'timing': ['viztype_pathways', 'likkert_use-pathways_maps_easy',
       'likkert_use-pathways_maps_confidence',
       'likkert_use-pathways_maps_enough_information',
       'likkert_use-pathways_maps_scalability'],
    'system_analysis': ['system_analysis_pathways_easy', 'system_analysis_performance_easy',
       'system_analysis_pathways_confidence',
       'system_analysis_performance_confidence',
       'system_analysis_pathways_enough_information',
       'system_analysis_performance_enough_information',
       'system_analysis_pathways_scalability',
       'system_analysis_performance_scalability']}
quantitative_answers = {
    'alternatives': ['pathway_number', 'f_resilient_crops', 'long_term', 'flexibility',],
    'robustness': ['crop_loss', 'robustness', 'tradeoff', 'general_interactions', 'interaction_least_productivity_loss'],   # 'coding' is missing becuase i need to manually add that.
    'timing': ['first_measure', 'number_measures', 'most_flexible15', 'most_flexible4', 'timing_shifts', 'ditch_shift'],
    'system_analysis': ['system_analysis_pathways_1560', 'system_analysis_pathways_1530', 'system_analysis_pathways_which_better','system_analysis_performance_1560', 'system_analysis_performance_1530', 'system_analysis_performance_which_better',]
}

questions = {
'alternatives': [
       'How many pathway alternatives do you have?',
       'How many alternative pathways start with measure "flood resilient crops"?',
       'Which measure is considered most often as the long-term measure (being implemented at a later stage)?',
       'Which first implemented measure offers the most flexibility with regards to future options?',
       ],
    'robustness': [
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
    'system_analysis': [
       'Looking at Pathways Maps with the pathway combination Farmer Flood - Pathway 1, Farmer - Drought Pathway 5, Municipality - Flood Pathway 6 and Shipping - Drought Pathway 0: how many measures  are implemented for Farmer - Flood Pathway 1 in a 4 \u2103 climate scenario?',
       'Looking at Pathways Maps with the pathway combination Farmer Flood - Pathway 1, Farmer - Drought Pathway 5, Municipality - Flood Pathway 3 and Shipping - Drought Pathway 0: how many measures  are implemented for Farmer - Flood Pathway 1 in a 4 \u2103 climate scenario?',
       'Which of the two considered Municipality Flood Pathways is more attractive from a Farmer - Flood perspective in a 4 \u2103 climate scenario?',
       'Looking at Pathways Performance with the pathway combination Farmer Flood - Pathway 1, Farmer - Drought Pathway 5, Municipality - Flood Pathway 6 and Shipping - Drought Pathway 0: what are the expected Farmer - Flood Costs in a 4 \u2103 climate scenario?',
       'Looking at Pathways Maps with the pathway combination Farmer Flood - Pathway 1, Farmer - Drought Pathway 5, Municipality - Flood Pathway 3 and Shipping - Drought Pathway 0: what are the expected Farmer - Flood Costs in a 4 \u2103 climate scenario?',
       'Which of the two considered Municipality Flood Pathways is more attractive from a Farmer - Flood perspective in a 4 \u2103 climate scenario?',]

}

correct_answers = {
    'alternatives': [7, 2, 'large_dikes', 'Flood_Resilient_Crops', ],
    'robustness': [60, [3,4], [0], 'synergies', [0,1,2,3,4,5,6,7], ],
    'timing': [2052, 2, 'Flood_Resilient_Crops', 'Flood_Resilient_Crops', 'earlier', 3],
    'system_analysis': [2, 1,
                        3, [10, 110, 150],
                        [0, 20, 30 ], 3, ]

}


# Function to convert the string in 'data' column to a dictionary
def convert_to_dict(data_str):
    try:
        # Convert the string to a valid JSON object (dictionary)
        return json.loads(data_str)
    except json.JSONDecodeError:
        return {}

def load_relevant_data(fname, filter_ids):
    # Load CSV data into a DataFrame
    df = pd.read_csv(fname)

    # Filter the DataFrame by the 'id' column
    filtered_df = df[~df['id'].isin(filter_ids)]

    # Display the filtered DataFrame
    # Apply the function to convert the 'data' column into dictionaries
    filtered_df['data_dict'] = filtered_df['data'].apply(convert_to_dict)

    # Expand the dictionary into separate columns
    data_expanded = pd.json_normalize(filtered_df['data_dict'])

    # Merge the expanded data with the original DataFrame (excluding the 'data' and 'data_dict' columns)
    final_df = pd.concat([filtered_df.drop(columns=['data', 'data_dict']), data_expanded], axis=1)

    return final_df


# def calculate_correct_answer_ratios_and_plot(final_df, quantitative_answers, correct_answers, questions):
#     # Initialize an empty DataFrame to store the results
#     results = pd.DataFrame(index=final_df.index)
#
#     # Iterate over the keys of the dictionaries
#     for key in quantitative_answers:
#         # Get the columns to subset for the current key
#         columns = quantitative_answers[key]
#         correct_vals = correct_answers[key]
#         relevant_questions = questions[key]
#         # Ensure correct_vals and columns have the same length
#         if len(columns) != len(correct_vals):
#             raise ValueError(f"Mismatch between columns and correct answers for key '{key}'")
#
#         # Prepare for subplots
#         num_columns = len(columns)
#         fig, axs = plt.subplots(1, num_columns, figsize=(5 * num_columns, 5))
#         fig.suptitle(f"{key} (Total Rows: {len(final_df)})", fontsize=16)
#
#         # If there's only one subplot, convert axs to a list for consistency
#         if num_columns == 1:
#             axs = [axs]
#
#         # Iterate over each column
#         for idx, (col, correct_val, q) in enumerate(zip(columns, correct_vals, relevant_questions)):
#             correct_count = 0
#             partial_count = 0
#             wrong_count = 0
#             not_completed = False
#             ratios = []
#
#             # Iterate over each row in the DataFrame
#             for row_idx, row in final_df.iterrows():
#                 val = row[col]
#
#                 # Skip if the value is NaN, but only for scalar values, not lists or arrays
#                 if not isinstance(val, (list, np.ndarray)) and pd.isna(val):
#                     not_completed = True
#                     continue
#
#                 # Check the correctness
#                 if isinstance(correct_val, str):
#                     if val == correct_val:
#                         correct_count += 1
#                     else:
#                         wrong_count += 1
#
#                 elif isinstance(correct_val, int):
#                     if np.abs(int(val)) == np.abs(correct_val):
#                         correct_count += 1
#                     else:
#                         wrong_count += 1
#
#                 elif isinstance(correct_val, list):
#                     if isinstance(val, list):
#                         if set(val) == set(correct_val):
#                             correct_count += 1
#                         elif len(set(val) & set(correct_val)) > 0:
#                             partial_count += 1
#                         else:
#                             wrong_count += 1
#                     else:
#                         if val in correct_val:
#                             correct_count += 1
#                         else:
#                             wrong_count += 1
#
#             # Create a pie chart for this column
#             labels = ['Correct', 'Partially Correct', 'Wrong']
#             sizes = [correct_count, partial_count, wrong_count]
#             total_columns = correct_count + partial_count * 2 + wrong_count
#             colors = ['#66b3ff', '#ffcc99', '#ff9999']
#
#             axs[idx].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
#             axs[idx].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
#             axs[idx].set_title(f'{q} (n={total_columns})')
#
#             if not_completed:
#                 ratio = np.NaN
#             else:
#                 # Calculate the ratio of correct answers for the current row
#                 ratio = correct_count / total_columns
#             ratios.append(ratio)
#
#         plt.tight_layout(rect=[0, 0.03, 1, 0.95])
#         plt.savefig(f'figures/output_analysis/analysis_step_{key}_piecharts.png', dpi=300)
#
#         # Add the ratios as a new column in the results DataFrame
#         results[key] = ratios
#
#     return results

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



def analysis_step_pie_charts(final_df, quantitative_answers, correct_answers, questions):
    # Dictionary to store the data for pie chart values
    pie_data = {}

    # Iterate over the keys of the dictionaries
    for key in quantitative_answers:
        # Get the columns to subset for the current key
        columns = quantitative_answers[key]
        correct_vals = correct_answers[key]
        relevant_questions = questions[key]
        # Ensure correct_vals and columns have the same length
        if len(columns) != len(correct_vals):
            raise ValueError(f"Mismatch between columns and correct answers for key '{key}'")

        # Initialize a DataFrame to store the counts for this key
        pie_df = pd.DataFrame(columns=['Correct', 'Partially Correct', 'Wrong'], index=columns)

        # Iterate over each column
        for idx, (col, correct_val) in enumerate(zip(columns, correct_vals)):
            correct_count = 0
            partial_count = 0
            wrong_count = 0

            # Iterate over each row in the DataFrame
            for row_idx, row in final_df.iterrows():
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
        create_pie_charts(pie_df.T, relevant_questions)
        plt.savefig(f'figures/output_analysis/analysis_step_{key}_pies.png', dpi=300)


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

        # Iterate over each row in the DataFrame
        for idx, row in final_df.iterrows():
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
                    if key == 'robustness':
                        print(idx, col, val, correct_val)

                    # If the correct answer is a string, compare directly
                    if isinstance(correct_val, str):
                        if val == correct_val:
                            correct_count += 1

                    # If the correct answer is an integer, check if the absolute values are the same
                    elif isinstance(correct_val, int):
                        if np.abs(int(val)) == np.abs(correct_val):
                            correct_count += 1

                    # If the correct answer is a list, check for full or partial correctness
                    elif isinstance(correct_val, list):
                        if isinstance(val, list):
                            # Check for full match
                            if set(val) == set(correct_val):
                                correct_count += 1
                            # Check for partial match (intersection is not empty)
                            elif len(set(val) & set(correct_val)) > 0:
                                correct_count += 0.5
                        else:
                            # only the case for question where i did not specify which time horizon is of interest
                            if val in correct_val:
                                correct_count += 1
            if not_completed:
                ratio = np.NaN
            else:
                # Calculate the ratio of correct answers for the current row
                ratio = correct_count / total_columns
            ratios.append(ratio)

        # Add the ratios as a new column in the results DataFrame
        results[key] = ratios

    return results

def plot_parallel_coordinates(results_df, quantitative_answers):
    # Get the list of keys from quantitative_answers to use as axis labels
    axis_labels = list(quantitative_answers.keys())

    # Calculate the average across all rows
    avg_row = results_df.mean(axis=0)
    print(avg_row)

    # Set up the parallel coordinates plot
    plt.figure(figsize=(10, 6))

    # Plot each row in the results_df
    for idx, row in results_df.iterrows():
        plt.plot(axis_labels, row.values, color='blue', alpha=0.5)

    # Plot the average row with distinct color and thicker line
    plt.plot(axis_labels, avg_row, color='red', linewidth=3, label='Average')

    # Set the axis labels
    plt.xticks(rotation=45)
    plt.xlabel('Questions')
    plt.ylabel('Correct Answer Ratio')

    # Add a legend to distinguish the average line
    plt.legend()

    # Show the plot
    plt.title('Correctness of answers')
    plt.tight_layout()
    plt.savefig(f'figures/output_analysis/overview_objective_fit.png', dpi=300)

def calculate_number_inputs(df, allcolumns):
    for col in allcolumns:
        if col.startswith('completed_'):
            counter = len(df[df[col] == 'yes'])
            print(col, counter)

def create_subjective_fit_boxplots(results_df, columns_of_interest):
    for key in columns_of_interest:
        cols = columns_of_interest[key]
        # Step 1: Create a simplified DataFrame with signal words as columns
        signal_words = ['viztype', 'easy', 'confidence', 'information', 'scalability']
        simplified_df = pd.DataFrame(index=results_df.index)

        # Loop through the likkert_feedback to extract columns related to signal words
        for signal in signal_words:
            # Find columns from results_df that contain the signal word
            relevant_columns = [col for col in cols if signal in col.lower()]

            # If any columns were found, average them and add as a new column
            if relevant_columns:
                simplified_df[signal] = results_df[relevant_columns].mean(axis=1)
        simplified_df.rename(columns={'viztype': 'prior viz experience'})
        signal_words = ['prior viz experience', 'easy', 'confidence', 'information', 'scalability']
        # Step 2: Create a box-whisker plot from the simplified DataFrame
        plt.figure(figsize=(10, 6))
        # print(simplified_df)
        simplified_df.boxplot()
        #
        # Add labels and title to the plot
        plt.title('Box-Whisker Plot of Likert Feedback')
        plt.ylabel('Scores')
        plt.xlabel('Categories')
        plt.tight_layout()

        # Show the plot
        plt.savefig(f'figures/output_analysis/subjective_fit_{key}.png', dpi=300)

        # Step 3: Create the correlation matrix
        correlation_matrix = simplified_df.corr('spearman')

        # Step 4: Visualize the correlation matrix using Matplotlib
        plt.figure(figsize=(8, 6))

        # Create the heatmap using imshow
        heatmap = plt.imshow(correlation_matrix, interpolation='nearest', cmap='coolwarm', vmin=-1, vmax=1)

        # Add color bar
        plt.colorbar(heatmap)

        # Add labels for the axes
        plt.xticks(np.arange(len(signal_words)), signal_words, rotation=45)
        plt.yticks(np.arange(len(signal_words)), signal_words)

        # # Add correlation coefficients as text on the heatmap
        # for i in range(len(signal_words)):
        #     for j in range(len(signal_words)):
        #         plt.text(j, i, f"{correlation_matrix.iloc[i, j]:.2f}",
        #                  ha='center', va='center', color='black')

        # Add a title to the heatmap
        plt.title('Correlation Matrix')

        # Show the plot
        plt.tight_layout()
        plt.savefig(f'figures/output_analysis/subjective_fit_{key}_correlation.png', dpi=300)

def create_subjective_fit_overview(results_df):
    # Step 1: Create a simplified DataFrame with signal words as columns
    signal_words = ['viztype', 'easy', 'confidence', 'information', 'scalability']
    simplified_df = pd.DataFrame(index=results_df.index)

    # Loop through the likkert_feedback to extract columns related to signal words
    for signal in signal_words:
        # Find columns from results_df that contain the signal word
        relevant_columns = [col for col in results_df.columns if signal in col.lower()]

        # If any columns were found, average them and add as a new column
        if relevant_columns:
            simplified_df[signal] = results_df[relevant_columns].mean(axis=1)
    simplified_df.rename(columns={'viztype': 'prior viz experience'})
    signal_words = ['prior viz experience', 'easy', 'confidence', 'information', 'scalability']
    # Step 2: Create a box-whisker plot from the simplified DataFrame
    plt.figure(figsize=(10, 6))
    # print(simplified_df)
    # # simplified_df.boxplot()
    #
    # # Add labels and title to the plot
    # plt.title('Box-Whisker Plot of Likert Feedback')
    # plt.ylabel('Scores')
    # plt.xlabel('Categories')
    # Calculate the mean of each column to plot as a distinct line
    mean_values = simplified_df.mean()

    # Set up the parallel coordinates plot
    plt.figure(figsize=(10, 6))

    # Plot each row as a line in the parallel coordinates plot
    for idx, row in simplified_df.iterrows():
        plt.plot(signal_words, row.values, color='blue', alpha=0.5)

    # Plot the mean as a distinct line with a different color and thickness
    plt.plot(signal_words, mean_values, color='red', linewidth=3, label='Mean')

    # Set the axis labels
    plt.xticks(rotation=45)
    plt.xlabel('Categories')
    plt.ylabel('Scores')

    # Add a legend for the mean line
    plt.legend()

    # Show the plot
    plt.title('Overview subjective fit in relation to prior visualization experience')
    plt.tight_layout()

    # Show the plot
    plt.savefig(f'figures/output_analysis/overview_subjective_fit.png', dpi=300)

    # Step 3: Create the correlation matrix
    correlation_matrix = simplified_df.corr('spearman')

    # Step 4: Visualize the correlation matrix using Matplotlib
    plt.figure(figsize=(8, 6))

    # Create the heatmap using imshow
    heatmap = plt.imshow(correlation_matrix, interpolation='nearest', cmap='coolwarm', vmin=-1, vmax=1)

    # Add color bar
    plt.colorbar(heatmap)

    # Add labels for the axes
    plt.xticks(np.arange(len(signal_words)), signal_words, rotation=45)
    plt.yticks(np.arange(len(signal_words)), signal_words)

    # Add correlation coefficients as text on the heatmap
    for i in range(len(signal_words)):
        for j in range(len(signal_words)):
            plt.text(j, i, f"{correlation_matrix.iloc[i, j]:.2f}",
                     ha='center', va='center', color='black')

    # Add a title to the heatmap
    plt.title('Correlation Matrix')

    # Show the plot
    plt.tight_layout()
    plt.savefig(f'figures/output_analysis/overview_subjective_fit_correlation.png', dpi=300)

df = load_relevant_data(fname, filter_ids)
# print(df[qualitative_feedback])

create_subjective_fit_overview(df)

calculate_number_inputs(df, all_columns)

# analysis_step_pie_charts(df, quantitative_answers, correct_answers, questions)
create_subjective_fit_boxplots(df, columns_of_interest=subjective_fit_steps)

results = calculate_correct_answer_ratios(df, quantitative_answers, correct_answers)
plot_parallel_coordinates(results, quantitative_answers)