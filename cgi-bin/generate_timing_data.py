#!/usr/bin/env python

import cgi
import yate
import athletemodel
import cgitb

cgitb.enable()

form_data = cgi.FieldStorage()
athlete_name = form_data['which_athelete'].value

print(yate.start_response())
print(yate.header('Coach Kushagra\'s Timing Data:--'))

athletes = athletemodel.get_from_store()
print(yate.header("Athlete: " + athlete_name + ", DOB: " +athletes[athlete_name].dob + "."))
print(yate.para('The top 3 times for this athelete are:---'))
print(yate.u_list(athletes[athlete_name].top3))
print(yate.include_footer({"Home":'/index.html', 'Select another athelete': 'generate_list.py'}))