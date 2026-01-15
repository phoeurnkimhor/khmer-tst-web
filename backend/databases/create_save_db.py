from sqlalchemy import text

def create_predictions_table(engine):
    query = """
    CREATE TABLE IF NOT EXISTS text (
        input TEXT,
        output TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    with engine.begin() as conn:
        conn.execute(text(query))
    print("Table created or already exists.")

def insert_prediction(engine, input, output):
    query = text("""
        INSERT INTO text (input, output, created_at)
        VALUES (:input, :output, CURRENT_TIMESTAMP AT TIME ZONE 'Asia/Phnom_Penh')
    """)
    with engine.begin() as conn:
        conn.execute(query, {
            "input": input,
            "output": output
        })
    print("Prediction inserted successfully.")

