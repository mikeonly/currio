import numpy as np
import pytest
import matplotlib

matplotlib.use("Agg")

pytest.importorskip("pyvista")
pint = pytest.importorskip("pint")

from currio.sensor import RegularGridSensor, Sensor

ureg = pint.UnitRegistry()


def test_sensor_exposes_units_and_pints():
    sensor = Sensor(np.array([[0.0, 0.0, 0.0]], dtype=float))

    assert sensor.units["coordinates"] == "meter"
    assert str(sensor.pints["coordinates"]) == "meter"


def test_regular_grid_sensor_accepts_pint_length_for_centroid_and_move():
    sensor = RegularGridSensor(bounds=(0.0, 2.0e-3, 0.0, 2.0e-3, 0.0, 0.0), resolution=(3, 3, 1))

    centroid = sensor.get_centroid(z=1.5 * ureg.mm)
    np.testing.assert_allclose(centroid, np.array([1.0e-3, 1.0e-3, 1.5e-3]))

    sensor.move(to=np.array([4.0, 5.0, 6.0]) * ureg.mm)
    np.testing.assert_allclose(sensor.get_centroid(), np.array([4.0e-3, 5.0e-3, 6.0e-3]))


def test_sensor_unit_metadata_converts_coordinates_when_consumed_elsewhere():
    sensor = Sensor(np.array([[1.0, 2.0, 3.0]], dtype=float)).set_units(coordinates="mm")

    np.testing.assert_allclose(sensor.points, np.array([[1.0, 2.0, 3.0]], dtype=float))
    assert sensor.units["coordinates"] == "millimeter"


def test_regular_grid_sensor_plot_imshow_accepts_method_keyword():
    sensor = RegularGridSensor(bounds=(0.0, 2.0e-3, 0.0, 3.0e-3, 0.0, 0.0), resolution=(2, 3, 1))
    sensor.point_data["B"] = np.array(
        [
            [1.0, 0.0, 0.0],
            [2.0, 0.0, 0.0],
            [3.0, 0.0, 0.0],
            [4.0, 0.0, 0.0],
            [5.0, 0.0, 0.0],
            [6.0, 0.0, 0.0],
        ],
        dtype=float,
    )

    ax = sensor.plot("B", method="imshow", show=False)

    assert ax.get_title() == "B (magnitude)"
    assert len(ax.images) == 1
