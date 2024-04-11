**Exercise Tracker**

This exercise tracker project allows users to log their workouts via a natural language interface. The user can input exercises they performed, and the system will record these workouts along with relevant details like duration and calorie burn into a spreadsheet using the Sheety API.

**Features**

**Natural Language Input:** Users can describe their exercises in plain language (e.g., "ran 30 minutes" or "swam for an hour") and the system will interpret and log these activities.

**Nutritionix Integration:** Utilizes the Nutritionix API to parse the user's exercise input into structured data, extracting details such as exercise name, duration, and calories burned.

**Sheety API Integration:** Logs the exercise data into a Google Sheets document via the Sheety API, allowing for easy tracking and visualization of workout history.

**Technologies Used**

**Python:** Backend programming language used to build the exercise tracker.

**Requests Library:** Utilized to handle HTTP requests for integrating with external APIs like Nutritionix and Sheety.

**Datetime Module:** Used for obtaining and formatting current date and time to record when exercises were performed.

**Environment Variables:** Securely stores sensitive data (e.g., API keys) using environment variables.

**Git Version Control:** Project source code is managed and shared using Git version control.

**Getting Started**

To run this project locally or deploy it on your own environment, follow these steps:

Clone this repository:

git clone https://github.com/your-username/exercise-tracker.git

**Install project dependencies:**

pip install -r requirements.txt

**Set up environment variables:**

Obtain API credentials for Nutritionix and Sheety.

**Set these credentials as environment variables:**

export APP_ID="your_nutritionix_app_id"
export APP_KEY="your_nutritionix_app_key"
export SHEETY_ID="your_sheety_document_id"


**Run the application:**

python exerciseTracker.py


<img width="391" alt="image" src="https://github.com/patreeck/exerciseTracker/assets/163764755/1708e314-424d-483e-8c7d-3e8f226b2487">


<img width="527" alt="image" src="https://github.com/patreeck/exerciseTracker/assets/163764755/2e00c992-b23e-4993-b2bb-c648c841081c">

