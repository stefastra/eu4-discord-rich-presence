## Europa Universalis IV Discord Rich Presence Integration
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

> This little application shows Steam 'Rich Presence' data on your Discord profile.

![Preview](preview.png)

### What it does
- Shows exactly the steam provided rich presence data for your game
- Reads necessary data for it to work automatically
- Turns on and off along with the game .exe for a seamless experience [Coming soon]

### What it doesn't do
- If you have used multiple steam accounts on your machine, you may need to input your ID3 in the configuration file. It is the last digits after the ':' and can be found [here](https://www.steamidfinder.com/)

### Setup
- Use the provided installer. [Coming soon]
- ~~Subscribe to the mod on the Steam workshop.~~

### Test Build
While not the most elegant interface, it should work if you want to try out this program before it's complete.

### How it works
By reading your steam profile's ID3 from your installation directory, it is possible for a webscraper to get paradox's own rich presence data directly from your steam profile. After checking validity and it is then sent to discord using pypresence. Thankfully, doing things this way provides a much better result than what was done previously, which was actually opening and reading the latest autosave then parsing data from it. That was problematic in regards to encrypted ironman saves, so this new solution should be the final version of this app until EU5 comes around.
