CREATE TABLE IF NOT EXISTS menu(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS goods(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
price INTEGER NOT NULL
);