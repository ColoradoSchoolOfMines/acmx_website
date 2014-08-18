ACMxLabs.org
============

This is a complete rewrite of the ACMx Labs website in Django 1.7. It should
be up to the same point as the original Django-nonrel app by the first ACMx
meeting of the Fall '14 semester. If you want to work on it, you should
probably wait until then.

## How to Contribute

Before you can start working on ACMx Labs, there are a few initial setup
steps you'll have to complete.

1. Make sure you have accounts on [GitHub](https://github.com/) and
   [Trello](https://trello.com/), and ask to be added to the ACMx
   organizations on each.
2. Install and [configure](https://help.github.com/articles/set-up-git) `git`
   on your computer. If you're using Windows, try [GitHub for
   Windows](https://windows.github.com/); Mac users try [GitHub for
   Mac](https://mac.github.com/).
3. Windows and Mac users, read [this](#windows-mac); Linux users, read
   [this](#linux).
4. Learn how to use [git](#using-git) and [Django](#working-with-django).

### Working from a Windows or Mac computer <a name="windows-mac"></a>

If you have a Windows or Mac machine, you will probably want to work from a
local clone, then deploy to a test server to see your changes. To get
started, clone the acmw_website repo through the GitHub program, or from the
command-line with `git clone https://github.com/ColoradoSchoolOfMines/acmx_website.git`.

[Let me know](mailto:rshipp@mines.edu) that you're working from a Windows or Mac and
need a test server, and I'll help you get set up with one.

Make whatever changes you want (see [using git](#using-git) for an example
workflow, or use the GitHub program to manage your changes). Before pushing
to GitHub, deploy to the test server with `fab deploy` and make sure
everything works.

### Working from a development server (or a Linux computer) <a name="linux"></a>

#### Initial setup

If you have a Linux machine you can use as a dev server, awesome. If you
don't, but you want to try working on a server, just [let me
know](mailto:rshipp@mines.edu) and I'll get you set up with remote SSH access on one
of mine. The instructions below assume you're working on a Debian-based
server (like Ubuntu).

First, install and configure the tools you'll be using:

```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python-dev git build-essential python-pip
sudo pip install virtualenvwrapper
cat << EOF >> ~/.bashrc
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
EOF
source ~/.bashrc
```

Be sure to [set up git](https://help.github.com/articles/set-up-git).

Next, set up a virtualenv and grab everything you'll need to work on the
website:

```bash
mkvirtualenv acmx
git clone https://github.com/ColoradoSchoolOfMines/acmx_website.git
cd acmx_website
sudo pip install -r requirements.txt
```

There are a few secret settings that we can't store on GitHub, so you'll have
to ask for a copy of those before you can go any farther.

Once you have all the secret stuff, apply the database migrations and start
up the Django development server with:

```bash
./manage.py syncdb
./manage.py runserver
```

When you're working on a remote server like this, you won't be able to use any
IDE or fancy graphical text editor. I highly recommend you learn how to use
`vim`, but since it has a bit of a learning curve, you may want to start out
with `nano` instead. Just open files with `vim myfile.html` or `nano
myfile.html`.

#### Continuing development

Whenever you log into the server, you'll need to first "source" the
virtualenv, with:

    workon acmx

Then change to the website directory (`cd acmx_website`), make sure you have
the latest code (`git pull`), and start hacking.

### Using Git

Git is an awesome tool for collaborative development, but it takes some
getting used to if you've never seen it before. GitHub has a great [online
tutorial](https://try.github.io/) for getting started with git, that will
only take a few minutes.

For the most part, your development cycle should look something like this:

Pull in the latest code from GitHub:

    git pull

Work on whatever new feature or bugfix you're adding. When you're done, make
sure the tests still pass:

    ./manage.py test

If there are any failures, stop and find out what broke, and fix it. Then
add your changes:

    git add -p


The `-p` option brings up interactive add; press `y` if the changes look
correct, or `n` if they don't and you want to go back and fix something. You
can also use `q` to exit. Once everything looks right and you've added all
the changes, commit them:

(**Note**: If you added new files instead of just changing ones that were
already there, you should run `git add -A` at this point.)

    git commit -m "A short description of what I changed."

And push the changes to GitHub:

    git push

If there are errors at this point, someone may have pushed their changes
while you were making yours. Pull again, fix any merge conflicts, and push:

    git pull
    git push

### Working with Django

For a more in-depth guide to Django, go read [the official
tutorial](https://docs.djangoproject.com/en/1.7/intro/tutorial01/) and the
[Test Driven Development with Python](http://chimera.labs.oreilly.com/books/1234000000754/)
book. Here's a quick start guide:

#### Backend logic

Since Django is a Python framework, all the logic for the site is written in
Python. The models, which describe the database layout, are in
[projects/models.py](projects/models.py). The views, which tell Django how to
display different pages on the site, are in [projects/views.py](projects/views.py).
These are the files backend developers will work with most.

If you change the models, you'll need to create a "migration" for your
changes. In Django 1.7, this is as easy as running `./manage.py makemigrations`.
Windows and Mac users won't be able to do this without having Django
installed, so either do it on a Linux server, or ask for help from someone
running Linux.

#### Frontend

Django uses its own template language, mixed with HTML, to render site pages.
All of these are in [projects/templates/](projects/templates/). Static files,
like images, CSS and JavaScript, are stored in
[projects/static/](projects/static/).
