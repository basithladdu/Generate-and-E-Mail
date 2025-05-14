from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_intern_data(unique_code):
    conn = sqlite3.connect("interns.db")
    cur = conn.cursor()
    cur.execute("SELECT name, email, date, status FROM interns WHERE unique_code = ?", (unique_code,))
    result = cur.fetchone()
    conn.close()
    if result:
        return {"name": result[0], "email": result[1], "date": result[2], "status": result[3]}
    return None

@app.route('/verify', methods=['GET'])
def verify_certificate():
    code = request.args.get('code')
    intern = get_intern_data(code)
    if intern:
        return jsonify({"verified": True, "details": intern})
    else:
        return jsonify({"verified": False, "message": "Invalid or modified certificate."}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)