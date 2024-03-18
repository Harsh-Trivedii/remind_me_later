## Setup Instructions

1. Clone the repository to your local machine:
   
   git clone https://github.com/Harsh-Trivedii/remind_me_later/

2. Navigate to the project directory
   cd remind_me_later

3. Run migrations to create the database schema
   python manage.py migrate

4. Start the Django development server
   python manage.py runserver

4. Access the API endpoint using Postman or cURL
   Example cURL command- curl -X POST http://localhost:8000/api/reminder/ -H "Content-Type: application/json" -d "{\"date\": \"2024-03-18\", \"time\": \"14:30:00\", \"message\": \"Remember to attend the meeting\"}"
This command sends a POST request to the endpoint with the provided JSON data
