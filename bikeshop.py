"""Bike shop assignment"""


class Bicycle(object):
    """

    Attributes:
       model_name (str): THe model name for the bike.
       bike_cost (float): Base cost of the bike.

    """

    def __init__(self, model_name, bike_weight, bike_cost):
        """

        Args:
            model_name (str): --

        """

        self.model_name = model_name
        self.bike_weight = bike_weight
        self.bike_cost = bike_cost


class BikeShop(Bicycle):
    def __init__(self, shop_name, inventory):
        self.shop_name = shop_name
        self.inventory = inventory
        self.profit = 0

    def get_shop_name(self):
        return self.shop_name

    def get_inventory(self):
        return self.inventory

    def sell_to(self, customer):
        """Sells the most expensive bike the customer
        can afford (according to their budget).

        Args:
            customer (Customer): --

        Returns:
            bike|None: None if the customer cannot
                afford anything.

        """

        priciest_affordable_bike = None

        for bike in self.inventory:

            # Check the bike cost, make sure the
            # customer can afford, otherwise continue
            if bike.bike_cost <= customer.budget:

                # We already have set "priciest_affordable_bike" so now we need
                # to compare it against this new affordable bike to see which is
                # more expensive.
                if priciest_affordable_bike and priciest_affordable_bike.bike_cost < bike.bike_cost:
                    priciest_affordable_bike = bike
                # No bike to compare against.
                elif not priciest_affordable_bike:
                    priciest_affordable_bike = bike

        return priciest_affordable_bike


class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.own_bike = None


if __name__ == '__main__':

    # bike models for inventory
    hybrid = Bicycle("hybrid", 20, 400)
    bmx = Bicycle("bmx", 10, 80)
    road = Bicycle("road", 15, 560)
    mountain = Bicycle("mountain", 30, 320)
    racing = Bicycle("racing", 10, 640)
    cruiser = Bicycle("cruiser", 40, 160)

    initial_inventory = [hybrid, bmx, road, mountain, racing, cruiser]

    shop = BikeShop("Freddys Bicycles", initial_inventory)


    # customers
    josh = Customer("Josh", 1000)
    john = Customer("John", 500)
    joan = Customer("Joan", 200)

    customersList = [josh, john, joan]


    print "Welcome to {}!".format(shop.get_shop_name())
    print "Current Inventory:"
    print "Model - Weight - Cost"
    for bike in shop.get_inventory():
        print "{0} {1} ${2}".format(bike.model_name, bike.bike_weight, bike.bike_cost)

    for customer in customersList:
        print "I'll find the most expensive bike you can afford"
        bike = shop.sell_to(customer)
        print "{0} {1} ${2}".format(bike.model_name, bike.bike_weight, bike.bike_cost)

