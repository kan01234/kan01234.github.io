from jinja2 import Environment, FileSystemLoader  
import json

# Open the JSON file in read mode
with open("data.json", "r") as file:
  # Load the JSON content into a Python dictionary
  data = json.load(file)

# Create a Template Loader object
env = Environment(loader=FileSystemLoader('template'))

# Load the template
template = env.get_template('index.j2')

# Render the template with data
html_content = template.render(data=data)

# Write rendered HTML to a file (optional)
with open("index.html", "w") as f:
    f.write(html_content)
