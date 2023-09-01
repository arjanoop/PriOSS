import json
import tkinter as tk
from tkinter import *
import random


with open("sampledata/Userdata.json", "r", encoding="utf-8") as json_file:
    userData = json.load(json_file)
with open("sampledata/StreamingHistory.json", "r", encoding="utf-8") as json_file:
    lastStreamingHistory = json.load(json_file)
    currentStreamingHistory = lastStreamingHistory
with open("sampledata/Inferences.json", "r", encoding="utf-8") as json_file:
    inferences = json.load(json_file)

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
        label2["text"] = "Streaming History"
        show_streaming_history(currentStreamingHistory)
    else:
        button["text"] = "Home"
        label2["text"] = "User Deatils"
        show_user_details()

def on_song_search(event=None):
    input_text = input_field.get()
    if(input_text !=''):
        currentStreamingHistory = [item for item in lastStreamingHistory if input_text.lower() in item["artistName"].lower() or input_text.lower() in item["trackName"].lower()]
    else:
        currentStreamingHistory = lastStreamingHistory
    show_streaming_history(currentStreamingHistory)

def show_user_details():
     # Clear any existing widgets in pane2
    for widget in pane2.winfo_children():
        widget.destroy()

    # Create a new pane for user details
    user_details_pane = tk.Frame(pane2,  padx=50, pady=20)
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

def show_streaming_history(currentStreamingHistory):
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
    total_items = len(currentStreamingHistory)
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
            item = currentStreamingHistory[i]

            # Create a frame for each streaming item
            item_frame = tk.Frame(canvas, width=200, height=200)
            canvas.create_window((i - start_index) * 230, 0, window=item_frame, anchor=tk.NW)

            # Create an image label for the album image
            album_image_file_path = "assets/images/ualbum_image"+str(random.randint(0, 9))+".png"
            album_image = tk.PhotoImage(file=album_image_file_path)
            album_label = tk.Label(item_frame, image=album_image)
            # album_label = tk.Button(item_frame, image=album_image, command=lambda item_frame=item_frame, item=item: flip_item(item_frame, item))
            album_label.image = album_image
            album_label.pack()

            # Create a label for song details
            song_name = item["trackName"]
            truncated_song_name = song_name[:20] + "..." if len(song_name) > 20 else song_name
            song_label = tk.Label(item_frame, text=truncated_song_name)
            song_label.pack()

    current_page = 0
    update_streaming_items()    

def show_inference():
    # Clear any existing widgets in pane3
    for widget in pane3.winfo_children():
        widget.destroy()
    
    playlist = inferences["inferences"]
    fav_playlist = [item for item in playlist if "1P" in item]
    other_playlist = [item for item in playlist if "3P" in item]

    # Create favorite and other panes within pane3
    favorite_pane = tk.Frame(pane3, width=600, height=180)
    favorite_pane_label = tk.Label(favorite_pane, text="Favourite", font=("Helvetica", 10))
    favorite_pane_label.pack(side=tk.TOP, anchor=tk.W, padx=10)
    favorite_pane.grid(row=0, column=0, padx=10, pady=10)

    other_pane = tk.Frame(pane3, width=600, height=180)
    other_pane_label = tk.Label(other_pane, text="Others", font=("Helvetica", 10))
    other_pane_label.pack(side=tk.TOP, anchor=tk.W, padx=40)
    other_pane.grid(row=0, column=1, padx=10, pady=10)

    # Create buttons for sliding left and right
    left_button = tk.Button(other_pane, text="<", command=lambda: slide_playlist(-1))
    left_button.pack(side=tk.LEFT, padx=10)

    right_button = tk.Button(other_pane, text=">", command=lambda: slide_playlist(1))
    right_button.pack(side=tk.RIGHT, padx=10)

    # Create a canvas to hold the album images and song details
    canvas = tk.Canvas(other_pane, width=900, height=200)
    canvas.pack(pady=0, padx=2)

    def slide_playlist(direction):
        nonlocal current_page
        new_page = current_page + direction
        if 0 <= new_page <= total_items // items_per_page:
            current_page = new_page
            # update_streaming_items2(favorite_pane, fav_playlist)
            update_streaming_items2(other_pane, other_playlist, TRUE)

    def update_streaming_items2(pane, playlist, is_slide_applicable=FALSE):

        if(is_slide_applicable):
            canvas.delete("all")  # Clear the canvas
            start_index = current_page * items_per_page
            end_index = min(start_index + items_per_page, total_items)
        else:
            start_index = 0
            end_index = len(playlist)


        for i in range(start_index, end_index):
            # Create a frame for each streaming item in the pane
            item_frame = tk.Frame(pane, width=180, height=180)
            if(is_slide_applicable):
                canvas.create_window((i - start_index) * 240, 0, window=item_frame, anchor=tk.NW)
            else:
                item_frame.pack(side=tk.LEFT, padx=10)  # Use pack
            # Create an image label for the icon
            icon_image_file_path = "assets/images/ply.png"
            icon_image = tk.PhotoImage(file=icon_image_file_path)
            icon_label = tk.Label(item_frame, image=icon_image)
            icon_label.image = icon_image
            icon_label.pack()

            # Create a label for song details
            playlist_name = playlist[i][3:]
            truncated_playlist_name = playlist_name[:20] + "..." if len(playlist_name) > 20 else playlist_name
            song_label = tk.Label(item_frame, text=truncated_playlist_name)
            song_label.pack()

    current_page = 0
    total_items = len(other_playlist)
    items_per_page = 4
    # Call the streaming items update function for each pane
    update_streaming_items2(favorite_pane, fav_playlist)
    update_streaming_items2(other_pane, other_playlist, TRUE)



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

pane2heading = tk.Frame(root, width=1260, height=20)
pane2heading.pack(fill=tk.BOTH, padx=2, pady=2)
# pane2heading['background'] = 'blue'
label2 = tk.Label(pane2heading, text="Streaming History", font=("Helvetica", 14))
label2.pack(side=tk.TOP, anchor=tk.W, padx=30)

# Create details panes
pane2 = tk.Frame(root, width=1260, height=230)
pane2.pack(fill=tk.BOTH, padx=15, pady=(5,10))
# pane2['background'] = 'yellow'

pane3heading = tk.Frame(root, width=1260, height=20)
pane3heading.pack(fill=tk.BOTH, padx=2, pady=2)
# pane3heading['background'] = 'red'
label3 = tk.Label(pane3heading, text="Inferred Playlists", font=("Helvetica", 14))
label3.pack(side=tk.TOP, anchor=tk.W, padx=30)
# Create history panes
pane3 = tk.Frame(root, width=1260, height=230)
pane3.pack(fill=tk.BOTH, padx=15, pady=(5,10))
# pane3['background'] = 'yellow'

# Start the main event loop
show_streaming_history(currentStreamingHistory)
show_inference()
root.mainloop()