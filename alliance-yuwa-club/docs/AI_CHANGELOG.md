# Alliance Yuwa Club
## AI Implementation Changelog

---

## 1. Purpose

This file records all significant code changes generated or substantially
implemented by AI coding agents such as GitHub Copilot and OpenAI Codex.

The purpose is to:

- Explain why a piece of code was implemented.
- Prevent unnecessary code and features.
- Prevent duplicate functionality.
- Make AI-generated code easier to review.
- Track architectural decisions.
- Make future debugging easier.
- Provide a clear history of AI-assisted development.

This file is part of the project's development documentation and must be
maintained throughout the project lifecycle.

---

# 2. Core Rule

Every significant AI-generated implementation must have a corresponding
entry in this file.

AI agents must not add code simply because:

- It might be useful later.
- It is considered a best practice without a project requirement.
- Another framework commonly uses it.
- The AI thinks the project may eventually need it.
- It makes the architecture look more sophisticated.
- It reduces a small amount of typing.
- It introduces an abstraction that is not currently necessary.

Code must have a clear purpose related to the project's documented
requirements or an approved development decision.

---

# 3. Before Writing Code

Before implementing a feature or function, the AI agent should answer:

1. What problem does this code solve?
2. Which requirement does it satisfy?
3. Which document specifies the requirement?
4. Why is this implementation necessary?
5. Is there already existing code that solves this problem?
6. Does the implementation introduce a new dependency?
7. Does the implementation change the database?
8. Does the implementation change the API?
9. Does the implementation affect existing functionality?
10. Is there a simpler implementation?

If the code is not justified by a current requirement or approved
technical decision, the AI agent should not implement it.

---

# 4. Change Entry Format

Each significant AI-generated change should use the following format:

```text
## CHANGE-XXXX — Short Description

Date:
YYYY-MM-DD

Agent:
Codex / GitHub Copilot / Other

Type:
feature / fix / refactor / security / performance / documentation

Requirement:
Reference the relevant requirement or explain why the change is needed.

Reason:
Explain the problem being solved and why this code is necessary.

Files Changed:
- path/to/file1.py
- path/to/file2.jsx

Functions / Classes / Components:
- FunctionName()
- ClassName
- ComponentName

Code Location:
- file.py: lines XX-YY
- component.jsx: lines XX-YY

Implementation:
Brief explanation of what was implemented.

Why This Approach:
Explain why this implementation was chosen instead of a more complex
or alternative approach.

Dependencies Added:
None
OR
- package-name — reason

Database Changes:
None
OR
- Model changed
- Migration created

API Changes:
None
OR
- Added endpoint
- Modified endpoint

Tests:
- Test added
- Test updated
- Manual test performed

Verification:
- Lint passed
- Tests passed
- Build passed
- Manual verification completed

Unnecessary Alternatives Considered:
Describe any approach that was intentionally not implemented and why.

Related Documentation:
- REQUIREMENTS.md
- ARCHITECTURE.md
- DATABASE.md
- API.md
- DEVELOPMENT.md


5. Line Number Requirement

AI agents should record the relevant file and approximate line range for
significant implementations.

Example:

Code Location:
- backend/activities/models.py: lines 15-48
- backend/activities/serializers.py: lines 10-37

Line numbers are expected to change as the project evolves.

Therefore line numbers are primarily intended to help with immediate
review and historical understanding.

When line numbers become outdated, the latest file location should be
used during future updates.

6. What Requires an Entry

An AI changelog entry is required for:

New Django models.
New React pages.
New API endpoints.
New database relationships.
New authentication/authorization logic.
New reusable services.
New utilities.
New dependencies.
Significant refactoring.
Security-related changes.
Performance-related changes.
Deployment-related code changes.
Major UI components.
New form-processing logic.
Old color.
New color.
Reason.
Components affected.
Accessibility considerations.
Whether the change was approved.


7. What Usually Does Not Require a Separate Entry

A separate entry is generally unnecessary for trivial changes such as:

Typo corrections.
Simple text corrections.
Formatting-only changes.
Import cleanup with no functional effect.
Automatic formatting.
Minor CSS spacing adjustments.

These may still be included in an existing feature entry when they are
part of the same implementation.

8. No Duplicate Functionality

Before adding a new function, class, component, utility, endpoint, or
dependency, the AI agent must search the existing codebase.

The agent should determine whether an existing implementation can be
reused.

Do not create:

get_activity_data()
fetch_activity_data()
load_activity_data()
retrieve_activity_data()

when one function already provides the required behavior.

Prefer reuse over duplication.

9. No Premature Abstraction

The AI agent must not create abstractions solely because they may be
useful in the future.

Do not create:

Generic frameworks for one use case.
Service layers without a demonstrated need.
Base classes used only once.
Utility modules containing one trivial function.
Configuration systems for values that never change.
Complex design patterns without a project requirement.

Start with the simplest maintainable implementation.

Refactor when actual requirements justify it.

10. Dependency Rule

Before adding a package, the AI agent must explain:

Package:
Why needed:
What existing functionality cannot solve it:
Whether it can be avoided:

Example:

Package:
Some-new-package

Why needed:
Provides functionality required for production image processing.

Existing alternative:
Django/Python standard functionality is insufficient.

Decision:
Approved.

AI agents must not add dependencies merely for convenience.

11. Database Change Rule

Before changing the database, the AI agent must explain:

What data requirement requires the change?
Why can the existing models not support it?
What relationship is being added?
What migration will be generated?
Could the change affect existing data?

Database changes must also follow:

docs/DATABASE.md
12. API Change Rule

Before adding or changing an API endpoint, the AI agent must verify:

Is the endpoint required?
Is it already available?
Who can access it?
What data does it expose?
Does it expose private information?
Does it require authentication?
How will React use it?

All public API changes must follow:

docs/API.md
13. Security Change Rule

Any code involving:

Authentication
Authorization
Passwords
Tokens
User data
Membership data
Contact data
File uploads
Administrative operations
Production secrets

requires explicit explanation in the AI changelog.

Sensitive data must not be included in changelog examples.

14. AI Implementation Procedure

AI agents should follow this sequence:

1. Read project documentation
        ↓
2. Inspect existing code
        ↓
3. Search for existing functionality
        ↓
4. Identify the minimum required change
        ↓
5. Explain the implementation plan
        ↓
6. Implement the change
        ↓
7. Run linting/tests/checks
        ↓
8. Review changed files
        ↓
9. Update AI_CHANGELOG.md
        ↓
10. Report the final change
15. Minimum Necessary Code Principle

The goal is not to produce the largest or most sophisticated
implementation.

The goal is to implement the smallest clean solution that fully satisfies
the requirement.

Prefer:

Simple
Readable
Testable
Maintainable

over:

Complex
Highly abstracted
Over-engineered
Difficult to understand
16. AI Must Not Silently Expand Scope

An AI agent must not implement additional features merely because they
seem related.

Example:

If asked to implement:

Activity filtering by year

the agent must not automatically implement:

Search
Caching
Analytics
Recommendations
Activity subscriptions
Notifications

unless those features are explicitly requested or documented.

The agent may suggest future improvements, but must not implement them
without approval.

17. Change Size

AI agents should prefer focused changes.

A change should ideally address one clear feature, bug, or task.

Avoid mixing unrelated changes such as:

Activity API
+
Navbar redesign
+
Authentication refactor
+
Database restructuring

in a single implementation unless there is a clear dependency between
them.

18. Before/After Responsibility

For significant changes, the AI agent should identify:

Before:
What existed before the change?

After:
What exists after the change?

Reason:
Why was the change required?

Example:

Before:
Activities had no year filtering.

After:
Activities support filtering by year using ?year=2026.

Reason:
The requirements require historical activity browsing.
19. Testing Requirement

Every functional change should be verified.

The changelog should record:

Tests:
- Test name
- Test result

For frontend changes:

- npm run lint
- npm run build
- Manual browser testing where appropriate

For backend changes:

- python manage.py check
- python manage.py test
- ruff check .
20. Rejected Implementation Ideas

The AI changelog may also document ideas that were intentionally rejected.

Example:

Rejected:

Redis caching for activity lists.

Reason:
The expected V1 traffic does not justify the added infrastructure
complexity.

Decision:
Do not implement for V1.

This prevents future AI agents from repeatedly suggesting or
implementing the same unnecessary feature.

21. Example Change Entry
CHANGE-0001 — Add Activity Category Model

Date:
2026-09-03

Agent:
OpenAI Codex

Type:
feature

Requirement:
REQUIREMENTS.md — Activities & Programs

Reason:
Activities must be filterable by category. A database-backed category
model allows the organization to manage categories without modifying
application code.

Files Changed:

backend/activities/models.py
backend/activities/admin.py
backend/activities/migrations/0001_initial.py

Functions / Classes / Components:

ActivityCategory

Code Location:

backend/activities/models.py: ActivityCategory definition

Implementation:
Added an ActivityCategory model containing name, slug, description,
and timestamps.

Why This Approach:
A database-backed category model is simpler and more maintainable than
hardcoding categories into the frontend or API.

Dependencies Added:
None.

Database Changes:

Added ActivityCategory model.

API Changes:
None.

Tests:

Django model checks passed.

Verification:

python manage.py check
python manage.py makemigrations
python manage.py migrate

Unnecessary Alternatives Considered:
Hardcoded category choices were not used because the organization may
add or change categories in the future.

Related Documentation:

REQUIREMENTS.md
DATABASE.md

---

# 22. AI Agent Instruction

Every AI coding agent working on this repository must follow this rule:

> Do not implement code that cannot be justified by a documented
> requirement, an existing bug, an approved architectural decision, or a
> clearly necessary implementation detail.

Before completing a significant task:

1. Inspect the repository.
2. Read the relevant documentation.
3. Identify existing code that can be reused.
4. Implement only the required change.
5. Run appropriate checks and tests.
6. Update `AI_CHANGELOG.md`.
7. Report what was changed and why.

If the agent believes additional code would be beneficial but it is not
required, the agent should recommend it separately instead of silently
implementing it.

---

# 23. Changelog Entry Numbering

Use sequential IDs:

```text
CHANGE-0001
CHANGE-0002
CHANGE-0003
...

Do not reuse an existing ID.

24. Final Principle

AI is an implementation assistant, not the project architect.

The project requirements and approved architectural decisions determine
what should be built.

AI determines how to efficiently implement the approved requirements
while keeping the implementation as simple as reasonably possible.


## One improvement I'd make to our whole AI workflow

I would also add this rule to **`DEVELOPMENT.md`**, under the existing AI section:

```markdown
---

# AI Change Tracking

Every significant AI-generated code change must be documented in:

```text
docs/AI_CHANGELOG.md

The AI agent must explain:

Why the change is necessary.
Which requirement it satisfies.
Which files were changed.
Which functions/classes/components were added or modified.
The relevant code locations or line ranges.
Whether dependencies were added.
Whether the database changed.
Whether the API changed.
What tests/checks were performed.
What unnecessary alternatives were intentionally not implemented.

AI agents must not silently expand the project's scope.

When a possible improvement is not required by the current task, the
agent should suggest it separately rather than implement it automatically.

---

## CHANGE-0001 — Establish Django Backend Foundation

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
feature / security

Requirement:
REQUIREMENTS.md §14 requires environment-managed secrets and explicit CORS.
ARCHITECTURE.md §§2, 5, 12, and 13 require the documented Django apps,
Django REST Framework, django-cors-headers, environment configuration, and
local React development support. API.md §§1, 26, and 27 require the REST API
foundation and explicit local CORS configuration.

Reason:
The generated Django project had none of the existing project apps registered,
no REST or CORS configuration, a committed secret key, UTC timezone, or an API
availability endpoint. The minimum backend foundation was needed before later
documented models and APIs can be implemented.

Files Changed:
- backend/config/settings.py
- backend/config/urls.py
- backend/core/views.py
- backend/core/tests.py
- backend/requirements.txt

Functions / Classes / Components:
- get_list_setting()
- health_check()
- HealthCheckTests

Code Location:
- backend/config/settings.py: lines 13-40, 45-105, and 143-157
- backend/config/urls.py: lines 17-30
- backend/core/views.py: lines 1-10
- backend/core/tests.py: lines 1-9
- backend/requirements.txt: lines 1-3

Implementation:
Registered the seven existing Django apps, Django REST Framework, and
django-cors-headers. Added explicit localhost Vite CORS defaults, Kathmandu
timezone, local static/media paths, comma-separated environment settings, and
a generated development-only key when DEBUG is enabled; non-debug runs require
SECRET_KEY from the environment. Added GET /api/health/ returning
{"status": "ok"}, with the endpoint explicitly public while DRF defaults to
authenticated access. Added its minimal integration test.

Why This Approach:
Used Django and Python standard-library configuration instead of adding dotenv
or a database URL parser. This keeps the foundation small, protects future API
endpoints by default, and leaves production values to the hosting environment.

Dependencies Added:
- django-cors-headers==4.9.0 — required by ARCHITECTURE.md for explicitly
  configured React-to-Django CORS.

Database Changes:
None. No models or migrations were added.

API Changes:
- Added public GET /api/health/ returning HTTP 200 and {"status": "ok"}.

Tests:
- HealthCheckTests.test_health_check_returns_ok

Verification:
- DEBUG=True python manage.py check — passed.
- DEBUG=True python manage.py test — passed (1 test).
- ruff check . — run; reports 31 pre-existing unused imports in untouched
  generated app stubs and one import-order issue corrected in config/urls.py.
- ruff check config core/views.py core/tests.py — passed.
- ruff format --check . — run; reports pre-existing formatting in untouched
  starter files and settings.py.

Unnecessary Alternatives Considered:
Did not add python-dotenv, django-environ, JWT authentication, pagination,
models, migrations, extra Django apps, or React work. Those are not necessary
for this initial foundation.

Assumptions:
- SQLite remains the intended local-development database, as ARCHITECTURE.md
  permits it.
- The local React development server uses localhost:5173 or 127.0.0.1:5173.
- Production will provide SECRET_KEY, DEBUG, host, CORS, and CSRF values through
  its environment.

Related Documentation:
- REQUIREMENTS.md
- ARCHITECTURE.md
- DATABASE.md
- API.md
- DEVELOPMENT.md

---

## CHANGE-0002 — Implement V1 Database Models and Django Admin

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
feature

Requirement:
DATABASE.md §§3-27 defines the 13 V1 entities, fields, relationships,
publication/status rules, indexing, ordering, and deletion behavior.
ARCHITECTURE.md §§4, 5, and 10 requires Django ORM and Django Admin for V1
content management. DEVELOPMENT.md §§9 and 12 requires migrations and tests.

Reason:
The existing apps contained only Django starter stubs, so the documented
database-backed content and administration foundation did not exist.

Files Changed:
- backend/core/models.py
- backend/activities/models.py
- backend/events/models.py
- backend/news/models.py
- backend/team/models.py
- backend/memberships/models.py
- backend/gallery/models.py
- backend/contact/models.py
- backend/*/admin.py
- backend/*/tests.py
- backend/*/migrations/0001_initial.py
- backend/requirements.txt

Models / Classes Changed:
- Organization, Announcement
- ActivityCategory, Activity, ActivityImage
- Event, EventImage
- NewsArticle
- TeamMember
- MembershipApplication
- GalleryAlbum, GalleryImage
- ContactMessage
- Eight Django ModelAdmin classes and focused model test classes.

Code Location:
- backend/core/models.py: lines 4-50; backend/core/admin.py: lines 6-18
- backend/activities/models.py: lines 4-64; backend/activities/admin.py: lines 6-30
- backend/events/models.py: lines 4-52; backend/events/admin.py: lines 6-28
- backend/news/models.py: lines 5-38; backend/news/admin.py: lines 6-13
- backend/team/models.py: lines 4-20; backend/team/admin.py: lines 6-12
- backend/memberships/models.py: lines 5-43; backend/memberships/admin.py: lines 6-19
- backend/gallery/models.py: lines 4-34; backend/gallery/admin.py: lines 6-22
- backend/contact/models.py: lines 4-31; backend/contact/admin.py: lines 6-12
- backend/*/tests.py: lines 1-44
- backend/*/migrations/0001_initial.py: generated initial migrations

Implementation:
Implemented only the 13 database models in their existing Django apps with
documented fields, unique slugs, status/priority choices, timestamps, default
ordering, documented query indexes, and media upload paths. Applied PROTECT
for activity categories, CASCADE for image children, and SET_NULL for the two
administrative User relationships. Registered all models in Django Admin with
simple list, filter, search, ordering, slug, and timestamp support.

Why This Approach:
Used standard Django ORM, built-in User, ImageField, and ModelAdmin features.
This matches the architecture without introducing custom base classes,
services, managers, signals, or non-Django infrastructure.

Dependencies Added:
- Pillow==12.1.1 — approved dependency required by Django ImageField validation
  for the documented logo, cover, photo, and gallery image fields.

Database Changes:
- Created eight initial migration files covering all 13 documented models.
- Applied migrations to the local SQLite development database.

API Changes:
None. No public REST endpoints, serializers, or API views were added; the
existing health-check endpoint was left unchanged.

Frontend Changes:
None.

Tests:
- Added focused model tests for creation/defaults, unique slugs, ordering,
  PROTECT, CASCADE, and SET_NULL behavior.
- Existing health-check test remains in the suite.

Verification:
- DEBUG=True python manage.py makemigrations — created eight initial migrations.
- DEBUG=True python manage.py migrate — passed.
- DEBUG=True python manage.py check — passed.
- DEBUG=True python manage.py makemigrations --check — no changes detected.
- DEBUG=True python manage.py migrate --plan — no pending operations.
- DEBUG=True python manage.py test — passed (10 tests).
- Focused ruff check with RUF012 excluded — passed. RUF012 is incompatible with
  Django's required class-level model/admin metadata and generated migrations.
- Focused ruff format --check — passed.

Unnecessary Alternatives Considered:
Did not add django-environ, a custom user model, serializers, REST endpoints,
JWT, a React dashboard, image processing/storage services, abstract base
models, signals, soft deletion, generic repository layers, or future member,
ward, volunteer, and attendance models.

Assumptions:
- A single organization record is expected operationally; DATABASE.md does not
  prescribe a singleton database constraint, so none was added.
- Announcement is placed in core as global site content; DATABASE.md names the
  model but does not prescribe an owning Django app.
- Documented optional/unspecified text and image fields are blankable; required
  fields remain required by Django model validation.
- MembershipApplication.areas_of_interest is stored as text because DATABASE.md
  specifies the field but not a structured storage format; API serialization is
  intentionally deferred.

Related Documentation:
- REQUIREMENTS.md
- ARCHITECTURE.md
- DATABASE.md
- API.md
- DEVELOPMENT.md
- DESIGN_SYSTEM.md

---



## CHANGE-0003 — Implement V1 Public REST API

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
feature

Requirement:
API.md §§1-29 defines the V1 public REST endpoints, public-data rules,
pagination, filtering, membership submission, and contact submission.
ARCHITECTURE.md §§6-9 requires React-facing data to be served through Django
REST APIs. DEVELOPMENT.md §§10 and 12 requires documented API behavior and
tests.

Reason:
The database foundation existed but no serializers, public API views, or
application API routes exposed the documented V1 data and form submissions.

Files Changed:
- backend/config/settings.py
- backend/config/urls.py
- backend/core/{serializers.py,views.py,urls.py,tests.py}
- backend/activities/{serializers.py,views.py,urls.py,tests.py}
- backend/events/{serializers.py,views.py,urls.py,tests.py}
- backend/news/{serializers.py,views.py,urls.py,tests.py}
- backend/team/{serializers.py,views.py,urls.py,tests.py}
- backend/gallery/{serializers.py,views.py,urls.py,tests.py}
- backend/memberships/{serializers.py,views.py,urls.py,tests.py}
- backend/contact/{serializers.py,views.py,urls.py,tests.py}

Serializers / Views / Routes:
- Public content serializers for organization, announcements, activities,
  events, news, team, and gallery.
- Public ListAPIView/RetrieveAPIView endpoints and CreateAPIView form endpoints.
- App URL configurations included under /api/.

Code Location:
- backend/config/settings.py: lines 95-105
- backend/config/urls.py: lines 18-35
- backend/*/serializers.py: lines 1-55
- backend/*/views.py: lines 1-52
- backend/*/urls.py: lines 1-9
- backend/*/tests.py: API tests appended through approximately line 90

Implementation:
Added the documented endpoints: organization, activity categories, activities
list/detail, events list/detail, news list/detail, team, gallery album
list/detail, announcements, membership application, and contact submission.
Configured standard DRF page-number pagination with configurable page size.
Public querysets restrict activities/news to published records, team to active
records, gallery to published albums, announcements to active/current records,
and events to non-draft records. Detail routes use public querysets so private
slugs return 404. Form serializers exclude all administrative fields and force
model defaults for pending/unread states.

Why This Approach:
Used DRF generic views, ModelSerializer, standard pagination, select_related,
and prefetch_related rather than routers, viewsets, or service abstractions.
This is the smallest implementation that keeps read operations and public form
submissions explicit and avoids administrative mutation endpoints.

Dependencies Added:
None.

Database Changes:
None. No models or migrations were changed.

API Changes:
- Added all documented V1 public REST endpoints listed in API.md §28.
- The existing GET /api/health/ endpoint remains unchanged.
- No protected administrative mutation endpoints were added.

Frontend Changes:
None.

Tests:
- Added API tests for publication filtering, slug 404 behavior, documented
  filters, pagination, nested images, team ordering/privacy, public
  organization fields, gallery visibility, membership validation/admin-field
  protection, contact validation, and the existing health check.

Verification:
- DEBUG=True python manage.py check — passed.
- DEBUG=True python manage.py makemigrations --check — no changes detected.
- DEBUG=True python manage.py test — passed (24 tests).
- ruff check . — run; reports RUF012 on Django class-level metadata and
  generated migrations, which is incompatible with standard Django patterns.
- Focused ruff check with RUF012 excluded — passed.
- Focused ruff format --check — passed.

Unnecessary Alternatives Considered:
Did not add django-filter, JWT, viewsets, routers, administrative CRUD APIs,
custom pagination, search, caching, background jobs, WebSockets, GraphQL, or
frontend work.

Assumptions:
- Draft events are excluded from public responses because draft is an internal
  status, although API.md does not separately state an event publication rule.
- The public organization endpoint returns the lowest-ID organization record
  and returns 404 when none exists; no singleton model constraint was added.
- Membership areas_of_interest accepts API.md's documented JSON list and is
  stored as comma-separated text because DATABASE.md leaves its storage type
  unspecified.

Issues Requiring Human Review:
None.

Related Documentation:
- REQUIREMENTS.md
- ARCHITECTURE.md
- DATABASE.md
- API.md
- DEVELOPMENT.md
- DESIGN_SYSTEM.md


## CHANGE-0004 — Establish V1 React Frontend Foundation

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
feature

Requirement:
ARCHITECTURE.md §§2, 6, 7, 8, and 13 requires React, Vite, React Router,
Axios, a decoupled REST client, and documented public routes. REQUIREMENTS.md
§§2, 4, and 11 requires the public-site foundation and responsive support.
DESIGN_SYSTEM.md §§9-13, 27-33, 38, and 46-49 defines the brand tokens,
responsive layout, accessibility, component, and motion principles.

Reason:
The frontend was the default Vite starter and did not provide the shared
application shell, public routes, API client, design system, or reusable
components needed for later page implementation.

Files Changed:
- frontend/package.json
- frontend/package-lock.json
- frontend/.env.example
- frontend/src/main.jsx
- frontend/src/App.jsx
- frontend/src/index.css
- frontend/src/components/{Button,Footer,LoadingState,Navbar,NotFound,
  PageContainer,SectionHeading,components}.jsx/css
- frontend/src/pages/FoundationPage.jsx
- frontend/src/routes/AppRoutes.jsx
- frontend/src/services/api.js
- .gitignore

Components Created:
- Navbar, Footer, Button, SectionHeading, PageContainer, LoadingState, NotFound
- FoundationPage placeholder and App application shell.

Code Location:
- frontend/src/index.css: lines 1-78
- frontend/src/App.jsx: lines 1-35
- frontend/src/routes/AppRoutes.jsx: lines 1-49
- frontend/src/services/api.js: lines 1-8
- frontend/src/components/*.jsx: lines 1-48
- frontend/src/components/components.css: lines 1-32

Implementation:
Replaced the Vite demo with a responsive React Router shell and minimal
placeholders for every documented public route. Added a centralized Axios
client using VITE_API_BASE_URL, a tracked safe environment example, central
CSS tokens from the Alliance Yuwa Club design palette, an accessible responsive
navbar/footer, and a small Framer Motion route transition that honors reduced
motion preferences.

Why This Approach:
Used native CSS variables, React Router, Axios, and one small Framer Motion
transition rather than a UI framework, global state library, or animation
system. This gives later pages a coherent foundation without prematurely
designing their finished content.

Dependencies Added:
- react-router-dom — required documented client-side routing.
- axios — required documented centralized REST client.
- framer-motion — required documented purposeful motion foundation.

Database Changes:
None.

API Foundation Changes:
- Added frontend/src/services/api.js with VITE_API_BASE_URL support.
- No resource-specific client methods or additional backend APIs were added.

Frontend Changes:
- Added all documented public client routes: /, /about, /activities,
  /activities/:slug, /events, /events/:slug, /news, /news/:slug, /team,
  /membership, and /contact.
- No complete page designs, homepage sections, or forms were implemented.

Motion Decisions:
- A single opacity/vertical route transition is used for continuity.
- Framer Motion's useReducedMotion and a CSS reduced-motion override prevent
  unnecessary animation for users who request it.

Verification:
- npm run lint — passed.
- npm run build — passed.

Unnecessary Alternatives Considered:
Did not add a UI kit, Tailwind, icon library, Redux, Zustand, React Query,
form library, global state, Three.js, WebGL, Lenis, page-specific API services,
or complete page UI.

Assumptions:
- No approved logo asset exists in the frontend yet, so the navbar uses a
  textual wordmark rather than inventing or altering logo artwork.
- VITE_API_BASE_URL defaults to the local Django API when not configured; the
  production API URL must be supplied through deployment environment variables.

Related Documentation:
- REQUIREMENTS.md
- ARCHITECTURE.md
- DATABASE.md
- API.md
- DEVELOPMENT.md
- DESIGN_SYSTEM.md

## CHANGE-0005 — Integrate Official Organization Logo

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
frontend / accessibility

Requirement:
The approved production website task requires the official asset at
`frontend/src/assets/logo.svg` to replace the navbar wordmark, appear in the
footer brand column, provide the favicon and social-image metadata, remain
responsive without distortion, and have accessible alternative text.

Reason:
The shared application shell used a temporary textual wordmark and the Vite
favicon. The supplied official logo must be the consistent brand representation
in the site chrome and metadata.

Files Changed:
- frontend/src/assets/logo.svg
- frontend/src/components/Navbar.jsx
- frontend/src/components/Footer.jsx
- frontend/src/components/components.css
- frontend/index.html
- docs/AI_CHANGELOG.md

Implementation:
- Imported `logo.svg` through Vite-relative component imports in Navbar and
  Footer.
- Replaced the textual navbar wordmark and added the logo above the footer
  motto.
- Applied fixed logo heights with `width: auto` so the native square aspect
  ratio is preserved on mobile and desktop.
- Set favicon, shortcut icon, Open Graph image, and Twitter image metadata to
  the same Vite-managed SVG asset.
- Added the semantic alt text `Alliance Yuwa Club Logo` to both rendered image
  elements.

Dependencies Added:
None.

Database Changes:
None.

API Changes:
None.

Responsive / Accessibility Impact:
The navbar logo is constrained to 2.75rem high and cannot consume flexible
navigation space; the footer logo is 4.5rem high. Both use automatic widths to
avoid stretching. The home link has an explicit accessible label and each logo
image has meaningful alternative text.

Verification:
- npm.cmd run lint — passed.
- npm.cmd run build — passed; Vite emitted the logo asset and rewrote the
  favicon and social metadata URLs for production.
- git diff --check — passed.

Unnecessary Alternatives Considered:
Did not redraw, recolor, crop, inline, or duplicate the official logo, and did
not add an icon or image dependency. The provided SVG is used directly.

---

## CHANGE-0006 — Implement V1 Public Homepage

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
frontend / visual implementation

Requirement:
REQUIREMENTS.md §§1, 2, 4.1, 5, 6, 11, and 12 require a responsive public
homepage that communicates the organization’s purpose, documented history,
featured activities, impact, and membership/contact paths. DESIGN_SYSTEM.md
§§3, 7, 11–18, 22, 27–33, 38, and 49 requires an editorial, mobile-first,
brand-token-based page with purposeful motion and no generic template styling.
ARCHITECTURE.md §§6, 7, and 14 requires React routes and reusable frontend
components without direct database access.

Reason:
The root route displayed only the generic frontend foundation placeholder and
did not present the club’s documented purpose, activity record, or engagement
paths.

Files Changed:
- frontend/src/pages/Home.jsx
- frontend/src/pages/Home.css
- frontend/src/routes/AppRoutes.jsx
- frontend/src/components/components.css
- docs/AI_CHANGELOG.md

Implementation:
- Added the dedicated Home page and routed `/` to it.
- Created an asymmetric editorial hero for “Unity. Leadership. Service.” with
  Biratnagar-focused introduction copy and activity-photo placeholders ready
  for official imagery.
- Added verified impact metrics: 6+ years, 100+ community activities, and
  Biratnagar & Beyond.
- Added direct linked feature entries for the three documented 2026 programs,
  including category, date, location, and concise documented summaries.
- Added a 2020-to-present journey teaser with an activity-archive CTA and a
  final membership/contact engagement banner.
- Added a blue `secondary` Button variant using the existing approved primary
  blue token.

Visual / Motion Decisions:
The page follows the documented rhythm of typographic hero, metrics, activity
record, history, and dark community CTA. It uses neutral canvas space, green
for primary emphasis, blue for supporting action, and orange only as a small
activity accent. Framer Motion handles restrained entrance and in-view reveals
plus small card hover lifts; `useReducedMotion` removes positional motion and
reduces transitions to zero duration.

Dependencies Added:
None. Existing React Router and Framer Motion dependencies were reused.

Database Changes:
None.

API Changes:
None. The initially documented feature data is local presentation content; no
database or API contract was changed.

Responsive / Accessibility Impact:
The layout is single-column by default, becomes a composed two-column hero and
timeline at tablet widths, and uses an asymmetric desktop feature layout.
Sections use semantic headings, lists, articles, and destination links. The
visual image frames are clearly labelled as reserved activity-photography
space, avoiding invented imagery.

Verification:
- npm.cmd run lint — passed.
- npm.cmd run build — passed.
- git diff --check — passed.

Unnecessary Alternatives Considered:
Did not add stock photography, fabricated impact figures, generic icon sets,
gradients, additional dependencies, database models, or API endpoints. Actual
club photography and database-backed featured-content selection can replace
the labelled placeholders when approved media and content are available.

---

## CHANGE-0007 — Connect Activities and Events to the Public API

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
frontend / API integration

Requirement:
REQUIREMENTS.md §§4.3, 4.4, 6, 11, and 12 requires a responsive,
database-driven activity archive with category/date support and public
upcoming/past event information. API.md §§6–8 and 21–23 defines the public
activity/event list, detail, pagination, and filtering contracts.
ARCHITECTURE.md §§6–8 and 14 requires React to consume Django REST APIs via a
central client without directly accessing the database. DESIGN_SYSTEM.md
§§11–12, 17–19, 27–33, 38, and 49 requires responsive editorial content,
purposeful motion, and accessible interaction.

Reason:
The `/activities`, `/activities/:slug`, `/events`, and `/events/:slug` routes
were generic placeholders and did not expose the public content API.

Files Changed:
- frontend/src/services/api.js
- frontend/src/components/MediaFrame.jsx
- frontend/src/pages/contentUtils.js
- frontend/src/pages/{Activities,ActivityDetail,Events,EventDetail}.jsx
- frontend/src/pages/ContentPages.css
- frontend/src/routes/AppRoutes.jsx
- docs/AI_CHANGELOG.md

Implementation:
- Added central API functions for activity categories, activities, activity
  details, events, and event details. List methods support the documented
  category, year, status, page, and page_size query parameters.
- Replaced the four placeholder routes with REST-backed archive/list and detail
  pages, including pagination, request errors, unavailable-record states, and
  no-content states.
- Added an accessible activity category toolbar, a 2020–2026 year timeline,
  chronological activity cards, and direct slug-based navigation.
- Added activity and event detail layouts with API-sourced descriptions, dates,
  locations, cover media, and dynamic image galleries.
- Added dynamic event status indicators for upcoming, ongoing, completed, and
  cancelled records, plus optional API-backed registration links.
- Added a reusable media frame that renders published images when present and
  clearly labelled structural placeholders otherwise.

Data Limitation:
The public Activity serializer does not expose partners or organizers. The
activity detail page therefore includes that required section with an explicit
public-record fallback instead of inventing unverified collaborators.

Visual / Motion Decisions:
The archive uses an editorial timeline and bordered image/text records instead
of a generic card wall. Existing design tokens drive all colours. Framer Motion
provides small list entrances and hover lifts; `useReducedMotion` disables the
positional motion and transitions for users who request reduced motion.

Dependencies Added:
None.

Database Changes:
None.

API Changes:
None. The existing documented public endpoints are consumed without changing
their schema, routes, filtering behavior, or permissions.

Responsive / Accessibility Impact:
The layouts are single-column on mobile, become two-column for event records
and galleries on tablet, and use three-column activity/gallery layouts on
desktop. Filters are native keyboard-operable buttons in labelled toolbars with
`aria-pressed` state; semantic articles, headings, navigation, descriptions,
and meaningful image alt text are used throughout.

Verification:
- npm.cmd run lint — passed.
- npm.cmd run build — passed.
- git diff --check — passed.

Unnecessary Alternatives Considered:
Did not hardcode activity or event records, add a client-side database/cache,
change Django models or API endpoints, add stock photography, introduce an
icon library, or add dependencies. Organization images and partner data remain
API-driven and will appear when published by the club.

---

## CHANGE-0008 — Add Official Homepage Activity Photography

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
frontend / visual implementation

Requirement:
The approved production task requires the provided static photographs to be
imported into the homepage hero and the three documented featured-activity
records. DESIGN_SYSTEM.md §§20, 26, 38, 42, and 49 requires real organization
photography, responsive image treatment, meaningful alternative text, and
design-token-based implementation.

Reason:
The Home page used clearly labelled visual placeholders while awaiting official
photographs. The supplied club images now allow those placeholders to represent
actual Alliance Yuwa Club people and activities.

Files Changed:
- frontend/src/assets/images/{hero-community,border-cleanliness,general-convention,womens-sports-festival}.jpg
- frontend/src/pages/Home.jsx
- frontend/src/pages/Home.css
- docs/AI_CHANGELOG.md

Implementation:
- Imported the four supplied JPEGs through Vite-compatible relative imports.
- Replaced the hero’s structural placeholder with `hero-community.jpg` and the
approved alt text: “Alliance Yuwa Club youth volunteers in Biratnagar”.
- Mapped each activity photo to its matching featured-activity card.
- Applied `object-fit: cover`, token-based medium border radii, overflow
containment, and a small image-scale hover treatment for activity cards.

Dependencies Added:
None.

Database Changes:
None.

API Changes:
None.

Responsive / Accessibility Impact:
Each image fills its existing responsive frame without stretching. The hero
and activity cards maintain their mobile and desktop heights, and the activity
images use concise descriptive alternative text. Reduced-motion users retain
the static image treatment through the existing global motion preference rule.

Verification:
- npm.cmd run lint — passed.
- npm.cmd run build — passed; all four JPEG imports were emitted as production
  assets.

Unnecessary Alternatives Considered:
Did not crop, recolor, generate, or replace the supplied photos, and did not
add an image-processing dependency. The original static assets are used
directly through Vite.

---

## CHANGE-0009 — Add About, Team, and News Public Pages

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
frontend / API integration

Requirement:
REQUIREMENTS.md §§4.2, 4.5, 4.6, 11, and 12 requires public About, Team, and
News pages with responsive presentation of the club story, team, and published
updates. API.md §§9–10, 21, and 23 defines the public news/team API behavior.
ARCHITECTURE.md §§6–8 requires the React client to use the Django REST API.
DESIGN_SYSTEM.md §§10–12, 20–21, 27–33, 38, and 49 requires editorial,
responsive, accessible content and purposeful motion.

Reason:
The affected routes used generic foundation placeholders and did not render
the available public team or news content.

Files Changed:
- frontend/src/services/api.js
- frontend/src/components/MediaFrame.jsx
- frontend/src/pages/{About,Team,News,NewsDetail}.jsx
- frontend/src/pages/EditorialPages.css
- frontend/src/pages/ContentPages.css
- frontend/src/routes/AppRoutes.jsx
- docs/AI_CHANGELOG.md

Implementation:
- Added centralized news list/detail and executive-team client methods.
- Implemented the About page with the documented Shanti Yuwa Club transition,
  Biratnagar history, mission, vision, and Unity/Leadership/Service values.
- Implemented a REST-backed executive committee grid with role, biography,
  published portrait, and verified-social-link fallback states.
- Implemented paginated news cards and detail pages with dates, reading-time
  estimates, API article media, content rendering, return navigation, and
  loading/error/empty/404 states.
- Added an error-safe MediaFrame: failed API image requests now render a
  labelled inline SVG fallback rather than a broken image.

API Endpoint Resolution:
The requested `/api/v1/team/` path is not part of API.md and does not exist in
the Django route configuration. The implementation uses the documented and
implemented public endpoint `/api/team/` through the existing `/api` base URL.
No backend endpoint was changed.

Sample Asset References:
`sample-hero.jpg`, `sample-avatar.jpg`, and `sample-news.jpg` are not present
in `frontend/src/assets/images/`. The documented sample-image convention allows
fallback SVG renders, so MediaFrame supplies a labelled SVG image fallback for
the About hero, unavailable team photos, unavailable news images, and failed
media requests. No missing local image path is imported.

Visual / Motion Decisions:
The About view alternates open editorial space with a single dark-history
section. Team and news use restrained records with real media priority rather
than generic application cards. Existing Framer Motion transitions provide
small entrances and hover lifts; `useReducedMotion` disables positional motion
and transitions.

Dependencies Added:
None.

Database Changes:
None.

API Changes:
None. The existing public API contract is consumed directly.

Responsive / Accessibility Impact:
Each page starts as a single-column mobile layout and progresses to two/three
columns at tablet/desktop widths. Semantic headings, article elements, time
elements, accessible loading/error states, and meaningful image alt/fallback
labels are provided throughout.

Verification:
- npm.cmd run lint — passed.
- npm.cmd run build — passed.

Unnecessary Alternatives Considered:
Did not add nonexistent `/api/v1/` routes, hardcode team/news records, expose
private team contact details, invent social links or article categories, add
stock images, or create sample JPEG assets. Public content remains API-driven
and the fallback SVG handles unavailable media safely.

---

## CHANGE-0010 — Implement Public Membership and Contact Forms

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
frontend / API integration

Requirement:
REQUIREMENTS.md §§4.7–4.8, 7–8, 11, and 12 requires public membership and
contact experiences, responsive presentation, and secure form submission.
API.md §§11–13 and 20 defines the public organization data and form
contracts. DESIGN_SYSTEM.md §§9.19, 27–33, 37–38, and 49 requires token-based,
accessible, mobile-friendly forms with purposeful reduced-motion-aware motion.

Files Changed:
- frontend/src/services/api.js
- frontend/src/pages/{Membership,Contact,FormPages,formUtils}.jsx/css/js
- frontend/src/routes/AppRoutes.jsx
- docs/AI_CHANGELOG.md

Implementation:
- Added centralized REST methods for organization information, membership
  applications, and contact messages.
- Replaced the `/membership` placeholder with a Biratnagar-focused value
  proposition, participation expectations, and an accessible application form.
  The form includes API-required ward, occupation, and education fields in
  addition to personal details, interests, and motivation.
- Replaced the `/contact` placeholder with public organization data, a
  Biratnagar fallback location, verified API-provided email/phone/social links,
  and an accessible inquiry form.
- Added client validation, server-field error recovery, submitting states,
  inline alerts, and post-submit confirmations for both forms.

API Routes Used:
- GET `/api/organization/`
- POST `/api/membership/apply/`
- POST `/api/contact/`

Accessibility / Motion:
- Native labelled controls use `aria-invalid` and `aria-describedby` when
  errors are present, with live success/error feedback and keyboard-visible
  high-contrast focus rings.
- Controls meet a 2.75rem minimum tap target and layouts become single-column
  on mobile.
- Restrained Framer Motion entrances use `useReducedMotion` to remove
  positional animation for users who request reduced motion.

Dependencies Added:
None.

Database Changes:
None.

Verification:
- `npm.cmd run lint` — passed.
- `npm.cmd run build` — passed.

---

## CHANGE-0011 — Implement Public Gallery Module

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
frontend / API integration

Requirement:
REQUIREMENTS.md §4.9 requires a gallery architecture that accepts published
photographs over time. ARCHITECTURE.md §§6–8 and 11 requires the React client
to consume public REST media data. API.md §§14, 21, and 28 defines the public
gallery-album list/detail contract and its pagination. DESIGN_SYSTEM.md
§§11–12, 20, 26–33, 35, 38, and 49 requires responsive, real-media-first,
accessible presentation with purposeful reduced-motion-aware motion.

Files Changed:
- frontend/src/services/api.js
- frontend/src/components/GalleryLightbox.jsx
- frontend/src/components/{Navbar,Footer}.jsx
- frontend/src/components/components.css
- frontend/src/pages/{Gallery.jsx,GalleryDetail.jsx,Gallery.css,galleryUtils.js}
- frontend/src/routes/AppRoutes.jsx
- docs/AI_CHANGELOG.md

Implementation:
- Added centralized paginated album-list and slug-detail API methods.
- Added `/gallery` with a responsive published-album archive, cover-image
  fallbacks, execution dates, photo-count badges, pagination, request errors,
  and no-content states.
- Added `/gallery/:slug` with a responsive CSS-column masonry photo layout,
  image captions, dynamic tags when supplied by public data, return navigation,
  and unavailable-album states.
- Added a reusable full-screen lightbox with click-outside closing, Escape,
  ArrowLeft/ArrowRight photo navigation, focus trapping, focus restoration,
  scroll locking, and reduced-motion-aware transitions.
- Added Gallery links in the primary and footer navigation.

API Routes Used:
- GET `/api/gallery/albums/`
- GET `/api/gallery/albums/<slug>/`

API Contract Note:
The documented album-list serializer does not include a photo count or
category/tag fields. The overview obtains photo counts from its documented
album-detail requests. Tag filtering is enabled only when public album data
contains tags/categories, avoiding invented classifications; untagged albums
remain available chronologically.

Dependencies Added:
None.

Verification:
- `npm.cmd run lint` — passed.
- `npm.cmd run build` — passed.
- `git diff --check` — passed.

---

## CHANGE-0012 — Add Gallery Album Batch Uploads in Django Admin

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
backend / Django admin

Requirement:
The production gallery-administration task requires multi-file image uploads
while preserving individual image management. ARCHITECTURE.md §11 assigns the
gallery app responsibility for albums, images, and image ordering.

Files Changed:
- backend/gallery/admin.py
- backend/gallery/tests.py
- docs/AI_CHANGELOG.md

Implementation:
- Added `GalleryAlbumAdminForm` with the optional `batch_images` non-model
  field, labelled “Batch Upload Images (Select Multiple Files)”.
- Added Django-supported `MultipleFileInput` and `MultipleFileField` wrappers
  so the ClearableFileInput correctly accepts multiple selected files.
- Added `GalleryImageInline` as a tabular inline for individual image review,
  captions, reordering, additions, and deletion.
- Extended `GalleryAlbumAdmin.save_related` to append every
  `request.FILES.getlist("batch_images")` file as a `GalleryImage` linked to
  the saved album. Uploaded images receive consecutive display-order values
  after existing inline images.
- Added automated coverage for the multi-file save flow and image ordering.

Dependencies Added:
None.

Database Changes:
None.

Verification:
- `python manage.py check` — passed with no errors. The project still reports
  13 pre-existing `models.W042` `DEFAULT_AUTO_FIELD` warnings across apps.
- `python manage.py test gallery` — passed (3 tests).

---

## CHANGE-0013 — Add Minimal Production Deployment Configuration

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
deployment / security

Requirement:
The production deployment task requires environment-based Django security
configuration, WhiteNoise static serving, Dockerized Django/Gunicorn and
Vite/Nginx services, and PostgreSQL composition without introducing a broad
deployment framework.

Files Changed:
- backend/config/settings.py
- backend/requirements.txt
- backend/Dockerfile
- frontend/Dockerfile
- frontend/nginx.conf
- frontend/.env.production.example
- docker-compose.yml
- docs/AI_CHANGELOG.md

Implementation:
- Kept `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and `CORS_ALLOWED_ORIGINS`
  environment-driven and added the requested browser, MIME-sniffing, and frame
  protection settings.
- Added WhiteNoise middleware and compressed manifest static-file storage.
- Added optional PostgreSQL settings, activated by `POSTGRES_DB`, while
  retaining SQLite for local development without PostgreSQL variables.
- Added Python 3.11-slim Gunicorn backend and multi-stage Vite/Nginx frontend
  Dockerfiles.
- Added a compact Compose stack with healthy PostgreSQL startup, automatic
  backend migrations, persistent database/media volumes, and build-time
  `VITE_API_BASE_URL` configuration.

Dependencies Added:
- gunicorn==23.0.0
- psycopg2-binary==2.9.10
- whitenoise==6.11.0
- django-cors-headers remains explicitly pinned in backend/requirements.txt.

Verification:
- `git diff --check` — passed.
- No container build or runtime test was run, by request to avoid heavy
  terminal work.

---

## CHANGE-0014 — Restore Django Default Media Storage

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
backend / media correctness

Audit Finding Addressed:
The production-readiness audit found that `STORAGES` configured WhiteNoise
static-file storage only. Django therefore had no `default` storage alias,
which could raise `InvalidStorageError` when public serializers accessed an
`ImageField` URL. Production `/media/` delivery was also incorrectly easy to
mistake for a WhiteNoise responsibility.

Files Changed:
- backend/config/settings.py
- backend/config/urls.py
- backend/core/tests.py
- docs/AI_CHANGELOG.md

Functions / Classes / Configuration:
- `STORAGES`, `MEDIA_URL`, and `MEDIA_ROOT` in `config.settings`
- Development media routing in `config.urls`
- `PublicMediaSerializationTests` in `core.tests`

Code Location:
- backend/config/settings.py: approximately lines 188–204
- backend/config/urls.py: approximately lines 38–42
- backend/core/tests.py: approximately lines 58–160

Implementation:
- Declared Django's `default` storage as `FileSystemStorage` and retained
  WhiteNoise's compressed manifest storage exclusively for `staticfiles`.
- Kept `MEDIA_URL` and `MEDIA_ROOT` separate from static-file settings.
- Preserved Django's development-only media URL routing and documented that
  WhiteNoise is not an uploaded-media solution.
- Added API regression coverage for organization logos, activity cover/detail
  images, event cover/detail images, news images, team photos, and gallery
  cover/detail images. The tests assign field names only; they do not create
  synthetic image files.

Why This Approach:
This restores Django's standard, local filesystem-backed default without
inventing a provider or conflating uploads with immutable static assets.

Dependencies Added:
None.

Database Changes:
None.

API Changes:
None. Existing image fields retain their public URL response contract.

Tests:
- Added default-storage URL regression coverage.
- Added public serializer/API coverage for every public image field.

Verification:
- `python manage.py check` completed with the 13 pre-existing
  `DEFAULT_AUTO_FIELD` warnings.
- `python manage.py test` passed: 27 tests.
- Public media URLs are asserted to use `/media/` paths and never local
  filesystem paths.

Unnecessary Alternatives Considered:
- Serving uploads through WhiteNoise was rejected because WhiteNoise is for
  immutable static assets, not user-uploaded media.
- Adding a cloud media provider was not done because no provider or deployment
  credentials were approved for this focused fix.

Remaining Production Media Limitation:
`FileSystemStorage` is the correct local/default foundation only. Before a
production deployment, the chosen hosting architecture must provide durable
uploaded-media storage and public media delivery; no provider was invented by
this change.

Related Documentation:
- REQUIREMENTS.md
- ARCHITECTURE.md
- DATABASE.md
- API.md
- DEVELOPMENT.md

Scope Control:
Unrelated audit findings, including Docker build-context hygiene, dependency
environment mismatch, abuse protection, upload limits, host configuration,
homepage content, SEO, and administrative API documentation, were not
modified.

---

## CHANGE-0015 — Exclude Local Backend State from Docker Build Context

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
deployment / Docker build-context hygiene

Audit Finding Addressed:
The backend Compose service builds with `./backend` as its Docker context and
the Dockerfile uses `COPY . .`. That directory can contain ignored-but-local
runtime state, including `venv/`, `db.sqlite3`, and `media/`. Without a
context-specific ignore file, Docker can send those files to the builder and
the broad copy can place them in an image layer.

Why This Fix Was Necessary:
Excluding local environments, database state, uploaded media, secrets, and
tooling output keeps the build smaller and reproducible and avoids exposing
local data or PII to Docker build layers.

Files Changed:
- backend/.dockerignore
- docs/AI_CHANGELOG.md

Docker Configuration Changed:
- Added a backend-context `.dockerignore` for Python virtual environments and
  bytecode, local SQLite state, `media/`, `.env` variants, Git metadata, and
  clearly local test/lint/log artifacts.
- Kept `requirements.txt`, `manage.py`, `config/`, all Django application
  source directories, and the Dockerfile available to the existing Docker
  build. The Dockerfile and Compose configuration were not rewritten.

Application / Database / Media / Frontend Scope:
- No application code changed.
- No database changes were made.
- No media provider was added.
- No frontend changes were made.

Assumptions:
The production backend image is built from the source-controlled backend
files; local SQLite data, uploaded media, virtual environments, `.env` files,
and tooling caches are not image inputs. Persistent production media continues
to be supplied by the existing Compose volume at runtime, not by the build
context.

Tests and Verification:
- Inspected the live Compose context (`./backend`) and backend Dockerfile copy
  directives.
- Confirmed that the ignore rules retain all required backend source inputs.
- `docker compose config --no-interpolate` — passed; it resolves the backend
  build context to the backend directory and preserves the expected services,
  volumes, and environment placeholders.
- `docker compose build backend` — passed. Docker loaded the `.dockerignore`,
  transferred a 18.62 kB backend context, completed `COPY . .`, and completed
  `python manage.py collectstatic --noinput` successfully.
- `git diff --check` — passed.

Unnecessary Alternatives Rejected:
- Did not narrow or refactor the existing Dockerfile `COPY . .`, because the
  context-specific ignore file addresses the leak while preserving required
  source files.
- Did not change Git ignore rules, delete local database/media files, add a
  media provider, alter application code, or change unrelated Docker services.

---

## CHANGE-0016 — Align Backend Virtual Environment with Requirements

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
backend / dependency environment verification

Audit Finding Addressed:
The active backend virtual environment did not match `backend/requirements.txt`.
It contained Django 6.1.1 despite the declared `Django>=5.0,<6.0` range,
contained `psycopg2-binary` 2.9.12 instead of 2.9.10, and lacked the declared
Gunicorn and WhiteNoise packages. That made local Django checks and tests
inconsistent with the project dependency contract.

Environment Adjustment:
- Installed the existing `backend/requirements.txt` set into `backend/venv`.
- The resulting relevant versions are Django 5.2.17,
  djangorestframework 3.18.0, django-cors-headers 4.9.0, Pillow 12.1.1,
  gunicorn 23.0.0, psycopg2-binary 2.9.10, and whitenoise 6.11.0.
- `pip check` reports no broken requirements.
- No dependency was added or changed in `requirements.txt`.

Configuration Adjustment:
- Set `DEFAULT_AUTO_FIELD` to `django.db.models.BigAutoField`, matching every
  existing initial migration. This resolves the generated implicit-primary-key
  migration proposals after moving back to the declared Django 5.x range.
- No model was changed and no migration was created or applied.

Files Changed:
- backend/config/settings.py
- docs/AI_CHANGELOG.md

Verification:
- Ran `python manage.py check` from `backend/` with a process-local,
  non-production `SECRET_KEY`; passed with no issues.
- Ran `python manage.py makemigrations --check`; passed with no changes
  detected.
- Ran `python manage.py test`; passed: 27 tests.

Verification Environment Note:
The shell had `DEBUG=False` but no active `SECRET_KEY`. A temporary key was
provided only to the verification process; no secret was written to source or
stored in project configuration, and production secret validation remains
unchanged.

Scope Control:
- No frontend, API contract, model, migration, database schema, rate-limiting,
  security-header, or PaaS integration change was made.
- The test process emits a non-failing WhiteNoise notice because the local
  `staticfiles/` directory has not been generated; the test suite remains
  fully green and production image builds run `collectstatic`.

---

## CHANGE-0017 — Throttle Public Form Submissions

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
backend / API security

Audit Finding Addressed:
The public POST endpoints for contact messages and membership applications had
no submission throttling. Automated clients could repeatedly submit either
form, creating spam records and needlessly consuming application resources.

Implementation:
- Configured Django REST Framework's built-in `ScopedRateThrottle` as the
  default throttle class and added named throttle rates.
- Applied the `contact_submission` scope only to
  `ContactMessageCreateView` (`/api/contact/`) and the
  `membership_application` scope only to `MembershipApplicationCreateView`
  (`/api/membership/apply/`).
- Default per-client-IP limits are five contact submissions per hour and three
  membership applications per day.
- `CONTACT_SUBMISSION_THROTTLE_RATE` and
  `MEMBERSHIP_APPLICATION_THROTTLE_RATE` may override those rates through the
  environment without a code change.
- Successful submission responses and their HTTP 201 status remain unchanged.
  Requests over the limit receive DRF's standard HTTP 429 response with its
  `detail` error payload.

Files Changed:
- backend/config/settings.py
- backend/contact/views.py
- backend/contact/tests.py
- backend/memberships/views.py
- backend/memberships/tests.py
- docs/AI_CHANGELOG.md

Classes / Configuration Modified:
- `REST_FRAMEWORK` throttle classes and rates in `config.settings`
- `ContactMessageCreateView`
- `MembershipApplicationCreateView`
- Contact and membership API regression test classes

Tests Added:
- Contact submissions accept five rapid requests from one client IP and reject
  the sixth with HTTP 429 and a `detail` payload.
- Membership applications accept three rapid requests from one client IP and
  reject the fourth with HTTP 429 and a `detail` payload.
- Test cache setup/cleanup prevents one throttle test from affecting another.

Verification:
- `python manage.py check` — passed with no issues.
- `python manage.py test` — passed: 29 tests.

Scope Control:
- No frontend, API success contract, database model, migration, schema,
  deployment/host configuration, CAPTCHA service, or third-party dependency
  was changed.

---

## CHANGE-0018 — Validate Image Upload Size and Extensions

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
backend / upload validation

Audit Finding Addressed:
Image upload fields did not enforce an explicit size limit or allowed filename
extensions. Oversized uploads and unwanted file types could therefore enter
the Django Admin upload paths, including gallery batch uploads.

Validation Rules:
- Maximum image size: 5 MiB (5 × 1024 × 1024 bytes) per file.
- Allowed extensions: `.jpg`, `.jpeg`, `.png`, and `.webp`.
- Files over the limit raise a descriptive Django `ValidationError`; unsupported
  extensions are rejected with an allowed-extension message. DRF serializers
  that use these model fields surface the normal HTTP 400 field errors.

Implementation:
- Added reusable image validators in `core.validators`.
- Attached the shared validator list to every uploaded-image `ImageField`:
  organization logo; activity and event covers/detail images; news featured
  image; team photo; gallery album cover and album images.
- Applied the same validators to `GalleryAlbumAdminForm.batch_images`, so the
  custom multi-file Django Admin route cannot bypass validation.
- Added state-only `AlterField` migrations for the validation metadata. They
  do not alter database tables, columns, or data.

Files Changed:
- backend/core/validators.py
- backend/{core,activities,events,news,team,gallery}/models.py
- backend/{core,activities,events,news,team,gallery}/migrations/0002_*.py
- backend/gallery/admin.py
- backend/core/tests.py
- backend/gallery/tests.py
- docs/AI_CHANGELOG.md

Tests Added:
- Valid `.jpg`, `.png`, and `.webp` uploads below the limit are accepted.
- An upload over 5 MiB raises a validation error.
- An unsupported extension is rejected.
- Every model image field is asserted to use the shared validators.
- Gallery Admin batch upload rejection is covered.

Verification:
- `python manage.py check` — passed with no issues.
- `python manage.py makemigrations --check` — passed with no changes detected.
- `python manage.py test` — passed: 34 tests.

Scope Control:
- No frontend, public API success contract, cloud-storage configuration,
  rate-limiting/security-header setting, third-party dependency, or database
  schema/data change was made.

---

## CHANGE-0019 — Add Conditional Supabase S3 Media Storage

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
deployment / production media storage

Audit Finding Addressed:
Local filesystem media is lost when an ephemeral production container restarts.
Supabase Storage is the approved durable production media provider, but Django
did not yet have an S3-compatible storage driver or a conditional production
storage configuration.

Dependencies Added:
- django-storages[s3]==1.14.6
- boto3==1.43.88

Storage Backend Selection:
- `USE_SUPABASE_STORAGE` defaults to false. Without the flag, local development
  continues to use `FileSystemStorage` and `/media/` unchanged.
- With the flag true, the default storage is
  `storages.backends.s3boto3.S3Boto3Storage`; WhiteNoise remains the unchanged
  `staticfiles` backend.
- Supabase uses path-style S3 addressing and unsigned public object URLs.
  The public media base is derived from the S3 endpoint as
  `/storage/v1/object/public/<bucket>/`; an optional
  `SUPABASE_STORAGE_PUBLIC_URL` supports a custom public URL.

Required Production Environment Variables:
- USE_SUPABASE_STORAGE=true
- SUPABASE_STORAGE_BUCKET
- SUPABASE_S3_ACCESS_KEY_ID
- SUPABASE_S3_SECRET_ACCESS_KEY
- SUPABASE_S3_ENDPOINT_URL
- SUPABASE_S3_REGION (defaults to `us-east-1` when omitted)

Files Changed:
- backend/requirements.txt
- backend/config/settings.py
- backend/core/tests.py
- docs/AI_CHANGELOG.md

Tests Added:
- Local configuration with `USE_SUPABASE_STORAGE=False` resolves to
  `FileSystemStorage` and `/media/`.
- Supabase configuration resolves the requested S3Boto3 backend, public media
  URL, default region, and unsigned URL setting without contacting Supabase.

Verification:
- `python -m pip check` — passed with no broken requirements.
- `python manage.py check` — passed with no issues.
- `python manage.py test` — passed: 36 tests.

Scope Control:
- No credentials were hardcoded.
- No frontend, database model/migration, public API contract, CORS/host,
  deployment-platform, or static-file configuration change was made.

---

## CHANGE-0020 — Harden Production Host, Proxy, and Security Settings

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
security / deployment

Requirement:
PRODUCTION_READINESS_AUDIT.md §6 (Security) and §7 (Deployment) — complete
production host, CORS, CSRF, reverse-proxy, and security-header configuration
for PaaS deployment on Render. REQUIREMENTS.md §14 and ARCHITECTURE.md §12
require environment-managed secrets, explicit CORS, and HTTPS without
hardcoded hosts or credentials.

Audit Finding Addressed:
1. `ALLOWED_HOSTS` formatting had to safely parse comma-separated environment
   strings.
2. Explicit `CORS_ALLOWED_ORIGINS` and `CSRF_TRUSTED_ORIGINS` parsing was
   needed for the Vercel frontend domains.
3. Render runs behind a reverse proxy, requiring `SECURE_PROXY_SSL_HEADER` and
   dynamic `$PORT` handling for Gunicorn.
4. Production security headers (HTTPS redirect, HSTS, secure cookies) had to
   activate only when `DEBUG=False`.

Implementation:
- `get_list_setting()` now accepts an optional `environment` mapping (mirroring
  `get_boolean_setting`) so the comma-separated parser is directly testable.
  Values are split on commas, trimmed of surrounding whitespace, and blank
  entries are dropped, so strings such as
  `https://allianceyuwaclub.org.np, https://*.vercel.app,` never yield empty
  host/origin entries. `ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS`, and
  `CSRF_TRUSTED_ORIGINS` all use this parser.
- Set `SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")` so
  `request.is_secure()` and the HTTPS redirects behave correctly behind
  Render's TLS-terminating proxy.
- Added a `if not DEBUG:` production-hardening block that enables
  `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`, `SECURE_SSL_REDIRECT`,
  `SECURE_HSTS_SECONDS` (default 31536000), and optional HSTS subdomain/preload
  and `SECURE_REFERRER_POLICY`. `SECURE_SSL_REDIRECT` defaults to true in
  production but honors a `SECURE_SSL_REDIRECT` environment override so the
  redirect can be disabled if the proxy already performs it (avoiding loops).
- Kept `SECURE_BROWSER_XSS_FILTER`, `SECURE_CONTENT_TYPE_NOSNIFF`, and
  `X_FRAME_OPTIONS = "DENY"` enabled in every environment.
- The `else` (DEBUG) branch explicitly keeps `SECURE_SSL_REDIRECT`,
  `SESSION_COOKIE_SECURE`, and `CSRF_COOKIE_SECURE` disabled so local HTTP
  development continues to work with no environment variables.
- `backend/Dockerfile` CMD switched to shell form so Gunicorn binds to
  `0.0.0.0:${PORT:-8000}`, respecting Render's dynamic `$PORT` while defaulting
  to 8000 for plain local Docker runs.

Required Production Environment Variables (Render):
- DEBUG=false
- SECRET_KEY (persistent, from the Render environment)
- ALLOWED_HOSTS (comma-separated, e.g. `allianceyuwaclub.org.np,.onrender.com`)
- CORS_ALLOWED_ORIGINS (comma-separated, e.g.
  `https://allianceyuwaclub.org.np,https://*.vercel.app`)
- CSRF_TRUSTED_ORIGINS (comma-separated, scheme required, e.g.
  `https://allianceyuwaclub.org.np,https://*.vercel.app`)
- Database `DATABASE_URL` / `POSTGRES_*` values (unchanged from prior work)
- Optional overrides: `SECURE_SSL_REDIRECT`, `SECURE_HSTS_SECONDS`,
  `SECURE_HSTS_INCLUDE_SUBDOMAINS`, `SECURE_HSTS_PRELOAD`,
  `SECURE_REFERRER_POLICY`

Files Changed:
- backend/config/settings.py
- backend/Dockerfile
- backend/core/tests.py
- docs/AI_CHANGELOG.md

Functions / Classes / Configuration:
- `get_list_setting()` (added `environment` parameter)
- `SECURE_PROXY_SSL_HEADER` and the `if not DEBUG:` security block
- `ProductionEnvironmentParsingTests`

Tests Added:
- `test_allowed_hosts_splits_and_strips_comma_separated_values`
- `test_cors_origins_parse_https_and_wildcard_entries`
- `test_csrf_trusted_origins_parse_comma_separated_values`
- `test_missing_value_falls_back_to_default`
- `test_empty_string_yields_empty_list`
- `test_settings_expose_parsed_lists`

Verification:
- `python manage.py check` — passed with no issues.
- `python manage.py test` — passed: 42 tests (36 prior + 6 new).
- Manual `DEBUG=False` shell check confirmed comma parsing plus
  `SECURE_PROXY_SSL_HEADER`, `SECURE_SSL_REDIRECT`, secure cookies, and HSTS
  all activate; a clean-environment `DEBUG=True` check confirmed local defaults
  (localhost hosts, Vite CORS, no SSL redirect, non-secure cookies) are
  unchanged.

Unnecessary Alternatives Considered:
- Did not convert wildcard origins (e.g. `https://*.vercel.app`) into
  `CORS_ALLOWED_ORIGIN_REGEXES`. The audit required only safe comma-separated
  parsing; adding regex translation would change CORS matching behavior beyond
  the task scope and is left as a documented follow-up if wildcard matching is
  later required.
- Did not add a `render.yaml`, a separate settings module, python-dotenv, or an
  entrypoint script; the existing single settings module plus the shell-form
  Docker CMD already satisfies the `$PORT` and proxy requirements.

Scope Control:
- No secrets, passwords, or host domains were hardcoded.
- No React components, frontend styles, page layouts, database models,
  migrations, or public REST API schemas were changed.
- Local development defaults (running with no environment variables) are
  preserved.

---

## CHANGE-0021 — Configure Vercel SPA Routing and Verify Frontend Build

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
deployment / frontend

Requirement:
ARCHITECTURE.md §7 defines the client-side React Router routes (`/about`,
`/activities/:slug`, `/events/:slug`, `/news/:slug`, `/team`, `/membership`,
`/contact`, `/gallery`, …) and §13 states the frontend and backend deploy
independently. The Vercel frontend deployment therefore needs single-page
application (SPA) rewriting so direct navigation and browser refreshes on those
deep routes resolve to the built `index.html`.

Audit Finding Addressed:
The frontend lacked a `vercel.json` routing configuration. On Vercel, direct
navigation or a browser refresh on a non-root path (for example `/gallery`,
`/membership`, or `/about`) would return HTTP 404 because the static host has
no server-side route for those client-side paths and no SPA rewrite existed.

Implementation:
- Added `frontend/vercel.json` with the standard SPA rewrite
  `{ "source": "/(.*)", "destination": "/index.html" }`. Vercel serves existing
  static files (hashed JS/CSS/images under `/assets`) from the filesystem first,
  so only unknown client-side routes are rewritten to the built `index.html`.
- Verified the API base URL fallback in `frontend/src/services/api.js` already
  reads `import.meta.env.VITE_API_BASE_URL` and falls back to the local
  development default `http://127.0.0.1:8000/api` (the `/api` prefix is required
  by the documented endpoint paths). No change was needed, and the request
  contract was intentionally left untouched.
- Confirmed `frontend/vite.config.js` uses the default Vite `dist` output, which
  is the directory Vercel deploys and the location of the rewrite target.

Build Verification:
- `npm run build` (`vite build`) from `frontend/` — passed cleanly: Vite 8.2.2,
  519 modules transformed, `dist/index.html` plus hashed CSS/JS and image assets
  emitted, built in ~700ms, with no TypeScript, JSX, or bundling errors.

Files Changed:
- frontend/vercel.json (created)
- docs/AI_CHANGELOG.md

Configuration Added:
- `frontend/vercel.json` SPA `rewrites` rule.

Unnecessary Alternatives Considered:
- Did not add a `redirects` block, a `builds` array, a `framework` key, or a
  custom `_redirects` file. A single catch-all rewrite is the documented,
  minimal Vite/React Router SPA configuration and avoids conflicting with
  Vercel's automatic static asset handling.
- Did not change `vite.config.js`, the Axios client, environment variable names,
  or the existing Docker/Nginx deployment path; those are out of scope for this
  Vercel routing task.

Scope Control:
- No React components, page layouts, or styles were redesigned.
- No backend Django settings, database models, or migrations were modified.
- No new frontend dependencies or UI libraries were added.
- No API request contract was changed; the `VITE_API_BASE_URL` fallback and the
  local development default remain intact.

---

## CHANGE-0022 — Final Pre-Launch Smoke Test and Readiness Sign-Off

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
documentation / deployment sign-off

Pre-Launch Readiness Status:
GREEN.

Requirement:
Final verification pass prior to production deployment across the backend and
frontend build environments, confirming the cumulative pre-launch audit
remediations (CHANGE-0014 through CHANGE-0022) are complete and non-regressed.

Backend Verification (run from `backend/` in a clean local-default environment):
- `python manage.py check` — passed: "System check identified no issues
  (0 silenced)." (exit code 0).
- `python manage.py makemigrations --check` — passed: "No changes detected,"
  confirming zero pending migrations (exit code 0).
- `python manage.py test` — passed: 42 tests, "OK" (exit code 0), with zero
  errors or unexpected failures.

Frontend Verification (run from `frontend/`):
- `npm run build` (`vite build`) — passed cleanly: Vite 8.2.2, 519 modules
  transformed, `dist/index.html` plus hashed CSS/JS and image assets emitted,
  no TypeScript, JSX, or bundling errors (exit code 0).

Audit Items Completed (CHANGE-0014 through CHANGE-0022):
- CHANGE-0014 — Default media storage restored (FileSystemStorage default).
- CHANGE-0015 — Backend Docker build-context hygiene (.dockerignore).
- CHANGE-0016 — Backend virtual environment aligned with requirements.
- CHANGE-0017 — Public form submissions throttled (contact/membership).
- CHANGE-0018 — Image upload size and extension validation.
- CHANGE-0019 — Conditional Supabase S3 media storage.
- CHANGE-0020 — Production host, CORS/CSRF, proxy, and security headers.
- CHANGE-0021 — Vercel SPA routing configuration.
- CHANGE-0022 — This final pre-launch smoke test and sign-off.

Files Changed:
- docs/AI_CHANGELOG.md

Verification:
- Backend check/makemigrations/test exit codes: 0 / 0 / 0.
- Backend passing test count: 42.
- Pending migrations: none.
- Frontend production build exit code: 0 (clean bundle).

Scope Control:
- This is a verification-only pass. No application code, configuration, models,
  migrations, dependencies, or documentation content other than this changelog
  entry was modified.

Sign-Off:
All documented pre-launch backend and frontend verification checks pass with
zero errors, zero pending migrations, and a clean production bundle. The
Alliance Yuwa Club V1 codebase is signed off as ready for production
deployment (backend to Render, frontend to Vercel) with the required
environment variables supplied by each hosting provider.

---

## CHANGE-0023 — Implement React Frontend SEO Infrastructure

Date:
2026-09-04

Agent:
OpenAI Codex

Type:
frontend / SEO

Requirement:
REQUIREMENTS.md and ARCHITECTURE.md require a launch-ready public website with
basic SEO (per DEVELOPMENT.md Day 8 "SEO basics"). The React single-page
frontend previously had only a static `index.html` title/favicon and no
per-route metadata, structured data, or crawler files.

Audit Finding Addressed:
The frontend lacked SEO infrastructure: no dynamic per-page `<title>`/meta
description/Open Graph/canonical tags, no `robots.txt`/`sitemap.xml`, and no
Schema.org structured data, limiting search-engine indexing and social-link
preview quality.

Implementation:
- Installed `react-helmet-async` (added to `frontend/package.json`; 5 packages,
  0 vulnerabilities).
- Wrapped the application root in `frontend/src/main.jsx` with
  `<HelmetProvider>` (outside `BrowserRouter`), enabling safe head-tag management.
- Added a reusable `frontend/src/components/Seo.jsx` that renders only Helmet
  tags (title with site-name suffix, meta description, canonical link, Open
  Graph `og:type/site_name/title/description/url`, and Twitter card tags) and
  contributes no visible DOM, so page layout and styling are unchanged. The
  canonical origin defaults to `https://allianceyuwaclub.org.np` and is
  overridable via `VITE_SITE_URL` for preview/staging hosts.
- Applied `<Seo>` to the five key routes: Home (`/`), About (`/about`),
  Gallery (`/gallery`), Membership (`/membership`), and Contact (`/contact`),
  each with a tailored title and meta description.
- Created `frontend/public/robots.txt` (allow all, disallow `/admin/`, sitemap
  reference) and `frontend/public/sitemap.xml` with canonical URLs for the five
  routes. Vite copies `public/` verbatim, so both are emitted to `dist/`.
- Added a Schema.org `NGO` JSON-LD block to `frontend/index.html` `<head>`.

Dependencies Added:
- react-helmet-async — required for client-side management of document head
  metadata (title/meta/OG/canonical) in the React SPA.

Files Changed:
- frontend/package.json (dependency added)
- frontend/src/main.jsx (HelmetProvider)
- frontend/src/components/Seo.jsx (new)
- frontend/src/pages/Home.jsx
- frontend/src/pages/About.jsx
- frontend/src/pages/Gallery.jsx
- frontend/src/pages/Membership.jsx
- frontend/src/pages/Contact.jsx
- frontend/public/robots.txt (new)
- frontend/public/sitemap.xml (new)
- frontend/index.html (JSON-LD)
- docs/AI_CHANGELOG.md

Build Verification:
- `npm run build` (`vite build`) from `frontend/` — passed cleanly (exit code 0):
  Vite 8.2.2, 524 modules transformed, no TypeScript/JSX/bundling errors.
- Confirmed `dist/robots.txt` and `dist/sitemap.xml` are emitted and the
  `application/ld+json` script is present in `dist/index.html`.

Scope Control:
- No component layouts or visual styling were redesigned; `Seo` renders only
  head metadata.
- No backend Django settings, models, migrations, or API request contracts were
  changed.
- The only new dependency is `react-helmet-async`, explicitly required by this
  task.

---

## CHANGE-0003 - Normalize Production Domain and Configuration

Date:
2026-09-05

Agent:
GitHub Copilot

Type:
security / deployment / documentation

Requirement:
The official production website is `https://allianceyuwaclub.org.np` and the
API is `https://api.allianceyuwaclub.org.np`. Production configuration must not
silently fall back to development database, origin, or media settings.

Reason:
Production references were inconsistent across documentation, frontend build
defaults, Docker configuration, SEO, and deployment routing. DEBUG=False also
allowed database and media fallbacks that were inappropriate for production.

Files Changed:
- backend/config/settings.py
- backend/core/tests.py
- docker-compose.yml
- frontend/Dockerfile
- frontend/.env.production.example
- README.md
- docs/REQUIREMENTS.md
- docs/ARCHITECTURE.md
- docs/API.md
- docs/DEVELOPMENT.md

Implementation:
- Normalized active production references to the official `.org.np` website and
  API hosts.
- Required `DATABASE_URL`, non-empty `ALLOWED_HOSTS`,
  `CORS_ALLOWED_ORIGINS`, and `CSRF_TRUSTED_ORIGINS` when `DEBUG=False`.
- Required Supabase-compatible durable media storage when `DEBUG=False`.
- Updated Docker Compose production defaults and required media variables.
- Preserved local DEBUG=True fallbacks and existing Render/Vercel routing.

Database Changes:
None. No migrations were created.

API Changes:
None. API routes and response contracts were not changed.

Tests:
- Added a regression test for the production durable-media requirement.

Verification:
- `python manage.py check` passed.
- `python manage.py test` passed.
- `python manage.py makemigrations --check` passed.
- `npm run lint` passed.
- `npm run build` passed.
- Repository-wide search confirmed no active superseded-domain or placeholder
  production references remain.

Unnecessary Alternatives Considered:
No dependencies, frontend redesign, API changes, migrations, or unrelated
refactors were introduced.

Related Documentation:
- REQUIREMENTS.md
- ARCHITECTURE.md
- API.md
- DEVELOPMENT.md

---

## CHANGE-0025 - Add Membership Email Notifications

Date:
2026-09-05

Agent:
GitHub Copilot

Type:
feature / security

Requirement:
Membership submissions require applicant confirmation, and authorized staff
need explicit approval/rejection workflows with status notifications.

Reason:
The existing membership flow saved applications but did not notify applicants
or provide explicit, non-duplicating review actions in Django Admin.

Files Changed:
- backend/config/settings.py
- backend/memberships/emails.py
- backend/memberships/views.py
- backend/memberships/admin.py
- backend/memberships/tests.py
- docs/DEVELOPMENT.md
- README.md
- docs/AI_CHANGELOG.md

Implementation:
- Added a small plain-text membership email service for receipt, approval, and
  rejection messages.
- Sends the receipt after the application is saved, preserving the existing
  HTTP 201 response if delivery fails; failures are logged without sensitive
  application data.
- Added explicit Admin approve/reject actions that set status, review time,
  reviewer, and send one status email only when the status changes.
- Configured Gmail SMTP through Django settings and environment variables.
  DEBUG=True without an explicit backend continues to use the console backend.

Database Changes:
None. Existing status, reviewed_at, reviewed_by, and primary-key reference
fields were sufficient. No migration was created.

API Changes:
None. The membership submission response remains unchanged.

Dependencies Added:
None.

Tests:
- Membership submission saves a pending application and sends a personalized
  receipt through Django's in-memory email backend.
- SMTP failure preserves the saved application and successful API response.
- Admin approval and rejection update review metadata and send notifications.
- Repeating an Admin action does not resend a notification.
- Admin status changes persist when notification delivery fails.
- SMTP password setting is read from environment configuration.

Verification:
- `python manage.py check` passed.
- `python manage.py test memberships` passed (11 tests).
- `python manage.py test` passed (53 tests).
- `python manage.py makemigrations --check` passed.
- `npm run lint` passed.
- `npm run build` passed.

Security:
- No Gmail password or App Password is stored in source, documentation, Git,
  or frontend files.
- Approval/rejection emails do not include admin notes or unnecessary personal
  information.

---

## CHANGE-0026 - Migrate Membership Email Delivery to Resend

Date:
2026-09-05

Agent:
GitHub Copilot

Type:
security / deployment / feature maintenance

Requirement:
Production membership notifications must work on Render Free, where outbound
SMTP ports are blocked. The existing membership workflow and API contract must
remain unchanged.

Reason:
The previous Gmail SMTP configuration correctly reached `smtp.gmail.com:587`
but failed at network connection time on Render. Resend provides an HTTPS API
transport that is compatible with the deployed environment.

Files Changed:
- backend/config/settings.py
- backend/memberships/emails.py
- backend/memberships/tests.py
- README.md
- docs/DEVELOPMENT.md
- docs/AI_CHANGELOG.md

Implementation:
- Replaced production SMTP selection with the Resend HTTPS API.
- Kept the public notification functions and Admin/API call sites unchanged.
- Added one provider boundary with an explicit configurable timeout.
- Preserved the local console email backend when DEBUG=True and Resend is not
  configured.
- Configured the verified sender as `no-reply@allianceyuwaclub.org.np` with
  `Alliance Yuwa Club` as the sender name and the Gmail account as Reply-To.
- Resend failures return safely without changing saved application/status data.

Environment Variables:
- EMAIL_PROVIDER
- RESEND_API_KEY
- EMAIL_FROM_EMAIL
- EMAIL_FROM_NAME
- EMAIL_REPLY_TO

No API key or other credential is stored in source, documentation, Git, or
frontend files.

Database Changes:
None. No migrations were created.

API Changes:
None. Membership request and response contracts are unchanged.

Dependencies Added:
None. The adapter uses Python's standard HTTPS library.

Tests:
- Resend payload, sender, Reply-To, and timeout are tested with mocked HTTPS.
- Provider timeout and delivery failure are handled without data loss.
- Existing receipt, approval, rejection, duplicate-prevention, and API tests
  remain covered.

Verification:
- `python manage.py check`
- `python manage.py test`
- `python manage.py makemigrations --check`
- `npm run lint`
- `npm run build`
