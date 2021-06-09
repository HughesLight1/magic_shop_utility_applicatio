DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS alchemists;



CREATE TABLE alchemists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    status VARCHAR(255)

);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    description TEXT,
    quantity INT,
    cost INT,
    price INT,
    alchemist_id INT REFERENCES alchemists(id) ON DELETE CASCADE

);

-- remember its (psql -d magic_shop -f db/magic_shop.sql) to run in terminal!!
-- python3 console.py
-- flask run