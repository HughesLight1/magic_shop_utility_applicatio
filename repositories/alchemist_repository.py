from db.run_sql import run_sql
from models.alchemist import Alchemist
from models.item import Item

def save(alchemist):
    sql = "INSERT INTO alchemists (name, email, status) VALUES (%s, %s, %s) RETURNING *"
    values = [alchemist.name, alchemist.email, alchemist.status]
    results = run_sql(sql, values)
    id = results #[0]['id'] took this out to see what happened June13@19:36
    alchemist.id =id
    return alchemist

def select_all():
    alchemists =[]
    sql = "SELECT * from alchemists ORDER by id"
    results = run_sql(sql)

    for row in results:
        alchemist  = Alchemist(row['name'], row['email'], row['status'], row['id'])
        alchemists.append(alchemist)
    return alchemists

def select(id):
    alchemist = None
    sql = "SELECT * FROM alchemists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        alchemist = Alchemist(result['name'], result['email'], result['status'], result['id'])
    return alchemist

def delete_all():
    sql = "DELETE FROM alchemists"
    run_sql(sql)

def update(alchemist):
    sql = "UPDATE alchemists SET (name, email, status)=(%s, %s, %s) WHERE id = %s"
    values = [alchemist.name, alchemist.email, alchemist.status, alchemist.id]
    run_sql(sql,values)