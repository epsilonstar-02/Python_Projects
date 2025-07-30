# Day 67 - Blog with Authentication

## Advanced RESTful Blog with User Authentication

This project builds upon previous Flask knowledge to create a full-featured blog with user authentication, role-based access control, and comment functionality.

### Features:
- **User Authentication**: Registration, login, logout with password hashing
- **Role-Based Access**: Admin-only post creation, editing, and deletion
- **Comment System**: Authenticated users can comment on posts
- **Rich Text Editor**: CKEditor integration for post and comment creation
- **Gravatar Integration**: Profile pictures for comment authors
- **Responsive Design**: Bootstrap 5 styling with custom Clean Blog theme

### Key Technologies:
- **Flask-Login**: Session management and user authentication
- **Flask-WTF**: Form handling and CSRF protection
- **Flask-CKEditor**: Rich text editing capabilities
- **Flask-Bootstrap**: Bootstrap integration
- **Flask-Gravatar**: Profile picture generation
- **Werkzeug Security**: Password hashing and verification
- **SQLAlchemy**: Database ORM with relationships

### Database Models:

#### User Model:
- `id` - Primary key
- `email` - Unique user email
- `password` - Hashed password
- `name` - User display name
- `posts` - One-to-many relationship with BlogPost
- `comments` - One-to-many relationship with Comment

#### BlogPost Model:
- `id` - Primary key
- `title` - Post title (unique)
- `subtitle` - Post subtitle
- `date` - Publication date
- `body` - Post content (rich text)
- `img_url` - Header image URL
- `author_id` - Foreign key to User
- `author` - Many-to-one relationship with User
- `comments` - One-to-many relationship with Comment

#### Comment Model:
- `id` - Primary key
- `text` - Comment content
- `author_id` - Foreign key to User (commenter)
- `post_id` - Foreign key to BlogPost
- `comment_author` - Many-to-one relationship with User
- `parent_post` - Many-to-one relationship with BlogPost

### Authentication Features:
- **Registration**: New user signup with form validation
- **Login**: Secure authentication with session management
- **Password Security**: Werkzeug PBKDF2 hashing with salt
- **Access Control**: Admin decorator for protected routes
- **Session Management**: Flask-Login handles user sessions

### Admin Functionality:
- Only user with ID 1 has admin privileges
- Admin can create, edit, and delete blog posts
- Admin controls are hidden from regular users
- Decorator-based route protection

### Comment System:
- Authenticated users can comment on posts
- Comments display with Gravatar profile pictures
- Rich text commenting with CKEditor
- Comments linked to both user and post

### Installation Requirements:
```bash
pip install flask flask-sqlalchemy flask-login flask-wtf flask-ckeditor flask-bootstrap flask-gravatar
```

### Usage:
1. Run the application: `python main.py`
2. Register as a new user or login
3. Browse blog posts and leave comments
4. Admin users can create and manage posts

### Routes:
- `GET /` - Homepage with all blog posts
- `GET/POST /register` - User registration
- `GET/POST /login` - User login
- `GET /logout` - User logout
- `GET/POST /post/<id>` - Individual post with comments
- `GET/POST /new-post` - Create new post (admin only)
- `GET/POST /edit-post/<id>` - Edit post (admin only)
- `GET /delete/<id>` - Delete post (admin only)
- `GET /about` - About page
- `GET /contact` - Contact page

This project demonstrates advanced Flask concepts including authentication, authorization, database relationships, and full-stack web development practices.
