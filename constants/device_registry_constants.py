"""Constant values useful for testing the device registry."""

from .device_registry_data_classes import UserData, DeviceData

#Static test users
Pythonista = UserData(
    login="pythonista",
    password="I<3testing",
)

Engineer = UserData(
    login="engineer",
    password="Muh5devices",
)

#Default Devices
PorchLight = DeviceData(
    name="Front Porch Light",
    location="Front Porch",
    type="Light Switch",
    model="GenLight64B",
    serial_number="GL64B-99987",
)

Thermostat = DeviceData(
    name="Main Thermostat",
    location="Living Room",
    type="Thermostat",
    model="ThermoBest 3G",
    serial_number="TB3G-12345",
)

Fridge = DeviceData(
    name="Family Fridge",
    location="Kitchen",
    type="Refrigerator",
    model="El Gee Mondo21",
    serial_number="LGM-20201",
)
