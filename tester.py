import pandas as pd
import matplotlib.pyplot as plt


def plot_grouped_scatter(df, groups_dict):
    """
    Function to create a grouped scatter plot with custom annotations.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data. The first column should be the labels (y-axis), and the rest should be binary columns (x-axis).
    groups_dict (dict): A dictionary where keys are tuples containing group name and color, and values are lists of column names in that group.
                        Example: {('Group1', 'orange'): ['col1', 'col2'], ('Group2', 'green'): ['col3']}
    """
    # Define plot
    fig, ax = plt.subplots(figsize=(12, 8))

    # Extract y-axis labels from the first column of the DataFrame
    y_labels = df.iloc[:, 0]
    y = range(len(y_labels))

    # Define x-axis labels from the dictionary
    x_labels = []
    colors = []
    x_pos = []
    current_x = 0

    for (group_name, color), columns in groups_dict.items():
        x_labels.extend(columns)
        colors.extend([color] * len(columns))
        group_center = current_x + len(columns) / 2 - 0.5
        plt.text(group_center, len(y_labels) + 15.5, group_name, ha='center', fontsize=12, color=color)
        current_x += len(columns)
        x_pos.extend(range(current_x - len(columns), current_x))

    # Plot the scatter points
    for j, tool in enumerate(y):
        for i, col in enumerate(x_labels):
            if df.iloc[j, df.columns.get_loc(col)] == 1:
                ax.scatter(i, j, color=colors[i], s=100)

    # Set the ticks and labels
    ax.set_xticks(range(len(x_labels)))
    ax.set_xticklabels(x_labels, rotation=90, ha='center')
    ax.set_yticks(y)
    ax.set_yticklabels(y_labels)

    # Move the x-axis labels to the top
    ax.xaxis.tick_top()

    # Manually set the color of each x-axis label
    for i, label in enumerate(ax.get_xticklabels()):
        label.set_color(colors[i])

    # Add gridlines for better visibility
    ax.grid(True, linestyle='--', alpha=0.5)

    # Set labels for x and y axes
    ax.set_ylabel(df.columns[0])
    ax.set_xlabel('Categories')

    # Adjust the layout to ensure everything fits
    plt.subplots_adjust(top=0.6, bottom=0.05, left=0.45, right=0.95)
    fig.savefig('software_tools.png', dpi=300)
    plt.show()

# Example DataFrame
# data = {
#     "Tool": ["EMA Workbench", "Rhodium", "openMORDM", "PRIM (Python package)", "TMIP-EMAT", "PRIM (R package)",
#              "SALib", "scikit-learn", "ScenarioWizard", "Colorado River Basin Post-2026 Operations Exploration Tool",
#              "Colorado River Robustness Tradeoffs", "ARCH Resilience Pathways Visualization Tool",
#              "Adaptation Catalyst", "Pathways Generator"],
#     "Generation of Alternatives - Exploration": [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
#     "Generation of Alternatives - Search": [1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
#     "Generation of Alternatives - Prespecified": [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
#     "Generation of Alternatives - Iterative": [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     "Generation of Scenarios - Exploration": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
#     "Generation of Scenarios - Search": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
#     "Generation of Scenarios - Prespecified": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
#     "Robustness Evaluation - Regret": [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0],
#     "Robustness Evaluation - Satisficing": [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0],
#     "Vulnerability Analysis - Subspace Partitioning": [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0],
#     "Vulnerability Analysis - Sensitivity Analysis": [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0],
# }


# df = pd.DataFrame(data)
df = pd.read_excel('software_tools.xlsx')
print(df.nunique())
# # Group dictionary
groups_dict = {
    ('Scope', 'green'): [
        'Generation of Alternatives',
        'Generation of Scenarios',
        'Robustness Evaluation',
        'Vulnerability Analysis',
        'Raising awareness'
    ],
    ('Methods', 'blue'): [
        'RDM',
        'DAPP',
        'MCDA',
        'Info-Gap',
        'Decision Scaling'
    ],
    ('Level of Analysis', 'red'): [
        'Level 1 (qualitative)',
        'Level 2 (semi-quantiative)',
        'Level 3 (qualitative)'
    ],
    ('Audience', 'orange'): [
        'policy maker',
        'technical expert',
        'Project manager',
        'general public'
    ],
    ('', 'purple'): [
        'Case study example'
    ]
}

# groups_dict = {
#     ('Generation of Alternatives', 'orange'): [
#         'Generation of Alternatives - Exploration',
#         'Generation of Alternatives - Search',
#         'Generation of Alternatives - Prespecified',
#         'Generation of Alternatives - Iterative'
#     ],
#     ('Generation of Scenarios', 'green'): [
#         'Generation of Scenarios - Exploration',
#         'Generation of Scenarios - Search',
#         'Generation of Scenarios - Prespecified'
#     ],
#     ('Robustness Evaluation', 'blue'): [
#         'Robustness Evaluation - Regret',
#         'Robustness Evaluation - Satisficing'
#     ],
#     ('Vulnerability Analysis', 'red'): [
#         'Vulnerability Analysis - Subspace Partitioning',
#         'Vulnerability Analysis - Sensitivity Analysis'
#     ]
# }

# Call the function with the DataFrame and group dictionary
plot_grouped_scatter(df, groups_dict)
