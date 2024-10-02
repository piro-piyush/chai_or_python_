# For installing pymongo libraries
# url - https://pypi.org/project/pymongo/
# pip install pymongo

# for installing whole library
# import pymago

# for installing just one method
import time
from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')

# You can use mongoDb from here url - https://www.mongodb.com/products/platform/atlas-database
# Create a account and change network access to 0.0.0.0/0 so you can access it from anywhere
# Create a username and password from database access option then give access to read write from role and  open databases then connect choose compus then click to copy link
# here <piyush>:<piyush> are username and password of the mongoDB

# Attempt to connect to the MongoDB database
try:
    client = MongoClient(
    f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@cluster0.hyhjh.mongodb.net/",
    tlsAllowInvalidCertificates=True,
)

    print("Connected to MongoDB successfully.")
except Exception as e:
    print("Connection error:", str(e))

# add ssl certificate if it doesnt allow
# Not a good way to handle ssl
# Not a good idea to include id and password in code files

# Access the database and collection
db = client["ytmanager"]
video_collection = db["videos"]

# print(video_collection)


# listing videos
def list_videos():
    """List of  all videos in the collection."""
    print("\nList of Videos:\n")
    for video in video_collection.find():
        print(
            f"ID: {video['_id']}, Name: {video['name']}, Duration: {video['duration']}"
        )


# To add a video
def add_video(name, duration):
    """Add a new video to the collection."""
    video_collection.insert_one({"name": name, "duration": duration})
    print("Video has been added successfully.")


# To update a video
def update_video(id, new_name, new_duration):
    """Update an existing video in the collection."""
    try:
        video_collection.update_one(
            {"_id": ObjectId(id)},  # Ensure id is an ObjectId
            {"$set": {"name": new_name, "duration": new_duration}},
        )
        print("Video has been updated successfully.")
    except Exception as e:
        print("Error updating video:", str(e))


# To delete a video
def del_video(id):
    """Delete a video from the collection."""
    try:
        video_collection.delete_one({"_id": ObjectId(id)})
        print("Video has been deleted successfully.")
    except Exception as e:
        print("Error deleting video:", str(e))
    # To-do: Debug this id problem


# Main function
def main():
    """Main function to run the YouTube Manager app."""
    while True:
        # Display menu
        print("\nYouTube Manager App with DB")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app\n")

        # Taking user choice
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nYou chose to list available videos.")
            list_videos()

        elif choice == "2":
            print("\nYou chose to add a video.\n")
            name = input("Enter the video name: ")
            duration = input("Enter the video duration: ")
            add_video(name, duration)

        elif choice == "3":
            print("\nYou chose to update a video.\n")
            id = input(
                "Enter the video id to update: "
            )  # Keep as string for ObjectId conversion
            new_name = input("Enter the new video name: ")
            new_duration = input("Enter the new video duration: ")
            update_video(id, new_name, new_duration)

        elif choice == "4":
            print("\nYou chose to delete a video.\n")
            id = input(
                "Enter the video id to delete: "
            )  # Keep as string for ObjectId conversion
            del_video(id)

        elif choice == "5":
            # quitting app in seconds
            print("\nQuitting app in 3 seconds...")
            time.sleep(1)
            print("Quitting app in 2 seconds...")
            time.sleep(1)
            print("Quitting app in 1 second...")
            time.sleep(1)
            print("\nBye Bye !!")
            break

        else:
            print("Invalid choice entered. Please try again.")


# main body of program
if __name__ == "__main__":
    main()