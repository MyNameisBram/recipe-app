from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/recipe', methods=['POST'])
def get_recipe():
    url = request.json['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    instructions = soup.find('div', {'class': 'instructions'}).find('p').text

    return jsonify({'instructions': instructions})

if __name__ == '__main__':
    app.run(debug=True)

