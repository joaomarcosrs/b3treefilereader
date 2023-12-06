

class ReadFiles:
    def __init__(self, file) -> None:
        self.file = file
        
class MetaData:
    def __init__(self, data) -> None:
        self.metadata = data.get('metadata', {})
        self.markets = data.get('markets', {})
        self.indopc = data.get('indopc', {})
        self.codbdi = data.get('codbdi', {})

    def add_metadata(self, key, value):
        self.metadata[key] = value

    def add_market(self, key, value):
        self.markets[key] = value

    def add_indopc(self, key, value):
        self.indopc[key] = value

    def add_codbdi(self, key, value):
        self.codbdi[key] = value
        