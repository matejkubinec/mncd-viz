from io import StringIO


def plt_to_str(plt):
    image_data = StringIO()

    plt.savefig(image_data, format="svg")

    image_data.seek(0)

    return image_data.read()
