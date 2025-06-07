# 🛒 E-commerce Sales Chatbot

This is a full-stack chatbot application built as part of the **Uplyft.ai Full Stack Internship Case Study (June 2025)**. The project simulates product discovery and purchase interactions on an e-commerce platform using a conversational UI.

---

## ✨ Features

- 🔐 **Mock Login System**  
  Basic authentication using hardcoded credentials

- 💬 **Chatbot Interface**  
  Users can enter product-related queries to fetch matching items

- 📦 **Flask Backend + SQLite**  
  REST API that fetches products from a mock inventory of 100+ items

- 🕒 **Timestamps + Session Tracking**  
  Messages display timestamps, and chats persist across sessions

- 💾 **Chat History with LocalStorage**  
  Previous conversations are saved locally and reloaded on page refresh

- ♻️ **Reset Chat Functionality**  
  Clears localStorage and resets session

- 📱 **Responsive Design**  
  Works on both desktop and mobile browsers

---

## ⚙️ Tech Stack

| Layer      | Technology                 |
|------------|----------------------------|
| Frontend   | React, JavaScript, CSS     |
| Backend    | Flask (Python)             |
| Database   | SQLite3                    |
| Mock Data  | Faker (Python)             |
| API Format | REST (JSON)                |
| Tools      | Axios, LocalStorage        |

---

## 📁 Project Structure

### Frontend – React App


frontend/
├── src/
│   ├── components/
│   │   ├── Login.jsx       # Login form
│   │   └── Chatbot.jsx     # Chat window
│   ├── App.jsx
│   ├── styles.css          # Global styles
│   └── index.js


### Backend – Flask App


backend/
├── app.py                  # Main Flask app with /api/products
├── db_init.py              # Script to populate the database
├── models.py               # Database schema
├── config.py               # Config constants
├── database.db             # SQLite DB (auto-created)
└── requirements.txt        # Backend dependencies


---

## 🚀 Getting Started Locally

### Backend (Flask)


cd backend
pip install -r requirements.txt
python db_init.py         # Creates DB with 100+ mock products
python app.py             # Starts Flask server at http://localhost:5000


### Frontend (React)


cd frontend
npm install
npm start                 # Starts React app at http://localhost:3000


---

## 🔐 Login Credentials

\`\`\`
Username: admin
Password: 1234
\`\`\`

---

## 🧪 Sample Chat Queries

Try asking about:

- Books
- Electronics
- Textiles
- matrix
- bottom-line
- wireless

The chatbot will fetch products from those categories or with matching keywords in the name/description.

---

## 🖼️ Screenshots

### 🔐 Login Screen

![Login Screen](screenshots/login.png)

### 🤖 Chatbot Interface

![Chat Interface](screenshots/chat.png)

### 📦 Product Cards

![Product Cards](screenshots/products.png)

> _Screenshots can be placed in a `screenshots/` folder in your repo._

---

## 📚 Learnings

- Built a full-stack chatbot app from scratch
- Implemented Flask REST API and React frontend with live state handling
- Used SQLite with Faker to generate mock data
- Applied UI/UX principles to build a clean, responsive chatbot interface
- Persisted chat sessions using localStorage
- Handled query filtering in SQL with partial matches across multiple fields

---

## ✅ Project Requirements Covered

| Requirement                      | Status  |
|----------------------------------|---------|
| Chatbot Interface                | ✅ Done |
| Backend API with product data    | ✅ Done |
| 100+ Mock products               | ✅ Done |
| Responsive UI                    | ✅ Done |
| Chat History Persistence         | ✅ Done |
| Reset Chat + Timestamps          | ✅ Done |
| Project Report & Documentation   | ✅ Done |

---

## 👤 Author

**Yogaraja Adithya Somasundar**  
Berlin, Germany  
Full Stack Intern Applicant — [Uplyft.ai](https://www.linkedin.com/company/uplyft-ai/)

---

## 📂 Submission Deliverables

- ✅ GitHub Repository (source code + README)
- ✅ Project Report (PDF)
- ✅ Presentation Slides (PPT)
