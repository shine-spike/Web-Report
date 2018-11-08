import Site

class Reporter(Object):
    """Collects and reports info on a set of websites"""

    def __init__(self, Sites):
        """Initialises this Reporter with a bunch of fresh Sites"""
        self.sites = []
        for Site in Sites:
            self.sites.append(site())

    def update(self, sites = self.sites):
        pass

    def get_site(self, site_name):
        pass

    def add_site(self, site):
        pass


