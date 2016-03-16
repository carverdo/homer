## Getting Started / Overall instructions
Ribcage is a fast and frugal baseline to quickly get your project up and 
running.

0. Create local version of project by creating a local empty project
(of whatever name) and then linking to (see below) and pulling from github.
1. Create your own `venv` directory (won't be in github) directly under
src root  and import package requirements. At a minimum you will need Flask, 
Flask-Login, Flask-DebugToolbar, Flask-SQLalchemy, Flask-Script, 
Flask-Migrate, Flask-WTF, wtforms, psycopg2, requests.
2. Name the local database in `config_vars`;
3. Physically create database of same name (in pgadmin);
4. In one_offs, follow db instructions under `db_create_migrate.py` OR `manager.py` 
(modify this to your own setup; you'll need to move to/from one_offs 
to run) to establish database model in pgadmin;
Make sure your one_off .gitignore is not mangled by this to and fro.
You might run/modify `db_init_data.py` to give an initial populate. 
5. You may need to create a number of local environment variables 
in order for the config files to work properly.
6. Run `run`.

Now you're free to build out your project on top of this skeleton.

## Explanations (directories/Files outside of app)
`logs, migrations, tests` self-explanatory.
`one_offs` e.g. for stuff used in set up only.
`config` and variants primarily for DB setting;
`manager` sets up commands for you to use cmd directly; run from cmd.
`procfile` see more in `heroku`.
`requirements.txt`: keep up to date; useful for moving to production.
NB. Will always be a longer than you suspect (dependencies).

## Explanations (app)
there are three main blueprint areas: `log_auth`, `log_records`, and 
`proj` each of which gets paired with the app as part of `create_app`.

`log_auth` holds a user login system (since every project will need something similar).
`proj` is empty, waiting to be populated for each user-case. Contains static and 
templates (see below)... more to follow.
`log_records` for easy inspecting of your logs.

`templates and static/css`
`base.html` is the template for all other templates (dont change this name - jinja uses).
calls in all sorts of external fonts, bootstrap, highcharts etc. 
looks to `static/css` and also calls `main_new.css` - our modifications.
each (sub-)template extends layout and then calls builds its own blocks -
- redder (calls input_errors); and
- content.
`macros` knows how to:
- present forms (around which panels are drawn); 
- present panels; and 
- present rows (within panels) etc.
the `tdata.htmls` supply the data to those rows; panel header info 
supplied via `views.py / patex`

`db_models` for all model tailoring. 
`gunner` for email generation (tokens).

# Pycharm / Local Set Up
`Run / Edit Config / Defaults / Python / Command Line` - 
so we can play with scripts after running.
`File / Settings / Project Structure / Source` - 
set as source directory.
Create Git repository.

# Gitbash / Gitignores
Check all of your gitignores. 
For the primary one (beneath source) use the intellij default 
and then tailor to, among other things, ignore the venv. 
This will keep the github sync as small as possible. 
(Place other gitignores under subdirectories as required.)  
Make sure there are no stray files / folders, even .pycs. Clear the logs.
Open up Gitbash, cd to the right directory.
`git init` (might reinitialise existing - no problem);
`git add -A`;
`git commit -m"Comment"`;

# Github (deploy part 2)
Now you have version control up and running. 
Let's back that up externally.
`git remote add origin http://github.com/yourgithubaccount/githubproject`
We've added the idea of linkage (a remote origin) but we haven't actually
created anything. 
In your github account make sure that `githubproject` exists.
Push your local to the origin (master branch) -
`git push origin master` (you'll need to sign in to github)

# Heroku (deploy part 2)
Make sure procfile is beneath src root - specific instructions to heroku. 
Double-check `requirements.txt`. 
Login via website, create and name a new app (make it snappy - it's 
a public url!). Go to Deploy and connect to GitHub... 
you're (halfway) done! Website will show up but it's a dummy: you won't
yet be able to log-in.
NB Any pages with any references to dbase will not present properly.
 
## Error Checklist
1. set create_app('production') / debug=False?
2. tested on local AND production?
3. double-checked all config / environment vars (in production)?
4. got rid of stray files incl .pycs?
5. got rid of stray folders?
6. gitignores all ok?
7. procfile names all good?
8. requirements.txt correct?
9. git up to date?
10. double-checked that don't need any config / environ vars in heroku?
11. does the slug look too big (7MB about right)?

## Databases / Provision a database
You still don't have a production database.
`Resources / Add-ons`: just type postgres in the box and click/select 
`Heroku Postgres Hobby-Dev Free` Provision.
### Promote
In git bash if we haven't already, `heroku login`.
`heroku addons` will show us our databases.
`heroku pg:promote DATABASE --app [NAME OF APP]` (which means rewire DATABASE; test this by looking to connection
setting `Psql` on the heroku dashboard). Not strictly necessary with only one db, but 
it will re-title the db with an easier-to-remember colour-scheme name.
### Capture/Backup facility
`heroko pg:backups capture --app [APP NAME]`: captures this facility, ie now you can use 'backups'.


### Copy across a DB
In pgAdmin right-click and `backup` to somewhere in dropbox. Copy the link which will look
like this (go into dropbox.com and share link):
`https://www.dropbox.com/s/8a2cmqr9hho96z3/gscore_v0.dump?dl=0`  
But adjust (see start; drop the end):
`https://dl.dropboxusercontent.com/s/8a2cmqr9hho96z3/gscore_v0.dump`
And trick the system into using this back-up to 'restore' our database -
`heroku pg:backups restore '[DROPBOX LINK]' [DATABASE] --app [APP NAME]` (keep the single quotation
marks - don't mistakenly use GRAVE ACCENTS!; rid squares, use real link, real database name eg HEROKU_POSTGRES_COPPER_URL)  
Will get a destruction warning...
Quick-check: heroku dashboard should now show correct number of tables.

## Config Vars (under Settings)
Add a `SECRET_KEY` (otherwise you end up with lots of CSRF errors as heroku keeps regenerating);
no need for quotation marks as you enter the number. Only need to do once per project.
Repeat for any other config vars set by environment.

## Debug = False
Don't forget.
Finito!