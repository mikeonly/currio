import pathlib

__modelpath__ = pathlib.Path(__file__).parent.parent.resolve() / "models"
"""Standard path to the directory where all models are stored."""

__resultpath__ = pathlib.Path(__file__).parent.parent.resolve() / "results"
"""Standard path to the directory where results of a simulation are stored."""

from currio.neuron import Neuron
from currio.io import IO
from currio.sensor import Sensor

__all__ = ["Neuron", "IO", "Sensor", "utils"]
