# League of Legends Role CMS

This is a simple Django-based Content Management System (CMS) that presents guides and articles about the five main roles in the game **League of Legends** — Top, Jungle, Mid, Bottom (ADC), and Support.

---

## 🧠 Project Overview

The application allows users to:

- View a homepage with a list of role-specific articles
- Visit a **detail page** for each article, author, and role (category)
- Navigate between articles, their authors, and categories
- Manage content via Django Admin interface
- Load sample data via Django fixtures

---

## 🧱 Data Models

The project includes three Django models:

- **Category**: Represents one of the five main roles (Top, Jungle, Mid, Bottom, Support)
- **Article**: A guide related to a champion or role, linked to a category and one or more authors
- **Author**: The creator of a guide (can be real or fictional)

### Relationships:

- 1:N between **Category** and **Article**
- M:N between **Article** and **Author**

---

## 📁 Sample Data (Fixtures)

Sample content is included in the file:  
`content/fixtures/articles.json`

To load the sample data into the database, run:

```bash
python manage.py loaddata content/fixtures/articles.json
