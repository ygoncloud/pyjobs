from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DB_PATH = "data/jobs.db"


def get_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    db = get_db()
    
    # Filtering by status
    filter_status = request.args.get("status")
    
    # Sorting
    sort_by = request.args.get("sort_by", "date_applied")
    order = request.args.get("order", "DESC") # Default to descending

    # Validate sort_by column to prevent SQL injection
    valid_sort_columns = ["company", "job_title", "status", "date_applied"]
    if sort_by not in valid_sort_columns:
        sort_by = "date_applied" # Default if invalid

    # Validate order
    if order.upper() not in ["ASC", "DESC"]:
        order = "DESC" # Default if invalid

    query = "SELECT * FROM jobs"
    params = []

    if filter_status:
        query += " WHERE status = ?"
        params.append(filter_status)
    
    query += f" ORDER BY {sort_by} {order}" # F-string is safe here because sort_by and order are validated

    jobs = db.execute(query, tuple(params)).fetchall()
    
    # Pass filter_status, sort_by, and order to the template
    return render_template("index.html", jobs=jobs, filter_status=filter_status, sort_by=sort_by, order=order)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        company = request.form["company"]
        job_title = request.form["job_title"]
        status = request.form["status"]
        application_link = request.form.get("application_link") # .get() for optional fields
        notes = request.form.get("notes")
        date_applied = request.form["date_applied"]
        location = request.form.get("location")
        source = request.form.get("source")

        db = get_db()
        db.execute(
            "INSERT INTO jobs (company, job_title, status, application_link, notes, date_applied, location, source) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (company, job_title, status, application_link, notes, date_applied, location, source),
        )
        db.commit()
        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/update_job_status/<int:job_id>", methods=["POST"])
def update_job_status(job_id):
    db = get_db()
    data = request.get_json()
    new_status = data.get("status")

    if not new_status:
        return {"success": False, "message": "No status provided"}, 400

    try:
        db.execute("UPDATE jobs SET status = ? WHERE id = ?", (new_status, job_id))
        db.commit()
        return {"success": True, "message": "Status updated successfully"}, 200
    except Exception as e:
        db.rollback()
        return {"success": False, "message": str(e)}, 500


@app.route("/delete/<int:job_id>", methods=["POST"]) # Changed to POST for better practice
def delete(job_id):
    db = get_db()
    db.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
    db.commit()
    return redirect(url_for("index"))


@app.route("/edit/<int:job_id>", methods=["GET", "POST"])
def edit(job_id):
    db = get_db()
    job = db.execute("SELECT * FROM jobs WHERE id = ?", (job_id,)).fetchone()

    if job is None:
        return redirect(url_for("index")) # Job not found, redirect to index

    if request.method == "POST":
        company = request.form["company"]
        job_title = request.form["job_title"]
        status = request.form["status"]
        application_link = request.form.get("application_link")
        notes = request.form.get("notes")
        date_applied = request.form["date_applied"]
        location = request.form.get("location")
        source = request.form.get("source")

        db.execute(
            """
            UPDATE jobs SET
                company = ?,
                job_title = ?,
                status = ?,
                application_link = ?,
                notes = ?,
                date_applied = ?,
                location = ?,
                source = ?
            WHERE id = ?
            """,
            (company, job_title, status, application_link, notes, date_applied, location, source, job_id),
        )
        db.commit()
        return redirect(url_for("index"))

    return render_template("edit.html", job=job)


if __name__ == "__main__":
    db = get_db()
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            job_title TEXT NOT NULL,
            status TEXT NOT NULL,
            application_link TEXT,
            notes TEXT,
            date_applied TEXT NOT NULL,
            location TEXT,
            source TEXT
        )
        """
    )
    db.commit()

    app.run(host="0.0.0.0", port=5000)

