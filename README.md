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

## ☁️ Deployment
Sproutly is live on Heroku! Try it out here: https://sproutly-30d053e33e11.herokuapp.com/

**Step-by-Step:**

1. Clone this repository: `git clone https://github.com/yourusername/SproutList.git`
2. *(Optional,  Recommended)* Use a virtual environment and activate it.
3. Install project dependencies: `pip install -r requirements.txt`
4. Prepare the database: 
   * `python manage.py makemigrations`
   * `python manage.py migrate`
5.  Start the SproutList server: `python manage.py runserver`

_Open `http://127.0.0.1:8000/` in your web browser to explore your digital garden!_

## ✨ UX Design Philosophy
Sproutly aims to provide a  straightforward and enjoyable experience for plant enthusiasts.  Here's how the design focuses on your needs:

Plant Management Made Easy: Adding new plants and setting up watering/fertilizing reminders is designed to be quick and intuitive.
Clear Task Overview: The to-do list provides a satisfying visual display of your plant care schedule, helping you stay on top of your plants' needs.
Focus on Well-being: A calming color palette and emphasis on successful task completion aims to make plant care a positive and rewarding part of your routine.

## 🌱 User Stories

* **As a busy plant enthusiast,** I want to easily track my watering and fertilization schedule so my plants stay happy and healthy.
* **As a forgetful plant newbie,** I need clear reminders about when and how to fertilize my plants. 
* **As a proud plant parent,**  I want to see how my plants change over time, through photos stored with their profiles.  

## 🧪 Testing and Quality Assurance

To ensure Sproutly functions as intended and provides a reliable experience for plant lovers, we employ a mix of automated and manual testing strategies.

* **Automated Tests:** Our test suite covers core functionalities such as plant profile creation, to-do list generation, and successful user signup. This helps us catch potential errors early in the development process.
* **Manual Testing:** We thoroughly test SproutList across different browsers and devices to ensure a smooth user experience for everyone.

**Test Results:** Our current tests pass successfully, giving us confidence in the stability of Sproutly's core features. We are committed to expanding our test coverage as we add new functionalities.

## Development Status

The following features are currently under active development:

* **To-Do List:** Basic task creation functionality is implemented. Due date tracking and reminder features are planned for future updates. 

## Development Challenges

* **Challenge: Incorrect Display of To-Do Tasks Based on Due Dates**

   **Description:** The To-Do list feature within my Sproutly application encountered a problem where tasks were failing to display entirely. This severely undermined the core functionality of the To-Do list as a plant care reminder system.

   **Troubleshooting:** To identify the root of the issue, I followed a systematic debugging proces which is described in details - [label](< development_challenges.txt>)

```

## 💚 Future Goals

* **Customization:** Personalized care guides based on specific plant species.
* **Progress Tracking:** Plant photo gallery to observe their growth over time. 
* **Community Features:** Plant advice forum or ability to share collections with fellow plant parents.

## 🤝 Contributing

We welcome contributions to Sproutly!  Help us build the best plant care tool possible. For guidelines, please see [insert link if you have a CONTRIBUTING.md file or a section]

I would like to express my gratitude to my mentor Adegbenga Adeye who helped me extensively to fix numerous problems with my code and supported me very patiently throughout all the stages of the creation of this portfolio.