import uuid
import caldav
import urllib.parse

# Caldav url
# XXX
url = "https://USER:PASS@HOSTNAME/remote.php/dav/"
CAL_NAME = "todos"

# Connect
client = caldav.DAVClient(url)
principal = client.principal()
calendars = principal.calendars()

# Find the right calendar
calendar = None
for c in calendars:
    if c.name == CAL_NAME:
        calendar = c

if calendar == None:
    print("Could not connect to calendar!")
    exit(1)


def get_todos():
    todos = []
    for todo in calendar.todos():
        data_raw = todo.data
        data_lines = data_raw.splitlines()
        data = dict(e.split(":", 1) for e in data_lines)

        todos.append((data['SUMMARY'], todo))

    return todos


def delete_todo(todo):
    todo.delete()

def add_todo(summary):
    # Escape newlines
    summary = summary.replace("\n", "\\n")

    # Create unique UID for the event
    uid = str(uuid.uuid4())[:16]
    vcal = f"""
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VTODO
UID:{uid}
SUMMARY:{summary}
END:VTODO
END:VCALENDAR
"""

    calendar.add_todo(vcal)

