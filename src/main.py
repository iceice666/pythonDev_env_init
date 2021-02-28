

class init():
    def __init__(self, name="main", needIcon=False):

        try:
            self.writeTaskfile(name, needIcon)
        except BaseException as e:
            from ui import debug
            debug(e)

    def writeTaskfile(self, name="main", needIcon=False):
        task = ""
        icon = ""

        if needIcon:
            icon = "\"--icon\",\"icon.ico\","
        elif not needIcon:
            icon = ""

        with open("TASK.json", encoding="UTF-8", mode="r") as f:
            task = f.read().replace("@{name}", name)\
                .replace("@{icon}", icon)

        with open(".vscode\\tasks.json", encoding="utf-8", mode="w") as f:
            f.write(task)
