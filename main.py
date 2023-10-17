# TEE PELI TÄHÄN
import random
import pygame

class Rahapeli():
    def __init__(self) -> None:
    # Määritetään muuttujia
        pygame.init()
        self.naytto = pygame.display.set_mode((640, 480))
        self.lataa_kuvat()
        self.raha_x = random.randint(0,640-self.kolikko.get_width())
        self.raha_y = random.randint(0,460-self.kolikko.get_height())
        self.robo_x = 0
        self.robo_y = 480-self.robo.get_height()
        self.hirvio1_x = 0
        self.hirvio1_y = 100
        self.hirvio2_x = 640-self.hirvio.get_width()
        self.hirvio2_y = 300
        self.hirvio1_nopeus = 1
        self.hirvio2_nopeus = 1
        self.robo_nopeus = 1.5
        self.ylos = False
        self.alas = False
        self.vasen = False
        self.oikea = False
        self.pisteet = 0
        self.osuma = False
        self.kello = pygame.time.Clock()
        pygame.display.set_caption("Rahapeli")
        self.silmukka()
    
    # Toimitetaan hirviö 1 paikka
    def get_hirvio1_x(self):
        return self.hirvio1_x
    
    # Liikutetaan hirviö 1 sivuttais suunnassa
    def liikuta_hirvio1_x(self):
        self.hirvio1_x+=self.hirvio1_nopeus
        return self.hirvio1_x
    
    # Toimitetaan hirviö 2 paikka
    def get_hirvio2_x(self):
        return self.hirvio2_x
    
    # Liikutetaan hirviö 2 sivuttais suunnassa
    def liikuta_hirvio2_x(self):
        self.hirvio2_x+=self.hirvio2_nopeus
        return self.hirvio2_x
    
    # Lisätään pistemäärää
    def lisää_piste(self):
        self.pisteet+=1
        return self.pisteet
    
    # Toimitetaan pistemäärä
    def get_pisteet(self):
        return self.pisteet
    
    # Lisätään vaikeusastetta (hirviöt nopeutuvat, myös robotti nopeutuu, jos saadaan riittävästi pisteitä)
    def vaikeusaste(self):
        if self.hirvio1_nopeus > 0:
            self.hirvio1_nopeus+=0.5
        else:
            self.hirvio1_nopeus-=0.5
        if self.hirvio2_nopeus > 0:
            self.hirvio2_nopeus+=0.5
        else:
            self.hirvio2_nopeus-=0.5
        if self.get_pisteet()>=5 and self.get_pisteet()<10:
            self.robo_nopeus=2.5
        if self.get_pisteet()>=10 and self.get_pisteet()<15:
            self.robo_nopeus=3.5

    # Ladataan tarvittavat kuvat
    def lataa_kuvat(self):
        self.kolikko = pygame.image.load("kolikko.png")
        self.hirvio = pygame.image.load("hirvio.png")
        self.robo = pygame.image.load("robo.png")
    
    # Siirretään kuvia tarvittaviin suuntiin
    def siirra_kuvat(self):
        if self.robo_x>0 and self.vasen:
            self.robo_x-=self.robo_nopeus
        if self.robo_x<640-self.robo.get_width() and self.oikea:
            self.robo_x+=self.robo_nopeus
        if self.robo_y>0 and self.ylos:
            self.robo_y-=self.robo_nopeus
        if self.robo_y<480-self.robo.get_height() and self.alas:
            self.robo_y+=self.robo_nopeus
        self.liikuta_hirvio1_x()
        self.liikuta_hirvio2_x()
        if self.hirvio1_nopeus > 0 and self.get_hirvio1_x()+self.hirvio.get_width() >= 640:
            self.hirvio1_nopeus = -self.hirvio1_nopeus
        if self.hirvio1_nopeus < 0 and self.get_hirvio1_x() <= 0:
            self.hirvio1_nopeus = -self.hirvio1_nopeus
        if self.hirvio2_nopeus > 0 and self.get_hirvio2_x()+self.hirvio.get_width() >= 640:
            self.hirvio2_nopeus = -self.hirvio2_nopeus
        if self.hirvio2_nopeus < 0 and self.get_hirvio2_x() <= 0:
            self.hirvio2_nopeus = -self.hirvio2_nopeus
    
    # Tarkistetaan tuleeko osumia rahaan tai hirviöihin
    def osumat(self):
        if ((self.robo_x+self.robo.get_width()/2)-(self.raha_x+self.kolikko.get_width()/2) < 40 and (self.robo_y+self.robo.get_height()/2)-(self.raha_y+self.kolikko.get_height()/2) < 63 and (self.raha_x+self.kolikko.get_width()/2)-(self.robo_x+self.robo.get_width()/2) < 40 and (self.raha_y+self.kolikko.get_height()/2)-(self.robo_y+self.robo.get_height()/2) < 63):
            self.raha_x = random.randint(0,640-self.kolikko.get_width())
            self.raha_y = random.randint(0,460-self.kolikko.get_height())
            self.lisää_piste()
            self.vaikeusaste()
        if ((self.robo_x+self.robo.get_width()/2)-(self.hirvio1_x+self.hirvio.get_width()/2) < 38 and (self.robo_y+self.robo.get_height()/2)-(self.hirvio1_y+self.hirvio.get_height()/2) < 72 and (self.hirvio1_x+self.hirvio.get_width()/2)-(self.robo_x+self.robo.get_width()/2) < 38 and (self.hirvio1_y+self.hirvio.get_height()/2)-(self.robo_y+self.robo.get_height()/2) < 72):
            self.osuma = True
            self.hirvio1_nopeus = 0
            self.hirvio2_nopeus = 0
            self.robo_nopeus = 0
            return self.osuma
        if ((self.robo_x+self.robo.get_width()/2)-(self.hirvio2_x+self.hirvio.get_width()/2) < 38 and (self.robo_y+self.robo.get_height()/2)-(self.hirvio2_y+self.hirvio.get_height()/2) < 72 and (self.hirvio2_x+self.hirvio.get_width()/2)-(self.robo_x+self.robo.get_width()/2) < 38 and (self.hirvio2_y+self.hirvio.get_height()/2)-(self.robo_y+self.robo.get_height()/2) < 72):
            self.osuma = True
            self.hirvio1_nopeus = 0
            self.hirvio2_nopeus = 0
            self.robo_nopeus = 0
            return self.osuma
    
    # Pyöritetään peliä silmukassa
    def silmukka(self):
        while True:
            self.tutki_tapahtumat()
            self.siirra_kuvat()
            self.piirra_naytto()
            self.osumat()
            self.kello.tick(60)
    
    # Rekisteröidään tiettyjen nappien painaminen ja ikkunan sulkeminen
    def tutki_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_UP:
                    self.ylos = True
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = True
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasen = True
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikea = True
                if tapahtuma.key == pygame.K_F2:
                    Rahapeli()
                if tapahtuma.key == pygame.K_ESCAPE:
                    exit()
            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_UP:
                    self.ylos = False
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = False
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasen = False
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikea = False
            if tapahtuma.type == pygame.QUIT:
                exit()
    
    # Piirretään krafiikat näytölle
    def piirra_naytto(self):
        self.naytto.fill((192,192,192))
        self.naytto.blit(self.robo, (self.robo_x, self.robo_y))
        self.naytto.blit(self.kolikko, (self.raha_x, self.raha_y))
        self.naytto.blit(self.hirvio, (self.get_hirvio1_x(), self.hirvio1_y))
        self.naytto.blit(self.hirvio, (self.get_hirvio2_x(), self.hirvio2_y))
        fontti = pygame.font.SysFont("Arial", 24)
        self.uusipeli_teksti = fontti.render("F2 = Uusi peli   ESC = Lopetus", True, (255, 0, 0))
        self.pisteet_teksti = fontti.render("Pisteet: "+str(self.get_pisteet()), True, (255, 0, 0))
        self.naytto.blit(self.uusipeli_teksti, (20, 0))
        self.naytto.blit(self.pisteet_teksti, (530, 0))
        if self.osuma:
            fontti2 = pygame.font.SysFont("Arial", 60)
            self.gameover = fontti2.render("Game Over!", True, (255, 0, 0))
            self.naytto.blit(self.gameover, (190, 200))
        pygame.display.flip()

# Käynnistetään peli
if __name__ == "__main__":
    Rahapeli()