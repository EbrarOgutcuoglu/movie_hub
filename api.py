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


@app.get("/api/movies/{movie_id}")
def get_single_movie_api(movie_id: int):
    conn = sqlite3.connect("db.sqlite3")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM movies_movie WHERE id = ?", (movie_id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return Response(
            content=json.dumps({"hata": "Bu ID'ye sahip bir film bulunamadı."}, ensure_ascii=False),
            status_code=404,
            media_type="application/json"
        )

    pretty_json_string = json.dumps(
        {"movie": dict(row)}, indent=4, ensure_ascii=False
    )

    return Response(content=pretty_json_string, media_type="application/json")


@app.delete("/api/movies/{movie_id}")
def delete_movie_api(movie_id: int):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM movies_movie WHERE id = ?", (movie_id,))
    conn.commit()

    deleted_rows = cursor.rowcount
    conn.close()

    if deleted_rows == 0:
        return Response(
            content=json.dumps({"error": "Movie not found or already deleted."}, ensure_ascii=False),
            status_code=404,
            media_type="application/json; charset=utf-8"
        )

    success_json = json.dumps(
        {"message": f"Movie with ID {movie_id} successfully deleted!"},
        ensure_ascii=False
    )
    return Response(content=success_json, media_type="application/json; charset=utf-8")