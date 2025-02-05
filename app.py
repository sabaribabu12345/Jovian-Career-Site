from flask import Flask, render_template
from database import engine
from sqlalchemy.sql import text

app = Flask(__name__)

# Fetch all jobs
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.fetchall():
            jobs.append(dict(row._mapping))
        return jobs

# Fetch a specific job by ID
def load_job_by_id(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :id"), {"id": id})
        row = result.fetchone()
        return dict(row._mapping) if row else None

# Home route
@app.route("/")
def helloworld():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)

# Job details route
@app.route("/jobs/<int:id>")
def job_listing(id):  # Accept `id` as an argument
    job = load_job_by_id(id)
    if job:
        return render_template('jobpage.html', job=job)
    else:
        return "Job not found", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
