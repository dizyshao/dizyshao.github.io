- 123CONTACTFORM -

LEAP gave us the following specifications for two order forms through which donors could provide basic information about themselves
before buying either full-price Dinner & Reception Tickets for the fundraiser event, or a cheaper Reception Only ticket. One order form
would be for regular donors, the other would be for sponsors, who should not be charged for their tickets.

    - REGULAR DONOR FORM -

    The following elements were created as part of the form:

    - Text fields asking for Name, Email, Phone, and Address.
    - A multiple choice question asking whether a donor would purchase Dinner & Reception tickets or Reception Only tickets.
    - A heading text that instructs a user to choose 3 different dinner choices.
    - Three drop down menus asking the user to select 3 different choices/preferences for a Dinner reception to attend.
    - A text field asking for the number of tickets to be bought
    - A text field asking for the salutation and full name of the user filling out the form.
    - A multiple choice question asking whether the user wants to add another guest, followed by an additional field for a salutation and name to be given (this is repeated four times).
    - A text field detailing how to purchase additional tickets outside the form.
    - A multiple choice question asking whether or not a user has dietary restrictions.
    - A text field for the user to elaborate on dietary restrictions.
    - Three invisible text fields:
        - Regular dinner & reception ticket price (default value 150)
        - Reception only ticket price (default value 50)
        - Donation Base value (default value 1)
    - A multiple choice question asking whether the user would like to make an additional donation.
    - A text field to specify an amount of money to donate.
    - A purchase button, and a 'Clear form and start from scratch' button.

    - SPONSOR FORM -

    The form had all the previous elements, with the addition of:

    - A textfield for the user to specify which sponsor organization they represent.
    - Three invisible text fields:
        - Regular dinner & reception ticket price (default value 0)
        - Reception only ticket price (default value 0)
        - Donation Base value (default value 1)

    See Figure 1 in the Supplements .doc or .pdf file for details.

    - FIELD RULES/PROGRAMMING -

    The guiding principle of programming this form was to prevent clutter, and to only show the information necessary to a user after
    they've provided certain preqrequisite information. In some ways, the form can be followed as a flowchat. The first major question
    is whether the user will be attending a Dinner & Reception, or just a reception. In two separate rules, it is apparent that if the
    user checks the Dinner & Reception box, it will prompt instructions and drop down menus to select dinners, as well as a text field
    for the number of dinner tickets, and a question for dietary restrictions. If the user checks the box for Reception Only, a text
    field asking for the number of reception tickets will be the only thing that appears. There are some elements that should appear
    regardless of what type of ticket the user purchases; this was solved by having a rule with two conditions joined by 'OR'. If either
    the Dinner & Reception or Reception Only box is checked, the form will be prompted to ask for the salutation/name of the user, a
    multiple choice question asking whether they'd like to provide details of another guest/plus-one, and a multiple choice question
    asking whether they'd like to make an additional donation.

    For dietary restrictions, the text field asking for elaboration only appears if the user answered 'Yes' to the preceding question
    about whether they have dietary restrictions. Similarly, the text field asking the user to specify a donation amount will only
    appear if they check 'Yes' on the preceding question asking whether or not they want to donate. The mechanism of providing the
    information of additional guests also works in this way, though with greater complexity. If the multiple choice question of "Add
    another guest" is answered with 'Yes', the form is programmed to show an additional text field to provide a salutation/name, and
    another "Add another guest" question. This way, the user has control over how many text fields they need depending on how many other
    guests they are buying tickets for. 123contactform doesn't allow a inherently iterative process for this, so it was necessary to
    create different rules to account for every time the user wanted to add a text field. As a result, there is a maximum of five text
    fields that are manually programmed to appear. When the last text field appears, there is an additional heading text that informs
    the user that they can purchase additional tickets through a provided phone number and email.

    - PAYMENT -

    LEAP's payment processor is Stripe, which was pre-linked to their 123contactform account. In the regular donor form, we created three
    invisible elements, each one corresponding to the monetary value of an "item" for sale. Reception & Dinner tickets are $150, while
    Reception only tickets are $50. We set the donation value to be $1; 123contactform doesn't have an option to simply donate money,
    so instead we approached this obstacle by thinking about a donation "item" with a fixed price of $1. When the user is prompted to
    specify how much they want to donate, they are actually inputting the quantity, or the number of donation items they want to purchase.
    This emulates an effective donation function in the form, with the only limitation being the inability to donate a value that is not
    an integer.

    The sponsor form uses this same mechanism, except the prices for both tickets are set to zero. This could have been made simpler
    by only registering the donation item. However, keeping in mind that this form/programming may be used in future years, LEAP may
    decide later on to only give a discount to sponsors, rather than giving them free tickets. Therefore, we decided to still register
    the tickets as items, even though they have a price of $0.

    - AUTO-RESPONDER -

    As per LEAP's requests, the confirmation email included details of the user's name, what they purchased, how much they donated (if
    anything), and what dinners they selected (if applicable). The actual template can be visible in this project's supplementary materials.
    It was necessary to create two separate auto-responders for the regular donor form and the sponsor form. When creating a template,
    the variables available in the drop-down list are unique to that specific form. When you open and select that autoresponder in another
    form, it may not work properly because that form does not necessarily have all the variables used in the original form.

    - AREAS FOR IMPROVEMENT -

    One specification that we ultimately could not meet during this project time frame involved the dinner selection. We attempted to
    program the form so that the user could not submit/proceed unless all the dinners selected were different. However, we quickly realized
    that due to the narrow structure of the programming format, it was not feasible. 123contactform only allows conditional statements
    and comparisons to be made between user input and creator input, not user input and other user input. In other programming languages,
    we would have been able to compare a variable containing the user's first choice with the user's second choice, but this is not
    possible in 123contactform. This demonstrates a consistent dilemma in computer science: some languages may have lots of built in
    functionality to be writer-friendly, but a drawback will often be the limit in flexibility with unique tasks such as those in this
    project.

EVALUATION FORM WEBSITE

The main 'application.py' file imports several different libraries and functions. Among some other important functions is CS50's configuration
of the SQL module that allows us to use review.db, which is where the evaluation data is stored. Within the 'helpers.py' file are the
'login_required' function and the 'apology' function; the 'login-required function' allows us to make pages visible only to registered
and logged in users, while the apology function makes use of the cs50's error format to return grumpy cat in case of error.

    - General notes on design/Specifications -

    LEAP asked us to convert their complete evaluation form into a digital format. This involves the following specifications:
    - A section for details about the evaluated employee's name, title, department, and how long they've been in the position.
    - A section to specify department goals.
    - A section to detail 2 goals of the past year, and evaluate whether those goals were met, alongside a section to propose the coming year's goals.
    - A section for 'Performance Categories' ratings such as work quality, job knowledge, organization, analysis, etc.
    - A section for 'Non task-specific performance' ratings
    - A section for overall comments

    We decided to implement this form through a number of consecutive page (rather than one humongous HTML) to be more interactive and
    intimidating to the eyes.

    - application.py -

    In general, our strategy for programming this website was to store inputted information in global variables. We wanted to avoid a
    situation where a user would fill out the pages and then stop for some reason; this would be disastrous in the SQL tables as some
    would be filled, and some would be left unfilled after the session. We decided to store all the information as the user enters it,
    and only insert it into the tables at the very end of the form when it is submitted. The user is warned (using flash messages) at
    the beginning of the form that they must complete it in one sitting, as there is no built-in save function. However, our design
    at least prevents incomplete submissions from endangering the structure of the SQL tables.

    We also implemented several apology messages to make sure that the user registers correctly, accounting for empty text fields, lack
    of password matching, or attempting to use an existing username.

    - SQL -

    Within review.db, we have 9 tables total:
    - department
    - evaluation
    - info_form
    - part1
    - part2a
    - part2b
    - part3
    - part4
    - reg_users

    Within each of these tables, we use an integer primary key, and have a field for every question asked on the corresponding HTML
    page.

    - HTML -

    In general, the HTML was structured in a way that was meant to be easily readible and reasonably-spaced. We paid special attention
    to making text boxes appropriate sizes; this way, open-ended questions can be read while they're being typed (as opposed to the
    standard size of an HTML text field). Our tables include shading in alternate rows for ease of reading, with a pleasant-colored
    bootstrap theme taken from https://bootswatch.com/ (the specific template can be seen in the layout.html).