import matplotlib.pyplot as plt
import io
import base64
import numpy as np


def build_gist(prob_dictionary):
    img = io.BytesIO()
    keys = prob_dictionary.keys()
    values = prob_dictionary.values()
    plt.style.use('dark_background')
    plt.bar(keys, np.divide(list(values), sum(values)), label='Real distribution')
    plt.ylim(0, 1)
    plt.ylabel('Percentage')
    plt.xticks(list(keys), rotation='vertical')
    plt.tight_layout()
    plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0.)
    plt.savefig(img, format='png', dpi=600)
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)
