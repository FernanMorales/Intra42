from auth42 import Auth42
from annuaire.models import Student

ldap = Auth42()

with open("login") as f:
    for line in f:
        try:
            s = Student(login=line.strip(),
                        firstname=ldap.ldap_get_firstname(line.strip()),
                        lastname=ldap.ldap_get_lastname(line.strip()),
                        photo=ldap.ldap_get_picture(line.strip()))
            s.save()
        except TypeError:
            print line
        except AttributeError:
            print line
