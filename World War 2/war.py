import sys, os
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import random

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

screen = resource_path("warGame.ui")

class War(QMainWindow):
    def __init__(self):
        super(War, self).__init__()
        uic.loadUi('warGame.ui', self)

        usFlag = QPixmap('img/USA.png')
        germanFlag = QPixmap('img/german.png')
        japanFlag = QPixmap('img/japan.png')
        sovietFlag = QPixmap('img/SU.png')
        ukFlag = QPixmap('img/UK.png')
        italyFlag = QPixmap('img/italy.png')

        self.unitedStatesFlag.setPixmap(usFlag)
        self.unitedKingdomFlag.setPixmap(ukFlag)
        self.sovietFlag.setPixmap(sovietFlag)
        self.germanFlag.setPixmap(germanFlag)
        self.italyFlag.setPixmap(italyFlag)
        self.japanFlag.setPixmap(japanFlag)

        self.alliedCountries = ['USA', 'UK', 'Soviet']
        self.axisCountries = ['Germany', 'Italy', 'Japan']
        
        self.axisCountriesScores = [960, 800, 780]
        self.alliedCountriesScores = [880, 840, 840]

        self.displayScores()

        self.playButton.clicked.connect(self.play)
        self.playButton.clicked.connect(self.defeatCheck)
        self.resetButton.clicked.connect(self.reset)

    # Reset function for the reset button. Whenever the game ends, or the user wants to restart.
    def reset(self):
        self.USAScore.setText(str(880))
        self.UKScore.setText(str(840))
        self.sovietScore.setText(str(840))
        self.germanScore.setText(str(960))
        self.japanScore.setText(str(800))
        self.italyScore.setText(str(780))

        self.USALabel.setStyleSheet("background-color: rgb(16, 48, 23);" + "color: rgb(176, 173, 177);")
        self.UKLabel.setStyleSheet("background-color: rgb(16, 48, 23);" + "color: rgb(176, 173, 177);")
        self.sovietLabel.setStyleSheet("background-color: rgb(16, 48, 23);" + "color: rgb(176, 173, 177);")
        self.germanLabel.setStyleSheet("background-color: rgb(16, 48, 23);" + "color: rgb(176, 173, 177);")
        self.japanLabel.setStyleSheet("background-color: rgb(16, 48, 23);" + "color: rgb(176, 173, 177);")
        self.italyLabel.setStyleSheet("background-color: rgb(16, 48, 23);" + "color: rgb(176, 173, 177);")
        
        self.USADefeat.setStyleSheet("background-color: rgba(255, 97, 71, 0);")
        self.UKDefeat.setStyleSheet("background-color: rgba(255, 97, 71, 0);")
        self.sovietDefeat.setStyleSheet("background-color: rgba(255, 97, 71, 0);")
        self.germanyDefeat.setStyleSheet("background-color: rgba(255, 97, 71, 0);")
        self.japanDefeat.setStyleSheet("background-color: rgba(255, 97, 71, 0);")
        self.italyDefeat.setStyleSheet("background-color: rgba(255, 97, 71, 0);")

        self.vsLabel.setStyleSheet('color: rgba(255, 255, 255, 0);')
        self.axisLabel.setText('')
        self.allyLabel.setText('')
        self.battleLog.setText('')

    # Displaying the score inside the country label, and rounding it the hundredth decimal place.
    def displayScores(self):
        self.USAScore.setText(str(round(float(self.alliedCountriesScores[0]), 2)))
        self.UKScore.setText(str(round(float(self.alliedCountriesScores[1]), 2)))
        self.sovietScore.setText(str(round(float(self.alliedCountriesScores[2]), 2)))
        self.germanScore.setText(str(round(float(self.axisCountriesScores[0]), 2)))
        self.japanScore.setText(str(round(float(self.axisCountriesScores[1]), 2)))
        self.italyScore.setText(str(round(float(self.axisCountriesScores[2]), 2)))
        
    # 'Play' game function.
    def play(self):

        # Reseting the background color from the red and green background, which signifies loss or win.
        self.USALabel.setStyleSheet("background-color: rgb(16, 48, 23);" + "color: rgb(176, 173, 177);")
        self.UKLabel.setStyleSheet("background-color: rgb(16, 48, 23);" + "color: rgb(176, 173, 177);")
        self.sovietLabel.setStyleSheet("background-color: rgb(16, 48, 23);" + "color: rgb(176, 173, 177);")
        self.germanLabel.setStyleSheet("background-color: rgb(16, 48, 23);" + "color: rgb(176, 173, 177);")
        self.japanLabel.setStyleSheet("background-color: rgb(16, 48, 23);" + "color: rgb(176, 173, 177);")
        self.italyLabel.setStyleSheet("background-color: rgb(16, 48, 23);" + "color: rgb(176, 173, 177);")

        # Choosing one country from the allied and axis side to do battle.
        axis = random.choice(self.axisCountries)
        allies =  random.choice(self.alliedCountries)

        # The attack rating is determined by taking the country's attack rating, dividing it by ten, and then picking a random number between 0 and the dividend. Which ever country has the highest resulting number is the one who wins.
        if allies == 'USA':
            alliesAttack = float(self.USAScore.text())/10
        elif allies == 'UK':
            alliesAttack = float(self.UKScore.text())/10
        elif allies == 'Soviet':
            alliesAttack = float(self.sovietScore.text())/10

        if axis == 'Germany':
            axisAttack = float(self.germanScore.text())/10
        elif axis == 'Japan':
            axisAttack = float(self.japanScore.text())/10
        elif axis == 'Italy':
            axisAttack = float(self.italyScore.text())/10

        axiAttack = random.randint(0,int(axisAttack))
        allyAttack = random.randint(0,int(alliesAttack))

        # In case of a tie between attack scores.
        if allyAttack == axiAttack and axis == 'Germany' and allies == 'USA':
            self.germanScore.setText(str(float(self.germanScore.text()) - 20))
            self.USAScore.setText(str(float(self.USAScore.text()) - 20))
            self.germanLabel.setStyleSheet("background-color: #aa0000;")
            self.USALabel.setStyleSheet("background-color: #00aa00;")
        elif allyAttack == axiAttack and axis == 'Germany' and allies == 'UK':
            self.germanScore.setText(str(float(self.germanScore.text()) - 20))
            self.UKScore.setText(str(float(self.UKScore.text()) - 20))
            self.germanLabel.setStyleSheet("background-color: #aa0000;")
            self.UKLabel.setStyleSheet("background-color: #00aa00;")
        elif allyAttack == axiAttack and axis == 'Germany' and allies == 'Soviet':
            self.germanScore.setText(str(float(self.germanScore.text()) - 20))
            self.sovietScore.setText(str(float(self.sovietScore.text()) - 20))
            self.germanLabel.setStyleSheet("background-color: #aa0000;")
            self.sovietLabel.setStyleSheet("background-color: #00aa00;")

        elif allyAttack == axiAttack and axis == 'Japan' and allies == 'USA':
            self.japanScore.setText(str(float(self.japanScore.text()) - 20))
            self.USAScore.setText(str(float(self.USAScore.text()) - 20))
            self.japanLabel.setStyleSheet("background-color: #aa0000;")
            self.USALabel.setStyleSheet("background-color: #00aa00;")
        elif allyAttack == axiAttack and axis == 'Japan' and allies == 'UK':
            self.japanScore.setText(str(float(self.japanScore.text()) - 20))
            self.UKScore.setText(str(float(self.UKScore.text()) - 20))
            self.japanLabel.setStyleSheet("background-color: #aa0000;")
            self.UKLabel.setStyleSheet("background-color: #00aa00;")
        elif allyAttack == axiAttack and axis == 'Japan' and allies == 'Soviet':
            self.japanScore.setText(str(float(self.japanScore.text()) - 20))
            self.sovietScore.setText(str(float(self.sovietScore.text()) - 20))
            self.japanLabel.setStyleSheet("background-color: #aa0000;")
            self.sovietLabel.setStyleSheet("background-color: #00aa00;")

        elif allyAttack == axiAttack and axis == 'Italy' and allies == 'USA':
            self.italyScore.setText(str(float(self.italyScore.text()) - 20))
            self.USAScore.setText(str(float(self.USAScore.text()) - 20))
            self.italyLabel.setStyleSheet("background-color: #aa0000;")
            self.USALabel.setStyleSheet("background-color: #00aa00;")
        elif allyAttack == axiAttack and axis == 'Italy' and allies == 'UK':
            self.italyScore.setText(str(float(self.italyScore.text()) - 20))
            self.UKScore.setText(str(float(self.UKScore.text()) - 20))
            self.italyLabel.setStyleSheet("background-color: #aa0000;")
            self.UKLabel.setStyleSheet("background-color: #00aa00;")
        elif allyAttack == axiAttack and axis == 'Italy' and allies == 'Soviet':
            self.italyScore.setText(str(float(self.italyScore.text()) - 20))
            self.sovietScore.setText(str(float(self.sovietScore.text()) - 20))
            self.italyLabel.setStyleSheet("background-color: #aa0000;")
            self.sovietLabel.setStyleSheet("background-color: #00aa00;")

        elif axiAttack == allyAttack and allies == 'USA' and axis == 'Germany':
            self.USAScore.setText(str(float(self.USAScore.text()) - 20))
            self.germanScore.setText(str(float(self.germanScore.text()) - 20))
            self.USALabel.setStyleSheet("background-color: #aa0000;")
            self.germanLabel.setStyleSheet("background-color: #00aa00;")
        elif axiAttack == allyAttack and allies == 'USA' and axis == 'Japan':
            self.USAScore.setText(str(float(self.USAScore.text()) - 20))
            self.japanScore.setText(str(float(self.japanScore.text()) - 20))
            self.USALabel.setStyleSheet("background-color: #aa0000;")
            self.japanLabel.setStyleSheet("background-color: #00aa00;")
        elif axiAttack == allyAttack and allies == 'USA' and axis == 'Italy':
            self.USAScore.setText(str(float(self.USAScore.text()) - 20))
            self.italyScore.setText(str(float(self.italyScore.text()) - 20))
            self.USALabel.setStyleSheet("background-color: #aa0000;")
            self.italyLabel.setStyleSheet("background-color: #00aa00;")

        elif axiAttack == allyAttack and allies == 'UK' and axis == 'Germany':
            self.UKScore.setText(str(float(self.UKScore.text()) - 20))
            self.germanScore.setText(str(float(self.germanScore.text()) - 20))
            self.UKLabel.setStyleSheet("background-color: #aa0000;")
            self.germanLabel.setStyleSheet("background-color: #00aa00;")
        elif axiAttack == allyAttack and allies == 'UK' and axis == 'Japan':
            self.UKScore.setText(str(float(self.UKScore.text()) - 20))
            self.japanScore.setText(str(float(self.japanScore.text()) - 20))
            self.UKLabel.setStyleSheet("background-color: #aa0000;")
            self.japanLabel.setStyleSheet("background-color: #00aa00;")
        elif axiAttack == allyAttack and allies == 'UK' and axis == 'Italy':
            self.UKScore.setText(str(float(self.UKScore.text()) - 20))
            self.italyScore.setText(str(float(self.italyScore.text()) - 20))
            self.UKLabel.setStyleSheet("background-color: #aa0000;")
            self.italyLabel.setStyleSheet("background-color: #00aa00;")

        elif axiAttack == allyAttack and allies == 'Soviet' and axis == 'Germany':
            self.sovietScore.setText(str(float(self.sovietScore.text()) - 20))
            self.germanScore.setText(str(float(self.germanScore.text()) - 20))
            self.sovietLabel.setStyleSheet("background-color: #aa0000;")
            self.germanLabel.setStyleSheet("background-color: #00aa00;")
        elif axiAttack == allyAttack and allies == 'Soviet' and axis == 'Japan':
            self.sovietScore.setText(str(float(self.sovietScore.text()) - 20))
            self.japanScore.setText(str(float(self.japanScore.text()) - 20))
            self.sovietLabel.setStyleSheet("background-color: #aa0000;")
            self.japanLabel.setStyleSheet("background-color: #00aa00;")
        elif axiAttack == allyAttack and allies == 'Soviet' and axis == 'Italy':
            self.sovietScore.setText(str(float(self.sovietScore.text()) - 20))
            self.italyScore.setText(str(float(self.italyScore.text()) - 20))
            self.sovietLabel.setStyleSheet("background-color: #aa0000;")
            self.italyLabel.setStyleSheet("background-color: #00aa00;")

        # The majority of cases will come from this section, in which one country out of the two that are battling, will have a higher number than the other.
        elif allyAttack > axiAttack and axis == 'Germany' and allies == 'USA':
            self.germanScore.setText(str(float(self.germanScore.text()) - allyAttack))
            self.USAScore.setText(str(float(self.USAScore.text()) - (axiAttack/20)))
            self.germanLabel.setStyleSheet("background-color: #aa0000;")
            self.USALabel.setStyleSheet("background-color: #00aa00;")
        elif allyAttack > axiAttack and axis == 'Germany' and allies == 'UK':
            self.germanScore.setText(str(float(self.germanScore.text()) - allyAttack))
            self.UKScore.setText(str(float(self.UKScore.text()) - (axiAttack/20)))
            self.germanLabel.setStyleSheet("background-color: #aa0000;")
            self.UKLabel.setStyleSheet("background-color: #00aa00;")
        elif allyAttack > axiAttack and axis == 'Germany' and allies == 'Soviet':
            self.germanScore.setText(str(float(self.germanScore.text()) - allyAttack))
            self.sovietScore.setText(str(float(self.sovietScore.text()) - (axiAttack/20)))
            self.germanLabel.setStyleSheet("background-color: #aa0000;")
            self.sovietLabel.setStyleSheet("background-color: #00aa00;")

        elif allyAttack > axiAttack and axis == 'Japan' and allies == 'USA':
            self.japanScore.setText(str(float(self.japanScore.text()) - allyAttack))
            self.USAScore.setText(str(float(self.USAScore.text()) - (axiAttack/20)))
            self.japanLabel.setStyleSheet("background-color: #aa0000;")
            self.USALabel.setStyleSheet("background-color: #00aa00;")
        elif allyAttack > axiAttack and axis == 'Japan' and allies == 'UK':
            self.japanScore.setText(str(float(self.japanScore.text()) - allyAttack))
            self.UKScore.setText(str(float(self.UKScore.text()) - (axiAttack/20)))
            self.japanLabel.setStyleSheet("background-color: #aa0000;")
            self.UKLabel.setStyleSheet("background-color: #00aa00;")
        elif allyAttack > axiAttack and axis == 'Japan' and allies == 'Soviet':
            self.japanScore.setText(str(float(self.japanScore.text()) - allyAttack))
            self.sovietScore.setText(str(float(self.sovietScore.text()) - (axiAttack/20)))
            self.japanLabel.setStyleSheet("background-color: #aa0000;")
            self.sovietLabel.setStyleSheet("background-color: #00aa00;")

        elif allyAttack > axiAttack and axis == 'Italy' and allies == 'USA':
            self.italyScore.setText(str(float(self.italyScore.text()) - allyAttack))
            self.USAScore.setText(str(float(self.USAScore.text()) - (axiAttack/20)))
            self.italyLabel.setStyleSheet("background-color: #aa0000;")
            self.USALabel.setStyleSheet("background-color: #00aa00;")
        elif allyAttack > axiAttack and axis == 'Italy' and allies == 'UK':
            self.italyScore.setText(str(float(self.italyScore.text()) - allyAttack))
            self.UKScore.setText(str(float(self.UKScore.text()) - (axiAttack/20)))
            self.italyLabel.setStyleSheet("background-color: #aa0000;")
            self.UKLabel.setStyleSheet("background-color: #00aa00;")
        elif allyAttack > axiAttack and axis == 'Italy' and allies == 'Soviet':
            self.italyScore.setText(str(float(self.italyScore.text()) - allyAttack))
            self.sovietScore.setText(str(float(self.sovietScore.text()) - (axiAttack/20)))
            self.italyLabel.setStyleSheet("background-color: #aa0000;")
            self.sovietLabel.setStyleSheet("background-color: #00aa00;")

        elif axiAttack > allyAttack and allies == 'USA' and axis == 'Germany':
            self.USAScore.setText(str(float(self.USAScore.text()) - axiAttack))
            self.germanScore.setText(str(float(self.germanScore.text()) - (allyAttack/20)))
            self.USALabel.setStyleSheet("background-color: #aa0000;")
            self.germanLabel.setStyleSheet("background-color: #00aa00;")
        elif axiAttack > allyAttack and allies == 'USA' and axis == 'Japan':
            self.USAScore.setText(str(float(self.USAScore.text()) - axiAttack))
            self.japanScore.setText(str(float(self.japanScore.text()) - (allyAttack/20)))
            self.USALabel.setStyleSheet("background-color: #aa0000;")
            self.japanLabel.setStyleSheet("background-color: #00aa00;")
        elif axiAttack > allyAttack and allies == 'USA' and axis == 'Italy':
            self.USAScore.setText(str(float(self.USAScore.text()) - axiAttack))
            self.italyScore.setText(str(float(self.italyScore.text()) - (allyAttack/20)))
            self.USALabel.setStyleSheet("background-color: #aa0000;")
            self.italyLabel.setStyleSheet("background-color: #00aa00;")

        elif axiAttack > allyAttack and allies == 'UK' and axis == 'Germany':
            self.UKScore.setText(str(float(self.UKScore.text()) - axiAttack))
            self.germanScore.setText(str(float(self.germanScore.text()) - (allyAttack/20)))
            self.UKLabel.setStyleSheet("background-color: #aa0000;")
            self.germanLabel.setStyleSheet("background-color: #00aa00;")
        elif axiAttack > allyAttack and allies == 'UK' and axis == 'Japan':
            self.UKScore.setText(str(float(self.UKScore.text()) - axiAttack))
            self.japanScore.setText(str(float(self.japanScore.text()) - (allyAttack/20)))
            self.UKLabel.setStyleSheet("background-color: #aa0000;")
            self.japanLabel.setStyleSheet("background-color: #00aa00;")
        elif axiAttack > allyAttack and allies == 'UK' and axis == 'Italy':
            self.UKScore.setText(str(float(self.UKScore.text()) - axiAttack))
            self.italyScore.setText(str(float(self.italyScore.text()) - (allyAttack/20)))
            self.UKLabel.setStyleSheet("background-color: #aa0000;")
            self.italyLabel.setStyleSheet("background-color: #00aa00;")

        elif axiAttack > allyAttack and allies == 'Soviet' and axis == 'Germany':
            self.sovietScore.setText(str(float(self.sovietScore.text()) - axiAttack))
            self.germanScore.setText(str(float(self.germanScore.text()) - (allyAttack/20)))
            self.sovietLabel.setStyleSheet("background-color: #aa0000;")
            self.germanLabel.setStyleSheet("background-color: #00aa00;")
        elif axiAttack > allyAttack and allies == 'Soviet' and axis == 'Japan':
            self.sovietScore.setText(str(float(self.sovietScore.text()) - axiAttack))
            self.japanScore.setText(str(float(self.japanScore.text()) - (allyAttack/20)))
            self.sovietLabel.setStyleSheet("background-color: #aa0000;")
            self.japanLabel.setStyleSheet("background-color: #00aa00;")
        elif axiAttack > allyAttack and allies == 'Soviet' and axis == 'Italy':
            self.sovietScore.setText(str(float(self.sovietScore.text()) - axiAttack))
            self.italyScore.setText(str(float(self.italyScore.text()) - (allyAttack/20)))
            self.sovietLabel.setStyleSheet("background-color: #aa0000;")
            self.italyLabel.setStyleSheet("background-color: #00aa00;")

        # Setting the labels that tells the story of the battle.
        self.allyLabel.setText(allies)
        self.axisLabel.setText(axis)

        self.vsLabel.setStyleSheet('color: rgb(255, 255, 255);')

        # Setting the battle log which sums up the battle.
        if allyAttack > axiAttack:
            self.battleLog.setText(f'In this battle, {allies} faught against {axis}. It was hard faught, but {allies} came out on top. The score for the axis\' was {axiAttack} and {allyAttack} for the allies.')
        elif allyAttack < axiAttack:
            self.battleLog.setText(f'In this battle, {allies} faught against {axis}. It was hard faught, but {axis} came out on top. The score for the allies\' was {allyAttack} and {axiAttack} for the axis\'.')
        elif allyAttack == axiAttack:
            self.battleLog.setText(f'In this battle, {allies} faught against {axis}. It was hard faught, but the stalemate ended with no clear winner came out on top. Both sides ended up taking a beating of 20 points')

    # Checking if a country has a zero or negative score, and disabling that country.
    def defeatCheck(self):
        if float(self.USAScore.text()) <= 0 and "USA" in self.alliedCountries: 
            self.alliedCountries.remove('USA') 
            self.USADefeat.setStyleSheet("background-color: rgba(255, 97, 71, 74);")
        elif float(self.UKScore.text()) <= 0 and "UK" in self.alliedCountries:
            self.alliedCountries.remove('UK') 
            self.UKDefeat.setStyleSheet("background-color: rgba(255, 97, 71, 74);")
        elif float(self.sovietScore.text()) <= 0 and "Soviet" in self.alliedCountries:
            self.alliedCountries.remove('Soviet') 
            self.sovietDefeat.setStyleSheet("background-color: rgba(255, 97, 71, 74);")

        elif float(self.germanScore.text()) <= 0 and "Germany" in self.axisCountries:
            self.axisCountries.remove('Germany') 
            self.germanyDefeat.setStyleSheet("background-color: rgba(255, 97, 71, 74);")
        elif float(self.japanScore.text()) <= 0 and "Japan" in self.axisCountries:
            self.axisCountries.remove('Japan') 
            self.japanDefeat.setStyleSheet("background-color: rgba(255, 97, 71, 74);")
        elif float(self.italyScore.text()) <= 0 and "Italy" in self.axisCountries:
            self.axisCountries.remove('Italy') 
            self.italyDefeat.setStyleSheet("background-color: rgba(255, 97, 71, 74);")

        if len(self.alliedCountries) == 0:
            self.winLabel.setText('The axis countries win! Lord have mercy on our souls..')
            self.playButton.setEnabled(False)
        elif len(self.axisCountries) == 0:
            self.winLabel.setText('The allied countries win! Freedom prevails.')
            self.playButton.setEnabled(False)

        # Rounding the score to the nearest hundredth place, so that we dont get long repeating numbers like 
        # '9.577777777777777777777777'
        self.USAScore.setText(str(round(float(self.USAScore.text()), 2)))
        self.UKScore.setText(str(round(float(self.UKScore.text()), 2)))
        self.sovietScore.setText(str(round(float(self.sovietScore.text()), 2)))
        self.germanScore.setText(str(round(float(self.germanScore.text()), 2)))
        self.japanScore.setText(str(round(float(self.japanScore.text()), 2)))
        self.italyScore.setText(str(round(float(self.italyScore.text()), 2)))

app = QApplication(sys.argv)
war = War()
war.show()
app.exec_()