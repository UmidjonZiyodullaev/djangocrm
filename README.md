# DJCRM

A simple CRM application built with Django.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/djcrm.git
    cd djcrm
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

## Configuration

1. **Create an `.env` file in the root directory:**

    ```bash
    touch .env
    ```

2. **Add the following environment variables to the `.env` file:**

    ```dotenv
    DEBUG=True
    SECRET_KEY=your_secret_key_value_here
    ```

## Usage

1. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

2. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/`

3. **Admin Panel:**

    Access the admin panel at `http://127.0.0.1:8000/admin` using the superuser credentials created earlier.

## Features

- User authentication and authorization
- Lead management
- Agent management
- Tailwind CSS for styling with crispy forms

## Contributing

1. **Fork the repository**

2. **Create a new branch:**

    ```bash
    git checkout -b feature/your-feature-name
    ```

3. **Make your changes and commit them:**

    ```bash
    git commit -m 'Add some feature'
    ```

4. **Push to the branch:**

    ```bash
    git push origin feature/your-feature-name
    ```

5. **Create a pull request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
