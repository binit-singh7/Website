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

---

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
