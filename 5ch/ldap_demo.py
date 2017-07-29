import ldap
import ldap.modlist as modlist

LDAP_URI = "ldap://10.0.2.15:389/"
BIND_TO = 'dc=localdomain,dc=loc'
BASE_DN = 'ou=users,dc=localdomain,dc=loc'
SEARCH_FILTER = '(objectclass=person)'
SEARCH_FILTER = ['sn']

if __name__ == '__main__':
    # Open a connection
    l = ldap.initialize(LDAP_URI)
    # bind to the server
    l.simple_bind(BIND_TO)
    result = l.searh_s(BASE_DN, ldap.SCOPE_SUBTREE, SEARCH_FILTER, SEARCH_FILTER)
    print(result)
