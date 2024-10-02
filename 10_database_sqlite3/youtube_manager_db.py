import sqlite3
import time

conn = sqlite3.connect("videos.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS VIDEOS (
        ID INTEGER PRIMARY KEY,
        NAME TEXT NOT NULL,
        DURATION TEXT NOT NULL
    )
"""
)


def list_videos():

    # Execute the query to select all videos
    cursor.execute("SELECT * FROM VIDEOS")
    rows = cursor.fetchall()

    # Display the results in a MySQL shell-like format
    print("+----+------------------------------------+---------------+")
    print("| ID | NAME                               | DURATION      |")
    print("+----+------------------------------------+---------------+")
    for row in rows:
        print(f"| {row[0]:<2} | {row[1]:<34} | {row[2]:<13} |")
    print("+----+------------------------------------+---------------+")


def add_video(name, duration):
    cursor.execute("INSERT INTO VIDEOS (NAME, DURATION) VALUES (?,?)", (name, duration))
    conn.commit()


def update_video(id, new_name, new_duration):
    cursor.execute(
        "UPDATE FROM VIDEOS SET NAME = ? time = ? WHERE ID = ?",
        (new_name, new_duration, id),
    )
    conn.commit()


def del_video(id):
    cursor.execute("DELETE FROM VIDEOS WHERE ID =?", (id,))
    conn.commit()


def main():
    while True:
        # display menu
        print("\nYouTube Manager app with DB")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video ")
        print("4. Delete a youtube video ")
        print("5. Exit the app \n")

        # taking user choice to be performed
        choice = input("Enter your choice : ")

        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("Enter the video name : ")
            duration = input("Enter the video duration: ")
            add_video(name, duration)

        elif choice == "3":
            id = int(input("Enter the video id to be update : "))
            name = input("Enter the video name : ")
            duration = input("Enter the video duration : ")
            update_video(name, duration)

        elif choice == "4":
            id = int(input("Enter the video id to delete : "))
            del_video(id)

        elif choice == "5":
            print("Quitting app in 3 seconds ")
            time.sleep(3)
            break
        else:
            print("Invalid choice entered")
    conn.close()


if __name__ == "__main__":
    main()
