# Flash Card App with Automatic Card Flip and Learning Buttons

This flash card app allows users to learn French words in a dynamic manner. The app displays a French word, and the card automatically flips every 3 seconds, revealing the English translation. Users can also click on the "Wrong" or "Right" buttons to indicate whether they knew the translation or not. This helps users discover words they didn't know and reinforces words they already knew.

## How to Use

1. Ensure that you have the necessary dependencies installed, including `tkinter` and `pandas`.
2. Run the provided Python script.
3. Observe the flash card displaying a French word.
4. Wait for the card to automatically flip every 3 seconds to reveal the English translation.
5. Click the "Wrong" or "Right" buttons to indicate whether you knew the translation or not.

## Code Overview

The app is built using Python and the `tkinter` library for the graphical user interface. It also utilizes the `pandas` library to read French words from a CSV file and present them as flash cards.

The main components of the code include:
- Loading French words from a CSV file using `pandas`.
- Displaying the French word on the canvas.
- Automatically flipping the card every 3 seconds to reveal the English translation.
- Learning buttons to indicate whether the user knew the translation or not.
- Saving words you did not know into a new file (saving progress in words_to_learn.csv) 
- Visual elements such as buttons and background images to enhance the user experience.

- The code provides a simple and interactive way for users to learn and practice French vocabulary with a dynamic learning experience.
- To extend the functionality of this flash card app, users can modify the code to add new features or customize the existing ones.<br><br>For example:<br>
&emsp; users can add new buttons to the interface to provide additional functionality, such as a "Hint" button that displays a picture or a sentence to help users remember the translation.<br>&emsp;Users can also modify the code to load words from a different CSV file or database, or to support different languages.<br>&emsp;The possibilities are endless, and users can use this code as a starting point to build their own flash card apps for different purposes and domains.

## Acknowledgement

#100 Days of Code (Udemy's python course by Dr. Angela Yu).<br>
Here is the link to the course -> <a href="https://www.udemy.com/course/100-days-of-code/">link!</a>
