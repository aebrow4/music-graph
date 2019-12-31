class BaseModel:
    """Deserialize a node in the graph"""
    def to_dict(self):
        return self.__properties__
