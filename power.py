import sys

import mechanize


uri = "http://www.powertochoose.com/"


request = mechanize.Request(uri)
response = mechanize.urlopen(request)
forms = mechanize.ParseResponse(response, backwards_compat=False)
response.close()
## f = open("example.html")
## forms = mechanize.ParseFile(f, "http://example.com/example.html",
##                              backwards_compat=False)
## f.close()
form = forms[0]
print form  # very useful!

form["zip_code"] = "77459"
print form["zip_code"]

