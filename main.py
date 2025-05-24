import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,  QPushButton,QLineEdit,QMessageBox
import qrcode
from qrcode import QRCode 
import qrcode.constants

class Qrcodedisplay(QMainWindow):
     def __init__(self):
          super().__init__()
          self.setWindowTitle("QR Code Generator")
          self.setGeometry(0,0,500,102)
          self.setFixedSize(500, 102)
          self.dataTextField = QLineEdit(self)
          self.genaratebutton = QPushButton("Generate ",self)
          self.initUI()

     def initUI(self):
          self.dataTextField.setGeometry(0,0,400,100)
          self.dataTextField.setPlaceholderText("Enter Data to generate QR code")
          self.genaratebutton.setGeometry(400,0,100,100)
          self.genaratebutton.clicked.connect(self.func)
          self.setStyleSheet("""QPushButton{ font-size: 20px;
                                             border: 1px solid;
                                             border-radius: 10px;
                                             font-family: cooper Black;
                                             background-color: hsl(176, 92%, 49%);
                             }
                             QPushButton:hover{
                              background-color: hsl(176, 92%, 69%)
                             }
                             QLineEdit{ font-size: 20px;
                                        background-color: hsl(176, 100%, 100%);
                                        border: 1px solid;
                                        border-radius: 10px;
                                       
                             }""")

     def func(self):
          data=self.dataTextField.text().strip()

          if not data:
                 QMessageBox.warning(self, "Input Error", "Please enter some data to generate the QR code.")
                 return


          qrc=QRCode(version=1, 
           error_correction=qrcode.constants.ERROR_CORRECT_Q,
           box_size=10,
           border=5)

          

          qrc.add_data(data)

          qrc.make(fit=True)

          img=qrc.make_image(fill_color='black', back_color='white')
          img.show()
          
          
if __name__ == "__main__":
          app = QApplication(sys.argv)
          qrcodedisplay = Qrcodedisplay()
          qrcodedisplay.show()
          sys.exit(app.exec_())
