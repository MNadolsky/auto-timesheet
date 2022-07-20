# invites

PLEASE INVITE PEOPLE IN ENGINEERING I MISSED. Use proper discretion; slack me if you're not sure.

# auto-timesheet

Script for automatically filling out your timesheet. No timesheet in particular. Just one you may
have to fill out.

# how to use

Put the appropriate values in the following environment variables: 
$TIMESHEET_URL      - url of the timesheet dashboard
                      (this should bring up the login page, but ensure you use the dashboard url
                       in case we support refresh tokens later) 
$TIMESHEET_USERNAME - login username
$TIMESHEET_PASSWORD - login password

Run fill_timesheet.py any time during the week you want your timesheet filled out

# result

Script navigates to the timesheet for the current week, copies your timesheet from the previous
week, and sends it. 

# contribution

This is not a business or even a real open-source project, there are no merge restrictions. That being said, make a PR and seek a review or two from whoever for sanity reasons, though this will not be enforced in any way. Also it's probably good to have a beta branch (though I haven't made one yet) that you can merge new features into and people can just use beta if they want, and every so often we can just test beta and if it's good we can merge to master.

# todo
- support headless
-- headless default
- add params
-- vacay - pto days
-- project_code - to use a project code different than last week
-- headed - in case you really want to ruin the magic
-- week - fill out a specified week
