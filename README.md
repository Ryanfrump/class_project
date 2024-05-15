# Workout API Setup Guide

Welcome to the Workout API setup guide! Follow these steps to get started with using our API.

1. **Clone the Repository:**  
   First, clone the GitHub repository to your local machine using the following command:

   ```bash
   git clone (https://github.com/Ryanfrump/class_project)
   ```

2. **Install Requirements:**  
   Navigate to the project directory and install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

   This command will install all the necessary Python packages specified in the `requirements.txt` file.

3. **Run the Server:**  
   Once the dependencies are installed, you can start the server. We use Uvicorn as the ASGI server, which will serve your API and Swagger UI. Run the following command:
   ```bash
   uvicorn main:app --reload
   ```
   This command starts the server and enables auto-reloading, which means the server will restart automatically whenever you make changes to your code.

```

```
