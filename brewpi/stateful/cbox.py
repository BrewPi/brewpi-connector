"""
API to controllers running controlbox firmware.

Specific subclasses may add features for specific controller revisions.
"""


class ImmutableCollection:
    """
    Describes a non-mutable collection of things.
    """
    def find(self, id):
        """ retrieves an item by ID. The item is a stateful object with a connection to the controller """

    def all(self):
        """ retrieves a dict of all the contained items, keyed by id """


class MutableCollection:
    def create(self, *args, **kwargs):
        """ creates an item in this collection. The returned value is the id of the item """

    def delete(self, id):
        """ removes the given object with the given ID. """


class ValueCollection:

    def all_values(self):
        """ retrieves all values, keyed by ID """


class TempSensorsCollection(MutableCollection, ValueCollection):
    family_ds18b20 = 0x28

    def all_onewire_addresses(self):
        """ fetches the onewire addresses of all temp sensors """

    def find_by_address(self, address):
        """ finds a sensor by it's onewire address. """


class SwitchesCollection(MutableCollection, ValueCollection):
    family_ds2413 = 0x3A
    family_ds2408 = 0x29

    def create(self, address, pio):
        """
        persistently adds a new switch to this controller
        :param address: The onewire address
        :param pio: The index of the GPIO to set as output
        :return:
        """

    def find_by_address(self, address, pio):
        """ finds an actuator by onewire address and pio """


class OneWireBus:

    def reset(self):
        """resets the bus """

    def search(self):
        """ enumerate all devices on the bus. """

    def search_family(self, family):
        """ enumerates items with the given family """


class PinSwitchesCollection(ImmutableCollection):
    pass


"""
onewire list all
onewire list uninstalled




"""
