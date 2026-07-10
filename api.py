import sqlite3
import json
from fastapi import FastAPI , Response

app = FastAPI()


@app.get("/api/movies")
def get_movies_api():

    conn = sqlite3.connect("db.sqlite3")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()



    cursor.execute("SELECT * FROM movies_movie")
    rows = cursor.fetchall()


    movies_list = [dict(row) for row in rows]
    conn.close()
    pretty_json_string = json.dumps(
        {"movies": movies_list}, indent=4, ensure_ascii=False
    )


    return Response(content=pretty_json_string, media_type="application/json")

@app.get("/api/directors")
def get_director_api():
    conn = sqlite3.connect("db.sqlite3")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM directors_director")
    rows = cursor.fetchall()

    directors_list = [dict(row) for row in rows]
    conn.close()
    pretty_json_string = json.dumps(
        {"directors": directors_list}, indent=4, ensure_ascii=False
    )

    return Response(content=pretty_json_string, media_type="application/json")