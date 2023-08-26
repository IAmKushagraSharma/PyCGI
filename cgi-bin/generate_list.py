#!/usr/bin/env python

import athletemodel
import yate
import glob

data_files = glob.glob('data/*.txt')

athletes = athletemodel.put_to_store(data_files)

print(yate.start_response())
print(yate.header('Coach Kushagra\'s List of Atheletes'))
print(yate.start_form("generate_timing_data.py"))
print(yate.para('Select an athelete from the list to work with:--'))
for each_athelete in athletes:
    print(yate.radio_button('which_athelete', athletes[each_athelete].name))
print(yate.end_form("Select"))
print(yate.include_footer({'Home:':'/index.html'}))