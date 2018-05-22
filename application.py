from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///review.db")


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show Evaluation Form"""
    if request.method == "POST":
        global name
        name=request.form.get("name")
        global job
        job=request.form.get("job")
        global depart
        depart=request.form.get("department")
        global start
        start=request.form.get("start")
        global employment
        employment=request.form.get("employment")
        global education
        education=request.form.get("education")

        return render_template("department.html")
    else:
        return render_template("info_form.html")

@app.route("/department", methods=["GET", "POST"])
@login_required
def department():
    """Show Evaluation Form"""
    if request.method == "POST":
        # if request.form['submit'] == 'back':
        #     return render_template("info_form.html")
        # elif request.form['submit'] == 'forward':
        global goal
        goal=request.form.get("goal")
        return render_template("part1.html")
    else:
        return render_template("department.html")

@app.route("/part1", methods=["GET", "POST"])
@login_required
def part1():
    """Show Evaluation Form"""
    if request.method == "POST":
        # if request.form['submit'] == 'back':
        #     return render_template("department.html")
        # elif request.form['submit'] == 'forward':
        global goal1
        goal1=request.form.get("goal1")
        global goal2
        goal2=request.form.get("goal2")
        global level1
        level1=request.form.get("level1")
        global level2
        level2=request.form.get("level2")
        global area1
        area1=request.form.get("area1")
        global area2
        area2=request.form.get("area2")
        global description1
        description1=request.form.get("description1")
        global description2
        description2 =request.form.get("description2")
        global objective1
        objective1=request.form.get("objective1")
        global objective2
        objective2=request.form.get("objective2")
        global resources1
        resources1=request.form.get("resources1")
        global resources2
        resources2=request.form.get("resources2")

        return render_template("part2.html")
    else:
        return render_template("part1.html")

@app.route("/part2", methods=["GET", "POST"])
@login_required
def part2():
    """Show Evaluation Form"""
    if request.method == "POST":
        global work_quality
        work_quality=request.form.get("work_quality")
        global job_know
        job_know=request.form.get("job_know")
        global new_know
        new_know=request.form.get("new_know")
        global organization
        organization=request.form.get("organization")
        global analysis
        analysis=request.form.get("analysis")
        global resource
        resource=request.form.get("resource")
        global attendance
        attendance=request.form.get("attendance")
        global safety
        safety=request.form.get("safety")
        global dependability
        dependability=request.form.get("dependability")
        global communication
        communication=request.form.get("communication")
        global interpersonal
        interpersonal=request.form.get("interpersonal")
        global initiative
        initiative=request.form.get("initiative")

        global caring
        caring=request.form.get("caring")
        global caring_t
        caring_t=request.form.get("caring_t")
        global collab
        collab=request.form.get("collab")
        global collab_t
        collab_t=request.form.get("collab_t")
        global committed
        committed=request.form.get("committed")
        global committed_t
        committed_t=request.form.get("committed_t")
        global honest
        honest=request.form.get("honest")
        global honest_t
        honest_t=request.form.get("honest_t")
        global respectful
        respectful=request.form.get("respectful")
        global respectful_t
        respectful_t=request.form.get("respectful_t")

        return render_template("part3.html")
    else:
        return render_template("part2.html")

@app.route("/part3", methods=["GET", "POST"])
@login_required
def part3():
    """Show Evaluation Form"""
    if request.method == "POST":
        global goals
        goals=request.form.get("goals")

        return render_template("part4.html")
    else:
        return render_template("part3.html")

@app.route("/part4", methods=["GET", "POST"])
@login_required
def part4():
    """Show Evaluation Form"""
    if request.method == "POST":
        global sup_comm
        sup_comm=request.form.get("sup_comm")
        global emp_comm
        emp_comm=request.form.get("emp_comm")
        global sup_sig
        sup_sig=request.form.get("sup_sig")
        global emp_sig
        emp_sig=request.form.get("emp_sig")

        db.execute("INSERT INTO info_form (name, job, department, start, employment, education, user_id) VALUES(:name, :job, :department, :start, :employment, :education, :user_id)",
                    name=name, job=job, department=depart, start=start, employment=employment, education=education, user_id=session["user_id"])
        db.execute("INSERT INTO department (goals, user_id) VALUES(:goals, :user_id)", goals=goal, user_id=session["user_id"])
        db.execute("INSERT INTO part1 (goal1, goal2, level1, level2, area1, area2, description1, description2, objective1, objective2, resources1, resources2, user_id) VALUES(:goal1, :goal2, :level1, :level2, :area1, :area2, :description1, :description2, :objective1, :objective2, :resources1, :resources2, :user_id)",
                    goal1=goal1, goal2=goal2, level1=level1, level2=level2, area1=area1, area2=area2, description1=description1, description2=description2, objective1=objective1, objective2=objective2, resources1=resources1, resources2=resources2, user_id=session["user_id"])
        db.execute("INSERT INTO part2a (work_quality, job_know, new_know, organization, analysis, resource, attendance, safety, dependability, communication, interpersonal, initiative, user_id) VALUES(:work_quality, :job_know, :new_know, :organization, :analysis, :resource, :attendance, :safety, :dependability, :communication, :interpersonal, :initiative, :user_id)",
                    work_quality=work_quality, job_know=job_know, new_know=new_know, organization=organization, analysis=analysis, resource=resource, attendance=attendance, safety=safety, dependability=dependability, communication=communication, interpersonal=interpersonal, initiative=initiative, user_id=session["user_id"])
        db.execute("INSERT INTO part2b (caring, caring_t, collab, collab_t, committed, committed_t, honest, honest_t, respectful, respectful_t, user_id) VALUES(:caring, :caring_t, :collab, :collab_t, :committed, :committed_t, :honest, :honest_t, :respectful, :respectful_t, :user_id)",
                    caring=caring, caring_t=caring_t, collab=collab, collab_t=collab_t, committed=committed, committed_t=committed_t, honest=honest, honest_t=honest_t, respectful=respectful, respectful_t=respectful_t, user_id=session["user_id"])
        db.execute("INSERT INTO part3 (goals, user_id) VALUES(:goals, :user_id)", goals=goals, user_id=session["user_id"])
        db.execute("INSERT INTO part4 (sup_comm, emp_comm, sup_sig, emp_sig, user_id) VALUES(:sup_comm, :emp_comm, :sup_sig, :emp_sig, :user_id)",
                    sup_comm=sup_comm, emp_comm=emp_comm, sup_sig=sup_sig, emp_sig=emp_sig, user_id=session["user_id"])
        return render_template("submitted.html")
    else:
        return render_template("part4.html")

@app.route("/submitted", methods=["GET", "POST"])
@login_required
def submitted():
    """Show Evaluation Form"""
    if request.method == "POST":
        if request.form['submit'] == 'again':
            return render_template("info_form.html")
        elif request.form['submit'] == 'past':
            evaluations = db.execute(
                "SELECT * FROM info_form WHERE user_id = :user_id", user_id=session["user_id"])
            return render_template("past_evals.html", evaluations=evaluations)

    else:
        return render_template("submitted.html")

@app.route("/past_evals", methods=["GET", "POST"])
@login_required
def history():
    """Show past evaluations"""
    if request.method == "GET":
        evaluations = db.execute(
            "SELECT * FROM info_form WHERE user_id = :user_id", user_id=session["user_id"])
        return render_template("past_evals.html", evaluations=evaluations)

    else:
        employee = request.form.get("submit")
        evaluations = db.execute(
            "SELECT * FROM info_form WHERE id=:name", name=employee)
        part_one = db.execute(
            "SELECT * FROM part1 WHERE id=:name", name=employee)
        dpt = db.execute("SELECT * FROM department WHERE id==:name", name=employee)
        part_twoa = db.execute("SELECT * FROM part2a WHERE id==:name", name=employee)
        part_twob = db.execute("SELECT * FROM part2b WHERE id==:name", name=employee)
        part_three = db.execute("SELECT * FROM part3 WHERE id==:name", name=employee)
        part_four = db.execute("SELECT * FROM part4 WHERE id==:name", name=employee)

        return render_template("employee_eval.html", evaluations=evaluations, one=part_one, dpt=dpt, part_twoa=part_twoa, part_twob=part_twob, part_three=part_three, part_four=part_four)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM reg_users WHERE username = :username", username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        warning = "Warning: Evaluation must be completed in one session; if you close out the session before finishing, your data will be lost."

        flash(warning)
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        # require an input for username
        if not request.form.get("username"):
            return apology("Must enter username", 400)

        # require an input for password
        elif not request.form.get("password"):
            return apology("Must enter password", 400)

        elif not request.form.get("confirmation"):
            return apology("Must re-enter password", 400)

        # if passwords do not match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords do not match")
        #require password to have certain characteristics
        password = request.form.get("password")
        number = False
        letter = False
        symbol = False
        length = False

        # if len(password) > 8:
        #     length = True

        # for i in range(len(password)):
        #     if password[i].isdigit():
        #         number = True
        #     elif password[i].isalpha():
        #         letter = True
        #     elif ord(password[i]) > 32 and ord(password[i]) < 48:
        #         symbol = True

        # if not number or not letter or not symbol or not length:
        #     return apology("password must be more that 8 characters long and contain at least 1 character, number, and symbol (!,#,$,%,&,',(,),*,+,-,.,/)")

        result = db.execute("INSERT INTO reg_users (username, hash, first_name, last_name, dept) VALUES(:username, :hash, :first, :last, :dept)",
                            username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")),
                            first=request.form.get("first_name"), last=request.form.get("last_name"), dept=request.form.get("dept"))
        if not request.form.get("username"):
            return apology("Please choose a username")

        if not result:
            return apology("Username already exists")

        if not request.form.get("first_name"):
            return apology("Please enter your first name")

        if not request.form.get("last_name"):
            return apology("Please enter your last name")

        if not request.form.get("dept"):
            return apology("Please enter your department")

        session["user.id"] = result

        warning = "Warning: Evaluation must be completed in one session; if you close out the session before finishing, your data will be lost."

        flash(warning)
        return redirect("/")
    else:
        return render_template("register.html")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)