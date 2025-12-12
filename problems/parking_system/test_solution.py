import pytest
from .solution import ParkingSystem


def test_initialization():
    ps = ParkingSystem(1, 2, 3)
    assert ps.big == 1
    assert ps.medium == 2
    assert ps.small == 3


def test_add_big_car_success():
    ps = ParkingSystem(1, 0, 0)
    assert ps.addCar(1) is True
    # now big should be 0
    assert ps.big == 0


def test_add_big_car_fail_when_full():
    ps = ParkingSystem(1, 0, 0)
    assert ps.addCar(1) is True
    assert ps.addCar(1) is False  # no more big spots


def test_add_medium_car():
    ps = ParkingSystem(0, 2, 0)
    assert ps.addCar(2) is True
    assert ps.addCar(2) is True
    assert ps.addCar(2) is False  # third medium car should fail


def test_add_small_car():
    ps = ParkingSystem(0, 0, 1)
    assert ps.addCar(3) is True
    assert ps.addCar(3) is False


def test_mixed_usage():
    ps = ParkingSystem(1, 1, 1)

    # all should work once
    assert ps.addCar(1) is True
    assert ps.addCar(2) is True
    assert ps.addCar(3) is True

    # all should now be full
    assert ps.addCar(1) is False
    assert ps.addCar(2) is False
    assert ps.addCar(3) is False


@pytest.mark.parametrize("carType", [1, 2, 3])

def test_invalid_car_type_does_not_crash(carType):
    ps = ParkingSystem(1, 1, 1)
    # Should return boolean; calling with valid types is safe
    assert isinstance(ps.addCar(carType), bool)
