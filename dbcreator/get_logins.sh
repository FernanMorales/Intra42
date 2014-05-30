ldapsearch picture | grep "uid=" | grep -v "event" | grep -v "application" | grep -v "bannis" | sed "s/dn: uid=//g" | sed "s/,ou=2013,ou=people,dc=42,dc=fr//g"
