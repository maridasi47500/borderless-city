
mkdir templates 
python3 scaffold.py user username phone country_id:references email password
python3 scaffold.py discussion title content user_id:references
python3 scaffold.py answer user_id:references discussion_id:references content
python3 scaffold.py image_sharing pic title user_id:references
python3 scaffold.py social_post user_id:references title content
python3 scaffold.py ooh city_id:references country_id:references place_id:references title description
python3 scaffold.py place lat lon name
python3 scaffold.py language name
python3 scaffold.py meteo content place_id:references
python3 scaffold.py news title content place_id:references
python3 scaffold.py dooh lat lon title description place_id:references language_id:references meteo_id:references news_id:references
