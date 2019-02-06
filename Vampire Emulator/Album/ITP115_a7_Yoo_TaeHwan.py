import pickle
# load the library
libraryFileName = "music_library.dat"
def loadLibrary(libraryFileName):
    fileIn = open(libraryFileName,"rb")
    libraryDictionary = pickle.load(fileIn)
    fileIn.close()
    return libraryDictionary

# save the library
def saveLibrary(libraryFileName, musicLibDct):
    fileOut = open(libraryFileName, "wb")
    pickle.dump(musicLibDct, fileOut)
    fileOut.close()

# display menu
def displayMenu():
    print("Welcome to the Music Library of ITP 115!")
    print("Options:")
    print(" 1) Display Library\n 2) Display all artists\n 3) Add an album\n 4) Delete an album \n 5) Delete an artist\n 6) Search Library\n 7) Exit")
# display library
def displayLibrary(musicLibDct):
    for artist in musicLibDct.keys():
        print("Artist: ", artist)
        artistAlbum = musicLibDct[artist]
        print("Albums:")
        for album in artistAlbum:
            print(album)
# display artist
def displayArtists(musicLibDct):
    for artist in musicLibDct.keys():
        print("- ",artist)
# add album
def addAlbum(musicLibDct):
    artistChoice = input("Please choose an artist: ")
    albumChoice = input("Please enter an album: ")
    if artistChoice not in musicLibDct.keys():
        musicLibDct[artistChoice] = [albumChoice]
    else:
        musicLibDct[artistChoice].append(albumChoice)

# delete album
def deleteAlbum(musicLibDct):
    artistChoice = input("Please choose an artist: ")
    albumChoice = input("Please enter an album: ")
    if artistChoice not in musicLibDct:
        print("Artist not in the library!")
        return False
    else:
        if albumChoice not in musicLibDct[artistChoice]:
            print("Album is not in the library! Failed to delete!")
            return False
        else:
            musicLibDct[artistChoice].remove(albumChoice)
            print("Album has been deleted!")
            return True

# delete artist
def deleteArtist(musicLibDct):
    artistChoice = input("Please choose an artist: ")
    if artistChoice not in musicLibDct:
        print("Artist not in the library! Erase failed! ")
        return False
    elif artistChoice in musicLibDct:
        del musicLibDct[artistChoice]
        print("Artist has been deleted!")
        return True
# search library
def searchLibrary(musicLibDct):
    search = input("To search, please put in a term: ")
    allArtists = []
    allAlbums = []
    allKeys = musicLibDct.keys()

    for artist in allKeys:
        if search.lower() in artist.lower():
            allArtists.append(artist)
        artistAlbum = musicLibDct[artist]
        for album in artistAlbum:
            if search.lower() in album.lower():
                allAlbums.append(album)
    print("These are all the Artists that match your term: ")
    for newArtists in allArtists:
        print(newArtists)
    print("These are all the Albums that match your term:")
    for newAlbums in allAlbums:
        print(newAlbums)
# Generate Random Playlist
def randomPlaylist(musicLibDct):
    print("This is your playlist!")
# main
def main():
    libraryDictionary = loadLibrary(libraryFileName)
    correctWord = True
    displayMenu()
    while correctWord:
        decisionChoice = input("Please choose an option:(1-7) ")
        if decisionChoice == "1":
            displayLibrary(libraryDictionary)
            displayMenu()
        elif decisionChoice == "2":
            displayArtists(libraryDictionary)
            displayMenu()
        elif decisionChoice == "3":
            addAlbum(libraryDictionary)
            displayMenu()
        elif decisionChoice == "4":
            deleteAlbum(libraryDictionary)
            displayMenu()
        elif decisionChoice == "5":
            deleteArtist(libraryDictionary)
            displayMenu()
        elif decisionChoice == "6":
            searchLibrary(libraryDictionary)
            displayMenu()
        elif decisionChoice == "7":
            print("Alright, goodbye! ")
            saveLibrary(libraryFileName, libraryDictionary)
            correctWord = False
        else:
            print("")

main()

