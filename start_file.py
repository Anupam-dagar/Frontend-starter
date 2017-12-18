import os
import urllib
import datetime
class CssLibrary():
    bootstrap = "https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.css"
    materialize = "https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.css"
    bulma = "https://cdnjs.cloudflare.com/ajax/libs/bulma/0.6.1/css/bulma.css"
    fontawesome = "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
    def downloadBootstrap(self):
        bootstrapFile = urllib.urlopen(self.bootstrap).read()
        return bootstrapFile

    def downloadMaterialize(self):
        materializeFile = urllib.urlopen(self.materialize)
        return materializeFile

    def downloadBulma(self):
        bulmaFile = urllib.urlopen(self.bulma)
        return bulmaFile

    def downloadFontAwesome(self):
        fontawesomeFile = urllib.urlopen(self.fontawesome)
        return fontawesomeFile

class JsLibrary():
    jQuery = "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"
    bootstrapjs = "https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"
    materializejs = "https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"

    def downloadJquery(self):
        jqueryFile = urllib.urlopen(self.jQuery)
        return jqueryFile

    def downloadBootstrapjs(self):
        bootstrapjsFile = urllib.urlopen(self.bootstrapjs)
        return bootstrapjsFile

    def downloadMaterializejs(self):
        materializejsFile = urllib.urlopen(self.materializejs)
        return materializejsFile

def createlicense():
    name = str(raw_input("Enter your name:\n"))
    currentDate = datetime.datetime.now()
    year = str(currentDate.year)
    license = 'Copyright ' + year + ' ' + name + '\n\n' + 'Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.'
    return license


