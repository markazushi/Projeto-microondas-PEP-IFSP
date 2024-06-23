import os
import sys
import mplcursors
import matplotlib
import numpy as np
matplotlib.use('QtAgg')
os.environ['QT_API'] = 'PyQt6'
import matplotlib.pyplot as plt
from PyQt6 import QtCore, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QErrorMessage, QWidget, QTabWidget

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
        self.widget1.setGeometry(QtCore.QRect(60, 40, 1780, 150))
        self.widget1.setObjectName("widget1")

        # Layout de grade
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # Adiciona e nomeia os objetos
        self.add_labels()
        self.add_line_edits()
        self.add_button()

        # Área do gráfico com abas
        self.tab_widget = QTabWidget(self.centralwidget)
        self.tab_widget.setGeometry(QtCore.QRect(50, 200, 1800, 800))
        self.tab_widget.setObjectName("tab_widget")

        self.graph_widgets = []
        self.figures = []
        self.canvases = []

        nome_graf = ["Parte real da impedancia ao longo da linha",
                     "Parte imaginaria da impedancia ao longo da linha",
                     "Modulo da impedancia ao longo da linha",
                     "Tensão ao longo da linha",
                     "Corrente ao longo da linha",
                     ]

        for i in range(5):
            graph_widget = QWidget()
            graph_layout = QVBoxLayout(graph_widget)
            figure = Figure()
            canvas = FigureCanvas(figure)
            toolbar = NavigationToolbar(canvas, graph_widget)
            graph_layout.addWidget(toolbar)
            graph_layout.addWidget(canvas)
            self.tab_widget.addTab(graph_widget, nome_graf[i])
            self.graph_widgets.append(graph_widget)
            self.figures.append(figure)
            self.canvases.append(canvas)

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
            ("per_d", "Distância (m):"),
            ("per_zo", "Impedância do cabo (ohms):"),
            ("per_C", "Capacitância do cabo (F/m):"),
            ("per_L", "Indutância do cabo (H/m):"),
            ("per_f", "Frequência (Hz):"),
            ("per_zl", "Impedância da carga (ohms):"),
            ("per_vi", "Tensão sobre a carga (V):"),
            ("per_pts", "Numero de pontos (padrão 1000):"),
            ("label_omega", "Omega (rad/s):"),
            ("label_beta", "Beta (rad/m):"),
            ("label_lg", "Comp. de onda (m):"),
            ("label_vp", "Vel. de propagação (m/s):"),
            ("label_vg", "Vel. de grupo (m/s):"),
            ("label_gamma_L", "Coef. de reflexão (ads):"),
            ("label_tao", "Coef. de refração (ads):"),
            ("label_SWR", "Coef. SWR (ads):")
        ]

        positions = [
            (0, 0), (0, 3), (0, 6), (0, 9), (2, 0), (2, 3), (2, 6), (2, 9),
            (0, 12), (0, 15), (0, 18), (0, 21), (2, 12), (2, 15), (2, 18), (2, 21)
        ]
        
        for (name, text), pos in zip(labels_text, positions):
            label = QtWidgets.QLabel(self.widget1)
            label.setObjectName(name)
            label.setText(text)
            self.gridLayout.addWidget(label, *pos, 1, 3)

    def add_line_edits(self):
    # Adiciona os campos de entrada ao layout
        self.line_edits = {}
        line_edits_names = ["res_d", "res_zo", "res_C", "res_L", "res_f", "res_vi", "res_pts"]
        positions = [(1, 0), (1, 3), (1, 6), (1, 9), (3, 0), (3, 6), (3, 9)]

        for name, pos in zip(line_edits_names, positions):
            line_edit = QtWidgets.QLineEdit(self.widget1)
            line_edit.setObjectName(name)
            self.gridLayout.addWidget(line_edit, *pos, 1, 3)
            self.line_edits[name] = line_edit

        # Ajuste os campos de entrada para a impedância da carga
        impedance_layout = QtWidgets.QHBoxLayout()
        
        line_edit_real = QtWidgets.QLineEdit(self.widget1)
        line_edit_real.setObjectName("prt_real")
        impedance_layout.addWidget(line_edit_real)
        self.line_edits["prt_real"] = line_edit_real

        label_sep = QtWidgets.QLabel(self.widget1)
        label_sep.setObjectName("sep")
        label_sep.setText("+ j")
        label_sep.adjustSize()
        impedance_layout.addWidget(label_sep)

        line_edit_imag = QtWidgets.QLineEdit(self.widget1)
        line_edit_imag.setObjectName("prt_imag")
        impedance_layout.addWidget(line_edit_imag)
        self.line_edits["prt_imag"] = line_edit_imag

        self.gridLayout.addLayout(impedance_layout, 3, 3, 1, 3)


    def add_button(self):
        # Adiciona o botão ao layout
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Calcular")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 24)
        self.pushButton.clicked.connect(self.calcular)

    def retranslateUi(self):
        # Define os textos dos elementos da interface
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Programa de cálculo de ondas - PEP-IFSP"))

    def calcular(self):
        try:
            # Recupera os valores dos campos de entrada
            d = float(self.line_edits["res_d"].text())
            zo = float(self.line_edits["res_zo"].text())
            C = float(self.line_edits["res_C"].text()) * d
            L = float(self.line_edits["res_L"].text()) * d
            f = float(self.line_edits["res_f"].text())
            zl = complex(float(self.line_edits["prt_real"].text()), float(self.line_edits["prt_imag"].text()))
            vi = float(self.line_edits["res_vi"].text())

            # Verifica se o campo 'res_pts' está vazio e define um valor padrão
            pts_text = self.line_edits["res_pts"].text()
            if pts_text.strip() == "":
                pts = 1000
            else:
                pts = int(pts_text)

            # Realiza os cálculos
            omega = 2 * np.pi * f
            beta = omega * np.sqrt(L * C)
            lambda_g = 2 * np.pi / beta
            vp = 1 / np.sqrt(L * C)
            vg = vp
            gamma_L = (zl - zo) / (zl + zo)
            tao = gamma_L + 1
            SWR = (1 + gamma_L) / (1 - gamma_L)
            dt = np.linspace(0, d, pts)
            itens = np.linspace(0, 10, 100)
            zd = zo*((zl+1j*zo*np.tan(beta*dt))/(zo+1j*zl*np.tan(beta*dt)))

            # Verifica se algum dos valores é negativo
            if any(x < 0 for x in [d, zo, C, L, f, vi, pts]):
                raise ValueError()
            
            # Apresenta os resultados
            res_text = [
                omega, beta, lambda_g, vp, vg, gamma_L, tao, SWR
            ]

            res_positions = [
                (1, 12), (1, 15), (1, 18), (1, 21), (3, 12), (3, 15), (3, 18), (3, 21)
            ]

            for i, (value, pos) in enumerate(zip(res_text, res_positions)):
                if self.result_labels[i] is None:
                    label = QtWidgets.QLabel(self.widget1)
                    label.setObjectName(f"res_label_{i}")
                    self.gridLayout.addWidget(label, *pos, 1, 3)
                    self.result_labels[i] = label
                self.result_labels[i].setText(f'{value:.3e}')

            # Limpa as figuras atuais
            for figure in self.figures:
                figure.clear()

            # Cria os subplots e plota os resultados em cada aba
            ax1 = self.figures[0].add_subplot(111)
            ax2 = self.figures[1].add_subplot(111)
            ax3 = self.figures[2].add_subplot(111)
            ax4 = self.figures[3].add_subplot(111)
            ax5 = self.figures[4].add_subplot(111)

            ax1.plot(dt, np.real(zd), label='Parte Real', color='red')
            ax1.grid()
            ax1.set_title('Impedância ao longo da linha')
            ax1.set_xlabel('$d [m]$')
            ax1.set_ylabel('$Z (d) [\Omega]$')
            ax1.legend(loc='upper right')

            ax2.plot(dt, np.imag(zd), label='Parte Imaginária', color='blue')
            ax2.grid()
            ax2.set_title('Impedância ao longo da linha')
            ax2.set_xlabel('$d [m]$')
            ax2.set_ylabel('$Z (d) [\Omega]$')
            ax2.legend(loc='upper right')

            ax3.plot(dt, np.sqrt(np.real(zd)**2 + np.imag(zd)**2), label='Módulo', color='green')
            ax3.grid()
            ax3.set_title('Impedância ao longo da linha')
            ax3.set_xlabel('$d [m]$')
            ax3.set_ylabel('$Z (d) [\Omega]$')
            ax3.legend(loc='upper right')

            for t in itens:                         # calculando a amplitude da onda (tensão e corrente) no ponto d
                v = vi*(np.cos(beta*dt)+gamma_L*np.cos(beta*dt))*np.cos(2*np.pi*t)-vi*(np.sin(beta*dt)-gamma_L*np.sin(beta*dt))*np.sin(2*np.pi*t)
                ax4.plot(dt,np.real(v),linestyle = 'dotted')
                i = (vi/zo)*np.cos(2*np.pi*t+beta*dt)-(vi/zo)*gamma_L*np.cos(2*np.pi*t-beta*dt)
                ax5.plot(dt,np.real(i),linestyle = 'dotted')
            
            envoltoria_v = vi*(1+(gamma_L**2)+2*gamma_L*np.cos(2*beta*dt))**(1/2)
            ax4.plot(dt,np.real(envoltoria_v), label='envoltória +', linewidth = '3.0')
            ax4.plot(dt,np.real(-envoltoria_v), label='envoltória -', linewidth = '3.0')

            envoltoria_i = (vi/zo)*np.sqrt((1+(gamma_L**2)-2*gamma_L*np.cos(2*beta*dt)))
            ax5.plot(dt,np.real(envoltoria_i), label='envoltória +', linewidth = '3.0')
            ax5.plot(dt,np.real(-envoltoria_i), label='envoltória -', linewidth = '3.0')

            ax4.grid()
            ax4.set_title('Tensão ao longo da linha')
            ax4.set_xlabel('$d [m]$')
            ax4.set_ylabel('$v (d,t) [V]$')
            ax4.legend(loc='right')

            ax5.grid()
            ax5.set_title('Corrente ao longo da linha')
            ax5.set_xlabel('$d [m]$')
            ax5.set_ylabel('$i (d,t) [A]$')
            ax5.legend(loc='right')

            # Adiciona o cursor interativo para cada gráfico
            for ax in [ax1, ax2, ax3, ax4, ax5]:
                cursor = mplcursors.cursor(ax, hover=True)
                @cursor.connect("add")
                def on_add(sel):
                    x, y = sel.target
                    sel.annotation.set(text=f"x: {x:.3e}, y: {y:.3e}", fontsize=10, ha="center")

            # Arruma o layout
            for figure in self.figures:
                figure.tight_layout()
                for ax in figure.axes:
                    ax.autoscale(enable=True, axis='x', tight=True)

            # Atualiza os canvases com as novas figuras
            for canvas in self.canvases:
                canvas.draw()

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
