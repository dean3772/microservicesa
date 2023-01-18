from flask import Flask, jsonify, request 
import pytest
# parser = argparse.ArgumentParser()
# parser.add_argument("--trustkey_jks", action="store_true")
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def check_packages():
    packages = request.json.get('packages')
    # Do something with the packages
    return jsonify({'status': 'success'})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# curl -X POST http://localhost:5000/api -H "Content-Type: application/json" -d '{"packages": ["pkg1", "pkg2", "pkg3", "pkg4", "pkg5", "pkg6", "pkg7", "pkg8", "pkg9", "pkg10"]}'
# pip install pytest-xdist

