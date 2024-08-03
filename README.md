# MENTORING SYSTEM

## ABOUT

This system will serve as a centralized platform for mentors, mentees to effectively communicate, track progress, and generate insightful reports. This is mainly developed for educational institutions.

## TECH STACK

- Python
- Django
- HTML
- CSS
- Files: Json, csv

## DESIGN AND DEVELOPMENT

The Mentoring System is designed using Python programming language based on the OOPS concept along with using Data Structures like Linked lists, Linked stacks, Dynamic stacks, Lists and Dictionaries. 

It has two main parts:

1. Mentor part
   - Profile
   - Mentorship
     - List of Mentees (each mentee has the following parts when approached from mentor's login)
       - Profile
       - Self assessment
       - Goals and Challenges
       - Student Achievements
       - New Achievements
       - Previous Meeting Details
       - New Meeting
         
2. Mentee part
   - Profile
   - Mentorship
     - Self assessment
     - Goals and Challenges
     - Student Achievements
     - Previous Meeting Details
     - Meeting
     - Mentor Timetable 

## MENTOR

**1. Profile**

This page shows the profile of the mentor. 

**2. Mentorship**

This section deals with mentorship activities. A list of 10 mentees is assigned to every mentor. When the mentor clicks any of the 10 mentees, the mentee's details are shown.

- The mentee's profile is shown when 'Profile' is clicked.
- The mentor can view the Self assessment of the particular mentee when 'Self assessment' is clicked.
- The mentor can view the Goals and Challenges of the particular mentee when 'Goals and Challenges' is clicked. These can be modified only from the mentor's login and so, the mentee changes these details in the presence of the mentor only.
- The mentor can view the Previous meeting details of the particular mentee when 'Previous meeting details' is clicked.
- The new achievements of the mentee can be added by the Mentor by clicking the 'New Achievements' button.
- Under 'New Meeting', the mentor can arrange a meeting with individual mentee or with all mentees which is mailed to the parent's mail directly and the mentees will see the same in this application from their login.

## MENTEE

**1. Profile**

This page shows the entire bio data of the mentee.

**2. Mentorship**

This section deals with mentorship activities.

- The self assessment page has a set of questions to be answered by the mentee. This can be done from mentee's login by clicking the 'Self assessment' button.
- The goals and challenges page shows the goals of the mentee and the challenges faced by the mentee. This is editable only from mentor's login.
- Under 'Achievements', the achievements of the mentee are displayed.
- Under 'Previous meeting details', the entire history of the meetings will be displayed.
- Under 'Meeting', the mentee can request a personal meeting with the mentor upon which it will be mailed to the mentor automatically.
- Under 'Mentor Timetable', the mentor's timetable is displayed for mentee's reference.

## ADDITIONAL FUNCTIONALITIES:

1. Emails are sent when meetings are arranged.
2. Change Password functionality including OTP generation.

## TECH TEAM:

1. LOKESH S
2. MADHUKRISHAA N K
3. MADHUSUDHANAN
4. MALAVIKA C V
5. MANISH KUMAR N K
6. MANJU SRI S
