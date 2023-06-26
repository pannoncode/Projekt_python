movie_meta = """
create table if not exists movie_meta(
adult boolean,
backdrop_path text,
id integer primary key,
original_language text,
original_title text,
overview text,
popularity numeric,
poster_path text,
release_date date,
title text,
video boolean,
vote_average numeric,
vote_count numeric,
my_poster_path text
)
"""
movie_genre = """
create table if not exists movie_genre(
movie_id integer,
genre_id integer,
CONSTRAINT fk_movie_id FOREIGN KEY (movie_id) REFERENCES movie_meta(id)
)
"""

insert_movie_genre = """
INSERT INTO public.movie_genre
(movie_id, genre_id)
VALUES(:movie_id, :genre_id);
"""
insert_movie_meta = """
INSERT INTO public.movie_meta
(adult, backdrop_path, id, original_language, original_title, overview, popularity, poster_path, release_date, title, video, vote_average, vote_count, my_poster_path)
VALUES(:adult, :backdrop_path, :id, :original_language, :original_title, :overview, :popularity, :poster_path, :release_date, :title, :video, :vote_average, :vote_count, :my_poster_path );
"""


select_meta = """
select mm.title  from movie_meta mm
"""

delete_meta = """
delete from movie_meta where lower(title) = '{title}' 
"""

delete_genre = """
delete from movie_genre m
where m.movie_id in (select id from movie_meta where lower(title) = '{title}')
"""
