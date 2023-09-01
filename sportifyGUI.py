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
root.resizable(False, False)
root['padx'] = 10
root['pady'] = 10

# Header Pane Related event handlers
def user_home_handler():
    if home_button["text"] == "Home":
        home_button["text"] = "User"
        streaming_history_pane_label["text"] = "Streaming History"
        show_streaming_history(currentStreamingHistory)
    else:
        home_button["text"] = "Home"
        streaming_history_pane_label["text"] = "User Deatils"
        show_user_details()

#  Handler for song search
def on_song_search(event=None):
    input_text = search_input_field.get()
    if(input_text !=''):
        currentStreamingHistory = [item for item in lastStreamingHistory if input_text.lower() in item["artistName"].lower() or input_text.lower() in item["trackName"].lower()]
    else:
        currentStreamingHistory = lastStreamingHistory
    show_streaming_history(currentStreamingHistory)

# Handler for showing User details
def show_user_details():
    for widget in streaming_history_sub_pane.winfo_children():
        widget.destroy()
    user_details_pane = tk.Frame(streaming_history_sub_pane,  padx=50, pady=20)
    user_details_pane.pack( side=tk.RIGHT, anchor=tk.CENTER, padx=50 )
    labels = [
        ("Username:", userData["username"]),
        ("Email:", userData["email"]),
        ("Country:", userData["country"]),
        ("Birthdate:", userData["birthdate"]),
        ("Gender:", userData["gender"]),
        ("Creation Time:", userData["creationTime"])
    ]
    for row, (label_text, value) in enumerate(labels):
        label = tk.Label(user_details_pane, text=label_text, font=("Helvetica", 12))
        label.grid(row=row, column=0, sticky="w", padx=10, pady=5)
        value_label = tk.Label(user_details_pane, text=value, font=("Helvetica", 12), fg="blue", anchor="e")
        value_label.grid(row=row, column=1, sticky="e", padx=10, pady=0)
    user_image = tk.PhotoImage(file='assets/images/user_image2.png')
    image_label = tk.Label(streaming_history_sub_pane, image=user_image)
    image_label.image = user_image  
    image_label.pack(side=tk.LEFT, padx=50)

# Handler for showing streaming history
def show_streaming_history(currentStreamingHistory):
    for widget in streaming_history_sub_pane.winfo_children():
        widget.destroy()
    streaming_history_pane = tk.Frame(streaming_history_sub_pane)
    streaming_history_pane.pack(fill=tk.BOTH, padx=10, pady=10)
    left_button = tk.Button(streaming_history_pane, text="<", command=lambda: slide_history(-1))
    left_button.pack(side=tk.LEFT, padx=10)
    right_button = tk.Button(streaming_history_pane, text=">", command=lambda: slide_history(1))
    right_button.pack(side=tk.RIGHT, padx=10)
    canvas = tk.Canvas(streaming_history_pane, width=1200, height=200)
    canvas.pack(pady=10)
    total_items = len(currentStreamingHistory)
    items_per_page = 5

    # Slide direction handler
    def slide_history(direction):
        nonlocal current_page
        new_page = current_page + direction
        if 0 <= new_page <= total_items // items_per_page:
            current_page = new_page
            update_streaming_items()

    # update inferences
    def update_streaming_items():
        canvas.delete("all") 
        start_index = current_page * items_per_page
        end_index = min(start_index + items_per_page, total_items)
        for i in range(start_index, end_index):
            item = currentStreamingHistory[i]
            item_frame = tk.Frame(canvas, width=200, height=200)
            canvas.create_window((i - start_index) * 230, 0, window=item_frame, anchor=tk.NW)
            album_image_file_path = "assets/images/ualbum_image"+str(random.randint(0, 9))+".png"
            album_image = tk.PhotoImage(file=album_image_file_path)
            album_label = tk.Label(item_frame, image=album_image)
            album_label.image = album_image
            album_label.pack()
            song_name = item["trackName"]
            truncated_song_name = song_name[:20] + "..." if len(song_name) > 20 else song_name
            song_label = tk.Label(item_frame, text=truncated_song_name)
            song_label.pack()
    current_page = 0
    update_streaming_items()    

def show_inference():
    for widget in category_sub_pane.winfo_children():
        widget.destroy()
    playlist = inferences["inferences"]
    fav_playlist = [item for item in playlist if "1P" in item]
    other_playlist = [item for item in playlist if "3P" in item]
    favorite_pane = tk.Frame(category_sub_pane, width=600, height=180)
    favorite_pane_label = tk.Label(favorite_pane, text="Favourite", font=("Helvetica", 10))
    favorite_pane_label.pack(side=tk.TOP, anchor=tk.W, padx=10)
    favorite_pane.grid(row=0, column=0, padx=10, pady=10)
    other_pane = tk.Frame(category_sub_pane, width=600, height=180)
    other_pane_label = tk.Label(other_pane, text="Others", font=("Helvetica", 10))
    other_pane_label.pack(side=tk.TOP, anchor=tk.W, padx=40)
    other_pane.grid(row=0, column=1, padx=10, pady=10)
    left_button = tk.Button(other_pane, text="<", command=lambda: slide_playlist(-1))
    left_button.pack(side=tk.LEFT, padx=10)
    right_button = tk.Button(other_pane, text=">", command=lambda: slide_playlist(1))
    right_button.pack(side=tk.RIGHT, padx=10)
    canvas = tk.Canvas(other_pane, width=900, height=200)
    canvas.pack(pady=0, padx=2)
    # Slide direction handler
    def slide_playlist(direction):
        nonlocal current_page
        new_page = current_page + direction
        if 0 <= new_page <= total_items // items_per_page:
            current_page = new_page
            # update_streaming_items2(favorite_pane, fav_playlist)
            update_inferences(other_pane, other_playlist, TRUE)
    # update inferences
    def update_inferences(pane, playlist, is_slide_applicable=FALSE):
        if(is_slide_applicable):
            canvas.delete("all")  # Clear the canvas
            start_index = current_page * items_per_page
            end_index = min(start_index + items_per_page, total_items)
        else:
            start_index = 0
            end_index = len(playlist)
        for i in range(start_index, end_index):
            item_frame = tk.Frame(pane, width=180, height=180)
            if(is_slide_applicable):
                canvas.create_window((i - start_index) * 240, 0, window=item_frame, anchor=tk.NW)
            else:
                item_frame.pack(side=tk.LEFT, padx=10)
            icon_image_file_path = "assets/images/ply.png"
            icon_image = tk.PhotoImage(file=icon_image_file_path)
            icon_label = tk.Label(item_frame, image=icon_image)
            icon_label.image = icon_image
            icon_label.pack()
            playlist_name = playlist[i][3:]
            truncated_playlist_name = playlist_name[:20] + "..." if len(playlist_name) > 20 else playlist_name
            song_label = tk.Label(item_frame, text=truncated_playlist_name)
            song_label.pack()
    current_page = 0
    total_items = len(other_playlist)
    items_per_page = 4
    update_inferences(favorite_pane, fav_playlist)
    update_inferences(other_pane, other_playlist, TRUE)



# Create header panes
header_pane = tk.Frame(root, width=1260, height=70)
header_pane.pack(fill=tk.BOTH, padx=25, pady=25)

search_input_field = tk.Entry(header_pane, width=80, font=("Helvetica", 12))
search_input_field.insert(0, "Search for the song")
search_input_field.pack(side=tk.LEFT, anchor=tk.CENTER, padx=(25,0), pady=25,  ipady=5, )
search_input_field.bind("<Return>", on_song_search)

search_button = tk.Button(header_pane, text="Search", command=on_song_search, height=2)
search_button.pack(side=tk.LEFT, anchor=tk.CENTER)
home_button = tk.Button(header_pane, text="User", command=user_home_handler,  width=10, height=2)
home_button.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=25, pady=25)

streaming_history_pane = tk.Frame(root, width=1260, height=20)
streaming_history_pane.pack(fill=tk.BOTH, padx=2, pady=2)
streaming_history_pane_label = tk.Label(streaming_history_pane, text="Streaming History", font=("Helvetica", 14))
streaming_history_pane_label.pack(side=tk.TOP, anchor=tk.W, padx=30)
streaming_history_sub_pane = tk.Frame(root, width=1260, height=230)
streaming_history_sub_pane.pack(fill=tk.BOTH, padx=15, pady=(5,10))

category_pane = tk.Frame(root, width=1260, height=20)
category_pane.pack(fill=tk.BOTH, padx=2, pady=2)
category_pane_label = tk.Label(category_pane, text="Inferred Playlists", font=("Helvetica", 14))
category_pane_label.pack(side=tk.TOP, anchor=tk.W, padx=30)
category_sub_pane = tk.Frame(root, width=1260, height=230)
category_sub_pane.pack(fill=tk.BOTH, padx=15, pady=(5,10))

show_streaming_history(currentStreamingHistory)
show_inference()
root.mainloop()