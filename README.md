# Toodle
An Opensource alternative to Doodle

# Setup

## Backend

### Python local development
1. Open a terminal and navigate to the project directory:
    ```
    cd /Users/tobiasrothlin/Documents/HTTPProjekte/Toodle/backend
    ```

2. Create a new virtual environment:
    ```
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    - For macOS/Linux:
      ```
      source venv/bin/activate
      ```
    - For Windows:
      ```
      venv\Scripts\activate
      ```

4. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

5. Start FastAPI Server
```
    fastapi dev main.py
```

### Build and build Backend Container
```
    cd /backend
    docker build -t toodle-backend .
    docker run -d -p 8000:8000 --name toodle-backend toodle-backend
```

