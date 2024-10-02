# will import json file for load and dump methods for converting a string to json and vice-versa
import json

# will import a time method for performing a given option in a time
import time


def load_data():
    try:
        # load data from a file if exsits
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # return empty list if doesn't exist
        return []


def save_data_helper(videos):
    # save all videos to the text file
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    # Print top border
    print("\n")
    print("*" * 70)

    # Check if the list is empty
    if not videos:
        print("No videos available.")
    else:
        # Enumerate and print video details
        for index, video in enumerate(videos, start=1):
            # Ensure each video has 'name' and 'duration'
            if "name" in video and "duration" in video:
                print(f"{index}. {video['name']}, Duration: {video['duration']} ")
            else:
                print(f"{index}. Incomplete video data")

    # Print bottom border
    print("\n")
    print("*" * 70)


def add_video(videos):
    # take video name and duration as input
    name = input("Enter video name : ")
    duration = input("Enter video duration : ")

    # appeding entered video details in the video list
    videos.append({"name": name, "duration": duration})
    save_data_helper(videos)


def update_video(videos):
    # listing all videos available
    list_all_videos(videos)
    # taking index of video to be deleted
    index = int(input("Enter the video number to update "))
    # checking if that index is available
    if 1 <= index <= len(videos):
        # checking the details
        name = input("Enter the new video name")
        duration = input("Enter the new video duration")

        # taking index - 1 as list still exists from 0th index not 1
        videos[index - 1] = {"name": name, "duration": duration}

        # saving it to file
        save_data_helper(videos)
    else:
        # invalid index if wrong index is selected
        print("Invalid index selected")


def delete_video(videos):
    # listing all videos available
    list_all_videos(videos)
    # taking index of video to be deleted
    index = int(input("Enter the video number to be deleted "))
    # checking if that index is available
    if 1 <= index <= len(videos):
        del videos[index - 1]
        # saving it to file
        save_data_helper(videos)
    else:
        # invalid index if wrong index is selected
        print("Invalid index selected")


def main():
    # loading videos from the available txt file in the same directory if doesn't exist it will create one
    videos = load_data()

    while True:
        # display menu
        print("YouTube Manager | Choose an option \n")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video ")
        print("4. Delete a youtube video ")
        print("5. Exit the app \n")

        # taking user choice to be performed
        choice = input("Enter your choice : ")
        print("\n")

        # matching choice with the availble index
        match choice:

            case "1":
                # will list all available videos
                list_all_videos(videos)

            case "2":
                # to add a video
                add_video(videos)

            case "3":
                # to update a video
                update_video(videos)

            case "4":
                # to delete a video
                delete_video(videos)

            case "5":
                # quitiing app in 3 seconds
                print("Quiting app in 3 seconds ...")
                time.sleep(3)
                break

            case _:
                # invalid choice choose
                print("Invalid Choice entered ")


# this will match the main function in the body from here the code will start excuting
if __name__ == "__main__":
    # this will call the main function where program is written
    main()
