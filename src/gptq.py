def obq(weights: list):
    """Takes a list of weights (e.g., from a neural network), and applies the OBQ quantization to them.

    Args:
        weights (list): List of weights to quantize.
    """
    # Based on the following paper: https://arxiv.org/pdf/2210.17323.pdf
    # you can go layer by layer through a network, quantizing the weight
    # that will minimize error, as calculated by the objective function

    # In order to choose which weight to quantize, they define formulas
    # for doing so. The way that they come up with these formulas is described
    # in https://www.babak.caltech.edu/pubs/conferences/00298572.pdf (they use
    # Taylor series to approximate error once a specific weight is quantized)


def gptq(weights: list):
    """Takes a list of weights (e.g., from a neural network), and applies the GPTQ quantization to them.

    Args:
        weights (list): List of weights to quantize.
    """
    print("This is a test of the gptq function")

    