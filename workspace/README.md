# Little Lemon Web Application

The Little Lemon Web Application is a Django-based web application that provides functionalities to view menus and manage table bookings for the Little Lemon restaurant.

## Prerequisites

- Python (3.7+ recommended)
- Django (4.2.5 recommended)
- Django REST framework
- MySQL

## Setup & Installation

1. Clone the repository: `git clone [YOUR_GITHUB_REPO_URL]`
2. Navigate to the project directory: `cd [YOUR_PROJECT_DIRECTORY]`
3. Install required packages: `pip install -r requirements.txt` *(You might need to create this file listing all the necessary packages)*
4. Update `settings.py` in the `LittleLemon` directory with your MySQL database credentials.
5. Update the directory to project folder..\\LittleLemon\workspace\littlelemon
6. Run the migrations: `python manage.py migrate`
7. Don not forget these commands: 'pipenv install', 'pipenv shell', 'pipenv install django'.
8. If there is a problem with rest(DRF) packages you've to make sure that using a python.exe file for virtual environment
9. Start the server: `python manage.py runserver`
10. Open a browser and navigate to `http://127.0.0.1:8000/` to access the application.

## API Endpoints
# Most of api points need to a valid token like: 57fb3cd7b7e9635a73fb6ba025ce53169e17fe0a 
# There is an image folder that shows the results of the API code implementation..

1. **Menu List & Creation**
    - Endpoint: `/restaurant/menu/`
    - Method: `GET` (To retrieve all menus). 
    - Method: `POST` (To create a new menu item)

2. **Booking List & Creation**
    - Endpoint: `/restaurant/booking/tables/`
    - Method: `GET` (To retrieve all bookings)
    - Method: `POST` (To create a new booking)


## Testing

Use the [Insomnia REST Client](https://insomnia.rest/) or a similar tool to test the API endpoints.

## Contributing

Feel free to submit pull requests or issues if you find any bugs or improvements to add.

## License

This project is licensed under the MIT License. (You can change this to any license you prefer)

