from battery import Battery
from utils import add_yeas_to_date

class SpindlerBattery(Battery):
    def __init__(self,current_date,last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
    
    def needs_service(self):
        date_which_battery_should_be_Serviced_by = add_yeas_to_date(self.last_service_date,2)
        if date_which_battery_should_be_Serviced_by < self.current_date:
            return True
        else:
            return False