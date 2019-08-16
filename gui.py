from PyQt5 import uic, QtWidgets

from firebase import auth, db
from data import User, LevelOfAccess, Book

class LoginUI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(LoginUI, self).__init__(parent)
        uic.loadUi('login.ui', self)

class CadastrarUsuario(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CadastrarUsuario, self).__init__(parent)
        uic.loadUi('TelaCadastrarUsuario.ui', self)

        self.pushButton_cadastrar.clicked.connect(self.save_to_firebase)

    def save_to_firebase(self):

        password = self.lineEdit_Senha.text()
        confimPassword = self.lineEdit_ConfirmarSenha.text()

        if password == confimPassword:
            email = self.lineEdit_Login.text()
            name = self.lineEdit_nome.text()
            cpf = self.lineEdit_CPF.text()

            #Remove dots and dashes from CPF
            from re import sub as re_sub
            cpf = re_sub('[.-]', '', cpf)

            user = User(email, name, cpf, LevelOfAccess.COMMON_USER)

            auth.create_user_with_email_and_password(email, password)
            db.child('users').push(user.to_dict())

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.NoIcon)
            msg.setText("Sucesso")
            msg.setInformativeText("Cadastrado com sucesso!")
            msg.setWindowTitle("Sucesso")
            msg.exec_()
        else:
            print("Erro")
        


class CadastrarLivro(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CadastrarLivro, self).__init__(parent)
        uic.loadUi('cadastrar_livro.ui', self)

        self.pushButton_cadastrar.clicked.connect(self.save_to_firebase)

    def save_to_firebase(self):

            
            titulo = self.lineEdit_titulo.text()
            numerodepaginas = self.lineEdit_numerodepaginas.text()
            isbn = self.lineEdit_ISBN.text()
            ano = self.lineEdit_ano.text()
            genero = self.lineEdit_Genero.text()
            descricao = self.lineEdit_descricao.text()
            autor = self.lineEdit_autor.text()

            if not(titulo == '' or numerodepaginas == '' or isbn == '' or  genero == '' or descricao == '' or autor == ''):


            #Remove dots and dashes from CPF
    
                book = Book(isbn, titulo, numerodepaginas, genero, descricao, ano, autor)

                db.child('books').push(book.to_dict())

                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.NoIcon)
                msg.setText("Sucesso")
                msg.setInformativeText("Cadastrado com sucesso!")
                msg.setWindowTitle("Sucesso")
                msg.exec_()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.NoIcon)
                msg.setText("Failure")
                msg.setInformativeText("Todos os campos são obrigatorios")
                msg.setWindowTitle("Failure")
                msg.exec_()
            
class EditarCadastro(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(EditarCadastro, self).__init__(parent)
        uic.loadUi('Editar_cadastro.ui', self)

class EditarLivro(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(EditarLivro, self).__init__(parent)
        uic.loadUi('atualizar_livro.ui', self)

class menuAdm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(menuAdm, self).__init__(parent)
        uic.loadUi('menuAdm.ui', self)
        
class AdmLivros(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AdmLivros, self).__init__(parent)
        uic.loadUi('adm_livros.ui', self)
        
class AdmUsuarios(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AdmUsuarios, self).__init__(parent)
        uic.loadUi('adm_usuarios.ui', self)