# Journal!

**16 May - Figured out how to fetch .epub files!**

I finally figured out how to fetch books from Zlibrary, in plain python. I want to run this on an ESP32 , running MicroPython, so I can't use any libraries other than the ones packaged with it. The first library I'd found was [this one](https://github.com/sertraline/zlibrary), which is async. I'd initially considered the idea of using a Pi Zero to host a server to fetch the books, which'd work with this, however, this particular library wouldn't work when it came to fetching urls no matter what I'd do, so I had to look for other ways.

After this, I found a [library](https://github.com/bipinkrish/Zlibrary-API) which used the Zlibrary API, and could run in MicroPython, which means I can now embed the ability to search for and download books straight into the E-Reader! Tried out the download and search functionality on my laptop as well. I plan on doing this on the sprig to check if it works later.

**Time Spent - ~2 hours, 15 minutes**


