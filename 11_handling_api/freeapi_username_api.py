# use this to install requests library first
# url - https://pypi.org/project/requests/
# pip install requests

# Use this to get free api
# url - https://api.freeapi.app/#/

import requests


def fetch_random_user_freeapi():
    # saving the url in a varibale name url
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    # sending req to url and saving response
    response = requests.get(url)

    # converting response to json
    data = response.json()

    # if data is loaded it contains success
    if data["success"] and "data" in data:
        # taking data key method from the data and storing in user_data
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        # return username, country
        return username, country
    else:
        # will raise a custom exception
        raise Exception("Failed to fetch user data")


def main():
    try:
        username, country = fetch_random_user_freeapi()
        print(f"\nUsername : {username} \nCountry : {country}\n")
    except Exception as e:
        print(str(e))


# calling main body
if __name__ == "__main__":
    main()
