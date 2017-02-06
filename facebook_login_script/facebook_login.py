#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
#
# ---------------- READ ME ---------------------------------------------
# This Script is Created For Practise And Educational Purpose Only
# I will Not Take Any Type Of Responsibility.
# Use This Script On Your Own Responsibility.
# No Warranty, No Responsibility
# This Script Is Only A Example. Created For http://bitforestinfo.blogspot.com

'''
print __author__
# Import Modules
import mechanize
import cookielib
import cookielib
import sys

# Take User Inputs
user=raw_input('[+] Facebook A/c Username : ')		# UserName
password=raw_input('[+] Facebook A/c Password : ')	# Password

# Facebook Login Page Url
login='https://m.facebook.com/login.php?login_attempt=1'

# Creating Browser
br = mechanize.Browser()

# Browser Configurations
cj=cookielib.LWPCookieJar()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1) 

# User Agent
k=('Mozilla/5.0 (BeOS; U; BeOS BeBox; fr; rv:1.9) Gecko/2008052906 BonEcho/2.0')

print " [+] User Agent : ", k

# Add User Agent In Header
br.addheaders = [('User-agent', k)]

print " [+]   Please Wait Loading Page .... [+]"

# Try To Get Login Page
try:
	# Open Login Page
    site = br.open(login)

except Exception as e:
	# Print Error
	print e
	print " [+] Please Check Internet Connections " 
	sys.exit(0) 

# Now Login Page Is Ready 
try:
	br._factory.is_html = True
except Exception as e:
	print e

# Select Form By Index
br.select_form(nr=0)

# Enter Username
br.form['email']=user

# Enter Password
br.form['pass']=password

# Now Submit
br.submit()

# Get Url
log=br.geturl()

# Check Login Page Url
if ".facebook.com/home.php" in log:
	print " [+] [=]   Login Sucessful   [=] [+] "    
else:
	print "[*] Enable To Login"
