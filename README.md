# Pathways Analysis Dashboard

An interactive web application designed to analyze and visualize pathway data, facilitating insights into complex systems. Built using Python and Plotly Dash, this dashboard offers dynamic data exploration capabilities.

## Features

- **Interactive Visualizations**: Engage with dynamic plots and charts to explore pathway data intuitively.
- **Modular Architecture**: Organized codebase with components, callbacks, and utilities for maintainability and scalability.
- **Data Management**: Tools to export databases to CSV and generate comprehensive figures for analysis.
- **Deployment Ready**: Includes configurations like `Procfile` for seamless deployment on platforms such as Heroku.

## Live Dashboard & Publication

- 🚀 **Try the Live Dashboard**: [https://www.pathways-analysis-dashboard.net/](https://www.pathways-analysis-dashboard.net/))
- 📄 **Related Publication**: Findings from this research are published at [https://doi.org/10.5194/egusphere-2024-3655](https://doi.org/10.5194/egusphere-2024-3655)

## About

This research is conducted as part of the HORIZON 2020 [MYRIAD-EU project](https://www.myriadproject.eu/). If you have any questions regarding this study or the project, please reach out to [julius.schlumberger@deltares.nl](mailto:julius.schlumberger@deltares.nl).

This research is a collaborative effort with Jeroen Aerts, Marleen de Ruiter, Robert Šakić Trogrlić, Jung-Hee Hyun, Stefan Hochrainer-Stigler, and Marjolijn Haasnoot. We thank the 21 participants in our group discussions and semi-structured interviews, as well as the 54 survey participants, for their critical contributions.

### Abstract (from the publication)

With accelerating climate change, impacts will compound and cascade, making them more complex to assess and manage. At the same time, tools that help decision makers choose between different management options are very limited.

This study introduces a visual analytics dashboard prototype designed to support pathways analysis for multi-risk Disaster Risk Management (DRM). Developed through a systematic design approach, the dashboard employs interactive visualisations of pathways and their evaluation — including Decision Trees, Parallel Coordinates Plots, Stacked Bar Charts, Heatmaps, and Pathways Maps — to facilitate complex, multi-criteria decision-making under uncertainty.

We demonstrate the utility of the dashboard through an evaluation with 54 participants at varying levels and disciplines of expertise. Depending on their background (non-experts, adaptation/DRM experts, pathways experts), users were able to interpret options, performance, and timing of decisions with precision between 71% and 80%. Participants particularly valued the dashboard’s interactivity, which allowed for scenario exploration and contextual data access.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/JuliusSchlumberger/Pathways_Analysis_Dashboard.git
   cd Pathways_Analysis_Dashboard
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare the Data**:
   Ensure your pathway data is correctly formatted and placed in the appropriate directory.

2. **Run the Application**:
   ```bash
   python app.py
   ```

   Access the dashboard by navigating to `http://127.0.0.1:8050/` in your web browser.

## Project Structure

```plaintext
├── app.py                     # Main application file
├── dashapp.py                 # Dash application setup
├── components/                # Reusable UI components
├── callbacks/                 # Callback functions for interactivity
├── pages/                     # Multi-page layout components
├── utilities/                 # Helper functions and utilities
├── scripts/                   # Scripts for data processing and figure generation
├── assets/                    # Static assets like CSS and images
├── requirements.txt           # Python dependencies
├── Procfile                   # Deployment configuration
└── README.md                  # Project documentation
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

## Acknowledgments

Developed by [Julius Schlumberger](https://github.com/JuliusSchlumberger).
