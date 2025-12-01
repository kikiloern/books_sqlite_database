#%%
import sqlite3
import pandas as pd
#%%
conn = sqlite3.connect('books.db')
cursor = conn.cursor()
# %%

# Add book
title = "Die Serbische Küche"
author = "Tatjana Petkovski"
date_read = "2024-06-15"
notes = "Gomboce sa slivama do sad najbolje knedle koje sam napravio i pojeo."

cursor.execute(
    'INSERT INTO books (title, author, date_read, notes) VALUES (?, ?, ?, ?)',
    (title, author, date_read, notes)
)
conn.commit()

print("Book added successfully!\n") 

# List all books
cursor.execute('SELECT id, title, author, date_read, notes FROM books')
books = cursor.fetchall()
print("Books in the database:")
for book in books:
    print(book)

df = pd.read_sql_query("SELECT * FROM books", conn)
df.to_excel("books.xlsx", index=False)

conn.close()
print("Exported all books to books.xlsx")


# %%


# %%

#%%

#%%
conn = sqlite3.connect('books.db')
cursor = conn.cursor()


# Delete a book by its id, for example id = 1
book_id_to_delete = 5
cursor.execute('DELETE FROM books WHERE id = ?', (book_id_to_delete,))
conn.commit()

print(f"Book with id {book_id_to_delete} deleted.")
conn.close()
# %%
