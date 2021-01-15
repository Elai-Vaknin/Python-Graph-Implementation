class NodeData():
    def __init__(self, key: int):
        self.id = key
        self.tag = 0.0
        self.info = ""
        self.pos: tuple = (0.0, 0.0, 0.0)

    def get_id(self):
        return self.id

    def get_tag(self):
        return self.tag

    def get_info(self):
        return self.info

    def get_pos(self):
        return self.pos

    def get_ni(self):
        return self.ni

    def set_tag(self, tag: float):
        self.tag = tag

    def set_info(self, info: str):
        self.info = info

    def set_pos(self, pos: tuple):
        self.pos = pos

    def __str__(self):
        return str(self.key)
