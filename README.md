# Pathways Analysis Dashboard

An interactive web application designed to analyze and visualize pathway data, facilitating insights into complex systems. Built using Python and Plotly Dash, this dashboard offers dynamic data exploration capabilities.

## Features

- **Interactive Visualizations**: Engage with dynamic plots and charts to explore pathway data intuitively.
- **Modular Architecture**: Organized codebase with components, callbacks, and utilities for maintainability and scalability.
- **Data Management**: Tools to export databases to CSV and generate comprehensive figures for analysis.
- **Deployment Ready**: Includes configurations like `Procfile` for seamless deployment on platforms such as Heroku.

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

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Developed by [Julius Schlumberger](https://github.com/JuliusSchlumberger).
