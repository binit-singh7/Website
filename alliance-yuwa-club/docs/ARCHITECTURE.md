# Alliance Yuwa Club
## System Architecture — V1

---

## 1. Architecture Overview

Alliance Yuwa Club V1 will use a decoupled frontend/backend architecture.

```text
                    Internet
                       |
                       v
              allianceyuwaclub.com.np
                       |
                       v
                React Frontend
                       |
                    REST API
                       |
                       v
                Django Backend
                       |
          +------------+------------+
          |                         |
          v                         v
      PostgreSQL                 Media Storage
          |
          v
    Application Data

    2. Technology Stack
Frontend
React
Vite
React Router
Axios
ESLint
Prettier
Backend
Python
Django
Django REST Framework
django-cors-headers
Database
PostgreSQL

SQLite may be used during early local development, but PostgreSQL
will be used for production.

Version Control
Git
GitHub
Development Tools
VS Code
GitHub Copilot
OpenAI Codex
Postman or Thunder Client
3. Repository Structure
alliance-yuwa-club/
│
├── backend/
│   ├── config/
│   ├── core/
│   ├── activities/
│   ├── events/
│   ├── news/
│   ├── team/
│   ├── memberships/
│   ├── gallery/
│   ├── contact/
│   ├── manage.py
│   └── venv/
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
├── docs/
│   ├── REQUIREMENTS.md
│   ├── ARCHITECTURE.md
│   ├── DATABASE.md
│   ├── API.md
│   └── DEVELOPMENT.md
│
├── .gitignore
└── README.md
4. Backend Architecture

Django is responsible for:

Database access.
Business logic.
REST API.
Authentication.
Authorization.
Content management.
Form processing.
Administrative management.

The Django Admin interface will be the primary management interface
for V1.

5. Django Applications
core

Contains shared/global functionality.

Responsibilities may include:

Organization/site information.
Global settings.
Shared utilities.
Common models if required.
activities

Responsible for the organization's activity archive.

Examples:

Community cleanup drives.
Awareness campaigns.
Leadership activities.
Sports programs.
Cultural programs.
events

Responsible for scheduled events.

Examples:

Upcoming programs.
Public events.
Internal events where appropriate.
news

Responsible for:

News articles.
Announcements.
Activity reports.
Public updates.
team

Responsible for:

Executive committee members.
Organizational positions.
Team member information.
memberships

Responsible for:

Membership applications.
Application status.
Membership-related administration.

Full member authentication is out of scope for V1.

gallery

Responsible for:

Albums.
Images.
Image ordering.
Activity/event media relationships where appropriate.

The gallery architecture must support future migration of historical
photographs.

contact

Responsible for:

Contact form submissions.
Visitor inquiries.
6. Frontend Architecture

React is responsible for:

Rendering pages.
Navigation.
User interaction.
API communication.
Form interfaces.
Responsive presentation.

React must not directly access the database.

All application data must be obtained through the Django API.

7. Frontend Routing

Initial routes:

/
 /about
 /activities
 /activities/:slug
 /events
 /events/:slug
 /news
 /news/:slug
 /team
 /membership
 /contact
8. API Communication

The frontend communicates with Django through HTTP REST APIs.

Example:

React
   |
   | GET /api/activities/
   v
Django REST Framework
   |
   v
PostgreSQL

The frontend must not contain database credentials.

9. Public vs Protected Operations
Public

These endpoints may be accessible without authentication:

Published activities.
Published events.
Published news.
Public team information.
Public organization information.
Protected

Authentication is required for:

Creating activities.
Updating activities.
Deleting activities.
Creating events.
Updating events.
Deleting events.
Managing news.
Managing team information.
Reviewing membership applications.
Viewing contact messages.
Managing gallery content.
10. Content Management Strategy

V1 will use Django Admin as the primary CMS.

This provides:

Fast development.
Reliable administration.
Authentication.
Permission handling.
Database-backed content management.

A custom React dashboard is intentionally postponed.

11. Media Architecture

The system will separate media files from application code.

Logical structure:

media/
├── activities/
├── events/
├── news/
├── team/
└── gallery/

The exact production media provider will be decided during deployment.

Historical photographs do not need to be migrated before the first
public launch.

12. Configuration

Environment-specific configuration must use environment variables.

Examples:

SECRET_KEY
DEBUG
DATABASE_URL
ALLOWED_HOSTS
CORS_ALLOWED_ORIGINS
CSRF_TRUSTED_ORIGINS

Production secrets must never be stored in Git.

13. Development Environments
Local
React
localhost:5173

Django
localhost:8000
Production

The frontend and backend may be deployed independently.

The custom domain:

https://allianceyuwaclub.com.np

will serve the public website.

The exact deployment providers will be selected before production
deployment.

14. Architectural Principles
Keep the backend and frontend clearly separated.
Prefer simple solutions over unnecessary complexity.
Follow Django and React conventions.
Do not duplicate business logic in the frontend.
Keep API contracts explicit.
Use reusable React components.
Use database-driven content.
Keep sensitive configuration out of source control.
Make the system easy for future developers to understand.
Do not introduce new technologies without a clear requirement.
15. AI Coding Rules

GitHub Copilot and OpenAI Codex may be used extensively for
implementation.

However, AI-generated code must follow these rules:

Read the documentation before modifying the project.
Follow the architecture defined in this document.
Do not replace the technology stack without explicit approval.
Do not create unnecessary Django apps.
Do not create unnecessary dependencies.
Do not modify unrelated files when implementing a feature.
Do not introduce secrets into source code.
Add tests for important backend behavior.
Keep code readable and maintainable.
Explain significant architectural changes before making them.

The documentation in docs/ is the source of truth for AI coding
agents.

16. Future Architecture

Possible future expansion:

                    React Frontend
                         |
                   Django REST API
                         |
        +----------------+----------------+
        |                |                |
    PostgreSQL       Media Storage    Background Jobs
        |
        +------------+
        |            |
     Members       Activities
        |
     Ward Groups
        |
   Volunteer System