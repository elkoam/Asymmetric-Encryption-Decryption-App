import os
import rsa
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets


class  MyGUI(QMainWindow):
    
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("mygui.ui", self)
        
        self.show()

        self.GenerateKeys.clicked.connect(self.KeysGen)
        self.BrowsePriKey.clicked.connect(self.BrowseKeyFn)
        self.BrowseFile.clicked.connect(self.BrowseFileFn)
        self.EncryptBtn.clicked.connect(self.EncryptFn)
        self.DecryptBtn.clicked.connect(self.DecryptFn)
        # self.SignKeyBtn.clicked.connect(self.SelectPrivateKeyFn)
        # self.SignMsgBtn.clicked.connect(self.SelectMessageFn)
        # self.SignMessage.clicked.connect(self.SignMessageFn)
        # self.VerifyKeyBtn.clicked.connect(self.VerifyKeyBtnFn)
        # self.BrowseSgnBtn.clicked.connect(self.BrowseSgnBtnFn)
        # self.VerifyMessageBtn.clicked.connect(self.VerifyMessageBtnFn)

    def KeysGen(self):
        public_key, private_key = rsa.newkeys(2048)

        save_folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select a folder to save the file")
        if save_folder_path:
            public_key_path = os.path.join(save_folder_path, "public.pem")
            with open(public_key_path, "wb") as f:
                f.write(public_key.save_pkcs1("PEM"))

            private_key_path = os.path.join(save_folder_path, "private.pem")
            with open(private_key_path, "wb") as f:
                f.write(private_key.save_pkcs1("PEM"))


    def BrowseKeyFn(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select your public key for encryption")
        self.KeyPath.setText(filepath)

    def BrowseFileFn(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select your the file to be encrypted")
        self.FilePath.setText(filepath)


    def EncryptFn(self):
        filepath1 = self.KeyPath.text()
        filepath2 = self.FilePath.text()

        with open(filepath1 ,"rb") as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())

        with open(filepath2 ,"rb") as f:
            message = f.read()

        encrypted_message =rsa.encrypt(message , public_key)
        
        save_filepath, _ = QtWidgets.QFileDialog.getSaveFileName(self,"Save the encrypted file")
        with open(save_filepath ,"wb") as TheEncryptedFile:
            TheEncryptedFile.write(encrypted_message)

    def DecryptFn(self):
        filepath1 = self.KeyPath.text()
        filepath2 = self.FilePath.text()

        with open(filepath1 ,"rb") as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())

        with open(filepath2 ,"rb") as f:
            en_message = f.read()

        decrypted_message =rsa.decrypt(en_message , private_key)
        
        save_filepath, _ = QtWidgets.QFileDialog.getSaveFileName(self,"Save the encrypted file")
        with open(save_filepath ,"wb") as TheEncryptedFile:
            TheEncryptedFile.write(decrypted_message)

    # def SelectPrivateKeyFn(self):
    #     filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select your private key in order to sign your message")
    #     self.SignKeypath.setText(filepath)

    # def SelectMessageFn(self):
    #     filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select the message you want to sign")
    #     self.SignMsgPath.setText(filepath)


    # def SignMessageFn(self):
    #     filepath1 = self.SignKeypath.text()
    #     filepath2 = self.SignMsgPath.text()

    #     with open(filepath1 ,"rb") as f:
    #         private_key = rsa.PrivateKey.load_pkcs1(f.read())

    #     with open(filepath2 ,"rb") as f:
    #         message = f.read()

    #     signature = rsa.sign(message , private_key , "SHA-256")

    #     # with open("signature", "wb") as f:
    #     #     f.write(signature)

    #     save_filepath, _ = QtWidgets.QFileDialog.getSaveFileName(self,"Save your signature")
    #     with open(save_filepath ,"wb") as ThesignatureFile:
    #         ThesignatureFile.write(signature)

    # def VerifyKeyBtnFn(self):
    #     filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select the public key for verification purpose")
    #     self.VerifyKeyPath.setText(filepath)

    # def BrowseSgnBtnFn(self):
    #     filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select the signature for verification purpose")
    #     self.SignPath.setText(filepath)

    # def VerifyMessageBtnFn(self):
    #     filepath1 = self.SignKeypath.text()
    #     filepath2 = self.SignMsgPath.text()

    #     with open(filepath1 ,"rb") as f:
    #         public_key = rsa.PrivateKey.load_pkcs1(f.read())

    #     with open(filepath2 ,"rb") as f:
    #         signature = f.read()
        
    #     rsa.verify(message , )






def main():
        app = QApplication([])
        window = MyGUI()
        app.exec_()


if __name__ == '__main__':
    main()
