import requests
urlvarify =f"https://apps.emaillistvalidation.com/api/verifEmail?secret="
apikey="jtSxXvO1yLavEu8m4aLmd"
email='shiv.chaudhary@kapso.in'
url=urlvarify+apikey+"&email="+email
print(url)
# r=requests.get(url)
# print(r)