import web
import xml.etree.ElementTree as ET


# Loading file
tree = ET.parse('user_data.xml')
root = tree.getroot()

# Generating routes
urls = (
    '/users', 'list_users',
    '/users/(.*)', 'get_user',
    '/(.*)', 'hello',
)
app = web.application(urls, globals())


class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'


class list_users:
    def GET(self):
        output = 'users: '
        users = []
        for child in root:
            users.append(child.attrib)
        output += str(users)
        return output


class get_user:
    def GET(self, user):
        for child in root:
            if child.attrib['id'] == user:
                return str(child.attrib)


if __name__ == "__main__":
    app.run()
