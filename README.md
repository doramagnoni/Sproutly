# Sproutly 🌿

**Your personal plant care companion for flourishing houseplants.**

## 🌱 Why Sproutly?

Forget messy plant care notes and missed watering schedules! Sproutly is for plant lovers who want to nurture their indoor garden effortlessly. Get organized, receive timely reminders, and see your plant friends thrive.

## ✨ Core Features

* **Plant Profiles:** Add each plant to your collection, tracking:
    * Add each plant with name, species, and light needs ☀️
    * Set custom watering schedules 💧
    * Track fertilization needs for extra happy plants 🌱
    * Upload photos to see them grow  📸
* **Actionable To-Do List:**  Never miss a crucial care task with a clear overview of upcoming watering and fertilization reminders.
* **Intuitive Interface:** Designed for plant enthusiasts of all skill levels, prioritizing ease of use and  a gentle learning curve.

## 🪴 Getting Started

**Prerequisites:**

* Python (3.8 or above)
* Django (recent version)



## ✨ UX Design Philosophy
Sproutly aims to provide a  straightforward and enjoyable experience for plant enthusiasts.  Here's how the design focuses on your needs:

Plant Management Made Easy: Adding new plants and setting up watering/fertilizing reminders is designed to be quick and intuitive.
Clear Task Overview: The to-do list provides a satisfying visual display of your plant care schedule, helping you stay on top of your plants' needs.
Focus on Well-being: A calming color palette and emphasis on successful task completion aims to make plant care a positive and rewarding part of your routine.

## 🌱 User Stories


*As a user, I want to create an account so that I can have a personalized experience.

Priority: High
Acceptance Criteria:
A signup form is available.
Users can sign up with a username, email, and password.
Validation for password complexity and matching.
Optionally, a confirmation email is sent.
Successful signup redirects to the homepage.



*As a user, I want to log in to the app so that I can access my personalized dashboard.

Priority: High
Acceptance Criteria:
A login form is available.
Users can log in with a username and password.
Error messages are displayed for incorrect credentials.
Successful login redirects to the homepage with a welcome message.


*As a user, I want to log out so that I can ensure my account is secure.

Priority: Medium
Acceptance Criteria:
A logout button is visible when the user is logged in.
Logging out redirects to the login page or homepage.
Epic 2: Plant Management


*As a user, I want to add a new plant to my collection so that I can track its care schedule.

Priority: High
Acceptance Criteria:
A form to add a plant is available.
Required fields include plant name, species, and care intervals.
The plant is added to the user’s collection upon form submission.
A success message is displayed, and the user is redirected to their plant list.


*As a user, I want to upload a photo of my plant so that I can visually track its growth.

Priority: Medium
Acceptance Criteria:
The plant creation form includes an option to upload a photo.
The uploaded image is saved and displayed on the plant's detail page.
The image must display correctly in both DEBUG=True and DEBUG=False modes.


*As a user, I want to view a list of all my plants so that I can easily manage them.

Priority: High
Acceptance Criteria:
A dashboard displays all plants associated with the user.
Each plant entry includes the name, species, and a thumbnail image (if available).
Links to each plant’s detailed view are available.


*As a user, I want to edit my plant's information so that I can update care details as needed.

Priority: Medium
Acceptance Criteria:
An edit button is available on the plant detail page.
The user can update the plant’s name, species, care intervals.
Changes are saved and reflected immediately on the plant detail page.


*As a user, I want to delete a plant from my collection so that I can remove plants I no longer own.

Priority: Medium
Acceptance Criteria:
A delete button is available on the plant detail page.
A confirmation prompt appears before deletion.
The plant is removed from the list after confirmation.


*As a user, I want to view a calendar of my plant care schedule so that I can plan my plant care routine.

Priority: Low
Acceptance Criteria:
A form or button to share updates (text and images) with the community is available.
The update appears in a communal feed visible to all users.
Other users can like or comment on shared updates.
As a user, I want to view a communal feed of plant updates so that I can see what other users are doing.


*Sprint Planning

Sprint 1: Foundation & Authentication
Implement user signup, login, and logout.
Set up basic navigation and homepage.

Sprint 2: Basic Plant Management
Implement plant creation, listing, and detail views.
Enable image upload functionality for plants.

Sprint 3: Enhanced Plant Management 
Add edit and delete functionalities for plants.


Sprint 4: Testing & Debugging
Conduct comprehensive testing, including both unit and manual tests.
Fix any issues identified during testing, especially those related to the DEBUG=False setting.


## 🧪 Testing and Quality Assurance

To ensure Sproutly functions as intended and provides a reliable experience for plant lovers, we employ a mix of automated and manual testing strategies. 

* **Automated Tests:**


We have implemented a series of automated tests using Django's built-in testing framework. These tests help verify that the core functionalities of the application work as expected, particularly for creating and managing plants, as well as user signup.

. Setting Up the Testing Environment
Before running the tests, ensure that you have Django and the necessary dependencies installed. You can run the tests using the Django test command: python manage.py test


This command will automatically create a test database, execute the tests, and then destroy the test database.

2. Plant Model Tests
The PlantModelTest class is designed to verify the functionality related to the Plant model. Specifically, it tests the following:

Test Plant Creation:

-This test ensures that a Plant instance can be successfully created and saved to the database.
-The test checks that the species and watering_interval fields are correctly assigned and retrieved from the database.

3. User Signup Tests
The SignupTestCase class is focused on testing the user signup process:

Test Successful Signup:

-This test simulates a user signing up through the signup form.
-It verifies that a user can sign up with a valid username, email, and password, and that the application redirects the user to the appropriate page upon successful signup.
-The test checks the response status code (302 for a successful redirect) and verifies that the new user is correctly saved in the database.


If all the tests pass, you will see an output indicating that all tests were successful:

Ran X tests in Y.YYYs

OK


* **Manual Testing:**

We thoroughly test SproutList across different browsers and devices to ensure a smooth user experience for everyone.
The following section details the manual testing process used to verify the functionality of key elements within the application. Each test case is designed to be specific, objective, and easily replicable, ensuring consistent results across different testing scenarios.

1. Navigation Links
Test Case: Navigation Bar Links

Expected: When a user clicks on the "Home" link in the navigation bar, they should be redirected to the homepage (/). The same applies to other navigation links like "About," "Contact," etc.

Testing: Manually clicked on the "Home" link in the navigation bar.

Result: The "Home" link redirected the user to the homepage as expected.

Fix: N/A – The feature worked as expected.

2. Signup Form
Test Case: User Signup Process

Expected: When a user fills out the signup form with valid credentials (username, email, password), they should be successfully registered and redirected to the homepage.

Testing: Tested the signup form by entering a valid username (testuser), email (test@example.com), and matching passwords (testpassword123).

Result: The user was successfully registered and redirected to the homepage. The new user appeared in the admin panel's user list.

Fix: N/A – The feature worked as expected.

Test Case: Signup with Invalid Password

Expected: If the passwords entered in the signup form do not match, the user should receive an error message, and the form should not be submitted.

Testing: Entered a valid username and email but mismatched passwords in the signup form.

Result: The form displayed an error message stating that the passwords did not match, and the form was not submitted.

Fix: N/A – The feature worked as expected.

3. Plant Creation Form
Test Case: Creating a New Plant Entry

Expected: When a user fills out the plant creation form with valid data, the plant should be added to the user's list of plants.

Testing: Entered valid data into the plant creation form (e.g., "Golden Pothos" for name, "Epipremnum aureum" for species) and submitted the form.

Result: The plant was successfully added to the database and displayed on the user's plant list.

Fix: N/A – The feature worked as expected.

Test Case: Invalid Data in Plant Creation Form

Expected: If the user submits the plant creation form without filling in all required fields, they should see an error message, and the form should not be submitted.

Testing: Attempted to submit the plant creation form without entering a name for the plant.

Result: An error message appeared, stating that the name field is required, and the form was not submitted.

Fix: N/A – The feature worked as expected.

4. Login Process
Test Case: User Login with Correct Credentials

Expected: When a user enters correct credentials, they should be logged in and redirected to the homepage with a welcome message.
Testing: Logged in with valid credentials (testuser and testpassword).
Result: The user was successfully logged in and redirected to the homepage with a welcome message.
Fix: N/A – The feature worked as expected.
Test Case: User Login with Incorrect Credentials

Expected: When a user enters incorrect credentials, they should receive an error message, and the login should fail.

Testing: Entered an incorrect password during login.

Result: The login form displayed an error message, and the login attempt failed.
Fix: N/A – The feature worked as expected.

**Test Results:** Our current tests pass successfully, giving us confidence in the stability of Sproutly's core features. We are committed to expanding our test coverage as we add new functionalities.




## 🗄️ Deployment Write-up

Sproutly is live on Heroku! Try it out here: https://sproutly-30d053e33e11.herokuapp.com/

**Step-by-Step:**
To deploy Sproutly on Heroku, follow these steps:

Prerequisites:
Before you start the deployment process, ensure you have the following:

*A Heroku account (sign up for a free tier if needed)
*Git installed on your local machine
The complete Sproutly codebase, cloned to your local environment.


1. Configuration Files:

To deploy Sproutly successfully to Heroku, you need several configuration files:

*Procfile: This file instructs Heroku on how to start your application.

Create a file named Procfile at the root of your Sproutly project (where manage.py is located).
Add the following line:

web: gunicorn App.wsgi --log-file -


*requirements.txt: This file outlines the Python dependencies.

In your project's root directory, execute the following command:

pip freeze > requirements.txt


2. Ensure Static and Media Files Handling:

Make sure you have the necessary configurations for handling static and media files. In Heroku, you might need additional configurations or packages like django-storages for production environments.

*Deployment to Heroku:
1. Initialize a Git Repository:

Navigate to your Sproutly project's root directory.
If you haven’t already initialized a Git repository, do so by running:

git init

2. Connect to Heroku:

Create a new app on your Heroku account.

3. Push to Heroku:

Ensure all code changes are committed to your local Git repository.
Deploy your application to Heroku:

git add .
git commit -m "Deploying to Heroku"
git push heroku master


4.Run Migrations and Collect Static Files:

After deploying, you need to run database migrations and collect static files:


heroku run python manage.py migrate
heroku run python manage.py collectstatic --noinput

5. Access Your Deployed App:

Once the deployment is complete, you can access your Sproutly application through the URL provided by Heroku.


```

## 💚 Future Goals

* **Customization:** Personalized care guides based on specific plant species.
* **Progress Tracking:** Plant photo gallery to observe their growth over time. 
* **Community Features:** Plant advice forum or ability to share collections with fellow plant parents.



## 🙏 Acknowledgments

I want to express my sincere gratitude to the following individuals and resources for their invaluable contributions and support in the making of this project:

ALl the tutors from Code Institude: who helped me extensively to fix numerous problems with my code and supported me very patiently throughout all the stages of the creation of this portfolio. Especially to Rebecca, who always brought a smile to my face

[Online Resource/Tutorial]: I used extensively the walkthrough project provided by Code Institute.

I extend my gratitude to the contributors of Wikimedia Commons for their valuable contributions. Additionally, all web page content, design, and functionality were created by the author of this project.

For more information on image licenses and usage, please refer to the respective Wikimedia Commons pages linked to the images used.