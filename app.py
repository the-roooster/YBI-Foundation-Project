from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

# Our existing data structures
guest_list = []
guest_set = set()
valid_statuses = {'Attending', 'Not Attending', 'Pending'}

@app.route('/')
def index():
    try:
        return render_template('index.html', guests=guest_list)
    except Exception as e:
        return f"Error rendering template: {str(e)}", 500

@app.route('/add', methods=['POST'])
def add_guest():
    try:
        name = request.form.get('name', '').strip()
        event = request.form.get('event', '').strip()
        status = request.form.get('status', '').strip()
        
        if not all([name, event, status]):
            return "All fields are required", 400
            
        guest_key = f"{name.lower()}_{event.lower()}"
        
        if guest_key in guest_set:
            return "This guest is already registered for this event", 400
            
        if status not in valid_statuses:
            return "Invalid RSVP status", 400
            
        guest_list.append((name, event, status))
        guest_set.add(guest_key)
        return redirect(url_for('index'))
        
    except Exception as e:
        return f"Error adding guest: {str(e)}", 500

@app.route('/export')
def export():
    try:
        if not guest_list:
            return "No guests to export", 400
            
        df = pd.DataFrame(guest_list, columns=['Name', 'Event', 'Status'])
        
        # Ensure the directory exists
        os.makedirs('exports', exist_ok=True)
        export_path = os.path.join('exports', 'guest_list.csv')
        
        df.to_csv(export_path, index=False)
        return f"Guest list successfully exported to {export_path}"
    except Exception as e:
        return f"Export failed: {str(e)}", 500

if __name__ == '__main__':
    print("Starting Flask server...")
    print(f"Template folder path: {os.path.abspath(app.template_folder)}")
    app.run(debug=True, host='0.0.0.0', port=5000)