# Webex Troubleshooting Program
# Student Name: [Muhamad Izzul Najwan]
# Date: [5/11/2023]

import requests
import json

# Webex API Base URL
base_url = "https://api.ciscospark.com/v1"  # This is the base URL for Cisco Webex API.

# Prompting user to enter Webex access token
access_token = input("Please enter your Webex access token: ")  # Enter the user's Webex token to access data on the Webex server.

# Headers for API requests
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

# Testing the connection to Webex
def test_connection():
    response = requests.get(f"{base_url}/people/me", headers=headers)
    if response.status_code == 200:
        print("Connection to Webex server successful.")
    else:
        print("Connection to Webex server failed.")
    input("Press Enter to return.")

# Displaying user information
def display_user_info():
    response = requests.get(f"{base_url}/people/me", headers=headers)
    if response.status_code == 200:
        user_info = json.loads(response.text)
        print("User Information:")
        print(f"Display Name: {user_info['displayName']}")
        print(f"Nickname: {user_info['nickName']}")
        print("Emails:")
        for email in user_info['emails']:
            print(email)
    input("Press Enter to return.")

# Listing rooms information
def list_rooms():
    response = requests.get(f"{base_url}/rooms", headers=headers)
    if response.status_code == 200:
        rooms = json.loads(response.text)
        print("List of Rooms:")
        for room in rooms['items'][:5]:
            print(f"Room ID: {room['id']}")
            print(f"Room Title: {room['title']}")
            print(f"Create Date: {room['created']}")
            print(f"Recent Activity: {room['lastActivity']}")
            print()
    input("Press Enter to return.")

# Creating a new room
def create_room():
    room_title = input("Please Enter Room Name: ")
    room_data = {
        "title": room_title
    }
    response = requests.post(f"{base_url}/rooms", headers=headers, json=room_data)
    if response.status_code == 200:
        print("Room created successfully.")
    else:
        print("Failed to create a room.")
    input("Press Enter to return.")

# Sending a message to a room
def send_message():
    response = requests.get(f"{base_url}/rooms", headers=headers)
    if response.status_code == 200:
        rooms = json.loads(response.text)
        print("Select a room to send a message:")
        for i, room in enumerate(rooms['items'][:5]):
            print(f"{i}. {room['title']}")

        room_index = int(input("Enter the room ID: "))
        if 0 <= room_index < 5:
            room_id = rooms['items'][room_index]['id']
            message = input("Enter the message: ")
            message_data = {"roomId": room_id, "text": message}
            response = requests.post(f"{base_url}/messages", headers=headers, json=message_data)
            if response.status_code == 200:
                print("Message sent successfully.")
            else:
                print("Failed to send the message.")
    input("Press Enter to return.")

# Main program interfaces
while True:
    print("Webex Troubleshooting Center:")
    print("0. Test Connection with Webex")
    print("1. Display User Information")
    print("2. List All Room Information")
    print("3. Create a Room")
    print("4. Send Message to a Room")
    print("5. Exit")
    
    option = input("Please select an option: ")
    
    if option == "0":
        test_connection()
    elif option == "1":
        display_user_info()
    elif option == "2":
        list_rooms()
    elif option == "3":
        create_room()
    elif option == "4":
        send_message()
    elif option == "5":
        print("Logging Out. Have a nice day!")
        break
    else:
        print("Failed to pick an option. Please choose the correct option.")
