# `pages` Folder

## Student Pages 
These pages in the student profile simulate the view of a single student. It allows them to 
interact with their profile, write and edit the student's reviews, and view others' reviews.

### Student_Home.py
This is a general navigation page for the student. Featured reviews are displayed on the right side.
It includes a link to all reviews and student profile. 

### Student_Profile.py
This page includes the students profile information, including their general info, skills, and experiences.
Buttons below each information box allows for editing and deletion of the information. 

### Student_All_Reviews.py
This page displays all of the reviews written on the platform allowing a student to scroll through them. 
A link to the students personal reviews page is also present.

### Student_My_Reviews.py
This page displays a specific student's written reviews. It allows the student to add another review,
and edit and delete published reviews.

## Co-op Advisor Pages
These pages in the advisor profile simulate the view of a Co-op advisor. It allows them to view aggregated 
data for each company, recommend co-ops to their students, and view an editable list of their students. 

### Advisor_Data.py
This page displays a graph of the averaged overall score of x number of companies. Advisors can add any number 
of companies to the graph to compare them with overall scores of other companies. These scores are the average 
company score of many categories such as culture, compensation, satisfaction, etc.

### Advisor_Rec
This page allows advisors to recommend any co-ops to any of their students. An advisor can choose from a dropdown menu 
of their students and choose from a dropdown menu of the companies and then recommend a role.

### Advisor_Students
This page displays all of the students and all of their information that is associated with the advisor. It also allows 
for the deletion of a student.

## Company Pages
The company profile simulates a specific company and allows it to view and edit its company profile, manage its
co-op postings, and add new co-ops. 

### Company_Profile.py
This page displays the company profile information and has a button to edit the informaton.

### Company_Job_Postings.py
This page displays all of the co-op postings for the company and allows you to view the reviews for each co-op.

### Job_Posting
This page shows all of the reviews for a specific positng. The job data is wrutten and the average scores are graphically
displayed. 

### Add_Job.py
This is a form to add a new co-op position for the company. 

## Admin Pages
This is the page for a system admin to flag reviews from the list off all reviews then either approve or deny the reviews,
keeping or removing them in the database. The log of flagging and approving/denying also appears. 

### Admin_Flag_Review.py
This page displays all of the flagged reviews with the infomration and buttons to approve or deny the review from staying
on the platform.

### Admin_Review_Check.py
This is all of the reviews on the website and the admin has the option to send any of them to the flagged page. 

### Admin_Activity.py
Shows all of the activity including the flagging of reviews, the incorrect flagging, as well as if the reviews are 
approved or denied. 