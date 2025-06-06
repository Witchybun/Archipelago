from ..bases import SVTestBase
from ...locations import LocationTags, location_table
from ...options import BuildingProgression, Shipsanity


class TestShipsanityNone(SVTestBase):
    options = {
        Shipsanity.internal_name: Shipsanity.option_none
    }

    def test_no_shipsanity_locations(self):
        for location in self.get_real_locations():
            self.assertFalse("Shipsanity" in location.name)
            self.assertNotIn(LocationTags.SHIPSANITY, location_table[location.name].tags)


class TestShipsanityCrops(SVTestBase):
    options = {
        Shipsanity.internal_name: Shipsanity.option_crops
    }

    def test_only_crop_shipsanity_locations(self):
        for location in self.get_real_locations():
            if LocationTags.SHIPSANITY in location_table[location.name].tags:
                self.assertIn(LocationTags.SHIPSANITY_CROP, location_table[location.name].tags)


class TestShipsanityFish(SVTestBase):
    options = {
        Shipsanity.internal_name: Shipsanity.option_fish
    }

    def test_only_fish_shipsanity_locations(self):
        for location in self.get_real_locations():
            if LocationTags.SHIPSANITY in location_table[location.name].tags:
                self.assertIn(LocationTags.SHIPSANITY_FISH, location_table[location.name].tags)


class TestShipsanityFullShipment(SVTestBase):
    options = {
        Shipsanity.internal_name: Shipsanity.option_full_shipment
    }

    def test_only_full_shipment_shipsanity_locations(self):
        for location in self.get_real_locations():
            if LocationTags.SHIPSANITY in location_table[location.name].tags:
                self.assertIn(LocationTags.SHIPSANITY_FULL_SHIPMENT, location_table[location.name].tags)
                self.assertNotIn(LocationTags.SHIPSANITY_FISH, location_table[location.name].tags)


class TestShipsanityFullShipmentWithFish(SVTestBase):
    options = {
        Shipsanity.internal_name: Shipsanity.option_full_shipment_with_fish
    }

    def test_only_full_shipment_and_fish_shipsanity_locations(self):
        for location in self.get_real_locations():
            if LocationTags.SHIPSANITY in location_table[location.name].tags:
                self.assertTrue(LocationTags.SHIPSANITY_FULL_SHIPMENT in location_table[location.name].tags or
                                LocationTags.SHIPSANITY_FISH in location_table[location.name].tags)


class TestShipsanityEverything(SVTestBase):
    options = {
        Shipsanity.internal_name: Shipsanity.option_everything,
        BuildingProgression.internal_name: BuildingProgression.option_progressive
    }

    def test_all_shipsanity_locations_require_shipping_bin(self):
        bin_name = "Shipping Bin"
        self.collect_all_except(bin_name)
        shipsanity_locations = [location
                                for location in self.get_real_locations()
                                if LocationTags.SHIPSANITY in location_table[location.name].tags]
        bin_item = self.create_item(bin_name)

        for location in shipsanity_locations:
            with self.subTest(location.name):
                self.assert_cannot_reach_location(location.name)

                self.collect(bin_item)
                self.assert_can_reach_location(location.name)
                self.remove(bin_item)
