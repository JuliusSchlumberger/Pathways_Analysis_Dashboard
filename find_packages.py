import os
import re

def find_python_packages(root_dir):
    package_set = set()
    # Regex to match import statements
    import_pattern = re.compile(r"^\s*(from\s+(\w+)|import\s+(\w+))")

    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(subdir, file)
                with open(filepath, "r") as file:
                    for line in file:
                        match = import_pattern.match(line)
                        if match:
                            # Check if the import statement is "from something" or "import something"
                            package_name = match.group(2) or match.group(3)
                            package_set.add(package_name)

    return package_set

# Usage
# directory_path = f"C:\Users\schlumbe\OneDrive - Stichting Deltares\Documents\PhD\30_Paper3\PathwaysAnalysis_Dashboard_v1"
directory_path = os.getcwd()
print(directory_path)
packages = find_python_packages(directory_path)
print("Packages found:", packages)
