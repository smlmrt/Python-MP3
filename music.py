from random import choice

class music():
    def __init__(self, musicList = []):
        self.nowMusic = ""
        self.voice = 100
        self.musicList = musicList
        self.case = True

    
    def musicChoose(self):
        sayac = 1
        for sarki in self.musicList:
            print("{}){}".format(sayac,sarki))
            sayac += 1

        secilenSarki = int(input("Silmek istenilen sarki no: "))

        while secilenSarki < 1 or secilenSarki > len(self.musicList):
            secilenSarki = int(input("Silmek istenilen sarki nosunu doğru giriniz:(1-{}) ".format(self.musicList)))

        self.nowMusic = self.musicList[secilenSarki - 1]

    def voiceUp(self):
        if self.voice == 100:
            pass
        else:
            self.voice += 10

    def voiceDown(self):
        if self.voice == 0:
            pass
        else:
            self.voice -= 10

    def randomMusic(self):
        rsec = choice(self.musicList)
        self.nowMusic = rsec

    def addMusic(self):
        sanatci = input("sanatçıyı giriniz: ")
        sarki = input("Şarkıyı giriniz: ")

        self.musicList.append(sanatci + "--" + sarki)

    def deletemusic(self):
        sayac = 1
        for sarki in self.musicList:
            print("{}{}".format(sayac,sarki))
            sayac += 1

        silinecekSarki = int(input("Silmek istenilen sarki no: "))

        while silinecekSarki < 1 or silinecekSarki > len(self.musicList):
            silinecekSarki = int(input("Silmek istenilen sarki nosunu doğru giriniz:(1-{}) ".format(self.musicList)))

        self.musicList.pop(silinecekSarki-1)

    def close(self):
        self.case = False

    def showMenu(self):
        print("""
        Music List: {}
        The Son Playing: {}
        Voice: {}

        1.Select Song
        2.Voice Up
        3.Voice Down
        4.Random Song
        5.Add Song
        6.Delete Song
        7.Close
        """.format(self.musicList,self.nowMusic,self.voice))
    
    def select(self):
        sec = int(input("choose from 1 to 7: "))

        while sec < 1 or sec > 7 :
            sec = int(input("Wrong choose"))
        
        return sec

    def open(self):
        self.showMenu()
        select = self.select()

        if select == 1:
            self.musicChoose()
        if select == 2:
            self.voiceUp()
        if select == 3:
            self.voiceDown()
        if select == 4:
            self.randomMusic()
        if select == 5:
            self.addMusic()
        if select == 6:
            self.deletemusic()
        if select == 7:
            self.close()


mp3music = music()
while mp3music.case:
    mp3music.open()

print("Programming closing")