from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
{"id": 1, "name": "Juan", "grade": 85, "section": "Zechariah"},
{"id": 2, "name": "Maria", "grade": 90, "section": "Zechariah"},
{"id": 3, "name": "Pedro", "grade": 70, "section": "Zion"}
]

@app.route('/')
def home():
    return "Student API Running"

@app.route('/student')
def get_student():
    grade = int(request.args.get('grade',0))
    remarks = "Pass" if grade >= 75 else "Fail"

    return jsonify({
        "name":"Juan",
        "grade":grade,
        "section":"Zechariah",
        "remarks":remarks
    })

@app.route('/students')
def get_students():
    return jsonify(students)

@app.route('/student/<int:id>')
def get_student_by_id(id):

    student = next((s for s in students if s["id"] == id), None)

    if student:
        return jsonify(student)

    return jsonify({"error":"Student not found"}),404

@app.route('/summary')
def summary():

    grades = [s["grade"] for s in students]

    passed = len([g for g in grades if g >= 75])
    failed = len(grades) - passed
    avg = sum(grades)/len(grades)

    return jsonify({
        "average":avg,
        "passed":passed,
        "failed":failed
    })

if __name__ == '__main__':
    app.run()