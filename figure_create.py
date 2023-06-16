from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
import matplotlib.pyplot as plt

def figure_draw_1(fig2,ax2,ax3,mean,mean_1,fig_agg2,j,xax):
    ax2.cla()  # clear the subplot
    ax2.grid()
    ax2.plot(xax, mean, color='blue', label="average")
    ax2.set_xlabel("time")
    ax2.set_ylabel("left sensor average")
    ax2.set_xlim(left=max(0, j - 50), right=j + 50)
    ax2.set_ylim(ymin=0, ymax=20)
    ax2.legend(loc="upper left")
    ###########
    ax3.cla()  # clear the subplot
    ax3.grid()
    ax3.plot(xax, mean_1, color='blue', label="average")
    ax3.set_xlabel("time")
    ax3.set_ylabel("right sensor average")
    ax3.set_xlim(left=max(0, j - 50), right=j + 50)
    ax3.set_ylim(ymin=0, ymax=20)
    ax3.legend(loc="upper left")
    return (fig_agg2)

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


