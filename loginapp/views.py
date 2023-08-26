from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.


def home(request):
    return render(request, "index.html")


def mysignup(request):

    if request.method == 'POST':
        data = request.POST
        if data.get("Password1") == data.get("Password2"):
            if not User.objects.filter(username=data.get("studUsername")):
                password = data.get("Password1")
                username = data.get("studUsername")
                firstname = data.get("studFName")
                lastname = data.get("studLName")
                email = data.get("studEmail")
                myuser = User.objects.create_user(
                    username=username, email=email, password=password)
                myuser.first_name = firstname
                myuser.last_name = lastname
                myuser.save()

                Student.objects.create(studEmail=email, studUsername=username,
                                       studFName=firstname, studLName=lastname, studPassword=password)

            else:
                messages.error(request, "User Already Exist. Please")
                return redirect("signup")
        else:
            messages.warning(request, "Passwords do not match")
            return redirect("signup")

        return redirect("/")
    else:
        return render(request, "signup.html")


def mylogout(request):
    logout(request)
    return redirect("/")


def account(request, id):
    myuser = Student.objects.get(studUsername=id)
    print(myuser.studBirthdate)
    return render(request, "account.html", {"myuser": myuser})


def completesignup(request, id):
    if request.method == "POST":
        data = request.POST
        myuser = Student.objects.get(studUsername=id)
        print(data)
        myuser.studBirthdate = data["studBirthdate"]
        myuser.studEmail = data["studEmail"]
        myuser.studFName = data["studFName"]
        myuser.studLName = data["studLName"]
        myuser.studAge = data["studAge"]
        myuser.studAddress = data["studAddress"]
        myuser.studClass = data["studClass"]

        myuser.save()

        return redirect("/accounts/"+id)

    myuser = Student.objects.get(studUsername=id)
    return render(request, "completesignup.html", {"myuser": myuser})


def contact(request, id):
    if request.method == "POST":
        messagebox = request.POST
        Name = messagebox.get("Name")
        Email = messagebox.get("Email")
        Message = messagebox.get("Message")
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        sender = 'pmsoni2016@gmail.com'
        myPass = "sqqpkpjigjluiukb"

        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = sender
        message['Subject'] = 'Regarding Your Website'

        # HTML-formatted content
        html_content = f"""
        <html>
        <head></head>
        <body>
            <h2>Hello,</h2>
            <p>This is an <strong>auto generated</strong> email sent using Python.</p>
            <p>This <strong>Email</strong> is sent to you by : <strong><font color="red">{Name}</font></strong> with the email <strong><font color="red">{Email}</font></strong> </p>
            <p>The <strong>Message</strong> says that : <strong><font color="red">{Message}</font></strong>
            <p>Regards,<strong><br>Python Bot</strong></p>
        </body>
        </html>
        """

        # Attach the HTML content
        message.attach(MIMEText(html_content, 'html'))

        try:
            server = smtplib.SMTP("smtp.gmail.com", port=587)
            server.starttls()  # Start TLS encryption
            server.login(sender, myPass)
            text = message.as_string()
            server.sendmail(sender, sender, text)
            server.quit()
            print('Email sent successfully!')
        except Exception as e:
            print('Error:', str(e))

    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def projects(request):
    return render(request, "projects.html")


def handlelogin(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(username=data.get(
            "studUsername"), password=data.get("Password1"))
        if user is not None:
            myuser = {
                "username": user.get_username()
            }
            messages.success(request, "Success Login")
            login(request, user=user)
            return redirect("/")
        else:
            messages.error(request, "No User found/Invalid Password")
            return redirect("/")
