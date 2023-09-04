# PriOSS : Sportify Sample GUI Project

This is a simple GUI project for a music streaming application called "Sportify." It provides a user interface for searching songs, viewing streaming history, and displaying inferred playlists. The project is implemented using Python and the Tkinter library for the graphical user interface.

## Table of Contents
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Snapshots](#snapshots)

## Project Overview

Sportify Sample is a basic music streaming application that allows users to perform the following actions:

- Search for streaming songs.
- View streaming history.
- Display inferred playlists.

## Prerequisites

Before running the project, make sure you have the following prerequisites installed on your system:

- Python 3.x: You can download Python from [python.org](https://www.python.org/downloads/).

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/arjanoop/PriOSS.git
   ```

2. Navigate to the project directory:

   ```bash
   cd PriOSS
   ```

3. Install the required dependencies:

   ```bash
   pip install tk
   ```

4. Run the application:

   ```bash
   python sportifyGUI.py
   ```

## Usage

1. Upon running the application, you will see the Sportify Sample GUI.
2. You can use the search field to search for songs. Press the "Search" button or press Enter to initiate the search.
3. The "User" button in the header allows you to switch between the user's home and streaming history views.
4. The streaming history view displays a list of songs with album images and song names.
5. In the "Inferred Playlists" section, you can view favorite and other playlists.

## Project Structure

The project's file structure is as follows:

- `sportifyGUI.py`: The main Python script that initializes and runs the Tkinter GUI.
- `sampledata/`: Directory containing sample JSON data files for user data, streaming history, and inferences.
- `assets/`: Directory containing images used in the GUI.
- `screenshot/`: Directory containing images of application GUI.
- `README.md`: This readme file.

## Contributing

Contributions are welcome! If you want to improve this project or fix any issues, please submit a pull request.

## Snapshots

Main Screen [Streaming History & Inferred Playlist]
![main_screen1](https://github.com/arjanoop/PriOSS/blob/master/screenshot/main_screen1.png)

User Details
![user_details1](https://github.com/arjanoop/PriOSS/blob/master/screenshot/User_details1.png)

Streaming History Filter
![streaming_history_filter1](https://github.com/arjanoop/PriOSS/blob/master/screenshot/streaming_history_filter1.png)

Streaming History Scroll 
![streaming_history_scroll1](https://github.com/arjanoop/PriOSS/blob/master/screenshot/streaming_history_scroll1.png)
