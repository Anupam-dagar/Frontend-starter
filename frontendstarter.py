import os
import urllib
from halo import Halo

root = os.path.dirname(__file__)
print root
static = ""
jsdir = ""
cssdir = ""
vendordir = ""
imgdir = ""
vendorcss = ""
spinner = Halo(text="creating directories...", spinner="dots")

class CssLibrary():
    bootstrap = "https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.css"
    materialize = "https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.css"
    fontawesome = "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
    def downloadBootstrap(self):
        bootstrapFile = urllib.urlopen(self.bootstrap).read()
        return bootstrapFile

    def downloadMaterialize(self):
        materializeFile = urllib.urlopen(self.materialize).read()
        return materializeFile

    def downloadFontAwesome(self):
        fontawesomeFile = urllib.urlopen(self.fontawesome).read()
        return fontawesomeFile

class JsLibrary():
    jQuery = "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"
    bootstrapjs = "https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"
    materializejs = "https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"

    def downloadJquery(self):
        jqueryFile = urllib.urlopen(self.jQuery).read()
        return jqueryFile

    def downloadBootstrapjs(self):
        bootstrapjsFile = urllib.urlopen(self.bootstrapjs).read()
        return bootstrapjsFile

    def downloadMaterializejs(self):
        materializejsFile = urllib.urlopen(self.materializejs).read()
        return materializejsFile

def createlicense():
    license = urllib.urlopen("https://raw.githubusercontent.com/Anupam-dagar/Frontend-starter/master/LICENSE").read()
    return license

def createdirectories():
    global root
    global static
    global cssdir
    global vendorcss
    global imgdir
    global jsdir
    global vendordir
    global spinner
    spinner.start()
    os.mkdir("Frontend-starter")
    os.chdir("Frontend-starter")
    root = os.path.realpath('.')

    os.mkdir("static")
    os.chdir("static")
    static = os.path.realpath('.')

    os.mkdir("css")
    os.chdir("css")
    cssdir = os.path.realpath('.')
    os.mkdir("vendor")
    os.chdir("vendor")
    vendorcss = os.path.realpath('.')
    os.chdir(static)

    os.mkdir("img")
    os.chdir("img")
    imgdir = os.path.realpath('.')
    os.chdir(static)

    os.mkdir("js")
    os.chdir("js")
    jsdir = os.path.realpath('.')
    os.mkdir("vendor")
    os.chdir("vendor")
    vendordir = os.path.realpath('.')
    os.chdir(static)

    os.chdir(root)
    spinner.stop()

def createindex(cssframework):
    os.chdir(root)
    if cssframework == '1':
        filenamecss = "bootstrap.css"
        filenamejs = "bootstrap.min.js"
    elif cssframework == '2':
        filenamecss = "materialize.css"
        filenamejs = "materialize.min.js"
    with open("index.html", "w+") as index:
        index.write('<!-- Generated using Frontend-Starter (https://github.com/Anupam-dagar/Frontend-starter)\n \
                     Author: Anupam Dagar\n \
                     License: MIT -->\n \
                     <!DOCTYPE html>\n \
                     <html>\n \
                     <head>\n \
                        <title>Frontend-Starter</title>\n \
                        <link rel="stylesheet" type="text/css" href="static/css/' + filenamecss + '">\n \
                        <link rel="stylesheet" type="text/css" href="static/css/font-awesome.min.css">\n \
                        <link rel="stylesheet" type="text/css" href="static/css/style.css">\n \
                     </head>\n \
                    <body>\n \
                        <div class="content">\n \
                            <h1 align="center">All set, you can start working on your website.</h1>\n \
                            <h2 align="center">To contribute to Frontend-starter visit <a href="https://github.com/Anupam-dagar/Frontend-starter">Frontend-starter on GitHub</a></h2>\n \
                        </div>\n\n\n\n \
                        <script type="text/javascript" src="static/js/vendor/jquery.min.js"></script>\n \
                        <script type="text/javascript" src="static/js/vendor/' + filenamejs + '"></script>\n \
                        <script type="text/javascript" src="static/js/main.js"></script>\n \
                     </body>\n \
                    </html>'
                    )


def createfiles(cssval):
    cssObj = CssLibrary()
    jsObj = JsLibrary()
    global spinner

    if cssval == '1':
        spinner.text = "Creating bootstrap.css"
        spinner.start()
        os.chdir(cssdir)
        with open("bootstrap.css", "w+") as bootstrap:
            bootstrap.write(cssObj.downloadBootstrap())
        spinner.stop()
        spinner.text = "Creating bootstrap.min.js"
        spinner.start()
        os.chdir(vendordir)
        with open("bootstrap.min.js", "w+") as bootstrapjs:
            bootstrapjs.write(jsObj.downloadBootstrapjs())
        spinner.stop()

    elif cssval == '2':
        spinner.text = "Creating materialize.css"
        spinner.start()
        os.chdir(cssdir)
        with open("materialize.css", "w+") as bootstrap:
            bootstrap.write(cssObj.downloadMaterialize())
        spinner.stop()
        spinner.text = "Creating materialize.min.js"
        spinner.start()
        os.chdir(vendordir)
        with open("materialize.min.js", "w+") as bootstrapjs:
            bootstrapjs.write(jsObj.downloadMaterializejs())
        spinner.stop()

    spinner.text = "Creating jquery.min.js"
    spinner.start()
    with open("jquery.min.js", "w+") as jquery:
        jquery.write(jsObj.downloadJquery())
    spinner.stop()
    spinner.text = "Creating style.css"
    spinner.start()
    os.chdir(cssdir)
    with open("style.css", "w+") as style:
        style.write("/*style.css Generated using Frontend-Starter (https://github.com/Anupam-dagar/Frontend-starter)\nAuthor: Anupam Dagar\nLicense: MIT\nWrite all your custom defined css rule here*/")
    spinner.stop()
    spinner.text = "Creating font-awesome.min.css"
    spinner.start()
    os.chdir(vendorcss)
    with open("font-awesome.min.css", "w+") as fa:
        fa.write(cssObj.downloadFontAwesome())
    spinner.stop()
    spinner.text = "Creating main.js"
    spinner.start()
    os.chdir(jsdir)
    with open("main.js", "w+") as main:
        main.write("//main.js Generated using Frontend-Starter (https://github.com/Anupam-dagar/Frontend-starter)\nAuthor: Anupam Dagar\nLicense: MIT\nWrite all your custom js here")
    spinner.stop()
    spinner.text = "Creating index.html"
    spinner.start()
    createindex(cssval)
    spinner.stop()

def main():
    global spinner
    print "Welcome to Frontend-starter\n"
    css = str(raw_input("Choose the css framework to include:\n1.Bootstrap\t\t2.Materialize\n"))
    print css + " selected\n"
    createdirectories()
    spinner.text = "Creating License"
    spinner.start()
    with open("License.md", "w+") as lic:
        lic.write(createlicense())
    spinner.stop()
    spinner.text = "Creating files"
    createfiles(css)

main()