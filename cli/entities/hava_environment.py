class HavaEnvironment:
    def __init__(self, hava_env):
        self.id = hava_env["id"]
        self.name = hava_env["name"]
        self.state = hava_env["state"]
        self.current_revision = hava_env["current_revision"]["id"]
        self.share_id = ""

