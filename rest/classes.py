class Group:
    def __init__(self, id, number, course, pulpit_id):
        self.id = id
        self.number = number
        self.course = course
        self.pulpit_id = pulpit_id

    def jason(self):
        response = {
            'id': self.id,
            'number': self.number,
            'course': self.course,
            'pulpit_id': self.pulpit_id
        }
        return response

    def sqlitify(self):
        response = (self.id, self.number, self.course, self.pulpit_id)
        return response

class Pulpit:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

    def jason(self):
        response = {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }
        return response

    def sqlitify(self):
        response = (self.id, self.title, self.description)
        return response

class Student:
    def __init__(self, id, name, phone, email, group_id):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.group_id = group_id

    def jason(self):
        response = {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'group_id': self.group_id
        }
        return response

    def sqlitify(self):
        response = (self.id, self.name, self.phone, self.email, self.group_id)
        return response

class Subject:
    def __init__(self, id, title, description, pulpit_id):
        self.id = id
        self.title = title
        self.description = description
        self.pulpit_id = pulpit_id

    def jason(self):
        response = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'pulpit_id': self.pulpit_id
        }
        return response

    def sqlitify(self):
        response = (self.id, self.title, self.description, self.pulpit_id)
        return response

class Teacher:
    def __init__(self, id, name, biography, phone, email):
        self.id = id
        self.name = name
        self.biography = biography
        self.phone = phone
        self.email = email

    def jason(self):
        response = {
            'id': self.id,
            'name': self.name,
            'biography': self.biography,
            'phone': self.phone,
            'email': self.email
        }
        return response

    def sqlitify(self):
        response = (self.id, self.name, self.biography, self.phone, self.email)
        return response
