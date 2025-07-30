# Day 69 - Adding Users to Blog

## Complete Blog Application with User Management and Deployment

This project represents the culmination of the Flask blog series, adding complete user management, email functionality, and production-ready deployment configurations.

### Features:
- **Complete User System**: Registration, login, logout with secure authentication
- **Role-Based Access Control**: Admin privileges for post management
- **Comment System**: Users can comment on posts with rich text editor
- **Email Contact Form**: Functional contact form with SMTP integration
- **Gravatar Integration**: Profile pictures for all users
- **Production Configuration**: Environment variables and deployment settings
- **Database Cascade Deletion**: Proper foreign key relationships
- **Enhanced Security**: Improved authentication checks

### New Features in Day 69:
- **Environment Variables**: Database URI and email credentials
- **SMTP Email Integration**: Functional contact form
- **Enhanced Admin Checks**: Improved security for admin routes
- **Cascade Deletion**: Comments deleted when posts are deleted
- **Production Configuration**: Debug mode disabled for production
- **Email Validation**: Enhanced form validation

### Technologies Used:
- **Flask & Extensions**: Core framework with Login, Bootstrap, CKEditor
- **SQLAlchemy ORM**: Advanced database relationships
- **Flask-Gravatar**: Profile picture integration
- **SMTP Integration**: Email functionality
- **Environment Variables**: Secure configuration management
- **Bootstrap 5**: Responsive design framework

### Database Models:

#### Enhanced User Model:
- Improved relationship management
- Better authentication handling
- Gravatar integration

#### Enhanced BlogPost Model:
- Foreign key relationships
- Cascade deletion configuration
- Author attribution

#### Enhanced Comment Model:
- Proper foreign key relationships
- Rich text support
- User attribution

### Email Integration:
```python
def send_email(name, email, phone, message):
    # SMTP configuration with environment variables
    # Secure email sending functionality
```

### Deployment Features:
- **Environment Configuration**: 
  - `DB_URI` for database connection
  - `MY_EMAIL` and `MY_PASSWORD` for SMTP
- **Production Settings**: Debug mode disabled
- **Security Enhancements**: Improved admin authentication

### Environment Variables Required:
```bash
DB_URI=your_database_connection_string
MY_EMAIL=your_smtp_email
MY_PASSWORD=your_smtp_password
```

### Installation:
```bash
pip install flask flask-sqlalchemy flask-login flask-wtf flask-ckeditor flask-bootstrap flask-gravatar
```

### Production Deployment:
1. Set environment variables
2. Configure database URI
3. Set up SMTP credentials
4. Deploy with debug=False

### Security Features:
- **Enhanced Admin Checks**: Authentication + ID verification
- **Secure Password Hashing**: PBKDF2 with salt
- **CSRF Protection**: Flask-WTF form protection
- **Input Validation**: Comprehensive form validation
- **Environment Variables**: Secure credential management

### Key Routes:
- `GET/POST /` - Homepage with all posts
- `GET/POST /register` - User registration
- `GET/POST /login` - User authentication
- `GET /logout` - Session termination
- `GET/POST /post/<id>` - Post view with comments
- `GET/POST /new-post` - Post creation (admin only)
- `GET/POST /edit-post/<id>` - Post editing (admin only)
- `GET /delete/<id>` - Post deletion (admin only)
- `GET/POST /contact` - Contact form with email
- `GET /about` - About page

### Advanced Features:
- **Rich Text Editing**: CKEditor for posts and comments
- **User Avatars**: Gravatar integration for all users
- **Email Functionality**: Contact form sends actual emails
- **Responsive Design**: Mobile-optimized interface
- **Production Ready**: Environment-based configuration

This represents a complete, production-ready blog application suitable for deployment with full user management, content creation, and communication features.
