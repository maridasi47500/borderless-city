CREATE TABLE  IF NOT EXISTS contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS groups (
   group_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS contact_groups(
   contact_id INTEGER,
   group_id INTEGER,
   PRIMARY KEY (contact_id, group_id),
   FOREIGN KEY (contact_id) 
      REFERENCES contacts (contact_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
   FOREIGN KEY (group_id) 
      REFERENCES groups (group_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '1', 'anonyme', 'noname', 'anonymous@email.fr', '+2653546434');
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '2', 'anne onim', 'onim', 'anne.onim@email.com', '+86877779898');
create table if not exists user(
        id integer primary key autoincrement,
        username text,
            phone text,
            country_id text,
            email text,
            password text
                    );
create table if not exists discussion(
        id integer primary key autoincrement,
        title text,
            content text,
            user_id text
                    );
create table if not exists answer(
        id integer primary key autoincrement,
        user_id text,
            discussion_id text,
            content text
                    );
create table if not exists image_sharing(
        id integer primary key autoincrement,
        pic text,
            title text,
            user_id text
                    );
create table if not exists social_post(
        id integer primary key autoincrement,
        user_id text,
            title text,
            content text
                    );
create table if not exists ooh(
        id integer primary key autoincrement,
        city_id text,
            country_id text,
            place_id text,
            title text,
            description text
                    );
create table if not exists place(
        id integer primary key autoincrement,
        lat text,
            lon text,
            name text
                    );
create table if not exists language(
        id integer primary key autoincrement,
        name text
                    );
create table if not exists meteo(
        id integer primary key autoincrement,
        content text,
            place_id text
                    );
create table if not exists news(
        id integer primary key autoincrement,
        title text,
            content text,
            place_id text
                    );
create table if not exists dooh(
        id integer primary key autoincrement,
        lat text,
            lon text,
            title text,
            description text,
            place_id text,
            language_id text,
            meteo_id text,
            news_id text
                    );
