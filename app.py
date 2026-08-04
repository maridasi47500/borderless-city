from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,phone,country_id,email,password) values (:username,:phone,:country_id,:email,:password)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','phone','country_id','email','password']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','phone','country_id','email','password']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','phone','country_id','email','password']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_discussion", methods=["GET","POST"])
def add_one_discussion():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into discussion (title,content,user_id) values (:title,:content,:user_id)",hey)
        user = query_db('select * from discussion')

        return render_template("discussionform.html", discussions=user, one_user=one_user, the_title="add new discussion", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from discussion')
    one_user = query_db("select * from discussion limit 1", one=True)
    return render_template("discussionform.html", discussions=user, one_user=one_user, the_title="add new discussion", touslesuser=touslesuser)

@app.route("/add_one_answer", methods=["GET","POST"])
def add_one_answer():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslesdiscussion= query_db("select * from discussion")

        one_user = query_db("insert into answer (user_id,discussion_id,content) values (:user_id,:discussion_id,:content)",hey)
        user = query_db('select * from answer')

        return render_template("answerform.html", answers=user, one_user=one_user, the_title="add new answer", touslesuser=touslesuser, touslesdiscussion=touslesdiscussion)


    touslesuser= query_db("select * from user")

    touslesdiscussion= query_db("select * from discussion")

    user = query_db('select * from answer')
    one_user = query_db("select * from answer limit 1", one=True)
    return render_template("answerform.html", answers=user, one_user=one_user, the_title="add new answer", touslesuser=touslesuser, touslesdiscussion=touslesdiscussion)

@app.route("/add_one_image_sharing", methods=["GET","POST"])
def add_one_image_sharing():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into image_sharing (pic,title,user_id) values (:pic,:title,:user_id)",hey)
        user = query_db('select * from image_sharing')

        return render_template("image_sharingform.html", image_sharings=user, one_user=one_user, the_title="add new image_sharing", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from image_sharing')
    one_user = query_db("select * from image_sharing limit 1", one=True)
    return render_template("image_sharingform.html", image_sharings=user, one_user=one_user, the_title="add new image_sharing", touslesuser=touslesuser)

@app.route("/add_one_social_post", methods=["GET","POST"])
def add_one_social_post():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into social_post (user_id,title,content) values (:user_id,:title,:content)",hey)
        user = query_db('select * from social_post')

        return render_template("social_postform.html", social_posts=user, one_user=one_user, the_title="add new social_post", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from social_post')
    one_user = query_db("select * from social_post limit 1", one=True)
    return render_template("social_postform.html", social_posts=user, one_user=one_user, the_title="add new social_post", touslesuser=touslesuser)

@app.route("/add_one_ooh", methods=["GET","POST"])
def add_one_ooh():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescity= query_db("select * from city")

        touslescountry= query_db("select * from country")

        touslesplace= query_db("select * from place")

        one_user = query_db("insert into ooh (city_id,country_id,place_id,title,description) values (:city_id,:country_id,:place_id,:title,:description)",hey)
        user = query_db('select * from ooh')

        return render_template("oohform.html", oohs=user, one_user=one_user, the_title="add new ooh", touslescity=touslescity, touslescountry=touslescountry, touslesplace=touslesplace)


    touslescity= query_db("select * from city")

    touslescountry= query_db("select * from country")

    touslesplace= query_db("select * from place")

    user = query_db('select * from ooh')
    one_user = query_db("select * from ooh limit 1", one=True)
    return render_template("oohform.html", oohs=user, one_user=one_user, the_title="add new ooh", touslescity=touslescity, touslescountry=touslescountry, touslesplace=touslesplace)

@app.route("/add_one_place", methods=["GET","POST"])
def add_one_place():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into place (lat,lon,name) values (:lat,:lon,:name)",hey)
        user = query_db('select * from place')

        return render_template("placeform.html", places=user, one_user=one_user, the_title="add new place")


    user = query_db('select * from place')
    one_user = query_db("select * from place limit 1", one=True)
    return render_template("placeform.html", places=user, one_user=one_user, the_title="add new place")

@app.route("/add_one_language", methods=["GET","POST"])
def add_one_language():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into language (name) values (:name)",hey)
        user = query_db('select * from language')

        return render_template("languageform.html", languages=user, one_user=one_user, the_title="add new language")


    user = query_db('select * from language')
    one_user = query_db("select * from language limit 1", one=True)
    return render_template("languageform.html", languages=user, one_user=one_user, the_title="add new language")

@app.route("/add_one_meteo", methods=["GET","POST"])
def add_one_meteo():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesplace= query_db("select * from place")

        one_user = query_db("insert into meteo (content,place_id) values (:content,:place_id)",hey)
        user = query_db('select * from meteo')

        return render_template("meteoform.html", meteos=user, one_user=one_user, the_title="add new meteo", touslesplace=touslesplace)


    touslesplace= query_db("select * from place")

    user = query_db('select * from meteo')
    one_user = query_db("select * from meteo limit 1", one=True)
    return render_template("meteoform.html", meteos=user, one_user=one_user, the_title="add new meteo", touslesplace=touslesplace)

@app.route("/add_one_news", methods=["GET","POST"])
def add_one_news():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesplace= query_db("select * from place")

        one_user = query_db("insert into news (title,content,place_id) values (:title,:content,:place_id)",hey)
        user = query_db('select * from news')

        return render_template("newsform.html", newss=user, one_user=one_user, the_title="add new news", touslesplace=touslesplace)


    touslesplace= query_db("select * from place")

    user = query_db('select * from news')
    one_user = query_db("select * from news limit 1", one=True)
    return render_template("newsform.html", newss=user, one_user=one_user, the_title="add new news", touslesplace=touslesplace)

@app.route("/add_one_dooh", methods=["GET","POST"])
def add_one_dooh():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesplace= query_db("select * from place")

        tousleslanguage= query_db("select * from language")

        touslesmeteo= query_db("select * from meteo")

        touslesnews= query_db("select * from news")

        one_user = query_db("insert into dooh (lat,lon,title,description,place_id,language_id,meteo_id,news_id) values (:lat,:lon,:title,:description,:place_id,:language_id,:meteo_id,:news_id)",hey)
        user = query_db('select * from dooh')

        return render_template("doohform.html", doohs=user, one_user=one_user, the_title="add new dooh", touslesplace=touslesplace, tousleslanguage=tousleslanguage, touslesmeteo=touslesmeteo, touslesnews=touslesnews)


    touslesplace= query_db("select * from place")

    tousleslanguage= query_db("select * from language")

    touslesmeteo= query_db("select * from meteo")

    touslesnews= query_db("select * from news")

    user = query_db('select * from dooh')
    one_user = query_db("select * from dooh limit 1", one=True)
    return render_template("doohform.html", doohs=user, one_user=one_user, the_title="add new dooh", touslesplace=touslesplace, tousleslanguage=tousleslanguage, touslesmeteo=touslesmeteo, touslesnews=touslesnews)

