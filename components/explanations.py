from dash import html
from utilities.create_modal import create_modal, create_modal_with_image

GLOSSARY_TERMS={
    'Disaster Risk Management': 'Strategies and practices to reduce vulnerabilities and manage the impacts of natural hazards.',
    'Pathway': 'A sequence of measures that are implemented to adjust to future changes.',
    'Multi-Risk Setting': 'A context in which multiple hazards interact and impacts to and responses by different actors influence each other.',
    'Sectoral Risk Owner': 'Individuals or entities responsible for managing risks in specific sectors, such as a shipping company, farmer, or municipality.',
    'Climate Scenarios': 'Plausible time-series of e.g. precipitation intensity or river discharge for different warming scenarios. '
                         'Multiple time-series per climate scenario to capture uncertainty and natural variability.',
    'Robustness': 'Evaluated regarding a set of criteria using indicators to deal with uncertainty in and across climate scenarios.',
    'Trade-offs': 'Compromises made when choosing between two or more competing options.',
    'Interactions': 'Pathways of different sectoral risk owners can interfere with or benefit from each other, leading to changes in robustness or available options.'
}

# Word explanations
pathways_explanation = create_modal(
    "pathways_explanation",
    "Pathways",
    [
        html.P("Adaptation pathways are flexible plans that outline different options for responding to changing "
               "conditions, like climate change, over time. They help decision-makers choose actions now while "
               "keeping future options open, allowing adjustments as circumstances evolve. This approach ensures "
               "that we can adapt effectively without locking into a single strategy too early."),
        html.P("Pathways are created using so called Adaptation Tipping Points which determine when additional "
               "measures are needed, e.g. to keep flood damages below an acceptable/desirable threshold while sea "
               "level rise.")
    ]
)

robustness_explanation = create_modal(
    "robustness_explanation",
    "Robustness",
    [
        html.P("Performance robustness refers to how well a DRM strategy continues to work effectively under a wide "
               "range of possible future conditions. In the context of adaptation pathways, it means choosing options "
               "that will remain reliable and successful even as the environment or circumstances change, reducing the "
               "risk of failure over time."),
        html.P("Performance robustness can be calculated to explore how a strategy performs across a wide range of "
               "scenarios, such as different climate projections or economic changes. The robustness is then "
               "quantified by measuring how consistently the strategy meets key objectives (like reducing risks or "
               "costs) across all these scenarios, often using statistical methods like the mean and variance of "
               "performance metrics, or by counting the number of scenarios where the strategy achieves a "
               "satisfactory outcome.")
    ]
)

scenario_explanation = create_modal(
    "scenario_explanation",
    "Climate Scenarios",
    [
        "A scenario is a plausible description of how the future may develop based on key driving forces (e.g. climate "
        "change). For the analysis here, we distinguish between three climate scenarios: 'historic' climate, with 1.5 "
        "\u2103 warming and with 4 \u2103 warming until 2100. Climate change alone does not detmerine the relevant "
        "hazard-drivers (e.g. precipitation). Randomness and other phenomena determine precipitation patterns over "
        "the coming 100 years. As a consequence, there are multiple plausible time-series (e.g. precipitation) within "
        "each scenario. It is across these variations within each climate scenario we determine the robustness."
    ]
)

interaction_explanation = create_modal(
    "interaction_explanation",
    "Interactions",
    [
        html.P("The interaction between measures can have different effects: they can increase the risks and related "
               "impacts (trade-off. Example: implementing drought-resilient crops leads to higher flood-related "
               "productivity losses) or contribute to reducing risks and impacts (synergy. Example: room for the river "
               "has the primary purpose to reduce flood risk, and a secondary effect on groundwater recharge reducing "
               "drought risk) for another sector or hazard. This influences not only the performance robustness of a "
               "pathway but can also influence when measures need to be implemented."),
        html.P(
            html.B(
                "At this stage of the analysis, we are only interested to identify the flood risk pathways for farmers "
               "which work best with most pathways of other actors. At a later stage we can also investigate which "
               "specific combinations of pathways work best for all actors and hazard considered. "
            )
        )
    ]
)

timing_explanation = create_modal(
    "timing_explanation",
    "How the timing of decision-points is identified",
    [
        html.P("Pathways map show expected timings of decision-points using approaches similar to how the robustness "
            "performance is determined. Statistics can be used to identify these timings based on the scenarios "
            "underlying the analysis."),
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


