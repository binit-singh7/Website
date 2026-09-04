# Alliance Yuwa Club
## Database Design — V1

---

## 1. Database Overview

Alliance Yuwa Club V1 will use PostgreSQL as the production database.

The database will store:

- Organization information
- Activities and programs
- Events
- News and updates
- Executive committee/team members
- Membership applications
- Gallery albums and images
- Contact messages
- Announcements

The database must be designed so that the organization can continue
adding activities, events, members, news, and media for many years.

The system currently has approximately six years of organizational
history and more than 100 programs.

---

## 2. Database Principles

The database should follow these principles:

1. Avoid unnecessary duplication of data.
2. Use Django ORM for database access.
3. Use PostgreSQL in production.
4. Use foreign keys for relationships.
5. Use timestamps on important content records.
6. Use slugs for public detail-page URLs.
7. Use status fields where content may be drafted or published.
8. Avoid storing sensitive information unless required.
9. Do not hardcode website content that should be managed through the
   database.
10. Database models must remain simple enough for future developers
    and AI coding agents to understand.

---

# 3. Entity Overview

The initial entities are:

```text
Organization
    |
    +── Site Settings / Global Information

Activity
    |
    +── Activity Category
    |
    +── Activity Images

Event
    |
    +── Event Images

News Article

Team Member

Membership Application

Gallery Album
    |
    +── Gallery Images

Contact Message

Announcement

Django's built-in User model will be used for administrative accounts.

4. Organization

The organization model stores official club information that may be
displayed throughout the website.

Model: Organization

Suggested fields:

id
name
short_name
description
motto
vision
mission
address
phone
email
facebook_url
instagram_url
youtube_url
logo
created_at
updated_at

Only one primary organization record is expected in V1.

The exact legal/registration details must only be added after they are
verified against official organizational documents.

5. Activity Category

Activities need categories so that visitors can filter the archive.

Model: ActivityCategory

Fields:

id
name
slug
description
created_at
updated_at

Initial categories:

Community Service
Environment
Youth & Leadership
Sports
Culture
Awareness
Health
Other

Categories must be database records rather than hardcoded values so
that administrators can add or modify categories later.

6. Activity

The Activity model is one of the most important models in the system.

It represents historical and current programs conducted by the
organization.

Examples include:

Community cleanup drives
Environmental campaigns
Youth leadership activities
Sports programs
Cultural programs
Awareness programs
Social welfare activities
Model: Activity

Fields:

id
title
slug
description
date
location
category
featured
status
cover_image
created_at
updated_at
Field rules
title

Required.

The public name of the activity.

slug

Required and unique.

Used for URLs such as:

/activities/international-youth-day-border-cleanliness-drive/
description

Required.

Contains the main description/report of the activity.

date

Required.

Stores the date on which the activity took place.

location

Optional.

Stores where the activity was conducted.

category

Foreign key to ActivityCategory.

featured

Boolean.

Used to determine whether the activity appears in featured sections
such as the homepage.

status

Possible values:

draft
published
archived

Only published activities should normally appear publicly.

cover_image

Optional image representing the activity.

Historical images may be added later.

7. Activity Image

An activity may contain multiple images.

Model: ActivityImage

Fields:

id
activity
image
caption
display_order
created_at

Relationship:

Activity 1 ──────── * ActivityImage

One activity can have many images.

Images should be ordered using display_order.

Historical photographs do not have to be migrated before the initial
website launch.

8. Event

An Event represents a scheduled organizational event.

Activities and events are intentionally separate concepts.

An activity represents something the organization has conducted or
completed, while an event represents a scheduled/publicly presented
event.

Model: Event

Fields:

id
title
slug
description
start_datetime
end_datetime
location
status
featured
registration_required
registration_url
cover_image
created_at
updated_at

Possible status values:

draft
upcoming
ongoing
completed
cancelled
9. Event Image
Model: EventImage

Fields:

id
event
image
caption
display_order
created_at

Relationship:

Event 1 ──────── * EventImage
10. News Article

The News model stores official updates and articles.

Model: NewsArticle

Fields:

id
title
slug
excerpt
content
featured_image
author
status
published_at
created_at
updated_at

Possible status values:

draft
published
archived
Author

The author should use Django's built-in User model.

Relationship:

User 1 ──────── * NewsArticle
11. Team Member

This model stores executive committee and organizational team
information.

Model: TeamMember

Fields:

id
name
position
bio
photo
phone
email
display_order
is_active
created_at
updated_at

Not every team member needs to have a publicly displayed phone number
or email address.

Contact information should only be published when approved by the
organization.

Team members should be ordered using display_order.

12. Membership Application

V1 will use an application-based membership process.

Visitors submit an application through the public website.

Model: MembershipApplication

Fields:

id
full_name
date_of_birth
phone
email
address
ward
occupation
education
areas_of_interest
reason_for_joining
status
submitted_at
reviewed_at
reviewed_by
admin_notes

Possible status values:

pending
approved
rejected
Relationships
User 1 ──────── * MembershipApplication

The reviewed_by relationship is optional because an application may
still be pending.

Administrative notes must never be publicly exposed through the API.

13. Gallery Album

The gallery should support event/activity based photo organization.

Model: GalleryAlbum

Fields:

id
title
slug
description
date
cover_image
is_published
created_at
updated_at

Examples:

International Youth Day Border Cleanliness Drive 2026

First General Convention 2026

Women's Sports and Cultural Festival 2083
14. Gallery Image
Model: GalleryImage

Fields:

id
album
image
caption
display_order
created_at

Relationship:

GalleryAlbum 1 ──────── * GalleryImage

The gallery is designed now, but historical image migration will be
performed later when the organization's photographs are organized.

15. Contact Message

Visitors can contact the organization through the website.

Model: ContactMessage

Fields:

id
name
email
phone
subject
message
status
created_at
updated_at

Possible status values:

unread
read
replied
archived

Contact messages are private administrative data.

They must never be exposed through public API endpoints.

16. Announcement

Announcements are short official notices that may appear on the
website.

Model: Announcement

Fields:

id
title
content
priority
is_active
start_date
end_date
created_at
updated_at

Possible priority values:

normal
important
urgent

An announcement should only be publicly visible when:

is_active = true

and the current date falls within the configured date range when dates
are provided.

17. Relationship Diagram

The high-level relationships are:

                     ┌─────────────────┐
                     │  ActivityCategory│
                     └────────┬────────┘
                              │
                              │ 1:N
                              ▼
                     ┌─────────────────┐
                     │    Activity     │
                     └────────┬────────┘
                              │
                              │ 1:N
                              ▼
                     ┌─────────────────┐
                     │ ActivityImage   │
                     └─────────────────┘


                     ┌─────────────────┐
                     │      Event      │
                     └────────┬────────┘
                              │
                              │ 1:N
                              ▼
                     ┌─────────────────┐
                     │   EventImage    │
                     └─────────────────┘


                     ┌─────────────────┐
                     │  GalleryAlbum   │
                     └────────┬────────┘
                              │
                              │ 1:N
                              ▼
                     ┌─────────────────┐
                     │  GalleryImage   │
                     └─────────────────┘


                     ┌─────────────────┐
                     │      User       │
                     └───────┬─┬───────┘
                             │ │
                ┌────────────┘ └────────────┐
                ▼                           ▼
        ┌─────────────────┐         ┌─────────────────┐
        │   NewsArticle   │         │MembershipApplication│
        └─────────────────┘         └─────────────────┘
18. Deletion Rules

Important relationships must use appropriate Django on_delete
behavior.

General guidance:

ActivityCategory → Activity

Do not automatically delete historical activities when a category is
deleted.

Prefer:

PROTECT

or carefully restrict category deletion.

Activity → ActivityImage

When an activity is deleted, its activity images may also be removed.

Prefer:

CASCADE
Event → EventImage

Prefer:

CASCADE
GalleryAlbum → GalleryImage

Prefer:

CASCADE
User → NewsArticle

Historical articles should normally remain if an author account is
deleted.

Prefer:

SET_NULL

where the author field is nullable.

User → MembershipApplication

Reviewed applications should retain their records where possible.

Prefer:

SET_NULL

for reviewed_by.

19. Indexing

Indexes should be added where they improve common queries.

Initial candidates:

Activity.date
Activity.status
Activity.slug
Activity.category

Event.start_datetime
Event.status
Event.slug

NewsArticle.published_at
NewsArticle.status
NewsArticle.slug

MembershipApplication.status
MembershipApplication.submitted_at

ContactMessage.status
ContactMessage.created_at

Django model indexes should be used rather than manually writing SQL
for normal application requirements.

20. Slugs

Public content models should use unique slugs.

Models requiring slugs:

Activity
Event
NewsArticle
GalleryAlbum
ActivityCategory

URLs should use slugs rather than database IDs where appropriate.

Example:

/activities/border-cleanliness-awareness-drive/

/events/womens-sports-festival-2083/

/news/general-convention-2026/
21. Timestamps

Important content models should include:

created_at
updated_at

These fields should generally be automatically managed by Django.

22. Publication Rules

Public APIs should return only appropriate published content.

For example:

Activities
status = published
News
status = published
Announcements
is_active = true
Team members
is_active = true

Administrative APIs may access draft, archived, and pending content
according to permissions.

23. Pagination

Large collections must not be returned in a single API response.

Pagination must be used for:

Activities
Events
News
Gallery
Membership applications in admin interfaces
Contact messages in admin interfaces

The default public API pagination size should be reasonable and
configurable.

24. Search and Filtering

V1 should support basic filtering.

Activities:

category
year
status
featured

Events:

status
date

News:

published date
status

Advanced full-text search is not required for initial launch.

25. Privacy

The following information must be treated as private administrative
data:

Membership applications
Contact messages
Admin notes
Administrative user information
Unpublished content

Public APIs must never expose these fields accidentally.

26. Future Member System

V1 does not require a full member database.

Future versions may introduce:

MemberProfile
Ward
VolunteerProfile
Attendance
EventParticipation
Certificate
Notification

These should be added later without unnecessarily changing the V1
models.

27. AI Coding Rules for Database

Copilot and Codex must follow this document when creating Django models.

Rules:

Do not invent additional models unless required.
Do not rename models without approval.
Do not change relationships without approval.
Use Django ORM conventions.
Add appropriate database constraints.
Add indexes only where justified.
Generate migrations after model changes.
Never manually modify migration history unnecessarily.
Add model validation where appropriate.
Do not expose private fields through public serializers.
Add tests for important model behavior.
Do not add a new third-party database technology.