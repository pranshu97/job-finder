from flask import Flask, request
from job_scraper import job_scraper

app = Flask(__name__)

@app.route("/")
def job_finder():
    data = dict(request.values)
    skill = data['skill']
    loc = data['location']
    yoe = data['yoe']
    jobs_data = job_scraper(skill,loc,yoe)
    return jobs_data

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
