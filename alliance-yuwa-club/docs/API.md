# Alliance Yuwa Club
## API Specification — V1

---

# 1. API Overview

The Alliance Yuwa Club backend exposes a RESTful API using Django REST
Framework.

The React frontend communicates with the Django backend through these
API endpoints.

The API is responsible for:

- Public website content.
- Membership applications.
- Contact messages.
- Administrative content management.
- Authentication and authorization for protected operations.

Base URL during local development:

```text
http://127.0.0.1:8000/api/

Production:

https://allianceyuwaclub.com.np/api/

The production API domain may be separated from the public frontend
domain depending on deployment configuration.

2. API Design Principles

The API should follow these principles:

Use standard HTTP methods.
Return JSON responses.
Use meaningful HTTP status codes.
Keep public endpoints simple.
Keep administrative operations protected.
Use pagination for large collections.
Validate all incoming data on the backend.
Do not expose private administrative information.
Use slugs for public detail URLs where appropriate.
Keep response structures consistent.
Avoid returning unnecessary fields.
Follow REST conventions where practical.
3. HTTP Methods

The API will use:

GET
POST
PATCH
PUT
DELETE

General usage:

GET     Retrieve data
POST    Create data
PATCH   Partially update data
PUT     Replace/update data where appropriate
DELETE  Delete data

Public users will generally use GET endpoints.

Public form submissions may use POST.

Administrative create, update, and delete operations require
authentication and appropriate permissions.

4. HTTP Status Codes

The API should use appropriate status codes.

200 OK
201 Created
204 No Content
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
405 Method Not Allowed
409 Conflict
429 Too Many Requests
500 Internal Server Error

Examples:

Successful GET       → 200
Successful POST      → 201
Successful DELETE    → 204
Invalid form data    → 400
Not authenticated    → 401
Not authorized       → 403
Resource not found   → 404

The backend should not return unnecessary 500 errors for expected
validation failures.

5. API Versioning

V1 endpoints use:

/api/

A future breaking version may use:

/api/v2/

V1 should remain stable after the initial launch wherever practical.

6. Activities API

Activities represent programs and activities conducted by Alliance
Yuwa Club.

6.1 List Activities
GET /api/activities/

Authentication:

Not required

Only published activities should normally be returned.

Example response:

{
  "count": 25,
  "next": "http://example.com/api/activities/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "International Youth Day Border Cleanliness & Awareness Drive",
      "slug": "international-youth-day-border-cleanliness-awareness-drive",
      "description": "Community cleanup and awareness activity...",
      "date": "2026-08-12",
      "location": "Biratnagar–Jogbani (Rani) border area",
      "category": {
        "id": 2,
        "name": "Environment",
        "slug": "environment"
      },
      "featured": true,
      "cover_image": null
    }
  ]
}
6.2 Activity Detail
GET /api/activities/<slug>/

Authentication:

Not required

Returns a single published activity.

Example:

{
  "id": 1,
  "title": "International Youth Day Border Cleanliness & Awareness Drive",
  "slug": "international-youth-day-border-cleanliness-awareness-drive",
  "description": "Community cleanup and plastics collection activity...",
  "date": "2026-08-12",
  "location": "Biratnagar–Jogbani (Rani) border area",
  "category": {
    "id": 2,
    "name": "Environment",
    "slug": "environment"
  },
  "featured": true,
  "cover_image": null,
  "images": []
}
6.3 Activity Filtering

Supported query parameters:

category
year
featured
page
page_size

Examples:

GET /api/activities/?category=environment
GET /api/activities/?year=2026
GET /api/activities/?featured=true

Parameters may be combined:

GET /api/activities/?category=sports&year=2026
7. Activity Categories API
7.1 List Categories
GET /api/activity-categories/

Authentication:

Not required

Example:

[
  {
    "id": 1,
    "name": "Community Service",
    "slug": "community-service"
  },
  {
    "id": 2,
    "name": "Environment",
    "slug": "environment"
  }
]

Categories should normally be returned only when active/usable.

8. Events API

Events represent scheduled or publicly presented events.

8.1 List Events
GET /api/events/

Authentication:

Not required

Public response should contain appropriate event information.

Example:

{
  "count": 10,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Youth Convention",
      "slug": "youth-convention",
      "description": "Youth convention organized by Alliance Yuwa Club.",
      "start_datetime": "2026-09-15T10:00:00+05:45",
      "end_datetime": "2026-09-15T16:00:00+05:45",
      "location": "Biratnagar",
      "status": "upcoming",
      "featured": true,
      "registration_required": false,
      "registration_url": null,
      "cover_image": null
    }
  ]
}
8.2 Event Detail
GET /api/events/<slug>/

Authentication:

Not required
8.3 Event Filtering

Supported query parameters:

status
year
featured
page
page_size

Examples:

GET /api/events/?status=upcoming
GET /api/events/?year=2026
9. News API

The news API manages public announcements, articles, and updates.

9.1 List News
GET /api/news/

Authentication:

Not required

Only published news should normally be returned.

Example:

{
  "count": 10,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Alliance Yuwa Club Conducts General Convention",
      "slug": "alliance-yuwa-club-conducts-general-convention",
      "excerpt": "The organization conducted its first general convention...",
      "featured_image": null,
      "published_at": "2026-08-16T10:00:00+05:45"
    }
  ]
}
9.2 News Detail
GET /api/news/<slug>/

Authentication:

Not required
9.3 News Filtering

Supported query parameters:

year
page
page_size
10. Team API

The team API provides public executive committee information.

10.1 List Team Members
GET /api/team/

Authentication:

Not required

Only active team members should be returned.

Example:

[
  {
    "id": 1,
    "name": "Example Name",
    "position": "President",
    "bio": "Short public biography.",
    "photo": null,
    "display_order": 1
  }
]

Private contact information must not be returned unless specifically
approved for public display.

11. Organization API

The API may expose official organization information required by the
public website.

11.1 Organization Information
GET /api/organization/

Authentication:

Not required

Possible public fields:

name
short_name
description
motto
vision
mission
address
phone
email
social links
logo

Legal or registration information must only be exposed after official
verification and approval.

12. Membership API

The membership API allows prospective members to submit applications.

12.1 Submit Membership Application
POST /api/membership/apply/

Authentication:

Not required

Example request:

{
  "full_name": "Example User",
  "date_of_birth": "2002-04-10",
  "phone": "98XXXXXXXX",
  "email": "example@email.com",
  "address": "Biratnagar",
  "ward": "10",
  "occupation": "Student",
  "education": "Bachelor's",
  "areas_of_interest": [
    "Social Service",
    "Environment"
  ],
  "reason_for_joining": "I want to participate in community service."
}

Successful response:

{
  "message": "Membership application submitted successfully."
}

The API should normally return:

201 Created
12.2 Membership Validation

The backend must validate:

Required fields.
Email format.
Phone format where applicable.
Date format.
Reasonable field lengths.
Accepted areas of interest.

Administrative fields such as:

status
reviewed_at
reviewed_by
admin_notes

must not be accepted from public users.

The backend controls these fields.

13. Contact API
13.1 Submit Contact Message
POST /api/contact/

Authentication:

Not required

Example request:

{
  "name": "Example User",
  "email": "example@email.com",
  "phone": "98XXXXXXXX",
  "subject": "Membership Inquiry",
  "message": "I would like to learn more about joining the club."
}

Successful response:

{
  "message": "Your message has been submitted successfully."
}

Expected status:

201 Created
14. Gallery API

Gallery content is public when published.

14.1 List Albums
GET /api/gallery/albums/

Authentication:

Not required

Only published albums should be returned.

14.2 Album Detail
GET /api/gallery/albums/<slug>/

Authentication:

Not required

The response may include the album's images.

Example:

{
  "id": 1,
  "title": "International Youth Day Border Cleanliness Drive 2026",
  "slug": "international-youth-day-border-cleanliness-drive-2026",
  "description": "Photos from the community cleanup drive.",
  "date": "2026-08-12",
  "cover_image": null,
  "images": []
}
15. Announcements API

Announcements are short official messages shown on the website.

15.1 Active Announcements
GET /api/announcements/

Authentication:

Not required

Only active/public announcements should be returned.

Expired announcements should normally be excluded.

16. Administrative API

Administrative operations are protected.

The exact administrative URLs may use the same resource endpoints with
authentication and permission checks.

Examples:

POST   /api/activities/
PATCH  /api/activities/<slug>/
DELETE /api/activities/<slug>/

POST   /api/events/
PATCH  /api/events/<slug>/
DELETE /api/events/<slug>/

POST   /api/news/
PATCH  /api/news/<slug>/
DELETE /api/news/<slug>/

These operations require authentication.

17. Authentication

V1 administrative authentication may use Django authentication with
token-based API authentication where required by the React
administration interface.

The exact authentication implementation must prioritize security and
simplicity.

Possible implementation:

JWT authentication

using an established Django REST Framework compatible package.

Public endpoints do not require authentication.

18. Permissions

The API should distinguish between:

Public user
Authenticated staff
Administrator
Super administrator

V1 may initially use Django's built-in user and group permissions.

Future roles may include:

Executive Administrator
Content Manager
Membership Manager

Users must only perform operations allowed by their permissions.

19. Sensitive Data Protection

The following data must never be returned by public endpoints:

MembershipApplication.status
MembershipApplication.reviewed_by
MembershipApplication.admin_notes

ContactMessage records

Administrative user information

Draft content

Archived private content

Public serializers and administrative serializers should be separated
where necessary.

20. Validation

All public POST requests must be validated by Django REST Framework.

Invalid requests should return structured errors.

Example:

{
  "email": [
    "Enter a valid email address."
  ],
  "full_name": [
    "This field is required."
  ]
}

The API should not trust frontend validation.

Frontend validation improves user experience, but backend validation is
authoritative.

21. Pagination

Collection endpoints must support pagination.

Initial paginated endpoints:

/api/activities/
/api/events/
/api/news/
/api/gallery/albums/

Example:

{
  "count": 100,
  "next": "http://example.com/api/activities/?page=2",
  "previous": null,
  "results": []
}

The page size should be configurable.

22. Filtering

Activities:

category
year
featured

Events:

status
year
featured

News:

year

Future filtering may include:

location
date range
search

but advanced filtering is not required for the first release.

23. Ordering

Default ordering should be defined at the API/view level or model
level where appropriate.

Suggested public ordering:

Activities

Newest first.

date DESC
Events

Upcoming events ordered by start date.

Past events ordered newest first.

News

Newest published articles first.

published_at DESC
Team

Use:

display_order ASC
24. Search

Full search is not required for V1.

Basic filtering is sufficient for launch.

A future version may introduce:

GET /api/search/?q=environment

across:

Activities
Events
News
25. API Error Format

Errors should use a consistent JSON structure.

Example:

{
  "detail": "Requested resource was not found."
}

Validation errors may provide field-specific messages:

{
  "email": [
    "Enter a valid email address."
  ]
}

Do not expose internal stack traces or database errors to public users.

26. CORS

During local development, the backend should allow the configured
React development origin.

Example:

http://localhost:5173

Production CORS configuration must contain only trusted frontend
origins.

Do not use unrestricted CORS such as:

CORS_ALLOW_ALL_ORIGINS = True

in production.

27. CSRF and Security

All state-changing operations must follow Django's security
requirements.

The implementation must:

Use HTTPS in production.
Keep secret keys private.
Configure trusted origins.
Validate user input.
Protect authenticated operations.
Avoid exposing internal errors.
Apply appropriate rate limiting or abuse protection to public forms
where necessary.
28. Public API Summary
GET  /api/organization/

GET  /api/activity-categories/
GET  /api/activities/
GET  /api/activities/<slug>/

GET  /api/events/
GET  /api/events/<slug>/

GET  /api/news/
GET  /api/news/<slug>/

GET  /api/team/

GET  /api/gallery/albums/
GET  /api/gallery/albums/<slug>/

GET  /api/announcements/

POST /api/membership/apply/

POST /api/contact/
29. Administrative API Summary

Administrative endpoints require authentication and permissions.

POST   /api/activities/
PATCH  /api/activities/<slug>/
DELETE /api/activities/<slug>/

POST   /api/events/
PATCH  /api/events/<slug>/
DELETE /api/events/<slug>/

POST   /api/news/
PATCH  /api/news/<slug>/
DELETE /api/news/<slug>/

POST   /api/team/
PATCH  /api/team/<id>/
DELETE /api/team/<id>/

POST   /api/gallery/albums/
PATCH  /api/gallery/albums/<slug>/
DELETE /api/gallery/albums/<slug>/

Exact administrative endpoints may be adjusted during implementation
provided that the public API contract remains consistent.

30. API Development Rules for AI Coding Agents

Copilot and Codex must follow this document when implementing APIs.

Rules:

Do not invent undocumented public endpoints.
Do not change existing endpoint names without approval.
Use serializers for validation and data representation.
Use appropriate HTTP methods.
Use appropriate HTTP status codes.
Protect administrative operations.
Never expose private membership or contact information.
Use pagination for large collections.
Follow the documented filtering behavior.
Keep response structures consistent.
Add tests for important API behavior.
Do not expose Django debug information through API responses.
Do not add unnecessary API dependencies.
Update this document when an approved API change is made.
31. API Testing Requirements

Important endpoints must have automated tests.

At minimum test:

Activities list
Activity detail
Activity filtering

Events list
Event detail

News list
News detail

Team list

Membership application
Membership validation

Contact form submission

Protected administrative operations

Permission failures

404 behavior

Pagination

Example test scenarios:

Published activity is visible publicly.
Draft activity is not visible publicly.
Invalid membership application is rejected.
Unauthenticated user cannot modify activities.
Authorized administrator can create an activity.
Contact form creates a message.
Private admin notes are not exposed publicly.
32. Backward Compatibility

Once a V1 public API is released, avoid unnecessary breaking changes.

When a change is required:

Update the documentation.
Update backend tests.
Update the React client.
Check existing frontend functionality.
Document the change in Git.

Major breaking changes may require a new API version.

33. Definition of API Complete

The V1 API is considered complete when:

[ ] Public endpoints are implemented.
[ ] Protected endpoints are authenticated.
[ ] Permissions are enforced.
[ ] Validation works.
[ ] Pagination works.
[ ] Filtering works.
[ ] Private data is protected.
[ ] API tests pass.
[ ] React can consume the required endpoints.
[ ] API documentation matches the implementation.