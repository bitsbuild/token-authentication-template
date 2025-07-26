# 🔐 Token Authentication Template Using DRF

This Repository Serves As A Boilerplate For Building REST APIs Using Django REST Framework (DRF) With Token-Based Authentication. It Is Designed To Accelerate Backend Development By Providing A Clean, Modular, And Extensible Structure Out-Of-The-Box.

🔗 **Repository URL:** [https://github.com/bitsbuild/token-authentication-template-using-drf.git](https://github.com/bitsbuild/token-authentication-template-using-drf.git)

---

## 🚀 Features

- 🔐 **Token-Based Authentication** using `rest_framework.authtoken`
- 👤 **User Registration With Validation**
  - Checks for existing username and email
  - Confirms matching password and confirm_password
  - Secure password hashing using `set_password`
- 🔑 **Login** via token generation endpoint
- ❌ **Delete Authenticated User**
- 🔒 Passwords are never returned in responses
- 📦 Clean and modular serializer-based logic

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/bitsbuild/token-authentication-template-using-drf.git
cd token-authentication-template-using-drf/tokenauth
````

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run Development Server

```bash
python manage.py runserver
```

---

## 🔑 API Endpoints

| Method | Endpoint     | Description                         |
| ------ | ------------ | ----------------------------------- |
| POST   | `/create/`   | Register a new user                 |
| POST   | `/gettoken/` | Obtain authentication token (login) |
| DELETE | `/delete/`   | Delete the authenticated user       |

---

## 📬 Example Usage

### 🔹 Register User

```http
POST /create/
Content-Type: application/json

{
  "username": "myuser",
  "email": "myuser@example.com",
  "password": "mypassword",
  "confirm_password": "mypassword"
}
```

✅ Validations:

* Username must be unique
* Email must be unique
* Password and Confirm Password must match

---

### 🔹 Get Token

```http
POST /gettoken/
Content-Type: application/json

{
  "username": "myuser",
  "password": "mypassword"
}
```

**Response:**

```json
{
  "token": "abcd1234efgh5678..."
}
```

---

### 🔹 Delete Authenticated User

```http
DELETE /delete/
Authorization: Token abcd1234efgh5678...
```

---

## 🧪 Testing Tips

* Use [Postman](https://www.postman.com/), [Insomnia](https://insomnia.rest/), or `curl`
* Always pass the token in the header for protected routes:

```http
Authorization: Token <your-token>
```

---

## 📌 Use Cases

* 🧱 DRF Token Auth Boilerplate For New Projects
* 🧪 Learning DRF Serializers & Auth Flows
* 🚀 Starting Point For Any Auth-Enabled Django API

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

**Built With ❤️ Using Django + DRF**
