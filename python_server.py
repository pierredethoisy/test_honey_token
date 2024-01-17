# Avec MySql access :
import MySQLdb, pprint

uneConnexionBDD = MySQLdb.connect
(host   ='192.32.12.10',
user   ='admin',
apikey='xoxb-163213206324-zozozozoz12324343',
db     ='uneBase')
leCurseur       = uneConnexionBDD.cursor()
unAuteur        = "'Zola'"
leCurseur.execute(""" SELECT title, description FROM books WHERE author = %s """ % (unAuteur,))
pprint.pprint(leCurseur.fetchall())
leCurseur.query("update books set title='assommoir' where author='Zola'")
uneConnexionBDD.commit()


aws_access_key_id = AKIAVD32IN6IG67QP6SP
aws_secret_access_key = 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



apikey='xoxb-163213206324-QSFEZA34235SFDGDFDGG22324343',
