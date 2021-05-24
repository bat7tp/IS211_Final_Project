#This project is an example of a simple blog. As per the EC,
# it has been expanded to allow for multiple users to be able to use.

#THE DB CONNECTION PATH HAS BEEN HARDCODED (Thank you!)

# Currently (as can be found in the final_sql.py file, two users are 'in the system.'
# (Technically, Using more SQL Insert statements, additional users can be added.)
# The users were added as part of SQL and not through the program application itself
# as the requirements and scope of this project were beyond creating a 'register new user' feature

# Current Users Information for testing:
# Username: Batsheva and Password: mypassword
# Username: John and Password: notsure

# Clicking on the browser link leads to the 'home' (/) page with ALL the posts shown,
# in reverse chronological order (newest first). Posts were added to blog with authors
# other than 'Batsheva' or 'John' just to have other content shown. If 'Batsheva' or 'John'
# (or any other later added username), is entered for the author name,
# then their posts will be shown only upon their logging in
# Upon logging on as Batsheva (or John), only posts with the author: Batsheva (or John) show

# If incorrect credentials are put in (username and/or password not found in SQL DB)
# Then the login page will again be shown
#If try accessing add route without logging in, login page will be shown

#Dates must be entered in a mm-dd-yyyy format (as per the datetime features I set up)
# ex. May 6, 1998 should be entered as: 05-06-1998

