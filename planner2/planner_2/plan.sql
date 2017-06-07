CREATE TABLE IF NOT EXISTS plan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL DEFAULT '',
        task_text TEXT NOT NULL DEFAULT '',
        task_status TEXT NOT NULL DEFAULT ''
        )
