from scripts.DecisionTree.DecisionTree import decision_tree
from scripts.figures_pathways_robustness import *
from scripts.PathwaysMaps.generate_pathways_map import generate_pathways_map

from scripts.main_central_path_directions import FILTER_CONDITIONS, DIRECTORY_MEASURE_LOGOS, INPUT_ALTERNATIVES
from assets.static_inputs import (INTRO_TEXT, ROH_DICT, MEASURE_ALTERNATIVES, TIMEHORIZONS,
                                  SCENARIOS, WHICH_OPTIONS, ROBUSTNESS_METRICS, CUSTOM_HOVER, INTERACTIONS_static)
# from assets.static_inputs import INTRO_TEXT,  OPTION_DICT, INTERACTIONS_static, RANDOM_DEFAULT
import pathlib

from assets.static_inputs import CUSTOM_LEGEND_CHANGE



# Page B
# for risk_owner_hazard in ROH_DICT.values():
#     fig = decision_tree(f'{INPUT_ALTERNATIVES}{risk_owner_hazard}.txt', risk_owner_hazard,
#                                 DIRECTORY_MEASURE_LOGOS + '/colorized', FILTER_CONDITIONS[risk_owner_hazard])
#     pathlib.Path(f'figures_static/decision_tree/').mkdir(parents=True, exist_ok=True)
#     # fig.write_html(f"figures/decision_tree/alternative_pathways_{sector}.html")
#     fig.write_json(f"figures_static/decision_tree/alternative_pathways_{risk_owner_hazard}.json")

# Page C

# for t_option in TIMEHORIZONS:
#     for s_option in SCENARIOS:
#         for r_option in ROBUSTNESS_METRICS:
#             for f_option in WHICH_OPTIONS:
#                 for risk_owner_hazard in ROH_DICT.values():
#                     for i_option in INTERACTIONS_static[risk_owner_hazard]:
#                         i_option_value  = i_option[next(iter(i_option))]
#                         print(risk_owner_hazard, r_option, s_option, t_option, f_option,
#                               i_option_value
#                               )
#                         timehorizon = TIMEHORIZONS[t_option]
#                         scenario = SCENARIOS[s_option]
#                         robustness = ROBUSTNESS_METRICS[r_option]
#                         fig_type = WHICH_OPTIONS[f_option]
#
#                         if i_option_value != ['no_interactions']:
#                             interacting_sector_string = risk_owner_hazard + '&' + '&'.join(i_option_value)
#                             fig = pathways_robustness_with_interactions(scenario, fig_type,
#                                                                         risk_owner_hazard,
#                                                                         robustness, timehorizon,
#                                                                         interacting_sector_string)
#                             end_fig_name = f'_{interacting_sector_string}.html'
#                         else:
#                             fig = pathways_robustness(scenario, fig_type, risk_owner_hazard, robustness,
#                                                       timehorizon)
#                             end_fig_name = f'.html'
#
#                         if fig_type == 'StackedBar':
#                             # Convert the figure to an HTML string
#                             fig_html = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')
#
#                             # Custom JavaScript to be added
#                             custom_js = CUSTOM_LEGEND_CHANGE
#
#                             # Append the custom JavaScript to the HTML string
#                             fig_html_with_js = f"{fig_html}\n<script>{custom_js}</script>"
#
#                         pathlib.Path(f'figures_static/{fig_type}/{risk_owner_hazard}/').mkdir(
#                             parents=True, exist_ok=True)
#                         # fig.write_json(f'figures/{fig_type}/{risk_owner_hazard}/plot_{timehorizon}_{scenario}_{robustness}.json')
#                         fig.write_html(
#                             f'figures_static/{fig_type}/{risk_owner_hazard}/plot_{timehorizon}_{scenario}_{robustness}{end_fig_name}')

# Page D
for s_option in SCENARIOS:
    for r_option in ROBUSTNESS_METRICS:
        for risk_owner_hazard in ROH_DICT.values():
            for i_option in INTERACTIONS_static[risk_owner_hazard]:
                i_option_value = i_option[next(iter(i_option))]
                print(risk_owner_hazard, r_option, s_option,
                      i_option_value
                      )
                scenario = SCENARIOS[s_option]
                robustness = ROBUSTNESS_METRICS[r_option]
                i_option_value  = i_option[next(iter(i_option))]
                if i_option_value == ['no_interactions']:
                    fig = generate_pathways_map(scenario, risk_owner_hazard,
                                                interacting_sector_string=False)
                    end_fig_name = f'.html'
                    # figure_identifier = f'assets/figures/PathwaysMaps/{risk_owner_hazard}/pathways_map_{risk_owner_hazard}_{stored_data["scenarios"]}.json'
                else:
                    interacting_sector_string = risk_owner_hazard + '&' + '&'.join(i_option_value)
                    fig = generate_pathways_map(scenario, risk_owner_hazard,
                                                interacting_sector_string=interacting_sector_string)
                    end_fig_name = f'_{interacting_sector_string}.html'

                # Convert the figure to an HTML string
                fig_html = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')

                # Custom JavaScript to be added
                custom_js = CUSTOM_HOVER

                # Append the custom JavaScript to the HTML string
                fig_html_with_js = f"{fig_html}\n<script>{custom_js}</script>"
                pathlib.Path(f'figures_static/PathwaysMaps/{risk_owner_hazard}/').mkdir(
                                            parents=True, exist_ok=True)
                # fig.write_json(f'figures/{fig_type}/{risk_owner_hazard}/plot_{timehorizon}_{scenario}_{robustness}.json')
                fig.write_html(
                    f'figures_static/PathwaysMaps/{risk_owner_hazard}/plot_{scenario}_{robustness}{end_fig_name}')

# Page E