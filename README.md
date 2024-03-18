# Circlism

This repository provides a Flask application for uploading images, processing them using custom algorithms, and returning the processed images. Additionally, it includes a React frontend for interacting with the Flask backend.

## Setup

To set up the environment and install necessary dependencies, follow these steps:

1. Install `virtualenv` using pip:

   ```
   python3 -m pip install --user virtualenv
   ```

2. Create a virtual environment:

   ```
   python3 -m venv env
   ```

3. Activate the virtual environment:

   ```
   source env/bin/activate
   ```

4. Check the Python version:

   ```
   which python
   ```

5. Install dependencies from `requirements.txt`:

   ```
   python3 -m pip install -r requirements.txt
   ```

6. Freeze installed dependencies to `requirements.txt`:

   ```
   python3 -m pip freeze > requirements.txt
   ```

7. Install additional system dependencies:

   ```
   sudo apt install libcairo2-dev pkg-config python3-dev
   ```

## Running the Application

To run the Flask application, execute the following command:

```
python3 app.py
```

This will start the Flask server, and the application will be accessible at `http://localhost:5000`.

## Usage

### Uploading and Processing Images

The Flask application provides endpoints for uploading and processing images. The following endpoints are available:

- `/upload/ciclism`: Uploads an image and processes it using the circlism algorithm.
- `/upload/number`: Processes an image to generate numerical representation.

Both endpoints expect a POST request with a file attached and an identifier. Upon processing, the endpoints return the URL of the processed image.

### React Frontend

The repository includes a React frontend for interacting with the Flask backend. The main component `ProcessImage` renders a file upload interface and allows users to transform their photos using circlism mode and numerical representation.

The `SubmitButton` component triggers the image processing algorithms and displays an animation while processing is in progress.

## Credits

This project was inspired by the "File Upload with React & Flask" article written by Ashish Pandey and Arshpreet Wadehra. Their Medium article provided insights into integrating React with Flask for file upload functionality.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it according to your needs.
