import sys

from mechanize import urlopen, urljoin


uri = "http://wwwsearch.sourceforge.net/"

response = urlopen(urljoin(uri, "mechanize/example.html"))
#forms = ParseResponse(response, backwards_compat=False)
form = forms[0]
print form
form["comments"] = "Thanks, Gisle"