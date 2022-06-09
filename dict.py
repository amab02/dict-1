import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="dict",
   user="dict",
   password="456abc"
)

the_list = []
print("-----Hello and welcome to the dictionary! Available commands:-----")

commands = [
    'ADD: Add a name to the list',
    'LIST: Print the list of names',
    'DELETE: Delete a name from the list',
    'QUIT: End the program',
    'SAVE: Saves the data',
    'HELP: This message will come up again!' ]
for x in commands:
    print(x)

# read_dict: returns the list of all dictionary entries:
# argument: C - the database connection.
def read_dict(C):
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
#add_word: Adds a new word to the dictionary
def add_word(C, word, translation):
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
#delete_word: deletes the word from the dictionary
def delete_word(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
# save_dict: saves the data
def save_dict(C):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ").strip().lower()
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ").strip().title()
        phone = input("  Translation: ")
        add_word(conn, name, phone)
        print(f" Added word { name}")
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        exit()
