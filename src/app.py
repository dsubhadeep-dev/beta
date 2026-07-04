from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Aarav Sharma", "role": "Software Engineer", "dept": "Engineering", "status": "Active"},
    {"id": 2, "name": "Neha Verma", "role": "HR Specialist", "dept": "Human Resources", "status": "Active"},
    {"id": 3, "name": "Karan Singh", "role": "Accountant", "dept": "Finance", "status": "On Leave"},
]

HTML = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>HR Management System</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 0; background: #f4f7fb; color: #233; }
      .container { max-width: 1000px; margin: 0 auto; padding: 24px; }
      .card { background: white; border-radius: 12px; padding: 20px; margin-bottom: 20px; box-shadow: 0 6px 20px rgba(0,0,0,0.06); }
      h1, h2 { color: #1f4e79; }
      table { width: 100%; border-collapse: collapse; }
      th, td { padding: 10px; border-bottom: 1px solid #e5e7eb; text-align: left; }
      th { background: #eef5ff; }
      form { display: grid; gap: 10px; max-width: 400px; }
      input, select, button { padding: 10px; border-radius: 8px; border: 1px solid #cbd5e1; }
      button { background: #1f4e79; color: white; cursor: pointer; }
      .pill { display: inline-block; padding: 4px 8px; border-radius: 999px; font-size: 12px; }
      .active { background: #dcfce7; color: #166534; }
      .leave { background: #fef3c7; color: #92400e; }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="card">
        <h1>Human Resource Management System</h1>
        <p>A simple dashboard for tracking employees, departments, and attendance status.</p>
      </div>

      <div class="card">
        <h2>Add Employee</h2>
        <form method="post" action="/add">
          <input name="name" placeholder="Employee name" required />
          <input name="role" placeholder="Role" required />
          <input name="dept" placeholder="Department" required />
          <select name="status">
            <option value="Active">Active</option>
            <option value="On Leave">On Leave</option>
            <option value="Inactive">Inactive</option>
          </select>
          <button type="submit">Save Employee</button>
        </form>
      </div>

      <div class="card">
        <h2>Employee Directory</h2>
        <table>
          <thead>
            <tr>
              <th>ID</th><th>Name</th><th>Role</th><th>Department</th><th>Status</th>
            </tr>
          </thead>
          <tbody>
            {% for emp in employees %}
            <tr>
              <td>{{ emp['id'] }}</td>
              <td>{{ emp['name'] }}</td>
              <td>{{ emp['role'] }}</td>
              <td>{{ emp['dept'] }}</td>
              <td><span class="pill {{ 'active' if emp['status'] == 'Active' else 'leave' }}">{{ emp['status'] }}</span></td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </div>
  </body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML, employees=employees)

@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form.get('name', '').strip()
    role = request.form.get('role', '').strip()
    dept = request.form.get('dept', '').strip()
    status = request.form.get('status', 'Active').strip()

    if name and role and dept:
        employees.append({
            'id': len(employees) + 1,
            'name': name,
            'role': role,
            'dept': dept,
            'status': status,
        })

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
