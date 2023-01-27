import sqlite3


def get_by_title(title_film):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    data = {}
    sqlite_query = ("""
    SELECT title, country, release_year, listed_in, description FROM netflix
    WHERE release_year = 2021
    AND title = ?
    ORDER BY release_year DESC
    LIMIT 1
    """)
    cur.execute(sqlite_query, (title_film,))
    executed_query = cur.fetchall()
    con.close()
    data["title"] = executed_query[0][0]
    data["country"] = executed_query[0][1]
    data["release_year"] = executed_query[0][2]
    data["genre"] = executed_query[0][3]
    data["description"] = executed_query[0][4]
    return data


def search_with_lim(year1, year2):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    data = {}
    data_ = []
    sqlite_query = ("""
        SELECT title, release_year FROM netflix
        WHERE release_year BETWEEN ? AND ?
        LIMIT 100
        """)
    cur.execute(sqlite_query, (year1, year2,))
    executed_query = cur.fetchall()
    for i in executed_query:
        data['title'] = i[0]
        data['release_year'] = i[1]
        data_.append(data)
        data = {}
    con.close()
    return data_


def type_search(rating):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    data = {}
    data_ = []
    if rating == 'children':
        sqlite_query = ("""
               SELECT title, rating, description FROM netflix
               WHERE rating = 'G'
               
               """)
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()
        for i in executed_query:
            data['title'] = i[0]
            data['rating'] = i[1]
            data['description'] = i[2]
            data_.append(data)
            data = {}
        con.close()
        return data_
    elif rating == 'family':
        sqlite_query = ("""
               SELECT title, rating, description FROM netflix
               WHERE rating = 'G'
               OR rating = 'PG'
               OR rating = 'PG-13'
                """)
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()
        for i in executed_query:
            data['title'] = i[0]
            data['rating'] = i[1]
            data['description'] = i[2]
            data_.append(data)
            data = {}
        con.close()
        return data_
    else:
        sqlite_query = ("""
                       SELECT title, rating, description FROM netflix
                       WHERE rating = 'R'
                       OR rating = 'NC-17'
                        """)
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()
        for i in executed_query:
            data['title'] = i[0]
            data['rating'] = i[1]
            data['description'] = i[2]
            data_.append(data)
            data = {}
        con.close()
        return data_


def search_by_genre(genre):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    data = {}
    data_ = []
    sqlite_query = (f"""
        SELECT title, description FROM netflix
        WHERE listed_in LIKE '%{genre.lower()}%'
        LIMIT 100
        """)
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    for i in executed_query:
        data['title'] = i[0]
        data['description'] = i[1]
        data_.append(data)
        data = {}
    con.close()
    return data_


def step5(name1, name2):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    data = {}
    sqlite_query = (f"""
            SELECT netflix.cast FROM netflix
            WHERE netflix.cast LIKE '%{name1}%'
            AND netflix.cast LIKE '%{name2}%'
            
            """)
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    for i in executed_query:
        if i != name1 and i != name2:
            if i not in data:
                data[i] = 1
            else:
                data[i] += 1
    for k, v in data.items():
        if v > 2:
            print(k)

    return executed_query


def step6(type_of_movie, release_year, genre):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    data = {}
    data_ = []
    sqlite_query = (f"""
       SELECT title, description FROM netflix
       WHERE listed_in LIKE '%{genre}%'
       and release_year = {release_year}
       and netflix.type = '{type_of_movie}'
       """)
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    for i in executed_query:
        data['title'] = i[0]
        data['description'] = i[1]
        data_.append(data)
        data = {}
    con.close()
    return data_
