stringsSQL = [
    """
    CREATE TABLE IF NOT EXISTS characters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        balance DECIMAL(9,2),
        gender VARCHAR(1)
    )
    """,

    """
    INSERT INTO characters (name, balance, gender) VALUES (?, ?, ?)
    """,

    """
    UPDATE characters 
    SET name = ?, 
        balance = ?, 
        gender = ? 
    WHERE id = ?;
    """,

    """
    Delete from characters
    where id = ?
    """,

    """
    Select * from characters
    """
]