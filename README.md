# integr8-demo

## Frontend Setup - Follow the instructions below to set it up:

1. Clone the repository:
    ```bash
    git clone https://github.com/JDSNX/integr8-demo.git
    cd integr8-demo/file-demo/frontend
    ```

1. Install dependencies
    ```bash
    npm install
    ```

2. Run the app in development mode
    ```bash
    npm start
    ```

3. Open http://localhost:3000 in your browser to view the app.


## Backend Setup - Follow the instructions below to set it up:

1. Clone the repository:
   ```bash
   git clone https://github.com/JDSNX/integr8-demo.git
   cd integr8-demo/file-demo/backend
   ```

1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:
* On Windows:
    ```bash
    venv\Scripts\activate
    ```
* On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

3. Install depedencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI:
    ```bash
    cd src/app
    uvicorn main:app
    ```

5. Open http://127.0.0.1:8000/docs in your browser to access the API Swagger Documentation.