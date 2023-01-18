from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/npm_packages', methods=['POST'])
def npm_packages():
    packages = request.get_json()
    return jsonify(packages)


if __name__ == '__main__':
    app.run(debug=True)


