## How to use

This project depends on Clippi to know when matches are finished. To achieve this, setup a Clippi Automator that writes any amount of text to `C:\Users\[user]\Documents\clippifile.txt`, every time a match ends.

Clone the repository and activate the virtual python environment.

`.\Scripts\activate.bat`

Install the requirements.

`pip install -r requirements.txt`

Run the script, passing in your Slippi name as a parameter.

`python main.py NANO#493`