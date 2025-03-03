🚗 Automax - Used Car Marketplace
Automax is a Django-powered web application for buying and selling used cars. Users can list cars for sale, place bids, filter cars by various attributes, and like cars. The platform includes authentication, ensuring that only registered users can interact with the system.

✨ Features
✅ User Registration & Authentication (via Django Auth)
✅ List Used Cars (CRUD operations for sellers)
✅ Bidding System (Users can bid for cars they are interested in)
✅ Filter & Search (Filter by model, VIN number, color, etc.)
✅ Car Likes (Users can like their favorite cars)
✅ Bootstrap 5 Styling (Modern UI with responsive design)
✅ Django Forms (Enhanced with crispy-forms)

🛠 Tech Stack
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap 5
Database: Django ORM
Authentication: Django Auth
Forms Handling: Django Forms + Crispy Forms

🚀 Installation & Setup
1️⃣ Clone the Repository
```
git clone <repo-url>
cd automax
```

2️⃣ Create a Virtual Environment
```
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

4️⃣ Apply Migrations
```
python manage.py migrate
```

5️⃣ Create a Superuser (Admin Panel Access)
```
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

6️⃣ Run the Server
```
python manage.py runserver
Open http://127.0.0.1:8000/ in your browser.
```

🖼 Screenshot
![django4](https://github.com/user-attachments/assets/a815606a-b37d-4974-bf62-896ca0f43a8d)



🔐 Authentication & Authorization
Users must register and log in before listing cars or bidding.
Only the car owner can edit or delete their listings.
Buyers can only bid, like, and filter cars.
Email is sent to user that listed the car if anyone is interested in buying.
