import http.server
import socketserver
import json
import sqlite3 #database choice -> SQlite
import base64
import hashlib

# Define the PHR class
class PHR:
    #In this class there are helper functions that will execute the CRUD operations for our PHR system
    #create a database if it does not exsit 
    def __init__(self):
        self.conn = sqlite3.connect('phr.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                record_id INTEGER PRIMARY KEY,
                full_name text,
                dob text,
                sex text,
                allergies text,
                medications text,
                diagnosis text,
                treatment text,
                notes text
            )
        ''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                               (username text, password_hash text)''')
        
    #helper function to get one record
    def view_records(self, record_id):
        self.cursor.execute("SELECT * FROM records WHERE record_id=?", (record_id))
        return [dict(zip([column[0] for column in self.cursor.description], row)) for row in self.cursor.fetchall()]
    
    #helper function get all the records
    def view_all_records(self):
        self.cursor.execute("SELECT * FROM records")
        return [dict(zip([column[0] for column in self.cursor.description], row)) for row in self.cursor.fetchall()]
    
    def add_record(self, record_id, full_name, dob, sex, allergies, medications, diagnosis, treatment, notes):
        self.cursor.execute(
            "INSERT INTO records (record_id, full_name, dob, sex, allergies, medications, diagnosis, treatment, notes) VALUES (?,?,?,?,?,?,?,?,?)", (record_id, full_name, dob, sex, allergies, medications, diagnosis, treatment, notes)
        )
        self.conn.commit()

    #helper function to update one record 
    def update_record(self, record_id, full_name, dob, sex, allergies, medications, diagnosis, treatment, notes):
        self.cursor.execute(
            "UPDATE records SET full_name=?, dob=?, sex=?, allergies=?, medications=?, diagnosis=?, treatment=?, notes=? WHERE record_id=?", 
            (full_name, dob, sex, allergies, medications, diagnosis, treatment, notes, record_id)
        )
        self.conn.commit()
    
    #helper function to delete a record
    def delete_record(self, record_id):
        self.cursor.execute("DELETE FROM records WHERE record_id=?", (record_id,))
        self.conn.commit()

    #helper function to check if there is a user
    def check_user(self, username, password):
        self.cursor.execute("SELECT password_hash FROM users WHERE username=?", (username,))
        result = self.cursor.fetchone()
        if result is None:
            return False
        return result[0] == hashlib.sha256(password.encode()).hexdigest()
    
    #helper function to add a new record
    def add_user(self, username, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute("INSERT INTO users VALUES (?,?)", (username, password_hash))
        self.conn.commit()

#HTTP request handler
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    #function to define the auth
    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"PHR\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    #this function will check the user's credentinals to see if they are in the system
    def check_credentials(self, headers):
        auth_header = headers.get('Authorization')
        if not auth_header:
            return False
        auth_type, auth_string = auth_header.split(' ')
        if auth_type != 'Basic':
            return False
        auth_string = base64.b64decode(auth_string).decode('utf-8')
        username, password = auth_string.split(':')
        return phr_system.check_user(username, password)
    
    #do_GET method this is responsible for getting records
    def do_GET(self):
        if not self.check_credentials(self.headers):
            self.do_AUTHHEAD()
            self.wfile.write(b'Unauthorized')
            return

        if self.path.startswith('/records/'):
            record_id = self.path.split('/')[2]  #Assuming the record_id is in the URL path after /records/
            records = phr_system.view_records(record_id)
        elif self.path == '/':
            auth_header = self.headers.get('Authorization')
            auth_type, auth_string = auth_header.split(' ')
            auth_string = base64.b64decode(auth_string).decode('utf-8')
            username, password = auth_string.split(':')
            records = phr_system.view_all_records(username)
        else:
            self.send_response(404)
            self.wfile.write(b'Not Found')
            return

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(records).encode())

    #do_POST method this is responssible for creating new records
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode())

        if self.path == '/register':
            username = data['username']
            password = data['password']
            phr_system.add_user(username, password)
            self.send_response(200)
        elif self.path == '/records':
            if not self.check_credentials(self.headers):
                self.do_AUTHHEAD()
                self.wfile.write(b'Unauthorized')
                return 
            record_id = data['record_id']
            full_name = data['full_name']
            dob = data['dob']
            sex = data['sex']
            allergies = data['allergies']
            medications = data['medications']
            diagnosis = data['diagnosis']
            treatment = data['treatment']
            notes = data['notes']
            phr_system.add_record(record_id, full_name, dob, sex, allergies, medications, diagnosis, treatment, notes)
            self.send_response(200)
        else:
            self.send_response(404)
            self.wfile.write(b'Not Found')

        self.end_headers()

    #do_PUT method this is responssible for updating records
    def do_PUT(self):
        if not self.check_credentials(self.headers):
            self.do_AUTHHEAD()
            self.wfile.write(b'Unauthorized')
            return

        if self.path.startswith('/records/'):
            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length)
            data = json.loads(put_data.decode())
            record_id = self.path.split('/')[2]  #Assuming the record_id is in the URL path after /records/
            full_name = data['full_name']
            dob = data['dob']
            sex = data['sex']
            allergies = data['allergies']
            medications = data['medications']
            diagnosis = data['diagnosis']
            treatment = data['treatment']
            notes = data['notes']
            phr_system.update_record(record_id, full_name, dob, sex, allergies, medications, diagnosis, treatment, notes)
            self.send_response(200)
        else:
            self.send_response(404)
            self.wfile.write(b'Not Found')

        self.end_headers()

    #do_DELETE method this is responssible for deleting records
    def do_DELETE(self):
        if not self.check_credentials(self.headers):
            self.do_AUTHHEAD()
            self.wfile.write(b'Unauthorized')
            return

        if self.path.startswith('/records/'):
            record_id = self.path.split('/')[2]  #Assuming the record_id is in the URL path after /records/
            phr_system.delete_record(record_id)
            self.send_response(200)
        else:
            self.send_response(404)
            self.wfile.write(b'Not Found')

        self.end_headers()


#Initialize the PHR system use in the methods 
phr_system = PHR() 

#Connect on port 8000
PORT = 8000
Handler = RequestHandler

# Start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Listening on port", PORT)
    httpd.serve_forever()