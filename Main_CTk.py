import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Prog(ctk.CTk):

    # inicialização #

    def __init__(self):
        super().__init__()
    
        # cabeçalho #
        
        dimx = (self.winfo_screenwidth()-450)
        dimy = (self.winfo_screenheight()-150)

        self.input_title = ctk.CTkLabel(self, text="\n - Dados iniciais - ", width=200, font=('Arial Narrow bold', 20))
        self.input_title.grid(row=0, column=0, columnspan=2, pady=0, padx=10)

        self.graphs_title = ctk.CTkLabel(self, text="\n - Gráficos gerados - ", width=dimx, font=('Arial Narrow bold', 20))
        self.graphs_title.grid(row=0, column=2, pady=0, padx=10)

        self.output_title = ctk.CTkLabel(self, text="\n - Resultados - ", width=200, font=('Arial Narrow bold', 20))
        self.output_title.grid(row=0, column=3, pady=0, padx=10)

        # espaço para os gráficos #

        self.graphs_box = ctk.CTkTabview(self, width=dimx, height=dimy, fg_color="#fff")
        self.graphs_box.place(x=230, y=50)

        self.graphs_box.add("Visão Geral")
        self.graphs_box.tab("Visão Geral").grid(row=0, column=1, pady=5, padx=20)

        self.graphs_box.add("Parte real da impedância")
        self.graphs_box.tab("Parte real da impedância").grid(row=0, column=2, pady=5, padx=20)
        
        self.graphs_box.add("Parte imaginária da impedância")
        self.graphs_box.tab("Parte imaginária da impedância").grid(row=0, column=3, pady=5, padx=20)
        
        self.graphs_box.add("Módulo da impedância")
        self.graphs_box.tab("Módulo da impedância").grid(row=0, column=4, pady=5, padx=20)
        
        self.graphs_box.add("Tensão")
        self.graphs_box.tab("Tensão").grid(row=0, column=5, pady=5, padx=20)
        
        self.graphs_box.add("Corrente")
        self.graphs_box.tab("Corrente").grid(row=0, column=6, pady=5, padx=20)
        
        # entradas #

        self.d_text = ctk.CTkLabel(self, text="\n Distância (em m) ", width=150, font=('Arial Narrow bold', 14))
        self.d_text.grid(row=1, column=0, columnspan=2, pady=5, padx=10)
        self.d_input = ctk.CTkEntry(self, width=150, font=('Arial Narrow', 14))
        self.d_input.grid(row=2, column=0, columnspan=2, pady=5, padx=10)

        self.zo_text = ctk.CTkLabel(self, text="\n Impedância do cabo (em ohm) ", width=150, font=('Arial Narrow bold', 14))
        self.zo_text.grid(row=3, column=0, columnspan=2, pady=5, padx=10)
        self.zo_input = ctk.CTkEntry(self, width=150, font=('Arial Narrow', 14))
        self.zo_input.grid(row=4, column=0, columnspan=2, pady=5, padx=10)

        self.C_text = ctk.CTkLabel(self, text="\n Capacitância do cabo (em F/m) ", width=150, font=('Arial Narrow bold', 14))
        self.C_text.grid(row=5, column=0, columnspan=2, pady=5, padx=10)
        self.C_input = ctk.CTkEntry(self, width=150, font=('Arial Narrow', 14))
        self.C_input.grid(row=6, column=0, columnspan=2, pady=5, padx=10)

        self.L_text = ctk.CTkLabel(self, text="\n Indutância do cabo (em H/m) ", width=150, font=('Arial Narrow bold', 14))
        self.L_text.grid(row=7, column=0, columnspan=2, pady=5, padx=10)
        self.L_input = ctk.CTkEntry(self, width=150, font=('Arial Narrow', 14))
        self.L_input.grid(row=8, column=0, columnspan=2, pady=5, padx=10)

        self.f_text = ctk.CTkLabel(self, text="\n Frequência (em Hz)", width=150, font=('Arial Narrow bold', 14))
        self.f_text.grid(row=9, column=0, columnspan=2, pady=5, padx=10)
        self.f_input = ctk.CTkEntry(self, width=150, font=('Arial Narrow', 14))
        self.f_input.grid(row=10, column=0, columnspan=2, pady=5, padx=10)

        self.zl_text = ctk.CTkLabel(self, text="\n Impedância da carga (em ohm) ", width=150, font=('Arial Narrow bold', 14))
        self.zl_text.grid(row=11, column=0, columnspan=2, pady=5, padx=10)
        self.zl_input_txt = ctk.CTkLabel(self, text="   + j ", width=75, font=('Arial Narrow bold', 14))
        self.zl_input_txt.grid(row=12, column=0, columnspan=2, pady=5, padx=10)
        self.zl_input_real = ctk.CTkEntry(self, width=75, font=('Arial Narrow', 14))
        self.zl_input_real.grid(row=12, column=0, pady=5, padx=0)
        self.zl_input_imag = ctk.CTkEntry(self, width=75, font=('Arial Narrow', 14))
        self.zl_input_imag.grid(row=12, column=1, pady=5, padx=0)

        self.vi_text = ctk.CTkLabel(self, text="\n Tensão sobre a carga (em V) ", width=150, font=('Arial Narrow bold', 14))
        self.vi_text.grid(row=13, column=0, columnspan=2, pady=5, padx=10)
        self.vi_input = ctk.CTkEntry(self, width=150, font=('Arial Narrow', 14))
        self.vi_input.grid(row=14, column=0, columnspan=2, pady=5, padx=10)

        self.pn_text = ctk.CTkLabel(self, text="\n Número de pontos (def 1000) ", width=150, font=('Arial Narrow bold', 14))
        self.pn_text.grid(row=15, column=0, columnspan=2, pady=5, padx=10)
        self.pn_input = ctk.CTkEntry(self, width=150, font=('Arial Narrow', 14))
        self.pn_input.grid(row=16, column=0, columnspan=2, pady=5, padx=10)
        
        self.x1_text = ctk.CTkLabel(self, text="\n Ponto de amostragem (x em m) ", width=150, font=('Arial Narrow bold', 14))
        self.x1_text.grid(row=17, column=0, columnspan=2, pady=5, padx=10)
        self.x1_input = ctk.CTkEntry(self, width=150, font=('Arial Narrow', 14))
        self.x1_input.grid(row=18, column=0, columnspan=2, pady=5, padx=10)

        # saídas #

        self.omega_text = ctk.CTkLabel(self, text="\n Ômega (em rad/s) ", width=150, font=('Arial Narrow bold', 14))
        self.omega_text.grid(row=1, column=3, pady=5, padx=10)

        self.beta_text = ctk.CTkLabel(self, text="\n Beta (em rad/m) ", width=150, font=('Arial Narrow bold', 14))
        self.beta_text.grid(row=3, column=3, pady=5, padx=10)
        
        self.lambdag_text = ctk.CTkLabel(self, text="\n Comp. de onda (em m) ", width=150, font=('Arial Narrow bold', 14))
        self.lambdag_text.grid(row=5, column=3, pady=5, padx=10)

        self.vp_text = ctk.CTkLabel(self, text="\n Vel. de propagação (em m/s) ", width=150, font=('Arial Narrow bold', 14))
        self.vp_text.grid(row=7, column=3, pady=5, padx=10)

        self.vg_text = ctk.CTkLabel(self, text="\n Vel. de grupo (em m/s) ", width=150, font=('Arial Narrow bold', 14))
        self.vg_text.grid(row=9, column=3, pady=5, padx=10)

        self.gammal_text = ctk.CTkLabel(self, text="\n Coef. de reflexão (ads) ", width=150, font=('Arial Narrow bold', 14))
        self.gammal_text.grid(row=11, column=3, pady=5, padx=10)

        self.tao_text = ctk.CTkLabel(self, text="\n Coef. de refração (ads) ", width=150, font=('Arial Narrow bold', 14))
        self.tao_text.grid(row=13, column=3, pady=5, padx=10)

        self.swr_text = ctk.CTkLabel(self, text="\n Coef. SWR (ads) ", width=150, font=('Arial Narrow bold', 14))
        self.swr_text.grid(row=15, column=3, pady=5, padx=10)
        
        # botão run #

        self.play = ctk.CTkButton(self, text="Calcular", font=('Arial Narrow bold', 20), command=self.calc).grid(rowspan=18, row=17, column=3, pady=20, padx=10)

    # caixa de diálogo - bugs #

    def error(self, *args, **kwargs):
        bug = ctk.CTkToplevel(self)
        bug.geometry = ("400x300")
        bug.title(" ERRO!")
        bug.resizable(False, False)
        
        warn_txt = ctk.CTkLabel(master = bug, text="\n Insira um número válido para as entradas! \n", width=400, font=('Arial Narrow bold', 14)).pack()
        check_btn = ctk.CTkButton(master = bug, text="Ok", font=('Arial Narrow bold', 16), command=bug.destroy).pack()
        trash_txt = ctk.CTkLabel(master = bug, text=" ", width=400, font=('Arial Narrow bold', 14)).pack()

        bug.focus_set()

        return bug

    # programa principal #

    def calc(self):

    # verificador de inputs

        if(self.d_input.get()==""):
            d = 0
        else:
            d = self.d_input.get()
        d = float(d)

        if(self.zo_input.get()==""):
            zo = 0
        else:
            zo = self.zo_input.get()
        zo = float(zo)

        if(self.C_input.get()==""):
            C = 0
        else:
            C = self.C_input.get()
        C = float(C)

        if(self.L_input.get()==""):
            L = 0
        else:
            L = self.L_input.get()
        L = float(L)

        if(self.f_input.get()==""):
            f = 0
        else:
            f = self.f_input.get()
        f = float(f)

        if(self.zl_input_real.get()==""):
            zl_real = 0
        else:
            zl_real = self.zl_input_real.get()
        zl_real = float(zl_real)

        if(self.zl_input_imag.get()==""):
            zl_imag = 0
        else:
            zl_imag = self.zl_input_imag.get()
        zl_imag = float(zl_imag)

        if(self.vi_input.get()==""):
            vi = 1
        else:
            vi = self.vi_input.get()
        vi = float(vi)

        if(self.pn_input.get()==""):
            pn = 1000
        else:
            pn = self.pn_input.get()
        pn = int(pn)

        if(self.x1_input.get()==""):
            x1 = 0
        else:
            x1 = self.x1_input.get()
        x1 = float(x1)

        zl = complex(zl_real,zl_imag)

        # verificador de bugs #

        if d<0 or zo<0 or C<0 or L<0 or f<=0 or zl_real<0 or vi<=0 or pn<=1 or x1<0:
            self.bugbug = self.error()

        # constantes de saída #

        omega = 2*np.pi*f
        self.omega_out = ctk.CTkLabel(self, text=(f'{omega:.2e}'), fg_color="#111", width=150, font=('Arial Narrow bold', 14))
        self.omega_out.grid(row=2, column=3, pady=5, padx=10)

        beta = omega*np.sqrt(L*C)
        self.beta_out = ctk.CTkLabel(self, text=(f'{beta:.2e}'), fg_color="#111", width=150, font=('Arial Narrow bold', 14))
        self.beta_out.grid(row=4, column=3, pady=5, padx=10)

        lambda_g = 2*np.pi/beta
        self.lambdag_out = ctk.CTkLabel(self, text=(f'{lambda_g:.2e}'), fg_color="#111", width=150, font=('Arial Narrow bold', 14))
        self.lambdag_out.grid(row=6, column=3, pady=5, padx=10)

        vp = 1/(np.sqrt(L*C))
        self.vp_out = ctk.CTkLabel(self, text=(f'{vp:.2e}'), fg_color="#111", width=150, font=('Arial Narrow bold', 14))
        self.vp_out.grid(row=8, column=3, pady=5, padx=10)

        vg = vp
        self.vg_out = ctk.CTkLabel(self, text=(f'{vg:.2e}'), fg_color="#111", width=150, font=('Arial Narrow bold', 14))
        self.vg_out.grid(row=10, column=3, pady=5, padx=10)

        gamma_L = (zl-zo)/(zl+zo)
        self.gammal_out = ctk.CTkLabel(self, text=(f'{gamma_L:.2e}'), fg_color="#111", width=150, font=('Arial Narrow bold', 14))
        self.gammal_out.grid(row=12, column=3, pady=5, padx=10)

        tao = gamma_L + 1
        self.tao_out = ctk.CTkLabel(self, text=(f'{tao:.2e}'), fg_color="#111", width=150, font=('Arial Narrow bold', 14))
        self.tao_out.grid(row=14, column=3, pady=5, padx=10)

        SWR = (1+gamma_L)/(1-gamma_L)
        self.swr_out = ctk.CTkLabel(self, text=(f'{SWR:.2e}'), fg_color="#111", width=150, font=('Arial Narrow bold', 14))
        self.swr_out.grid(row=16, column=3, pady=5, padx=10)

        # início dos plots #

        dimx = (self.winfo_screenwidth()-450)
        dimy = (self.winfo_screenheight()-200)

        longx = (0.95*dimx)/100
        longy = (0.95*dimy)/100

        graph_1 = plt.Figure(figsize=(longx/3,longy/2), dpi=100)
        graph_1_zoomed = plt.Figure(figsize=(3*longx/4,longy), dpi=100)
        graph_2 = plt.Figure(figsize=(longx/3,longy/2), dpi=100)
        graph_2_zoomed = plt.Figure(figsize=(3*longx/4,longy), dpi=100)
        graph_3 = plt.Figure(figsize=(longx/3,longy/2), dpi=100)
        graph_3_zoomed = plt.Figure(figsize=(3*longx/4,longy), dpi=100)
        graph_4 = plt.Figure(figsize=(longx/2,longy/2), dpi=100)
        graph_4_zoomed = plt.Figure(figsize=(3*longx/4,longy), dpi=100)
        graph_5 = plt.Figure(figsize=(longx/2,longy/2), dpi=100)
        graph_5_zoomed = plt.Figure(figsize=(3*longx/4,longy), dpi=100)

        ax1 = graph_1.add_subplot(111)
        ax1_zoomed = graph_1_zoomed.add_subplot(111)
        ax2 = graph_2.add_subplot(111)
        ax2_zoomed = graph_2_zoomed.add_subplot(111)
        ax3 = graph_3.add_subplot(111)
        ax3_zoomed = graph_3_zoomed.add_subplot(111)
        ax4 = graph_4.add_subplot(111)
        ax4_zoomed = graph_4_zoomed.add_subplot(111)
        ax5 = graph_5.add_subplot(111)
        ax5_zoomed = graph_5_zoomed.add_subplot(111)

        dt = np.linspace(0,d,pn)              # distância de 0m até d(m)
        itens = np.linspace(0,10,100)           # quantidade de ondas a serem plotadas

        zd = zo*((zl+1j*zo*np.tan(beta*dt))/(zo+1j*zl*np.tan(beta*dt)))
        zdx = zo*((zl+1j*zo*np.tan(beta*x1))/(zo+1j*zl*np.tan(beta*x1)))
        
        # plots #

        ax1.plot(dt, np.real(zd), label='Parte Real', color='red')
        ax1.grid()
        ax1.set_xlabel('d [m]', labelpad=1)
        ax1.set_ylabel('Z(d) [ohms]', labelpad=1)
        ax1.legend(loc='upper right')

        ax1_zoomed.plot(dt, np.real(zd), label='Parte Real', color='red')
        ax1_zoomed.plot(x1, np.real(zdx), 'ok')
        ax1_zoomed.grid()
        ax1_zoomed.set_xlabel('d [m]', labelpad=1)
        ax1_zoomed.set_ylabel('Z(d) [ohms]', labelpad=1)
        ax1_zoomed.set_title('\n Parte Real da Impedância ao longo da linha', pad=20)
        ax1_zoomed.legend(loc='upper right')

        ax2.plot(dt, np.imag(zd), label='Parte Imaginária', color='blue')
        ax2.grid()
        ax2.set_xlabel('d [m]', labelpad=1)
        ax2.set_ylabel('Z(d) [ohms]', labelpad=1)
        ax2.set_title('\n Impedância ao longo da linha', pad=20)
        ax2.legend(loc='upper right')

        ax2_zoomed.plot(dt, np.imag(zd), label='Parte Imaginária', color='blue')
        ax2_zoomed.plot(x1, np.imag(zdx), 'ok')
        ax2_zoomed.grid()
        ax2_zoomed.set_xlabel('d [m]', labelpad=1)
        ax2_zoomed.set_ylabel('Z(d) [ohms]', labelpad=1)
        ax2_zoomed.set_title('\n Parte Imaginária da Impedância ao longo da linha', pad=20)
        ax2_zoomed.legend(loc='upper right')

        ax3.plot(dt, np.sqrt(np.real(zd)**2 + np.imag(zd)**2), label='Módulo', color='green')
        ax3.grid()
        ax3.set_xlabel('d [m]', labelpad=1)
        ax3.set_ylabel('|Z(d)| [ohms]', labelpad=1)
        ax3.legend(loc='upper right')

        ax3_zoomed.plot(dt, np.sqrt(np.real(zd)**2 + np.imag(zd)**2), label='Módulo', color='green')
        ax3_zoomed.plot(x1, np.sqrt(np.real(zdx)**2 + np.imag(zdx)**2), 'ok')
        ax3_zoomed.grid()
        ax3_zoomed.set_xlabel('d [m]', labelpad=1)
        ax3_zoomed.set_ylabel('|Z(d)| [ohms]', labelpad=1)
        ax3_zoomed.legend(loc='upper right')
        ax3_zoomed.set_title('\n Parte Imaginária da Impedância ao longo da linha', pad=20)


        for t in itens:                         # calculando a amplitude da onda (tensão e corrente) no ponto d
            v = vi*(np.cos(beta*dt)+gamma_L*np.cos(beta*dt))*np.cos(2*np.pi*t)-vi*(np.sin(beta*dt)-gamma_L*np.sin(beta*dt))*np.sin(2*np.pi*t)
            ax4.plot(dt,np.real(v),linestyle = 'dotted')
            ax4_zoomed.plot(dt,np.real(v),linestyle = 'dotted')
            i = (vi/zo)*np.cos(2*np.pi*t+beta*dt)-(vi/zo)*gamma_L*np.cos(2*np.pi*t-beta*dt)
            ax5.plot(dt,np.real(i),linestyle = 'dotted')
            ax5_zoomed.plot(dt,np.real(i),linestyle = 'dotted')

        envoltoria_v = vi*(1+(gamma_L**2)+2*gamma_L*np.cos(2*beta*dt))**(1/2)
        envoltoria_vx = vi*(1+(gamma_L**2)+2*gamma_L*np.cos(2*beta*x1))**(1/2)
        ax4.plot(dt,np.real(envoltoria_v), label='envoltória +', linewidth = '3.0')
        ax4.plot(dt,np.real(-envoltoria_v), label='envoltória -', linewidth = '3.0')
        ax4_zoomed.plot(dt,np.real(envoltoria_v), label='envoltória +', linewidth = '3.0')
        ax4_zoomed.plot(dt,np.real(-envoltoria_v), label='envoltória -', linewidth = '3.0')
        ax4_zoomed.plot(x1, np.real(envoltoria_vx), 'ok', x1, np.real(-envoltoria_vx), 'ok')

        envoltoria_i = (vi/zo)*np.sqrt((1+(gamma_L**2)-2*gamma_L*np.cos(2*beta*dt)))
        envoltoria_ix = (vi/zo)*np.sqrt((1+(gamma_L**2)-2*gamma_L*np.cos(2*beta*x1)))
        ax5.plot(dt,np.real(envoltoria_i), label='envoltória +', linewidth = '3.0')
        ax5.plot(dt,np.real(-envoltoria_i), label='envoltória -', linewidth = '3.0')
        ax5_zoomed.plot(dt,np.real(envoltoria_i), label='envoltória +', linewidth = '3.0')
        ax5_zoomed.plot(dt,np.real(-envoltoria_i), label='envoltória -', linewidth = '3.0')
        ax5_zoomed.plot(x1, np.real(envoltoria_ix), 'ok', x1, np.real(-envoltoria_ix), 'ok')

        ax4.grid()
        ax4.set_title('Tensão ao longo da linha', pad=20)
        ax4.set_xlabel('d [m]')
        ax4.set_ylabel('V(d,t) [V]')
        ax4.legend(loc='right')
        ax4_zoomed.grid()
        ax4_zoomed.set_title('Tensão ao longo da linha', pad=20)
        ax4_zoomed.set_xlabel('d [m]')
        ax4_zoomed.set_ylabel('V(d,t) [V]')
        ax4_zoomed.legend(loc='right')

        ax5.grid()
        ax5.set_title('Corrente ao longo da linha', pad=20)
        ax5.set_xlabel('d [m]')
        ax5.set_ylabel('I(d,t) [A]')
        ax5.legend(loc='right')
        ax5_zoomed.grid()
        ax5_zoomed.set_title('Corrente ao longo da linha', pad=20)
        ax5_zoomed.set_xlabel('d [m]')
        ax5_zoomed.set_ylabel('I(d,t) [A]')
        ax5_zoomed.legend(loc='right')

        # Tab "Visão Geral" #
        
        graphs_vg_r1 = ctk.CTkFrame(master=self.graphs_box.tab("Visão Geral"), width=dimx, fg_color="#fff")
        graphs_vg_r1.grid(column=1,row=1, padx=5, pady=5)
        graphs_vg_r2 = ctk.CTkFrame(master=self.graphs_box.tab("Visão Geral"), width=dimx, fg_color="#fff")
        graphs_vg_r2.grid(column=1,row=2, padx=5, pady=5)

        canva_vg1 = FigureCanvasTkAgg(graph_1, master=graphs_vg_r1)
        canva_vg1.draw()
        canva_vg1.get_tk_widget().grid(column=0,row=0, padx=10, pady=10)

        canva_vg2 = FigureCanvasTkAgg(graph_2, master=graphs_vg_r1)
        canva_vg2.draw()
        canva_vg2.get_tk_widget().grid(column=1,row=0, padx=10, pady=10)

        canva_vg3 = FigureCanvasTkAgg(graph_3, master=graphs_vg_r1)
        canva_vg3.draw()
        canva_vg3.get_tk_widget().grid(column=2,row=0, padx=10, pady=10)

        canva_vg4 = FigureCanvasTkAgg(graph_4, master=graphs_vg_r2)
        canva_vg4.draw()
        canva_vg4.get_tk_widget().grid(column=0,row=0, padx=10, pady=10)

        canva_vg5 = FigureCanvasTkAgg(graph_5, master=graphs_vg_r2)
        canva_vg5.draw()
        canva_vg5.get_tk_widget().grid(column=1,row=0, padx=10, pady=10)

        self.graphs_box.set("Visão Geral")

        # Tab "Parte real da impedância" #
        
        graphs_zd1_c1 = ctk.CTkFrame(master=self.graphs_box.tab("Parte real da impedância"), width=3*dimx/4, height=dimy, fg_color="#fff")
        graphs_zd1_c1.grid(column=0,row=0, padx=0, pady=5)
        graphs_zd1_c2 = ctk.CTkFrame(master=self.graphs_box.tab("Parte real da impedância"), width=dimx/4, height=dimy, fg_color="#fff")
        graphs_zd1_c2.grid(column=1,row=0, padx=0, pady=5)

        canva_zd1 = FigureCanvasTkAgg(graph_1_zoomed, master=graphs_zd1_c1)
        canva_zd1.draw()
        canva_zd1.get_tk_widget().grid(column=0,row=0, padx=10, pady=10)

        self.zd1_txt2 = ctk.CTkLabel(master=graphs_zd1_c2, text="\n - Valores no ponto de amostragem - ", text_color="#000", font=('Arial Narrow bold', 18))
        self.zd1_txt2.grid(row=1, column=0, pady=0, padx=10)
        self.zd1_txt2 = ctk.CTkLabel(master=graphs_zd1_c2, text="\n Posição escolhida x [m] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.zd1_txt2.grid(row=2, column=0, pady=0, padx=10)
        self.zd1_out2 = ctk.CTkLabel(master=graphs_zd1_c2, text=(f'{x1:.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.zd1_out2.grid(row=3, column=0, pady=0, padx=10)
        self.zd1_txt2 = ctk.CTkLabel(master=graphs_zd1_c2, text="\n Valor da parte real de Z(x) [ohms] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.zd1_txt2.grid(row=4, column=0, pady=0, padx=10)
        self.zd1_out2 = ctk.CTkLabel(master=graphs_zd1_c2, text=(f'{np.real(zdx):.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.zd1_out2.grid(row=5, column=0, pady=0, padx=10)

        self.zd1_txt2 = ctk.CTkLabel(master=graphs_zd1_c2, text="\n\n - Valores nos limites - ", text_color="#000", font=('Arial Narrow bold', 18))
        self.zd1_txt2.grid(row=6, column=0, pady=0, padx=10)
        self.zd1_txt1 = ctk.CTkLabel(master=graphs_zd1_c2, text="\n Valor máximo da parte real de Z(d) [ohms] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.zd1_txt1.grid(row=7, column=0, pady=0, padx=10)
        self.zd1_out1 = ctk.CTkLabel(master=graphs_zd1_c2, text=(f'{max(np.real(zd)):.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.zd1_out1.grid(row=8, column=0, pady=0, padx=10)
        self.zd1_txt1 = ctk.CTkLabel(master=graphs_zd1_c2, text="\n Valor mínimo da parte real de Z(d) [ohms] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.zd1_txt1.grid(row=9, column=0, pady=0, padx=10)
        self.zd1_out1 = ctk.CTkLabel(master=graphs_zd1_c2, text=(f'{min(np.real(zd)):.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.zd1_out1.grid(row=10, column=0, pady=0, padx=10)

        # Tab "Parte imaginária da impedância" #

        graphs_zd2_c1 = ctk.CTkFrame(master=self.graphs_box.tab("Parte imaginária da impedância"), width=3*dimx/4, height=dimy, fg_color="#fff")
        graphs_zd2_c1.grid(column=0,row=0, padx=0, pady=5)
        graphs_zd2_c2 = ctk.CTkFrame(master=self.graphs_box.tab("Parte imaginária da impedância"), width=dimx/4, height=dimy, fg_color="#fff")
        graphs_zd2_c2.grid(column=1,row=0, padx=0, pady=5)

        canva_zd2 = FigureCanvasTkAgg(graph_2_zoomed, master=graphs_zd2_c1)
        canva_zd2.draw()
        canva_zd2.get_tk_widget().grid(column=0,row=0, padx=10, pady=10)

        self.zd2_txt2 = ctk.CTkLabel(master=graphs_zd2_c2, text="\n - Valores no ponto de amostragem - ", text_color="#000", font=('Arial Narrow bold', 18))
        self.zd2_txt2.grid(row=1, column=0, pady=0, padx=10)
        self.zd2_txt2 = ctk.CTkLabel(master=graphs_zd2_c2, text="\n Posição escolhida x [m] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.zd2_txt2.grid(row=2, column=0, pady=0, padx=10)
        self.zd2_out2 = ctk.CTkLabel(master=graphs_zd2_c2, text=(f'{x1:.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.zd2_out2.grid(row=3, column=0, pady=0, padx=10)
        self.zd2_txt2 = ctk.CTkLabel(master=graphs_zd2_c2, text="\n Valor da parte imaginária de Z(x) [ohms] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.zd2_txt2.grid(row=4, column=0, pady=0, padx=10)
        self.zd2_out2 = ctk.CTkLabel(master=graphs_zd2_c2, text=(f'{np.imag(zdx):.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.zd2_out2.grid(row=5, column=0, pady=0, padx=10)

        self.zd2_txt2 = ctk.CTkLabel(master=graphs_zd2_c2, text="\n\n - Valores nos limites - ", text_color="#000", font=('Arial Narrow bold', 18))
        self.zd2_txt2.grid(row=6, column=0, pady=0, padx=10)
        self.zd2_txt1 = ctk.CTkLabel(master=graphs_zd2_c2, text="\n Valor máximo da parte imaginária de Z(d) [ohms] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.zd2_txt1.grid(row=7, column=0, pady=0, padx=10)
        self.zd2_out1 = ctk.CTkLabel(master=graphs_zd2_c2, text=(f'{max(np.imag(zd)):.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.zd2_out1.grid(row=8, column=0, pady=0, padx=10)
        self.zd2_txt1 = ctk.CTkLabel(master=graphs_zd2_c2, text="\n Valor mínimo da parte imaginária de Z(d) [ohms] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.zd2_txt1.grid(row=9, column=0, pady=0, padx=10)
        self.zd2_out1 = ctk.CTkLabel(master=graphs_zd2_c2, text=(f'{min(np.imag(zd)):.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.zd2_out1.grid(row=10, column=0, pady=0, padx=10)

        # Tab "Módulo da impedância" #

        graphs_zd3_c1 = ctk.CTkFrame(master=self.graphs_box.tab("Módulo da impedância"), width=3*dimx/4, height=dimy, fg_color="#fff")
        graphs_zd3_c1.grid(column=0,row=0, padx=0, pady=5)
        graphs_zd3_c2 = ctk.CTkFrame(master=self.graphs_box.tab("Módulo da impedância"), width=dimx/4, height=dimy, fg_color="#fff")
        graphs_zd3_c2.grid(column=1,row=0, padx=0, pady=5)

        canva_zd3 = FigureCanvasTkAgg(graph_3_zoomed, master=graphs_zd3_c1)
        canva_zd3.draw()
        canva_zd3.get_tk_widget().grid(column=0,row=0, padx=10, pady=10)

        self.zd3_txt2 = ctk.CTkLabel(master=graphs_zd3_c2, text="\n - Valores do ponto de amostragem - ", text_color="#000", font=('Arial Narrow bold', 18))
        self.zd3_txt2.grid(row=1, column=0, pady=0, padx=10)
        self.zd3_txt2 = ctk.CTkLabel(master=graphs_zd3_c2, text="\n Posição escolhida x [m] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.zd3_txt2.grid(row=2, column=0, pady=0, padx=10)
        self.zd3_out2 = ctk.CTkLabel(master=graphs_zd3_c2, text=(f'{x1:.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.zd3_out2.grid(row=3, column=0, pady=0, padx=10)
        self.zd3_txt2 = ctk.CTkLabel(master=graphs_zd3_c2, text="\n Valor do módulo de Z(x) [ohms] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.zd3_txt2.grid(row=4, column=0, pady=0, padx=10)
        self.zd3_out2 = ctk.CTkLabel(master=graphs_zd3_c2, text=(f'{np.abs(zdx):.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.zd3_out2.grid(row=5, column=0, pady=0, padx=10)

        self.zd3_txt2 = ctk.CTkLabel(master=graphs_zd3_c2, text="\n\n - Valores nos limites - ", text_color="#000", font=('Arial Narrow bold', 18))
        self.zd3_txt2.grid(row=6, column=0, pady=0, padx=10)
        self.zd3_txt1 = ctk.CTkLabel(master=graphs_zd3_c2, text="\n Valor máximo do módulo de Z(d) [ohms] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.zd3_txt1.grid(row=7, column=0, pady=0, padx=10)
        self.zd3_out1 = ctk.CTkLabel(master=graphs_zd3_c2, text=(f'{max(np.abs(zd)):.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.zd3_out1.grid(row=8, column=0, pady=0, padx=10)
        self.zd3_txt1 = ctk.CTkLabel(master=graphs_zd3_c2, text="\n Valor mínimo do módulo de Z(d) [ohms] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.zd3_txt1.grid(row=9, column=0, pady=0, padx=10)
        self.zd3_out1 = ctk.CTkLabel(master=graphs_zd3_c2, text=(f'{min(np.abs(zd)):.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.zd3_out1.grid(row=10, column=0, pady=0, padx=10)

        # Tab "Tensão" #

        graphs_vd0_c1 = ctk.CTkFrame(master=self.graphs_box.tab("Tensão"), width=3*dimx/4, height=dimy, fg_color="#fff")
        graphs_vd0_c1.grid(column=0,row=0, padx=0, pady=5)
        graphs_vd0_c2 = ctk.CTkFrame(master=self.graphs_box.tab("Tensão"), width=dimx/4, height=dimy, fg_color="#fff")
        graphs_vd0_c2.grid(column=1,row=0, padx=0, pady=5)

        canva_vd0 = FigureCanvasTkAgg(graph_4_zoomed, master=graphs_vd0_c1)
        canva_vd0.draw()
        canva_vd0.get_tk_widget().grid(column=0,row=0, padx=10, pady=10)

        self.vd0_txt2 = ctk.CTkLabel(master=graphs_vd0_c2, text="\n - Valores do ponto de amostragem - ", text_color="#000", font=('Arial Narrow bold', 18))
        self.vd0_txt2.grid(row=1, column=0, pady=0, padx=10)
        self.vd0_txt2 = ctk.CTkLabel(master=graphs_vd0_c2, text="\n Posição escolhida x [m] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.vd0_txt2.grid(row=2, column=0, pady=0, padx=10)
        self.vd0_out2 = ctk.CTkLabel(master=graphs_vd0_c2, text=(f'{x1:.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.vd0_out2.grid(row=3, column=0, pady=0, padx=10)
        self.vd0_txt2 = ctk.CTkLabel(master=graphs_vd0_c2, text="\n Valor da tensão V(x, t) [V] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.vd0_txt2.grid(row=4, column=0, pady=0, padx=10)
        self.vd0_out2 = ctk.CTkLabel(master=graphs_vd0_c2, text=(f'{np.real(envoltoria_vx):.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.vd0_out2.grid(row=5, column=0, pady=0, padx=10)

        self.vd0_txt2 = ctk.CTkLabel(master=graphs_vd0_c2, text="\n\n - Valores nos limites - ", text_color="#000", font=('Arial Narrow bold', 18))
        self.vd0_txt2.grid(row=6, column=0, pady=0, padx=10)
        self.vd0_txt1 = ctk.CTkLabel(master=graphs_vd0_c2, text="\n Valor máximo da tensão V(d, t) [V] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.vd0_txt1.grid(row=7, column=0, pady=0, padx=10)
        self.vd0_out1 = ctk.CTkLabel(master=graphs_vd0_c2, text=(f'{max(np.real(envoltoria_v)):.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.vd0_out1.grid(row=8, column=0, pady=0, padx=10)
        self.vd0_txt1 = ctk.CTkLabel(master=graphs_vd0_c2, text="\n Valor mínimo da tensão V(d, t) [V] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.vd0_txt1.grid(row=9, column=0, pady=0, padx=10)
        self.vd0_out1 = ctk.CTkLabel(master=graphs_vd0_c2, text=(f'{min(np.real(envoltoria_v)):.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.vd0_out1.grid(row=10, column=0, pady=0, padx=10)

        # Tab "Corrente" #

        graphs_id0_c1 = ctk.CTkFrame(master=self.graphs_box.tab("Corrente"), width=3*dimx/4, height=dimy, fg_color="#fff")
        graphs_id0_c1.grid(column=0,row=0, padx=0, pady=5)
        graphs_id0_c2 = ctk.CTkFrame(master=self.graphs_box.tab("Corrente"), width=dimx/4, height=dimy, fg_color="#fff")
        graphs_id0_c2.grid(column=1,row=0, padx=0, pady=5)

        canva_id0 = FigureCanvasTkAgg(graph_5_zoomed, master=graphs_id0_c1)
        canva_id0.draw()
        canva_id0.get_tk_widget().grid(column=0,row=0, padx=10, pady=10)

        self.id0_txt2 = ctk.CTkLabel(master=graphs_id0_c2, text="\n - Valores do ponto de amostragem - ", text_color="#000", font=('Arial Narrow bold', 18))
        self.id0_txt2.grid(row=1, column=0, pady=0, padx=10)
        self.id0_txt2 = ctk.CTkLabel(master=graphs_id0_c2, text="\n Posição escolhida x [m] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.id0_txt2.grid(row=2, column=0, pady=0, padx=10)
        self.id0_out2 = ctk.CTkLabel(master=graphs_id0_c2, text=(f'{x1:.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.id0_out2.grid(row=3, column=0, pady=0, padx=10)
        self.id0_txt2 = ctk.CTkLabel(master=graphs_id0_c2, text="\n Valor da corrente I(x, t) [A] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.id0_txt2.grid(row=4, column=0, pady=0, padx=10)
        self.id0_out2 = ctk.CTkLabel(master=graphs_id0_c2, text=(f'{np.real(envoltoria_ix):.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.id0_out2.grid(row=5, column=0, pady=0, padx=10)

        self.id0_txt2 = ctk.CTkLabel(master=graphs_id0_c2, text="\n\n - Valores nos limites - ", text_color="#000", font=('Arial Narrow bold', 18))
        self.id0_txt2.grid(row=6, column=0, pady=0, padx=10)
        self.id0_txt1 = ctk.CTkLabel(master=graphs_id0_c2, text="\n Valor máximo da corrente I(d, t) [A] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.id0_txt1.grid(row=7, column=0, pady=0, padx=10)
        self.id0_out1 = ctk.CTkLabel(master=graphs_id0_c2, text=(f'{max(np.real(envoltoria_i)):.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.id0_out1.grid(row=8, column=0, pady=0, padx=10)
        self.id0_txt1 = ctk.CTkLabel(master=graphs_id0_c2, text="\n Valor mínimo da corrente I(d, t) [A] ", text_color="#000", font=('Arial Narrow bold', 14))
        self.id0_txt1.grid(row=9, column=0, pady=0, padx=10)
        self.id0_out1 = ctk.CTkLabel(master=graphs_id0_c2, text=(f'{min(np.real(envoltoria_i)):.2e}'), text_color="#000", font=('Arial Narrow bold', 14))
        self.id0_out1.grid(row=10, column=0, pady=0, padx=10)

# definição #

wdw = Prog()
wdw.geometry("{0}x{1}+0+0".format(wdw.winfo_screenwidth(), wdw.winfo_screenheight()))
wdw.title("Simulador de LTs [OLCL5 - 2024]")
wdw.mainloop()
