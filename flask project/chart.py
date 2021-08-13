import io
import numpy as np
import matplotlib.pyplot as plt
import base64

x = np.linspace(-20, 20, num = 100)

def draw_chart(a1, b1, c1, d1, a2, b2, c2, d2):

    y1 = []
    y2 = []
    for i in range(len(x)):
        y1.append((int(a1) * (x[i] ** 3)) + (int(b1) * (x[i] ** 2)) + (int(c1) * x[i]) + int(d1))
        y2.append((int(a2) * (x[i] ** 3)) + (int(b2) * (x[i] ** 2)) + (int(c2) * x[i]) + int(d2))

    plt.plot(x, y1, color = 'r', label = "first")
    plt.plot(x, y2, color='g', label="second")
    plt.xlabel('x values')
    plt.title('plotted x and y values')
    plt.legend()
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return f'data:image/png;base64,{plot_url}'
    #plt.show()


