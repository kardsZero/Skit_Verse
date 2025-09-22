import qrcode
data = "https://kardszero.github.io/Skit_Verse/skitVerse.html"
img = qrcode.make(data)
img.save("skitqr.jpg")
