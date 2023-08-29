import json
import tkinter as tk
from tkinter import *
import random


with open("sampledata/Userdata.json", "r", encoding="utf-8") as json_file:
    userData = json.load(json_file)
with open("sampledata/StreamingHistory.json", "r", encoding="utf-8") as json_file:
    streamingHistory = json.load(json_file)
with open("sampledata/Inferences.json", "r", encoding="utf-8") as json_file:
    inferences = json.load(json_file)
# print(userData) 
theme = "black"

# Create the main window
root = tk.Tk()
root.title("Sportify Sample")
root.geometry("1280x750")

# Prevent window from being resizable
root.resizable(False, False)

# Add internal padding
root['padx'] = 10
root['pady'] = 10

# Header Pane Related event handlers
def user_home_handler():
    if button["text"] == "Home":
        button["text"] = "User"
        show_streaming_history()
    else:
        button["text"] = "Home"
        show_user_details()

def on_song_search(event=None):
    input_text = input_field.get()
    print("Input:", input_text)

def show_user_details():
     # Clear any existing widgets in pane2
    for widget in pane2.winfo_children():
        widget.destroy()

    # Create a new pane for user details
    user_details_pane = tk.Frame(pane2,  padx=50, pady=20, )
    user_details_pane.pack( side=tk.RIGHT, anchor=tk.CENTER, padx=50 )

    labels = [
        ("Username:", userData["username"]),
        ("Email:", userData["email"]),
        ("Country:", userData["country"]),
        ("Birthdate:", userData["birthdate"]),
        ("Gender:", userData["gender"]),
        ("Creation Time:", userData["creationTime"])
    ]

    # Add labels and right-aligned values to user_details_pane using the grid layout
    for row, (label_text, value) in enumerate(labels):
        label = tk.Label(user_details_pane, text=label_text, font=("Helvetica", 12))
        label.grid(row=row, column=0, sticky="w", padx=10, pady=5)

        value_label = tk.Label(user_details_pane, text=value, font=("Helvetica", 12), fg="blue", anchor="e")
        value_label.grid(row=row, column=1, sticky="e", padx=10, pady=0)

    # Keep a reference to prevent image from being garbage collected
    user_image = tk.PhotoImage(file='assets/images/user_image2.png')
    image_label = tk.Label(pane2, image=user_image)
    image_label.image = user_image  
    image_label.pack(side=tk.LEFT, padx=50)

def show_streaming_history():
     # Clear any existing widgets in pane2
    for widget in pane2.winfo_children():
        widget.destroy()

        # Create a new pane for streaming history
    streaming_history_pane = tk.Frame(pane2)
    streaming_history_pane.pack(fill=tk.BOTH, padx=10, pady=10)

    # Create buttons for sliding left and right
    left_button = tk.Button(streaming_history_pane, text="<", command=lambda: slide_history(-1))
    left_button.pack(side=tk.LEFT, padx=10)

    right_button = tk.Button(streaming_history_pane, text=">", command=lambda: slide_history(1))
    right_button.pack(side=tk.RIGHT, padx=10)

    # Create a canvas to hold the album images and song details
    canvas = tk.Canvas(streaming_history_pane, width=1200, height=200)
    canvas.pack(pady=10)

    # Calculate the total number of streaming items and the number of items per page
    total_items = len(streamingHistory)
    items_per_page = 5

    def slide_history(direction):
        nonlocal current_page
        new_page = current_page + direction
        if 0 <= new_page <= total_items // items_per_page:
            current_page = new_page
            update_streaming_items()

    def update_streaming_items():
        canvas.delete("all")  # Clear the canvas

        start_index = current_page * items_per_page
        end_index = min(start_index + items_per_page, total_items)

        for i in range(start_index, end_index):
            item = streamingHistory[i]

            # Create a frame for each streaming item
            item_frame = tk.Frame(canvas, width=200, height=200)
            canvas.create_window((i - start_index) * 230, 0, window=item_frame, anchor=tk.NW)

            # Create an image label for the album image
            album_image_file_path = "assets/images/ualbum_image"+str(random.randint(0, 9))+".png"
            album_image = tk.PhotoImage(file=album_image_file_path)
            album_label = tk.Label(item_frame, image=album_image)
            album_label.image = album_image
            album_label.pack()

            # Create a label for song details
            song_name = item["trackName"]
            truncated_song_name = song_name[:20] + "..." if len(song_name) > 20 else song_name
            song_label = tk.Label(item_frame, text=truncated_song_name)
            song_label.pack()

    current_page = 0
    update_streaming_items()
    

# Create header panes
pane1 = tk.Frame(root, width=1260, height=70)
pane1.pack(fill=tk.BOTH, padx=25, pady=25)
# pane1['background'] = 'yellow'

# Create input field
input_field = tk.Entry(pane1, width=80, font=("Helvetica", 12))
input_field.insert(0, "Search for the song")
input_field.pack(side=tk.LEFT, anchor=tk.CENTER, padx=(25,0), pady=25,  ipady=5, )
# Bind Enter key press event to input field
input_field.bind("<Return>", on_song_search)
# Create Search button
search_button = tk.Button(pane1, text="Search", command=on_song_search, height=2)
search_button.pack(side=tk.LEFT, anchor=tk.CENTER)

# Create user detail button
button = tk.Button(pane1, text="User", command=user_home_handler,  width=10, height=2)
button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=25, pady=25)


# Create details panes
pane2 = tk.Frame(root, width=1260, height=250)
pane2.pack(fill=tk.BOTH, padx=25, pady=25)
# pane2['background'] = 'blue'



# Create history panes
pane3 = tk.Frame(root, width=1260, height=250)
pane3.pack(fill=tk.BOTH, padx=25, pady=25)
pane3['background'] = 'red'


# Start the main event loop
show_streaming_history()
root.mainloop()