from flask import Flask,render_template,jsonify

app=Flask(__name__)

jobs = [
    {
        "title": "Software Developer",
        "company": "lGoogle",
        "location": "Mountain View, CA",
        "salary": "$120,000",
        "description": "Work on the core software that powers Google's search engine."
    },
    {
        "title": "Data Scientist",
        "company": "Facebook",
        "location": "Menlo Park, CA",
        "salary": "$130,000",
        "description": "Analyze data to identify trends and make predictions."
    },
    {
        "title": "Product Manager",
        "company": "Amazon",
        "location": "Seattle, WA",
        "salary": "$125,000",
        "description": "Lead the development of new products and features."
    }
]

@app.route("/")
def helloworld():
    return render_template('home.html',jobs=jobs)

@app.route("/api/jobs")
def job_listing():
    return jsonify(jobs)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)