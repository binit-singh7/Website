# Alliance Yuwa Club Website
## Requirements Specification — V1

**Organization:** Alliance Yuwa Club  
**Former/previous identity:** Shanti Yuwa Club  
**Location:** Biratnagar, Nepal  
**Website:** https://allianceyuwaclub.org.np

---

## 1. Project Overview

Alliance Yuwa Club is a youth and social welfare organization based in
Biratnagar, Nepal.

The organization works to empower local youth and serve the community
through social service, leadership development, civic awareness, sports,
cultural activities, environmental initiatives, and collaboration with
local authorities and community organizations.

The website will serve as the official digital presence of Alliance Yuwa
Club and will provide reliable information about the organization, its
activities, events, leadership, membership, and contact information.

The organization has approximately six years of activity history and has
conducted more than 100 programs and activities.

---

## 2. Project Goals

The V1 website must:

1. Present Alliance Yuwa Club professionally.
2. Explain the organization's vision, mission, objectives, and activities.
3. Showcase the club's history and community work.
4. Provide an archive of past activities and programs.
5. Display upcoming and past events.
6. Present the executive committee and organizational team.
7. Allow interested youth to submit membership applications.
8. Allow visitors to contact the organization.
9. Allow authorized staff to manage website content.
10. Be responsive on mobile, tablet, and desktop devices.
11. Be suitable for production deployment on
    allianceyuwaclub.org.np.
12. Provide a foundation for future member-management features.

---

## 3. Target Users

### 3.1 General Visitors

People who want to learn about Alliance Yuwa Club.

They should be able to:

- Read about the organization.
- View activities.
- View events.
- Read news and updates.
- View the executive committee.
- Contact the organization.
- Apply for membership.

### 3.2 Youth / Prospective Members

Local youth interested in participating in the organization.

They should be able to:

- Learn about membership.
- Understand eligibility and expectations.
- Submit a membership application.
- Contact the organization.

### 3.3 Organization Staff / Committee

Authorized club representatives responsible for managing website content.

They should be able to:

- Add and edit activities.
- Add and edit events.
- Publish news and updates.
- Manage team information.
- Review membership applications.
- View contact messages.
- Manage gallery content.

---

## 4. V1 Public Pages

### 4.1 Home

The homepage should include:

- Organization name and logo.
- Core motto:
  "Unity, Leadership, and Service"
- Short introduction.
- Main focus areas.
- Featured activities.
- Impact/statistics section.
- Upcoming events.
- Latest news/updates.
- Membership call-to-action.
- Contact/social links.
- Footer.

---

### 4.2 About Us

The About page should contain:

- Who We Are
- Organization history
- Vision
- Mission
- Objectives
- Core values
- Organizational structure
- Relationship/history involving the previous Shanti Yuwa Club
  identity where officially appropriate

Legal/registration information must only be published after verification
against official organizational records.

---

### 4.3 Activities & Programs

The activities page is a central feature of the website.

It must support:

- Activity listing.
- Activity categories.
- Activity detail pages.
- Date-based organization.
- Year filtering.
- Category filtering.
- Featured activities.

Initial activity categories:

- Community Service
- Environment
- Youth & Leadership
- Sports
- Culture
- Awareness
- Health
- Other

The system must be capable of storing 100+ historical activities and
additional future activities.

---

### 4.4 Events

The events page must support:

- Upcoming events.
- Past events.
- Event details.
- Event date.
- Location.
- Description.
- Registration/information where applicable.

---

### 4.5 News & Updates

The news section will be used for:

- Official announcements.
- Activity reports.
- Organizational updates.
- Public notices.
- Achievements.

Each news item should support:

- Title
- Slug
- Content
- Publication date
- Author
- Featured image
- Publication status

---

### 4.6 Team

The team page should display:

- Executive committee members.
- Position/role.
- Name.
- Profile/photo where available.
- Short biography where appropriate.

The exact organizational hierarchy will be based on official club
information.

---

### 4.7 Membership

The membership page must explain:

- Why join Alliance Yuwa Club.
- Membership eligibility.
- Areas of participation.
- General expectations.
- Membership application process.

The initial membership system will use an application form.

V1 does not require a full member login system.

---

### 4.8 Contact

The contact page should provide:

- Organization address.
- Phone number.
- Email.
- Social media links.
- Map/location.
- Contact form.

---

### 4.9 Gallery

A gallery system will exist in V1 architecture.

However, photo organization and bulk historical photo migration are
not launch-critical tasks.

The gallery must be designed so that photos can be added later without
changing the architecture.

---

## 5. Recent Featured Activities

The following activities should initially be represented on the site:

### International Youth Day Border Cleanliness & Awareness Drive

Date:
August 12, 2026

Location:
Biratnagar–Jogbani (Rani) border area

The activity involved community cleanup and plastics collection,
with participation/coordination involving local volunteers, Nepal
Police, and Metropolitan Waste Management.

---

### First General Convention / Adhibheshana

Date:
August 15, 2026

Purpose:
Internal election and executive committee formation to structure
club leadership and formalize core member roles.

---

### Women's Sports and Cultural Festival 2083

Date:
June 2026

Purpose:
Community sports and cultural activities promoting youth engagement
and cultural preservation.

---

## 6. Historical Activities

Alliance Yuwa Club / its previous Shanti Yuwa Club identity has a
history of approximately six years and more than 100 programs.

V1 must therefore use a database-driven activity archive rather than
hardcoded event content.

Historical activities can be added gradually after launch.

---

## 7. Membership Application

The V1 membership form should collect only information necessary for
membership processing.

Initial fields:

- Full name
- Date of birth
- Phone number
- Email
- Address
- Ward
- Occupation
- Education
- Areas of interest
- Reason for joining

Application statuses:

- Pending
- Approved
- Rejected

The application must be visible to authorized administrators.

---

## 8. Contact Form

The contact form should support:

- Name
- Email
- Phone (optional)
- Subject
- Message

Messages should be stored securely and visible to authorized staff.

---

## 9. Content Management

Authorized staff must be able to manage:

- Activities
- Events
- News
- Team members
- Membership applications
- Contact messages
- Gallery albums/images
- Announcements

Django Admin will be used for V1 content management.

A custom React administration dashboard is planned for a future version.

---

## 10. Authentication and Authorization

Public visitors do not need an account.

Administrative operations must require authentication.

The system should support role-based permissions in preparation for
future staff roles.

Potential future roles include:

- Super Administrator
- Executive Administrator
- Content Manager
- Membership Manager

---

## 11. Responsive Design

The website must work correctly on:

- Mobile phones
- Tablets
- Laptops
- Desktop monitors

The design should be mobile-first.

---

## 12. Performance

The website should:

- Load quickly.
- Optimize images when possible.
- Avoid unnecessary JavaScript.
- Use pagination for large lists.
- Avoid loading all 100+ activities on one page.
- Use lazy loading where appropriate.

---

## 13. SEO

V1 should include basic SEO:

- Descriptive page titles.
- Meta descriptions.
- Semantic HTML.
- Clean URLs/slugs.
- Open Graph metadata.
- Sitemap.
- Robots.txt.
- Descriptive image alt text.

---

## 14. Security Requirements

The system must:

- Keep secret keys outside source control.
- Use environment variables for production secrets.
- Protect admin endpoints.
- Validate incoming form data.
- Use Django CSRF protection where applicable.
- Configure CORS explicitly.
- Avoid exposing sensitive administrative information.
- Use HTTPS in production.
- Never commit passwords, API keys, or database credentials.

---

## 15. V1 Out of Scope

The following are intentionally excluded from V1:

- Member-to-member chat.
- Real-time ward coordination.
- Mobile application.
- Online payment processing.
- Advanced volunteer scheduling.
- Certificate generation.
- Full member portal.
- Complex analytics.
- AI chatbot.
- Custom React admin dashboard.

These may be considered for V2/V3.

---

## 16. Future Expansion

The architecture should allow future development of:

- Member accounts.
- Member profiles.
- Ward-based member groups.
- Volunteer management.
- Event participation.
- Attendance.
- Digital certificates.
- Notifications.
- Internal announcements.
- Member dashboard.
- Advanced organization management.