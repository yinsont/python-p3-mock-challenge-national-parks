class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []
        self.visitors_count = {}
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception("Name must not exist and must be a string")
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        
        if new_visitor and isinstance(new_visitor, Visitor) and new_visitor not in self._visitors:
            self._visitors.append(new_visitor)
            
        return self._visitors
        
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        for trip in self._trips:
            # looping over the trips
            if trip.visitor in self.visitors_count:
                self.visitors_count[trip.visitor] += 1
            else: 
                self.visitors_count[trip.visitor] = 1
        return max(self.visitors_count, key=self.visitors_count.get)