class TaxCalculator:
    def __init__(self, country: str):
        self.country = country

    @staticmethod
    def get_gt_rate():
        return 0.12

    def get_taxes(self, total: float):
        taxes = 0.0
        if self.country == 'GT':
            taxes = total * TaxCalculator.get_gt_rate()
        elif self.country == 'US':
            taxes = total * 0.11
        elif self.country == 'ES':
            taxes = total * 0.48

        return taxes
