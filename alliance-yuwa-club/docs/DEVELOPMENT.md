# Alliance Yuwa Club
## Development Guide — V1

---

## 1. Purpose

This document defines the development workflow, coding standards,
testing practices, Git workflow, and AI-assisted development rules for
the Alliance Yuwa Club website.

The project will be developed using Django for the backend and React
for the frontend.

The goal is to produce a maintainable production-ready website within
the initial launch period while keeping the architecture simple enough
for future development.

---

# 2. Development Environment

## Backend

Backend development will use:

- Python
- Django
- Django REST Framework
- PostgreSQL for production
- SQLite may be used during initial local development

Python dependencies must be installed inside the backend virtual
environment.

Example:

```text
backend/
└── venv/

The virtual environment must never be committed to Git.

Frontend

Frontend development will use:

Node.js
React
Vite
React Router
Axios
ESLint
Prettier

Node dependencies must remain inside the frontend project.

The node_modules directory must never be committed to Git.

3. Local Project Structure
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
│
├── .gitignore
└── README.md
4. Environment Variables

Environment-specific and secret values must not be hardcoded.

The backend should use environment variables for values such as:

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

A local .env file may be used during development.

The .env file must never be committed to Git.

A safe example file such as .env.example may be committed.

Example:

SECRET_KEY=replace-me
DEBUG=True
DATABASE_URL=replace-me
ALLOWED_HOSTS=localhost,127.0.0.1

Production values must be stored in the hosting provider's environment
configuration.

When DEBUG=False, DATABASE_URL, ALLOWED_HOSTS, CORS_ALLOWED_ORIGINS,
CSRF_TRUSTED_ORIGINS, and durable media storage configuration are required.

5. Python Coding Standards

Python code must follow normal modern Python and Django conventions.

General rules:

Use clear descriptive names.
Prefer small functions and methods.
Avoid unnecessary abstraction.
Follow PEP 8 where practical.
Use type hints where they improve readability.
Keep business logic out of serializers when it belongs in a service
or model layer.
Avoid duplicated logic.
Write code that another developer can understand without AI assistance.
6. Python Linting

The backend will use Ruff.

Ruff should be configured in:

backend/pyproject.toml

Ruff will be used for:

Linting
Import sorting
Common Python code-quality checks

Before committing backend changes, run:

ruff check .

Formatting should be checked using:

ruff format --check .

When formatting changes are required:

ruff format .
7. React / JavaScript Coding Standards

React code should follow these principles:

Use functional components.
Use React hooks where appropriate.
Keep components small and reusable.
Avoid unnecessary global state.
Keep API calls separate from presentation components where practical.
Use descriptive component and variable names.
Do not duplicate UI logic unnecessarily.
Keep pages responsible for page-level composition.
Keep reusable UI elements inside the components directory.
Avoid unnecessary dependencies.
8. Frontend Linting and Formatting

The frontend will use:

ESLint
Prettier

Before committing frontend changes:

npm run lint

Formatting should be checked using the project's Prettier
configuration.

The project should maintain a consistent formatting style across all
frontend files.

9. Django Model Development

When modifying Django models:

Update the model.
Run Django checks.
Create migrations.
Review the migration.
Apply the migration.
Run tests.

Example:

python manage.py check
python manage.py makemigrations
python manage.py migrate

Migrations are part of the source code and must be committed to Git.

Do not delete or rewrite migration history simply to make development
errors disappear.

10. API Development

All APIs must follow the specifications defined in:

docs/API.md

Before implementing an endpoint, confirm:

HTTP method.
URL.
Request structure.
Response structure.
Authentication requirement.
Permission requirement.
Validation behavior.
Pagination behavior.
Filtering behavior.

API responses should remain consistent across the project.

Breaking API changes require updating the API documentation.

11. Frontend API Integration

React must communicate with Django through the documented API.

API configuration should be centralized.

For example:

frontend/src/services/api.js

The frontend must not:

Access the database directly.
Contain database credentials.
Reimplement backend business rules unnecessarily.

Backend validation remains authoritative.

12. Testing

Testing is required for important backend functionality.

Initial testing priorities:

Models
Membership applications
Contact submissions
Public activity API
Public event API
News API
Permission-protected operations
Important validation rules

Basic Django test command:

python manage.py test

Frontend tests may be introduced where useful, but testing should not
delay the initial launch unnecessarily.

13. Manual Testing

Before a feature is considered complete, test it from the user's
perspective.

For public pages check:

Desktop layout.
Tablet layout.
Mobile layout.
Navigation.
Loading behavior.
Empty states.
Error states.
Form validation.
Broken links.

For admin functionality check:

Create.
Read.
Update.
Delete.
Authentication.
Permissions.
14. Git Workflow

Git will be used throughout development.

The main branch should always represent a stable version of the
project.

Recommended branches:

main
develop
feature/<feature-name>
fix/<issue-name>

For small changes during the rapid V1 development period, a feature
branch may be used when practical.

Examples:

feature/activity-api
feature/membership-form
feature/homepage
fix/contact-validation
15. Commit Messages

Commit messages should be clear and meaningful.

Recommended format:

feat: add activity model
feat: add public activities API
feat: create homepage
fix: validate membership email
docs: update API specification
refactor: simplify activity serializer
test: add membership API tests

Avoid vague messages such as:

update
changes
final
done
working
16. Pull Requests

For larger features, use a pull request before merging into main.

A pull request should explain:

What changed.
Why it changed.
How it was tested.
Any known limitations.

AI-generated code should be reviewed before merging.

17. AI-Assisted Development

GitHub Copilot and OpenAI Codex are approved development tools for this
project.

AI-generated code is treated as developer-generated code and must be
reviewed before being accepted.

AI coding agents must read these documents before implementing features:

docs/REQUIREMENTS.md
docs/ARCHITECTURE.md
docs/DATABASE.md
docs/API.md
docs/DEVELOPMENT.md

The documentation is the project's source of truth.

18. AI Coding Rules

Copilot and Codex must:

Follow the existing architecture.
Follow the documented database design.
Follow the documented API contract.
Avoid creating unnecessary files.
Avoid creating unnecessary dependencies.
Avoid changing unrelated files.
Avoid replacing the project's technology stack.
Never add secrets to source code.
Create migrations when models change.
Add tests for important backend behavior.
Preserve existing working functionality.
Explain significant changes when requested.
Report assumptions when requirements are unclear.
Avoid silently changing documented requirements.
Prefer simple maintainable implementations.

Sample Image Rule: Whenever a component or page requires an image, reference standard filenames from frontend/src/assets/images/sample-[name].jpg or use inline SVG placeholders. Never hardcode unmapped image paths or fail builds if physical assets are missing; provide a styled fallback element or standard sample asset reference.

19. AI Agent Workflow

Before implementing a feature, the AI agent should:

Read requirements
        ↓
Read architecture
        ↓
Read database/API specification
        ↓
Inspect existing code
        ↓
Plan the change
        ↓
Implement the feature
        ↓
Run checks/tests
        ↓
Report changed files
        ↓
Report test results

The agent should not begin by rewriting existing project files
unnecessarily.

20. Human Review Requirements

Before accepting AI-generated code, the developer should verify:

The code solves the intended problem.
The architecture has not been changed unnecessarily.
No secrets were introduced.
No unexpected dependencies were added.
Database migrations are correct.
API behavior matches API.md.
Tests pass.
The frontend works correctly.
No unrelated files were changed.

AI output must not be accepted solely because it compiles or runs.

21. Feature Completion Checklist

A feature is considered complete when:

[ ] Requirements understood
[ ] Database changes completed if required
[ ] API implemented if required
[ ] Frontend implemented if required
[ ] Validation added
[ ] Authentication/permissions checked
[ ] Tests added where appropriate
[ ] Linting passes
[ ] Formatting passes
[ ] Manual testing completed
[ ] Documentation updated if required
[ ] Git commit created
22. Development Order

Features should generally be implemented in this order:

Database/model
      ↓
Serializer
      ↓
API/view
      ↓
URL routing
      ↓
API testing
      ↓
React service
      ↓
React component/page
      ↓
Responsive styling
      ↓
Manual testing

This keeps backend and frontend responsibilities clear.

23. V1 Development Priority

Development should prioritize features in this order:

Priority 1 — Core Website
Home
About
Activities
Events
Team
News
Contact
Priority 2 — Core Management
Django Admin
Activity management
Event management
News management
Team management
Priority 3 — Community Interaction
Membership application
Contact form
Priority 4 — Media
Gallery
Activity/event images

The historical photograph organization can happen after the core
website is functional.

24. Ten-Day Launch Plan
Day 1

Project setup and architecture.

Tasks:

Repository setup.
Django setup.
React setup.
Documentation.
Environment configuration.
Initial linting configuration.
Day 2

Core backend and homepage foundation.

Tasks:

Database models.
Core API structure.
React layout.
Navbar.
Footer.
Homepage structure.
Day 3

Activities backend and frontend.

Tasks:

Activity model.
Category model.
Activity API.
Activity list page.
Activity detail page.
Filtering.
Day 4

Events and news.

Tasks:

Event model and API.
Event pages.
News model and API.
News pages.
Day 5

About, team, and contact.

Tasks:

About page.
Team model/API.
Team page.
Contact form.
Contact API.
Day 6

Membership.

Tasks:

Membership model.
Membership API.
Membership page.
Form validation.
Admin application review.
Day 7

Administration and content.

Tasks:

Django Admin customization.
Add initial real organization content.
Add activities.
Add events.
Add team information.
Add news.
Day 8

Responsive design and quality.

Tasks:

Mobile testing.
Tablet testing.
Desktop testing.
Error states.
Loading states.
Accessibility improvements.
SEO basics.
Day 9

Production deployment.

Tasks:

Production settings.
PostgreSQL.
Static/media configuration.
Backend deployment.
Frontend deployment.
Domain configuration.
HTTPS.
Day 10

Launch readiness.

Tasks:

Full testing.
Security review.
Content verification.
Broken-link check.
SEO verification.
Backup verification.
Final deployment.
Public launch.
25. Definition of Done for V1

The project is ready for launch when:

[ ] Public website is accessible.
[ ] allianceyuwaclub.org.np works.
[ ] HTTPS is enabled.
[ ] Home page works.
[ ] About page works.
[ ] Activities archive works.
[ ] Activity detail pages work.
[ ] Events page works.
[ ] News page works.
[ ] Team page works.
[ ] Membership form works.
[ ] Contact form works.
[ ] Django Admin works.
[ ] Public APIs return correct data.
[ ] Protected operations require authentication.
[ ] PostgreSQL is working in production.
[ ] Environment secrets are configured securely.
[ ] Mobile layout is usable.
[ ] No critical console errors exist.
[ ] No critical backend errors exist.
[ ] Basic SEO is configured.
[ ] Important tests pass.
[ ] Initial content has been reviewed by the organization.
26. Important Scope Rule

The 10-day launch takes priority over non-essential features.

When a feature threatens the launch schedule, the feature should be
postponed rather than introducing unnecessary complexity.

The initial goal is:

Reliable
Professional
Fast
Maintainable
Launchable

not:

Maximum number of features
27. Future Development

After V1 launch, development can continue with:

Member accounts.
Member profiles.
Ward management.
Volunteer management.
Attendance.
Event participation.
Certificates.
Notifications.
Custom administration dashboard.
Advanced analytics.

Future features should be evaluated separately and should not be added to V1 without a clear requirement.