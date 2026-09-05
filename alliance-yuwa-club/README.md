# Alliance Yuwa Club

Official website and digital platform for **Alliance Yuwa Club**, a youth
and social welfare organization based in Biratnagar, Nepal.

> **Unity. Leadership. Service.**

Website:
https://allianceyuwaclub.org.np

---

## About the Project

Alliance Yuwa Club works to empower local youth and serve the community
through:

- Community and social welfare
- Environmental initiatives
- Youth leadership
- Civic awareness
- Sports
- Cultural programs
- Public awareness activities
- Collaboration with local authorities and community organizations

The organization has approximately six years of activity history and has
conducted more than 100 programs and activities.

This project provides the organization's official online presence and
creates a foundation for future digital member and volunteer management.

---

## Project Status

### V1 — In Development

Current development priorities:

- Public organization website
- Activities archive
- Events
- News and updates
- Executive committee
- Membership applications
- Contact system
- Gallery foundation
- Django Admin content management

Future versions may include:

- Member accounts
- Member profiles
- Ward-based coordination
- Volunteer management
- Attendance
- Event participation
- Certificates
- Notifications
- Custom administration dashboard

---

## Technology Stack

### Frontend

- React
- Vite
- React Router
- Axios
- ESLint
- Prettier
- Framer Motion

### Backend

- Python
- Django
- Django REST Framework
- django-cors-headers

### Database

- PostgreSQL for production
- SQLite may be used during early local development

### Development

- Git
- GitHub
- VS Code
- GitHub Copilot
- OpenAI Codex

---

## Project Structure

```text
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
│   └── manage.py
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
│   ├── DEVELOPMENT.md
│   ├── AI_CHANGELOG.md
│   └── DESIGN_SYSTEM.md
│
├── .gitignore
└── README.md
Documentation

The docs/ directory is the source of truth for project development.

Requirements

docs/REQUIREMENTS.md

Defines what the V1 website must do.

Architecture

docs/ARCHITECTURE.md

Defines how the system is structured.

Database

docs/DATABASE.md

Defines the database entities, fields, relationships, indexing,
ordering, deletion behavior, and publication rules.

API

docs/API.md

Defines the REST API contract between the React frontend and Django
backend.

Development

docs/DEVELOPMENT.md

Defines development workflow, coding standards, testing, Git practices,
and AI-assisted development rules.

AI Changelog

docs/AI_CHANGELOG.md

Records significant AI-assisted implementations and explains why they
were made.

Design System

docs/DESIGN_SYSTEM.md

Defines the visual identity, color system, typography, layout, motion,
responsive behavior, and frontend design rules.

Local Development
Backend

Navigate to the backend:

cd backend

Activate the virtual environment.

Windows PowerShell
.\venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Run Django checks:

python manage.py check

Run migrations:

python manage.py migrate

Start the development server:

python manage.py runserver

Backend:

http://127.0.0.1:8000/

Health check:

http://127.0.0.1:8000/api/health/
Frontend

Open another terminal:

cd frontend

Install dependencies:

npm install

Start the development server:

npm run dev

Frontend:

http://localhost:5173/
Environment Variables

Environment-specific values must not be committed to Git.

The backend should use environment variables such as:

SECRET_KEY
DEBUG
DATABASE_URL
ALLOWED_HOSTS
CORS_ALLOWED_ORIGINS
CSRF_TRUSTED_ORIGINS
FRONTEND_BASE_URL
USE_SUPABASE_STORAGE
SUPABASE_STORAGE_BUCKET
SUPABASE_S3_ACCESS_KEY_ID
SUPABASE_S3_SECRET_ACCESS_KEY
SUPABASE_S3_ENDPOINT_URL
EMAIL_PROVIDER
RESEND_API_KEY
EMAIL_FROM_EMAIL
EMAIL_FROM_NAME
EMAIL_REPLY_TO

Create a local .env file when required.

Never commit:

.env

Production secrets must be configured through the production hosting
environment.

When DEBUG=False, DATABASE_URL, ALLOWED_HOSTS, CORS_ALLOWED_ORIGINS,
CSRF_TRUSTED_ORIGINS, and durable media storage configuration are required.

Production email uses Resend over HTTPS. Supply `RESEND_API_KEY` through the
Render backend environment, after verifying the organization domain with
Resend and adding its DNS records in Cloudflare. Never expose it to the
frontend.

Backend Apps

The Django backend is divided into focused applications:

App	Responsibility
core	Shared/global functionality
activities	Club activity and program archive
events	Upcoming and past events
news	News and organizational updates
team	Executive committee/team
memberships	Membership applications
gallery	Albums and images
contact	Contact messages

config is the Django project configuration package and is not a
feature application.

Development Principles

This project follows these principles:

Keep the architecture simple.
Implement only documented requirements.
Prefer reusable code over duplication.
Avoid unnecessary dependencies.
Avoid premature abstraction.
Protect private data.
Keep the frontend and backend separated.
Use database-driven content.
Test important functionality.
Keep documentation synchronized with implementation.
AI-Assisted Development

GitHub Copilot and OpenAI Codex are used as implementation assistants.

AI agents must read the relevant documentation before making changes.

The documentation is the source of truth.

AI agents must:

Inspect existing code before modifying it.
Reuse existing functionality.
Implement the minimum necessary code.
Avoid unnecessary dependencies.
Avoid undocumented features.
Avoid changing the architecture without approval.
Add tests for important functionality.
Update docs/AI_CHANGELOG.md for significant changes.

AI should suggest future improvements rather than silently implementing
them.

Design Direction

The website should have a distinctive Alliance Yuwa Club identity.

The visual direction combines:

Strong typography
Editorial composition
Real organizational photography
Youth-oriented energy
Community-focused storytelling
Subtle and purposeful motion

The official club logo is the source of the visual color identity.

The design must not fall back to generic AI-generated SaaS, NGO, startup,
or portfolio layouts.

See:

docs/DESIGN_SYSTEM.md
Git Workflow

Use meaningful commit messages.

Examples:

feat: add activity model
feat: implement activities API
feat: create homepage
fix: validate membership email
docs: update API specification
refactor: simplify activity serializer
test: add membership API tests

The main branch should represent a stable version of the project.

Testing

Backend:

python manage.py check
python manage.py test

Linting:

ruff check .

Formatting:

ruff format --check .

Frontend:

npm run lint

Additional tests should be added as the application grows.

Deployment

Production deployment will use:

Frontend → React
Backend  → Django
Database → PostgreSQL
Domain   → allianceyuwaclub.org.np

The final hosting providers and deployment configuration will be
documented when production deployment begins.

Production must use:

HTTPS
Secure environment variables
Production database
Proper CORS configuration
Proper CSRF configuration
Debug disabled
Contributing

Before making significant changes:

Read the relevant documentation.
Inspect existing implementation.
Make the smallest necessary change.
Test the change.
Update documentation when required.
Update AI_CHANGELOG.md when the change is significantly
AI-generated.
Create a meaningful Git commit.
License

The Alliance Yuwa Club website and its content belong to Alliance Yuwa
Club unless otherwise stated.

Code licensing and public repository status should be finalized by the
organization before open-source publication.

Alliance Yuwa Club

Unity. Leadership. Service.

Biratnagar, Nepal
