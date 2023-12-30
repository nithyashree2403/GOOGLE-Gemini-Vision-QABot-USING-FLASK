# Gemini Flask Application

## Description

Gemini Flask Application is a web-based interface that utilizes the Gemini API to provide information about images based on user prompts and uploaded images. The application is built with Flask and enables users to interact with the Gemini-pro-vision model.

## Getting Started

### Prerequisites

- Python 3.10
- Pip (Python package installer)

### Getting the Google Gemini API Key

To use this chat interface, you need to obtain an API key from the [Google AI Developer website](https://ai.google.dev/). Follow the instructions on the website to generate your API key.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/gemini-flask-app.git
    cd gemini-flask-app
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file with your Google API key:

    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

### Usage

1. Run the Flask app:

    ```bash
    python app.py
    ```


2. Enter an input prompt and upload an image to get Gemini responses.

## Project Structure

- `templates/`: Contains HTML templates for the Flask app.
- `venv/`: Virtual environment for Python.
- `app.py`: Main script for the Flask application.
- `requirements.txt`: Lists Python dependencies.

