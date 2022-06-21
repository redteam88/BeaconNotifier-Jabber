# BeaconNotifier-Jabber
Cobalt strike CNA script to notify you via Jabber whenever there is a new beacon.

Make sure you have python3 installed

Make sure you have xmpppy pip module installed

Steps:

1) register account for notifier script (404.city was tested, all works)
2) register account for you (if you need)
3) set up 2 jabber accounts: add to roster notify account and test that messages are sent from notify acc to your acc
4) Paste the notify account credentials in request.py
5) Edit the path of request.py in notify.cna
6) Edit the message as you want (Optional)
7) Run the cna as following:

./agscript [C2 IP] [C2 Port] [username] [C2 password] [path to cna]


![image](https://user-images.githubusercontent.com/21979646/151166400-26fbd802-e8fa-4a72-afb6-b334fb935c83.png)


Reference:
https://download.cobaltstrike.com/aggressor-script/functions.html