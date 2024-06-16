import os
import sys
import matplotlib
import numpy as np
matplotlib.use('QtAgg')
os.environ['QT_API'] = 'PyQt6'
from PyQt6 import QtCore, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QErrorMessage, QWidget

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        # Configura a janela principal
        self.setObjectName("MainWindow")
        self.showMaximized()  # Janela em fullscreen

        # Widget central
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(575, 50, 1225, 110))
        self.widget1.setObjectName("widget1")

        # Layout de grade
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # Adiciona e nomeia os objetos
        self.add_labels()
        self.add_line_edits()
        self.add_button()

        # Área do gráfico
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 200, 1800, 800))
        self.widget.setObjectName("widget")
        self.graphLayout = QVBoxLayout(self.widget)
        self.widget.setLayout(self.graphLayout)

        # Cria uma figura de matplotlib
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.graphLayout.addWidget(self.canvas)

        # Define o widget central e a barra de menu
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        
        # Barra de status
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # Inicializa os labels dos resultados como None
        self.result_labels = [None] * 8

        # Tradução da interface do usuário
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def add_labels(self):
        # Adiciona os labels ao layout
        labels_text = [
            ("label", "Capacitância do cabo (F/m):"),
            ("label_4", "Indutância do cabo (H/m):"),
            ("label_3", "Distância da carga ao ponto (m):"),
            ("label_6", "Impedância do cabo (ohms):"),
            ("label_2", "Tensão sobre a carga (V):"),
            ("label_5", "Impedância da carga (ohms):"),
            ("label_7", "Frequência (Hz):"),
            ("label_omega", "Omega:"),
            ("label_beta", "Beta:"),
            ("label_lg", "Lambda_g:"),
            ("label_vp", "Velocidade de fase (vp):"),
            ("label_vg", "Velocidade de grupo (vg):"),
            ("label_gamma_L", "Gamma_L:"),
            ("label_tao", "tao:"),
            ("label_SWR", "SWR:")
        ]

        positions = [(0, 0), (0, 1), (0, 2), (0, 3), (2, 0), (2, 1), (2, 2), (0, 5), (0, 6), (0, 7), (0, 8), (2, 5), (2, 6), (2, 7), (2, 8)]
        
        for (name, text), pos in zip(labels_text, positions):
            label = QtWidgets.QLabel(self.widget1)
            label.setObjectName(name)
            label.setText(text)
            self.gridLayout.addWidget(label, *pos, 1, 1)

    def add_line_edits(self):
        # Adiciona os campos de entrada ao layout
        self.line_edits = {}
        line_edits_names = ["lineEdit", "lineEdit_4", "lineEdit_3", "lineEdit_6", "lineEdit_2", "lineEdit_5", "lineEdit_7"]
        positions = [(1, 0), (1, 1), (1, 2), (1, 3), (3, 0), (3, 1), (3, 2)]
        
        for name, pos in zip(line_edits_names, positions):
            line_edit = QtWidgets.QLineEdit(self.widget1)
            line_edit.setObjectName(name)
            self.gridLayout.addWidget(line_edit, *pos, 1, 1)
            self.line_edits[name] = line_edit

    def add_button(self):
        # Adiciona o botão ao layout
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Calcular")
        self.gridLayout.addWidget(self.pushButton, 3, 3, 1, 1)
        self.pushButton.clicked.connect(self.calcular)

    def retranslateUi(self):
        # Define os textos dos elementos da interface
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Programa de cálculo de ondas - PEP-IFSP"))

    def calcular(self):
        try:
            # Recupera os valores dos campos de entrada
            d = float(self.line_edits["lineEdit_3"].text())
            zo = float(self.line_edits["lineEdit_6"].text())
            C = float(self.line_edits["lineEdit"].text()) * d
            L = float(self.line_edits["lineEdit_4"].text()) * d
            f = float(self.line_edits["lineEdit_7"].text())
            zl = float(self.line_edits["lineEdit_5"].text())
            vi = float(self.line_edits["lineEdit_2"].text())

            # Realiza os cálculos
            omega = 2 * np.pi * f
            beta = omega * np.sqrt(L * C)
            lambda_g = 2 * np.pi / beta
            vp = 1 / np.sqrt(L * C)
            vg = vp
            gamma_L = (zl - zo) / (zl + zo)
            tao = gamma_L + 1
            SWR = (1 + gamma_L) / (1 - gamma_L)
            dt = np.linspace(0, d, 1000)
            itens = np.linspace(0, 10, 100)
            zd = zo * ((zl + 1j * zo * np.tan(beta * dt)) / (zo + 1j * zl * np.tan(beta * dt)))
            
            # Apresenta os resultados
            res_text = [
                omega, beta, lambda_g, vp, vg, gamma_L, tao, SWR
            ]

            positions = [(1, 5), (1, 6), (1, 7), (1, 8), (3, 5), (3, 6), (3, 7), (3, 8)]
        
            for i, (value, pos) in enumerate(zip(res_text, positions)):
                if self.result_labels[i] is None:
                    label = QtWidgets.QLabel(self.widget1)
                    label.setObjectName(f"res_label_{i}")
                    self.gridLayout.addWidget(label, *pos, 1, 1)
                    self.result_labels[i] = label
                self.result_labels[i].setText(f'{value:.4f}')

            # Limpa a figura atual
            self.figure.clear()

            # Cria os subplots
            ax1 = self.figure.add_subplot(231)
            ax2 = self.figure.add_subplot(232)
            ax3 = self.figure.add_subplot(233)
            ax4 = self.figure.add_subplot(223)
            ax5 = self.figure.add_subplot(224)

            # Plota os resultados
            ax1.plot(dt, np.real(zd), label='Parte Real', color='red')
            ax1.grid()
            ax1.set_xlabel('$d [m]$')
            ax1.set_ylabel('$Z (d) [\Omega]$')
            ax1.legend(loc='upper right')

            ax2.plot(dt, np.sqrt(np.real(zd)**2 + np.imag(zd)**2), label='Módulo', color='green')
            ax2.grid()
            ax2.set_xlabel('$d [m]$')
            ax2.set_ylabel('$Z (d) [\Omega]$')
            ax2.legend(loc='upper right')

            ax3.plot(dt, np.imag(zd), label='Parte Imaginária', color='blue')
            ax3.grid()
            ax3.set_xlabel('$d [m]$')
            ax3.set_ylabel('$Z (d) [\Omega]$')
            ax3.legend(loc='upper right')

            for t in itens:
                v = vi * (np.cos(beta * dt) + gamma_L * np.cos(beta * dt)) * np.cos(2 * np.pi * t) - \
                    vi * (np.sin(beta * dt) - gamma_L * np.sin(beta * dt)) * np.sin(2 * np.pi * t)
                ax4.plot(dt, v, linestyle='dotted')
                i = (vi / zo) * np.cos(2 * np.pi * t + beta * dt * 2 * np.pi) - \
                    (vi / zo) * gamma_L * np.cos(2 * np.pi * t - beta * dt * 2 * np.pi)
                ax5.plot(dt, i, linestyle='dotted')

            envoltoria_v = vi * (1 + (gamma_L ** 2) + 2 * gamma_L * np.cos(2 * beta * dt)) ** (1 / 2)
            ax4.plot(dt, envoltoria_v, label='envoltória +', linewidth='3.0')
            ax4.plot(dt, -envoltoria_v, label='envoltória -', linewidth='3.0')

            envoltoria_i = (vi / zo) * np.sqrt((1 + (gamma_L ** 2) - 2 * gamma_L * np.cos(2 * beta * dt * 2 * np.pi)))
            ax5.plot(dt, envoltoria_i, label='envoltória +', linewidth='3.0')
            ax5.plot(dt, -envoltoria_i, label='envoltória -', linewidth='3.0')

            ax4.grid()
            ax4.set_xlabel('$d [m]$')
            ax4.set_ylabel('$v (d,t) [V]$')
            ax4.legend(loc='right')

            ax5.grid()
            ax5.set_xlabel('$d [m]$')
            ax5.set_ylabel('$i (d,t) [A]$')
            ax5.legend(loc='right')

            # Atualiza o canvas com a nova figura
            self.canvas.draw()

        except ValueError:
            # Exibe uma mensagem de erro se algum valor não puder ser convertido para float
            error_dialog = QErrorMessage()
            error_dialog.showMessage("Por favor, insira valores válidos em todos os campos.")
            error_dialog.exec()

def main():
    app = QApplication(sys.argv)
    mostrar = Janela()
    mostrar.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
