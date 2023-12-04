class Job:
    def __init__(self, id, job_name, job_field, salary) -> None:
        self.id = id
        self.job_name = job_name
        self.job_field = job_field
        self.salary = salary
    
    def __str__(self) -> str:
        return f'ID: {self.id}, Tên: {self.job_name}, Lĩnh vực: {self.job_field}, Lương: {self.salary}'

class AI(Job):
    def __init__(self, job_code, job_name, field_name, salary, python_skill, ml_skill, deep_skill, math_skill):
        Job.__init__(self, job_code, job_name, field_name, salary)
        self.python_skill = python_skill
        self.ml_skill = ml_skill
        self.deep_skill = deep_skill
        self.math_skill = math_skill
        
    def __str__(self) -> str:
        return super().__str__() + f', Kỹ năng: {self.python_skill}, {self.ml_skill}, {self.deep_skill}, {self.math_skill}'
    
    def evaluate(self):
        score_dict = {
            "python_skill": self.python_skill,
            "ml_skill": self.ml_skill,
            "deep_skill": self.deep_skill,
            "math_skill": self.math_skill
        }
        score = sum(score_dict.values()) / 4
        
        if score > 9:
            return "Rất phù hợp"
        elif score > 7:
            return "Phù hợp"
        elif score > 5:
            return "Tạm được"
        elif score > 3:
            skill_under_4 = {key: value for (key, value) in score_dict.items() if value < 4}
            return f"Cần bổ sung thêm kiến thức, kỹ năng: {skill_under_4}"
        else:
            return "Bad"

class BackEnd(Job):
    def __init__(self, id, job_name, job_field, salary, SQL_skill, OOP_skill, Api_skill, Java_skill) -> None:
        Job.__init__(self, id, job_name, job_field, salary)
        self.Sql_skill = SQL_skill
        self.OOP_skill = OOP_skill
        self.Api_skill = Api_skill
        self.Java_skill = Java_skill
        
    def __str__(self) -> str:
        return super().__str__() + f', Kỹ năng: {self.Sql_skill}, {self.OOP_skill}, {self.Api_skill}, {self.Java_skill}'
    
    def evaluate(self):
        score_dict = {
            "sql_skill": self.Sql_skill,
            "oop_skill": self.OOP_skill,
            "api_skill": self.Api_skill,
            "java_skill": self.Java_skill
        }
        score = sum(score_dict.values()) / 4
        if score > 9:
            return "Rất phù hợp"
        elif score > 7:
            return "Phù hợp"
        elif score > 5:
            return "Tạm được"
        elif score > 3:
            skill_under_4 = {key: value for (key, value) in score_dict.items() if value < 4}
            return f"Cần bổ sung thêm kiến thức, kỹ năng: {skill_under_4}"
        else:
            return "Bad"

class FrontEnd(Job):
    def __init__(self, id, job_name, job_field, salary, HTML_skill, CSS_skill, Nodejs_skill, UX, UI) -> None:
        Job.__init__(self, id, job_name, job_field, salary)
        self.HTML_skill = HTML_skill
        self.CSS_skill = CSS_skill
        self.Nodejs_skill = Nodejs_skill
        self.UX = UX
        self.UI = UI
    
    def __str__(self) -> str:
        return super().__str__() + f', Kỹ năng: {self.HTML_skill}, {self.CSS_skill}, {self.Nodejs_skill}, {self.UX}, {self.UI}'
    
    def evaluate(self):
        score_dict = {
            "html_skill": self.HTML_skill,
            "css_skill": self.CSS_skill,
            "nodejs_skill": self.Nodejs_skill,
            "ux_skill": self.UX,
            "ui_skill": self.UI
        }
        score = sum(score_dict.values()) / 5
        if score > 9:
            return "Rất phù hợp"
        elif score > 7:
            return "Phù hợp"
        elif score > 5:
            return "Tạm được"
        elif score > 3:
            skill_under_4 = {key: value for (key, value) in score_dict.items() if value < 4}
            return f"Cần bổ sung thêm kiến thức, kỹ năng: {skill_under_4}"
        else:
            return "Bad"

class FullStack(BackEnd, FrontEnd):
    def __init__(self, job_code, job_name, field_name, salary, sql_skill, oop_skill, api_skill, java_skill, html_skill, css_skill, nodejs_skill, ux_skill, ui_skill):
        BackEnd.__init__(self,job_code, job_name, field_name, salary, sql_skill, oop_skill, api_skill, java_skill)
        FrontEnd.__init__(self, job_code, job_name, field_name, salary, html_skill, css_skill, nodejs_skill, ux_skill, ui_skill)
    
    def __str__(self) -> str:
        return super().__str__() + f', {self.HTML_skill}, {self.CSS_skill}, {self.Nodejs_skill}, {self.UX}, {self.UI}'
    
    def evaluate(self):
        score_dict = {
            "sql_skill": self.Sql_skill,
            "oop_skill": self.OOP_skill,
            "api_skill": self.Api_skill,
            "java_skill": self.Java_skill,
            "html_skill": self.HTML_skill,
            "css_skill": self.CSS_skill,
            "nodejs_skill": self.Nodejs_skill,
            "ux_skill": self.UX,
            "ui_skill": self.UI
        }
        score = sum(score_dict.values()) / 9
        if score > 9:
            return "Rất phù hợp"
        elif score > 7:
            return "Phù hợp"
        elif score > 5:
            return "Tạm được"
        elif score > 3:
            skill_under_4 = {key: value for (key, value) in score_dict.items() if value < 4}
            return f"Cần bổ sung thêm kiến thức, kỹ năng: {skill_under_4}"
        else:
            return "Bad"

if __name__ == '__main__':
    # Create 4 object AI, BackEnd, FrontEnd, FullStack
    ai = AI(1, "AI", "IT", 2000, 10, 1, 1, 2)
    backend = BackEnd(2, "BackEnd", "IT", 1500, 0, 1, 2, 3)
    frontend = FrontEnd(3, "FrontEnd", "IT", 1250, 10, 10, 10, 10, 10)
    fullstack = FullStack(4, "FullStack", "IT", 2500, 10, 10, 10, 10, 10, 10, 10, 10, 10)
    
    print("\n\n")
    print("AI: ", ai.evaluate())
    print(ai)
    print("\n\n")
    print("BackEnd: ", backend.evaluate())
    print(backend)
    print("\n\n")
    print("FrontEnd: ", frontend.evaluate())
    print(frontend)
    print("\n\n")
    print("FullStack: ", fullstack.evaluate())
    print(fullstack)
    print("\n\n")