from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn2_circles

import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close
    return graph

def get_plot(x, y, z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))
    plt.title('Gráfico AUB')
    diagrama = venn2(subsets=(1, 1, 1), set_labels=('A', 'B'), set_colors=('white', 'white'))
    venn2_circles((1,1,1))
    diagrama.get_label_by_id("10").set_text(x)
    diagrama.get_label_by_id("11").set_text(y)
    diagrama.get_label_by_id("01").set_text(z)
    plt.show()
    graph = get_graph()
    return graph

def get_inter(x, y, z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))
    plt.title('Gráfico A ∩ B')
    diagrama = venn2(subsets=(1, 1, 1), set_labels=('A', 'B'), set_colors=('#FF3939', '#3993FF'), alpha=0.9)
    venn2_circles((1,1,1))
    diagrama.get_label_by_id("10").set_text(x)
    diagrama.get_label_by_id("11").set_text(y)
    diagrama.get_label_by_id("01").set_text(z)
    plt.show()
    graph = get_graph()
    return graph

def get_dif(x, y, z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))
    plt.title('Gráfico A - B')
    diagrama = venn2(subsets=(1, 1, 1), set_labels=('A', 'B'), set_colors=('#FCFF39', '#39B1FF'), alpha=0.9)
    venn2_circles((1,1,1))
    diagrama.get_label_by_id("10").set_text(x)
    diagrama.get_label_by_id("11").set_text(y)
    diagrama.get_label_by_id("01").set_text(z)
    plt.show()
    graph = get_graph()
    return graph

def get_difsim(x, y, z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))
    plt.title('Gráfico A Δ B')
    diagrama = venn2(subsets=(1, 1, 1), set_labels=('A', 'B'), set_colors=('#FFBA63', '#FFBA63'), alpha=0.9)
    venn2_circles((1,1,1))
    diagrama.get_label_by_id("10").set_text(x)
    diagrama.get_label_by_id("11").set_text(y)
    diagrama.get_label_by_id("01").set_text(z)
    plt.show()
    graph = get_graph()
    return graph