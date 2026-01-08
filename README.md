# 📌 Job Application Tracker

This is a simple Flask web application designed to help you keep track of your job applications. It allows you to add, view, edit, and delete job application entries, along with features for filtering and sorting your applications. The application uses SQLite for database storage and includes Docker support for easy containerization.

## ✨ Features

*   **Add Job Applications:** Easily add new job application entries with details such as company, job title, status, application link, date applied, location, source, and notes.
*   **View All Applications:** Display a list of all your tracked job applications in a clean, tabular format.
*   **Edit Applications:** Modify existing job application details through a dedicated edit page.
*   **Delete Applications:** Remove job applications you no longer need to track.
*   **Filter by Status:** Filter your job applications by their current status (e.g., Applied, Interviewing, Offer, Rejected, Accepted) using a dropdown menu.
*   **Sort Applications:** Sort your applications by various criteria such as company, job title, status, or date applied, in either ascending or descending order.
*   **Inline Status Editing:** Quickly update the status of a job application directly from the main listing page using an interactive dropdown, with AJAX-based updates for a smooth user experience.
*   **Status Color Coding:** The status dropdowns are color-coded to provide quick visual cues about the application's current stage.
*   **Docker Support:** The application includes a `Dockerfile` and `docker-compose.yml` for easy setup and deployment in a containerized environment.

## 🚀 Technologies Used

*   **Backend:** Flask (Python)
*   **Database:** SQLite3
*   **Frontend:** HTML, CSS (Bootstrap 5), JavaScript (Vanilla JS for AJAX)
*   **Containerization:** Docker

## 🛠️ Setup Instructions

Follow these steps to get the application up and running on your local machine.

### Prerequisites

*   Python 3.8+
*   pip (Python package installer)
*   Git
*   Docker (Optional, for containerized setup)

### Local Development Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/job-application-tracker.git
    cd job-application-tracker
    ```
    *(Note: Replace `https://github.com/your-username/job-application-tracker.git` with the actual repository URL)*

2.  **Install Python Dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Initialize the Database:**
    The database will be automatically created and initialized when you run `app.py` for the first time.
    ```bash
    python app.py
    ```
    If you are updating from an older schema and encounter database errors (e.g., "no such column"), you might need to delete the existing `data/jobs.db` file to recreate the database with the new schema:
    ```bash
    rm data/jobs.db # On Windows, use `del data\jobs.db`
    python app.py
    ```

4.  **Run the Application:**
    ```bash
    python app.py
    ```
    The application will be accessible at `http://127.0.0.1:5000`.

### Docker Setup (Optional)

1.  **Build and run with Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    This will build the Docker image and start the Flask application. The database (`jobs.db`) will be persisted in a `data/` directory mounted from your host machine.
    The application will be accessible at `http://localhost:5000`.

2.  **Stop Docker Compose:**
    ```bash
    docker-compose down
    ```

## 📝 Usage

*   Navigate to `http://127.0.0.1:5000` (or `http://localhost:5000` if using Docker).
*   Use the **"+ Add Application"** button to add new job entries.
*   View your applications in the table.
*   Use the **"Filter by Status"** dropdown to narrow down the list.
*   Use the **"Sort By"** and **"Order"** dropdowns to organize your applications.
*   Click the **"Edit"** button in the Actions column to modify an application's details.
*   Click the **"Delete"** button to remove an application (a confirmation prompt will appear).
*   Change the status of an application directly from the table using the inline **status dropdown**.

## ☁️ Deployment

This Flask application requires a server-side environment to run. GitHub Pages is only for static websites and cannot host dynamic applications like this.

Recommended platforms for deploying a Flask application include:

*   **Render:** A developer-friendly PaaS with excellent Docker support and options for persistent storage (crucial for SQLite databases).
*   **Heroku:** A popular PaaS that can host Flask apps, particularly via its Container Registry.
*   **Google Cloud Run / AWS Fargate:** Serverless container platforms that are highly scalable but may have a steeper learning curve.

If you consider platforms like **Vercel**, be aware that it primarily uses serverless functions with ephemeral filesystems. This means you would need to migrate your SQLite database to an external, persistent database service (e.g., PostgreSQL) for your data to be saved.

## 🤝 Contributing

Feel free to fork this repository, open issues, or submit pull requests to improve the application.
