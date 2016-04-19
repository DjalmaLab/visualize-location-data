#Installation
1. sudo pip install matplotlib
2. download basemap http://matplotlib.org/basemap/users/installing.html Follow the instruction in the INSTALL file to configure, build and install 

#Get your google data
1. https://takeout.google.com/settings/takeout You only need to download Locations History

#how tor run.
1. Create a file called data.py in the root directory. 
2. The file should have the pase to your .json file you downloaded from google<br>
<code>
    google_location_data = "<filepath>"
</code>
3. Run python visualize.py
