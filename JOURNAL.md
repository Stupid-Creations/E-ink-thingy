# Journal!
**16 May - Figured out how to fetch .epub files!**

I finally figured out how to fetch books from Zlibrary, in plain python. I want to run this on an ESP32 , running MicroPython, so I can't use any libraries other than the ones packaged with it. The first library I'd found was [this one](https://github.com/sertraline/zlibrary), which is async. I'd initially considered the idea of using a Pi Zero to host a server to fetch the books, which'd work with this, however, this particular library wouldn't work when it came to fetching urls no matter what I'd do, so I had to look for other ways.

After this, I found a [library](https://github.com/bipinkrish/Zlibrary-API) which used the Zlibrary API, and could run in MicroPython, which means I can now embed the ability to search for and download books straight into the E-Reader! Tried out the download and search functionality on my laptop as well. I plan on doing this on the sprig to check if it works later.

**Time Spent - ~2 hours, 15 minutes**
#
**20 May: Parsing EPUB files is tough </3** 
Started off with the work I needed to do for the epub parser! The first thing I started off with today was figuring out how the epub file format works - after a few google searches, I figured out that epubs are just zipped HTML files! That was pretty cool to learn!

After this, I looked for libraries to make sure that unzipping files is actually possible in MicroPython, and found two libraries, though I am yet to check if they work with the epub files

Seeing that an implementation exists, I started making a basic HTML parser on my laptop in plain python using the zipfile library, and, after a lot of struggle, ended up with a basic HTML reader which could separate text from the HTML tags! I then realized I needed to parse the CSS part as well, so I started working on that. While making the CSS parser, I checked if all epubs follow the same internal structure, which they didn't, which meant I had to add the ability to find the html and css files manually </3

After this ordeal, I realized that my HTML parser was able to only deal with the one specific file I'd tested it on, and started to add ways to generalize it, but now it's 11 PM and my brain is on strike </3. I'll look at this tomorrow. Hoping to get a very very basic HTML file rendered from a zip on the sprig by tomorrow. 

![enter image description here](https://hc-cdn.hel1.your-objectstorage.com/s/v3/6fae25f4e452a0b4bf9ced82d558b286988bf749_image.png)
The broken HTML parser broken HTML parsing some HTML </3
**Time spent: 3.5 hours** 
