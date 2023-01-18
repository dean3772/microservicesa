import requests
from datetime import datetime, timedelta


def check_package_health(packages):
    result = []
    for package in packages:
        # Get package details from NPM
        package_details = requests.get(f'https://registry.npmjs.org/{package}').json()
        # Get repository details from GitHub
        repo_details = requests.get(package_details['repository']['url']).json()
        
        # Check if the last version is maximum 30 days old
        last_version_date = datetime.strptime(package_details['time']['modified'], '%Y-%m-%dT%H:%M:%S.%fZ')
        if (datetime.now() - last_version_date) > timedelta(days=30):
            continue
        
        # Check if the number of maintainers is at least 2
        if len(package_details['maintainers']) < 2:
            continue
        
        # Check if the latest commit in the related GitHub repository is maximum 14 days old
        latest_commit_date = datetime.strptime(repo_details['pushed_at'], '%Y-%m-%dT%H:%M:%SZ')
        if (datetime.now() - latest_commit_date) > timedelta(days=14):
            continue
        
        result.append(package)
    return result


from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/health_check', methods=['POST'])
def health_check():
    packages = request.get_json()
    result = check_package_health(packages)
    return jsonify(result)

