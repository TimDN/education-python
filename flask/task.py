class Task:
    def __init__(self, id, title, assigned_to = "", completed = False, description = ""):
        self.__id = id
        self.title = title
        self.completed = completed
        self.assigned_to = assigned_to
        self.description = description

    @property
    def id(self):
        return self.__id

    def update(self, task_dict):
        if "title" in task_dict:
            self.title = task_dict["title"]
        if "description" in task_dict:
            self.descritpion = task_dict["description"]
        if "completed" in task_dict:
            self.completed = task_dict["completed"]
        if "assigned_to" in task_dict:
            self.assigned_to = task_dict["assigned_to"]

    def to_json(self):
        return {"id":self.__id, "title": self.title, "assigned_to": self.assigned_to,
         "completed": self.completed, "description":self.description}

def get_tasks():
   return [Task(0, "Take out trash", "Foo Bar"),
           Task(1, "Cath the Road Runner", "Wile Coyote", description="BEEP BEEP"),
           Task(2, "Hack the Planet", "The Plague", completed=True)]


