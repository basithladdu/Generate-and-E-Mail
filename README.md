# ✉️ Bulk Offer Letter & Certificate Verifier (UQR)

Generates bulk intern offer letters and verifies certificates via a Flask API. Uses SQLite for data storage.

**✨ Features:** Bulk letter generation, certificate verification API (`/verify`), SQLite database.

**⚙️ Files:**
- `verify_api.py`: Flask API for certificate verification.
- `database.py`: Initializes the `interns` SQLite database.
- `offer_letter_generator.py` (To be Implemented): Generates bulk offer letters.

**🚀 Usage:**
1. `git clone https://github.com/basithladdu/Generate-and-E-Mail`
2. `cd uqr`
3. `pip install flask`
4. `python database.py`
5. `python verify_api.py` (API at `http://127.0.0.1:5000/verify?code=<unique_code>`)

**🛠️ Future:** Implement letter generator, email sending, API enhancements.

**📄 License:** MIT License.

**🤝 Contribute:** Fork and submit pull requests.

**📧 Contact:** Reach out for questions/feedback.

**📝 To Add README:** Save as `README.md` in `uqr`, then `git add README.md`, `git commit -m "Added README"`, `git push`.
