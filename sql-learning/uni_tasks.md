# Part 1

## 1.
SELECT * \
FROM movies.movie \
WHERE year=2000 

## 2.
SELECT year, COUNT(year) \
FROM movies.movie \
GROUP BY year 

## 3.
SELECT n.name, n.year, m.genre \
FROM movies.movie n, movies.genre m \
WHERE n.mid = m.mid

## 4.
SELECT m.name, m.year, g1.genre, g2.genre \
FROM movies.movie m, movies.genre g1, movies.genre g2 \
WHERE m.mid=g1.mid AND m.mid=g2.mid AND g1. \ genre='Crime' AND g2.genre='Drama'

## 5.
SELECT p.name, a.role, m.name, m.year \
FROM movies.movie m, movies.person p, movies.acts a \
WHERE a.role LIKE '%Tom%' AND a.pid=p.pid AND m.mid=a.mid \
ORDER BY p.name, m.year

## 6.
SELECT p.name, COUNT(d.mid) as count1 \
FROM movies.person p, movies.directs d \
WHERE p.pid=d.pid \
GROUP BY p.pid, p.name \
ORDER BY count1 DESC

## 7.
SELECT l.language, COUNT(DISTINCT m.mid), COUNT(DISTINCT p.pid) \
FROM movies.language l, movies.movie m, movies.person p, movies.acts a \
WHERE a.mid=l.mid AND a.mid=m.mid AND a.pid=p.pid \
GROUP BY l.language

# Assignment table

1. Player ( 
    - player_id PK, 
    - player_name, 
    - player_username UNIQUE, 
    - date_of_birth, 
    - country, 
    - favorite_genre_id FK -> Genre(genre_id) 
    )
2. Contact_Information ( 
    - player_email PK, 
    - phone, 
    - player_id FK -> Player(player_id) UNIQUE NOT NULL )
3. Purchase ( 
    - purchase_id PK, 
    - purchase_date, 
    - payment_method,
    - player_id FK -> Player(player_id),
    - store_id FK -> Store(store_id) )
4. Genre ( 
    - genre_id PK, 
    - genre_name )
5. Platform ( 
    - platform_id PK, 
    - platform_name )
6. Studio ( 
    - studio_id PK, 
    - studio_name, 
    - studio_country, 
    - studio_email )
7. Game ( 
    - game_id PK, 
    - title, 
    - release_year, 
    - rating, 
    - game_price, 
    - platform_id FK -> Platform(platform_id), 
    - genre_id FK -> Genre(genre_id), 
    - studio_id FK -> Studio(studio_id) )
8. Store ( 
    - store_id PK, 
    - store_name, 
    - store_city )
9. PurchaseLineItem ( 
    - item_id PK, 
    - quantity, 
    - item_price,
    - purchase_id FK -> Purchase(purchase_id),
    - game_id FK -> Game(game_id) )
