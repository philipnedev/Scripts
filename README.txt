Small scripts for Mac

ipadd.py
Scripts purpouse is to show ipaddress/mask/MAC/DG in pretty table in the format:
+-----------+--------------+-----------------+-------------------+-----------------+
| Interface |  IP Address  |       Mask      |     MAC Adress    | Default Gateway |
+-----------+--------------+-----------------+-------------------+-----------------+
|    en0    | 10.29.164.236| 255.255.255.0   | 21:21:21:11:11:11 |   10.29.164. 1  |
+-----------+--------------+-----------------+-------------------+-----------------+

pdg.py
finds the default gateway for en0 and starts pinging this IP address
