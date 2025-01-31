# ProductivityApp

A simple, collaborative productivity app for task management and organization.

📌 Features

✅ User authentication (sign-up & login)

✅ Task creation, editing, and deletion

✅ Task categorization and prioritization

✅ Community-based task sharing (optional)

✅ Intuitive UI with smooth navigation


⚙️ Tech Stack

Frontend: Kivy (Python)

Backend: MySQL (database), Python

Database: MySQL

Authentication: Custom authentication system

🚀 Installation & Setup
# 1. Clone the Repository

git clone https://github.com/yourusername/productivity-app.git

cd productivity-app

# 2. Set Up a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  (Mac/Linux)
venv\Scripts\activate  (# Windows)
# 3. Install Dependencies

pip install -r requirements.txt

4. Set Up MySQL Database

Create a MySQL database:

sql

Copy

Edit

CREATE DATABASE productivity_app;

Update database credentials in config.py:

DB_HOST = "your_host"

DB_USER = "your_user"

DB_PASSWORD = "your_password"

DB_NAME = "productivity_app"

# 5. Run the Application
python main.py
# 📖 Usage
Register or log in to your account.

Add new tasks, set deadlines, and mark them as complete.

Navigate through different screens using the menu.

View shared tasks from the community (once enabled).

# 1. Fork & Clone the Repository
git clone https://github.com/yourusername/productivity-app.git
# 2. Create a Feature Branch
git checkout -b feature-branch
# 3. Make Your Changes & Commit
git commit -m "Added new feature"
# 4. Push & Create a Pull Request
git push origin feature-branch

# 📝 License
This project is licensed under the MIT License.

# 📬 Contact
For questions or collaboration, reach out at twregis05@gmail.com or open an issue on GitHub.
