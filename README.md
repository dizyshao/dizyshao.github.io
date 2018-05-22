- LEAP Fall 2017 Project Background/Documentation/User Manual -

Douglas Shao and Cecily Gao

- Project Background -

Video: https://youtu.be/Hci1SLHea1I

Leadership, Education, and Athletics in Partnership (LEAP) is a 501(c)3 organization that trains New Haven college and public high school
students to work with younger children, providing a literacy-based curriculum as well as classes in the arts, computer science,
swimming, athletics, camping, cooking, and team building. Their model is specifically implemented in high poverty neighborhood with
underresourced students; this dually provides enrichment for young children while also providing work and leadership experience to
older students.

This year, the Connecticut state government failed to include LEAP in its budget for the first time in many years. As a result, LEAP
lost almost 25% of its annual funding and was forced to close one of its five New Haven sites in September. This means that more than
ever before, the organization is depending on fundraising events and donors to provide its service to New Haven youth. One of these
events is the LEAP Year Event (LYE), in which donors purchase tickets to attend dinner receptions with distinguished guests who present on
specific topics, such as the arts, recent scientific breakthroughs, and civil rights causes.

With LEAP as a client, this CS50 final project involved recreating a digital registration form for the 2018 LYE. LEAP asked that this
be accomplished using 123contactform (also called 123formbuilder), a form software that uses a logic-based language to implement certain
functionalities, making certain elements appear only under certain conditions. This project involved learning this language, which is
comprable to Scratch in its graphic-based platform for programming. The second part of this project involves the creation of an evaluation
platform through which LEAP supervisors can digitally create and access evaluations of employees. This involves the use of Python, Flask,
and HTML.

As mentioned earlier, this project falls under the Community Based Learning Track for CPSC100. This entails creating a final project
that is both rigorous in using the problem-solving skills learned throughout the semester, while still observing the values of ethical
community service. By nature of being a community-centered project, it is imperative that this project meet the actual needs of the
organization as they direct, and present these solutions in forms that will be sustainable in the long-term, whether or not the organization
continues to have the direct support of computer science students/experts.

- LEAP YEAR EVENT REGISTRATION FORM DOCUMENTATION -

The LYE registration form was accomplished using 123contactform (123formbuilder), a form software that requires the use of logical if-then
statements to create certain functions within the form itself. On the form creator's part, 123contactform presents itself uses a graphic-based
environment (much like Scratch) to create blocks of code that determine when or where parts of the form will appear.

This environment is only accessible through the 123contactform site itself. At the time of this project's conception, LEAP had already
purchased a membership for this site, hence why they asked us to use this specific platform. Once a form creator is logged into their
account, they should start by creating the elements/fields of the form. 123contactform accomplishes this with a fairly intuitive
drag-and-drop action to bring different types of elements (text fields, multiple choice questions, etc.) into the form as required or
not required elements. Once the element has been added to the form, it is necessary to give it a label or field name, which can be thought
of as its identifier. This initial stage of creating the form with all its elements will occur under the 'EDIT' tab of the site.

After the elements are in the form, the creator can then navigate to the 'Rules' link under the 'SETTINGS' tab. This is where the programming
takes place. New rules (analogous to functions in other programming languages) can be created by clicking the '+Add Rule' button. After
clicking this button, an empty if-then branch statement will appear. One must start by filling in the 'if' branch, designating which
form element will be referenced for the condition statement. For text fields, the creator will simply choose the element corresponding
to the text field. For multiple choice questions, each choice in the question is a separate element that can be chosen. 123contact form
also allows a form creator to import data from CSV files as choices. From a drop-down menu, the creator can then select a logical operator
depending on the nature of the form element being referenced. For text fields, they can use operators such as 'IS', 'IS NOT', 'CONTAINS',
'IS GREATER THAN', etc., whereas with multiple choice elements, they has access to operators such as 'IS CHECKED' or 'IS NOT CHECKED'.
Finally, the creator will provide their own input as a text string for the form element to be compared to. It is worth noting that the
form creator cannot compare a form element to another form element - this is an inherent limitation of 123contactform.

After clicking 'Continue', the 'then' branch will appear. There are two parts to a 'then' branch: (1) a form element to be acted upon,
and (2) whether that element will be shown or hidden when the 'if' condition is met.

    - EXAMPLE -
    //Consider the text fields 'First Name' and 'Last Name' which must not be empty in order to make a submit button appear.

    If [First Name] DOES NOT CONTAIN " "
        AND
        [Last Name] DOES NOT CONTAIN " "
    Then SHOW Submit Button

    //Note: In this example, notice that 123contactform supports multiple conditions separated by 'AND' or 'OR'. These can be accessed
    //by clicking the '+' symbol that appears next to the 'if' branch, before continuing to the 'then' branch.

    //Next, consider a multiple-choice question that asks whether or not someone has dietary restrictions. If they choose Yes, a text field
    //asking them to elaborate will appear.

    If [Do you have dietary restrictions...Yes] IS CHECKED
    Then SHOW [Please Elaborate: ]

    //Consider a multiple choice question asking if the user has an emergency contact they want to provide information for. If they
    //If they choose Yes, multiple elements are prompted to appear.

    If [Do you have an emergency contact...Yes] IS CHECKED
    Then SHOW [First Name], [Last Name], [Cell Phone Number]

123contactform does not technically support multiple branches within a single 'then' branch. That is, if the form creator wants a certain
condition to hide some elements and simultaneously show some elements, they will need to create separate rules. However, if the creator
wants to either show multiple elements or hide multiple elements, they may do so while programming the 'then' branch. When choosing the
form element(s) to be acted upon, one can do this by checking boxes in a drop-down list of all the elements in the form. Deleting
duplicating rules is simple; the creator can select a rule and click buttons at the top right to duplicate or delete the rule. Duplicating
a rule is useful in the event of needing to simultaneously hide some elements while showing others with a single condition.

Another major aspect of 123contactform is the ability to make monetary transactions and purchases through the platform. On the form
creator's part, this necessitates creating 'items' that can be sold through a form. The most logical method of accomplishing this is
creating text field elements that are hidden from user view, with the field's default value set as the item's price. Once the form creator
navigates to the the 'Payments' link under the 'SETTINGS' tab, they must register the item in a list of items for sale. This process
involves selecting the item from a drop-down list of all the elements in the form (this is why it was added as an invisible element),
as well as the element that corresponds to the quantity a user inputed into the form. The form creator has the option of also creating
a discount or markup on a certain item. See Figure 4.1 and 4.2 in the Supplements .doc or .pdf file.

Another functionality of 123contactform is its autoresponder function. 123contactform allows the form creator to program a
dynamic template for confirmation emails that are sent to a user once they have completed the form. This function is found by navigating
to the 'Notifications' link under the 'SETTINGS' and 'Form User (Sender)' tabs. From this page, it is necessary to specify a host email
that will appear as the sender on each confirmation email. The creator can then choose a specific autoresponder template from a drop-down
menu, or create their own by clicking the 'Customize' button. After the customization page is brought up, the creator can specify the
name of this new autoresponder, the subject line of the confirmation email, and the actual text of the email. Within this email,
123contactform allows a form creator to have the platform dynamically substitute information from the form into the email.

See Figure 2, Figure 3.1, and Figure 3.2 in the Supplements .doc or .pdf file.

    //Consider a confirmation email being sent to a user. Within the form, they inputted their name into a text field. The autoresponder
    //template would resemble thie following, much like the Jinja method of substitution:

    "Thank you for joining our event this year!

    This email is to confirm [{Name(35168309)}]'s purchase of the following items..."

The last important functionality is specifying an email (likely the form creator's) to receive the form submissions. This is done at
the 'Notifications' link under the 'SETTINGS' and 'Form Owners' tab. 123contactform supports multiple recipients for submission notifications.

For this specific project, the form itself will only be available for demonstration in person. LEAP is set to publish the link in January
when they open registration for the event. When the form is published, it will go live at this link: https://www.leapforkids.org/lye

- LEAP EMPLOYEE EVALUATION SITE DOCUMENTATION -

Currently, the evaluation website can be viewed by running it locally in the CS50 IDE, with all the files and templates found with the
application.py in the submission folder. The site will be ported to a LEAP server in the near future.

The following files should be in the 'FinalProj' folder:
    - DESIGN.md
    - README.md
    - 'perf/'
        - The 'static' folder
            - styles.css
        - The 'templates' folder
            - apology.html
            - department.html
            - employee_eval.html
            - index.html
            - info_form.html
            - layout.html
            - login.html
            - part1.html
            - part2.html
            - part3.html
            - part4.html
            - past_evals.html
            - quote.html
            - register.html
            - submitted.html
        - application.py
        - helpers.py
        - requirements.txt
        - review.db

Running the flask site should be possible by opening a terminal window to the project folder within the CS50 IDE, and then executing
"flask run" in the terminal window. NOTE: The terminal window should be ~/workspace/FinalProj/perf/

To use the evaluation site, it's necessary to first register for an account by setting up a username, password, and providing other
details as well such as name and department. After creating an account/logging in, the user is warned through a flash message that they
must complete the evaluation in one session; if they end the session before submitting, the data will not be saved and they will have
to start over. The page they have arrived at is the first page of the evaluation where they provide details on the employee being evaluated.

This brings them to the next page (/department) which asks for details regarding the current goals of the department. After submitting
this page, the user is directed through three separate pages of evaluations. The process of completing the evaluation simply involves
filling out the textfields and pressing the 'Next' button, or the 'Submit' button on the last page.

The user is also able to view the past evaluations by clicking the "Past Evaluations" link on the left. When this is clicked, it brings
the user to a page where they see a list of all the evaluations they have submitted in the past in a table. Each row has a link to view
details of that specific employee evaluation.


- CONTACT INFORMATION -

Douglas Shao (douglas.shao@yale.edu)
Cecily Gao (cecily.gao@yale.edu)
Rachel Kline Brown - Development Director of LEAP (rklinebrown@leapforkids.org)
Henry Fernandez - Executive Director of LEAP (hfernandez@leapforkids.org)

