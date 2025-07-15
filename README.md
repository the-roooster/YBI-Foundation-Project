# YBI-Foundation-Project
# Event Guest List Manager

A web application and CLI tool for managing event guest lists with RSVP tracking, built with Python (Flask for web version) and Pandas for data handling.

## Features
- **Web Interface** (Flask):
  - Add guests with name, event, and RSVP status
  - View all guests in a table format
  - Export guest list to CSV
  - Form validation and error handling
- **CLI Version**:
  - Interactive menu system
  - Add/view guests
  - Attendance summary statistics
  - CSV export functionality
- **Common Features**:
  - Prevents duplicate guest-event combinations
  - Valid RSVP status enforcement (Attending/Not Attending/Pending)
  - Pandas-based data handling for CSV exports
