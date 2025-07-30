# Day 68 - Flask Authentication

## Secure User Authentication System

This project demonstrates how to implement secure user authentication in Flask using Flask-Login, password hashing, and session management.

### Features:
- **User Registration**: New user signup with email validation
- **Secure Login**: Password hashing with Werkzeug security
- **Session Management**: Flask-Login handles user sessions
- **Protected Routes**: Login-required decorator for restricted content
- **File Downloads**: Authenticated users can download protected files
- **Flash Messages**: User feedback for authentication events

### Key Technologies:
- **Flask-Login**: User session management and authentication
- **Werkzeug Security**: Password hashing with PBKDF2 and salt
- **SQLAlchemy**: User data persistence
- **Flask Flash Messages**: User feedback system
- **Bootstrap**: Responsive UI styling

### Authentication Flow:
1. **Registration**: 
   - User submits registration form
   - Check if email already exists
   - Hash password with salt
   - Create new user in database
   - Automatically log in new user

2. **Login**:
   - User submits credentials
   - Verify email exists in database
   - Check password hash
   - Create user session
   - Redirect to protected content

3. **Protected Access**:
   - `@login_required` decorator checks authentication
   - Redirect to login if not authenticated
   - Access granted if authenticated

### Security Features:
- **Password Hashing**: PBKDF2 with SHA256 and 8-byte salt
- **Session Security**: Flask-Login manages secure sessions
- **Input Validation**: Required form fields
- **Duplicate Prevention**: Email uniqueness check
- **Safe Redirects**: Proper redirect handling

### Database Schema:
```python
class User(UserMixin, db.Model):
    id: int (Primary Key)
    email: str (Unique)
    password: str (Hashed)
    name: str
```

### Routes:
- `GET /` - Public homepage
- `GET/POST /register` - User registration
- `GET/POST /login` - User login
- `GET /logout` - User logout
- `GET /secrets` - Protected page (login required)
- `GET /download` - Protected file download

### Installation:
```bash
pip install flask flask-sqlalchemy flask-login
```

### Usage:
1. Run: `python main.py`
2. Visit `http://localhost:5000`
3. Register a new account
4. Login to access protected content
5. Download protected files

### Authentication Best Practices:
- Never store plain text passwords
- Use strong hashing algorithms (PBKDF2, bcrypt, scrypt)
- Implement proper session management
- Validate user input
- Provide clear user feedback
- Handle authentication errors gracefully

This project teaches fundamental web authentication concepts and secure user management in Flask applications.
