# Mapping objects used for the loading of data into the database


# Mappings for chicago census blocks shape file. This object will map the header
# names in the shape file to match the column names in the database
chicago_census_blocks_mapping = {
    'ID': 'GEOID',
    'geom': 'MULTIPOLYGON',
}


# Mappings for chicago community area shape file. This object will map the header
# names in the shape file to match the column names in the database
community_area_mapping = {
    'ID': 'area_numbe',
    'geom': 'MULTIPOLYGON',
}


# This object is used to map IUCR codes to the crime types defined in the database
IUCR_crime_type_mapping = {
    '110': 'HOMICIDE',
    '130': 'HOMICIDE',
    '141': 'HOMICIDE',
    '142': 'HOMICIDE',
    '261': 'SEXUAL ASSAULT',
    '262': 'SEXUAL ASSAULT',
    '263': 'SEXUAL ASSAULT',
    '264': 'SEXUAL ASSAULT',
    '265': 'SEXUAL ASSAULT',
    '266': 'SEXUAL ASSAULT',
    '271': 'SEXUAL ASSAULT',
    '272': 'SEXUAL ASSAULT',
    '273': 'SEXUAL ASSAULT',
    '274': 'SEXUAL ASSAULT',
    '275': 'SEXUAL ASSAULT',
    '281': 'SEXUAL ASSAULT',
    '291': 'SEXUAL ASSAULT',
    '312': 'ROBBERY',
    '313': 'ROBBERY',
    '031A': 'ROBBERY',
    '031B': 'ROBBERY',
    '320': 'ROBBERY',
    '325': 'ROBBERY',
    '326': 'ROBBERY',
    '330': 'ROBBERY',
    '331': 'ROBBERY',
    '334': 'ROBBERY',
    '337': 'ROBBERY',
    '033A': 'ROBBERY',
    '033B': 'ROBBERY',
    '340': 'ROBBERY',
    '041A': 'BATTERY',
    '041B': 'BATTERY',
    '420': 'BATTERY',
    '430': 'BATTERY',
    '440': 'BATTERY',
    '450': 'BATTERY',
    '451': 'BATTERY',
    '452': 'BATTERY',
    '453': 'BATTERY',
    '454': 'BATTERY',
    '460': 'BATTERY',
    '461': 'BATTERY',
    '462': 'BATTERY',
    '470': 'PUBLIC PEACE VIOLATION',
    '475': 'BATTERY',
    '479': 'BATTERY',
    '480': 'BATTERY',
    '481': 'BATTERY',
    '482': 'BATTERY',
    '483': 'BATTERY',
    '484': 'BATTERY',
    '485': 'BATTERY',
    '486': 'BATTERY',
    '487': 'BATTERY',
    '488': 'BATTERY',
    '489': 'BATTERY',
    '490': 'RITUALISM',
    '491': 'RITUALISM',
    '492': 'RITUALISM',
    '493': 'RITUALISM',
    '494': 'RITUALISM',
    '495': 'BATTERY',
    '496': 'BATTERY',
    '497': 'BATTERY',
    '498': 'BATTERY',
    '510': 'RITUALISM',
    '051A': 'ASSAULT',
    '051B': 'ASSAULT',
    '520': 'ASSAULT',
    '530': 'ASSAULT',
    '545': 'ASSAULT',
    '550': 'ASSAULT',
    '551': 'ASSAULT',
    '552': 'ASSAULT',
    '553': 'ASSAULT',
    '554': 'ASSAULT',
    '555': 'ASSAULT',
    '556': 'ASSAULT',
    '557': 'ASSAULT',
    '558': 'ASSAULT',
    '560': 'ASSAULT',
    '580': 'STALKING',
    '581': 'STALKING',
    '583': 'STALKING',
    '584': 'STALKING',
    '610': 'BURGLARY',
    '620': 'BURGLARY',
    '630': 'BURGLARY',
    '650': 'BURGLARY',
    '810': 'THEFT',
    '820': 'THEFT',
    '850': 'THEFT',
    '860': 'THEFT',
    '865': 'THEFT',
    '870': 'THEFT',
    '880': 'THEFT',
    '890': 'THEFT',
    '895': 'THEFT',
    '910': 'MOTOR VEHICLE THEFT',
    '915': 'MOTOR VEHICLE THEFT',
    '917': 'MOTOR VEHICLE THEFT',
    '918': 'MOTOR VEHICLE THEFT',
    '920': 'MOTOR VEHICLE THEFT',
    '925': 'MOTOR VEHICLE THEFT',
    '927': 'MOTOR VEHICLE THEFT',
    '928': 'MOTOR VEHICLE THEFT',
    '930': 'MOTOR VEHICLE THEFT',
    '935': 'MOTOR VEHICLE THEFT',
    '937': 'MOTOR VEHICLE THEFT',
    '938': 'MOTOR VEHICLE THEFT',
    '1010': 'ARSON',
    '1020': 'ARSON',
    '1025': 'ARSON',
    '1030': 'ARSON',
    '1035': 'ARSON',
    '1050': 'HUMAN TRAFFICKING',
    '1055': 'HUMAN TRAFFICKING',
    '1090': 'ARSON',
    '1110': 'DECEPTIVE PRACTICE',
    '1120': 'DECEPTIVE PRACTICE',
    '1121': 'DECEPTIVE PRACTICE',
    '1122': 'DECEPTIVE PRACTICE',
    '1130': 'DECEPTIVE PRACTICE',
    '1135': 'DECEPTIVE PRACTICE',
    '1140': 'DECEPTIVE PRACTICE',
    '1150': 'DECEPTIVE PRACTICE',
    '1151': 'DECEPTIVE PRACTICE',
    '1152': 'DECEPTIVE PRACTICE',
    '1153': 'DECEPTIVE PRACTICE',
    '1154': 'DECEPTIVE PRACTICE',
    '1155': 'DECEPTIVE PRACTICE',
    '1156': 'DECEPTIVE PRACTICE',
    '1160': 'DECEPTIVE PRACTICE',
    '1170': 'DECEPTIVE PRACTICE',
    '1185': 'DECEPTIVE PRACTICE',
    '1195': 'DECEPTIVE PRACTICE',
    '1200': 'DECEPTIVE PRACTICE',
    '1205': 'DECEPTIVE PRACTICE',
    '1206': 'DECEPTIVE PRACTICE',
    '1210': 'DECEPTIVE PRACTICE',
    '1220': 'DECEPTIVE PRACTICE',
    '1230': 'DECEPTIVE PRACTICE',
    '1235': 'DECEPTIVE PRACTICE',
    '1240': 'DECEPTIVE PRACTICE',
    '1241': 'DECEPTIVE PRACTICE',
    '1242': 'DECEPTIVE PRACTICE',
    '1245': 'DECEPTIVE PRACTICE',
    '1255': 'DECEPTIVE PRACTICE',
    '1260': 'DECEPTIVE PRACTICE',
    '1624': 'GAMBLING',
    '1261': 'DECEPTIVE PRACTICE',
    '1265': 'CRIMINAL DAMAGE',
    '1305': 'CRIMINAL DAMAGE',
    '1310': 'CRIMINAL DAMAGE',
    '1320': 'CRIMINAL DAMAGE',
    '1330': 'CRIMINAL TRESPASS',
    '1335': 'CRIMINAL TRESPASS',
    '1340': 'CRIMINAL DAMAGE',
    '1345': 'CRIMINAL DAMAGE',
    '1350': 'CRIMINAL TRESPASS',
    '1360': 'CRIMINAL TRESPASS',
    '1365': 'CRIMINAL TRESPASS',
    '1370': 'CRIMINAL DAMAGE',
    '1375': 'CRIMINAL DAMAGE',
    '141A': 'WEAPONS VIOLATION',
    '141B': 'WEAPONS VIOLATION',
    '141C': 'WEAPONS VIOLATION',
    '142A': 'WEAPONS VIOLATION',
    '142B': 'WEAPONS VIOLATION',
    '1435': 'WEAPONS VIOLATION',
    '143A': 'WEAPONS VIOLATION',
    '143B': 'WEAPONS VIOLATION',
    '143C': 'WEAPONS VIOLATION',
    '1440': 'WEAPONS VIOLATION',
    '1450': 'WEAPONS VIOLATION',
    '1460': 'WEAPONS VIOLATION',
    '1475': 'WEAPONS VIOLATION',
    '1476': 'WEAPONS VIOLATION',
    '1477': 'WEAPONS VIOLATION',
    '1478': 'CONCEALED CARRY LICENSE VIOLATION',
    '1479': 'CONCEALED CARRY LICENSE VIOLATION',
    '1480': 'CONCEALED CARRY LICENSE VIOLATION',
    '1481': 'NON-CRIMINAL',
    '1505': 'PROSTITUTION',
    '1506': 'PROSTITUTION',
    '1507': 'PROSTITUTION',
    '1510': 'PROSTITUTION',
    '1511': 'PROSTITUTION',
    '1512': 'PROSTITUTION',
    '1513': 'PROSTITUTION',
    '1515': 'PROSTITUTION',
    '1520': 'PROSTITUTION',
    '1521': 'PROSTITUTION',
    '1525': 'PROSTITUTION',
    '1526': 'PROSTITUTION',
    '1530': 'PROSTITUTION',
    '1531': 'PROSTITUTION',
    '1535': 'OBSCENITY',
    '1536': 'PUBLIC INDECENCY',
    '1537': 'OFFENSE INVOLVING CHILDREN',
    '1540': 'OBSCENITY',
    '1541': 'OBSCENITY',
    '1542': 'OBSCENITY',
    '1544': 'SEX OFFENSE',
    '1549': 'PROSTITUTION',
    '1562': 'SEX OFFENSE',
    '1563': 'SEX OFFENSE',
    '1564': 'SEX OFFENSE',
    '1565': 'SEX OFFENSE',
    '1566': 'SEX OFFENSE',
    '1570': 'SEX OFFENSE',
    '1572': 'SEX OFFENSE',
    '1574': 'SEX OFFENSE',
    '1576': 'SEX OFFENSE',
    '1578': 'SEX OFFENSE',
    '1580': 'SEX OFFENSE',
    '1582': 'OFFENSE INVOLVING CHILDREN',
    '1585': 'SEX OFFENSE',
    '1590': 'SEX OFFENSE',
    '1610': 'GAMBLING',
    '1611': 'GAMBLING',
    '1620': 'GAMBLING',
    '1621': 'GAMBLING',
    '1622': 'GAMBLING',
    '1623': 'GAMBLING',
    '1625': 'GAMBLING',
    '1626': 'GAMBLING',
    '1627': 'GAMBLING',
    '1630': 'GAMBLING',
    '1631': 'GAMBLING',
    '1632': 'GAMBLING',
    '1633': 'GAMBLING',
    '1640': 'GAMBLING',
    '1650': 'GAMBLING',
    '1651': 'GAMBLING',
    '1661': 'GAMBLING',
    '1670': 'GAMBLING',
    '1680': 'GAMBLING',
    '1681': 'GAMBLING',
    '1682': 'OTHER OFFENSE',
    '1690': 'GAMBLING',
    '1691': 'GAMBLING',
    '1692': 'GAMBLING',
    '1693': 'GAMBLING',
    '1694': 'GAMBLING',
    '1695': 'GAMBLING',
    '1696': 'GAMBLING',
    '1697': 'GAMBLING',
    '1710': 'OFFENSE INVOLVING CHILDREN',
    '1715': 'OFFENSE INVOLVING CHILDREN',
    '1720': 'OFFENSE INVOLVING CHILDREN',
    '1725': 'OFFENSE INVOLVING CHILDREN',
    '1750': 'OFFENSE INVOLVING CHILDREN',
    '1751': 'OFFENSE INVOLVING CHILDREN',
    '1752': 'OFFENSE INVOLVING CHILDREN',
    '1753': 'OFFENSE INVOLVING CHILDREN',
    '1754': 'OFFENSE INVOLVING CHILDREN',
    '1755': 'OFFENSE INVOLVING CHILDREN',
    '1775': 'OFFENSE INVOLVING CHILDREN',
    '1780': 'OFFENSE INVOLVING CHILDREN',
    '1790': 'OFFENSE INVOLVING CHILDREN',
    '1791': 'OFFENSE INVOLVING CHILDREN',
    '1792': 'KIDNAPPING',
    '1811': 'NARCOTICS',
    '1812': 'NARCOTICS',
    '1821': 'NARCOTICS',
    '1822': 'NARCOTICS',
    '1840': 'NARCOTICS',
    '1850': 'NARCOTICS',
    '1860': 'NARCOTICS',
    '1900': 'OTHER NARCOTIC VIOLATION',
    '2010': 'NARCOTICS',
    '2011': 'NARCOTICS',
    '2012': 'NARCOTICS',
    '2013': 'NARCOTICS',
    '2014': 'NARCOTICS',
    '2015': 'NARCOTICS',
    '2016': 'NARCOTICS',
    '2017': 'NARCOTICS',
    '2018': 'NARCOTICS',
    '2019': 'NARCOTICS',
    '2020': 'NARCOTICS',
    '2021': 'NARCOTICS',
    '2022': 'NARCOTICS',
    '2023': 'NARCOTICS',
    '2024': 'NARCOTICS',
    '2025': 'NARCOTICS',
    '2026': 'NARCOTICS',
    '2027': 'NARCOTICS',
    '2028': 'NARCOTICS',
    '2029': 'NARCOTICS',
    '2030': 'NARCOTICS',
    '2031': 'NARCOTICS',
    '2032': 'NARCOTICS',
    '2033': 'NARCOTICS',
    '2034': 'NARCOTICS',
    '2040': 'NARCOTICS',
    '2050': 'NARCOTICS',
    '2060': 'NARCOTICS',
    '2070': 'NARCOTICS',
    '2080': 'NARCOTICS',
    '2090': 'NARCOTICS',
    '2091': 'NARCOTICS',
    '2092': 'NARCOTICS',
    '2093': 'NARCOTICS',
    '2094': 'NARCOTICS',
    '2095': 'NARCOTICS',
    '2110': 'NARCOTICS',
    '2111': 'NARCOTICS',
    '2120': 'NARCOTICS',
    '2160': 'NARCOTICS',
    '2170': 'NARCOTICS',
    '2210': 'LIQUOR LAW VIOLATION',
    '2220': 'LIQUOR LAW VIOLATION',
    '2230': 'LIQUOR LAW VIOLATION',
    '2240': 'LIQUOR LAW VIOLATION',
    '2250': 'LIQUOR LAW VIOLATION',
    '2251': 'LIQUOR LAW VIOLATION',
    '2500': 'CRIMINAL ABORTION',
    '2820': 'OTHER OFFENSE',
    '2825': 'OTHER OFFENSE',
    '2826': 'OTHER OFFENSE',
    '2830': 'OTHER OFFENSE',
    '2840': 'PUBLIC PEACE VIOLATION',
    '2850': 'PUBLIC PEACE VIOLATION',
    '2851': 'PUBLIC PEACE VIOLATION',
    '2860': 'PUBLIC PEACE VIOLATION',
    '2870': 'PUBLIC PEACE VIOLATION',
    '2890': 'PUBLIC PEACE VIOLATION',
    '2895': 'PUBLIC PEACE VIOLATION',
    '2900': 'WEAPONS VIOLATION',
    '3000': 'PUBLIC PEACE VIOLATION',
    '3100': 'PUBLIC PEACE VIOLATION',
    '3200': 'PUBLIC PEACE VIOLATION',
    '3300': 'PUBLIC PEACE VIOLATION',
    '3400': 'PUBLIC PEACE VIOLATION',
    '3610': 'OTHER OFFENSE',
    '3710': 'INTERFERENCE WITH PUBLIC OFFICER',
    '3720': 'INTERFERENCE WITH PUBLIC OFFICER',
    '3730': 'INTERFERENCE WITH PUBLIC OFFICER',
    '3731': 'INTERFERENCE WITH PUBLIC OFFICER',
    '3740': 'INTERFERENCE WITH PUBLIC OFFICER',
    '3750': 'INTERFERENCE WITH PUBLIC OFFICER',
    '3751': 'INTERFERENCE WITH PUBLIC OFFICER',
    '3760': 'INTERFERENCE WITH PUBLIC OFFICER',
    '3770': 'INTERFERENCE WITH PUBLIC OFFICER',
    '3800': 'INTERFERENCE WITH PUBLIC OFFICER',
    '3910': 'INTERFERENCE WITH PUBLIC OFFICER',
    '3920': 'INTERFERENCE WITH PUBLIC OFFICER',
    '3960': 'INTIMIDATION',
    '3966': 'INTIMIDATION',
    '3970': 'INTIMIDATION',
    '3975': 'INTIMIDATION',
    '3980': 'INTIMIDATION',
    '4210': 'KIDNAPPING',
    '4220': 'KIDNAPPING',
    '4230': 'KIDNAPPING',
    '4240': 'KIDNAPPING',
    '4255': 'KIDNAPPING',
    '4310': 'OTHER OFFENSE',
    '4386': 'OTHER OFFENSE',
    '4387': 'OTHER OFFENSE',
    '4388': 'OTHER OFFENSE',
    '4389': 'OTHER OFFENSE ',
    '4410': 'OTHER OFFENSE',
    '4420': 'OTHER OFFENSE',
    '4510': 'OTHER OFFENSE',
    '4625': 'OTHER OFFENSE',
    '4650': 'OTHER OFFENSE',
    '4651': 'OTHER OFFENSE',
    '4652': 'OTHER OFFENSE',
    '4740': 'OTHER OFFENSE',
    '4750': 'OTHER OFFENSE',
    '4800': 'OTHER OFFENSE',
    '4810': 'OTHER OFFENSE',
    '4860': 'OTHER OFFENSE',
    '5000': 'OTHER OFFENSE',
    '5001': 'OTHER OFFENSE',
    '5002': 'OTHER OFFENSE',
    '5003': 'OTHER OFFENSE',
    '5004': 'SEX OFFENSE',
    '5007': 'OTHER OFFENSE',
    '5009': 'OTHER OFFENSE',
    '500E': 'OTHER OFFENSE',
    '500N': 'OTHER OFFENSE',
    '5011': 'OTHER OFFENSE',
    '501A': 'OTHER OFFENSE',
    '501H': 'OTHER OFFENSE',
    '502P': 'OTHER OFFENSE',
    '502R': 'OTHER OFFENSE',
    '502T': 'OTHER OFFENSE',
    '5110': 'OTHER OFFENSE',
    '5111': 'OTHER OFFENSE',
    '5112': 'OTHER OFFENSE',
    '5120': 'OTHER OFFENSE',
    '5121': 'OTHER OFFENSE',
    '5122': 'OTHER OFFENSE',
    '5130': 'OTHER OFFENSE',
    '5131': 'OTHER OFFENSE',
    '5132': 'OTHER OFFENSE'
}
