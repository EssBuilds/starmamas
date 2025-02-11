# STAR MAMAS

[View Live Site](https://starmamas-e6bdaca50ef1.herokuapp.com/#)

## Introduction to Star Mamas

Welcome to Star Mamas, a comprehensive family task management solution designed to transform how busy families organize their daily lives. This documentation provides a detailed overview of the project's development, features, and implementation.

### Executive Summary

Star Mamas addresses the growing need for family-oriented task management solutions in our increasingly busy world. By combining intuitive design with powerful features, it helps families stay organized while promoting responsibility and collaboration.

### Project Vision Statement

"To empower families through intuitive task management, fostering responsibility and connection in our digital age."

[View Live Site](https://family-task-manager.herokuapp.com)

## Introduction

Welcome to Star Mama, a comprehensive family task management solution designed to transform how busy families and their Star Mamas organize their daily lives. Star Mama addresses the growing need for a family-oriented task management solution that helps their captain families stay organized while promoting responsibility and collaboration, all within an intuitive and visually appealing interface.

This application is built using Django, Bootstrap, JavaScript, and CSS, with PostgreSQL for the database. It's designed to be responsive and easy to use, catering specifically to the needs of working mothers.

Here's a sneak peek at Star Mama's responsiveness:

Responsive Design Example *[Replace with your actual image]*

## Contents

1.  [UX Design: User-Centered Approach](#ux-design-user-centered-approach)
    *   [User Stories](#user-stories)
    *   [Strategy & Scope](#strategy--scope)
    *   [Structural Skeleton](#structural-skeleton)
    *   [Wireframes & Mockups](#wireframes--mockups)
        *   [Initial Sketches](#initial-sketches)
        *   [Digital Wireframes](#digital-wireframes)
        *   [Final Prototypes](#final-prototypes)
    *   [Design Journey](#design-journey)

2.  [Design](#design)
    *   [Typography](#typography)
    *   [Color Scheme](#color-scheme)
    *   [Imagery](#imagery)

3.  [Website Features](#website-features)
    *   [Tablet View](#tablet-view)
    *   [Mobile View](#mobile-view)

4.  [Future Features](#future-features)

5.  [Technologies Used](#technologies-used)
    *   [Languages](#languages)
    *   [Frameworks](#frameworks)
    *   [Libraries](#libraries)

6.  [Agile Development](#agile-development)
    *   [Project Board](#project-board)
    *   [Sprint Progress](#sprint-progress)
    *   [User Story Testing](#user-story-testing)

7.  [Testing](#testing)
    *   [Automated Testing](#automated-testing)
    *   [Manual Testing](#manual-testing)
    *   [Bugs and Resolutions](#bugs-and-resolutions)
    *   [Validation Testing](#validation-testing)

8.  [Deployment](#deployment)
    *   [Step-by-Step Deployment to Heroku](#step-by-step-deployment-to-heroku)
    *   [Local Development Setup](#local-development-setup)

9.  [Credits](#credits)

## UX Design: User-Centered Approach

Star Mama's design process was deeply rooted in understanding the needs and pain points of busy working mothers. The following sections outline the UX process.

### User Stories

We began by crafting user stories to represent the goals and needs of our target users:

*   As a working mother, I want to quickly add tasks so that I don't forget important things.
*   As a working mother, I want to assign tasks to my children so that they can take responsibility.
*   As a working mother, I want to track the progress of tasks so that I can ensure everything is on schedule.
*   As a working mother, I want to be able to access the app on my phone so I can manage tasks on the go.

### Strategy & Scope

The strategy was to create a simple, intuitive task management app focused on the core needs of busy mothers: task creation, assignment, and progress tracking.

**Scope:**

*   User authentication (registration/login)
*   Task management (create, read, update, delete)
*   Child profile management
*   Task assignment to children
*   Progress tracking
*   Responsive design for mobile and tablet

### Structural Skeleton

The information architecture was designed to ensure easy navigation and quick access to essential features:

```
Star Mama
├── Dashboard
│   ├── Task Overview
│   ├── Quick Actions
│   └── Notifications
├── Tasks
│   ├── All Tasks
│   ├── My Tasks
│   └── Children's Tasks
├── Children
│   ├── Profiles
│   └── Progress
├── Settings
│   ├── Account
│   ├── Preferences
│   └── Notifications
└── Help
    ├── Guides
    ├── FAQs
    └── Support
```

### Wireframes & Mockups

#### Initial Sketches

Initial Sketches

*   Hand-drawn concept sketches to explore different layout ideas.
*   Focused on ease of use and quick task entry.

#### Digital Wireframes

Miro Board

*   Created using Miro for collaborative design.
*   Detailed layouts for mobile and desktop, showing component placement and user flows.

#### Final Prototypes

Balsamiq Designs

*   Refined in Balsamiq for interactive elements and responsive behavior.
*   Included annotations for user testing and feedback.

### Design Journey

The design evolved based on user feedback and usability testing. Initial designs were simplified to reduce cognitive load and prioritize essential features. The color scheme was refined to use softer shades of orange and pink for a more welcoming feel.

## Design

The visual design was carefully crafted to appeal to our target audience while ensuring a pleasant and efficient user experience.

### Typography

*   **Headings:** Montserrat (Bold) - Clean and modern, conveying a sense of efficiency.

```css
h1, h2, h3 {
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  letter-spacing: -0.02em;
}
```

*   **Body:** Open Sans (Regular) - Easy to read and provides a friendly, approachable feel.

```css
body {
  font-family: 'Open Sans', sans-serif;
  font-weight: 400;
  letter-spacing: 0;
}
```

### Color Scheme

The color palette uses a combination of orange and pink to create a warm and inviting atmosphere.

```css
/* Brand Color System */
:root {
  --primary-orange: #FFB347;    /* Warmth, energy */
  --secondary-pink: #FF70A6;  /* Comfort, care */
  --accent-gray: #607D8B;     /* Stability, trust */
}
```

*   **Primary Orange:** Used for primary buttons and key interactive elements.
*   **Secondary Pink:** Used for accents and background elements to create a soft, feminine feel.
*   **Accent Gray:** Used for text and borders to provide contrast and readability.

### Imagery

*   Friendly and relatable images of families, children, and organized spaces.
*   Use of icons to visually represent tasks and categories.

## Website Features

TaskNest offers a range of features designed to simplify family task management:

*   **User Authentication:** Secure registration and login system.
*   **Task Management:** Create, assign, and track tasks with due dates, priorities, and categories.
*   **Child Profiles:** Manage profiles for each child, including assigned tasks and progress.
*   **Dashboard:** Overview of upcoming tasks, recent activity, and progress metrics.
*   **Notifications:** Stay informed about new tasks, due dates, and completed tasks.
*   **Responsive Design:** Seamless experience across desktop, tablet, and mobile devices.

### Tablet View

Tablet Dashboard

*   Two-column layout for efficient use of screen space.
*   Side navigation for easy access to all sections.

### Mobile View

Mobile Dashboard

*   Single-column layout for optimal readability on smaller screens.
*   Bottom navigation for quick access to key features.

## Future Features

We plan to enhance TaskNest with the following features:

*   **Team Collaboration:** Real-time updates, team chat, and task sharing.
*   **Advanced Analytics:** Progress tracking, performance metrics, and usage statistics.
*   **Integration Options:** Calendar sync, email notifications, and file attachments.
*   **Gamification:** Points, badges, and rewards for completing tasks.

## Technologies Used

### Languages

*   Python
*   JavaScript
*   HTML
*   CSS

### Frameworks

*   Django (Backend)
*   Bootstrap (Frontend)

### Libraries

*   React
*   Redux
*   PostgreSQL
*   Heroku

## Agile Development

We followed an Agile development methodology to ensure flexibility, collaboration, and continuous improvement.

### Project Board

[View Project Board](https://github.com/users/username/projects/task-nest-board)

*   Used GitHub Projects for task tracking and sprint management.
*   Columns: Backlog, Sprint Planning, In Progress, Review, Done.

Project Board Screenshot

### Sprint Progress

*   **Sprint 1:** User authentication and core task management features.
*   **Sprint 2:** Task assignment, notifications, and basic reporting.
*   **Sprint 3:** Child profile management and enhanced progress tracking.

### User Story Testing

*   Used Gherkin syntax to define acceptance criteria for each user story.
*   Automated tests to ensure features meet requirements.

```gherkin
Feature: User Registration
Scenario: Successful Registration
  Given I am on the registration page
  When I enter valid credentials
  Then my account should be created
  And I should be redirected to the dashboard
  And I should see a welcome notification
```

## Testing

### Automated Testing

*   **Unit Tests:** Django's testing framework was used to verify individual components.

```python
class Star Mama(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='test123'
        )

    def test_task_creation(self):
        task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            due_date=timezone.now(),
            created_by=self.user
        )
        self.assertEqual(task.title, 'Test Task')
        self.assertFalse(task.completed)
```

*   **Integration Tests:** Ensured different parts of the app work together correctly.

```python
class StarFlowTests(TestCase):
    def test_task_workflow(self):
        # Create task
        response = self.client.post('/tasks/create/', {
            'title': 'Integration Test Task',
            'due_date': '2024-03-01'
        })
        self.assertEqual(response.status_code, 201)
        task_id = response.json()['id']
```

### Manual Testing

*   Feature testing table:
    | Feature           | Expected Outcome                                  | Testing Performed                  | Result             | Pass/Fail |
    | :---------------- | :------------------------------------------------ | :--------------------------------- | :----------------- | :-------- |
    | User Registration | Account created, email verification sent          | Created test account               | Email received     | Pass      |
    | Task Creation     | Task appears in list with correct details        | Created multiple tasks             | Tasks displayed    | Pass      |
    | Edit Task         | Task details update in database                   | Modified existing task             | Changes saved      | Pass      |
    | Delete Task       | Task removed from database                        | Deleted test task                  | Task removed       | Pass      |
    | Child Profile     | Profile created with correct permissions        | Added child profile                | Profile active     | Pass      |
*   Browser testing matrix:

| Browser | Version | Desktop | Mobile | Result |
| :------ | :------ | :------ | :----- | :----- |
| Chrome  | 98+     | ✓       | ✓      | Pass   |
| Firefox | 97+     | ✓       | ✓      | Pass   |
| Safari  | 15+     | ✓       | ✓      | Pass   |
| Edge    | 98+     | ✓       | ✓      | Pass   |

### Bugs and Resolutions

*   **Critical Bugs:**
    *   Database Migration Issue: Models changes breaking migrations. Reset database and clean migrations to resolve.
    *   Authentication Flow: Session persistence issues. Resolved by updated middleware configuration.
*   **Minor Bugs:**
    *   CSS Responsiveness: Mobile layout breaks. Resolved with updated media queries.
    *   Form Validation: Missing error messages. Fixed by adding Django form validation.

### Validation Testing

We performed validation testing to ensure code quality and compliance with standards.

*   **HTML Validation:**
    *   Home page: Pass
    *   Dashboard: Pass
    *   Task Forms: Pass
    *   Profile Pages: Pass
*   **CSS Validation:** Ensured that the styling adheres to CSS standards and best practices.
*   **Python PEP8 Compliance:** Verified that the Python code follows PEP8 guidelines for readability and maintainability.

## Deployment

### Step-by-Step Deployment to Heroku

1.  **Create a Heroku Account:** Sign up at [Heroku](https://www.heroku.com/).
2.  **Install the Heroku CLI:** Follow the instructions on the Heroku website to install the Heroku Command Line Interface (CLI).
3.  **Login to Heroku:** Open your terminal and run `heroku login`.
4.  **Create a New Heroku App:**

    ```bash
    heroku create task-nest
    ```
5.  **Set Up PostgreSQL:** Add the Heroku PostgreSQL add-on.

    ```bash
    heroku addons:create heroku-postgresql:hobby-dev
    ```
6.  **Set Up Redis:** Add the Heroku Redis add-on.

    ```bash
    heroku addons:create heroku-redis:hobby-dev
    ```
7.  **Configure Environment Variables:** Set the necessary environment variables for your Django app.

    ```bash
    heroku config:set \
        DJANGO_SETTINGS_MODULE=tasknest.settings.production \
        SECRET_KEY=$YOUR_DJANGO_SECRET_KEY \
        AWS_ACCESS_KEY_ID=$YOUR_AWS_ACCESS_KEY_ID \
        AWS_SECRET_ACCESS_KEY=$YOUR_AWS_SECRET_ACCESS_KEY
    ```

    Replace `$YOUR_DJANGO_SECRET_KEY`, `$YOUR_AWS_ACCESS_KEY_ID`, and `$YOUR_AWS_SECRET_ACCESS_KEY` with your actual values.

8.  **Create a `Procfile`:** Create a file named `Procfile` in the root of your project with the following content:

    ```
    web: gunicorn tasknest.wsgi:application
    worker: celery -A tasknest worker -l info
    ```

9.  **Push Code to Heroku:** Initialize a Git repository, add your files, commit, and push to Heroku.

    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git push heroku main
    ```

10. **Run Migrations:** After deploying, run the Django migrations.

    ```bash
    heroku run python manage.py migrate
    ```

11. **Create Superuser:** Create an admin user for your Django app.

    ```bash
    heroku run python manage.py createsuperuser
    ```

12. **Collect Static Files:** Collect static files to be served by Heroku.

    ```bash
    heroku run python manage.py collectstatic
    ```

13. **Open the App:**

    ```bash
    heroku open
    ```

### Local Development Setup

1.  **Prerequisites:**

    *   Python 3.9+
    *   Node.js 16+
    *   PostgreSQL 13+
    *   Redis 6+

2.  **Environment Setup:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    npm install
    ```

3.  **Environment Variables:**

    ```bash
    cp .env.example .env
    # Edit .env with your settings
    ```

4.  **Database Configuration:**

    ```python
    # settings.py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('DB_NAME'),
            'USER': env('DB_USER'),
            'PASSWORD': env('DB_PASSWORD'),
            'HOST': env('DB_HOST'),
            'PORT': env('DB_PORT', default='5432'),
        }
    }

    # Redis cache
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': env('REDIS_URL'),
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            }
        }
    }
    ```

## Credits

*   Django Documentation
*   Bootstrap Documentation
*   React Documentation
*   Heroku Dev Center
*   UX Design Feedback Group
*   Stack Overflow Community

