# room-challenge

## Software challenge for decorating a room

Python program to compute the area of the floor, volume of paint required to paint the walls and volume of the room given the dimensions of the room. Assumes 2 coats of paint at 12sqm per litre.

## Installation

The application requires tkinter and Python 3, tkinter should be installed by default. \

Download the roomchallenge.py file and then from the command line in the download directory type command:

        python roomchallenge.py

The resulting window should be: 

![Main Page](images/frontpage.png)

## Example Usage

Insert positive real numbers into the entry boxes for height, width and depth. Press the calculate button and then the area, volume and quantity of paint required should be displayed at the bottom

For example: 

![Example Usage](images/example.png)

## Changlog

### [0.1.1] - 25-10-2017
- Updated README with installation, usage and changelog sections
- Ensured only positive values are accepted as dimensions of the room

### [0.1.0] - 25-10-2017
- Changed README to describe project
- Removed setup.py as nothing will be installed, only one file will run
- Implemented main functionality of roomchallenge, including the app window, button to calculate and the necessary entry and label widgets to perform such actions

### [0.0.1] - 25-10-2017
- Initial setup of readme, setup and roomchallenge files