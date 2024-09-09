import plotly.graph_objects as go  # Import Plotly's graph_objects module
from scripts.design_choices.main_dashboard_dropdowns import ROH_DICT_INV, ROH_DICT
from scripts.map_system_parameters import SECTOR_OBJECTIVES
from scripts.design_choices.colors import SECTOR_OBJECTIVE_COLORS
from scripts.helperfunctions.add_line_breaks_axis_labels import add_line_breaks


def add_traces_oneBar(plot_objectives, sector_objectives, plot_df, text_df, text_df_benchmark, risk_owner_hazard, offsetgroup, legend_entries, groupname_base, interactions=None):
    group_entries = []
    traces = []
    # Iterate through each column

    # Dictionary to store the cumulative values for each group
    cumulative_values = {
        0: {'pos': {row: 0 for row in plot_df[risk_owner_hazard]},
            'neg': {row: 0 for row in plot_df[risk_owner_hazard]}},
        1: {'pos': {row: 0 for row in plot_df[risk_owner_hazard]},
            'neg': {row: 0 for row in plot_df[risk_owner_hazard]}},
        2: {'pos': {row: 0 for row in plot_df[risk_owner_hazard]},
            'neg': {row: 0 for row in plot_df[risk_owner_hazard]}}
        }

    for col in sorted(plot_objectives):
        # Iterate through each row to add individual traces
        for i in plot_df.index:
            if col in sector_objectives:
                if isinstance(text_df.at[i, col], float):
                    impact = text_df.at[i, col]
                else:
                    impact = text_df.at[i, col].unique()
                old_column_name = f'{col}_old'
                reference_case = [f'(without measures: {int(text_df_benchmark.at[0, col])})' if interactions is None else
                                f'(no interaction: {int(interactions.at[i, col])})'][0]

                hover_text = (
                    f"<b>{ROH_DICT_INV[risk_owner_hazard]} pathway {i}</b><br>"
                    f"{col.replace('_', ' ')}: {int(impact)} {reference_case}<extra></extra>"
                )
                groupname = groupname_base
            elif col.endswith('tradeoff'):
                obj_key = [column for column in sector_objectives if col.startswith(column)][0]
                hover_text = (
                    f"<b>{ROH_DICT_INV[risk_owner_hazard]} pathway {i}</b><br>"
                    f"interaction trade-off increasing {obj_key.replace('_', ' ')} by<br>"
                    f"{int(text_df_benchmark.at[i, col])}<extra></extra>"
                )
                groupname = 'Click here to show effective robustness (with interactions)'
            else:  # '_synergy'
                obj_key = [column for column in sector_objectives if col.startswith(column)][0]
                hover_text = (
                    f"<b>{ROH_DICT_INV[risk_owner_hazard]} pathway {i}</b><br>"
                    f"interaction synergy reducing {obj_key.replace('_', ' ')} by<br>"
                    f"{int(text_df_benchmark.at[i, col])}<extra></extra>"
                )
                groupname = 'Click here to show effective robustness (with interactions)'

            # Define the base objective
            base_objective = [objective for objective in sector_objectives if col.startswith(objective)]
            color = SECTOR_OBJECTIVE_COLORS[risk_owner_hazard][base_objective[0]]
            rgba_color_int = tuple(int(c * 255) for c in color)

            # Since you are using RGB, you need only the first 3 channels
            rgb_color = rgba_color_int[:3]
            pattern = dict(shape='/', bgcolor=rgb_color, fgcolor='white') if col.endswith('_tradeoff') else dict(shape='.',
                                                                                                            bgcolor=color,
                                                                                                             fgcolor='white') if col.endswith(
                '_synergy') else None

            # Calculate the base for stacking
            cumulative_values[offsetgroup]['pos'][i] += plot_df.at[i, col]

            # Determine if this legend entry has already been added
            showlegend = False

            if col not in legend_entries:
                legend_entries[col] = [rgb_color, pattern]
            if groupname == 'Click here to show effective robustness (with interactions)' and groupname not in group_entries:
                group_entries.append(groupname)
                showlegend = True
            # print(error)
            # Add individual trace for each row
            traces.append(go.Bar(
                name=groupname,
                x=[plot_df.at[i, col]],
                y=[str(plot_df.at[i, risk_owner_hazard])],
                offsetgroup=offsetgroup,
                orientation='h',

                customdata=[hover_text],
                # hoverinfo='text',
                marker=dict(color=f'rgb{rgb_color}', pattern=pattern),
                showlegend=showlegend,
                # name=custom_name,
                hoverinfo='none',  # Disable default hover info on the plot
                legendgroup=groupname  # Use legendgroup to separate legends
            ))
    return traces, legend_entries



def add_traces_oneBar_multi_risk(plot_df, text_df, sectors_of_interest_list, offsetgroup, legend_entries):
    traces = []
    objective_parameters = [item for s in sectors_of_interest_list for item in SECTOR_OBJECTIVES[s]]
    result = []
    [result.append(x) for x in objective_parameters if x not in result]

    plot_df['total'] = plot_df[result].sum(axis=1)
    plot_df = plot_df.sort_values('total', ascending=False)
    # print(errro)
    # Iterate through each column
    for col in result:
        if col == 'pw_combi':
            pass
        else:
            # Iterate through each row to add individual traces
            for i in plot_df.index:
                if isinstance(text_df.at[i, col], float):
                    impact = text_df.at[i, col]
                else:
                    impact = text_df.at[i, col].unique()
                measure_list = i.split(',')
                hover_text = (
                    f"<b>{'<br>'.join([f'{s}:  Pathway {measure_list[tick]}' for tick, s in enumerate(ROH_DICT)])}</b><br>"
                    f"{col.replace('_', ' ')}: {int(impact)}<extra></extra>"
                )

                # Define the base objective
                for key in SECTOR_OBJECTIVE_COLORS:
                    if col in SECTOR_OBJECTIVES[key]:
                        risk_owner_hazard = key
                    else:
                        pass
                color = SECTOR_OBJECTIVE_COLORS[risk_owner_hazard][col]
                rgba_color_int = tuple(int(c * 255) for c in color)

                rgb_color = rgba_color_int[:3]
                # Determine if this legend entry has already been added
                showlegend = False

                if col not in legend_entries:
                    legend_entries[col] = [rgb_color, None]

                # Add individual trace for each row
                traces.append(go.Bar(
                    # name=groupname,
                    x=[plot_df.at[i, col]],
                    y=[str(plot_df.at[i, 'pw_combi'])],
                    offsetgroup=offsetgroup,
                    orientation='h',

                    hovertemplate=hover_text,
                    # hoverinfo='text',
                    marker=dict(color=rgba_color_int),
                    showlegend=showlegend,
                    # name=custom_name,
                    # hoverinfo='none',  # Disable default hover info on the plot
                    # legendgroup=groupname  # Use legendgroup to separate legends
                ))
    return traces, legend_entries

