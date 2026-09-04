# Alliance Yuwa Club

Official website and digital platform for **Alliance Yuwa Club**, a youth
and social welfare organization based in Biratnagar, Nepal.

> **Unity. Leadership. Service.**

Website:
https://allianceyuwaclub.com.np

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
