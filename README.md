# Bulk Offer Letter Generator and Certificate Verifier

This project is designed to streamline the process of generating offer letters in bulk for interns and verifying their certificates using a Flask-based API. It uses a SQLite database to store intern details and provides an API endpoint for certificate verification.

---

## Features

1. **Bulk Offer Letter Generation**:
   - Automates the creation of offer letters for multiple interns.
   - Uses a predefined template to generate personalized letters.

2. **Certificate Verification API**:
   - Provides a `/verify` endpoint to validate certificates using a unique code.
   - Returns intern details if the certificate is valid.

3. **SQLite Database**:
   - Stores intern details such as name, email, date, status, and unique code.

---

## File Descriptions

### 1. `verify_api.py`
- **Purpose**: A Flask-based API to verify certificates.
- **Key Features**:
  - Connects to a SQLite database (`interns.db`).
  - Fetches intern details based on a unique code.
  - Returns a JSON response indicating whether the certificate is valid.

### 2. `database.py`
- **Purpose**: Initializes the SQLite database and creates the `interns` table.
- **Key Features**:
  - Sets up the database schema for storing intern details.

### 3. `offer_letter_generator.py` (to be implemented)
- **Purpose**: Generates offer letters in bulk for interns.
- **Key Features**:
  - Reads intern details from the database.
  - Uses a template to create personalized offer letters.
  - Saves the letters as PDF or Word documents.

---

## How to Clone and Use This Project

### Step 1: Clone the Repository
Clone the repository to your local machine:
```bash
git clone <repository-url>
