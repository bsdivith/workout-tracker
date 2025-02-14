# Exercise Tracker

## Overview
This Python script tracks your exercise and logs the details (exercise name, duration, and calories burned) into a Google Sheet using **Nutritionix API** and **Sheety API**.

## Features
- Accepts user input for an exercise or activity.
- Fetches exercise details like **duration** and **calories burned** from Nutritionix API.
- Logs exercise data (date, time, activity, duration, calories) to a Google Sheet.
- Uses environment variables for sensitive API credentials.

## Technologies Used
- **Python** (requests, datetime, os)
- **Nutritionix API** (exercise data retrieval)
- **Sheety API** (Google Sheets integration)

## Setup & Installation
### 1. Clone the Repository
```bash
git clone <repo_url>
cd <repo_name>
```

### 2. Install Dependencies
Ensure you have Python installed, then install `requests`:
```bash
pip install requests
```

### 3. Set Up Environment Variables
Create a **.env** file or export variables in your shell:
```bash
export APP_ID='your_nutritionix_app_id'
export API_KEY='your_nutritionix_api_key'
export SHEET_ENDPOINT='your_sheety_endpoint'
export BEARER_TOKEN='your_bearer_token'
```

### 4. Run the Script
```bash
python exercise_tracker.py
```

## Example Usage
```
Enter exercise or activity: Running 30 minutes
```
**Output (Logged to Google Sheet):**
| Date       | Time     | Exercise | Duration (min) | Calories |
|-----------|---------|----------|----------------|----------|
| 14/02/2025 | 10:30:00 | Running  | 30             | 250      |

## API Details
### **1. Nutritionix API**
- **Endpoint:** `https://trackapi.nutritionix.com/v2/natural/exercise`
- **Headers:**
  - `x-app-id`: Your Nutritionix App ID
  - `x-app-key`: Your Nutritionix API Key
- **Request Body:**
  ```json
  {
    "query": "Running 30 minutes",
    "weight_kg": 55,
    "height_cm": 168,
    "age": 22,
    "gender": "male"
  }
  ```
- **Response Example:**
  ```json
  {
    "exercises": [
      {
        "name": "running",
        "duration_min": 30,
        "nf_calories": 250
      }
    ]
  }
  ```

### **2. Sheety API**
- **Endpoint:** `your_google_sheet_webhook`
- **Authorization:** Bearer Token
- **Request Body:**
  ```json
  {
    "workout": {
      "date": "14/02/2025",
      "time": "10:30:00",
      "exercise": "Running",
      "duration": 30,
      "calories": 250
    }
  }
  ```

## License
This project is open-source and free to use.

---
**Happy Tracking! 🏃‍♂️🔥**



**Input**: Enter exercise or activity: jogging on a treadmill for 30 minutes at 10km per hour. 

**Output**:

![image](https://github.com/user-attachments/assets/202a3f04-437c-4ddd-a49d-22cf2a5e1831)

new entry made to google sheet using sheety api:

![image](https://github.com/user-attachments/assets/f477976c-da7a-45d8-8d25-558641770da6)
