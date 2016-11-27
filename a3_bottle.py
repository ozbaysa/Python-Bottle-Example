
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /assignment3/
#####################################################################

from bottle import Bottle, run, route, static_file, view, template, post, request,default_app, debug

def htmlify(title, css, content):
    page = """<!DOCTYPE html>
              <html>
                  <head>
                      <title>""" + title + """</title>
                      <meta charset="utf-8" />""" + css + """
                  </head>
                  <body>
                      """ + content + """
                  </body>
              </html>"""
    return page
def a3_login():
    css = """<link rel="stylesheet" type="text/css" href="/static/login.css">"""
    content = '''
        <form action="/index/" method="POST">
            Name: <input name="name" type="text" />
            </br>
            Surname: <input name="surname" type="text" />
            </br>
            <input value="Login" type="submit" />
        </form>
    '''
    return htmlify("Choosen One",css, content)
def StaticFile(filename):
    return static_file(filename, root="static")
def a3_index():
    global name
    global surname
    name = request.POST.getall('name')
    surname = request.POST.getall('surname')
    global l
    l = []
    l = [] + [name[0]]
    css = """<link rel="stylesheet" type="text/css" href="/static/login.css">"""
    content = "<h2>Choose One of These Five Category " + ", " + name[0] + " " +  surname[0] + "</h2><br>" +\
    """
        <ol>
            <li ><a href= "/music/" >Music</a></li>
            <li ><a href= "/art/">Art</a></li>
            <li ><a href= "/sport/">Sport</a></li>
            <li ><a href= "/travel/">Travel</a></li>
            <li ><a href= "/zaa/">DO NOT CLICK</a></li>
        </ol>
    """
    for b in l:
        content = content +  "</br><p>" + "Participants of this survey: " + b + "<p> </br>"
    return htmlify("Choosen One",css, content)
def a3_music():
    css = """<link rel="stylesheet" type="text/css" href="/static/login.css">"""
    content = """
     <h2>What Kind of Music Do You Listen Often ?</h2>
    <form method = "POST" action = "/final/">
        <input type="radio" name="music" value="metal" checked>metal
        <br>
        <input type="radio" name="music" value="rock">rock
        <br>
        <input type="radio" name="music" value="pop">pop
        <br>
        <input type="radio" name="music" value="rap">rap
        <br>
        <input type = "submit" value="Submit" />
    </form>
    """
    return htmlify("Choosen One",css, content)
def a3_while():
    css = """<link rel="stylesheet" type="text/css" href="/static/login.css">"""
    a = 0;
    content = ""
    while a < 10009:
        content = content + "<p>HI, " + name[0] +", " + " DO YOU WANNA MEET ? :))))))))" + "</p><br>"
        a += 1
    return htmlify("Choosen One",css, content)
def a3_art():
    css = """<link rel="stylesheet" type="text/css" href="/static/login.css">"""
    content = """
     <h2>What Kind of Art Do You Like?</h2>
    <form method = "POST" action = "/final/">
        <input type="checkbox" name="art" value="dr" checked>Drawing
        <br>
        <input type="checkbox" name="art" value="ma">Metalwork Art
        <br>
        <input type="checkbox" name="art" value="ph">Photography
        <br>
        <input type="checkbox" name="art" value="pa">Public Art
        <br>
        <input type = "submit" value="Submit" />
    </form>
    """
    return htmlify("Choosen One",css, content)
def a3_sport():
    css = """<link rel="stylesheet" type="text/css" href="/static/login.css">"""
    content = """
     <h2>What Kind of Sport Do You Like?</h2>
    <form method = "POST" action = "/final/">
        <input type="radio" name="sport" value="fb" checked>Football
        <br>
        <input type="radio" name="sport" value="bb">Basketball
        <br>
        <input type="radio" name="sport" value="rg">Rugby
        <br>
        <input type="radio" name="sport" value="tn">Tennis
        <br>
        <input type = "submit" value="Submit" />
    </form>
    """
    return htmlify("Choosen One",css, content)
def a3_travel():
    css = """<link rel="stylesheet" type="text/css" href="/static/login.css">"""
    content = """
     <h2>Where Do You Want To Travel</h2>
    <form method = "POST" action = "/final/">
        <input type="radio" name="travel" value="en" checked>England
        <br>
        <input type="radio" name="travel" value="us">USA
        <br>
        <input type="radio" name="travel" value="fr">France
        <br>
        <input type="radio" name="travel" value="tr">Turkey
        <br>
        <input type = "submit" value="Submit" />
    </form>
    """
    return htmlify("Choosen One",css, content)
def a3_final():
    css = """<link rel="stylesheet" type="text/css" href="/static/login.css">"""
    music = request.forms.get('music')
    art = request.forms.get('art')
    sport = request.forms.get('sport')
    travel = request.forms.get('travel')
    content = ""
    mu = {"rap":"Check Dis OUT", "pop":"KOP KOP POP", "rock": "DİE MODO FUKO", "metal": "YEAH "}
    ar = {"ph": "NICE ;) ", "ma": "NICE ;) ", "pa": "NICE ;) ", "dr": "NICE ;) "}
    spo = {"bb": "BAsKEEET !!", "fb": "GOOOAL", "rg": "WHO  PLAY THIS SUPPORt FOR REAL ?", "tn": "NİCE CHOICE ;)" }
    tra = {"en": "Would like to grab a tea traveller", "us": "HAMBURGE FAT PEOPLE", "fr": "BONJOUR", "tr": "TURKEY RULEZZZ"}
    if music in mu:
        content = "<p>" +  content + mu[music] + ", " + name[0] + " " + surname[0] + "</p> <br>"
    elif sport in spo:
        content = "<p>" +  content + spo[sport] + ", " + name[0] + " " +   surname[0] + "</p> <br>"
    elif travel in tra:
        content = "<p>" +  content + tra[travel] + ", " + name[0] + " " +   surname[0] + "</p> <br>"
    elif art in ar:
        content = "<p>" + content + ar[art] + ", " + name[0] + " " +   surname[0] + "</p> <br>"
    return htmlify("Choosen One",css, content)
route('/', 'GET', a3_login)
route('/index/', ['GET', 'POST'], a3_index)
route('/music/','GET',a3_music)
route('/art/','GET',a3_art)
route('/sport/','GET',a3_sport)
route('/travel/','GET',a3_travel)
route('/final/',"POST",a3_final)
route('/zaa/',['GET', 'POST'],a3_while)
route("/static/<filename>", "GET", StaticFile)




#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on PythonAnywhere
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on PythonAnywhere
application = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()
