
import sys
try:
	import xmpp
except ImportError:
	print("[!] please pip3 install xmpppy")


def send_xmpp_notify(text=""):
	#Change here
	jidparams = {
		'jid': "beaconnotify@404.city/resource",
		'password': "yourpassword",
	}

	senderList = ["mainacc@404.city"]

	jid=xmpp.protocol.JID(jidparams['jid'])
	cl=xmpp.Client(jid.getDomain(),debug=[])
	con=cl.connect()
	if not con:
		print('could not connect!')
		raise Exception("Fail in connect to jabber")
		return
	print('connected with',con)
	auth=cl.auth(jid.getNode(),jidparams['password'], resource=jid.getResource())
	if not auth:
		print('could not authenticate!')
		raise Exception("Fail in authenticate")
		return
	print('authenticated using',auth)

	#cl.SendInitPresence(requestRoster=0)   # you may need to uncomment this for old server

	for tojid in senderList:
		try:
			id=cl.send(xmpp.protocol.Message(tojid, text))
			print('sent message with id ',id)
		except Exception as exc:
			print("error: {}".format(str(exc)))
			raise Exception("Fail in send to jabber")



send_xmpp_notify(text=str(sys.argv[1]))