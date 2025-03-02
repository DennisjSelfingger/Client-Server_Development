
THERE IS A FILE CALLED README.txt which has screenshots of this working. Make sure to include your own unique name and password

Grazioso Salvare Rescue Dog Dashboard
Project Overview
This interactive dashboard was developed for Grazioso Salvare, an international rescue-animal training company. It interfaces with a MongoDB database containing data from five animal shelters around Austin, Texas, allowing users to efficiently categorize dogs suitable for various rescue operations.

Purpose
The dashboard assists Grazioso Salvare in training dogs for specialized rescue operations such as:

Water Rescue
Mountain or Wilderness Rescue
Disaster or Individual Tracking
Users can rapidly filter shelter data to find dogs matching specific criteria like breed, age, and sex for each rescue category.

Technologies Used
Python 3.x
MongoDB
Jupyter Dash
Dash Leaflet for geolocation visualization
Plotly Express for charts
Pandas for data manipulation
Setup and Installation
Prerequisites
Python 3.x
MongoDB
Access to the Austin Animal Center Outcomes dataset
Installation Instructions 

#### pip install jupyter-dash dash dash-leaflet pandas plotly  ###

Clone the repository:

(files are seperated so you may need copy and paste each one idividually in jupyter notebook or text editor)

git clone https://github.com/DennisjSelfingger/grazioso-salvare-dashboard.git
cd grazioso-salvare-dashboard


Database Setup

Import the dataset into MongoDB:

mongoimport --db AAC --collection animals --file aac_shelter_outcomes.csv --type csv --headerline


Create a MongoDB user with read access:

use AAC
db.createUser({
    user: "create credential",
    pwd: "create unique password",
    roles: [{ role: "read", db: "AAC" }]
})

Running the Application
Launch Jupyter Notebook:
Open ProjectTwoDashboard.ipynb and run all cells
Access the dashboard at http://127.0.0.1:8050/ in your browser
Features
Interactive Filtering: Filters dogs based on suitability for different rescue types.
Data Table: Displays animal records based on selected filters with pagination, sortable columns, and selection capability.
Visualizations: Includes breed distribution pie charts and geolocation maps.
Evidence of Functionality
Screenshots demonstrating the functionality of the dashboard are included in this repository within a designated screenshots directory.

Troubleshooting and Common Issues
Authentication Failures: Ensure that user credentials are correctly set in your MongoDB instance.
Document Not Found: Verify the accuracy of your query parameters if no results are returned.
Future Enhancements
Future updates may include more sophisticated query capabilities, integration with other databases, or enhanced security features for data access.

Author
Dennis Selfinger
Role: Lead Developer
Company: Global Rain
Contact: dself1976@gmail.com
Contributions: Led the design and development of the dashboard.


