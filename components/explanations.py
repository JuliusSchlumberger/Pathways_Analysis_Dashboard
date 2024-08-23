from dash import html
from utilities.create_modal import create_modal, create_modal_with_image

# Word explanations
pathways_explanation = create_modal(
    "pathways_explanation",
    "Pathways",
    [
        html.P("Adaptation pathways are flexible plans that outline different options for responding to changing "
               "conditions, like climate change, over time. They help decision-makers choose actions now while "
               "keeping future options open, allowing adjustments as circumstances evolve. This approach ensures "
               "that we can adapt effectively without locking into a single pathway too early."),
        html.P("Pathways are created using so called Adaptation Tipping Points which determine when additional "
               "measures are needed, e.g. to keep flood damages below an acceptable/desirable threshold while sea "
               "level rises.")
    ]
)

robustness_explanation = create_modal(
    "robustness_explanation",
    "Robustness",
    [
        html.P("Performance robustness explores how a pathway performs across a wide range of "
               "scenarios, such as different climate change projections (e.g. changes in intensity and frequency of flood "
               "events) or climate variability (e.g. possible timings of flood events) within the time-horizon of interest. "
               "The robustness is assessed by measuring how consistently the pathway meets key objectives "
               "(such as reducing risks or costs) across all these uncertainties. Typically, we use statistical methods "
               "like the mean and variance of performance metrics to quantify the performance robustness. This ensures "
               "that reliable and successful pathways are chosen even as the environment or circumstances change.")
    ]
)

scenario_explanation = create_modal(
    "scenario_explanation",
    "Climate Scenarios",
    [
        "A climate scenario is a plausible description of how the future may unfold based on key driving forces "
        "(e.g. climate change). For the performance robustness analysis, we distinguish between three "
        "climate scenarios until 2100: 1) 'historic' climate, 2) 1.5 \u2103 warming and 3) 4 \u2103 warming. "
        "Consequently, we determine the performance robustness across the uncertainty of climate variability (e.g. "
        "possible timings of flood events) following each climate scenario."
    ]
)

interaction_explanation = create_modal(
    "interaction_explanation",
    "Interactions",
    [
        html.P("The interaction between measures can have different effects: 1) trade-offs which increase the risks "
               "and related impacts (e.g. implementing drought-resilient crops which lead to higher flood-related "
               "productivity losses) or 2) synergies which contribute to reducing risks and impacts (e.g. room for the "
               "river primarily reduces flood risk, and also reduces drought risk by increasing groundwater recharge "
               "rates) for another sector or hazard. This not only influences the performance robustness of a "
               "pathway, but can also influence when measures need to be implemented."),
        html.P(
            html.B(
                "At this stage of the analysis, we only focus on the interest of farmers and want to identify farmer "
                "pathways that which work well with the majority of pathways of other actors. At a later stage we can also investigate which "
               "specific combinations of pathways work best for all actors and risks."
            )
        )
    ]
)

timing_explanation = create_modal(
    "timing_explanation",
    "How the timing of decision-points is identified",
    [
        html.P("Pathways maps show expected timings of decision-points using approaches similar to the robustness "
            "performance. Statistics can be used to identify these timings based on the scenarios underlying the "
               "analysis."),
        html.P("Here, we used the median to derive the expected timings, but other approaches could be used as well.")
    ]
)
personal_information_explanation = create_modal(
    'personalinformation_explanation',
    'Reason for collecting personal information',
    [
        # html.P("We collect details on your age and gender to ensure a diverse representation in our dataset, enabling
        # a more comprehensive understanding of how different demographic groups perceive and interact with our
        # visualization techniques. This information will solely be used for analytical purposes to identify
        # potential patterns or biases and will not be linked to individual responses or disclosed in any identifying
        # manner."),
        html.P("We ask a question regarding visual impairments solely to ensure our designs are inclusive and to "
               "understand any potential challenges participants might experience. Your feedback will be used to "
               "enhance the accessibility of our visual tools."),
        html.P('Furthermore, we collect information on your expertise and type of work to enable understanding of how '
               'different demographic groups perceive and interact with our visualization techniques. We want to '
               'establish your familiarity with visualizations and using them to extract information about alternative '
               'options to inform a decision.')
    ]
)



Stacked_Bar_Chart_explanation = create_modal_with_image(
    'Stacked_Bar_Chart_explanation',
    'What is a Stacked Bar Chart?',
    'assets/figures/explanation/stacked_bar_graph.png',
    [
        f'Copied from Datavizcatalogue. Further information about stacked bars can be found here: ',
        html.A('https://datavizcatalogue.com/methods/stacked_bar_graph.html',
               href='https://datavizcatalogue.com/methods/stacked_bar_graph.html',
               target="_blank")
    ],
)

Parallel_Coordinates_Plot_explanation = create_modal_with_image(
    'Parallel_Coordinates_Plot_explanation',
    'What is a Parallel Coordinates Plot?',
    'assets/figures/explanation/parallel_coordinates.svg',
    [
        f'Copied from Datavizcatalogue. Further information about parallel coordinate plots can be found here: ',
        html.A('https://datavizcatalogue.com/methods/parallel_coordinates.html',
               href='https://datavizcatalogue.com/methods/parallel_coordinates.html',
               target="_blank")
    ],
)

Heatmap_explanation = create_modal_with_image(
    'Heatmap_explanation',
    'What is a Heatmap?',
    'assets/figures/explanation/heatmap.svg',
    [
        f'Copied from Datavizcatalogue. Further information about heatmaps can be found here: ',
        html.A('https://datavizcatalogue.com/methods/heatmap.html',
               href='https://datavizcatalogue.com/methods/heatmap.html',
               target="_blank")
    ],
)

Pathways_Map_explanation = create_modal_with_image(
    'Pathways_Map_explanation',
    'What is a Pathways Map?',
    'assets/figures/explanation/pathways_map.png',
    [
        f'Copied from Haasnoot et al. (2013). Further information about heatmaps can be found here: ',
        html.A('https://www.deltares.nl/en/expertise/areas-of-expertise/sea-level-rise/dynamic-adaptive-policy-pathways',
               href='https://www.deltares.nl/en/expertise/areas-of-expertise/sea-level-rise/dynamic-adaptive-policy-pathways',
               target="_blank")],)

matching_dict = {
    'Stacked_Bar_Chart_explanation': Stacked_Bar_Chart_explanation,
    'Parallel_Coordinates_Plot_explanation': Parallel_Coordinates_Plot_explanation,
    'Heatmap_explanation': Heatmap_explanation,
    'Pathways_Map_explanation': Pathways_Map_explanation
}


