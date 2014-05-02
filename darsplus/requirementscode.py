__author__ = 'Jessica'
from darsplus.models import getCourseUnits
import re
import os, sys
class MyError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)
def main():
	print 'hello'
#http://ls-advise.berkeley.edu/requirement/breadth7/al.html


artAndLit={'AFRICAM.4A':'AfricanAmerican 4A','AFRICAM.5A':'AfricanAmerican 5A','AFRICAM.5B':'AfricanAmerican 5B','AFRICAM.26':'AfricanAmerican 26','AFRICAM.29AC':'AfricanAmerican 29AC','AFRICAM.39A':'AfricanAmerican 39A','AFRICAM.39G':'AfricanAmerican 39G',
	'AFRICAM.100':'AfricanAmerican 100','AFRICAM.142A':'AfricanAmerican 142A','AFRICAM.142B':'AfricanAmerican 142B','AFRICAM.142AC':'AfricanAmerican 142AC','AFRICAM.142C':'AfricanAmerican 142C','AFRICAM.142D':'AfricanAmerican 142D',
	'AFRICAM.150A':'AfricanAmerican 150A','AFRICAM.150B':'AfricanAmerican 150B','AFRICAM.N150B':'AfricanAmerican N150B','AFRICAM.151B':'AfricanAmerican 151B','AFRICAM.152A':'AfricanAmerican 152A','AFRICAM.152E':'AfricanAmerican 152E','AFRICAM.152F':'AfricanAmerican 152F','AFRICAM.153C':'AfricanAmerican 153C','AFRICAM.154':'AfricanAmerican 154','AFRICAM.155':'AfricanAmerican 155',
	'AFRICAM.156AC':'AfricanAmerican 156AC','AFRICAM.157':'AfricanAmerican 157','AFRICAM.158A':'AfricanAmerican 158A','AFRICAM.158B':'AfricanAmerican 158B','AFRICAM.159':'AfricanAmerican 159','AFRICAM.160':'AfricanAmerican 160','AFRICAM.161':'AfricanAmerican 161','AFRICAM.162':'AfricanAmerican 162','AFRICAM.163':'AfricanAmerican 163',
	'AMERSTD.C10':'AmericanStudies C10','AMERSTD.C111E':'AmericanStudies C111E','AMERSTD.C112F':'AmericanStudies C112F','AMERSTD.C174':'AmericanStudies C174',
	'ANTHRO.129A':'Antro 129A','ANTHRO.C146':'Antro C146','ANTHRO.160AC':'Antro 160AC','ANTHRO.162':'Antro 162','ANTHRO.162AC':'Antro 162AC','ANTHRO.163AC':'Antro 163AC',
	'ARABIC.104A':'Arabic 104A','ARABIC.104B':'Arabic 104B','ARABIC.105A':'Arabic 105A','ARABIC.105B':'Arabic 105B','ARABIC.106':'Arabic 106','ARABIC.108':'Arabic 108','ARABIC.111A':'Arabic 111A','ARABIC.111B':'Arabic 111B','ARABIC.120A':'Arabic 120A','ARABIC.120B':'Arabic 120B','ARABIC.148':'Arabic 148',
	'ARCH.39D':'Arch 39D','ARCH.100A':'Arch 100A','ARCH.100B':'Arch 100B','ARCH.100C':'Arch 100C','ARCH.100D':'Arch 100D','ARCH.101':'Arch 101','ARCH.102':'Arch 102','ARCH.109':'Arch 109','ARCH.109A':'Arch 109A','ARCH.109B':'Arch 109B','ARCH.109C':'Arch 109C','ARCH.135':'Arch 135','ARCH.160':'Arch 160',
	'ARCH.170A':'Arch 170A','ARCH.170B':'Arch 170B','ARCH.171':'Arch 171','ARCH.172':'Arch 172','ARCH.173':'Arch 173','ARCH.173B':'Arch 173B','ARCH.174A':'Arch 174A','ARCH.174B':'Arch 174B','ARCH.174C':'Arch 174C',
	'ARCH.175A':'Arch 175A','ARCH.175B':'Arch 175B','ARCH.175C':'Arch 175C','ARCH.175D':'Arch 175D',
	'ASAMST.170':'AsianAmerican 170','ASAMST.171':'AsianAmerican 171','ASAMST.172':'AsianAmerican 172','ASAMST.173':'AsianAmerican 173','ASAMST.175':'AsianAmerican 175','ASAMST.176':'AsianAmerican 176','ASAMST.177':'AsianAmerican 177','ASAMST.179':'AsianAmerican 179',
	'ASAMST.180':'AsianAmerican 180','ASAMST.181':'AsianAmerican 181','ASAMST.183':'AsianAmerican 183','ASAMST.184':'AsianAmerican 184','ASAMST.187':'AsianAmerican 187',
	'ASIANST.110':'AsianStudies 110',
	'BUDDSTD.C124':'Buddhist C124','BUDDSTD.C140':'Buddhist C140',
	'CELTIC.105B':'Celtic 105B','CELTIC.106C':'Celtic 106C','CELTIC.116B':'Celtic 116B','CELTIC.118A':'Celtic 118A','CELTIC.118B':'Celtic 118B','CELTIC.119A':'Celtic 119A',
	'CELTIC.119B':'Celtic 119B','CELTIC.125':'Celtic 125','CELTIC.126':'Celtic 126','CELTIC.129':'Celtic 129','CELTIC.138':'Celtic 138','CELTIC.139':'Celtic 139',
	'CELTIC.146A':'Celtic 146A','CELTIC.146B':'Celtic 146B','CELTIC.C168':'Celtic C168','CELTIC.169':'Celtic 169','CELTIC.171':'Celtic 171',
	'CHICANO.20':'Chicano 20','CHICANO.40':'Chicano 40','CHICANO.130':'Chicano 130','CHICANO.133':'Chicano 133','CHICANO.135':'Chicano 135','CHICANO.135A':'Chicano 135A','CHICANO.135B':'Chicano 135B',
	'CHICANO.135C':'Chicano 135C','CHICANO.141':'Chicano 141','CHICANO.142':'Chicano 142','CHICANO.143':'Chicano 143','CHICANO.148':'Chicano 148','CHICANO.149':'Chicano 149',
	'CHINESE.7A':'Chinese 7A','CHINESE.7B':'Chinese 7B','CHINESE.50':'Chinese 50','CHINESE.80':'Chinese 80','CHINESE.101':'Chinese 101', 'CHINESE.110':'Chinese 110','CHINESE.110A':'Chinese 110A','CHINESE.110B':'Chinese 110B','CHINESE.111':'Chinese 111','CHINESE.112':'Chinese 112','CHINESE.120':'Chinese 120','CHINESE.122':'Chinese 122','CHINESE.132':'Chinese 132','CHINESE.134':'Chinese 134',
	'CHINESE.136':'Chinese 136','CHINESE.138':'Chinese 138','CHINESE.C140':'Chinese C140','CHINESE.142':'Chinese 142','CHINESE.153':'Chinese 153','CHINESE.154':'Chinese 154','CHINESE.155':'Chinese 155','CHINESE.156':'Chinese 156','CHINESE.157':'Chinese 157','CHINESE.158':'Chinese 158','CHINESE.159':'Chinese 159',
	'CHINESE.180':'Chinese 180','CHINESE.181A':'Chinese 181A','CHINESE.181B':'Chinese 181B','CHINESE.182':'Chinese 182','CHINESE.183':'Chinese 183','CHINESE.C184':'Chinese C184','CHINESE.186':'Chinese 186','CHINESE.187':'Chinese 187','CHINESE.188':'Chinese 188','CHINESE.189':'Chinese 189',
	'CLASSIC.10A':'Classics 10A','CLASSIC.10B':'Classics 10B','CLASSIC.17A':'Classics 17A','CLASSIC.17B':'Classics 17B','CLASSIC.30B':'Classics 30B','CLASSIC.34':'Classics 34','CLASSIC.35':'Classics 35',
	'CLASSIC.39A':'Classics 39A','CLASSIC.39B':'Classics 39B','CLASSIC.39C':'Classics 39C','CLASSIC.39D':'Classics 39D','CLASSIC.39H':'Classics 39H','CLASSIC.39J':'Classics 39J','CLASSIC.R44':'Classics R44','CLASSIC.100A':'Classics 100A','CLASSIC.100B':'Classics 100B','CLASSIC.110':'Classics 110','CLASSIC.124':'Classics 124','CLASSIC.161':'Classics 161',
	'CLASSIC.170A':'Classics 170A','CLASSIC.170B':'Classics 170B','CLASSIC.170C':'Classics 170C','CLASSIC.170D':'Classics 170D','CLASSIC.175A':'Classics 175A',
	'CLASSIC.175B':'Classics 175B','CLASSIC.175C':'Classics 175C','CLASSIC.175D':'Classics 175D','CLASSIC.175E':'Classics 175E','CLASSIC.175F':'Classics 175F','CLASSIC.175G':'Classics 175G','CLASSIC.178':'Classics 178',
	'COLWRIT.N2':'CollegeWriting N2','COLWRIT.105':'CollegeWriting 105','COLWRIT.106':'CollegeWriting 106','COLWRIT.108':'CollegeWriting 108','COLWRIT.110':'CollegeWriting 110',
	'DUTCH.140':'Dutch 140','DUTCH.150':'Dutch 150','DUTCH.160':'Dutch 160','DUTCH.161':'Dutch 161','DUTCH.162':'Dutch 162','DUTCH.163':'Dutch 163','DUTCH.164':'Dutch 164','DUTCH.165':'Dutch 165',
	'DUTCH.166':'Dutch 166','DUTCH.177':'Dutch 177',
	'EALANG.105':'EastAsianLanguages 105','EALANG.106':'EastAsianLanguages 106','EALANG.C124':'EastAsianLanguages C124','EALANG.180':'EastAsianLanguages 180','EALANG.181':'EastAsianLanguages 181',
	'EDUC.C144':'Educ C144',
	'ENVDES.4A':'EnvironDesign 4A',
	'ESPM.C12':'ESPM C12','ESPM.C191':'ESPM C191',
	'ETHSTD.100':'EthnicStudies 100','ETHSTD.101B':'EthnicStudies 101B','ETHSTD.110':'EthnicStudies 110','ETHSTD.122AC':'EthnicStudies 122AC','ETHSTD.124':'EthnicStudies 124','ETHSTD.128':'EthnicStudies 128','ETHSTD.174':'EthnicStudies 174','ETHSTD.175':'EthnicStudies 175','ETHSTD.176':'EthnicStudies 176',
	'FRENCH.39A':'French 39A','FRENCH.39B':'French 39B','FRENCH.39C':'French 39C','FRENCH.41':'French 41','FRENCH.103A':'French 103A','FRENCH.103B':'French 103B','FRENCH.112A':'French 112A','FRENCH.112B':'French 112B','FRENCH.114A':'French 114A','FRENCH.114B':'French 114B',
	'FRENCH.116A':'French 116A','FRENCH.116B':'French 116B','FRENCH.117A':'French 117A','FRENCH.117B':'French 117B','FRENCH.118A':'French 118A','FRENCH.118B':'French 118B','FRENCH.119A':'French 119A','FRENCH.119B':'French 119B','FRENCH.120A':'French 120A','FRENCH.120B':'French 120B',
	'FRENCH.121A':'French 121A','FRENCH.121B':'French 121B','FRENCH.122A':'French 122A','FRENCH.122B':'French 122B','FRENCH.123':'French 123','FRENCH.124A':'French 124A','FRENCH.124B':'French 124B','FRENCH.125A':'French 125A','FRENCH.125B':'French 125B','FRENCH.139':'French 139',
	'FRENCH.140A':'French 140A','FRENCH.140B':'French 140B','FRENCH.140C':'French 140C','FRENCH.140D':'French 140D','FRENCH.141':'French 141','FRENCH.145':'French 145','FRENCH.150A':'French 150A','FRENCH.150B':'French 150B','FRENCH.151A':'French 151A','FRENCH.151B':'French 151B',
	'FRENCH.152':'French 152','FRENCH.170':'French 170','FRENCH.172A':'French 172A','FRENCH.172B':'French 172B','FRENCH.173':'French 173','FRENCH.174':'French 174','FRENCH.175A':'French 175A','FRENCH.175B':'French 175B','FRENCH.177A':'French 177A','FRENCH.177B':'French 177B',
	'FRENCH.178A':'French 178A','FRENCH.178B':'French 178B','FRENCH.180A':'French 180A','FRENCH.180B':'French 180B','FRENCH.180C':'French 180C','FRENCH.180D':'French 180D','FRENCH.184A':'French 184A','FRENCH.184B':'French 184B','FRENCH.185':'French 185',
	'GWS.39A':'GWS 39A','GWS.39D':'GWS 39D','GWS.39C':'GWS 39C','GWS.100AC':'GWS 100AC','GWS.101':'GWS 101','GWS.112':'GWS 112','GWS.C123AC':'GWS C123AC','GWS.125':'GWS 125','GWS.126':'GWS 126','GWS.140':'GWS 140','GWS.C146':'GWS C146','GWS.153A':'GWS 153A',
	'GERMAN.25':'German 25','GERMAN.39A':'German 39A','GERMAN.39B':'German 39B','GERMAN.39C':'German 39C','GERMAN.39D':'German 39D','GERMAN.39E':'German 39E','GERMAN.39F':'German 39F','GERMAN.39H':'German 39H',
	'GERMAN.39I':'German 39I','GERMAN.39L':'German 39L','GERMAN.100':'German 100','GERMAN.101':'German 101','GERMAN.102A':'German 102A','GERMAN.105':'German 105','GERMAN.C109':'German C109','GERMAN.110':'German 110',
	'GERMAN.111':'German 111','GERMAN.112':'German 112','GERMAN.C113':'German C113','GERMAN.120':'German 120','GERMAN.121':'German 121','GERMAN.122':'German 122','GERMAN.123':'German 123','GERMAN.130':'German 130',
	'GERMAN.132':'German 132','GERMAN.140':'German 140','GERMAN.141':'German 141','GERMAN.142':'German 142','GERMAN.143':'German 143','GERMAN.145':'German 145','GERMAN.151':'German 151',
	'GERMAN.152':'German 152','GERMAN.153':'German 153','GERMAN.154':'German 154','GERMAN.155':'German 155','GERMAN.156':'German 156','GERMAN.C159':'German C159','GERMAN.161':'German 161',
	'GERMAN.162':'German 162','GERMAN.165':'German 165','GERMAN.168':'German 168','GERMAN.175B':'German 175B','GERMAN.175C':'German 175C','GERMAN.176':'German 176','GERMAN.180':'German 180',
	'GERMAN.180B':'German 180B','GERMAN.181':'German 181','GERMAN.182':'German 182','GERMAN.183':'German 183','GERMAN.185':'German 185','GERMAN.186':'German 186','GERMAN.187':'German 187',
	'GREEK.100':'Greek 100','GREEK.101':'Greek 101','GREEK.102':'Greek 102','GREEK.105':'Greek 105','GREEK.115':'Greek 115','GREEK.116':'Greek 116','GREEK.117':'Greek 117','GREEK.120':'Greek 120','GREEK.121':'Greek 121','GREEK.122':'Greek 122','GREEK.123':'Greek 123','GREEK.125':'Greek 125',
	'HEBREW.104A':'Hebrew 104A','HEBREW.104B':'Hebrew 104B','HEBREW.148A':'Hebrew 148A','HEBREW.148B':'Hebrew 148B',
	'HINURD.101A':'Hindu-Urdu 101A','HINURD.101B':'Hindu-Urdu 101B','HINURD.102A':'Hindu-Urdu 102A','HINURD.102B':'Hindu-Urdu 102B','HINURD.104A':'Hindu-Urdu 104A','HINURD.104B':'Hindu-Urdu 104B',
	'HISTORY.39E':'History 39E','HISTORY.39F':'History 39F',
	'ISF.C100C':'ISF C100C','ISF.108':'ISF 108','ISF.117':'ISF 117','ISF.137AC':'ISF 137AC','ISF.C160':'ISF C160',
	'ITALIAN.30':'Italian 30','ITALIAN.39A':'Italian 39A','ITALIAN.39B':'Italian 39B','ITALIAN.39D':'Italian 39D','ITALIAN.40':'Italian 40','ITALIAN.50':'Italian 50','ITALIAN.70':'Italian 70','ITALIAN.75':'Italian 75','ITALIAN.80':'Italian 80',
	'ITALIAN.90':'Italian 90','ITALIAN.103':'Italian 103','ITALIAN.104':'Italian 104','ITALIAN.109':'Italian 109','ITALIAN.110':'Italian 110','ITALIAN.111':'Italian 111','ITALIAN.112':'Italian 112','ITALIAN.114':'Italian 114','ITALIAN.115':'Italian 115',
	'ITALIAN.117':'Italian 117','ITALIAN.120':'Italian 120','ITALIAN.130A':'Italian 130A','ITALIAN.130B':'Italian 130B','ITALIAN.140':'Italian 140','ITALIAN.163':'Italian 163','ITALIAN.170':'Italian 170','ITALIAN.175':'Italian 175',
	'JAPAN.7A':'Japanese 7A','JAPAN.7B':'Japanese 7B','JAPAN.39':'Japanese 39','JAPAN.39A':'Japanese 39A','JAPAN.39C':'Japanese 39C','JAPAN.101':'Japanese 101','JAPAN.103':'Japanese 103','JAPAN.111':'Japanese 111',
	'JAPAN.112':'Japanese 112','JAPAN.120':'Japanese 120','JAPAN.130':'Japanese 130','JAPAN.132':'Japanese 132','JAPAN.134':'Japanese 134','JAPAN.140':'Japanese 140','JAPAN.142':'Japanese 142','JAPAN.144':'Japanese 144',
	'JAPAN.146':'Japanese 146','JAPAN.155':'Japanese 155','JAPAN.159':'Japanese 159','JAPAN.180':'Japanese 180','JAPAN.182A':'Japanese 182A','JAPAN.182B':'Japanese 182B','JAPAN.183':'Japanese 183','JAPAN.184':'Japanese 184',
	'JAPAN.185':'Japanese 185','JAPAN.186':'Japanese 186','JAPAN.187':'Japanese 187','JAPAN.188':'Japanese 188','JAPAN.189':'Japanese 189',
	'JEWISH.39A':'Jewish 39A','JEWISH.39D':'Jewish 39D','JEWISH.39F':'Jewish 39F',
	'JOURN.39F':'Journalism 39F','JOURN.151':'Journalism 151','JOURN.175':'Journalism 175',
	'KHMER.101A':'Khmer 101A','KHMER.101B':'Khmer 101B',
	'KOREAN.7A':'Korean 7A','KOREAN.7B':'Korean 7B','KOREAN.101':'Korean 101','KOREAN.111':'Korean 111','KOREAN.112':'Korean 112','KOREAN.130':'Korean 130','KOREAN.140':'Korean 140',
	'KOREAN.150':'Korean 150','KOREAN.155':'Korean 155','KOREAN.157':'Korean 157','KOREAN.180':'Korean 180','KOREAN.185':'Korean 185','KOREAN.187A':'Korean 187A','KOREAN.187B':'Korean 187B',
	'LATIN.100':'Latin 100','LATIN.101':'Latin 101','LATIN.102':'Latin 102','LATIN.115':'Latin 115','LATIN.116':'Latin 116','LATIN.117':'Latin 117','LATIN.118':'Latin 118','LATIN.119':'Latin 119',
	'LATIN.120':'Latin 120','LATIN.121':'Latin 121','LATIN.122':'Latin 122','LATIN.123':'Latin 123','LATIN.140':'Latin 140','LATIN.155A':'Latin 155A','LATIN.155B':'Latin 155B',
	'LEGALST.114':'LegalStudies 114',
	'LGBT.C146':'LGBT C146','LGBT.C146A':'LGBT C146A',
	'L&S.17':'L&S 17','L&S.20A':'L&S 20A','L&S.20B':'L&S 20B','L&S.20C':'L&S 20C','L&S.20D':'L&S 20D','L&S.21':'L&S 21','L&S.25':'L&S 25','L&S.26':'L&S 26','L&S.27':'L&S 27','L&S.39B':'L&S 39B','L&S.40A':'L&S 40A','L&S.C40T':'L&S C40T',
	'L&S.116':'L&S 116','L&S.118':'L&S 118','L&S.120A':'L&S 120A','L&S.120B':'L&S 120B','L&S.120C':'L&S 120C','L&S.123':'L&S 123','L&S.125':'L&S 125','L&S.140A':'L&S 140A','L&S.140C':'L&S 140C','L&S.148':'L&S 148',
	'L&S.180B':'L&S 180B','L&S.C180T':'L&S C180T',
	'LINGUIS.65':'Linguistics 65','LINGUIS.106':'Linguistics 106','LINGUIS.127':'Linguistics 127','LINGUIS.128':'Linguistics 128',
	'MEDIAST.150':'Media 150',
	'MEDST.110':'Medieval 110',
	'MILAFF.124':'MilitaryAffairs 124',
	'NATAMST.20B':'NativeAmerican 20B','NATAMST.52':'NativeAmerican 52','NATAMST.120':'NativeAmerican 120','NATAMST.150':'NativeAmerican 150','NATAMST.C152':'NativeAmerican C152',
	'NATAMST.153':'NativeAmerican 153','NATAMST.154':'NativeAmerican 154','NATAMST.156':'NativeAmerican 156','NATAMST.158':'NativeAmerican 158','NATAMST.182':'NativeAmerican 182',
	'NESTUD.15':'NearEastern 15','NESTUD.C16':'NearEastern C16','NESTUD.18':'NearEastern 18','NESTUD.23':'NearEastern 23','NESTUD.25':'NearEastern 25','NESTUD.32':'NearEastern 32','NESTUD.34':'NearEastern 34','NESTUD.80':'NearEastern 80',
	'NESTUD.C92':'NearEastern C92','NESTUD.102A':'NearEastern 102A','NESTUD.102B':'NearEastern 102B','NESTUD.105A':'NearEastern 105A','NESTUD.105B':'NearEastern 105B','NESTUD.106A':'NearEastern 106A','NESTUD.106B':'NearEastern 106B','NESTUD.107':'NearEastern 107',
	'NESTUD.110':'NearEastern 110','NESTUD.113':'NearEastern 113','NESTUD.C120A':'NearEastern C120A','NESTUD.C120B':'NearEastern C120B','NESTUD.C121A':'NearEastern C121A','NESTUD.C121B':'NearEastern C121B','NESTUD.122':'NearEastern 122','NESTUD.122A':'NearEastern 122A',
	'NESTUD.122B':'NearEastern 122B','NESTUD.123':'NearEastern 123','NESTUD.123A':'NearEastern 123A','NESTUD.123B':'NearEastern 123B','NESTUD.124':'NearEastern 124','NESTUD.124A':'NearEastern 124A','NESTUD.124B':'NearEastern 124B','NESTUD.125':'NearEastern 125',
	'NESTUD.126':'NearEastern 126','NESTUD.127':'NearEastern 127','NESTUD.128':'NearEastern 128','NESTUD.C129':'NearEastern C129','NESTUD.132':'NearEastern 132','NESTUD.138':'NearEastern 138','NESTUD.139':'NearEastern 139','NESTUD.150A':'NearEastern 150A',
	'NESTUD.150B':'NearEastern 150B','NESTUD.151':'NearEastern 151','NESTUD.152':'NearEastern 152','NESTUD.153':'NearEastern 153','NESTUD.154':'NearEastern 154','NESTUD.155':'NearEastern 155','NESTUD.162A':'NearEastern 162A','NESTUD.162B':'NearEastern 162B',
	'NESTUD.165':'NearEastern 165','NESTUD.170A':'NearEastern 170A','NESTUD.170B':'NearEastern 170B',
	'PERSIAN.101A':'Persian 101A','PERSIAN.101B':'Persian 101B','PERSIAN.102A':'Persian 102A','PERSIAN.102B':'Persian 102B','PERSIAN.103A':'Persian 103A','PERSIAN.103B':'Persian 103B','PERSIAN.104A':'Persian 104A','PERSIAN.104B':'Persian 104B','PERSIAN.105':'Persian 105',
	'IDS.156AC':'InterDepartmental 156AC',
	'PHILOS.6':'Philo 6','PHILOS.7':'Philo 7','PHILOS.8':'Philo 8','PHILOS.109':'Philo 109','PHILOS.110':'Philo 110','PHILOS.111':'Philo 111','PHILOS.163':'Philo 163','PHILOS.170':'Philo 170','PHILOS.176':'Philo 176','PHILOS.180':'Philo 180',
	'PHYSED.160':'PE 160',
	'PORTUG.25':'Portugese 25','PORTUG.102':'Portugese 102','PORTUG.104':'Portugese 104','PORTUG.107A':'Portugese 107A','PORTUG.107B':'Portugese 107B','PORTUG.114':'Portugese 114',
	'PORTUG.125':'Portugese 125','PORTUG.128':'Portugese 128','PORTUG.134':'Portugese 134','PORTUG.135':'Portugese 135','PORTUG.138':'Portugese 138','PORTUG.144':'Portugese 144',
	'PSYCH.39E':'Psychology 39E','PSYCH.39F':'Psychology 39F',
	'RELIGSRT.C108':'ReligiousStudies C108','RELIGSRT.C109':'ReligiousStudies C109','RELIGSRT.115':'ReligiousStudies 115','RELIGSRT.C118':'ReligiousStudies C118','RELIGSRT.C119':'ReligiousStudies C119','RELIGSRT.C163':'ReligiousStudies C163','RELIGSRT.C165':'ReligiousStudies C165','RELIGSRT.C166':'ReligiousStudies C166','RELIGSRT.171AC':'ReligiousStudies 171AC',
	'RHETOR.20':'Rhetoric 20','RHETOR.22':'Rhetoric 22','RHETOR.39D':'Rhetoric 39D','RHETOR.39F':'Rhetoric 39F','RHETOR.39I':'Rhetoric 39I','RHETOR.40AC':'Rhetoric 40AC','RHETOR.41AC':'Rhetoric 41AC',
	'RHETOR.50A':'Rhetoric 50A','RHETOR.50B':'Rhetoric 50B','RHETOR.50C':'Rhetoric 50C','RHETOR.50D':'Rhetoric 50D','RHETOR.101':'Rhetoric 101','RHETOR.103A':'Rhetoric 103A','RHETOR.103B':'Rhetoric 103B',
	'RHETOR.104':'Rhetoric 104','RHETOR.110':'Rhetoric 110','RHETOR.112':'Rhetoric 112','RHETOR.118':'Rhetoric 118','RHETOR.120B':'Rhetoric 120B','RHETOR.120D':'Rhetoric 120D','RHETOR.121':'Rhetoric 121',
	'RHETOR.121A':'Rhetoric 121A','RHETOR.121B':'Rhetoric 121B','RHETOR.122':'Rhetoric 122','RHETOR.124':'Rhetoric 124','RHETOR.125':'Rhetoric 125','RHETOR.126':'Rhetoric 126','RHETOR.127':'Rhetoric 127',
	'RHETOR.130':'Rhetoric 130','RHETOR.131T':'Rhetoric 131T','RHETOR.132T':'Rhetoric 132T','RHETOR.133T':'Rhetoric 133T','RHETOR.134':'Rhetoric 134','RHETOR.136':'Rhetoric 136','RHETOR.137':'Rhetoric 137',
	'RHETOR.138':'Rhetoric 138','RHETOR.141AC':'Rhetoric 141AC','RHETOR.150':'Rhetoric 150','RHETOR.156':'Rhetoric 156','RHETOR.178':'Rhetoric 178','RHETOR.180AC':'Rhetoric 180AC',
	'SCANDIN.39B':'Scandinavian 39B','SCANDIN.50':'Scandinavian 50','SCANDIN.100A':'Scandinavian 100A','SCANDIN.100B':'Scandinavian 100B','SCANDIN.106':'Scandinavian 106','SCANDIN.107':'Scandinavian 107','SCANDIN.108':'Scandinavian 108',
	'SCANDIN.C114':'Scandinavian C114','SCANDIN.115':'Scandinavian 115','SCANDIN.116':'Scandinavian 116','SCANDIN.117':'Scandinavian 117','SCANDIN.118':'Scandinavian 118','SCANDIN.120':'Scandinavian 120','SCANDIN.125':'Scandinavian 125',
	'SCANDIN.140A':'Scandinavian 140A','SCANDIN.140B':'Scandinavian 140B','SCANDIN.150':'Scandinavian 150','SCANDIN.155':'Scandinavian 155','SCANDIN.C160':'Scandinavian C160','SCANDIN.165':'Scandinavian 165','SCANDIN.170':'Scandinavian 170',
	'SLAVIC.36':'Slavic 36','SLAVIC.R37W':'Slavic R37W','SLAVIC.39':'Slavic 39','SLAVIC.39C':'Slavic 39C','SLAVIC.39D':'Slavic 39D','SLAVIC.39E':'Slavic 39E','SLAVIC.39G':'Slavic 39G','SLAVIC.39J':'Slavic 39J',
	'SLAVIC.39K':'Slavic 39K','SLAVIC.39L':'Slavic 39L','SLAVIC.39N':'Slavic 39N','SLAVIC.45':'Slavic 45','SLAVIC.46':'Slavic 46','SLAVIC.50':'Slavic 50','SLAVIC.100':'Slavic 100','SLAVIC.130':'Slavic 130',
	'SLAVIC.131':'Slavic 131','SLAVIC.132':'Slavic 132','SLAVIC.133':'Slavic 133','SLAVIC.134A':'Slavic 134A','SLAVIC.134B':'Slavic 134B','SLAVIC.134C':'Slavic 134C','SLAVIC.134D':'Slavic 134D','SLAVIC.134E':'Slavic 134E',
	'SLAVIC.134F':'Slavic 134F','SLAVIC.134G':'Slavic 134G','SLAVIC.134N':'Slavic 134N','SLAVIC.135':'Slavic 135','SLAVIC.138':'Slavic 138','SLAVIC.140':'Slavic 140','SLAVIC.146':'Slavic 146','SLAVIC.147A':'Slavic 147A',
	'SLAVIC.147B':'Slavic 147B','SLAVIC.148':'Slavic 148','SLAVIC.150':'Slavic 150','SLAVIC.151':'Slavic 151','SLAVIC.154':'Slavic 154','SLAVIC.158':'Slavic 158','SLAVIC.160':'Slavic 160','SLAVIC.161':'Slavic 161',
	'SLAVIC.170':'Slavic 170','SLAVIC.171':'Slavic 171','SLAVIC.179':'Slavic 179','SLAVIC.180':'Slavic 180','SLAVIC.181':'Slavic 181','SLAVIC.182':'Slavic 182','SLAVIC.188':'Slavic 188',
	'SOCWEL.39A':'SocialWelfare 39A',
	'SOCIOL.160':'Sociology 160',
	'SSEASN.39A':'South and SouthEast Asian 39A','SSEASN.39B':'South and SouthEast Asian 39B','SSEASN.39D':'South and SouthEast Asian 39D','SSEASN.39F':'South and SouthEast Asian 39F','SSEASN.39G':'South and SouthEast Asian 39G',
	'SSEASN.39H':'South and SouthEast Asian 39H','SSEASN.39J':'South and SouthEast Asian 39J','SSEASN.C110':'South and SouthEast Asian C110','SSEASN.C113':'South and SouthEast Asian C113','SSEASN.138':'South and SouthEast Asian 138',
	'SASIAN.121':'SouthAsian 121','SASIAN.122':'SouthAsian 122','SASIAN.124':'SouthAsian 124','SASIAN.C128':'SouthAsian C128','SASIAN.129':'SouthAsian 129','SASIAN.131':'SouthAsian 131','SASIAN.138':'SouthAsian 138',
	'SASIAN.C140':'SouthAsian C140','SASIAN.C142':'SouthAsian C142','SASIAN.143':'SouthAsian 143','SASIAN.145':'SouthAsian 145','SASIAN.152':'SouthAsian 152','SASIAN.165':'SouthAsian 165',
	'SEASIAN.123':'SouthEastAsian 123','SEASIAN.124':'SouthEastAsian 124','SEASIAN.128':'SouthEastAsian 128','SEASIAN.129':'SouthEastAsian 129','SEASIAN.C164':'SouthEastAsian C164',
	'SPANISH.25':'Spanish 25','SPANISH.39A':'Spanish 39A','SPANISH.39B':'Spanish 39B','SPANISH.39C':'Spanish 39C','SPANISH.39D':'Spanish 39D','SPANISH.39E':'Spanish 39E','SPANISH.40':'Spanish 40',
	'SPANISH.104A':'Spanish 104A','SPANISH.104B':'Spanish 104B','SPANISH.107A':'Spanish 107A','SPANISH.107B':'Spanish 107B','SPANISH.108':'Spanish 108','SPANISH.109':'Spanish 109','SPANISH.11':'Spanish 110',
	'SPANISH.111A':'Spanish 111A','SPANISH.111B':'Spanish 111B','SPANISH.112':'Spanish 112','SPANISH.113':'Spanish 113','SPANISH.114':'Spanish 114','SPANISH.115':'Spanish 115','SPANISH.117':'Spanish 117',
	'SPANISH.123A':'Spanish 123A','SPANISH.123B':'Spanish 123B','SPANISH.126':'Spanish 126','SPANISH.127':'Spanish 127','SPANISH.128':'Spanish 128','SPANISH.129':'Spanish 129','SPANISH.130':'Spanish 130',
	'SPANISH.131':'Spanish 131','SPANISH.133':'Spanish 133','SPANISH.134':'Spanish 134','SPANISH.135':'Spanish 135','SPANISH.135AC':'Spanish 135AC','SPANISH.142':'Spanish 142','SPANISH.147':'Spanish 147',
	'SPANISH.165':'Spanish 165','SPANISH.185':'Spanish 185',
	'TIBETAN.110':'Tibetan 110','TIBETAN.110B':'Tibetan 110B','TIBETAN.120A':'Tibetan 120A','TIBETAN.120B':'Tibetan 120B','TIBETAN.124':'Tibetan 124','TIBETAN.128A':'Tibetan 128A','TIBETAN.128B':'Tibetan 128B','TIBETAN.150A':'Tibetan 150A','TIBETAN.150B':'Tibetan 150B',
	'TURKISH.101A':'Turkish 101A','TURKISH.101B':'Turkish 101B','TURKISH.102A':'Turkish 102A','TURKISH.102B':'Turkish 102B',
	'UGIS.C12':'UGIS C12','UGIS.44A':'UGIS 44A','UGIS.44B':'UGIS 44B','UGIS.44C':'UGIS 44C','UGIS.55A':'UGIS 55A','UGIS.C135':'UGIS C135',
	'UGIS.C136':'UGIS C136','UGIS.140':'UGIS 140','UGIS.160A':'UGIS 160A','UGIS.163':'UGIS 163','UGIS.164':'UGIS 164','UGIS.171':'UGIS 171',
	'VIETNMS.101B':'Vietnamese 101B',
	'VISSTD.180A':'VisualStudies 180A','VISSTD.180B':'VisualStudies 180B','VISSTD.181':'VisualStudies 181','VISSTD.182AC':'VisualStudies 182AC','VISSTD.185A':'VisualStudies 185A','VISSTD.185X':'VisualStudies 185X','VISSTD.186X':'VisualStudies 186X','VISSTD.189':'VisualStudies 189',
	'ART.8':'Art 8','ART.12':'Art 12','ART.13':'Art 13','ART.N13':'Art N13','ART.14':'Art 14','ART.16':'Art 16','ART.21':'Art 21','ART.23AC':'Art 23AC','ART.N23':'Art N23',
	'ART.W23AC':'Art W23AC','ART.26':'Art 26','ART.98':'Art 98','ART.99':'Art 99','ART.102':'Art 102','ART.N102':'Art N102','ART.117':'Art 117','ART.N117':'Art N117','ART.118':'Art 118',
	'ART.119':'Art 119','ART.120':'Art 120','ART.122':'Art 122','ART.123':'Art 123','ART.124':'Art 124','ART.130':'Art 130','ART.132':'Art 132','ART.133':'Art 133','ART.137':'Art 137',
	'ART.138':'Art 138','ART.141':'Art 141','ART.142':'Art 142','ART.160':'Art 160','ART.N160':'Art N160','ART.162':'Art 162','ART.163':'Art 163','ART.164':'Art 164','ART.165':'Art 165',
	'ART.171':'Art 171','ART.C171':'Art C171','ART.N171':'Art N171','ART.172':'Art 172','ART.173':'Art 173','ART.174':'Art 174','ART.C174':'Art C174','ART.178':'Art 178','ART.C179':'Art C179',
	'ART.180':'Art 180','ART.185':'Art 185','ART.H195A':'Art H195A','ART.H195B':'Art H195B','ART.198':'Art 198','ART.199':'Art 199','ART.N199':'Art N199',
	'THEATER.10':'TDPS 10','THEATER.N10':'TDPS N10','THEATER.11':'TDPS 11','THEATER.N11':'TDPS N11','THEATER.15':'TDPS 15','THEATER.24':'TDPS 24','THEATER.25AC':'TDPS 25AC',
	'THEATER.26':'TDPS 26','THEATER.339A':'TDPS 39A','THEATER.39B':'TDPS 39B','THEATER.39C':'TDPS 39C','THEATER.39D':'TDPS 39D','THEATER.39E':'TDPS 39E','THEATER.39F':'TDPS 39F',
	'THEATER.39G':'TDPS 39G','THEATER.39H':'TDPS 39H','THEATER.39I':'TDPS 39I','THEATER.39J':'TDPS 39J','THEATER.39K':'TDPS 39K','THEATER.39L':'TDPS 39L','THEATER.39M':'TDPS 39M',
	'THEATER.39N':'TDPS 39N','THEATER.39O':'TDPS 39O','THEATER.39P':'TDPS 39P','THEATER.39Q':'TDPS 39Q','THEATER.39R':'TDPS 39R','THEATER.39S':'TDPS 39S','THEATER.39T':'TDPS 39T',
	'THEATER.39U':'TDPS 39U','THEATER.39V':'TDPS 39V','THEATER.39W':'TDPS 39W','THEATER.39X':'TDPS 39X','THEATER.39Y':'TDPS 39Y','THEATER.39Z':'TDPS 39Z','THEATER.40':'TDPS 40',
	'THEATER.52AC':'TDPS 52AC','THEATER.84':'TDPS 84','THEATER.98':'TDPS 98','THEATER.99':'TDPS 99','THEATER.C107':'TDPS C107','THEATER.C108':'TDPS C108','THEATER.110A':'TDPS 110A',
	'THEATER.110B':'TDPS 110B','THEATER.111':'TDPS 111','THEATER.112':'TDPS 112','THEATER.113A':'TDPS 113A','THEATER.114':'TDPS 114','THEATER.115':'TDPS 115','THEATER.119':'TDPS 119',
	'THEATER.121':'TDPS 121','THEATER.122':'TDPS 122','THEATER.125':'TDPS 125','THEATER.126':'TDPS 126','THEATER.C131B':'TDPS C131B','THEATER.139A':'TDPS 139A','THEATER.139B':'TDPS 139B',
	'THEATER.141B':'TDPS 141B','THEATER.N141':'TDPS N141','THEATER.142':'TDPS 142','THEATER.N142':'TDPS N142','THEATER.143':'TDPS 143','THEATER.144':'TDPS 144','THEATER.145':'TDPS 145',
	'THEATER.146A':'TDPS 146A','THEATER.146B':'TDPS 146B','THEATER.147A':'TDPS 147A','THEATER.147B':'TDPS 147B','THEATER.151A':'TDPS 151A','THEATER.151B':'TDPS 151B','THEATER.153B':'TDPS 153B',
	'THEATER.162':'TDPS 162','THEATER.163':'TDPS 163','THEATER.166':'TDPS 166','THEATER.167':'TDPS 167','THEATER.168':'TDPS 168','THEATER.169':'TDPS 169','THEATER.170':'TDPS 170',
	'THEATER.171':'TDPS 171','THEATER.173A':'TDPS 173A','THEATER.173B':'TDPS 173B','THEATER.174A':'TDPS 174A','THEATER.174B':'TDPS 174B','THEATER.175A':'TDPS 175A','THEATER.175B':'TDPS 175B',
	'THEATER.178':'TDPS 178','THEATER.179':'TDPS 179','THEATER.180':'TDPS 180','THEATER.181':'TDPS 181','THEATER.182':'TDPS 182','THEATER.C183A':'TDPS C183A','THEATER.C183B':'TDPS C183B',
	'THEATER.C183C':'TDPS C183C','THEATER.H195A':'TDPS H195A','THEATER.H195B':'TDPS H195B','THEATER.196':'TDPS 196','THEATER.197':'TDPS 197','THEATER.198':'TDPS 198','THEATER.199':'TDPS 199',
	'FILM.25A':'Film 25A', 'FILM.25B':'Film 25B', 'FILM.26':'Film 26', 'FILM.50':'Film 50', 'FILM.N70':'Film N70', 'FILM.75':'Film 75', 'FILM.76':'Film 76', 'FILM.77X':'Film 77X', 'FILM.78X':'Film 78X',
	'FILM.84':'Film 84', 'FILM.98':'Film 98', 'FILM.100':'Film 100', 'FILM.105':'Film 105', 'FILM.108':'Film 108', 'FILM.N108':'Film N108', 'FILM.C115':'Film C115', 'FILM.116X':'Film 116X', 'FILM.117':'Film 117',
	'FILM.118':'Film 118', 'FILM.128':'Film 128', 'FILM.129':'Film 129', 'FILM.140':'Film 140', 'FILM.151':'Film 151', 'FILM.152':'Film 152', 'FILM.153':'Film 153', 'FILM.154':'Film 154', 'FILM.155X':'Film 155X',
	'FILM.160':'Film 160', 'FILM.N160':'Film N160', 'FILM.180A':'Film 180A', 'FILM.180B':'Film 180B', 'FILM.185':'Film 185', 'FILM.C185':'Film C185', 'FILM.186':'Film 186', 'FILM.C187':'Film C187',
	'FILM.H195':'Film H195', 'FILM.197A':'Film 197A', 'FILM.197B':'Film 197B', 'FILM.197C':'Film 197C', 'FILM.197D':'Film 197D', 'FILM.198':'Film 198', 'FILM.199':'Film 199',
	'ENGLISH.R1AN':'English R1AN', 'ENGLISH.N17':'English N17', 'ENGLISH.24':'English 24', 'ENGLISH.N25':'English N25', 'ENGLISH.N26':'English N26', 'ENGLISH.N27':'English N27', 
	'ENGLISH.N28':'English N28', 'ENGLISH.N30A':'English N30A', 'ENGLISH.N30B':'English N30B', 'ENGLISH.31AC':'English 31AC', 'ENGLISH.N31AC':'English N31AC', 'ENGLISH.S40':'English S40',
	'ENGLISH.43A':'English 43A', 'ENGLISH.43B':'English 43B', 'ENGLISH.N43A':'English N43A', 'ENGLISH.N43B':'English N43B', 'ENGLISH.N43D':'English N43D', 'ENGLISH.N44A':'English N44A',
	'ENGLISH.N44B':'English N44B', 'ENGLISH.45A':'English 45A', 'ENGLISH.45B':'English 45B', 'ENGLISH.45C':'English 45C', 'ENGLISH.N45A':'English N45A', 'ENGLISH.N45B':'English N45B',
	'ENGLISH.N45C':'English N45C', 'ENGLISH.N50':'English N50', 'ENGLISH.C77':'English C77', 'ENGLISH.80K':'English 80K', 'ENGLISH.84':'English 84', 'ENGLISH.98':'English 98', 'ENGLISH.99':'English 99',
	'ENGLISH.101':'English 101', 'ENGLISH.102':'English 102', 'ENGLISH.104':'English 104', 'ENGLISH.105':'English 105', 'ENGLISH.C107':'English C107', 'ENGLISH.N107':'English N107', 'ENGLISH.110':'English 110',
	'ENGLISH.111':'English 111', 'ENGLISH.112':'English 112', 'ENGLISH.114A':'English 114A', 'ENGLISH.114B':'English 114B', 'ENGLISH.N114A':'English N114A', 'ENGLISH.N114B':'English N114B', 'ENGLISH.115A':'English 115A',
	'ENGLISH.115B':'English 115B', 'ENGLISH.N115A':'English N115A', 'ENGLISH.N115B':'English N115B', 'ENGLISH.116':'English 116', 'ENGLISH.117A':'English 117A', 'ENGLISH.117B':'English 117B', 'ENGLISH.N117S':'English N117S',
	'ENGLISH.117S':'English 117S', 'ENGLISH.118':'English 118', 'ENGLISH.N118':'English N118', 'ENGLISH.119':'English 119', 'ENGLISH.120':'English 120', 'ENGLISH.121':'English 121', 'ENGLISH.N121':'English N121',
	'ENGLISH.122':'English 122', 'ENGLISH.125A':'English 125A', 'ENGLISH.125B':'English 125B', 'ENGLISH.125C':'English 125C', 'ENGLISH.125D':'English 125D', 'ENGLISH.125E':'English 125E', 'ENGLISH.N125B':'English N125B',
	'ENGLISH.N125D':'English N125D', 'ENGLISH.N125E':'English N125E', 'ENGLISH.126':'English 126', 'ENGLISH.127':'English 127', 'ENGLISH.130A':'English 130A', 'ENGLISH.130B':'English 130B', 'ENGLISH.130C':'English 130C',
	'ENGLISH.130D':'English 130D', 'ENGLISH.N130A':'English N130A', 'ENGLISH.N130B':'English N130B', 'ENGLISH.N130D':'English N130D', 'ENGLISH.131':'English 131', 'ENGLISH.132':'English 132', 'ENGLISH.N132':'English N132',
	'ENGLISH.133A':'English 133A', 'ENGLISH.133B':'English 133B', 'ENGLISH.133T':'English 133T', 'ENGLISH.134':'English 134', 'ENGLISH.N134':'English N134', 'ENGLISH.135AC':'English 135AC', 'ENGLISH.N135':'English N135',
	'ENGLISH.S135':'English S135', 'ENGLISH.C136':'English C136', 'ENGLISH.137B':'English 137B', 'ENGLISH.137T':'English 137T', 'ENGLISH.138':'English 138', 'ENGLISH.139':'English 139', 'ENGLISH.141':'English 141', 
	'ENGLISH.N141':'English N141', 'ENGLISH.143A':'English 143A', 'ENGLISH.143B':'English 143B', 'ENGLISH.143C':'English 143C', 'ENGLISH.143N':'English 143N', 'ENGLISH.143T':'English 143T', 'ENGLISH.152':'English 152', 
	'ENGLISH.N152':'English N152', 'ENGLISH.160':'English 160', 'ENGLISH.161':'English 161', 'ENGLISH.165':'English 165', 'ENGLISH.165AC':'English 165AC', 'ENGLISH.166':'English 166', 'ENGLISH.166AC':'English 166AC',
	'ENGLISH.N166':'English N166', 'ENGLISH.170':'English 170', 'ENGLISH.173':'English 173', 'ENGLISH.N173':'English N173', 'ENGLISH.174':'English 174', 'ENGLISH.175':'English 175', 'ENGLISH.176':'English 176', 
	'ENGLISH.N176':'English N176', 'ENGLISH.N177':'English N177', 'ENGLISH.179':'English 179', 'ENGLISH.180A':'English 180A', 'ENGLISH.180E':'English 180E', 'ENGLISH.180H':'English 180H', 'ENGLISH.180L':'English 180L',
	'ENGLISH.180R':'English 180R', 'ENGLISH.180Z':'English 180Z', 'ENGLISH.180N':'English 180N', 'ENGLISH.N180A':'English N180A', 'ENGLISH.N180H':'English N180H', 'ENGLISH.N180Z':'English N180Z', 'ENGLISH.190':'English 190',
	'ENGLISH.H195A':'English H195A', 'ENGLISH.H195B':'English H195B', 'ENGLISH.198':'English 198', 'ENGLISH.199':'English 199',
	'COMLIT.20':'ComparativeLiterature 20', 'COMLIT.24':'ComparativeLiterature 24', 'COMLIT.39H':'ComparativeLiterature 39H', 'COMLIT.N40':'ComparativeLiterature N40', 'COMLIT.41A':'ComparativeLiterature 41A',
	'COMLIT.41C':'ComparativeLiterature 41C', 'COMLIT.41D':'ComparativeLiterature 41D', 'COMLIT.41E':'ComparativeLiterature 41E', 'COMLIT.N41A':'ComparativeLiterature N41A', 'COMLIT.N41B':'ComparativeLiterature N41B',
	'COMLIT.N41C':'ComparativeLiterature N41C', 'COMLIT.N41D':'ComparativeLiterature N41D', 'COMLIT.60AC':'ComparativeLiterature 60AC', 'COMLIT.N60AC':'ComparativeLiterature N60AC', 'COMLIT.98':'ComparativeLiterature 98',
	'COMLIT.100':'ComparativeLiterature 100', 'COMLIT.120':'ComparativeLiterature 120', 'COMLIT.151':'ComparativeLiterature 151', 'COMLIT.152':'ComparativeLiterature 152', 'COMLIT.153':'ComparativeLiterature 153',
	'COMLIT.154':'ComparativeLiterature 154', 'COMLIT.155':'ComparativeLiterature 155', 'COMLIT.156':'ComparativeLiterature 156', 'COMLIT.165':'ComparativeLiterature 165', 'COMLIT.170':'ComparativeLiterature 170',
	'COMLIT.171':'ComparativeLiterature 171', 'COMLIT.190':'ComparativeLiterature 190', 'COMLIT.H195':'ComparativeLiterature H195', 'COMLIT.198':'ComparativeLiterature 198', 'COMLIT.199':'ComparativeLiterature 199',
	'HISTART.10B':'HistoryOfArt 10B', 'HISTART.12':'HistoryOfArt 12', 'HISTART.24':'HistoryOfArt 24', 'HISTART.30':'HistoryOfArt 30', 'HISTART.N31':'HistoryOfArt N31', 'HISTART.32':'HistoryOfArt 32', 'HISTART.33':'HistoryOfArt 33',
	'HISTART.34':'HistoryOfArt 34', 'HISTART.35':'HistoryOfArt 35', 'HISTART.39A':'HistoryOfArt 39A', 'HISTART.39B':'HistoryOfArt 39B', 'HISTART.39C':'HistoryOfArt 39C', 'HISTART.39D':'HistoryOfArt 39D', 'HISTART.39E':'HistoryOfArt 39E',
	'HISTART.39F':'HistoryOfArt 39F', 'HISTART.39G':'HistoryOfArt 39G', 'HISTART.39F':'HistoryOfArt 39F', 'HISTART.39H':'HistoryOfArt 39H', 'HISTART.39I':'HistoryOfArt 39I', 'HISTART.39J':'HistoryOfArt 39J', 'HISTART.39K':'HistoryOfArt 39K',
	'HISTART.39L':'HistoryOfArt 39L', 'HISTART.39M':'HistoryOfArt 39M', 'HISTART.39N':'HistoryOfArt 39N', 'HISTART.39O':'HistoryOfArt 39O', 'HISTART.39P':'HistoryOfArt 39P', 'HISTART.39Q':'HistoryOfArt 39Q', 'HISTART.39R':'HistoryOfArt 39R',
	'HISTART.39S':'HistoryOfArt 39S', 'HISTART.39T':'HistoryOfArt 39T', 'HISTART.39U':'HistoryOfArt 39U', 'HISTART.39V':'HistoryOfArt 39V', 'HISTART.39W':'HistoryOfArt 39W', 'HISTART.39X':'HistoryOfArt 39X', 'HISTART.39Y':'HistoryOfArt 39Y',
	'HISTART.39Z':'HistoryOfArt 39Z', 'HISTART.41':'HistoryOfArt 41', 'HISTART.51':'HistoryOfArt 51', 'HISTART.62':'HistoryOfArt 62', 'HISTART.65':'HistoryOfArt 65', 'HISTART.98':'HistoryOfArt 98', 'HISTART.100':'HistoryOfArt 100', 
	'HISTART.N104':'HistoryOfArt N104', 'HISTART.107':'HistoryOfArt 107', 'HISTART.108':'HistoryOfArt 108', 'HISTART.120':'HistoryOfArt 120', 'HISTART.C120A':'HistoryOfArt C120A', 'HISTART.C120B':'HistoryOfArt C120B', 'HISTART.C121A':'HistoryOfArt C121A',
	'HISTART.127':'HistoryOfArt 127', 'HISTART.130A':'HistoryOfArt 130A', 'HISTART.131A':'HistoryOfArt 131A', 'HISTART.131B':'HistoryOfArt 131B', 'HISTART.131C':'HistoryOfArt 131C', 'HISTART.134A':'HistoryOfArt 134A', 'HISTART.134B':'HistoryOfArt 134B', 
	'HISTART.134C':'HistoryOfArt 134C', 'HISTART.136A':'HistoryOfArt 136A', 'HISTART.136B':'HistoryOfArt 136B', 'HISTART.136C':'HistoryOfArt 136C', 'HISTART.C140':'HistoryOfArt C140', 'HISTART.141A':'HistoryOfArt 141A', 'HISTART.141B':'HistoryOfArt 141B',
	'HISTART.141C':'HistoryOfArt 141C', 'HISTART.145':'HistoryOfArt 145', 'HISTART.151':'HistoryOfArt 151', 'HISTART.156A':'HistoryOfArt 156A', 'HISTART.C156B':'HistoryOfArt C156B', 'HISTART.161':'HistoryOfArt 161', 'HISTART.162':'HistoryOfArt 162', 
	'HISTART.166':'HistoryOfArt 166', 'HISTART.169A':'HistoryOfArt 169A', 'HISTART.170':'HistoryOfArt 170', 'HISTART.171':'HistoryOfArt 171', 'HISTART.172':'HistoryOfArt 172', 'HISTART.173':'HistoryOfArt 173', 'HISTART.174':'HistoryOfArt 174', 
	'HISTART.175':'HistoryOfArt 175', 'HISTART.179':'HistoryOfArt 179', 'HISTART.180A':'HistoryOfArt 180A', 'HISTART.180C':'HistoryOfArt 180C', 'HISTART.N180A':'HistoryOfArt N180A', 'HISTART.N180B':'HistoryOfArt N180B', 'HISTART.N180C':'HistoryOfArt N180C', 
	'HISTART.N181':'HistoryOfArt N181', 'HISTART.182':'HistoryOfArt 182', 'HISTART.N182':'HistoryOfArt N182', 'HISTART.183':'HistoryOfArt 183', 'HISTART.183E':'HistoryOfArt 183E', 'HISTART.185':'HistoryOfArt 185', 'HISTART.185A':'HistoryOfArt 185A', 
	'HISTART.185B':'HistoryOfArt 185B', 'HISTART.N185C':'HistoryOfArt N185C', 'HISTART.186A':'HistoryOfArt 186A', 'HISTART.186C':'HistoryOfArt 186C', 'HISTART.N186C':'HistoryOfArt N186C', 'HISTART.187AC':'HistoryOfArt 187AC', 'HISTART.188':'HistoryOfArt 188',
	'HISTART.188A':'HistoryOfArt 188A', 'HISTART.189':'HistoryOfArt 189', 'HISTART.C189':'HistoryOfArt C189', 'HISTART.190A':'HistoryOfArt 190A', 'HISTART.190B':'HistoryOfArt 190B', 'HISTART.190C':'HistoryOfArt 190C', 'HISTART.190DH':'HistoryOfArt 190DH', 
	'HISTART.190E':'HistoryOfArt 190E', 'HISTART.190F':'HistoryOfArt 190F', 'HISTART.190G':'HistoryOfArt 190G', 'HISTART.N190A':'HistoryOfArt N190A', 'HISTART.N190B':'HistoryOfArt N190B', 'HISTART.N190C':'HistoryOfArt N190C', 'HISTART.N190D':'HistoryOfArt N190D',
	'HISTART.N190E':'HistoryOfArt N190E', 'HISTART.N190F':'HistoryOfArt N190F', 'HISTART.N190G':'HistoryOfArt N190G', 'HISTART.N190H':'HistoryOfArt N190H', 'HISTART.192A':'HistoryOfArt 192A', 'HISTART.192B':'HistoryOfArt 192B', 'HISTART.192C':'HistoryOfArt 192C',
	'HISTART.192D':'HistoryOfArt 192D', 'HISTART.192DH':'HistoryOfArt 192DH', 'HISTART.192F':'HistoryOfArt 192F', 'HISTART.192G':'HistoryOfArt 192G', 'HISTART.192H':'HistoryOfArt 192H', 'HISTART.192AC':'HistoryOfArt 192AC', 'HISTART.193':'HistoryOfArt 193', 
	'HISTART.194':'HistoryOfArt 194', 'HISTART.H195':'HistoryOfArt H195', 'HISTART.C196A':'HistoryOfArt C196A', 'HISTART.C196B':'HistoryOfArt C196B', 'HISTART.C196W':'HistoryOfArt C196W', 'HISTART.198':'HistoryOfArt 198', 'HISTART.199':'HistoryOfArt 199', 
	'HISTART.N199':'HistoryOfArt N199',
	'MUSIC.20A':'Music 20A', 'MUSIC.20B':'Music 20B', 'MUSIC.24':'Music 24', 'MUSIC.25A':'Music 25A', 'MUSIC.25B':'Music 25B', 'MUSIC.26AC':'Music 26AC', 'MUSIC.N26AC':'Music N26AC', 'MUSIC.27':'Music 27', 'MUSIC.N27':'Music N27', 'MUSIC.28Y':'Music 28Y', 
	'MUSIC.29':'Music 29', 'MUSIC.39M':'Music 39M', 'MUSIC.39N':'Music 39N', 'MUSIC.40':'Music 40', 'MUSIC.41A':'Music 41A', 'MUSIC.41B':'Music 41B', 'MUSIC.41C':'Music 41C', 'MUSIC.42':'Music 42', 'MUSIC.43':'Music 43', 'MUSIC.44':'Music 44', 'MUSIC.45':'Music 45',
	'MUSIC.49A':'Music 49A', 'MUSIC.73':'Music 73', 'MUSIC.74':'Music 74', 'MUSIC.75':'Music 75', 'MUSIC.76':'Music 76', 'MUSIC.77':'Music 77', 'MUSIC.97':'Music 97', 'MUSIC.98':'Music 98', 'MUSIC.99':'Music 99', 'MUSIC.101':'Music 101', 'MUSIC.101M':'Music 101M', 
	'MUSIC.108':'Music 108', 'MUSIC.108M':'Music 108M', 'MUSIC.109':'Music 109', 'MUSIC.109M':'Music 109M', 'MUSIC.116A':'Music 116A', 'MUSIC.116AM':'Music 116AM', 'MUSIC.116B':'Music 116B', 'MUSIC.116BM':'Music 116BM', 'MUSIC.N116':'Music N116', 
	'MUSIC.128':'Music 128', 'MUSIC.128A':'Music 128A', 'MUSIC.128AM':'Music 128AM', 'MUSIC.128B':'Music 128B', 'MUSIC.128BM':'Music 128BM', 'MUSIC.C128P':'Music C128P', 'MUSIC.128D':'Music 128D', 'MUSIC.128DM':'Music 128DM', 'MUSIC.128E':'Music 128E', 
	'MUSIC.128GY':'Music 128GY', 'MUSIC.128P':'Music 128P', 'MUSIC.128Q':'Music 128Q', 'MUSIC.128S':'Music 128S', 'MUSIC.128SM':'Music 128SM', 'MUSIC.128T':'Music 128T', 'MUSIC.128TM':'Music 128TM', 'MUSIC.130B':'Music 130B', 'MUSIC.N130B':'Music N130B',
	'MUSIC.132':'Music 132', 'MUSIC.133AX':'Music 133AX', 'MUSIC.133C':'Music 133C', 'MUSIC.133D':'Music 133D', 'MUSIC.134A':'Music 134A', 'MUSIC.134B':'Music 134B', 'MUSIC.135A':'Music 135A', 'MUSIC.136':'Music 136', 'MUSIC.137AC':'Music 137AC', 
	'MUSIC.139':'Music 139', 'MUSIC.140':'Music 140', 'MUSIC.N140':'Music N140', 'MUSIC.141':'Music 141', 'MUSIC.142':'Music 142', 'MUSIC.143':'Music 143', 'MUSIC.144':'Music 144', 'MUSIC.145':'Music 145', 'MUSIC.146B':'Music 146B', 'MUSIC.147':'Music 147',
	'MUSIC.148':'Music 148', 'MUSIC.N148':'Music N148', 'MUSIC.149':'Music 149', 'MUSIC.150A':'Music 150A', 'MUSIC.150B':'Music 150B', 'MUSIC.150C':'Music 150C', 'MUSIC.150D':'Music 150D', 'MUSIC.150E':'Music 150E', 'MUSIC.150G':'Music 150G', 'MUSIC.150H':'Music 150H',
	'MUSIC.151':'Music 151', 'MUSIC.152':'Music 152', 'MUSIC.154A':'Music 154A', 'MUSIC.154B':'Music 154B', 'MUSIC.155':'Music 155', 'MUSIC.156':'Music 156', 'MUSIC.157A':'Music 157A', 'MUSIC.157B':'Music 157B', 'MUSIC.158':'Music 158', 'MUSIC.159':'Music 159', 
	'MUSIC.161A':'Music 161A', 'MUSIC.161B':'Music 161B', 'MUSIC.162':'Music 162', 'MUSIC.164':'Music 164', 'MUSIC.165':'Music 165', 'MUSIC.171D':'Music 171D', 'MUSIC.172A':'Music 172A', 'MUSIC.174C':'Music 174C', 'MUSIC.179':'Music 179', 'MUSIC.189':'Music 189', 
	'MUSIC.H195':'Music H195', 'MUSIC.197':'Music 197', 'MUSIC.198':'Music 198', 'MUSIC.199':'Music 199'}
#http://ls-advise.berkeley.edu/requirement/breadth7/bs.html
biologicalScience={
	'ANTHRO.1':'Anthro 1', 'ANTHRO.C100':'Anthro C100', 'ANTHRO.101':'Anthro 101', 'ANTHRO.C103':'Anthro C103', 'ANTHRO.105':'Anthro 105', 'ANTHRO.106':'Anthro 106', 'ANTHRO.107':'Anthro 107', 'ANTHRO.108':'Anthro 108', 'ANTHRO.109':'Anthro 109', 'ANTHRO.110':'Anthro 110', 'ANTHRO.112':'Anthro 112', 'ANTHRO.135':'Anthro 135',
	'COMPBIO.170B':'Biochemistry 170B',
	'BIOENG.C119':'Bioengineering C119', 'BIOENG.155':'Bioengineering 155',
	'BIOLOGY.1A':'Bio 1A', 'BIOLOGY.1B':'Bio 1B', 'BIOLOGY.11':'Bio 11',
	'CHMENG.170A':'ChemicalEngineering 170A', 'CHMENG.170E':'ChemicalEngineering 170E',
	'CIVENG.113':'CivEng 113',
	'COGSCI.C102':'CogSci C102', 'COGSCI.C110':'CogSci C110', 'COGSCI.C126':'CogSci C126', 'COGSCI.C127':'CogSci C127', 'COGSCI.C147':'CogSci C147',
	'COMPSCI.C182':'CompSci C182',
	'EPS.C30':'EPS C30', 'EPS.C82':'EPS C82', 'EPS.C129':'EPS C129', 'EPS.185':'EPS 185',
	'ENGLISH.C77':'English C77',
	'ESPM.2':'ESPM 2', 'ESPM.6':'ESPM 6', 'ESPM.8':'ESPM 8', 'ESPM.C10':'ESPM C10', 'ESPM.C11':'ESPM C11', 'ESPM.C12':'ESPM C12', 'ESPM.15':'ESPM 15', 'ESPM.36':'ESPM 36', 'ESPM.40':'ESPM 40', 'ESPM.42':'ESPM 42', 'ESPM.44':'ESPM 44', 'ESPM.100':'ESPM 100', 
	'ESPM.101A':'ESPM 101A', 'ESPM.101B':'ESPM 101B', 'ESPM.102A':'ESPM 102A', 'ESPM.102B':'ESPM 102B', 'ESPM.102C':'ESPM 102C', 'ESPM.C103':'ESPM C103', 'ESPM.105A':'ESPM 105A', 'ESPM.106':'ESPM 106', 'ESPM.C107':'ESPM C107', 'ESPM.108A':'ESPM 108A', 
	'ESPM.108B':'ESPM 108B', 'ESPM.109':'ESPM 109', 'ESPM.110':'ESPM 110', 'ESPM.111':'ESPM 111', 'ESPM.112':'ESPM 112', 'ESPM.113':'ESPM 113', 'ESPM.114':'ESPM 114', 'ESPM.115A':'ESPM 115A', 'ESPM.115B':'ESPM 115B', 'ESPM.115C':'ESPM 115C', 'ESPM.116A':'ESPM 116A',
	'ESPM.116B':'ESPM 116B', 'ESPM.116C':'ESPM 116C', 'ESPM.117':'ESPM 117', 'ESPM.118':'ESPM 118', 'ESPM.119':'ESPM 119', 'ESPM.129':'ESPM 129', 'ESPM.C129':'ESPM C129', 'ESPM.131':'ESPM 131', 'ESPM.132':'ESPM 132', 'ESPM.133':'ESPM 133', 'ESPM.134':'ESPM 134', 
	'ESPM.135':'ESPM 135', 'ESPM.136':'ESPM 136', 'ESPM.137':'ESPM 137', 'ESPM.138':'ESPM 138', 'ESPM.140':'ESPM 140', 'ESPM.141':'ESPM 141', 'ESPM.142':'ESPM 142', 'ESPM.143':'ESPM 143', 'ESPM.144':'ESPM 144', 'ESPM.145':'ESPM 145', 'ESPM.146':'ESPM 146', 
	'ESPM.149':'ESPM 149', 'ESPM.152':'ESPM 152', 'ESPM.164':'ESPM 164', 'ESPM.167':'ESPM 167', 'ESPM.181':'ESPM 181', 'ESPM.185':'ESPM 185', 'ESPM.186':'ESPM 186', 'ESPM.187':'ESPM 187', 'ESPM.189':'ESPM 189',
	'ENVSCI.10':'EnvironmentalScience 10', 'ENVSCI.C12':'EnvironmentalScience C12', 'ENVSCI.125':'EnvironmentalScience 125',
	'GEOG.30':'Geography 30', 'GEOG.40':'Geography 40', 'GEOG.C82':'Geography C82', 'GEOG.131':'Geography 131', 'GEOG.143':'Geography 143', 'GEOG.148':'Geography 148', 'GEOG.149':'Geography 149', 'GEOG.179D':'Geography 179D',
	'IDS.114A':'InterDepartmental 114A','IDS.114B':'InterDepartmental 114B',
	'LDARCH.12':'LandscapeArchitecture 12', 'LDARCH.110':'LandscapeArchitecture 110',
	'L&S.18':'L&S 18', 'L&S.19':'L&S 19', 'L&S.23':'L&S 23', 'L&S.C30T':'L&S C30T', 'L&S.C30U':'L&S C30U', 'L&S.C30V':'L&S C30V', 'L&S.C30W':'L&S C30W', 'L&S.C30X':'L&S C30X', 'L&S.117':'L&S 117', 'L&S.126':'L&S 126',
	'LINGUIS.C109':'Linguistics C109', 'LINGUIS.C147':'Linguistics C147', 'LINGUIS.160':'Linguistics 160',
	'MECENG.C176':'MecEng C176',
	'NUSCTX.10':'NutriSci 10', 'NUSCTX.11':'NutriSci 11', 'NUSCTX.39A':'NutriSci 39A', 'NUSCTX.39C':'NutriSci 39C', 'NUSCTX.100':'NutriSci 100', 'NUSCTX.103':'NutriSci 103', 'NUSCTX.106':'NutriSci 106', 'NUSCTX.110':'NutriSci 110', 'NUSCTX.113':'NutriSci 113', 
	'NUSCTX.120':'NutriSci 120', 'NUSCTX.150':'NutriSci 150', 'NUSCTX.160':'NutriSci 160', 'NUSCTX.161':'NutriSci 161', 'NUSCTX.170':'NutriSci 170',
	'OPTOM.10':'Optometry 10', 'OPTOM.C10':'Optometry C10', 'OPTOM.130':'Optometry 130',
	'PHYSED.32':'PE 32', 'PHYSED.C129':'PE C129', 'PHYSED.C165L':'PE C165L',
	'PHYSICS.177':'Physics 177',
	'PLANTBI.10':'PMB 10', 'PLANTBI.11':'PMB 11', 'PLANTBI.13':'PMB 13', 'PLANTBI.39A':'PMB 39A', 'PLANTBI.39B':'PMB 39B', 'PLANTBI.39C':'PMB 39C', 'PLANTBI.39D':'PMB 39D', 'PLANTBI.40':'PMB 40', 'PLANTBI.C41X':'PMB C41X', 'PLANTBI.100':'PMB 100', 'PLANTBI.101':'PMB 101', 
	'PLANTBI.102':'PMB 102', 'PLANTBI.C103':'PMB C103', 'PLANTBI.105':'PMB 105', 'PLANTBI.110':'PMB 110', 'PLANTBI.111':'PMB 111', 'PLANTBI.112':'PMB 112', 'PLANTBI.114':'PMB 114', 'PLANTBI.C116':'PMB C116', 'PLANTBI.120':'PMB 120', 'PLANTBI.130':'PMB 130', 
	'PLANTBI.135':'PMB 135', 'PLANTBI.140':'PMB 140', 'PLANTBI.142':'PMB 142', 'PLANTBI.C148':'PMB C148', 'PLANTBI.150':'PMB 150', 'PLANTBI.160':'PMB 160', 'PLANTBI.165':'PMB 165', 'PLANTBI.170':'PMB 170', 'PLANTBI.180':'PMB 180',
	'PSYCH.C19':'Psychology C19', 'PSYCH.39L':'Psychology 39L', 'PSYCH.100A':'Psychology 100A', 'PSYCH.110':'Psychology 110', 'PSYCH.111':'Psychology 111', 'PSYCH.C112':'Psychology C112', 'PSYCH.113':'Psychology 113', 'PSYCH.114':'Psychology 114', 'PSYCH.115A':'Psychology 115A',
	'PSYCH.115B':'Psychology 115B', 'PSYCH.C115C':'Psychology C115C', 'PSYCH.116':'Psychology 116', 'PSYCH.117':'Psychology 117', 'PSYCH.118':'Psychology 118', 'PSYCH.119':'Psychology 119', 'PSYCH.121':'Psychology 121', 'PSYCH.122':'Psychology 122', 'PSYCH.125':'Psychology 125',
	'PSYCH.C126':'Psychology C126', 'PSYCH.C127':'Psychology C127', 'PSYCH.C129':'Psychology C129', 'PSYCH.133':'Psychology 133',
	'PBHLTH.39C':'PublicHealth 39C', 'PBHLTH.39F':'PublicHealth 39F', 'PBHLTH.C102':'PublicHealth C102', 'PBHLTH.150C':'PublicHealth 150C', 'PBHLTH.C160':'PublicHealth C160', 'PBHLTH.161':'PublicHealth 161', 'PBHLTH.162A':'PublicHealth 162A', 'PBHLTH.162B':'PublicHealth 162B', 
	'PBHLTH.170':'PublicHealth 170', 'PBHLTH.170B':'PublicHealth 170B', 'PBHLTH.172':'PublicHealth 172',
	'UGIS.C10':'UGIS C10', 'UGIS.C12':'UGIS C12', 'UGIS.C130':'UGIS C130',
	'INTEGBI.C13':'IB C13', 'INTEGBI.24':'IB 24', 'INTEGBI.31':'IB 31', 'INTEGBI.N33':'IB N33', 'INTEGBI.35AC':'IB 35AC', 'INTEGBI.37':'IB 37', 'INTEGBI.41':'IB 41', 'INTEGBI.42':'IB 42', 'INTEGBI.C82':'IB C82', 'INTEGBI.84':'IB 84', 'INTEGBI.87':'IB 87', 'INTEGBI.88':'IB 88', 
	'INTEGBI.95':'IB 95', 'INTEGBI.C96':'IB C96', 'INTEGBI.98':'IB 98', 'INTEGBI.99':'IB 99', 'INTEGBI.100B':'IB 100B', 'INTEGBI.C100':'IB C100', 'INTEGBI.C101':'IB C101', 'INTEGBI.C101L':'IB C101L', 'INTEGBI.102LF':'IB 102LF', 'INTEGBI.103LF':'IB 103LF', 'INTEGBI.104LF':'IB 104LF',
	'INTEGBI.C105':'IB C105', 'INTEGBI.106A':'IB 106A', 'INTEGBI.C107L':'IB C107L', 'INTEGBI.C110L':'IB C110L', 'INTEGBI.112':'IB 112', 'INTEGBI.113L':'IB 113L', 'INTEGBI.115':'IB 115', 'INTEGBI.116L':'IB 116L', 'INTEGBI.117':'IB 117', 'INTEGBI.117LF':'IB 117LF', 'INTEGBI.118':'IB 118',
	'INTEGBI.119':'IB 119', 'INTEGBI.123AL':'IB 123AL', 'INTEGBI.C125L':'IB C125L', 'INTEGBI.127L':'IB 127L', 'INTEGBI.C129L':'IB C129L', 'INTEGBI.130':'IB 130', 'INTEGBI.131':'IB 131', 'INTEGBI.131A':'IB 131A', 'INTEGBI.131L':'IB 131L', 'INTEGBI.S131':'IB S131', 'INTEGBI.132':'IB 132',
	'INTEGBI.132L':'IB 132L', 'INTEGBI.133':'IB 133', 'INTEGBI.135':'IB 135', 'INTEGBI.C135L':'IB C135L', 'INTEGBI.136':'IB 136', 'INTEGBI.137':'IB 137', 'INTEGBI.138':'IB 138', 'INTEGBI.139':'IB 139', 'INTEGBI.140':'IB 140', 'INTEGBI.141':'IB 141', 'INTEGBI.C142L':'IB C142L', 
	'INTEGBI.C143A':'IB C143A', 'INTEGBI.C143B':'IB C143B', 'INTEGBI.144':'IB 144', 'INTEGBI.C144':'IB C144', 'INTEGBI.146':'IB 146', 'INTEGBI.146LF':'IB 146LF', 'INTEGBI.148':'IB 148', 'INTEGBI.C149':'IB C149', 'INTEGBI.151':'IB 151', 'INTEGBI.151L':'IB 151L', 'INTEGBI.152':'IB 152', 
	'INTEGBI.153':'IB 153', 'INTEGBI.153LF':'IB 153LF', 'INTEGBI.154':'IB 154', 'INTEGBI.154L':'IB 154L', 'INTEGBI.C155':'IB C155', 'INTEGBI.C156':'IB C156', 'INTEGBI.157LF':'IB 157LF', 'INTEGBI.158LF':'IB 158LF', 'INTEGBI.159':'IB 159', 'INTEGBI.160':'IB 160', 'INTEGBI.161':'IB 161', 
	'INTEGBI.162':'IB 162', 'INTEGBI.163':'IB 163', 'INTEGBI.164':'IB 164', 'INTEGBI.166':'IB 166', 'INTEGBI.167':'IB 167', 'INTEGBI.168':'IB 168', 'INTEGBI.168L':'IB 168L', 'INTEGBI.169':'IB 169', 'INTEGBI.173LF':'IB 173LF', 'INTEGBI.174LF':'IB 174LF', 'INTEGBI.175LF':'IB 175LF', 
	'INTEGBI.C176L':'IB C176L', 'INTEGBI.N176L':'IB N176L', 'INTEGBI.181L':'IB 181L', 'INTEGBI.183L':'IB 183L', 'INTEGBI.184L':'IB 184L', 'INTEGBI.C185L':'IB C185L', 'INTEGBI.C187':'IB C187', 'INTEGBI.190':'IB 190', 'INTEGBI.191':'IB 191', 'INTEGBI.194':'IB 194', 'INTEGBI.C195':'IB C195', 
	'INTEGBI.H196A':'IB H196A', 'INTEGBI.H196B':'IB H196B', 'INTEGBI.197':'IB 197', 'INTEGBI.198':'IB 198', 'INTEGBI.199':'IB 199',
	'MCELLBI.15':'MCB 15', 'MCELLBI.C31':'MCB C31', 'MCELLBI.32':'MCB 32', 'MCELLBI.32L':'MCB 32L', 'MCELLBI.N32L':'MCB N32L', 'MCELLBI.W32':'MCB W32', 'MCELLBI.41':'MCB 41', 'MCELLBI.C44':'MCB C44', 'MCELLBI.50':'MCB 50', 'MCELLBI.55':'MCB 55', 'MCELLBI.61':'MCB 61', 'MCELLBI.C61':'MCB C61',
	'MCELLBI.W61':'MCB W61', 'MCELLBI.C62':'MCB C62', 'MCELLBI.63':'MCB 63', 'MCELLBI.63X':'MCB 63X', 'MCELLBI.64':'MCB 64', 'MCELLBI.C64':'MCB C64', 'MCELLBI.84B':'MCB 84B', 'MCELLBI.90A':'MCB 90A', 'MCELLBI.90B':'MCB 90B', 'MCELLBI.90C':'MCB 90C', 'MCELLBI.90D':'MCB 90D', 'MCELLBI.90E':'MCB 90E', 
	'MCELLBI.91D':'MCB 91D', 'MCELLBI.C96':'MCB C96', 'MCELLBI.98':'MCB 98', 'MCELLBI.99':'MCB 99', 'MCELLBI.100B':'MCB 100B', 'MCELLBI.C100A':'MCB C100A', 'MCELLBI.102':'MCB 102', 'MCELLBI.C103':'MCB C103', 'MCELLBI.104':'MCB 104', 'MCELLBI.110':'MCB 110', 'MCELLBI.C110L':'MCB C110L', 
	'MCELLBI.110L':'MCB 110L', 'MCELLBI.C112':'MCB C112', 'MCELLBI.C112L':'MCB C112L', 'MCELLBI.113':'MCB 113', 'MCELLBI.C114':'MCB C114', 'MCELLBI.C116':'MCB C116', 'MCELLBI.118':'MCB 118', 'MCELLBI.130A':'MCB 130A', 'MCELLBI.N130L':'MCB N130L', 'MCELLBI.132':'MCB 132', 'MCELLBI.133L':'MCB 133L',
	'MCELLBI.C134':'MCB C134', 'MCELLBI.135A':'MCB 135A', 'MCELLBI.136':'MCB 136', 'MCELLBI.137':'MCB 137', 'MCELLBI.140':'MCB 140', 'MCELLBI.140L':'MCB 140L', 'MCELLBI.141':'MCB 141', 'MCELLBI.143':'MCB 143', 'MCELLBI.C148':'MCB C148', 'MCELLBI.149':'MCB 149', 'MCELLBI.150':'MCB 150',
	'MCELLBI.150L':'MCB 150L', 'MCELLBI.C160':'MCB C160', 'MCELLBI.160L':'MCB 160L', 'MCELLBI.163':'MCB 163', 'MCELLBI.165':'MCB 165', 'MCELLBI.166':'MCB 166', 'MCELLBI.167':'MCB 167', 'MCELLBI.180':'MCB 180', 'MCELLBI.180C':'MCB 180C', 'MCELLBI.H196A':'MCB H196A', 'MCELLBI.H196B':'MCB H196B', 
	'MCELLBI.197':'MCB 197', 'MCELLBI.198':'MCB 198', 'MCELLBI.199':'MCB 199'}
#http://ls-advise.berkeley.edu/requirement/breadth7/hs.html
historicalStudies={
	'AFRICAM.4A':'AfricanAmerican 4A', 'AFRICAM.4B':'AfricanAmerican 4B', 'AFRICAM.5A':'AfricanAmerican 5A', 'AFRICAM.5B':'AfricanAmerican 5B', 'AFRICAM.111':'AfricanAmerican 111', 'AFRICAM.113':'AfricanAmerican 113', 'AFRICAM.116':'AfricanAmerican 116',
	'AFRICAM.117':'AfricanAmerican 117', 'AFRICAM.121':'AfricanAmerican 121', 'AFRICAM.122':'AfricanAmerican 122', 'AFRICAM.123':'AfricanAmerican 123', 'AFRICAM.125':'AfricanAmerican 125', 'AFRICAM.126':'AfricanAmerican 126', 'AFRICAM.128':'AfricanAmerican 128',
	'AFRICAM.131':'AfricanAmerican 131', 'AFRICAM.C131':'AfricanAmerican C131', 'AFRICAM.N131':'AfricanAmerican N131', 'AFRICAM.135':'AfricanAmerican 135', 'AFRICAM.138':'AfricanAmerican 138', 'AFRICAM.150A':'AfricanAmerican 150A', 'AFRICAM.151B':'AfricanAmerican 151B',
	'AFRICAM.C178':'AfricanAmerican C178',
	'AMERSTD.10':'AmericanStudies 10', 'AMERSTD.10AC':'AmericanStudies 10AC', 'AMERSTD.C10':'AmericanStudies C10', 'AMERSTD.C112A':'AmericanStudies C112A', 'AMERSTD.C112B':'AmericanStudies C112B', 'AMERSTD.C112F':'AmericanStudies C112F', 'AMERSTD.C132':'AmericanStudies C132',
	'AMERSTD.C132B':'AmericanStudies C132B', 'AMERSTD.C171':'AmericanStudies C171', 'AMERSTD.172':'AmericanStudies 172', 'AMERSTD.C172':'AmericanStudies C172',
	'ANTHRO.2':'Anthro 2', 'ANTHRO.2AC':'Anthro 2AC', 'ANTHRO.10AC':'Anthro 10AC', 'ANTHRO.114':'Anthro 114', 'ANTHRO.121A':'Anthro 121A', 'ANTHRO.121AC':'Anthro 121AC', 'ANTHRO.121B':'Anthro 121B', 'ANTHRO.122A':'Anthro 122A', 'ANTHRO.122C':'Anthro 122C', 
	'ANTHRO.122D':'Anthro 122D', 'ANTHRO.122E':'Anthro 122E', 'ANTHRO.122F':'Anthro 122F', 'ANTHRO.123A':'Anthro 123A', 'ANTHRO.123B':'Anthro 123B', 'ANTHRO.123C':'Anthro 123C', 'ANTHRO.123D':'Anthro 123D', 'ANTHRO.123E':'Anthro 123E', 'ANTHRO.124A':'Anthro 124A',
	'ANTHRO.124AC':'Anthro 124AC', 'ANTHRO.C125A':'Anthro C125A', 'ANTHRO.C125B':'Anthro C125B', 'ANTHRO.129A':'Anthro 129A', 'ANTHRO.129C':'Anthro 129C', 'ANTHRO.C129F':'Anthro C129F', 'ANTHRO.134':'Anthro 134', 'ANTHRO.134A':'Anthro 134A', 'ANTHRO.173':'Anthro 173',
	'ANTHRO.174AC':'Anthro 174AC', 'ANTHRO.175':'Anthro 175', 'ANTHRO.180':'Anthro 180', 'ANTHRO.183':'Anthro 183', 'ANTHRO.187':'Anthro 187',
	'ARCH.130':'Architecture 130', 'ARCH.170A':'Architecture 170A', 'ARCH.170B':'Architecture 170B', 'ARCH.176':'Architecture 176', 'ARCH.179AC':'Architecture 179AC',
	'HISTART.34':'HistoryOfArt 34', 'HISTART.35':'HistoryOfArt 35', 'HISTART.39A':'HistoryOfArt 39A', 'HISTART.39B':'HistoryOfArt 39B', 'HISTART.39C':'HistoryOfArt 39C', 'HISTART.39D':'HistoryOfArt 39D', 'HISTART.39E':'HistoryOfArt 39E',
	'HISTART.39F':'HistoryOfArt 39F', 'HISTART.39G':'HistoryOfArt 39G', 'HISTART.39F':'HistoryOfArt 39F', 'HISTART.39H':'HistoryOfArt 39H', 'HISTART.39I':'HistoryOfArt 39I', 'HISTART.39J':'HistoryOfArt 39J', 'HISTART.39K':'HistoryOfArt 39K',
	'HISTART.39L':'HistoryOfArt 39L', 'HISTART.39M':'HistoryOfArt 39M', 'HISTART.39N':'HistoryOfArt 39N', 'HISTART.39O':'HistoryOfArt 39O', 'HISTART.39P':'HistoryOfArt 39P', 'HISTART.39Q':'HistoryOfArt 39Q', 'HISTART.39R':'HistoryOfArt 39R',
	'HISTART.39S':'HistoryOfArt 39S', 'HISTART.39T':'HistoryOfArt 39T', 'HISTART.39U':'HistoryOfArt 39U', 'HISTART.39V':'HistoryOfArt 39V', 'HISTART.39W':'HistoryOfArt 39W', 'HISTART.39X':'HistoryOfArt 39X', 'HISTART.39Y':'HistoryOfArt 39Y',
	'HISTART.39Z':'HistoryOfArt 39Z', 'HISTART.41':'HistoryOfArt 41', 'HISTART.51':'HistoryOfArt 51', 'HISTART.62':'HistoryOfArt 62', 'HISTART.65':'HistoryOfArt 65', 'HISTART.98':'HistoryOfArt 98', 'HISTART.100':'HistoryOfArt 100', 
	'HISTART.N104':'HistoryOfArt N104', 'HISTART.107':'HistoryOfArt 107', 'HISTART.108':'HistoryOfArt 108', 'HISTART.120':'HistoryOfArt 120', 'HISTART.C120A':'HistoryOfArt C120A', 'HISTART.C120B':'HistoryOfArt C120B', 'HISTART.C121A':'HistoryOfArt C121A',
	'HISTART.127':'HistoryOfArt 127', 'HISTART.130A':'HistoryOfArt 130A', 'HISTART.131A':'HistoryOfArt 131A', 'HISTART.131B':'HistoryOfArt 131B', 'HISTART.131C':'HistoryOfArt 131C', 'HISTART.134A':'HistoryOfArt 134A', 'HISTART.134B':'HistoryOfArt 134B', 
	'HISTART.134C':'HistoryOfArt 134C', 'HISTART.136A':'HistoryOfArt 136A', 'HISTART.136B':'HistoryOfArt 136B', 'HISTART.136C':'HistoryOfArt 136C', 'HISTART.C140':'HistoryOfArt C140', 'HISTART.141A':'HistoryOfArt 141A', 'HISTART.141B':'HistoryOfArt 141B',
	'HISTART.141C':'HistoryOfArt 141C', 'HISTART.145':'HistoryOfArt 145', 'HISTART.151':'HistoryOfArt 151', 'HISTART.156A':'HistoryOfArt 156A', 'HISTART.C156B':'HistoryOfArt C156B', 'HISTART.161':'HistoryOfArt 161', 'HISTART.162':'HistoryOfArt 162', 
	'HISTART.166':'HistoryOfArt 166', 'HISTART.169A':'HistoryOfArt 169A', 'HISTART.170':'HistoryOfArt 170', 'HISTART.171':'HistoryOfArt 171', 'HISTART.172':'HistoryOfArt 172', 'HISTART.173':'HistoryOfArt 173', 'HISTART.174':'HistoryOfArt 174', 
	'HISTART.175':'HistoryOfArt 175', 'HISTART.179':'HistoryOfArt 179', 'HISTART.180A':'HistoryOfArt 180A', 'HISTART.180C':'HistoryOfArt 180C', 'HISTART.N180A':'HistoryOfArt N180A', 'HISTART.N180B':'HistoryOfArt N180B', 'HISTART.N180C':'HistoryOfArt N180C', 
	'HISTART.N181':'HistoryOfArt N181', 'HISTART.182':'HistoryOfArt 182', 'HISTART.N182':'HistoryOfArt N182', 'HISTART.183':'HistoryOfArt 183', 'HISTART.183E':'HistoryOfArt 183E', 'HISTART.185':'HistoryOfArt 185', 'HISTART.185A':'HistoryOfArt 185A', 
	'HISTART.185B':'HistoryOfArt 185B', 'HISTART.N185C':'HistoryOfArt N185C', 'HISTART.186A':'HistoryOfArt 186A', 'HISTART.186C':'HistoryOfArt 186C', 'HISTART.N186C':'HistoryOfArt N186C', 'HISTART.187AC':'HistoryOfArt 187AC', 'HISTART.188':'HistoryOfArt 188',
	'HISTART.188A':'HistoryOfArt 188A', 'HISTART.189':'HistoryOfArt 189', 'HISTART.C189':'HistoryOfArt C189', 'HISTART.190A':'HistoryOfArt 190A', 'HISTART.190B':'HistoryOfArt 190B', 'HISTART.190C':'HistoryOfArt 190C', 'HISTART.190DH':'HistoryOfArt 190DH', 
	'HISTART.190E':'HistoryOfArt 190E', 'HISTART.190F':'HistoryOfArt 190F', 'HISTART.190G':'HistoryOfArt 190G', 'HISTART.N190A':'HistoryOfArt N190A', 'HISTART.N190B':'HistoryOfArt N190B', 'HISTART.N190C':'HistoryOfArt N190C', 'HISTART.N190D':'HistoryOfArt N190D',
	'HISTART.N190E':'HistoryOfArt N190E', 'HISTART.N190F':'HistoryOfArt N190F', 'HISTART.N190G':'HistoryOfArt N190G', 'HISTART.N190H':'HistoryOfArt N190H', 'HISTART.192A':'HistoryOfArt 192A', 'HISTART.192B':'HistoryOfArt 192B', 'HISTART.192C':'HistoryOfArt 192C',
	'HISTART.192D':'HistoryOfArt 192D', 'HISTART.192DH':'HistoryOfArt 192DH', 'HISTART.192F':'HistoryOfArt 192F', 'HISTART.192G':'HistoryOfArt 192G', 'HISTART.192H':'HistoryOfArt 192H', 'HISTART.192AC':'HistoryOfArt 192AC', 'HISTART.193':'HistoryOfArt 193', 
	'HISTART.194':'HistoryOfArt 194', 'HISTART.H195':'HistoryOfArt H195', 'HISTART.C196A':'HistoryOfArt C196A', 'HISTART.C196B':'HistoryOfArt C196B', 'HISTART.C196W':'HistoryOfArt C196W', 'HISTART.198':'HistoryOfArt 198', 'HISTART.199':'HistoryOfArt 199', 
	'HISTART.N199':'HistoryOfArt N199',
	'ASAMST.20A':'AsianAmerican 20A', 'ASAMST.120':'AsianAmerican 120', 'ASAMST.121':'AsianAmerican 121', 'ASAMST.122':'AsianAmerican 122', 'ASAMST.123':'AsianAmerican 123', 'ASAMST.124':'AsianAmerican 124', 'ASAMST.128AC':'AsianAmerican 128AC', 
	'ASAMST.131':'AsianAmerican 131','ASAMST.170':'AsianAmerican 170', 'ASAMST.171':'AsianAmerican 171', 'ASAMST.175':'AsianAmerican 175',
	'ASIANST.147':'AsianStudies 147', 'ASIANST.148':'AsianStudies 148',
	'BUDDSTD.C120':'BuddhistStudies C120', 'BUDDSTD.183':'BuddhistStudies 183',
	'UGBA.C172':'UGBA C172',
	'CELTIC.70':'Celtic 70', 'CELTIC.128':'Celtic 128', 'CELTIC.173':'Celtic 173',
	'CHICANO.50':'Chicano 50', 'CHICANO.130':'Chicano 130', 'CHICANO.135':'Chicano 135', 'CHICANO.135A':'Chicano 135A', 'CHICANO.135B':'Chicano 135B', 'CHICANO.150A':'Chicano 150A', 'CHICANO.150B':'Chicano 150B', 'CHICANO.161':'Chicano 161', 'CHICANO.162':'Chicano 162',
	
	'CHINESE.7A':'Chinese 7A', 'CHINESE.102':'Chinese 102', 'CHINESE.181':'Chinese 181', 'CHINESE.182':'Chinese 182', 'CHINESE.183':'Chinese 183',
	'CYPLAN.110':'CityPlanning 110','CYPLAN.112B':'CityPlanning 112B',
	'CLASSIC.10A':'Classics 10A', 'CLASSIC.10B':'Classics 10B', 'CLASSIC.17A':'Classics 17A', 'CLASSIC.17B':'Classics 17B', 'CLASSIC.29':'Classics 29', 'CLASSIC.36':'Classics 36', 'CLASSIC.C36':'Classics C36', 'CLASSIC.39B':'Classics 39B', 'CLASSIC.39G':'Classics 39G', 
	'CLASSIC.39I':'Classics 39I', 'CLASSIC.R44':'Classics R44', 'CLASSIC.121':'Classics 121', 'CLASSIC.155A':'Classics 155A', 'CLASSIC.155B':'Classics 155B', 'CLASSIC.161':'Classics 161',
	'COGSCI.C103':'CogSci C103',
	'COLWRIT.50AC':'CollegeWriting 50AC','COLWRIT.150AC':'CollegeWriting 150AC',
	'COMLIT.113':'ComparativeLiterature 113',
	'COMPSCI.39B':'CompSci 39B', 'COMPSCI.39C':'CompSci 39C', 'COMPSCI.39E':'CompSci 39E', 'COMPSCI.39K':'CompSci 39K',
	'DEMOG.145AC':'Demography 145AC',
	'DEVSTD.C100':'Development C100',
	'DUTCH.39A':'Dutch 39A', 'DUTCH.C170':'Dutch C170', 'DUTCH.171AC':'Dutch 171AC', 'DUTCH.173':'Dutch 173', 'DUTCH.175':'Dutch 175', 'DUTCH.177':'Dutch 177', 'DUTCH.C178':'Dutch C178',
	'EPS.C51':'EPS C51',
	'EALANG.109':'EastAsian 109','EALANG.C120':'EastAsian C120',
	'ECON.105':'Econ 105', 'ECON.113':'Econ 113', 'ECON.114':'Econ 114', 'ECON.115':'Econ 115', 'ECON.134':'Econ 134',
	'EDUC.122':'Educ 122','EDUC.183':'Educ 183',
	'ENGLISH.101':'English 101',
	'ENVDES.10':'EnvDesign 10', 'ENVDES.71':'EnvDesign 71', 'ENVDES.169A':'EnvDesign 169A', 'ENVDES.169B':'EnvDesign 169B', 'ENVDES.C169A':'EnvDesign C169A', 'ENVDES.C169B':'EnvDesign C169B',
	'ESPM.50AC':'ESPM 50AC', 'ESPM.160AC':'ESPM 160AC', 'ESPM.C160':'ESPM C160', 'ESPM.166':'ESPM 166', 'ESPM.C191':'ESPM C191',
	'ETHSTD.10A':'EthnicStudies 10A', 'ETHSTD.10AC':'EthnicStudies 10AC', 'ETHSTD.21AC':'EthnicStudies 21AC', 'ETHSTD.39A':'EthnicStudies 39A', 'ETHSTD.41AC':'EthnicStudies 41AC', 'ETHSTD.C73AC':'EthnicStudies C73AC', 'ETHSTD.124':'EthnicStudies 124', 
	'ETHSTD.130':'EthnicStudies 130', 'ETHSTD.130AC':'EthnicStudies 130AC', 'ETHSTD.132':'EthnicStudies 132',
	'FILM.25A':'Film 25A', 'FILM.25B':'Film 25B', 'FILM.129':'Film 129', 'FILM.160':'Film 160',
	'FRENCH.43':'French 43', 'FRENCH.43A':'French 43A', 'FRENCH.43B':'French 43B', 'FRENCH.145':'French 145', 'FRENCH.160A':'French 160A', 'FRENCH.160B':'French 160B', 'FRENCH.161A':'French 161A', 'FRENCH.161B':'French 161B', 'FRENCH.162A':'French 162A', 'FRENCH.162B':'French 162B', 'FRENCH.171A':'French 171A', 'FRENCH.171B':'French 171B', 'FRENCH.180A':'French 180A', 'FRENCH.180B':'French 180B', 'FRENCH.180C':'French 180C', 'FRENCH.180D':'French 180D', 'FRENCH.183A':'French 183A', 'FRENCH.183B':'French 183B',
	'GWS.100AC':'GWS 100AC', 'GWS.120':'GWS 120', 'GWS.122':'GWS 122', 'GWS.C145':'GWS C145', 'GWS.153A':'GWS 153A',
	'GEOG.39A':'Geography 39A', 'GEOG.51':'Geography 51', 'GEOG.55':'Geography 55', 'GEOG.70AC':'Geography 70AC', 'GEOG.C112':'Geography C112', 'GEOG.113':'Geography 113', 'GEOG.120':'Geography 120', 'GEOG.C152':'Geography C152', 'GEOG.154':'Geography 154', 'GEOG.157':'Geography 157', 'GEOG.158':'Geography 158', 'GEOG.160A':'Geography 160A', 'GEOG.160B':'Geography 160B', 'GEOG.C160A':'Geography C160A', 'GEOG.C160B':'Geography C160B', 'GEOG.163':'Geography 163', 'GEOG.164':'Geography 164', 'GEOG.165':'Geography 165', 'GEOG.166':'Geography 166', 'GEOG.167':'Geography 167', 'GEOG.168':'Geography 168', 'GEOG.189':'Geography 189',
	'GREEK.120':'Greek 120', 'GREEK.121':'Greek 121', 'GREEK.122':'Greek 122',
	'HMEDSCI.C133':'HealthMedical C133',
	'IAS.45':'International 45', 'IAS.145':'International 145', 'IAS.C145':'International C145', 'IAS.147':'International 147', 'IAS.148':'International 148',
	'ITALIAN.39F':'Italian 39F', 'ITALIAN.40':'Italian 40', 'ITALIAN.70':'Italian 70', 'ITALIAN.103':'Italian 103', 'ITALIAN.160':'Italian 160', 'ITALIAN.N160':'Italian N160',
	'LEGALST.103':'Legal 103', 'LEGALST.111':'Legal 111', 'LEGALST.112':'Legal 112', 'LEGALST.116':'Legal 116', 'LEGALST.121':'Legal 121', 'LEGALST.160':'Legal 160', 'LEGALST.161':'Legal 161', 'LEGALST.171':'Legal 171', 'LEGALST.174':'Legal 174', 'LEGALST.175':'Legal 175', 'LEGALST.176':'Legal 176', 'LEGALST.177':'Legal 177', 'LEGALST.178':'Legal 178',
	'L&S.16':'L&S 16', 'L&S.17':'L&S 17', 'L&S.21':'L&S 21', 'L&S.26':'L&S 26', 'L&S.40A':'L&S 40A', 'L&S.40AC':'L&S 40AC', 'L&S.40B':'L&S 40B', 'L&S.40C':'L&S 40C', 'L&S.C40T':'L&S C40T', 'L&S.C60U':'L&S C60U', 'L&S.C70X':'L&S C70X', 'L&S.120':'L&S 120', 'L&S.122':'L&S 122', 'L&S.123':'L&S 123', 'L&S.140A':'L&S 140A', 'L&S.140B':'L&S 140B', 'L&S.140C':'L&S 140C', 'L&S.140D':'L&S 140D', 'L&S.C140T':'L&S C140T', 'L&S.C140U':'L&S C140U', 'L&S.C140V':'L&S C140V', 'L&S.148':'L&S 148',
	'LGBT.145':'LGBT 145',
	'MUSIC.39F':'MUSIC 39F', 'MUSIC.75':'MUSIC 75', 'MUSIC.76':'MUSIC 76', 'MUSIC.77':'MUSIC 77', 'MUSIC.128':'MUSIC 128', 'MUSIC.128A':'MUSIC 128A', 'MUSIC.128AM':'MUSIC 128AM', 'MUSIC.128B':'MUSIC 128B', 'MUSIC.128BM':'MUSIC 128BM', 'MUSIC.128D':'MUSIC 128D', 'MUSIC.128DM':'MUSIC 128DM', 'MUSIC.128E':'MUSIC 128E', 'MUSIC.128P':'MUSIC 128P', 'MUSIC.128Q':'MUSIC 128Q', 'MUSIC.128R':'MUSIC 128R', 'MUSIC.128RM':'MUSIC 128RM', 'MUSIC.128S':'MUSIC 128S', 'MUSIC.128SM':'MUSIC 128SM', 'MUSIC.128T':'MUSIC 128T', 'MUSIC.128TM':'MUSIC 128TM', 'MUSIC.130A':'MUSIC 130A', 'MUSIC.130AM':'MUSIC 130AM', 'MUSIC.130B':'MUSIC 130B', 'MUSIC.137AC':'MUSIC 137AC',
	'NESTUD.15':'NearEasternStudies 15', 'NESTUD.18':'NearEasternStudies 18', 'NESTUD.20':'NearEasternStudies 20', 'NESTUD.C26':'NearEasternStudies C26', 'NESTUD.101A':'NearEasternStudies 101A', 'NESTUD.101B':'NearEasternStudies 101B', 'NESTUD.102A':'NearEasternStudies 102A', 'NESTUD.102B':'NearEasternStudies 102B', 'NESTUD.105A':'NearEasternStudies 105A', 'NESTUD.105B':'NearEasternStudies 105B', 'NESTUD.106A':'NearEasternStudies 106A', 'NESTUD.106B':'NearEasternStudies 106B', 'NESTUD.107':'NearEasternStudies 107', 'NESTUD.109':'NearEasternStudies 109', 'NESTUD.110':'NearEasternStudies 110', 'NESTUD.112':'NearEasternStudies 112', 'NESTUD.C120A':'NearEasternStudies C120A', 'NESTUD.C120B':'NearEasternStudies C120B', 'NESTUD.122':'NearEasternStudies 122', 'NESTUD.122A':'NearEasternStudies 122A', 'NESTUD.122B':'NearEasternStudies 122B', 'NESTUD.123':'NearEasternStudies 123', 'NESTUD.123A':'NearEasternStudies 123A', 'NESTUD.123B':'NearEasternStudies 123B', 'NESTUD.124':'NearEasternStudies 124', 'NESTUD.124A':'NearEasternStudies 124A', 'NESTUD.124B':'NearEasternStudies 124B', 'NESTUD.125':'NearEasternStudies 125', 'NESTUD.126':'NearEasternStudies 126', 'NESTUD.128':'NearEasternStudies 128', 'NESTUD.C129':'NearEasternStudies C129', 'NESTUD.130A':'NearEasternStudies 130A', 'NESTUD.130B':'NearEasternStudies 130B', 'NESTUD.131':'NearEasternStudies 131', 'NESTUD.C133':'NearEasternStudies C133', 'NESTUD.134':'NearEasternStudies 134', 'NESTUD.C135':'NearEasternStudies C135', 'NESTUD.136':'NearEasternStudies 136', 'NESTUD.137':'NearEasternStudies 137', 'NESTUD.140':'NearEasternStudies 140', 'NESTUD.141':'NearEasternStudies 141', 'NESTUD.143A':'NearEasternStudies 143A', 'NESTUD.143B':'NearEasternStudies 143B', 'NESTUD.144':'NearEasternStudies 144', 'NESTUD.146A':'NearEasternStudies 146A', 'NESTUD.146B':'NearEasternStudies 146B', 'NESTUD.147':'NearEasternStudies 147', 'NESTUD.150A':'NearEasternStudies 150A', 'NESTUD.150B':'NearEasternStudies 150B', 'NESTUD.160':'NearEasternStudies 160', 'NESTUD.162A':'NearEasternStudies 162A', 'NESTUD.162B':'NearEasternStudies 162B', 'NESTUD.171':'NearEasternStudies 171', 'NESTUD.173A':'NearEasternStudies 173A', 'NESTUD.173B':'NearEasternStudies 173B', 'NESTUD.175':'NearEasternStudies 175',
	'PHILOS.9':'Philosophy 9', 'PHILOS.25A':'Philosophy 25A', 'PHILOS.25B':'Philosophy 25B', 'PHILOS.C25A':'Philosophy C25A', 'PHILOS.114':'Philosophy 114', 'PHILOS.C151':'Philosophy C151', 'PHILOS.C152':'Philosophy C152', 'PHILOS.153':'Philosophy 153', 'PHILOS.160':'Philosophy 160', 'PHILOS.161':'Philosophy 161', 'PHILOS.163':'Philosophy 163', 'PHILOS.170':'Philosophy 170', 'PHILOS.171':'Philosophy 171', 'PHILOS.172':'Philosophy 172', 'PHILOS.173':'Philosophy 173', 'PHILOS.174':'Philosophy 174', 'PHILOS.175':'Philosophy 175', 'PHILOS.176':'Philosophy 176', 'PHILOS.178':'Philosophy 178', 'PHILOS.183':'Philosophy 183', 'PHILOS.184':'Philosophy 184',
	'PACS.125AC':'PACS 125AC','PACS.161':'PACS 161',
	'NAVSCI.2':'NavalScience 2',
	'PHYSED.39':'PE 39',
	'MATH.160':'Math 160',
	'POLSCI.33':'PoliSci 33', 'POLSCI.112A':'PoliSci 112A', 'POLSCI.112B':'PoliSci 112B', 'POLSCI.112C':'PoliSci 112C', 'POLSCI.112D':'PoliSci 112D', 'POLSCI.113A':'PoliSci 113A', 'POLSCI.N113A':'PoliSci N113A', 'POLSCI.115C':'PoliSci 115C', 'POLSCI.122A':'PoliSci 122A', 'POLSCI.124A':'PoliSci 124A', 'POLSCI.136A':'PoliSci 136A', 'POLSCI.137B':'PoliSci 137B', 'POLSCI.141A':'PoliSci 141A', 'POLSCI.146C':'PoliSci 146C', 'POLSCI.N146C':'PoliSci N146C',
	'PBHLTH.183':'PublicHealth 183',
	'RELIGST.120A':'ReligiousStudies 120A', 'RELIGST.120B':'ReligiousStudies 120B', 'RELIGST.123':'ReligiousStudies 123', 'RELIGST.C124':'ReligiousStudies C124', 'RELIGST.125':'ReligiousStudies 125', 'RELIGST.130':'ReligiousStudies 130', 'RELIGST.C132':'ReligiousStudies C132', 'RELIGST.C133':'ReligiousStudies C133', 'RELIGST.C134':'ReligiousStudies C134', 'RELIGST.C135':'ReligiousStudies C135', 'RELIGST.C156':'ReligiousStudies C156', 'RELIGST.C157':'ReligiousStudies C157', 'RELIGST.C164':'ReligiousStudies C164', 'RELIGST.173AC':'ReligiousStudies 173AC',
	'RHETOR.106':'Rhetoric 106', 'RHETOR.116':'Rhetoric 116', 'RHETOR.152':'Rhetoric 152', 'RHETOR.152AC':'Rhetoric 152AC', 'RHETOR.153':'Rhetoric 153', 'RHETOR.155':'Rhetoric 155', 'RHETOR.166':'Rhetoric 166',
	'THEATER.39A':'TDPS 39A', 'THEATER.125':'TDPS 125', 'THEATER.151A':'TDPS 151A', 'THEATER.151B':'TDPS 151B', 'THEATER.153A':'TDPS 153A', 'THEATER.153B':'TDPS 153B',
	'UGIS.44A':'UGIS 44A', 'UGIS.44B':'UGIS 44B', 'UGIS.44C':'UGIS 44C', 'UGIS.55A':'UGIS 55A', 'UGIS.55B':'UGIS 55B', 'UGIS.C132':'UGIS C132', 'UGIS.C133':'UGIS C133', 'UGIS.C136':'UGIS C136', 'UGIS.C145':'UGIS C145', 'UGIS.C152':'UGIS C152', 'UGIS.C153':'UGIS C153', 'UGIS.C154':'UGIS C154', 'UGIS.C155':'UGIS C155', 'UGIS.162A':'UGIS 162A',
	'SLAVIC.39A':'Slavic 39A', 'SLAVIC.39B':'Slavic 39B', 'SLAVIC.39D':'Slavic 39D', 'SLAVIC.39H':'Slavic 39H', 'SLAVIC.39I':'Slavic 39I', 'SLAVIC.100':'Slavic 100', 'SLAVIC.130':'Slavic 130', 'SLAVIC.131':'Slavic 131', 'SLAVIC.C139':'Slavic C139', 'SLAVIC.148':'Slavic 148', 'SLAVIC.149AC':'Slavic 149AC', 'SLAVIC.158':'Slavic 158', 'SLAVIC.190':'Slavic 190',
	'SOCIOL.131':'Sociology 131', 'SOCIOL.131AC':'Sociology 131AC', 'SOCIOL.181':'Sociology 181', 'SOCIOL.181':'Sociology 181', 'SOCIOL.186':'Sociology 186', 'SOCIOL.C189':'Sociology C189',
	'SPANISH.40':'Spanish 40', 'SPANISH.112':'Spanish 112', 'SPANISH.113':'Spanish 113', 'SPANISH.122':'Spanish 122', 'SPANISH.C178':'Spanish C178',
	'LATIN.100':'Latin 100', 'LATIN.120':'Latin 120', 'LATIN.121':'Latin 121', 'LATIN.155A':'Latin 155A', 'LATIN.155B':'Latin 155B',
	'LINGUIS.11':'Linguistics 11', 'LINGUIS.22':'Linguistics 22', 'LINGUIS.55AC':'Linguistics 55AC', 'LINGUIS.71':'Linguistics 71', 'LINGUIS.C139':'Linguistics C139', 'LINGUIS.155AC':'Linguistics 155AC',
	'JAPAN.7A':'Japanese 7A', 'JAPAN.80':'Japanese 80', 'JAPAN.102':'Japanese 102', 'JAPAN.104':'Japanese 104',
	'MILAFF.20':'MilitaryAffairs 20', 'MILAFF.120':'MilitaryAffairs 120', 'MILAFF.121':'MilitaryAffairs 121', 'MILAFF.123':'MilitaryAffairs 123', 'MILAFF.154':'MilitaryAffairs 154',
	'NATAMST.20A':'NativeAmerican 20A', 'NATAMST.71':'NativeAmerican 71', 'NATAMST.72':'NativeAmerican 72', 'NATAMST.90':'NativeAmerican 90', 'NATAMST.145':'NativeAmerican 145', 'NATAMST.173':'NativeAmerican 173',
	'NATAMST.175':'NativeAmerican 175', 'NATAMST.176':'NativeAmerican 176', 'NATAMST.177':'NativeAmerican 177', 'NATAMST.178':'NativeAmerican 178',
	'SCANDIN.75':'Scandinavian 75', 'SCANDIN.123':'Scandinavian 123', 'SCANDIN.127':'Scandinavian 127', 'SCANDIN.128':'Scandinavian 128', 'SCANDIN.132':'Scandinavian 132',
	'SASIAN.1A':'SouthAsian 1A', 'SASIAN.1B':'SouthAsian 1B', 'SASIAN.110A':'SouthAsian 110A', 'SASIAN.110B':'SouthAsian 110B', 'SASIAN.144':'SouthAsian 144', 'SASIAN.146':'SouthAsian 146', 'SASIAN.148':'SouthAsian 148', 'SASIAN.151':'SouthAsian 151',
	'SEASIAN.10A':'SouthEastAsian 10A', 'SEASIAN.10B':'SouthEastAsian 10B', 'SEASIAN.137':'SouthEastAsian 137', 'SEASIAN.138':'SouthEastAsian 138',
	'SOCWEL.C129':'Social Welfare C129',
	'PUBPOL.39':'PublicPolicy 39',
	'PSYCH.109':'Psychology 109',
	'MEDST.150':'Medieval 150',
	'KOREAN.7A':'Korean 7A','KOREAN.102':'Korean 102',
	'JOURN.39A':'Journalism 39A', 'JOURN.39AC':'Journalism 39AC', 'JOURN.140':'Journalism 140',
	'LDARCH.170':'LandscapeArchitecture 170','LDARCH.C171':'LandscapeArchitecture C171',
	'IDS.100AC':'InterDepartmental 100AC',
	'PORTUG.39A':'Portugese 39A', 'PORTUG.112':'Portugese 112', 'PORTUG.113':'Portugese 113',
	'MEDIA.104B':'Media 104B', 'MEDIA.104C':'Media 104C', 'MEDIA.C103':'Media C103',
	'POLECON.160':'PoliEcon 160','POLECON.160A':'PoliEcon 160A',
	'ISF.145':'ISF 145','ISF.C145':'ISF C145',
	'JEWISH.39B':'Jewish 39B','JEWISH.39E':'Jewish 39E',
	'INFO.C103':'Info C103','INFO.182AC':'Info 182AC',
	'SSEASN.C110':'SouthSouthEastAsian C110', 'SSEASN.C112':'SouthSouthEastAsian C112', 'SSEASN.C123':'SouthSouthEastAsian C123',
	'HISTORY.2':'History 2', 'HISTORY.3':'History 3', 'HISTORY.4A':'History 4A', 'HISTORY.4B':'History 4B', 'HISTORY.5':'History 5', 'HISTORY.W5':'History W5', 'HISTORY.6A':'History 6A', 'HISTORY.6B':'History 6B',
	'HISTORY.7A':'History 7A', 'HISTORY.7B':'History 7B', 'HISTORY.8A':'History 8A', 'HISTORY.8B':'History 8B', 'HISTORY.10':'History 10', 'HISTORY.11':'History 11', 'HISTORY.12':'History 12', 'HISTORY.14':'History 14',
	'HISTORY.24':'History 24', 'HISTORY.39C':'History 39C', 'HISTORY.39D':'History 39D', 'HISTORY.39E':'History 39E', 'HISTORY.39F':'History 39F', 'HISTORY.39G':'History 39G', 'HISTORY.39H':'History 39H',
	'HISTORY.39I':'History 39I', 'HISTORY.39J':'History 39J', 'HISTORY.39K':'History 39K', 'HISTORY.39L':'History 39L', 'HISTORY.39M':'History 39M', 'HISTORY.84':'History 84', 'HISTORY.98':'History 98', 'HISTORY.100':'History 100',
	'HISTORY.100AC':'History 100AC', 'HISTORY.100AP':'History 100AP', 'HISTORY.100B':'History 100B', 'HISTORY.100BP':'History 100BP', 'HISTORY.100D':'History 100D', 'HISTORY.100E':'History 100E', 'HISTORY.100F':'History 100F', 
	'HISTORY.100H':'History 100H', 'HISTORY.100L':'History 100L', 'HISTORY.100M':'History 100M', 'HISTORY.N100':'History N100', 'HISTORY.100S':'History 100S', 'HISTORY.100U':'History 100U', 'HISTORY.100UP':'History 100UP', 
	'HISTORY.101':'History 101', 'HISTORY.103A':'History 103A', 'HISTORY.103B':'History 103B', 'HISTORY.103C':'History 103C', 'HISTORY.103D':'History 103D', 'HISTORY.103E':'History 103E', 'HISTORY.103F':'History 103F', 
	'HISTORY.103H':'History 103H', 'HISTORY.103S':'History 103S', 'HISTORY.103U':'History 103U', 'HISTORY.104':'History 104', 'HISTORY.105A':'History 105A', 'HISTORY.105B':'History 105B', 'HISTORY.106A':'History 106A', 
	'HISTORY.106B':'History 106B', 'HISTORY.N106A':'History N106A', 'HISTORY.N106B':'History N106B', 'HISTORY.108':'History 108', 'HISTORY.109A':'History 109A', 'HISTORY.109B':'History 109B', 'HISTORY.109C':'History 109C',
	'HISTORY.N109C':'History N109C', 'HISTORY.111A':'History 111A', 'HISTORY.111B':'History 111B', 'HISTORY.111C':'History 111C', 'HISTORY.C111B':'History C111B', 'HISTORY.111D':'History 111D', 'HISTORY.112B':'History 112B',
	'HISTORY.112C':'History 112C', 'HISTORY.N112B':'History N112B', 'HISTORY.113A':'History 113A', 'HISTORY.113B':'History 113B', 'HISTORY.114A':'History 114A', 'HISTORY.114B':'History 114B', 'HISTORY.116A':'History 116A', 
	'HISTORY.116B':'History 116B', 'HISTORY.116C':'History 116C', 'HISTORY.116D':'History 116D', 'HISTORY.116G':'History 116G', 'HISTORY.117A':'History 117A', 'HISTORY.117D':'History 117D', 'HISTORY.118A':'History 118A', 
	'HISTORY.118B':'History 118B', 'HISTORY.118C':'History 118C', 'HISTORY.119A':'History 119A', 'HISTORY.N119A':'History N119A', 'HISTORY.120AC':'History 120AC', 'HISTORY.121B':'History 121B', 'HISTORY.122AC':'History 122AC', 
	'HISTORY.123':'History 123', 'HISTORY.124A':'History 124A', 'HISTORY.124B':'History 124B', 'HISTORY.N124A':'History N124A', 'HISTORY.N124B':'History N124B', 'HISTORY.125A':'History 125A', 'HISTORY.125B':'History 125B', 
	'HISTORY.N125B':'History N125B', 'HISTORY.126A':'History 126A', 'HISTORY.126B':'History 126B', 'HISTORY.127AC':'History 127AC', 'HISTORY.130B':'History 130B', 'HISTORY.131B':'History 131B', 'HISTORY.N131B':'History N131B',
	'HISTORY.C132B':'History C132B', 'HISTORY.134A':'History 134A', 'HISTORY.135':'History 135', 'HISTORY.136':'History 136', 'HISTORY.136AC':'History 136AC', 'HISTORY.137AC':'History 137AC', 'HISTORY.138':'History 138', 
	'HISTORY.138T':'History 138T', 'HISTORY.C139B':'History C139B', 'HISTORY.C139C':'History C139C', 'HISTORY.140B':'History 140B', 'HISTORY.141B':'History 141B', 'HISTORY.143':'History 143', 'HISTORY.N143':'History N143',
	'HISTORY.146':'History 146', 'HISTORY.149B':'History 149B', 'HISTORY.150B':'History 150B', 'HISTORY.151A':'History 151A', 'HISTORY.151B':'History 151B', 'HISTORY.151C':'History 151C', 'HISTORY.N151C':'History N151C', 
	'HISTORY.152A':'History 152A', 'HISTORY.154':'History 154', 'HISTORY.155A':'History 155A', 'HISTORY.155B':'History 155B', 'HISTORY.C157':'History C157', 'HISTORY.158A':'History 158A', 'HISTORY.158B':'History 158B', 
	'HISTORY.158C':'History 158C', 'HISTORY.N158C':'History N158C', 'HISTORY.159A':'History 159A', 'HISTORY.159B':'History 159B', 'HISTORY.160':'History 160', 'HISTORY.162A':'History 162A', 'HISTORY.162B':'History 162B',
	'HISTORY.N162A':'History N162A', 'HISTORY.163A':'History 163A', 'HISTORY.163B':'History 163B', 'HISTORY.164A':'History 164A', 'HISTORY.164B':'History 164B', 'HISTORY.164C':'History 164C', 'HISTORY.S164B':'History S164B',
	'HISTORY.165A':'History 165A', 'HISTORY.165B':'History 165B', 'HISTORY.165D':'History 165D', 'HISTORY.166A':'History 166A', 'HISTORY.166B':'History 166B', 'HISTORY.166C':'History 166C', 'HISTORY.167A':'History 167A', 
	'HISTORY.167B':'History 167B', 'HISTORY.167C':'History 167C', 'HISTORY.168A':'History 168A', 'HISTORY.169A':'History 169A', 'HISTORY.170':'History 170', 'HISTORY.171A':'History 171A', 'HISTORY.171B':'History 171B', 
	'HISTORY.171C':'History 171C', 'HISTORY.172':'History 172', 'HISTORY.173B':'History 173B', 'HISTORY.173C':'History 173C', 'HISTORY.174A':'History 174A', 'HISTORY.174B':'History 174B', 'HISTORY.C175B':'History C175B',
	'HISTORY.177A':'History 177A', 'HISTORY.177B':'History 177B', 'HISTORY.178':'History 178', 'HISTORY.180':'History 180', 'HISTORY.180T':'History 180T', 'HISTORY.181B':'History 181B', 'HISTORY.182A':'History 182A', 
	'HISTORY.182AT':'History 182AT', 'HISTORY.183':'History 183', 'HISTORY.183A':'History 183A', 'HISTORY.185A':'History 185A', 'HISTORY.185B':'History 185B', 'HISTORY.186':'History 186', 'HISTORY.C187':'History C187', 
	'HISTORY.C188A':'History C188A', 'HISTORY.C191':'History C191', 'HISTORY.C192':'History C192', 'HISTORY.C194':'History C194', 'HISTORY.H195':'History H195', 'HISTORY.C196A':'History C196A', 'HISTORY.C196B':'History C196B',
	'HISTORY.C196W':'History C196W', 'HISTORY.198':'History 198', 'HISTORY.199':'History 199',
	}
#http://ls-advise.berkeley.edu/requirement/breadth7/is.html
international={
	'AFRICAM.4B':'AfricanAmerican 4B', 'AFRICAM.8A':'AfricanAmerican 8A', 'AFRICAM.8B':'AfricanAmerican 8B', 'AFRICAM.9A':'AfricanAmerican 9A', 'AFRICAM.9B':'AfricanAmerican 9B', 'AFRICAM.10A':'AfricanAmerican 10A', 
	'AFRICAM.10B':'AfricanAmerican 10B', 'AFRICAM.14A':'AfricanAmerican 14A', 'AFRICAM.14B':'AfricanAmerican 14B', 'AFRICAM.15A':'AfricanAmerican 15A', 'AFRICAM.15B':'AfricanAmerican 15B', 'AFRICAM.19A':'AfricanAmerican 19A',
	'AFRICAM.19B':'AfricanAmerican 19B', 'AFRICAM.31A':'AfricanAmerican 31A', 'AFRICAM.31B':'AfricanAmerican 31B', 'AFRICAM.112A':'AfricanAmerican 112A', 'AFRICAM.112B':'AfricanAmerican 112B', 'AFRICAM.113':'AfricanAmerican 113',
	'AFRICAM.128':'AfricanAmerican 128', 'AFRICAM.131':'AfricanAmerican 131', 'AFRICAM.C131':'AfricanAmerican C131', 'AFRICAM.N131':'AfricanAmerican N131', 'AFRICAM.135':'AfricanAmerican 135', 'AFRICAM.160':'AfricanAmerican 160',
	'ANTHRO.147C':'Anthro 147C', 'ANTHRO.C147B':'Anthro C147B', 'ANTHRO.152':'Anthro 152', 'ANTHRO.170':'Anthro 170', 'ANTHRO.171':'Anthro 171', 'ANTHRO.175':'Anthro 175', 'ANTHRO.176':'Anthro 176', 'ANTHRO.177':'Anthro 177', 
	'ANTHRO.178':'Anthro 178', 'ANTHRO.179':'Anthro 179', 'ANTHRO.180':'Anthro 180', 'ANTHRO.181':'Anthro 181', 'ANTHRO.182':'Anthro 182', 'ANTHRO.183':'Anthro 183', 'ANTHRO.184':'Anthro 184', 'ANTHRO.185':'Anthro 185', 
	'ANTHRO.C186':'Anthro C186', 'ANTHRO.187':'Anthro 187', 'ANTHRO.188':'Anthro 188',
	'ARABIC.20A':'Arabic 20A', 'ARABIC.20B':'Arabic 20B', 'ARABIC.21':'Arabic 21', 'ARABIC.50':'Arabic 50',
	'ASIANST.10':'AsianStudies 10', 'ASIANST.110':'AsianStudies 110', 'ASIANST.147':'AsianStudies 147', 'ASIANST.148':'AsianStudies 148', 'ASIANST.149':'AsianStudies 149', 'ASIANST.150':'AsianStudies 150',
	'CELTIC.85':'Celtic 85', 'CELTIC.86':'Celtic 86', 'CELTIC.106C':'Celtic 106C', 'CELTIC.115':'Celtic 115', 'CELTIC.116B':'Celtic 116B', 'CELTIC.129':'Celtic 129',
	'CHICANO.10':'Chicano 10', 'CHICANO.135C':'Chicano 135C', 'CHICANO.161':'Chicano 161', 'CHICANO.163':'Chicano 163',
	'CHINESE.10':'Chinese 10', 'CHINESE.10A':'Chinese 10A', 'CHINESE.10B':'Chinese 10B', 'CHINESE.100A':'Chinese 100A', 'CHINESE.100B':'Chinese 100B', 'CHINESE.100S':'Chinese 100S', 'CHINESE.153':'Chinese 153', 'CHINESE.C184':'Chinese C184',
	'DEMOG.140':'Demoography 140', 'DEMOG.C165':'Demoography C165', 'DEMOG.C175':'Demoography C175',
	'DUTCH.110':'Dutchy 110', 'DUTCH.125':'Dutchy 125', 'DUTCH.C170':'Dutchy C170', 'DUTCH.174':'Dutchy 174',
	'AFRKANS.150':'Afrikaans 150',
	'HISTART.131C':'HistoryOfArt 131C',
	'ART.119':'Art 119',
	'BUDDSTD.C128':'Buddhist C128','BUDDSTD.181':'Buddhist 181',
	'UGBA.118':'UGBA 118','UGBA.178':'UGBA 178',
	'CATALAN.101':'Catalan 101','CATALAN.102':'Catalan 102',
	'CYPLAN.111':'CityPlanning 111','CYPLAN.115':'CityPlanning 115',
	'CLASSIC.N172A':'Classics N172A',
	'COMLIT.171':'CompLit 171',
	'ECON.90':'Econ 90', 'ECON.115':'Econ 115', 'ECON.151':'Econ 151', 'ECON.161':'Econ 161', 'ECON.162':'Econ 162', 'ECON.171':'Econ 171', 'ECON.172':'Econ 172', 'ECON.C175':'Econ C175', 'ECON.C181':'Econ C181', 'ECON.182':'Econ 182',
	'EALANG.C128':'EastAsian C128',
	'ENERES.162':'ERG 162',
	'ENVDES.100':'EnvDesign 100',
	'ENVECON.151':'EEP 151', 'ENVECON.152':'EEP 152', 'ENVECON.153':'EEP 153', 'ENVECON.C181':'EEP C181',
	'ESPM.C107':'ESPM C107', 'ESPM.155':'ESPM 155', 'ESPM.165':'ESPM 165', 'ESPM.166':'ESPM 166', 'ESPM.168':'ESPM 168', 'ESPM.169':'ESPM 169', 'ESPM.184':'ESPM 184',
	'GWS.14':'GWS 14', 'GWS.102':'GWS 102', 'GWS.141':'GWS 141', 'GWS.142':'GWS 142', 'GWS.144':'GWS 144',
	'FRENCH.3':'French 3', 'FRENCH.4':'French 4', 'FRENCH.14':'French 14',
	'GEOG.4':'Geography 4', 'GEOG.10':'Geography 10', 'GEOG.20':'Geography 20', 'GEOG.N20':'Geography N20', 'GEOG.C32':'Geography C32', 'GEOG.35':'Geography 35', 'GEOG.51':'Geography 51', 'GEOG.55':'Geography 55',
	'GEOG.100':'Geography 100', 'GEOG.104':'Geography 104', 'GEOG.108':'Geography 108', 'GEOG.110':'Geography 110', 'GEOG.111':'Geography 111', 'GEOG.C112':'Geography C112', 'GEOG.115':'Geography 115', 
	'GEOG.116':'Geography 116', 'GEOG.130':'Geography 130', 'GEOG.133':'Geography 133', 'GEOG.138':'Geography 138', 'GEOG.C152':'Geography C152', 'GEOG.153':'Geography 153', 'GEOG.157':'Geography 157', 
	'GEOG.164':'Geography 164', 'GEOG.169':'Geography 169',
	'GERMAN.3':'German 3', 'GERMAN.4':'German 4', 'GERMAN.50':'German 50', 'GERMAN.100':'German 100', 'GERMAN.101':'German 101', 'GERMAN.102A':'German 102A', 'GERMAN.102B':'German 102B', 'GERMAN.102C':'German 102C',
	'GERMAN.102D':'German 102D', 'GERMAN.103':'German 103', 'GERMAN.150':'German 150', 'GERMAN.160D':'German 160D', 'GERMAN.188':'German 188',
	'HEBREW.20A':'Hebrew 20A', 'HEBREW.20B':'Hebrew 20B', 'HEBREW.30':'Hebrew 30',
	'HINURD.100A':'Hindi-Urdu 100A', 'HINURD.100B':'Hindi-Urdu 100B', 'HINURD.101A':'Hindi-Urdu 101A', 'HINURD.101B':'Hindi-Urdu 101B', 'HINURD.103A':'Hindi-Urdu 103A', 'HINURD.103B':'Hindi-Urdu 103B',
	'HISTORY.160':'History 160', 'HISTORY.161':'History 161', 'HISTORY.162B':'History 162B', 'HISTORY.C176':'History C176', 'HISTORY.186':'History 186', 'HISTORY.C194':'History C194',
	'INTEGBI.C158':'IB C158',
	'IAS.20':'IAS 20', 'IAS.105':'IAS 105', 'IAS.105A':'IAS 105A', 'IAS.105B':'IAS 105B', 'IAS.113':'IAS 113', 'IAS.115':'IAS 115', 'IAS.120':'IAS 120', 'IAS.C142':'IAS C142', 'IAS.143':'IAS 143', 
	'IAS.145':'IAS 145', 'IAS.C145':'IAS C145', 'IAS.147':'IAS 147', 'IAS.148':'IAS 148', 'IAS.150':'IAS 150', 'IAS.160':'IAS 160', 'IAS.C170':'IAS C170', 'IAS.180':'IAS 180',
	'ISF.60':'ISF 60', 'ISF.100A':'ISF 100A', 'ISF.100D':'ISF 100D', 'ISF.100E':'ISF 100E', 'ISF.100H':'ISF 100H', 'ISF.145':'ISF 145', 'ISF.C145':'ISF C145',
	'JAPAN.10':'Japanese 10', 'JAPAN.10A':'Japanese 10A', 'JAPAN.10B':'Japanese 10B', 'JAPAN.B10':'Japanese B10', 'JAPAN.80':'Japanese 80', 'JAPAN.100B':'Japanese 100B', 'JAPAN.160':'Japanese 160','JAPAN.161':'Japanese 161',
	'ITALIAN.3':'Italian 3','ITALIAN.4':'Italian 4',
	'DEVSTD.C10':'Development C10', 'DEVSTD.C100':'Development C100', 'DEVSTD.150':'Development 150',
	'EAEURST.100':'EastEuropean 100',
	'ETHSTD.N180':'Ethnic N180','ETHSTD.N190':'Ethnic N190',
	'FILIPN.100A':'Filipino  100A', 'FILIPN.100B':'Filipino  100B', 'FILIPN.110A':'Filipino  110A',
	'GPP.105':'GPP 105','GPP.115':'GPP 115',
	'JOURN.39E':'Journalism 39E','JOURN.C183':'Journalism C183',
	'KHMER.101A':'Khmer 101A','KHMER.101B':'Khmer 101B',
	'KOREAN.10':'Korean  10', 'KOREAN.10A':'Korean  10A', 'KOREAN.10B':'Korean  10B', 'KOREAN.100A':'Korean  100A', 'KOREAN.100B':'Korean  100B',
	'EURAST.101A':'Eurasian 101A',
	'LEGALST.157':'LegalStudies  157', 'LEGALST.161':'LegalStudies  161', 'LEGALST.179':'LegalStudies  179',
	'LGBT.C147B':'LGBT C147B',
	'L&S.150A':'L&S  150A', 'L&S.150B':'L&S  150B', 'L&S.150C':'L&S  150C', 'L&S.C150T':'L&S  C150T',
	'LINGUIS.12':'Linguistics 12','LINGUIS.18':'Linguistics 18',
	'MUSIC.74':'Music 74', 'MUSIC.C131A':'Music C131A', 'MUSIC.132':'Music 132', 'MUSIC.133A':'Music 133A', 'MUSIC.133C':'Music 133C', 'MUSIC.133D':'Music 133D', 'MUSIC.134A':'Music 134A', 
	'MUSIC.134B':'Music 134B', 'MUSIC.C134C':'Music C134C', 'MUSIC.135':'Music 135', 'MUSIC.135A':'Music 135A', 'MUSIC.136':'Music 136', 'MUSIC.139':'Music 139',
	'NESTD.10':'NearEastern 10', 'NESTD.C26':'NearEastern C26', 'NESTD.127':'NearEastern 127', 'NESTD.154':'NearEastern 154', 'NESTD.165':'NearEastern 165', 'NESTD.175':'NearEastern 175',
	'PACS.124':'PACS 124', 'PACS.126':'PACS 126', 'PACS.127':'PACS 127', 'PACS.127A':'PACS 127A', 'PACS.127B':'PACS 127B', 'PACS.N127A':'PACS N127A', 'PACS.128AC':'PACS 128AC', 'PACS.135':'PACS 135',
	'PACS.149':'PACS 149', 'PACS.151':'PACS 151', 'PACS.164A':'PACS 164A', 'PACS.164B':'PACS 164B',
	'POLSCI.2':'PoliSci 2', 'POLSCI.5':'PoliSci 5', 'POLSCI.39B':'PoliSci 39B', 'POLSCI.39C':'PoliSci 39C', 'POLSCI.40':'PoliSci 40', 'POLSCI.117':'PoliSci 117', 'POLSCI.120A':'PoliSci 120A', 
	'POLSCI.120B':'PoliSci 120B', 'POLSCI.121A':'PoliSci 121A', 'POLSCI.121B':'PoliSci 121B', 'POLSCI.121C':'PoliSci 121C', 'POLSCI.122A':'PoliSci 122A', 'POLSCI.123':'PoliSci 123', 
	'POLSCI.123B':'PoliSci 123B', 'POLSCI.124A':'PoliSci 124A', 'POLSCI.124B':'PoliSci 124B', 'POLSCI.124C':'PoliSci 124C', 'POLSCI.125':'PoliSci 125', 'POLSCI.126A':'PoliSci 126A', 
	'POLSCI.126B':'PoliSci 126B', 'POLSCI.127A':'PoliSci 127A', 'POLSCI.128':'PoliSci 128', 'POLSCI.129B':'PoliSci 129B', 'POLSCI.136A':'PoliSci 136A', 'POLSCI.136B':'PoliSci 136B', 
	'POLSCI.137A':'PoliSci 137A', 'POLSCI.137B':'PoliSci 137B', 'POLSCI.137C':'PoliSci 137C', 'POLSCI.138A':'PoliSci 138A', 'POLSCI.138B':'PoliSci 138B', 'POLSCI.138C':'PoliSci 138C', 
	'POLSCI.138D':'PoliSci 138D', 'POLSCI.138E':'PoliSci 138E', 'POLSCI.138F':'PoliSci 138F', 'POLSCI.138G':'PoliSci 138G', 'POLSCI.139A':'PoliSci 139A', 'POLSCI.139B':'PoliSci 139B', 
	'POLSCI.139C':'PoliSci 139C', 'POLSCI.140B':'PoliSci 140B', 'POLSCI.140C':'PoliSci 140C', 'POLSCI.140D':'PoliSci 140D', 'POLSCI.140F':'PoliSci 140F', 'POLSCI.141A':'PoliSci 141A', 
	'POLSCI.141B':'PoliSci 141B', 'POLSCI.141C':'PoliSci 141C', 'POLSCI.142A':'PoliSci 142A', 'POLSCI.142B':'PoliSci 142B', 'POLSCI.143A':'PoliSci 143A', 'POLSCI.143B':'PoliSci 143B', 
	'POLSCI.143C':'PoliSci 143C', 'POLSCI.143D':'PoliSci 143D', 'POLSCI.143E':'PoliSci 143E', 'POLSCI.144A':'PoliSci 144A', 'POLSCI.144B':'PoliSci 144B', 'POLSCI.145A':'PoliSci 145A', 
	'POLSCI.145B':'PoliSci 145B', 'POLSCI.W145A':'PoliSci W145A', 'POLSCI.146A':'PoliSci 146A', 'POLSCI.146B':'PoliSci 146B', 'POLSCI.146C':'PoliSci 146C', 'POLSCI.N146C':'PoliSci N146C', 
	'POLSCI.147A':'PoliSci 147A', 'POLSCI.147B':'PoliSci 147B', 'POLSCI.147D':'PoliSci 147D', 'POLSCI.147E':'PoliSci 147E', 'POLSCI.147G':'PoliSci 147G', 'POLSCI.147H':'PoliSci 147H', 
	'POLSCI.148A':'PoliSci 148A', 'POLSCI.148B':'PoliSci 148B', 'POLSCI.149A':'PoliSci 149A', 'POLSCI.149B':'PoliSci 149B', 'POLSCI.149C':'PoliSci 149C', 'POLSCI.149D':'PoliSci 149D', 
	'POLSCI.149E':'PoliSci 149E', 'POLSCI.149F':'PoliSci 149F', 'POLSCI.149G':'PoliSci 149G', 'POLSCI.149H':'PoliSci 149H', 'POLSCI.149I':'PoliSci 149I', 'POLSCI.149J':'PoliSci 149J', 
	'POLSCI.149K':'PoliSci 149K', 'POLSCI.149L':'PoliSci 149L', 'POLSCI.149M':'PoliSci 149M', 'POLSCI.149N':'PoliSci 149N', 'POLSCI.149O':'PoliSci 149O', 'POLSCI.149P':'PoliSci 149P', 
	'POLSCI.149Q':'PoliSci 149Q', 'POLSCI.149R':'PoliSci 149R', 'POLSCI.149S':'PoliSci 149S', 'POLSCI.149T':'PoliSci 149T', 'POLSCI.149U':'PoliSci 149U', 'POLSCI.149V':'PoliSci 149V', 
	'POLSCI.149W':'PoliSci 149W', 'POLSCI.149X':'PoliSci 149X', 'POLSCI.149Y':'PoliSci 149Y', 'POLSCI.149Z':'PoliSci 149Z', 'POLSCI.149E':'PoliSci 149E', 'POLSCI.182':'PoliSci 182',
	'SCANDIN.12':'Scandinavian 12', 'SCANDIN.100A':'Scandinavian 100A', 'SCANDIN.100B':'Scandinavian 100B', 'SCANDIN.102':'Scandinavian 102', 'SCANDIN.170':'Scandinavian 170',
	'SLAVIC.3':'Slavic 3', 'SLAVIC.4':'Slavic 4', 'SLAVIC.20':'Slavic 20', 'SLAVIC.37':'Slavic 37', 'SLAVIC.R37W':'Slavic R37W', 'SLAVIC.39C':'Slavic 39C', 'SLAVIC.39F':'Slavic 39F', 
	'SLAVIC.39M':'Slavic 39M', 'SLAVIC.50':'Slavic 50', 'SLAVIC.115A':'Slavic 115A', 'SLAVIC.115B':'Slavic 115B', 'SLAVIC.116A':'Slavic 116A', 'SLAVIC.116B':'Slavic 116B', 'SLAVIC.117A':'Slavic 117A',
	'SLAVIC.117B':'Slavic 117B', 'SLAVIC.118A':'Slavic 118A', 'SLAVIC.118B':'Slavic 118B',
	'RHETOR.39G':'Rhetoric 39G',
	'SOCIOL.C116G':'Sociology C116G', 'SOCIOL.122A':'Sociology 122A', 'SOCIOL.127':'Sociology 127', 'SOCIOL.145L':'Sociology 145L', 'SOCIOL.146':'Sociology 146', 'SOCIOL.146AC':'Sociology 146AC',
	'SOCIOL.180C':'Sociology 180C', 'SOCIOL.180E':'Sociology 180E', 'SOCIOL.180I':'Sociology 180I', 'SOCIOL.180P':'Sociology 180P', 'SOCIOL.182':'Sociology 182', 'SOCIOL.183':'Sociology 183', 
	'SOCIOL.C183':'Sociology C183', 'SOCIOL.184':'Sociology 184', 'SOCIOL.C184':'Sociology C184', 'SOCIOL.189':'Sociology 189', 'SOCIOL.C189':'Sociology C189',
	'PUNJABI.100A':'Punjabi 100A','PUNJABI.100B':'Punjabi 100B',
	'PUBPOL.176':'PublicPolicy 176',
	'PBHLTH.112':'PublicHealth 112',
	'PERSIAN.20':'Persian 20', 'PERSIAN.100A':'Persian 100A', 'PERSIAN.100B':'Persian 100B',
	'PORTUG.26':'Portugese 26', 'PORTUG.N135':'Portugese N135', 'PORTUG.C170':'Portugese C170',
	'THEATER.113':'TDPS 113', 'THEATER.113A':'TDPS 113A', 'THEATER.122':'TDPS 122',
	'UGIS.118':'UGIS 118', 'UGIS.C134':'UGIS C134', 'UGIS.C147B':'UGIS C147B', 'UGIS.161':'UGIS 161', 'UGIS.162L':'UGIS 162L',
	'TAMIL.100A':'Tamil 100A', 'TAMIL.100B':'Tamil 100B', 'TAMIL.101A':'Tamil 101A', 'TAMIL.101B':'Tamil 101B',
	'THAI.100A':'Thai 100A', 'THAI.100B':'Thai 100B', 'THAI.180':'Thai 180',
	'SPANISH.3':'Spanish 3', 'SPANISH.4':'Spanish 4', 'SPANISH.N12':'Spanish N12', 'SPANISH.122':'Spanish 122', 'SPANISH.129':'Spanish 129',
	'VIETNMS.100A':'Vietnamese 100A', 'VIETNMS.100B':'Vietnamese 100B', 'VIETNMS.101B':'Vietnamese 101B',
	'YIDDISH.102':'Yiddish 102',
	'TURKISH.100A':'Turkish 100A','TURKISH.100B':'Turkish 100B',
	'TIBETAN.10A':'Tibetan 10A','TIBETAN.10B':'Tibetan 10B',
	'SEASIAN.10A':'SouthEastAsian 10A', 'SEASIAN.10B':'SouthEastAsian 10B', 'SEASIAN.C145':'SouthEastAsian C145',
	'LATAMST.10':'LatinAmerican 10','LATAMST.150':'LatinAmerican 150',
	'MALAYI.100A':'Malay/Indonesian 100A','MALAYI.100B':'Malay/Indonesian 100B',
	'MEDIA.160':'Media 160',
	'MESTU.10':'MiddleEastern 10', 'MESTU.20':'MiddleEastern 20', 'MESTU.150':'MiddleEastern 150',
	'OPTOM.39B':'Optometry 39B',
	'SSEASN.39C':'SouthSouthEastAsian 39C', 'SSEASN.C113':'SouthSouthEastAsian C113', 'SSEASN.C145':'SouthSouthEastAsian C145',
	'POLECON.101':'PoliticalEcon 101','POLECON.150':'PoliticalEcon 150'}
#http://ls-advise.berkeley.edu/requirement/breadth7/pv.html
philosophyValues={
	'BUDDHST.39A':'Buddhist 39A', 'BUDDHST.C50':'Buddhist C50', 'BUDDHST.C114':'Buddhist C114', 'BUDDHST.C115':'Buddhist C115', 'BUDDHST.C122':'Buddhist C122', 'BUDDHST.C124':'Buddhist C124', 
	'BUDDHST.C126':'Buddhist C126', 'BUDDHST.C128':'Buddhist C128', 'BUDDHST.C130':'Buddhist C130', 'BUDDHST.C135':'Buddhist C135', 'BUDDHST.154':'Buddhist 154', 'BUDDHST.C154':'Buddhist C154',
	'BUDDHST.181':'Buddhist 181',
	'UGBA.39AC':'UGBA 39AC', 'UGBA.107':'UGBA 107', 'UGBA.170':'UGBA 170',
	'ANTHRO.150':'Anthro 150', 'ANTHRO.156B':'Anthro 156B', 'ANTHRO.158':'Anthro 158',
	'CLASSIC.10A':'Classics 10A', 'CLASSIC.10B':'Classics 10B', 'CLASSIC.28':'Classics 28', 'CLASSIC.29':'Classics 29', 'CLASSIC.34':'Classics 34', 'CLASSIC.36':'Classics 36', 'CLASSIC.C36':'Classics C36', 
	'CLASSIC.39A':'Classics 39A', 'CLASSIC.39D':'Classics 39D', 'CLASSIC.39E':'Classics 39E', 'CLASSIC.39F':'Classics 39F', 'CLASSIC.100A':'Classics 100A', 'CLASSIC.100B':'Classics 100B', 
	'CLASSIC.121':'Classics 121', 'CLASSIC.124':'Classics 124', 'CLASSIC.130':'Classics 130', 'CLASSIC.132':'Classics 132', 'CLASSIC.161':'Classics 161', 'CLASSIC.163':'Classics 163', 
	'CLASSIC.178':'Classics 178',
	'EALANG.C50':'EastAsianLanguages C50', 'EALANG.105':'EastAsianLanguages 105', 'EALANG.C124':'EastAsianLanguages C124', 'EALANG.C126':'EastAsianLanguages C126', 'EALANG.C128':'EastAsianLanguages C128',
	'EALANG.C130':'EastAsianLanguages C130', 'EALANG.C135':'EastAsianLanguages C135',
	'EDUC.39D':'Educ 39D', 'EDUC.180':'Educ 180', 'EDUC.184':'Educ 184', 'EDUC.189':'Educ 189',
	'ESPM.C12':'ESPM C12', 'ESPM.39E':'ESPM 39E', 'ESPM.50AC':'ESPM 50AC', 'ESPM.161':'ESPM 161', 'ESPM.162':'ESPM 162', 'ESPM.163AC':'ESPM 163AC',
	'GERMAN.C25':'German C25', 'GERMAN.C75':'German C75', 'GERMAN.C113':'German C113', 'GERMAN.142':'German 142', 'GERMAN.143':'German 143', 'GERMAN.157A':'German 157A', 'GERMAN.157B':'German 157B',
	'GERMAN.157C':'German 157C', 'GERMAN.157D':'German 157D', 'GERMAN.C157B':'German C157B', 'GERMAN.C159':'German C159', 'GERMAN.162':'German 162', 'GERMAN.164':'German 164', 'GERMAN.176':'German 176',
	'GREEK.100':'Greek 100', 'GREEK.105':'Greek 105', 'GREEK.123':'Greek 123',
	'HISTORY.30':'History 30', 'HISTORY.C132B':'History C132B', 'HISTORY.C157':'History C157', 'HISTORY.164A':'History 164A', 'HISTORY.164B':'History 164B', 'HISTORY.164C':'History 164C', 
	'HISTORY.C175A':'History C175A', 'HISTORY.C175B':'History C175B', 'HISTORY.C191':'History C191',
	'ENGIN.124':'E 124', 'ENGIN.125':'E 125', 'ENGIN.130AC':'E 130AC',
	'ENGLISH.39A':'English 39A', 'ENGLISH.C77':'English C77', 'ENGLISH.177':'English 177',
	'CHINESE.130':'Chinese 130', 'CHINESE.183':'Chinese 183', 'CHINESE.C185':'Chinese C185', 'CHINESE.186':'Chinese 186',
	'CHICANO.110':'Chicano 110',
	'CELTIC.C168':'Celtic C168', 'CELTIC.169':'Celtic 169', 'CELTIC.173':'Celtic 173',
	'BIOENG.100':'BioEng 100',
	'ARABIC.108':'Arabic 108',
	'COGSCI.C101':'CogSci C101', 'COGSCI.C108':'CogSci C108', 'COGSCI.139':'CogSci 139',
	'HEBREW.101A':'Hebrew 101A',
	'HMEDSCI.C133':'HealthMedical C133',
	'GPP.105':'GPP 105',
	'GEOG.31':'Geography 31','GEOG.37':'Geography 37',
	'ETHSTD.145':'Ethnic 145','ETHSTD.C170':'Ethnic C170',
	'COMPSCI.39D':'CompSci 39D','COMPSCI.39M':'CompSci 39M',
	'COMLIT.39G':'CompLit 39G',
	'ISF.39A':'ISF 39A', 'ISF.39B':'ISF 39B', 'ISF.60':'ISF 60', 'ISF.61':'ISF 61', 'ISF.100A':'ISF 100A', 'ISF.100B':'ISF 100B', 'ISF.100E':'ISF 100E', 'ISF.100G':'ISF 100G',
	'IAS.105':'IAS 105', 'IAS.105A':'IAS 105A', 'IAS.105B':'IAS 105B',
	'ITALIAN.30':'ITALIAN 30', 'ITALIAN.130A':'ITALIAN 130A', 'ITALIAN.130B':'ITALIAN 130B',
	'JAPAN.C115':'Japanese C115',
	'JEWISH.39D':'Jewish 39D',
	'JOURN.165':'Journalism 165',
	'LATIN.116':'Latin 116',
	'LEGALST.19AC':'Legal 19AC', 'LEGALST.39D':'Legal 39D', 'LEGALST.39E':'Legal 39E', 'LEGALST.100':'Legal 100', 'LEGALST.100A':'Legal 100A', 'LEGALST.100B':'Legal 100B', 'LEGALST.101':'Legal 101',
	'LEGALST.103':'Legal 103', 'LEGALST.105':'Legal 105', 'LEGALST.107':'Legal 107', 'LEGALST.108':'Legal 108', 'LEGALST.109':'Legal 109', 'LEGALST.110':'Legal 110', 'LEGALST.112':'Legal 112', 
	'LEGALST.114':'Legal 114', 'LEGALST.115':'Legal 115', 'LEGALST.119':'Legal 119', 'LEGALST.120':'Legal 120', 'LEGALST.121':'Legal 121', 'LEGALST.140':'Legal 140', 'LEGALST.142':'Legal 142', 
	'LEGALST.150':'Legal 150', 'LEGALST.151':'Legal 151', 'LEGALST.161':'Legal 161', 'LEGALST.167':'Legal 167',
	'L&S.18':'L&S 18', 'L&S.27':'L&S 27', 'L&S.60A':'L&S 60A', 'L&S.C60T':'L&S C60T', 'L&S.C60U':'L&S C60U', 'L&S.116':'L&S 116', 'L&S.121':'L&S 121', 'L&S.123':'L&S 123', 'L&S.124':'L&S 124', 
	'L&S.126':'L&S 126', 'L&S.C140T':'L&S C140T', 'L&S.160A':'L&S 160A', 'L&S.160B':'L&S 160B', 'L&S.160C':'L&S 160C', 'L&S.160D':'L&S 160D', 'L&S.160E':'L&S 160E', 'L&S.C160T':'L&S C160T', 
	'L&S.C160U':'L&S C160U', 'L&S.C160V':'L&S C160V', 'L&S.C180U':'L&S C180U',
	'LINGUIS.52':'Linguistics 52', 'LINGUIS.105':'Linguistics 105', 'LINGUIS.106':'Linguistics 106', 'LINGUIS.C108':'Linguistics C108', 'LINGUIS.C142':'Linguistics C142',
	'MATH.10':'Math 10', 'MATH.125A':'Math 125A', 'MATH.125B':'Math 125B', 'MATH.135':'Math 135',
	'MEDIA.104A':'Media 104A',
	'MILAFF.144':'MilitaryAffairs 144',
	'MCELLBI 168':'MCB 168',
	'NESTUD.30':'NearEastern 30', 'NESTUD.34':'NearEastern 34', 'NESTUD.40':'NearEastern 40', 'NESTUD.42':'NearEastern 42', 'NESTUD.C92':'NearEastern C92', 'NESTUD.101B':'NearEastern 101B', 
	'NESTUD.102A':'NearEastern 102A', 'NESTUD.102B':'NearEastern 102B', 'NESTUD.C103':'NearEastern C103', 'NESTUD.C104':'NearEastern C104', 'NESTUD.105A':'NearEastern 105A', 'NESTUD.105B':'NearEastern 105B',
	'NESTUD.131':'NearEastern 131', 'NESTUD.C133':'NearEastern C133', 'NESTUD.134':'NearEastern 134', 'NESTUD.C135':'NearEastern C135', 'NESTUD.137':'NearEastern 137', 'NESTUD.142':'NearEastern 142', 
	'NESTUD.144':'NearEastern 144', 'NESTUD.146A':'NearEastern 146A', 'NESTUD.146B':'NearEastern 146B', 'NESTUD.160':'NearEastern 160',
	'NAVSCI.3':'Naval 3',
	'PACS.100':'PACS 100', 'PACS.126':'PACS 126', 'PACS.127':'PACS 127', 'PACS.127A':'PACS 127A', 'PACS.127B':'PACS 127B', 'PACS.N127A':'PACS N127A', 'PACS.128AC':'PACS 128AC', 'PACS.151':'PACS 151',
	'PACS.155':'PACS 155', 'PACS.164A':'PACS 164A', 'PACS.164B':'PACS 164B', 'PACS.165':'PACS 165', 'PACS.170':'PACS 170',
	'POLECON.100':'PoliticalEcon 100','POLECON.101':'PoliticalEcon 101',
	'POLSCI.4':'PoliticalScience 4', 'POLSCI.39A':'PoliticalScience 39A', 'POLSCI.60AC':'PoliticalScience 60AC', 'POLSCI.108A':'PoliticalScience 108A', 'POLSCI.112A':'PoliticalScience 112A', 
	'POLSCI.112B':'PoliticalScience 112B', 'POLSCI.112C':'PoliticalScience 112C', 'POLSCI.112D':'PoliticalScience 112D', 'POLSCI.N113A':'PoliticalScience N113A', 'POLSCI.114A':'PoliticalScience 114A',
	'POLSCI.115A':'PoliticalScience 115A', 'POLSCI.115B':'PoliticalScience 115B', 'POLSCI.115C':'PoliticalScience 115C', 'POLSCI.116':'PoliticalScience 116', 'POLSCI.116M':'PoliticalScience 116M', 
	'POLSCI.117':'PoliticalScience 117', 'POLSCI.124C':'PoliticalScience 124C', 'POLSCI.140H':'PoliticalScience 140H', 'POLSCI.C163A':'PoliticalScience C163A', 'POLSCI.C163B':'PoliticalScience C163B',
	'PSYCH.107':'Psychology 107', 'PSYCH.162':'Psychology 162', 'PSYCH.C162':'Psychology C162',
	'PBHLTH.116':'PublicHealth 116',
	'AFRICAM.C124':'AfricanAmerican C124', 'AFRICAM.138':'AfricanAmerican 138', 'AFRICAM.C175':'AfricanAmerican C175',
	'PUBPOL.C103':'PublicPolicy C103', 'PUBPOL.159':'PublicPolicy 159', 'PUBPOL.170':'PublicPolicy 170', 'PUBPOL.186':'PublicPolicy 186', 'PUBPOL.189':'PublicPolicy 189',
	'RELIGST.90A':'Religious 90A', 'RELIGST.C90B':'Religious C90B', 'RELIGST.C103':'Religious C103', 'RELIGST.C104':'Religious C104', 'RELIGST.C108':'Religious C108', 'RELIGST.C109':'Religious C109', 
	'RELIGST.111':'Religious 111', 'RELIGST.C112':'Religious C112', 'RELIGST.115':'Religious 115', 'RELIGST.C118':'Religious C118', 'RELIGST.120A':'Religious 120A', 'RELIGST.120B':'Religious 120B', 
	'RELIGST.123':'Religious 123', 'RELIGST.C124':'Religious C124', 'RELIGST.125':'Religious 125', 'RELIGST.130':'Religious 130', 'RELIGST.C132':'Religious C132', 'RELIGST.C133':'Religious C133', 
	'RELIGST.C134':'Religious C134', 'RELIGST.C135':'Religious C135', 'RELIGST.C156':'Religious C156', 'RELIGST.C157':'Religious C157', 'RELIGST.161':'Religious 161', 'RELIGST.162':'Religious 162', 
	'RELIGST.C162':'Religious C162', 'RELIGST.C163':'Religious C163', 'RELIGST.C164':'Religious C164', 'RELIGST.C165':'Religious C165', 'RELIGST.C166':'Religious C166', 'RELIGST.171AC':'Religious 171AC', 
	'RELIGST.172AC':'Religious 172AC', 'RELIGST.173AC':'Religious 173AC', 'RELIGST.C175':'Religious C175', 'RELIGST.182':'Religious 182', 'RELIGST.C185A':'Religious C185A', 'RELIGST.C185B':'Religious C185B', 
	'RELIGST.190':'Religious 190',
	'RHETOR.39B':'Rhetoric 39B', 'RHETOR.39G':'Rhetoric 39G', 'RHETOR.50A':'Rhetoric 50A', 'RHETOR.50B':'Rhetoric 50B', 'RHETOR.50C':'Rhetoric 50C', 'RHETOR.50D':'Rhetoric 50D', 'RHETOR.103A':'Rhetoric 103A',
	'RHETOR.103B':'Rhetoric 103B', 'RHETOR.105T':'Rhetoric 105T', 'RHETOR.107':'Rhetoric 107', 'RHETOR.108':'Rhetoric 108', 'RHETOR.117':'Rhetoric 117', 'RHETOR.120A':'Rhetoric 120A', 'RHETOR.120C':'Rhetoric 120C',
	'RHETOR.131':'Rhetoric 131', 'RHETOR.141AC':'Rhetoric 141AC', 'RHETOR.157A':'Rhetoric 157A', 'RHETOR.157B':'Rhetoric 157B', 'RHETOR.159A':'Rhetoric 159A', 'RHETOR.159B':'Rhetoric 159B', 'RHETOR.165':'Rhetoric 165',
	'SOCIOL.101':'Sociology 101', 'SOCIOL.102':'Sociology 102', 'SOCIOL.112':'Sociology 112', 'SOCIOL.137AC':'Sociology 137AC', 'SOCIOL.151':'Sociology 151', 'SOCIOL.163':'Sociology 163',
	'SLAVIC.134C':'Slavic 134C', 'SLAVIC.134D':'Slavic 134D', 'SLAVIC.134G':'Slavic 134G',
	'SASIAN.C114':'SouthAsian C114', 'SASIAN.127':'SouthAsian 127', 'SASIAN.C128':'SouthAsian C128', 'SASIAN.129':'SouthAsian 129', 'SASIAN.131':'SouthAsian 131', 'SASIAN.C140':'SouthAsian C140', 
	'SASIAN.141':'SouthAsian 141', 'SASIAN.C141':'SouthAsian C141', 'SASIAN.C142':'SouthAsian C142', 'SASIAN.151':'SouthAsian 151', 'SASIAN.C154':'SouthAsian C154', 'SASIAN.155':'SouthAsian 155', 
	'SASIAN.160':'SouthAsian 160', 'SASIAN.165':'SouthAsian 165',
	'UGIS.C12':'UGIS C12', 'UGIS.C133':'UGIS C133', 'UGIS.C152':'UGIS C152', 'UGIS.C153':'UGIS C153', 'UGIS.C154':'UGIS C154', 'UGIS.C155':'UGIS C155', 'UGIS.170':'UGIS 170',
	'SSEASN.C51':'SouthSouthEastAsian C51', 'SSEASN.C52':'SouthSouthEastAsian C52', 'SSEASN.C123':'SouthSouthEastAsian C123', 'SSEASN.C135':'SouthSouthEastAsian C135', 'SSEASN.C145':'SouthSouthEastAsian C145',
	'SCANDIN.C160':'Scandinavian C160',
	'OPTOM.39A':'Optometry 39A',
	'TIBETAN.C114':'Tibetan C114','TIBETAN.C154':'Tibetan C154',
	'NATRES.39E':'NaturalResources 39E',
	'NATAMST.150':'NativeAmerican 150','NATAMST.151':'NativeAmerican 151',
	'IDS.130':'InterDepartmental 130','IDS.182':'InterDepartmental 182',
	'AMERSTD.C132B':'AmericanStudies C132B',
	'PHILOS.2':'Philosophy 2', 'PHILOS.3':'Philosophy 3', 'PHILOS.4':'Philosophy 4', 'PHILOS.6':'Philosophy 6', 'PHILOS.7':'Philosophy 7', 'PHILOS.11':'Philosophy 11', 'PHILOS.12A':'Philosophy 12A', 
	'PHILOS.13':'Philosophy 13', 'PHILOS.16':'Philosophy 16', 'PHILOS.17':'Philosophy 17', 'PHILOS.21X':'Philosophy 21X', 'PHILOS.22X':'Philosophy 22X', 'PHILOS.23X':'Philosophy 23X', 'PHILOS.24':'Philosophy 24', 
	'PHILOS.24X':'Philosophy 24X', 'PHILOS.25A':'Philosophy 25A', 'PHILOS.25B':'Philosophy 25B', 'PHILOS.39M':'Philosophy 39M', 'PHILOS.98':'Philosophy 98', 'PHILOS.100':'Philosophy 100', 'PHILOS.104':'Philosophy 104', 
	'PHILOS.107':'Philosophy 107', 'PHILOS.108':'Philosophy 108', 'PHILOS.109':'Philosophy 109', 'PHILOS.110':'Philosophy 110', 'PHILOS.112':'Philosophy 112', 'PHILOS.C112':'Philosophy C112', 'PHILOS.114':'Philosophy 114',
	'PHILOS.115':'Philosophy 115', 'PHILOS.116':'Philosophy 116', 'PHILOS.119':'Philosophy 119', 'PHILOS.122':'Philosophy 122', 'PHILOS.125':'Philosophy 125', 'PHILOS.127':'Philosophy 127', 'PHILOS.128':'Philosophy 128', 
	'PHILOS.132':'Philosophy 132', 'PHILOS.C132':'Philosophy C132', 'PHILOS.133':'Philosophy 133', 'PHILOS.134':'Philosophy 134', 'PHILOS.135':'Philosophy 135', 'PHILOS.136':'Philosophy 136', 'PHILOS.138':'Philosophy 138',
	'PHILOS.140A':'Philosophy 140A', 'PHILOS.140B':'Philosophy 140B', 'PHILOS.141':'Philosophy 141', 'PHILOS.142':'Philosophy 142', 'PHILOS.143':'Philosophy 143', 'PHILOS.146':'Philosophy 146', 'PHILOS.149':'Philosophy 149',
	'PHILOS.155':'Philosophy 155', 'PHILOS.156A':'Philosophy 156A', 'PHILOS.160':'Philosophy 160', 'PHILOS.161':'Philosophy 161', 'PHILOS.163':'Philosophy 163', 'PHILOS.170':'Philosophy 170', 'PHILOS.172':'Philosophy 172', 
	'PHILOS.173':'Philosophy 173', 'PHILOS.176':'Philosophy 176', 'PHILOS.178':'Philosophy 178', 'PHILOS.181':'Philosophy 181', 'PHILOS.183':'Philosophy 183', 'PHILOS.184':'Philosophy 184', 'PHILOS.185':'Philosophy 185', 
	'PHILOS.186B':'Philosophy 186B', 'PHILOS.187':'Philosophy 187', 'PHILOS.188':'Philosophy 188', 'PHILOS.N188':'Philosophy N188', 'PHILOS.189':'Philosophy 189', 'PHILOS.190':'Philosophy 190', 'PHILOS.H195':'Philosophy H195', 
	'PHILOS.198':'Philosophy 198', 'PHILOS.199':'Philosophy 199',
	'SEASIAN.C145':'SothEastAsian C145'}
#http://ls-advise.berkeley.edu/requirement/breadth7/ps.html
physicalScience={
	'ANTHRO.131':'Anthro 131', 'ANTHRO.132':'Anthro 132', 'ANTHRO.133':'Anthro 133', 'ANTHRO.134':'Anthro 134', 'ANTHRO.134A':'Anthro 134A',
	'ARCH.39A':'Architecture 39A', 'ARCH.140':'Architecture 140', 'ARCH.149':'Architecture 149', 'ARCH.150':'Architecture 150', 'ARCH.152':'Architecture 152', 'ARCH.153':'Architecture 153', 'ARCH.159A':'Architecture 159A', 'ARCH.159B':'Architecture 159B', 'ARCH.159C':'Architecture 159C', 'ARCH.159D':'Architecture 159D', 'ARCH.159X':'Architecture 159X',
	'BIOENG.C125':'BioEng C125',
	'CHMENG.40':'ChemEng 40', 'CHMENG.124':'ChemEng 124', 'CHMENG.140':'ChemEng 140', 'CHMENG.141':'ChemEng 141', 'CHMENG.142':'ChemEng 142', 'CHMENG.150A':'ChemEng 150A', 'CHMENG.150B':'ChemEng 150B', 'CHMENG.152':'ChemEng 152',
	'CHMENG.154':'ChemEng 154', 'CHMENG.160':'ChemEng 160', 'CHMENG.162':'ChemEng 162', 'CHMENG.170A':'ChemEng 170A', 'CHMENG.170E':'ChemEng 170E', 'CHMENG.171':'ChemEng 171', 'CHMENG.173':'ChemEng 173', 'CHMENG.174':'ChemEng 174',
	'CHMENG.175':'ChemEng 175', 'CHMENG.176':'ChemEng 176', 'CHMENG.178':'ChemEng 178', 'CHMENG.179':'ChemEng 179', 'CHMENG.181':'ChemEng 181',
	'CIVENG.70':'CivEng 70', 'CIVENG.100':'CivEng 100', 'CIVENG.101':'CivEng 101', 'CIVENG.102':'CivEng 102', 'CIVENG.103':'CivEng 103', 'CIVENG.104':'CivEng 104', 'CIVENG.105':'CivEng 105', 'CIVENG.106':'CivEng 106', 
	'CIVENG.C106':'CivEng C106', 'CIVENG.108':'CivEng 108', 'CIVENG.109':'CivEng 109', 'CIVENG.110':'CivEng 110', 'CIVENG.111':'CivEng 111', 'CIVENG.112':'CivEng 112', 'CIVENG.113':'CivEng 113', 'CIVENG.115':'CivEng 115',
	'CIVENG.116N':'CivEng 116N', 'CIVENG.C116':'CivEng C116', 'CIVENG.117':'CivEng 117', 'CIVENG.118':'CivEng 118', 'CIVENG.119':'CivEng 119', 'CIVENG.120':'CivEng 120', 'CIVENG.120N':'CivEng 120N', 'CIVENG.121':'CivEng 121',
	'CIVENG.121N':'CivEng 121N', 'CIVENG.122':'CivEng 122', 'CIVENG.122N':'CivEng 122N', 'CIVENG.124':'CivEng 124', 'CIVENG.125':'CivEng 125', 'CIVENG.130':'CivEng 130', 'CIVENG.131':'CivEng 131', 'CIVENG.131N':'CivEng 131N',
	'CIVENG.140':'CivEng 140', 'CIVENG.144':'CivEng 144', 'CIVENG.148A':'CivEng 148A', 'CIVENG.148B':'CivEng 148B', 'CIVENG.150':'CivEng 150', 'CIVENG.153':'CivEng 153', 'CIVENG.160':'CivEng 160', 'CIVENG.166':'CivEng 166', 
	'CIVENG.168N':'CivEng 168N', 'CIVENG.170':'CivEng 170', 'CIVENG.171':'CivEng 171', 'CIVENG.172':'CivEng 172', 'CIVENG.173':'CivEng 173', 'CIVENG.175':'CivEng 175', 'CIVENG.176':'CivEng 176', 'CIVENG.177':'CivEng 177', 'CIVENG.185':'CivEng 185',
	'COMPSCI.39F':'CompSci 39F', 'COMPSCI.61C':'CompSci 61C', 'COMPSCI.61CL':'CompSci 61CL', 'COMPSCI.188':'CompSci 188',
	'COMPBIO.170B':'Biochemistry 170B',
	'ELENG.1':'EE 1', 'ELENG.20':'EE 20', 'ELENG.40':'EE 40', 'ELENG.41I':'EE 41I', 'ELENG.42':'EE 42', 'ELENG.100':'EE 100', 'ELENG.104':'EE 104', 'ELENG.110':'EE 110', 'ELENG.114':'EE 114', 'ELENG.117':'EE 117', 
	'ELENG.118':'EE 118', 'ELENG.121':'EE 121', 'ELENG.122':'EE 122', 'ELENG.123':'EE 123', 'ELENG.C125':'EE C125', 'ELENG.128':'EE 128', 'ELENG.129':'EE 129', 'ELENG.130':'EE 130', 'ELENG.131':'EE 131', 'ELENG.134':'EE 134', 
	'ELENG.135':'EE 135', 'ELENG.136':'EE 136', 'ELENG.140':'EE 140', 'ELENG.141':'EE 141', 'ELENG.142':'EE 142', 'ELENG.143':'EE 143', 'ELENG.145A':'EE 145A', 'ELENG.145B':'EE 145B', 'ELENG.145M':'EE 145M', 'ELENG.146':'EE 146',
	'ENERES.100':'ERG 100', 'ENERES.C100':'ERG C100', 'ENERES.102':'ERG 102', 'ENERES.120':'ERG 120', 'ENERES.140':'ERG 140', 'ENERES.141':'ERG 141',
	'OPTOM.39A':'Optometry 39A',
	'ENGIN.11':'E 11', 'ENGIN.36':'E 36', 'ENGIN.45':'E 45', 'ENGIN.49':'E 49', 'ENGIN.101':'E 101', 'ENGIN.102':'E 102', 'ENGIN.117':'E 117', 'ENGIN.135':'E 135', 'ENGIN.145':'E 145', 'ENGIN.C150':'E C150', 'ENGIN.153':'E 153', 
	'ENGIN.160':'E 160', 'ENGIN.161':'E 161', 'ENGIN.162':'E 162', 'ENGIN.165':'E 165', 'ENGIN.166':'E 166', 'ENGIN.172':'E 172',
	'ESPM.2':'ESPM 2', 'ESPM.4':'ESPM 4', 'ESPM.15':'ESPM 15', 'ESPM.20':'ESPM 20', 'ESPM.22':'ESPM 22', 'ESPM.C107':'ESPM C107', 'ESPM.120':'ESPM 120', 'ESPM.121':'ESPM 121', 'ESPM.124':'ESPM 124', 'ESPM.125':'ESPM 125', 
	'ESPM.126':'ESPM 126', 'ESPM.127':'ESPM 127', 'ESPM.128':'ESPM 128', 'ESPM.C128':'ESPM C128', 'ESPM.129':'ESPM 129', 'ESPM.C129':'ESPM C129', 'ESPM.130':'ESPM 130', 'ESPM.C130':'ESPM C130', 'ESPM.148':'ESPM 148', 
	'ESPM.172':'ESPM 172', 'ESPM.177':'ESPM 177', 'ESPM.179':'ESPM 179', 'ESPM.180':'ESPM 180', 'ESPM.C180':'ESPM C180', 'ESPM.181':'ESPM 181',
	'ENVSCI.10':'EnvSci 10','ENVSCI.125':'EnvSci 125',
	'GEOG.1':'Geography 1', 'GEOG.30':'Geography 30', 'GEOG.39C':'Geography 39C', 'GEOG.40':'Geography 40', 'GEOG.C82':'Geography C82', 'GEOG.C136':'Geography C136', 'GEOG.C139':'Geography C139', 'GEOG.140':'Geography 140',
	'GEOG.140A':'Geography 140A', 'GEOG.140B':'Geography 140B', 'GEOG.C141':'Geography C141', 'GEOG.142':'Geography 142', 'GEOG.143':'Geography 143', 'GEOG.144':'Geography 144', 'GEOG.146':'Geography 146', 'GEOG.147':'Geography 147',
	'GEOG.171':'Geography 171', 'GEOG.184':'Geography 184', 'GEOG.185':'Geography 185',
	'HISTORY.181B':'History 181B',
	'INDENG.39A':'IEOR 39A', 'INDENG.130':'IEOR 130', 'INDENG.131':'IEOR 131', 'INDENG.140':'IEOR 140', 'INDENG.150':'IEOR 150', 'INDENG.161':'IEOR 161', 'INDENG.162':'IEOR 162', 'INDENG.164':'IEOR 164', 'INDENG.165':'IEOR 165', 'INDENG.180':'IEOR 180',
	'INTEGBI.39D':'IB 39D', 'INTEGBI.C82':'IB C82', 'INTEGBI.106':'IB 106', 'INTEGBI.C158':'IB C158',
	'L&S.16':'L&S 16', 'L&S.70A':'L&S 70A', 'L&S.70B':'L&S 70B', 'L&S.C70T':'L&S C70T', 'L&S.C70U':'L&S C70U', 'L&S.C70V':'L&S C70V', 'L&S.C70W':'L&S C70W', 'L&S.C70X':'L&S C70X', 'L&S.C70Y':'L&S C70Y', 'L&S.117':'L&S 117', 'L&S.122':'L&S 122',
	'L&S.170AC':'L&S 170AC', 'L&S.C170AC':'L&S C170AC',
	'MATSCI.101':'MatSci 101', 'MATSCI.102':'MatSci 102', 'MATSCI.103':'MatSci 103', 'MATSCI.104':'MatSci 104', 'MATSCI.111':'MatSci 111', 'MATSCI.112':'MatSci 112', 'MATSCI.113':'MatSci 113', 'MATSCI.114':'MatSci 114', 'MATSCI.115':'MatSci 115', 
	'MATSCI.116':'MatSci 116', 'MATSCI.117':'MatSci 117', 'MATSCI.118':'MatSci 118', 'MATSCI.120':'MatSci 120', 'MATSCI.121':'MatSci 121', 'MATSCI.122':'MatSci 122', 'MATSCI.123':'MatSci 123', 'MATSCI.124':'MatSci 124', 'MATSCI.125':'MatSci 125', 
	'MATSCI.130':'MatSci 130', 'MATSCI.145':'MatSci 145', 'MATSCI.146':'MatSci 146', 'MATSCI.148':'MatSci 148', 'MATSCI.149':'MatSci 149', 'MATSCI.150':'MatSci 150', 'MATSCI.160':'MatSci 160', 'MATSCI.161':'MatSci 161', 'MATSCI.170':'MatSci 170', 
	'MATSCI.172':'MatSci 172', 'MATSCI.176':'MatSci 176', 'MATSCI.180':'MatSci 180',
	'MECENG.1':'MecEng 1', 'MECENG.39A':'MecEng 39A', 'MECENG.39C':'MecEng 39C', 'MECENG.39D':'MecEng 39D', 'MECENG.39E':'MecEng 39E', 'MECENG.101':'MecEng 101', 'MECENG.102A':'MecEng 102A', 'MECENG.104':'MecEng 104', 'MECENG.105':'MecEng 105', 
	'MECENG.106':'MecEng 106', 'MECENG.107A':'MecEng 107A', 'MECENG.107B':'MecEng 107B', 'MECENG.109':'MecEng 109', 'MECENG.110':'MecEng 110', 'MECENG.122':'MecEng 122', 'MECENG.130':'MecEng 130', 'MECENG.132':'MecEng 132', 'MECENG.133':'MecEng 133', 
	'MECENG.134':'MecEng 134', 'MECENG.135':'MecEng 135', 'MECENG.136':'MecEng 136', 'MECENG.140':'MecEng 140', 'MECENG.142':'MecEng 142', 'MECENG.145':'MecEng 145', 'MECENG.151':'MecEng 151', 'MECENG.161':'MecEng 161', 'MECENG.162':'MecEng 162', 
	'MECENG.163':'MecEng 163', 'MECENG.170':'MecEng 170', 'MECENG.173':'MecEng 173', 'MECENG.175':'MecEng 175', 'MECENG.185':'MecEng 185',
	'NUCENG.39':'NucEng 39', 'NUCENG.92':'NucEng 92', 'NUCENG.104A':'NucEng 104A', 'NUCENG.107':'NucEng 107', 'NUCENG.124':'NucEng 124', 'NUCENG.150':'NucEng 150', 'NUCENG.160':'NucEng 160', 'NUCENG.161':'NucEng 161', 'NUCENG.162':'NucEng 162', 
	'NUCENG.180':'NucEng 180',
	'IDS.80':'InterDepartmental 80',
	'PBHLTH.C171':'PublicHealth C171', 'PBHLTH.175':'PublicHealth 175', 'PBHLTH.176':'PublicHealth 176',
	'UGIS.66':'UGIS 66',
	'STAT.39B':'Stats 39B',
	'PUBPOL.C184':'PublicPolicy C184',
	'ASTRON.3':'Astronomy 3', 'ASTRON.7A':'Astronomy 7A', 'ASTRON.7B':'Astronomy 7B', 'ASTRON.10':'Astronomy 10', 'ASTRON.C10':'Astronomy C10', 'ASTRON.N10':'Astronomy N10', 'ASTRON.C12':'Astronomy C12', 'ASTRON.W12':'Astronomy W12', 'ASTRON.C13':'Astronomy C13', 
	'ASTRON.244':'Astronomy 244', 'ASTRON.39':'Astronomy 39', 'ASTRON.84':'Astronomy 84', 'ASTRON.98':'Astronomy 98', 'ASTRON.99':'Astronomy 99', 'ASTRON.120':'Astronomy 120', 'ASTRON.121':'Astronomy 121', 'ASTRON.160':'Astronomy 160', 'ASTRON.C161':'Astronomy C161',
	'ASTRON.C162':'Astronomy C162', 'ASTRON.H195':'Astronomy H195', 'ASTRON.198':'Astronomy 198', 'ASTRON.199':'Astronomy 199',
	'CHEM.1A':'Chem 1A', 'CHEM.1AL':'Chem 1AL', 'CHEM.1B':'Chem 1B', 'CHEM.W1A':'Chem W1A', 'CHEM.3A':'Chem 3A', 'CHEM.3AL':'Chem 3AL', 'CHEM.3B':'Chem 3B', 'CHEM.3BL':'Chem 3BL', 'CHEM.N3AL':'Chem N3AL', 'CHEM.4A':'Chem 4A', 'CHEM.4B':'Chem 4B', 'CHEM.15':'Chem 15',
	'CHEM.24':'Chem 24', 'CHEM.49':'Chem 49', 'CHEM.96':'Chem 96', 'CHEM.98':'Chem 98', 'CHEM.98W':'Chem 98W', 'CHEM.100':'Chem 100', 'CHEM.103':'Chem 103', 'CHEM.104A':'Chem 104A', 'CHEM.104B':'Chem 104B', 'CHEM.105':'Chem 105', 'CHEM.108':'Chem 108', 
	'CHEM.C110L':'Chem C110L', 'CHEM.112A':'Chem 112A', 'CHEM.112B':'Chem 112B', 'CHEM.113':'Chem 113', 'CHEM.114':'Chem 114', 'CHEM.115':'Chem 115', 'CHEM.120A':'Chem 120A', 'CHEM.120B':'Chem 120B', 'CHEM.122':'Chem 122', 'CHEM.125':'Chem 125', 
	'CHEM.C130':'Chem C130', 'CHEM.135':'Chem 135', 'CHEM.C138':'Chem C138', 'CHEM.143':'Chem 143', 'CHEM.146':'Chem 146', 'CHEM.149':'Chem 149', 'CHEM.C150':'Chem C150', 'CHEM.C170L':'Chem C170L', 'CHEM.C178':'Chem C178', 'CHEM.C182':'Chem C182',
	'CHEM.C191':'Chem C191', 'CHEM.192':'Chem 192', 'CHEM.H194':'Chem H194', 'CHEM.195':'Chem 195', 'CHEM.196':'Chem 196', 'CHEM.197':'Chem 197', 'CHEM.198':'Chem 198', 'CHEM.199':'Chem 199',
	'EPS.3':'EPS 3', 'EPS.8':'EPS 8', 'EPS.C12':'EPS C12', 'EPS.W12':'EPS W12', 'EPS.20':'EPS 20', 'EPS.C20':'EPS C20', 'EPS.24':'EPS 24',  'EPS.50':'EPS 50', 'EPS.51':'EPS 51', 'EPS.C51':'EPS C51', 'EPS.N51':'EPS N51', 'EPS.80':'EPS 80', 
	'EPS.C82':'EPS C82', 'EPS.N82':'EPS N82', 'EPS.84':'EPS 84', 'EPS.98':'EPS 98', 'EPS.100A':'EPS 100A', 'EPS.100B':'EPS 100B',  'EPS.101':'EPS 101', 'EPS.102':'EPS 102', 'EPS.103':'EPS 103','EPS.108':'EPS 108', 'EPS.109':'EPS 109', 
	'EPS.111':'EPS 111', 'EPS.115':'EPS 115', 'EPS.116':'EPS 116', 'EPS.117':'EPS 117', 'EPS.118':'EPS 118', 'EPS.119':'EPS 119', 'EPS.122':'EPS 122', 'EPS.124':'EPS 124', 'EPS.C129':'EPS C129', 'EPS.130':'EPS 130', 'EPS.131':'EPS 131', 
	'EPS.C146':'EPS C146', 'EPS.C162':'EPS C162', 'EPS.170AC':'EPS 170AC', 'EPS.C178':'EPS C178', 'EPS.C180':'EPS C180', 'EPS.C181':'EPS C181', 'EPS.C182':'EPS C182', 'EPS.C183':'EPS C183', 'EPS.185':'EPS 185', 'EPS.H195':'EPS H195', 
	'EPS.197':'EPS 197', 'EPS.198':'EPS 198', 'EPS.199':'EPS 199',
	'EPS.7A':'EPS 7A', 'EPS.7B':'EPS 7B', 'EPS.7C':'EPS 7C', 'EPS.H7A':'EPS H7A', 'EPS.H7B':'EPS H7B', 'EPS.H7C':'EPS H7C', 'EPS.8A':'EPS 8A', 'EPS.8B':'EPS 8B', 'EPS.C10':'EPS C10', 'EPS.C21':'EPS C21', 'EPS.24':'EPS 24', 'EPS.49':'EPS 49',
	'EPS.98':'EPS 98', 'EPS.99':'EPS 99', 'EPS.100':'EPS 100', 'EPS.105':'EPS 105', 'EPS.110A':'EPS 110A', 'EPS.110B':'EPS 110B', 'EPS.111':'EPS 111', 'EPS.112':'EPS 112', 'EPS.129':'EPS 129', 'EPS.130':'EPS 130', 'EPS.132':'EPS 132', 'EPS.137A':'EPS 137A',
	'EPS.137B':'EPS 137B', 'EPS.138':'EPS 138', 'EPS.139':'EPS 139', 'EPS.141A':'EPS 141A', 'EPS.141B':'EPS 141B', 'EPS.142':'EPS 142', 'EPS.151':'EPS 151', 'EPS.C161':'EPS C161', 'EPS.177':'EPS 177', 'EPS.H190':'EPS H190', 'EPS.C191':'EPS C191', 
	'EPS.H195A':'EPS H195A', 'EPS.H195B':'EPS H195B', 'EPS.198':'EPS 198', 'EPS.199':'EPS 199',}


#http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html
socialBehavioralScience={
	'AFRICAM.4A':'AfricanAmerican 4A', 'AFRICAM.4B':'AfricanAmerican 4B', 'AFRICAM.5A':'AfricanAmerican 5A', 'AFRICAM.5B':'AfricanAmerican 5B', 'AFRICAM.C15':'AfricanAmerican C15', 'AFRICAM.20':'AfricanAmerican 20', 'AFRICAM.25AC':'AfricanAmerican 25AC', 'AFRICAM.26':'AfricanAmerican 26', 'AFRICAM.27AC':'AfricanAmerican 27AC', 'AFRICAM.28AC':'AfricanAmerican 28AC', 'AFRICAM.39A':'AfricanAmerican 39A', 'AFRICAM.39C':'AfricanAmerican 39C', 'AFRICAM.39D':'AfricanAmerican 39D', 'AFRICAM.39E':'AfricanAmerican 39E', 'AFRICAM.39G':'AfricanAmerican 39G', 'AFRICAM.100':'AfricanAmerican 100', 'AFRICAM.101':'AfricanAmerican 101', 'AFRICAM.107':'AfricanAmerican 107', 'AFRICAM.109':'AfricanAmerican 109', 'AFRICAM.111':'AfricanAmerican 111', 'AFRICAM.112A':'AfricanAmerican 112A', 'AFRICAM.112B':'AfricanAmerican 112B', 'AFRICAM.113':'AfricanAmerican 113', 'AFRICAM.114':'AfricanAmerican 114', 'AFRICAM.116':'AfricanAmerican 116', 'AFRICAM.117':'AfricanAmerican 117', 'AFRICAM.121':'AfricanAmerican 121', 'AFRICAM.122':'AfricanAmerican 122', 'AFRICAM.C124':'AfricanAmerican C124', 'AFRICAM.126':'AfricanAmerican 126', 'AFRICAM.128':'AfricanAmerican 128', 'AFRICAM.131':'AfricanAmerican 131', 'AFRICAM.C131':'AfricanAmerican C131', 'AFRICAM.N131':'AfricanAmerican N131', 'AFRICAM.132':'AfricanAmerican 132', 'AFRICAM.C133A':'AfricanAmerican C133A', 'AFRICAM.C134':'AfricanAmerican C134', 'AFRICAM.135':'AfricanAmerican 135', 'AFRICAM.136AC':'AfricanAmerican 136AC', 'AFRICAM.137':'AfricanAmerican 137', 'AFRICAM.138':'AfricanAmerican 138', 'AFRICAM.144':'AfricanAmerican 144', 'AFRICAM.152F':'AfricanAmerican 152F', 'AFRICAM.C170':'AfricanAmerican C170', 'AFRICAM.C178':'AfricanAmerican C178',
	'AFRKANS.150':'Afrikaans 150',
	'AMERST.10':'AmericanStudies 10', 'AMERST.10AC':'AmericanStudies 10AC', 'AMERST.39':'AmericanStudies 39', 'AMERST.39A':'AmericanStudies 39A', 'AMERST.39B':'AmericanStudies 39B', 'AMERST.101':'AmericanStudies 101', 'AMERST.101AC':'AmericanStudies 101AC', 'AMERST.102':'AmericanStudies 102', 'AMERST.C111A':'AmericanStudies C111A', 'AMERST.C112A':'AmericanStudies C112A', 'AMERST.C112B':'AmericanStudies C112B', 'AMERST.C112F':'AmericanStudies C112F', 'AMERST.118AC':'AmericanStudies 118AC', 'AMERST.C125':'AmericanStudies C125', 'AMERST.C132':'AmericanStudies C132', 'AMERST.C132B':'AmericanStudies C132B', 'AMERST.C134':'AmericanStudies C134', 'AMERST.163':'AmericanStudies 163', 'AMERST.165':'AmericanStudies 165', 'AMERST.166':'AmericanStudies 166', 'AMERST.167':'AmericanStudies 167', 'AMERST.C171':'AmericanStudies C171', 'AMERST.C172':'AmericanStudies C172', 'AMERST.C177':'AmericanStudies C177', 'AMERST.179AC':'AmericanStudies 179AC',
	'ANTHRO.1':'Anthro 1', 'ANTHRO.2':'Anthro 2', 'ANTHRO.2AC':'Anthro 2AC', 'ANTHRO.3':'Anthro 3', 'ANTHRO.3AC':'Anthro 3AC', 'ANTHRO.10AC':'Anthro 10AC', 'ANTHRO.11AC':'Anthro 11AC', 'ANTHRO.12AC':'Anthro 12AC', 'ANTHRO.15':'Anthro 15', 'ANTHRO.16':'Anthro 16', 'ANTHRO.17':'Anthro 17', 'ANTHRO.18':'Anthro 18', 'ANTHRO.39B':'Anthro 39B', 'ANTHRO.72':'Anthro 72', 'ANTHRO.73':'Anthro 73', 'ANTHRO.74':'Anthro 74', 'ANTHRO.94':'Anthro 94', 'ANTHRO.106':'Anthro 106', 'ANTHRO.109':'Anthro 109', 'ANTHRO.111':'Anthro 111', 'ANTHRO.114':'Anthro 114', 'ANTHRO.115':'Anthro 115', 'ANTHRO.116':'Anthro 116', 'ANTHRO.117':'Anthro 117', 'ANTHRO.119':'Anthro 119', 'ANTHRO.121A':'Anthro 121A', 'ANTHRO.121AC':'Anthro 121AC', 'ANTHRO.121B':'Anthro 121B', 'ANTHRO.122A':'Anthro 122A', 'ANTHRO.122B':'Anthro 122B', 'ANTHRO.122C':'Anthro 122C', 'ANTHRO.122D':'Anthro 122D', 'ANTHRO.122E':'Anthro 122E', 'ANTHRO.122F':'Anthro 122F', 'ANTHRO.123A':'Anthro 123A', 'ANTHRO.123B':'Anthro 123B', 'ANTHRO.123C':'Anthro 123C', 'ANTHRO.123D':'Anthro 123D', 'ANTHRO.123E':'Anthro 123E', 'ANTHRO.124A':'Anthro 124A', 'ANTHRO.124AC':'Anthro 124AC', 'ANTHRO.C125A':'Anthro C125A', 'ANTHRO.C125B':'Anthro C125B', 'ANTHRO.128':'Anthro 128', 'ANTHRO.129A':'Anthro 129A', 'ANTHRO.129C':'Anthro 129C', 'ANTHRO.129D':'Anthro 129D', 'ANTHRO.129E':'Anthro 129E', 'ANTHRO.C129F':'Anthro C129F', 'ANTHRO.130':'Anthro 130', 'ANTHRO.132':'Anthro 132', 'ANTHRO.133':'Anthro 133', 'ANTHRO.134':'Anthro 134', 'ANTHRO.134A':'Anthro 134A', 'ANTHRO.C136K':'Anthro C136K', 'ANTHRO.137':'Anthro 137', 'ANTHRO.138A':'Anthro 138A', 'ANTHRO.138B':'Anthro 138B', 'ANTHRO.139':'Anthro 139', 'ANTHRO.140':'Anthro 140', 'ANTHRO.141':'Anthro 141', 'ANTHRO.142':'Anthro 142', 'ANTHRO.143':'Anthro 143', 'ANTHRO.144':'Anthro 144', 'ANTHRO.145':'Anthro 145', 'ANTHRO.146':'Anthro 146', 'ANTHRO.C146':'Anthro C146', 'ANTHRO.147A':'Anthro 147A', 'ANTHRO.147C':'Anthro 147C', 'ANTHRO.C147B':'Anthro C147B', 'ANTHRO.148':'Anthro 148', 'ANTHRO.149':'Anthro 149', 'ANTHRO.150':'Anthro 150', 'ANTHRO.151':'Anthro 151', 'ANTHRO.152':'Anthro 152', 'ANTHRO.153':'Anthro 153', 'ANTHRO.154':'Anthro 154', 'ANTHRO.156A':'Anthro 156A', 'ANTHRO.156B':'Anthro 156B', 'ANTHRO.156C':'Anthro 156C', 'ANTHRO.157':'Anthro 157', 'ANTHRO.158':'Anthro 158', 'ANTHRO.159':'Anthro 159', 'ANTHRO.160AC':'Anthro 160AC', 'ANTHRO.161':'Anthro 161', 'ANTHRO.162':'Anthro 162', 'ANTHRO.162AC':'Anthro 162AC', 'ANTHRO.163AC':'Anthro 163AC', 'ANTHRO.164':'Anthro 164', 'ANTHRO.166':'Anthro 166', 'ANTHRO.169B':'Anthro 169B', 'ANTHRO.170':'Anthro 170', 'ANTHRO.171':'Anthro 171', 'ANTHRO.172AC':'Anthro 172AC', 'ANTHRO.173':'Anthro 173', 'ANTHRO.174AC':'Anthro 174AC', 'ANTHRO.175':'Anthro 175', 'ANTHRO.176':'Anthro 176', 'ANTHRO.177':'Anthro 177', 'ANTHRO.178':'Anthro 178', 'ANTHRO.179':'Anthro 179', 'ANTHRO.180':'Anthro 180', 'ANTHRO.181':'Anthro 181', 'ANTHRO.182':'Anthro 182', 'ANTHRO.183':'Anthro 183', 'ANTHRO.184':'Anthro 184', 'ANTHRO.185':'Anthro 185', 'ANTHRO.C186':'Anthro C186', 'ANTHRO.187':'Anthro 187', 'ANTHRO.188':'Anthro 188', 'ANTHRO.189':'Anthro 189',
	'ARCH.39B':'Architecture 39B', 'ARCH.39D':'Architecture 39D', 'ARCH.100A':'Architecture 100A', 'ARCH.100B':'Architecture 100B', 'ARCH.101':'Architecture 101', 'ARCH.105':'Architecture 105', 'ARCH.110AC':'Architecture 110AC', 'ARCH.118AC':'Architecture 118AC', 'ARCH.C119':'Architecture C119', 'ARCH.120':'Architecture 120', 'ARCH.122':'Architecture 122', 'ARCH.130':'Architecture 130', 'ARCH.136':'Architecture 136', 'ARCH.159E':'Architecture 159E', 'ARCH.175':'Architecture 175', 'ARCH.176':'Architecture 176', 'ARCH.179AC':'Architecture 179AC',
	'HISTART.108':'HistoryOfArt 108','HISTART.C189':'HistoryOfArt C189',
	'ART.C178':'Art C178','ART.C179':'Art C179',
	'ASAMST.20A':'AsianAmerican 20A', 'ASAMST.20B':'AsianAmerican 20B', 'ASAMST.20C':'AsianAmerican 20C', 'ASAMST.120':'AsianAmerican 120', 'ASAMST.121':'AsianAmerican 121', 'ASAMST.122':'AsianAmerican 122', 'ASAMST.123':'AsianAmerican 123', 'ASAMST.124':'AsianAmerican 124', 'ASAMST.125':'AsianAmerican 125', 'ASAMST.126':'AsianAmerican 126', 'ASAMST.127':'AsianAmerican 127', 'ASAMST.128AC':'AsianAmerican 128AC', 'ASAMST.129':'AsianAmerican 129', 'ASAMST.130':'AsianAmerican 130', 'ASAMST.131':'AsianAmerican 131', 'ASAMST.132':'AsianAmerican 132', 'ASAMST.141':'AsianAmerican 141', 'ASAMST.142':'AsianAmerican 142', 'ASAMST.143':'AsianAmerican 143', 'ASAMST.144':'AsianAmerican 144', 'ASAMST.145':'AsianAmerican 145', 'ASAMST.146':'AsianAmerican 146', 'ASAMST.149':'AsianAmerican 149', 'ASAMST.150':'AsianAmerican 150', 'ASAMST.151':'AsianAmerican 151', 'ASAMST.165':'AsianAmerican 165', 'ASAMST.166':'AsianAmerican 166', 'ASAMST.170':'AsianAmerican 170', 'ASAMST.171':'AsianAmerican 171', 'ASAMST.175':'AsianAmerican 175', 'ASAMST.178':'AsianAmerican 178', 'ASAMST.190':'AsianAmerican 190',
	'ASIANST.10':'AsianStudies 10', 'ASIANST.147':'AsianStudies 147', 'ASIANST.148':'AsianStudies 148', 'ASIANST.149':'AsianStudies 149', 'ASIANST.150':'AsianStudies 150',
	'BUDDST.39':'Buddhist 39', 'BUDDST.C126':'Buddhist C126', 'BUDDST.183':'Buddhist 183',
	'UGBA.10':'UGBA 10', 'UGBA.39AC':'UGBA 39AC', 'UGBA.101A':'UGBA 101A', 'UGBA.101B':'UGBA 101B', 'UGBA.107':'UGBA 107', 'UGBA.112':'UGBA 112', 'UGBA.118':'UGBA 118', 'UGBA.152':'UGBA 152', 'UGBA.153':'UGBA 153', 'UGBA.154':'UGBA 154', 'UGBA.156AC':'UGBA 156AC', 'UGBA.160':'UGBA 160', 'UGBA.C172':'UGBA C172', 'UGBA.178':'UGBA 178', 'UGBA.184':'UGBA 184',
	'CELTIC.70':'Celtic 70', 'CELTIC.128':'Celtic 128', 'CELTIC.161':'Celtic 161',
	'CHICANO.20':'Chicano 20', 'CHICANO.50':'Chicano 50', 'CHICANO.70':'Chicano 70', 'CHICANO.80':'Chicano 80', 'CHICANO.101':'Chicano 101', 'CHICANO.102':'Chicano 102', 'CHICANO.110':'Chicano 110', 'CHICANO.133':'Chicano 133', 'CHICANO.135':'Chicano 135', 'CHICANO.135A':'Chicano 135A', 'CHICANO.135B':'Chicano 135B', 'CHICANO.135C':'Chicano 135C', 'CHICANO.145':'Chicano 145', 'CHICANO.150A':'Chicano 150A', 'CHICANO.150B':'Chicano 150B', 'CHICANO.155':'Chicano 155', 'CHICANO.159':'Chicano 159', 'CHICANO.161':'Chicano 161', 'CHICANO.163':'Chicano 163', 'CHICANO.170':'Chicano 170', 'CHICANO.172':'Chicano 172', 'CHICANO.174':'Chicano 174', 'CHICANO.176':'Chicano 176', 'CHICANO.179':'Chicano 179', 'CHICANO.180':'Chicano 180', 'CHICANO.190':'Chicano 190',
	'CHINESE.102':'Chinese 102', 'CHINESE.159':'Chinese 159', 'CHINESE.161':'Chinese 161', 'CHINESE.163':'Chinese 163', 'CHINESE.165':'Chinese 165', 'CHINESE.169':'Chinese 169', 'CHINESE.181':'Chinese 181',
	'CYPLAN.39A':'CityPlanning 39A', 'CYPLAN.39B':'CityPlanning 39B', 'CYPLAN.39C':'CityPlanning 39C', 'CYPLAN.110':'CityPlanning 110', 'CYPLAN.111':'CityPlanning 111', 'CYPLAN.112A':'CityPlanning 112A', 'CYPLAN.112B':'CityPlanning 112B', 'CYPLAN.113A':'CityPlanning 113A', 'CYPLAN.113B':'CityPlanning 113B', 'CYPLAN.114':'CityPlanning 114', 'CYPLAN.115':'CityPlanning 115', 'CYPLAN.116':'CityPlanning 116', 'CYPLAN.117':'CityPlanning 117', 'CYPLAN.118AC':'CityPlanning 118AC', 'CYPLAN.119':'CityPlanning 119',
	'CIVENG.151':'CivEng 151', 'CIVENG.167':'CivEng 167',
	'CLASSIC.39C':'Classics 39C', 'CLASSIC.39F':'Classics 39F', 'CLASSIC.R44':'Classics R44', 'CLASSIC.121':'Classics 121', 'CLASSIC.178':'Classics 178', 'CLASSIC.180':'Classics 180',
	'COGSCI.1':'CogSci 1', 'COGSCI.C1':'CogSci C1', 'COGSCI.100':'CogSci 100', 'COGSCI.C101':'CogSci C101', 'COGSCI.C102':'CogSci C102', 'COGSCI.C103':'CogSci C103', 'COGSCI.C104':'CogSci C104', 'COGSCI.C107':'CogSci C107', 'COGSCI.C110':'CogSci C110', 'COGSCI.C142':'CogSci C142', 'COGSCI.C147':'CogSci C147',
	'COLWRIT.25AC':'CollegeWriting 25AC', 'COLWRIT.50AC':'CollegeWriting 50AC', 'COLWRIT.C115':'CollegeWriting C115', 'COLWRIT.150AC':'CollegeWriting 150AC',
	'COMLIT.20':'CompLit 20', 'COMLIT.40':'CompLit 40', 'COMLIT.N40':'CompLit N40',
	'COMPSCI.39M':'CompSci 39M', 'COMPSCI.C182':'CompSci C182',
	'DEMOG.100':'Demography 100', 'DEMOG.110':'Demography 110', 'DEMOG.C126':'Demography C126', 'DEMOG.135':'Demography 135', 'DEMOG.140':'Demography 140', 'DEMOG.145AC':'Demography 145AC', 'DEMOG.164':'Demography 164', 'DEMOG.C165':'Demography C165', 'DEMOG.C175':'Demography C175',
	'DUTCH.39A':'Dutch 39A', 'DUTCH.C170':'Dutch C170', 'DUTCH.173':'Dutch 173', 'DUTCH.174':'Dutch 174', 'DUTCH.175':'Dutch 175', 'DUTCH.C178':'Dutch C178', 'DUTCH.179':'Dutch 179',
	'EALANG.39A':'EastAsianLanguages 39A', 'EALANG.103':'EastAsianLanguages 103', 'EALANG.109':'EastAsianLanguages 109', 'EALANG.C126':'EastAsianLanguages C126',
	'EPS.170AC':'EPS 170AC',
	'EDUC.C1':'Educ C1', 'EDUC.39A':'Educ 39A', 'EDUC.39B':'Educ 39B', 'EDUC.39C':'Educ 39C', 'EDUC.39D':'Educ 39D', 'EDUC.40AC':'Educ 40AC', 'EDUC.50':'Educ 50', 'EDUC.75':'Educ 75', 'EDUC.100':'Educ 100', 'EDUC.103':'Educ 103', 'EDUC.112':'Educ 112', 'EDUC.113':'Educ 113', 'EDUC.114A':'Educ 114A', 'EDUC.114B':'Educ 114B', 'EDUC.114C':'Educ 114C', 'EDUC.122':'Educ 122', 'EDUC.124':'Educ 124', 'EDUC.140AC':'Educ 140AC', 'EDUC.N140':'Educ N140', 'EDUC.141':'Educ 141', 'EDUC.142':'Educ 142', 'EDUC.144':'Educ 144', 'EDUC.C144':'Educ C144', 'EDUC.145':'Educ 145', 'EDUC.C147':'Educ C147', 'EDUC.156':'Educ 156', 'EDUC.169':'Educ 169', 'EDUC.170':'Educ 170', 'EDUC.180':'Educ 180', 'EDUC.181':'Educ 181', 'EDUC.182':'Educ 182', 'EDUC.182AC':'Educ 182AC', 'EDUC.183':'Educ 183', 'EDUC.184':'Educ 184', 'EDUC.185':'Educ 185', 'EDUC.186AC':'Educ 186AC', 'EDUC.187':'Educ 187', 'EDUC.188':'Educ 188', 'EDUC.189':'Educ 189', 'EDUC.190':'Educ 190',
	'ENERES.100':'ERG 100', 'ENERES.C100':'ERG C100', 'ENERES.102':'ERG 102', 'ENERES.121':'ERG 121', 'ENERES.141':'ERG 141', 'ENERES.151':'ERG 151', 'ENERES.162':'ERG 162', 'ENERES.190':'ERG 190',
	'ENGIN.39D':'E 39D', 'ENGIN.49':'E 49', 'ENGIN.120':'E 120', 'ENGIN.125':'E 125', 'ENGIN.130AC':'E 130AC',
	'ENGLISH.25':'English 25', 'ENGLISH.C77':'English C77', 'ENGLISH.101':'English 101', 'ENGLISH.102':'English 102', 'ENGLISH.175':'English 175',
	'ENVDES.1':'EnvDesign 1', 'ENVDES.4':'EnvDesign 4', 'ENVDES.4A':'EnvDesign 4A', 'ENVDES.4B':'EnvDesign 4B', 'ENVDES.10':'EnvDesign 10', 'ENVDES.71':'EnvDesign 71', 'ENVDES.100':'EnvDesign 100', 'ENVDES.169A':'EnvDesign 169A', 'ENVDES.169B':'EnvDesign 169B', 'ENVDES.C169A':'EnvDesign C169A', 'ENVDES.C169B':'EnvDesign C169B',
	'ESPM.C10':'ESPM C10', 'ESPM.C11':'ESPM C11', 'ESPM.C12':'ESPM C12', 'ESPM.50AC':'ESPM 50AC', 'ESPM.60':'ESPM 60', 'ESPM.100':'ESPM 100', 'ESPM.101E':'ESPM 101E', 'ESPM.102A':'ESPM 102A', 'ESPM.102B':'ESPM 102B', 'ESPM.102C':'ESPM 102C', 'ESPM.102D':'ESPM 102D', 'ESPM.C103':'ESPM C103', 'ESPM.136':'ESPM 136', 'ESPM.151':'ESPM 151', 'ESPM.153':'ESPM 153', 'ESPM.154':'ESPM 154', 'ESPM.155':'ESPM 155', 'ESPM.156':'ESPM 156', 'ESPM.157':'ESPM 157', 'ESPM.C159':'ESPM C159', 'ESPM.160AC':'ESPM 160AC', 'ESPM.C160':'ESPM C160', 'ESPM.161':'ESPM 161', 'ESPM.162':'ESPM 162', 'ESPM.163AC':'ESPM 163AC', 'ESPM.164':'ESPM 164', 'ESPM.165':'ESPM 165', 'ESPM.166':'ESPM 166', 'ESPM.167':'ESPM 167', 'ESPM.168':'ESPM 168', 'ESPM.169':'ESPM 169', 'ESPM.182':'ESPM 182', 'ESPM.183':'ESPM 183', 'ESPM.C183':'ESPM C183', 'ESPM.185':'ESPM 185', 'ESPM.188':'ESPM 188', 'ESPM.C191':'ESPM C191',
	'ENVSCI.10':'EnvSci 10','ENVSCI.C12':'EnvSci C12',
	'ETHSTD.10A':'Ethnic 10A', 'ETHSTD.10AC':'Ethnic 10AC', 'ETHSTD.10B':'Ethnic 10B', 'ETHSTD.11AC':'Ethnic 11AC', 'ETHSTD.20AC':'Ethnic 20AC', 'ETHSTD.21AC':'Ethnic 21AC', 'ETHSTD.30':'Ethnic 30', 'ETHSTD.39A':'Ethnic 39A', 'ETHSTD.41AC':'Ethnic 41AC', 'ETHSTD.C73AC':'Ethnic C73AC', 'ETHSTD.100':'Ethnic 100', 'ETHSTD.101A':'Ethnic 101A', 'ETHSTD.101B':'Ethnic 101B', 'ETHSTD.103A':'Ethnic 103A', 'ETHSTD.103B':'Ethnic 103B', 'ETHSTD.103C':'Ethnic 103C', 'ETHSTD.103D':'Ethnic 103D', 'ETHSTD.103E':'Ethnic 103E', 'ETHSTD.122AC':'Ethnic 122AC', 'ETHSTD.123':'Ethnic 123', 'ETHSTD.124':'Ethnic 124', 'ETHSTD.125AC':'Ethnic 125AC', 'ETHSTD.C126':'Ethnic C126', 'ETHSTD.128':'Ethnic 128', 'ETHSTD.130AC':'Ethnic 130AC', 'ETHSTD.131':'Ethnic 131', 'ETHSTD.132':'Ethnic 132', 'ETHSTD.133AC':'Ethnic 133AC', 'ETHSTD.135':'Ethnic 135', 'ETHSTD.136':'Ethnic 136', 'ETHSTD.141':'Ethnic 141', 'ETHSTD.142':'Ethnic 142', 'ETHSTD.143':'Ethnic 143', 'ETHSTD.144AC':'Ethnic 144AC', 'ETHSTD.145':'Ethnic 145', 'ETHSTD.146':'Ethnic 146', 'ETHSTD.147':'Ethnic 147', 'ETHSTD.148':'Ethnic 148', 'ETHSTD.149':'Ethnic 149', 'ETHSTD.150':'Ethnic 150', 'ETHSTD.150AC':'Ethnic 150AC', 'ETHSTD.159AC':'Ethnic 159AC', 'ETHSTD.C170':'Ethnic C170', 'ETHSTD.C173':'Ethnic C173',
	'FILM.39A':'Film 39A', 'FILM.135AC':'Film 135AC', 'FILM.C181':'Film C181',
	'FRENCH.35':'French 35', 'FRENCH.43':'French 43', 'FRENCH.43A':'French 43A', 'FRENCH.43B':'French 43B', 'FRENCH.138':'French 138', 'FRENCH.145':'French 145', 'FRENCH.146A':'French 146A', 'FRENCH.146B':'French 146B', 'FRENCH.147':'French 147', 'FRENCH.148':'French 148', 'FRENCH.160A':'French 160A', 'FRENCH.160B':'French 160B', 'FRENCH.161A':'French 161A', 'FRENCH.161B':'French 161B', 'FRENCH.162A':'French 162A', 'FRENCH.162B':'French 162B', 'FRENCH.171A':'French 171A', 'FRENCH.171B':'French 171B', 'FRENCH.172A':'French 172A', 'FRENCH.172B':'French 172B', 'FRENCH.173':'French 173', 'FRENCH.180A':'French 180A', 'FRENCH.180B':'French 180B', 'FRENCH.180C':'French 180C', 'FRENCH.180D':'French 180D', 'FRENCH.183A':'French 183A', 'FRENCH.183B':'French 183B',
	'GWS.10':'GWS 10', 'GWS.12':'GWS 12', 'GWS.14':'GWS 14', 'GWS.C15':'GWS C15', 'GWS.20':'GWS 20', 'GWS.R20W':'GWS R20W', 'GWS.39E':'GWS 39E', 'GWS.40':'GWS 40', 'GWS.50AC':'GWS 50AC', 'GWS.100AC':'GWS 100AC', 'GWS.101':'GWS 101', 'GWS.102':'GWS 102', 'GWS.103':'GWS 103', 'GWS.104':'GWS 104', 'GWS.111':'GWS 111', 'GWS.112':'GWS 112', 'GWS.113':'GWS 113', 'GWS.116AC':'GWS 116AC', 'GWS.120':'GWS 120', 'GWS.122':'GWS 122', 'GWS.125':'GWS 125', 'GWS.129':'GWS 129', 'GWS.130':'GWS 130', 'GWS.131':'GWS 131', 'GWS.133AC':'GWS 133AC', 'GWS.134':'GWS 134', 'GWS.136':'GWS 136', 'GWS.139':'GWS 139', 'GWS.140':'GWS 140', 'GWS.141':'GWS 141', 'GWS.142':'GWS 142', 'GWS.143':'GWS 143', 'GWS.144':'GWS 144', 'GWS.C145':'GWS C145', 'GWS.146':'GWS 146', 'GWS.C146A':'GWS C146A', 'GWS.153A':'GWS 153A', 'GWS.155':'GWS 155',
	'GEOG.4':'Geography 4', 'GEOG.7':'Geography 7', 'GEOG.10':'Geography 10', 'GEOG.C15':'Geography C15', 'GEOG.20':'Geography 20', 'GEOG.N20':'Geography N20', 'GEOG.31':'Geography 31', 'GEOG.C32':'Geography C32', 'GEOG.35':'Geography 35', 'GEOG.39':'Geography 39', 'GEOG.39A':'Geography 39A', 'GEOG.39B':'Geography 39B', 'GEOG.39C':'Geography 39C', 'GEOG.39D':'Geography 39D', 'GEOG.50AC':'Geography 50AC', 'GEOG.55':'Geography 55', 'GEOG.70AC':'Geography 70AC', 'GEOG.90':'Geography 90', 'GEOG.100':'Geography 100', 'GEOG.101':'Geography 101', 'GEOG.103':'Geography 103', 'GEOG.104':'Geography 104', 'GEOG.106':'Geography 106', 'GEOG.108':'Geography 108', 'GEOG.109':'Geography 109', 'GEOG.110':'Geography 110', 'GEOG.111':'Geography 111', 'GEOG.112':'Geography 112', 'GEOG.113':'Geography 113', 'GEOG.115':'Geography 115', 'GEOG.116':'Geography 116', 'GEOG.120':'Geography 120', 'GEOG.121':'Geography 121', 'GEOG.130':'Geography 130', 'GEOG.131':'Geography 131', 'GEOG.132':'Geography 132', 'GEOG.133':'Geography 133', 'GEOG.134':'Geography 134', 'GEOG.136':'Geography 136', 'GEOG.137':'Geography 137', 'GEOG.138':'Geography 138', 'GEOG.150AC':'Geography 150AC', 'GEOG.151':'Geography 151', 'GEOG.C152':'Geography C152', 'GEOG.153':'Geography 153', 'GEOG.154':'Geography 154', 'GEOG.155':'Geography 155', 'GEOG.156':'Geography 156', 'GEOG.157':'Geography 157', 'GEOG.158':'Geography 158', 'GEOG.159AC':'Geography 159AC', 'GEOG.160A':'Geography 160A', 'GEOG.160B':'Geography 160B', 'GEOG.C160A':'Geography C160A', 'GEOG.C160B':'Geography C160B', 'GEOG.162':'Geography 162', 'GEOG.163':'Geography 163', 'GEOG.164':'Geography 164', 'GEOG.165':'Geography 165', 'GEOG.166':'Geography 166', 'GEOG.167':'Geography 167', 'GEOG.168':'Geography 168', 'GEOG.180':'Geography 180', 'GEOG.181':'Geography 181', 'GEOG.188X':'Geography 188X', 'GEOG.189':'Geography 189',
	'GERMAN.25':'German 25', 'GERMAN.39F':'German 39F', 'GERMAN.50':'German 50', 'GERMAN.102D':'German 102D', 'GERMAN.103':'German 103', 'GERMAN.106':'German 106', 'GERMAN.C109':'German C109', 'GERMAN.150':'German 150', 'GERMAN.C159':'German C159', 'GERMAN.160A':'German 160A', 'GERMAN.160B':'German 160B', 'GERMAN.160C':'German 160C', 'GERMAN.160D':'German 160D', 'GERMAN.160K':'German 160K', 'GERMAN.164':'German 164', 'GERMAN.171':'German 171', 'GERMAN.172':'German 172', 'GERMAN.173':'German 173', 'GERMAN.174':'German 174', 'GERMAN.177':'German 177', 'GERMAN.178':'German 178', 'GERMAN.180B':'German 180B',
	'GPP.105':'GPP 105','GPP.115':'GPP 115',
	'HMEDSCI.C133':'HealthMedical C133',
	'HEBREW.105A':'Hebrew 105A', 'HEBREW.105B':'Hebrew 105B',
	'INDENG.39':'IEOR 39', 'INDENG.39A':'IEOR 39A', 'INDENG.166':'IEOR 166', 'INDENG.170':'IEOR 170', 'INDENG.171':'IEOR 171', 'INDENG.172':'IEOR 172',
	'INFO.39':'Info 39', 'INFO.39A':'Info 39A', 'INFO.W10':'Info W10', 'INFO.101':'Info 101', 'INFO.C103':'Info C103', 'INFO.142AC':'Info 142AC', 'INFO.146':'Info 146', 'INFO.182AC':'Info 182AC', 'INFO.C184':'Info C184',
	'INTEGBI.35AC':'IB 35AC', 'INTEGBI.39B':'IB 39B', 'INTEGBI.C156':'IB C156',
	'IDS.1':'InterDepartmental 1', 'IDS.100AC':'InterDepartmental 100AC', 'IDS.114A':'InterDepartmental 114A', 'IDS.114B':'InterDepartmental 114B', 'IDS.130':'InterDepartmental 130', 'IDS.156AC':'InterDepartmental 156AC', 'IDS.170':'InterDepartmental 170', 'IDS.180':'InterDepartmental 180', 'IDS.182':'InterDepartmental 182',
	'ISF.60':'ISF 60', 'ISF.62':'ISF 62', 'ISF.100A':'ISF 100A', 'ISF.100B':'ISF 100B', 'ISF.100D':'ISF 100D', 'ISF.100E':'ISF 100E', 'ISF.100F':'ISF 100F', 'ISF.100H':'ISF 100H', 'ISF.108':'ISF 108', 'ISF.115':'ISF 115', 'ISF.116':'ISF 116', 'ISF.117':'ISF 117', 'ISF.118AC':'ISF 118AC', 'ISF.C125':'ISF C125', 'ISF.145':'ISF 145', 'ISF.C145':'ISF C145', 'ISF.C160':'ISF C160',
	'IAS.20':'IAS 20', 'IAS.45':'IAS 45', 'IAS.102':'IAS 102', 'IAS.105':'IAS 105', 'IAS.105A':'IAS 105A', 'IAS.105B':'IAS 105B', 'IAS.106':'IAS 106', 'IAS.107':'IAS 107', 'IAS.113':'IAS 113', 'IAS.115':'IAS 115', 'IAS.143':'IAS 143', 'IAS.145':'IAS 145', 'IAS.C145':'IAS C145', 'IAS.148':'IAS 148', 'IAS.150':'IAS 150', 'IAS.155AC':'IAS 155AC', 'IAS.160':'IAS 160', 'IAS.175':'IAS 175', 'IAS.180':'IAS 180',
	'ITALIAN.39F':'Italian 39F', 'ITALIAN.40':'Italian 40', 'ITALIAN.80':'Italian 80', 'ITALIAN.103':'Italian 103', 'ITALIAN.160':'Italian 160', 'ITALIAN.N160':'Italian N160',
	'JAPAN.39B':'Japanese 39B', 'JAPAN.39C':'Japanese 39C', 'JAPAN.80':'Japanese 80', 'JAPAN.102':'Japanese 102', 'JAPAN.104':'Japanese 104', 'JAPAN.160':'Japanese 160', 'JAPAN.161':'Japanese 161', 'JAPAN.162':'Japanese 162',
	'JEWISH.39B':'Jewish 39B', 'JEWISH.39C':'Jewish 39C', 'JEWISH.39E':'Jewish 39E', 'JEWISH.39G':'Jewish 39G', 'JEWISH.101':'Jewish 101',
	'JOURN.39A':'Journalism 39A', 'JOURN.39AC':'Journalism 39AC', 'JOURN.39C':'Journalism 39C', 'JOURN.39D':'Journalism 39D', 'JOURN.100':'Journalism 100', 'JOURN.101':'Journalism 101', 'JOURN.102AC':'Journalism 102AC', 'JOURN.C103':'Journalism C103', 'JOURN.C141':'Journalism C141', 'JOURN.158':'Journalism 158', 'JOURN.163':'Journalism 163', 'JOURN.165':'Journalism 165', 'JOURN.C177':'Journalism C177', 'JOURN.180':'Journalism 180', 'JOURN.C183':'Journalism C183',
	'KOREAN.102':'Korean 102', 'KOREAN.160':'Korean 160',
	'LDARCH.12':'LandscaapeArchitecture 12', 'LDARCH.110':'LandscaapeArchitecture 110', 'LDARCH.130':'LandscaapeArchitecture 130', 'LDARCH.138AC':'LandscaapeArchitecture 138AC', 'LDARCH.141':'LandscaapeArchitecture 141', 'LDARCH.170':'LandscaapeArchitecture 170', 'LDARCH.C171':'LandscaapeArchitecture C171',
	'LATAMST.10':'LatinAmerican 10', 'LATAMST.150':'LatinAmerican 150',
	'LGBT.20AC':'LGBT 20AC', 'LGBT.145':'LGBT 145', 'LGBT.C147B':'LGBT C147B',
	'L&S.17':'L&S 17', 'L&S.18':'L&S 18', 'L&S.20C':'L&S 20C', 'L&S.23':'L&S 23', 'L&S.C30U':'L&S C30U', 'L&S.C30V':'L&S C30V', 'L&S.C30W':'L&S C30W', 'L&S.40AC':'L&S 40AC', 'L&S.40B':'L&S 40B', 'L&S.70B':'L&S 70B', 'L&S.80A':'L&S 80A', 'L&S.C103':'L&S C103', 'L&S.116':'L&S 116', 'L&S.119AC':'L&S 119AC', 'L&S.120':'L&S 120', 'L&S.120C':'L&S 120C', 'L&S.126':'L&S 126', 'L&S.127':'L&S 127', 'L&S.140D':'L&S 140D', 'L&S.C140U':'L&S C140U', 'L&S.C140V':'L&S C140V', 'L&S.150A':'L&S 150A', 'L&S.C150T':'L&S C150T', 'L&S.160A':'L&S 160A', 'L&S.160C':'L&S 160C', 'L&S.C160V':'L&S C160V', 'L&S.170AC':'L&S 170AC', 'L&S.C170AC':'L&S C170AC', 'L&S.180A':'L&S 180A', 'L&S.180AC':'L&S 180AC', 'L&S.180B':'L&S 180B', 'L&S.180C':'L&S 180C', 'L&S.C180T':'L&S C180T', 'L&S.C180U':'L&S C180U', 'L&S.C180V':'L&S C180V', 'L&S.C180W':'L&S C180W', 'L&S.C180X':'L&S C180X',
	'MATH.103':'Math 103',
	'MECENG.39B':'MecEng 39B',
	'MEDST.150':'Medieval 150',
	'MESTU.10':'MiddleEastern 10', 'MESTU.20':'MiddleEastern 20', 'MESTU.111':'MiddleEastern 111', 'MESTU.130':'MiddleEastern 130', 'MESTU.150':'MiddleEastern 150',
	'MILAFF.2':'MilitaryAffairs 2', 'MILAFF.3':'MilitaryAffairs 3', 'MILAFF.20':'MilitaryAffairs 20', 'MILAFF.120':'MilitaryAffairs 120', 'MILAFF.121':'MilitaryAffairs 121', 'MILAFF.123':'MilitaryAffairs 123', 'MILAFF.144':'MilitaryAffairs 144', 'MILAFF.145A':'MilitaryAffairs 145A', 'MILAFF.154':'MilitaryAffairs 154',
	'MCELLBI.41':'MCB 41', 'MCELLBI.C41X':'MCB C41X', 'MCELLBI.C61':'MCB C61',
	'MUSIC.26AC':'Music 26AC', 'MUSIC.39B':'Music 39B', 'MUSIC.109M':'Music 109M', 'MUSIC.135':'Music 135', 'MUSIC.135A':'Music 135A', 'MUSIC.136':'Music 136', 'MUSIC.137AC':'Music 137AC', 'MUSIC.177':'Music 177',
	'NATAMST.20A':'NativeAmerican 20A', 'NATAMST.50':'NativeAmerican 50', 'NATAMST.71':'NativeAmerican 71', 'NATAMST.72':'NativeAmerican 72', 'NATAMST.90':'NativeAmerican 90', 'NATAMST.100':'NativeAmerican 100', 'NATAMST.101':'NativeAmerican 101', 'NATAMST.102':'NativeAmerican 102', 'NATAMST.103':'NativeAmerican 103', 'NATAMST.104':'NativeAmerican 104', 'NATAMST.110':'NativeAmerican 110', 'NATAMST.120AC':'NativeAmerican 120AC', 'NATAMST.145':'NativeAmerican 145', 'NATAMST.149':'NativeAmerican 149', 'NATAMST.152':'NativeAmerican 152', 'NATAMST.155':'NativeAmerican 155', 'NATAMST.157':'NativeAmerican 157', 'NATAMST.158':'NativeAmerican 158', 'NATAMST.159':'NativeAmerican 159', 'NATAMST.173':'NativeAmerican 173', 'NATAMST.175':'NativeAmerican 175', 'NATAMST.176':'NativeAmerican 176', 'NATAMST.177':'NativeAmerican 177', 'NATAMST.178AC':'NativeAmerican 178AC', 'NATAMST.180':'NativeAmerican 180', 'NATAMST.190':'NativeAmerican 190',
	'NAVSCI.2':'NavalScience 2',
	'NESTUD.10':'NearEastern 10', 'NESTUD.15':'NearEastern 15', 'NESTUD.18':'NearEastern 18', 'NESTUD.20':'NearEastern 20', 'NESTUD.23':'NearEastern 23', 'NESTUD.C26':'NearEastern C26', 'NESTUD.C92':'NearEastern C92', 'NESTUD.101A':'NearEastern 101A', 'NESTUD.101B':'NearEastern 101B', 'NESTUD.102A':'NearEastern 102A', 'NESTUD.102B':'NearEastern 102B', 'NESTUD.122':'NearEastern 122', 'NESTUD.122A':'NearEastern 122A', 'NESTUD.122B':'NearEastern 122B', 'NESTUD.123':'NearEastern 123', 'NESTUD.123A':'NearEastern 123A', 'NESTUD.123B':'NearEastern 123B', 'NESTUD.124':'NearEastern 124', 'NESTUD.124A':'NearEastern 124A', 'NESTUD.124B':'NearEastern 124B', 'NESTUD.125':'NearEastern 125', 'NESTUD.126':'NearEastern 126', 'NESTUD.127':'NearEastern 127', 'NESTUD.128':'NearEastern 128', 'NESTUD.130A':'NearEastern 130A', 'NESTUD.130B':'NearEastern 130B', 'NESTUD.143A':'NearEastern 143A', 'NESTUD.143B':'NearEastern 143B', 'NESTUD.146A':'NearEastern 146A', 'NESTUD.146B':'NearEastern 146B', 'NESTUD.147':'NearEastern 147', 'NESTUD.154':'NearEastern 154', 'NESTUD.161':'NearEastern 161', 'NESTUD.165':'NearEastern 165', 'NESTUD.171':'NearEastern 171', 'NESTUD.172':'NearEastern 172', 'NESTUD.173A':'NearEastern 173A', 'NESTUD.173B':'NearEastern 173B', 'NESTUD.174':'NearEastern 174', 'NESTUD.175':'NearEastern 175',
	'NUCENG.170':'NucEng 170',
	'NUSCTX.39B':'NutriSci 39B', 'NUSCTX.39C':'NutriSci 39C', 'NUSCTX.104':'NutriSci 104', 'NUSCTX.135':'NutriSci 135', 'NUSCTX.C159':'NutriSci C159',
	'OPTOM.39B':'Optometry 39B',
	'PACS.10':'PACS 10', 'PACS.100':'PACS 100', 'PACS.125AC':'PACS 125AC', 'PACS.126':'PACS 126', 'PACS.127':'PACS 127', 'PACS.127A':'PACS 127A', 'PACS.127B':'PACS 127B', 'PACS.N127A':'PACS N127A', 'PACS.128AC':'PACS 128AC', 'PACS.149':'PACS 149', 'PACS.150':'PACS 150', 'PACS.151':'PACS 151', 'PACS.153':'PACS 153', 'PACS.154':'PACS 154', 'PACS.155':'PACS 155', 'PACS.164A':'PACS 164A', 'PACS.164B':'PACS 164B',
	'PHILOS.2':'Philosophy 2', 'PHILOS.5':'Philosophy 5', 'PHILOS.23':'Philosophy 23', 'PHILOS.113AC':'Philosophy 113AC', 'PHILOS.115':'Philosophy 115', 'PHILOS.117':'Philosophy 117',
	'PSYCH.1':'Psychology 1', 'PSYCH.W1':'Psychology W1', 'PSYCH.2':'Psychology 2', 'PSYCH.12':'Psychology 12', 'PSYCH.14':'Psychology 14', 'PSYCH.15':'Psychology 15', 'PSYCH.39':'Psychology 39', 'PSYCH.39A':'Psychology 39A', 'PSYCH.39AC':'Psychology 39AC', 'PSYCH.39B':'Psychology 39B', 'PSYCH.39C':'Psychology 39C', 'PSYCH.39D':'Psychology 39D', 'PSYCH.39F':'Psychology 39F', 'PSYCH.39G':'Psychology 39G', 'PSYCH.39H':'Psychology 39H', 'PSYCH.39J':'Psychology 39J', 'PSYCH.39K':'Psychology 39K', 'PSYCH.39M':'Psychology 39M', 'PSYCH.100A':'Psychology 100A', 'PSYCH.101':'Psychology 101', 'PSYCH.104':'Psychology 104', 'PSYCH.105':'Psychology 105', 'PSYCH.106':'Psychology 106', 'PSYCH.107':'Psychology 107', 'PSYCH.108':'Psychology 108', 'PSYCH.109':'Psychology 109', 'PSYCH.110':'Psychology 110', 'PSYCH.120A':'Psychology 120A', 'PSYCH.120B':'Psychology 120B', 'PSYCH.123':'Psychology 123', 'PSYCH.124':'Psychology 124', 'PSYCH.125':'Psychology 125', 'PSYCH.C129':'Psychology C129', 'PSYCH.130':'Psychology 130', 'PSYCH.131':'Psychology 131', 'PSYCH.132AC':'Psychology 132AC', 'PSYCH.133':'Psychology 133', 'PSYCH.135AC':'Psychology 135AC', 'PSYCH.136':'Psychology 136', 'PSYCH.138':'Psychology 138', 'PSYCH.140':'Psychology 140', 'PSYCH.141':'Psychology 141', 'PSYCH.142':'Psychology 142', 'PSYCH.143':'Psychology 143', 'PSYCH.144':'Psychology 144', 'PSYCH.146':'Psychology 146', 'PSYCH.147':'Psychology 147', 'PSYCH.148':'Psychology 148', 'PSYCH.149':'Psychology 149', 'PSYCH.150':'Psychology 150', 'PSYCH.151':'Psychology 151', 'PSYCH.152':'Psychology 152', 'PSYCH.153':'Psychology 153', 'PSYCH.154':'Psychology 154', 'PSYCH.155':'Psychology 155', 'PSYCH.158':'Psychology 158', 'PSYCH.159':'Psychology 159', 'PSYCH.160':'Psychology 160', 'PSYCH.161':'Psychology 161', 'PSYCH.162':'Psychology 162', 'PSYCH.C162':'Psychology C162', 'PSYCH.163':'Psychology 163', 'PSYCH.164':'Psychology 164', 'PSYCH.165':'Psychology 165', 'PSYCH.166':'Psychology 166', 'PSYCH.167AC':'Psychology 167AC', 'PSYCH.168':'Psychology 168', 'PSYCH.169A':'Psychology 169A', 'PSYCH.169B':'Psychology 169B', 'PSYCH.169C':'Psychology 169C', 'PSYCH.169D':'Psychology 169D', 'PSYCH.171':'Psychology 171', 'PSYCH.180':'Psychology 180', 'PSYCH.182':'Psychology 182', 'PSYCH.C191':'Psychology C191',
	'PBHLTH.14':'PublicHealth 14', 'PBHLTH.39B':'PublicHealth 39B', 'PBHLTH.39C':'PublicHealth 39C', 'PBHLTH.39D':'PublicHealth 39D', 'PBHLTH.39E':'PublicHealth 39E', 'PBHLTH.39F':'PublicHealth 39F', 'PBHLTH.39G':'PublicHealth 39G', 'PBHLTH.39H':'PublicHealth 39H', 'PBHLTH.103':'PublicHealth 103', 'PBHLTH.105':'PublicHealth 105', 'PBHLTH.106':'PublicHealth 106', 'PBHLTH.107':'PublicHealth 107', 'PBHLTH.112':'PublicHealth 112', 'PBHLTH.114':'PublicHealth 114', 'PBHLTH.116':'PublicHealth 116', 'PBHLTH.126':'PublicHealth 126', 'PBHLTH.130AC':'PublicHealth 130AC', 'PBHLTH.131AC':'PublicHealth 131AC', 'PBHLTH.143':'PublicHealth 143', 'PBHLTH.150A':'PublicHealth 150A', 'PBHLTH.150B':'PublicHealth 150B', 'PBHLTH.150C':'PublicHealth 150C', 'PBHLTH.150E':'PublicHealth 150E', 'PBHLTH.C160':'PublicHealth C160', 'PBHLTH.180':'PublicHealth 180', 'PBHLTH.181':'PublicHealth 181', 'PBHLTH.190':'PublicHealth 190',
	'PUBPOL.1':'PublicPolicy 1', 'PUBPOL.6':'PublicPolicy 6', 'PUBPOL.10':'PublicPolicy 10', 'PUBPOL.39':'PublicPolicy 39', 'PUBPOL.39A':'PublicPolicy 39A', 'PUBPOL.C71':'PublicPolicy C71', 'PUBPOL.101':'PublicPolicy 101', 'PUBPOL.C103':'PublicPolicy C103', 'PUBPOL.117AC':'PublicPolicy 117AC', 'PUBPOL.156':'PublicPolicy 156', 'PUBPOL.157':'PublicPolicy 157', 'PUBPOL.C157':'PublicPolicy C157', 'PUBPOL.159':'PublicPolicy 159', 'PUBPOL.160':'PublicPolicy 160', 'PUBPOL.161':'PublicPolicy 161', 'PUBPOL.162':'PublicPolicy 162', 'PUBPOL.163':'PublicPolicy 163', 'PUBPOL.164':'PublicPolicy 164', 'PUBPOL.165':'PublicPolicy 165', 'PUBPOL.166':'PublicPolicy 166', 'PUBPOL.167':'PublicPolicy 167', 'PUBPOL.168':'PublicPolicy 168', 'PUBPOL.170':'PublicPolicy 170', 'PUBPOL.171':'PublicPolicy 171', 'PUBPOL.173':'PublicPolicy 173', 'PUBPOL.174':'PublicPolicy 174', 'PUBPOL.175':'PublicPolicy 175', 'PUBPOL.176':'PublicPolicy 176', 'PUBPOL.177':'PublicPolicy 177', 'PUBPOL.178':'PublicPolicy 178', 'PUBPOL.179':'PublicPolicy 179', 'PUBPOL.180':'PublicPolicy 180', 'PUBPOL.181':'PublicPolicy 181', 'PUBPOL.182':'PublicPolicy 182', 'PUBPOL.183':'PublicPolicy 183', 'PUBPOL.184':'PublicPolicy 184', 'PUBPOL.C184':'PublicPolicy C184', 'PUBPOL.185':'PublicPolicy 185', 'PUBPOL.186':'PublicPolicy 186', 'PUBPOL.187':'PublicPolicy 187', 'PUBPOL.188':'PublicPolicy 188', 'PUBPOL.189':'PublicPolicy 189',
	'PORTUG.39A':'Portuguese 39A', 'PORTUG.112':'Portuguese 112', 'PORTUG.113':'Portuguese 113', 'PORTUG.136':'Portuguese 136', 'PORTUG.138':'Portuguese 138',
	'PLANTBI.10':'PMB 10','PLANTBI.C41X':'PMB C41X',
	'PHYSED.39':'PE 39','PHYSED.60':'PE 60',
	'RELIGST.C124':'ReligiousStudies C124', 'RELIGST.C134':'ReligiousStudies C134', 'RELIGST.C135':'ReligiousStudies C135', 'RELIGST.162':'ReligiousStudies 162', 'RELIGST.C162':'ReligiousStudies C162', 'RELIGST.171AC':'ReligiousStudies 171AC', 'RELIGST.172AC':'ReligiousStudies 172AC', 'RELIGST.173AC':'ReligiousStudies 173AC', 'RELIGST.C175':'ReligiousStudies C175', 'RELIGST.182':'ReligiousStudies 182', 'RELIGST.C185A':'ReligiousStudies C185A', 'RELIGST.C185B':'ReligiousStudies C185B', 'RELIGST.190':'ReligiousStudies 190',
	'RHETOR.39A':'Rhetoric 39A', 'RHETOR.39C':'Rhetoric 39C', 'RHETOR.39G':'Rhetoric 39G', 'RHETOR.42AC':'Rhetoric 42AC', 'RHETOR.109':'Rhetoric 109', 'RHETOR.116':'Rhetoric 116', 'RHETOR.120C':'Rhetoric 120C', 'RHETOR.123':'Rhetoric 123', 'RHETOR.127':'Rhetoric 127', 'RHETOR.129AC':'Rhetoric 129AC', 'RHETOR.134':'Rhetoric 134', 'RHETOR.136':'Rhetoric 136', 'RHETOR.137':'Rhetoric 137', 'RHETOR.151':'Rhetoric 151', 'RHETOR.152':'Rhetoric 152', 'RHETOR.152AC':'Rhetoric 152AC', 'RHETOR.162':'Rhetoric 162', 'RHETOR.167':'Rhetoric 167', 'RHETOR.168':'Rhetoric 168', 'RHETOR.170':'Rhetoric 170', 'RHETOR.171':'Rhetoric 171', 'RHETOR.172':'Rhetoric 172', 'RHETOR.176':'Rhetoric 176', 'RHETOR.182':'Rhetoric 182',
	'SCANDIN.39A':'Scandinavian 39A', 'SCANDIN.75':'Scandinavian 75', 'SCANDIN.118':'Scandinavian 118', 'SCANDIN.132':'Scandinavian 132', 'SCANDIN.165':'Scandinavian 165', 'SCANDIN.170':'Scandinavian 170',
	'SLAVIC.37':'Slavic 37', 'SLAVIC.R37W':'Slavic R37W', 'SLAVIC.38':'Slavic 38', 'SLAVIC.39A':'Slavic 39A', 'SLAVIC.39B':'Slavic 39B', 'SLAVIC.39F':'Slavic 39F', 'SLAVIC.39G':'Slavic 39G', 'SLAVIC.39H':'Slavic 39H', 'SLAVIC.39I':'Slavic 39I', 'SLAVIC.39M':'Slavic 39M', 'SLAVIC.50':'Slavic 50', 'SLAVIC.100':'Slavic 100', 'SLAVIC.104A':'Slavic 104A', 'SLAVIC.137':'Slavic 137', 'SLAVIC.C139':'Slavic C139', 'SLAVIC.147A':'Slavic 147A', 'SLAVIC.147B':'Slavic 147B', 'SLAVIC.149AC':'Slavic 149AC', 'SLAVIC.158':'Slavic 158', 'SLAVIC.190':'Slavic 190',
	'SSEASN.39C':'Slavic 39C', 'SSEASN.39F':'Slavic 39F', 'SSEASN.39G':'Slavic 39G', 'SSEASN.C112':'Slavic C112',
	'SPANISH.39':'Spanish 39', 'SPANISH.39A':'Spanish 39A', 'SPANISH.39B':'Spanish 39B', 'SPANISH.100':'Spanish 100', 'SPANISH.113':'Spanish 113', 'SPANISH.135AC':'Spanish 135AC', 'SPANISH.137':'Spanish 137', 'SPANISH.161':'Spanish 161', 'SPANISH.162':'Spanish 162', 'SPANISH.164':'Spanish 164', 'SPANISH.165':'Spanish 165', 'SPANISH.168':'Spanish 168', 'SPANISH.C178':'Spanish C178', 'SPANISH.179':'Spanish 179',
	'UGIS.C12':'UGIS C12', 'UGIS.C14':'UGIS C14', 'UGIS.20AC':'UGIS 20AC', 'UGIS.44A':'UGIS 44A', 'UGIS.44B':'UGIS 44B', 'UGIS.44C':'UGIS 44C', 'UGIS.55A':'UGIS 55A', 'UGIS.55B':'UGIS 55B', 'UGIS.56AC':'UGIS 56AC', 'UGIS.92':'UGIS 92', 'UGIS.110':'UGIS 110', 'UGIS.112':'UGIS 112', 'UGIS.114':'UGIS 114', 'UGIS.116':'UGIS 116', 'UGIS.118':'UGIS 118', 'UGIS.120':'UGIS 120', 'UGIS.121':'UGIS 121', 'UGIS.C130':'UGIS C130', 'UGIS.C132':'UGIS C132', 'UGIS.C133':'UGIS C133', 'UGIS.C134':'UGIS C134', 'UGIS.C136':'UGIS C136', 'UGIS.C137':'UGIS C137', 'UGIS.C145':'UGIS C145', 'UGIS.146':'UGIS 146', 'UGIS.C146A':'UGIS C146A', 'UGIS.C147B':'UGIS C147B', 'UGIS.C148':'UGIS C148', 'UGIS.C154':'UGIS C154', 'UGIS.C155':'UGIS C155', 'UGIS.161':'UGIS 161', 'UGIS.162':'UGIS 162', 'UGIS.162A':'UGIS 162A', 'UGIS.162B':'UGIS 162B', 'UGIS.162C':'UGIS 162C', 'UGIS.162D':'UGIS 162D', 'UGIS.162E':'UGIS 162E', 'UGIS.162I':'UGIS 162I', 'UGIS.162J':'UGIS 162J', 'UGIS.162K':'UGIS 162K', 'UGIS.162L':'UGIS 162L', 'UGIS.162M':'UGIS 162M', 'UGIS.162N':'UGIS 162N', 'UGIS.162O':'UGIS 162O', 'UGIS.162P':'UGIS 162P', 'UGIS.165':'UGIS 165', 'UGIS.167':'UGIS 167', 'UGIS.168':'UGIS 168', 'UGIS.169':'UGIS 169', 'UGIS.170':'UGIS 170', 'UGIS.171':'UGIS 171', 'UGIS.172':'UGIS 172', 'UGIS.173':'UGIS 173', 'UGIS.174':'UGIS 174', 'UGIS.175':'UGIS 175', 'UGIS.176A':'UGIS 176A', 'UGIS.177':'UGIS 177',
	'TIBETAN.167':'Tibetan 167',
	'STAT.39A':'Stats 39A','STAT.39C':'Stats 39C',
	'SASIAN.108':'SouthAsian 108', 'SASIAN.110A':'SouthAsian 110A', 'SASIAN.110B':'SouthAsian 110B', 'SASIAN.130':'SouthAsian 130', 'SASIAN.139':'SouthAsian 139', 'SASIAN.141':'SouthAsian 141', 'SASIAN.C141':'SouthAsian C141', 'SASIAN.144':'SouthAsian 144', 'SASIAN.145':'SouthAsian 145', 'SASIAN.146':'SouthAsian 146', 'SASIAN.148':'SouthAsian 148', 'SASIAN.151':'SouthAsian 151', 'SASIAN.152':'SouthAsian 152',
	'SEASIAN.122':'SouthEastAsian 122', 'SEASIAN.130':'SouthEastAsian 130', 'SEASIAN.137':'SouthEastAsian 137', 'SEASIAN.138':'SouthEastAsian 138',
	'DEVSTD.C10':'Devlopment C10', 'DEVSTD.24':'Devlopment 24', 'DEVSTD.C100':'Devlopment C100', 'DEVSTD.150':'Devlopment 150', 'DEVSTD.192':'Devlopment 192', 'DEVSTD.H195':'Devlopment H195', 'DEVSTD.197':'Devlopment 197', 'DEVSTD.198':'Devlopment 198', 'DEVSTD.199':'Devlopment 199',
	'ECON.1':'Econ 1', 'ECON.2':'Econ 2', 'ECON.C3':'Econ C3', 'ECON.24':'Econ 24', 'ECON.84':'Econ 84', 'ECON.98':'Econ 98', 'ECON.100A':'Econ 100A', 'ECON.100B':'Econ 100B', 'ECON.101A':'Econ 101A', 'ECON.101B':'Econ 101B', 'ECON.C102':'Econ C102', 'ECON.C103':'Econ C103', 'ECON.104':'Econ 104', 'ECON.105':'Econ 105', 'ECON.C110':'Econ C110', 'ECON.N110':'Econ N110', 'ECON.113':'Econ 113', 'ECON.N113':'Econ N113', 'ECON.115':'Econ 115', 'ECON.119':'Econ 119', 'ECON.121':'Econ 121', 'ECON.122':'Econ 122', 'ECON.123':'Econ 123', 'ECON.124':'Econ 124', 'ECON.C125':'Econ C125', 'ECON.131':'Econ 131', 'ECON.132':'Econ 132', 'ECON.134':'Econ 134', 'ECON.136':'Econ 136', 'ECON.N136':'Econ N136', 'ECON.138':'Econ 138', 'ECON.140':'Econ 140', 'ECON.141':'Econ 141', 'ECON.C142':'Econ C142', 'ECON.151':'Econ 151', 'ECON.152':'Econ 152', 'ECON.N152':'Econ N152', 'ECON.153':'Econ 153', 'ECON.154':'Econ 154', 'ECON.155':'Econ 155', 'ECON.157':'Econ 157', 'ECON.161':'Econ 161', 'ECON.162':'Econ 162', 'ECON.C171':'Econ C171', 'ECON.N171':'Econ N171', 'ECON.172':'Econ 172', 'ECON.173':'Econ 173', 'ECON.174':'Econ 174', 'ECON.C175':'Econ C175', 'ECON.N175':'Econ N175', 'ECON.C181':'Econ C181', 'ECON.N181':'Econ N181', 'ECON.182':'Econ 182', 'ECON.191':'Econ 191', 'ECON.H195A':'Econ H195A', 'ECON.H195AS':'Econ H195AS', 'ECON.H195B':'Econ H195B', 'ECON.H195BS':'Econ H195BS', 'ECON.196':'Econ 196', 'ECON.197':'Econ 197', 'ECON.198':'Econ 198', 'ECON.199':'Econ 199',
	'HISTORY.2':'History 2', 'HISTORY.3':'History 3', 'HISTORY.4A':'History 4A', 'HISTORY.4B':'History 4B', 'HISTORY.5':'History 5', 'HISTORY.W5':'History W5', 'HISTORY.6A':'History 6A', 'HISTORY.6B':'History 6B',
	'HISTORY.7A':'History 7A', 'HISTORY.7B':'History 7B', 'HISTORY.8A':'History 8A', 'HISTORY.8B':'History 8B', 'HISTORY.10':'History 10', 'HISTORY.11':'History 11', 'HISTORY.12':'History 12', 'HISTORY.14':'History 14',
	'HISTORY.24':'History 24', 'HISTORY.39C':'History 39C', 'HISTORY.39D':'History 39D', 'HISTORY.39E':'History 39E', 'HISTORY.39F':'History 39F', 'HISTORY.39G':'History 39G', 'HISTORY.39H':'History 39H',
	'HISTORY.39I':'History 39I', 'HISTORY.39J':'History 39J', 'HISTORY.39K':'History 39K', 'HISTORY.39L':'History 39L', 'HISTORY.39M':'History 39M', 'HISTORY.84':'History 84', 'HISTORY.98':'History 98', 'HISTORY.100':'History 100',
	'HISTORY.100AC':'History 100AC', 'HISTORY.100AP':'History 100AP', 'HISTORY.100B':'History 100B', 'HISTORY.100BP':'History 100BP', 'HISTORY.100D':'History 100D', 'HISTORY.100E':'History 100E', 'HISTORY.100F':'History 100F', 
	'HISTORY.100H':'History 100H', 'HISTORY.100L':'History 100L', 'HISTORY.100M':'History 100M', 'HISTORY.N100':'History N100', 'HISTORY.100S':'History 100S', 'HISTORY.100U':'History 100U', 'HISTORY.100UP':'History 100UP', 
	'HISTORY.101':'History 101', 'HISTORY.103A':'History 103A', 'HISTORY.103B':'History 103B', 'HISTORY.103C':'History 103C', 'HISTORY.103D':'History 103D', 'HISTORY.103E':'History 103E', 'HISTORY.103F':'History 103F', 
	'HISTORY.103H':'History 103H', 'HISTORY.103S':'History 103S', 'HISTORY.103U':'History 103U', 'HISTORY.104':'History 104', 'HISTORY.105A':'History 105A', 'HISTORY.105B':'History 105B', 'HISTORY.106A':'History 106A', 
	'HISTORY.106B':'History 106B', 'HISTORY.N106A':'History N106A', 'HISTORY.N106B':'History N106B', 'HISTORY.108':'History 108', 'HISTORY.109A':'History 109A', 'HISTORY.109B':'History 109B', 'HISTORY.109C':'History 109C',
	'HISTORY.N109C':'History N109C', 'HISTORY.111A':'History 111A', 'HISTORY.111B':'History 111B', 'HISTORY.111C':'History 111C', 'HISTORY.C111B':'History C111B', 'HISTORY.111D':'History 111D', 'HISTORY.112B':'History 112B',
	'HISTORY.112C':'History 112C', 'HISTORY.N112B':'History N112B', 'HISTORY.113A':'History 113A', 'HISTORY.113B':'History 113B', 'HISTORY.114A':'History 114A', 'HISTORY.114B':'History 114B', 'HISTORY.116A':'History 116A', 
	'HISTORY.116B':'History 116B', 'HISTORY.116C':'History 116C', 'HISTORY.116D':'History 116D', 'HISTORY.116G':'History 116G', 'HISTORY.117A':'History 117A', 'HISTORY.117D':'History 117D', 'HISTORY.118A':'History 118A', 
	'HISTORY.118B':'History 118B', 'HISTORY.118C':'History 118C', 'HISTORY.119A':'History 119A', 'HISTORY.N119A':'History N119A', 'HISTORY.120AC':'History 120AC', 'HISTORY.121B':'History 121B', 'HISTORY.122AC':'History 122AC', 
	'HISTORY.123':'History 123', 'HISTORY.124A':'History 124A', 'HISTORY.124B':'History 124B', 'HISTORY.N124A':'History N124A', 'HISTORY.N124B':'History N124B', 'HISTORY.125A':'History 125A', 'HISTORY.125B':'History 125B', 
	'HISTORY.N125B':'History N125B', 'HISTORY.126A':'History 126A', 'HISTORY.126B':'History 126B', 'HISTORY.127AC':'History 127AC', 'HISTORY.130B':'History 130B', 'HISTORY.131B':'History 131B', 'HISTORY.N131B':'History N131B',
	'HISTORY.C132B':'History C132B', 'HISTORY.134A':'History 134A', 'HISTORY.135':'History 135', 'HISTORY.136':'History 136', 'HISTORY.136AC':'History 136AC', 'HISTORY.137AC':'History 137AC', 'HISTORY.138':'History 138', 
	'HISTORY.138T':'History 138T', 'HISTORY.C139B':'History C139B', 'HISTORY.C139C':'History C139C', 'HISTORY.140B':'History 140B', 'HISTORY.141B':'History 141B', 'HISTORY.143':'History 143', 'HISTORY.N143':'History N143',
	'HISTORY.146':'History 146', 'HISTORY.149B':'History 149B', 'HISTORY.150B':'History 150B', 'HISTORY.151A':'History 151A', 'HISTORY.151B':'History 151B', 'HISTORY.151C':'History 151C', 'HISTORY.N151C':'History N151C', 
	'HISTORY.152A':'History 152A', 'HISTORY.154':'History 154', 'HISTORY.155A':'History 155A', 'HISTORY.155B':'History 155B', 'HISTORY.C157':'History C157', 'HISTORY.158A':'History 158A', 'HISTORY.158B':'History 158B', 
	'HISTORY.158C':'History 158C', 'HISTORY.N158C':'History N158C', 'HISTORY.159A':'History 159A', 'HISTORY.159B':'History 159B', 'HISTORY.160':'History 160', 'HISTORY.162A':'History 162A', 'HISTORY.162B':'History 162B',
	'HISTORY.N162A':'History N162A', 'HISTORY.163A':'History 163A', 'HISTORY.163B':'History 163B', 'HISTORY.164A':'History 164A', 'HISTORY.164B':'History 164B', 'HISTORY.164C':'History 164C', 'HISTORY.S164B':'History S164B',
	'HISTORY.165A':'History 165A', 'HISTORY.165B':'History 165B', 'HISTORY.165D':'History 165D', 'HISTORY.166A':'History 166A', 'HISTORY.166B':'History 166B', 'HISTORY.166C':'History 166C', 'HISTORY.167A':'History 167A', 
	'HISTORY.167B':'History 167B', 'HISTORY.167C':'History 167C', 'HISTORY.168A':'History 168A', 'HISTORY.169A':'History 169A', 'HISTORY.170':'History 170', 'HISTORY.171A':'History 171A', 'HISTORY.171B':'History 171B', 
	'HISTORY.171C':'History 171C', 'HISTORY.172':'History 172', 'HISTORY.173B':'History 173B', 'HISTORY.173C':'History 173C', 'HISTORY.174A':'History 174A', 'HISTORY.174B':'History 174B', 'HISTORY.C175B':'History C175B',
	'HISTORY.177A':'History 177A', 'HISTORY.177B':'History 177B', 'HISTORY.178':'History 178', 'HISTORY.180':'History 180', 'HISTORY.180T':'History 180T',  'HISTORY.182A':'History 182A', 
	'HISTORY.182AT':'History 182AT', 'HISTORY.183':'History 183', 'HISTORY.183A':'History 183A', 'HISTORY.185A':'History 185A', 'HISTORY.185B':'History 185B', 'HISTORY.186':'History 186', 'HISTORY.C187':'History C187', 
	'HISTORY.C188A':'History C188A', 'HISTORY.C191':'History C191', 'HISTORY.C192':'History C192', 'HISTORY.C194':'History C194', 'HISTORY.H195':'History H195', 'HISTORY.C196A':'History C196A', 'HISTORY.C196B':'History C196B',
	'HISTORY.C196W':'History C196W', 'HISTORY.198':'History 198', 'HISTORY.199':'History 199','HISTORY.30A':'History 30A','HISTORY.30B':'History 30B','HISTORY.30C':'History 30C',
	'LEGALST.39B':'LegalStudies 39B', 'LEGALST.39D':'LegalStudies 39D', 'LEGALST.39E':'LegalStudies 39E', 'LEGALST.98':'LegalStudies 98', 'LEGALST.100':'LegalStudies 100', 'LEGALST.102':'LegalStudies 102', 'LEGALST.103':'LegalStudies 103',
	'LEGALST.104':'LegalStudies 104', 'LEGALST.104AC':'LegalStudies 104AC', 'LEGALST.105':'LegalStudies 105', 'LEGALST.107':'LegalStudies 107', 'LEGALST.109':'LegalStudies 109', 'LEGALST.116':'LegalStudies 116', 
	'LEGALST.119':'LegalStudies 119', 'LEGALST.132AC':'LegalStudies 132AC', 'LEGALST.138':'LegalStudies 138', 'LEGALST.139':'LegalStudies 139', 'LEGALST.140':'LegalStudies 140', 'LEGALST.145':'LegalStudies 145', 
	'LEGALST.146':'LegalStudies 146', 'LEGALST.147':'LegalStudies 147', 'LEGALST.151':'LegalStudies 151', 'LEGALST.154':'LegalStudies 154', 'LEGALST.155':'LegalStudies 155', 'LEGALST.156':'LegalStudies 156', 'LEGALST.158':'LegalStudies 158',
	'LEGALST.160':'LegalStudies 160', 'LEGALST.161':'LegalStudies 161', 'LEGALST.162AC':'LegalStudies 162AC', 'LEGALST.163':'LegalStudies 163', 'LEGALST.168':'LegalStudies 168', 'LEGALST.170':'LegalStudies 170', 
	'LEGALST.171':'LegalStudies 171', 'LEGALST.174':'LegalStudies 174', 'LEGALST.176':'LegalStudies 176', 'LEGALST.177':'LegalStudies 177', 'LEGALST.178':'LegalStudies 178', 'LEGALST.179':'LegalStudies 179', 
	'LEGALST.180':'LegalStudies 180', 'LEGALST.181':'LegalStudies 181', 'LEGALST.182':'LegalStudies 182', 'LEGALST.183':'LegalStudies 183', 'LEGALST.184':'LegalStudies 184', 'LEGALST.185AC':'LegalStudies 185AC', 
	'LEGALST.189':'LegalStudies 189', 'LEGALST.190':'LegalStudies 190', 'LEGALST.H195A':'LegalStudies H195A', 'LEGALST.H195B':'LegalStudies H195B', 'LEGALST.198':'LegalStudies 198', 'LEGALST.199':'LegalStudies 199',
	'LINGUIS.1A':'Linguistics 1A', 'LINGUIS.1B':'Linguistics 1B', 'LINGUIS.3':'Linguistics 3', 'LINGUIS.5':'Linguistics 5', 'LINGUIS.11':'Linguistics 11', 'LINGUIS.16':'Linguistics 16', 'LINGUIS.S16':'Linguistics S16',
	'LINGUIS.22':'Linguistics 22', 'LINGUIS.23':'Linguistics 23', 'LINGUIS.24':'Linguistics 24', 'LINGUIS.40':'Linguistics 40', 'LINGUIS.51':'Linguistics 51', 'LINGUIS.55AC':'Linguistics 55AC', 'LINGUIS.S55':'Linguistics S55', 
	'LINGUIS.S55X':'Linguistics S55X', 'LINGUIS.65':'Linguistics 65', 'LINGUIS.97':'Linguistics 97', 'LINGUIS.98':'Linguistics 98', 'LINGUIS.100':'Linguistics 100', 'LINGUIS.C104':'Linguistics C104', 'LINGUIS.C105':'Linguistics C105',
	'LINGUIS.106':'Linguistics 106', 'LINGUIS.110':'Linguistics 110', 'LINGUIS.113':'Linguistics 113', 'LINGUIS.115':'Linguistics 115', 'LINGUIS.120':'Linguistics 120', 'LINGUIS.121':'Linguistics 121', 'LINGUIS.122':'Linguistics 122',
	'LINGUIS.123':'Linguistics 123', 'LINGUIS.124':'Linguistics 124', 'LINGUIS.125':'Linguistics 125', 'LINGUIS.127':'Linguistics 127', 'LINGUIS.128':'Linguistics 128', 'LINGUIS.130':'Linguistics 130', 'LINGUIS.C137':'Linguistics C137',
	'LINGUIS.C139':'Linguistics C139', 'LINGUIS.140':'Linguistics 140', 'LINGUIS.141':'Linguistics 141', 'LINGUIS.C142':'Linguistics C142', 'LINGUIS.146':'Linguistics 146', 'LINGUIS.C146':'Linguistics C146', 'LINGUIS.C147':'Linguistics C147',
	'LINGUIS.150':'Linguistics 150', 'LINGUIS.151':'Linguistics 151', 'LINGUIS.152':'Linguistics 152', 'LINGUIS.155AC':'Linguistics 155AC', 'LINGUIS.158':'Linguistics 158', 'LINGUIS.159':'Linguistics 159', 'LINGUIS.159L':'Linguistics 159L',
	'LINGUIS.C160':'Linguistics C160', 'LINGUIS.165':'Linguistics 165', 'LINGUIS.170':'Linguistics 170', 'LINGUIS.175':'Linguistics 175', 'LINGUIS.181':'Linguistics 181', 'LINGUIS.H195A':'Linguistics H195A', 'LINGUIS.H195B':'Linguistics H195B',
	'LINGUIS.197':'Linguistics 197', 'LINGUIS.198':'Linguistics 198', 'LINGUIS.199':'Linguistics 199',
	'MEDIA.10':'Media 10', 'MEDIA.N10':'Media N10', 'MEDIA.24':'Media 24', 'MEDIA.39A':'Media 39A', 'MEDIA.39B':'Media 39B', 'MEDIA.39C':'Media 39C', 'MEDIA.39D':'Media 39D', 'MEDIA.39E':'Media 39E', 'MEDIA.39F':'Media 39F', 'MEDIA.39G':'Media 39G',
	'MEDIA.39H':'Media 39H', 'MEDIA.39I':'Media 39I', 'MEDIA.39J':'Media 39J', 'MEDIA.39K':'Media 39K', 'MEDIA.39L':'Media 39L', 'MEDIA.39M':'Media 39M', 'MEDIA.39N':'Media 39N', 'MEDIA.39O':'Media 39O', 'MEDIA.39P':'Media 39P', 
	'MEDIA.39Q':'Media 39Q', 'MEDIA.39R':'Media 39R', 'MEDIA.39S':'Media 39S', 'MEDIA.39T':'Media 39T', 'MEDIA.39U':'Media 39U', 'MEDIA.39V':'Media 39V', 'MEDIA.39W':'Media 39W', 'MEDIA.39X':'Media 39X', 'MEDIA.39Y':'Media 39Y', 
	'MEDIA.39Z':'Media 39Z', 'MEDIA.84':'Media 84', 'MEDIA.101':'Media 101', 'MEDIA.102':'Media 102', 'MEDIA.C103':'Media C103', 'MEDIA.104A':'Media 104A', 'MEDIA.104B':'Media 104B', 'MEDIA.C104C':'Media C104C', 'MEDIA.104D':'Media 104D',
	'MEDIA.C118':'Media C118', 'MEDIA.C125':'Media C125', 'MEDIA.130':'Media 130', 'MEDIA.140':'Media 140', 'MEDIA.150':'Media 150', 'MEDIA.160':'Media 160', 'MEDIA.170':'Media 170', 'MEDIA.180':'Media 180', 'MEDIA.190':'Media 190', 
	'MEDIA.H196':'Media H196', 'MEDIA.C196A':'Media C196A', 'MEDIA.C196B':'Media C196B', 'MEDIA.C196W':'Media C196W', 'MEDIA.198':'Media 198', 'MEDIA.199':'Media 199',
	'POLECON.24':'PoliticalEcon 24', 'POLECON.84':'PoliticalEcon 84', 'POLECON.98':'PoliticalEcon 98', 'POLECON.100':'PoliticalEcon 100', 'POLECON.101':'PoliticalEcon 101', 'POLECON.130':'PoliticalEcon 130', 'POLECON.133':'PoliticalEcon 133',
	'POLECON.140':'PoliticalEcon 140', 'POLECON.150':'PoliticalEcon 150', 'POLECON.155':'PoliticalEcon 155', 'POLECON.160':'PoliticalEcon 160', 'POLECON.W160A':'PoliticalEcon W160A', 'POLECON.192':'PoliticalEcon 192', 'POLECON.H195':'PoliticalEcon H195',
	'POLECON.196':'PoliticalEcon 196', 'POLECON.C196A':'PoliticalEcon C196A', 'POLECON.C196B':'PoliticalEcon C196B', 'POLECON.C196W':'PoliticalEcon C196W', 'POLECON.197':'PoliticalEcon 197', 'POLECON.198':'PoliticalEcon 198', 'POLECON.199':'PoliticalEcon 199',
	'POLSCI.1':'PoliSci 1', 'POLSCI.2':'PoliSci 2', 'POLSCI.3':'PoliSci 3', 'POLSCI.4':'PoliSci 4', 'POLSCI.5':'PoliSci 5', 'POLSCI.18AC':'PoliSci 18AC', 'POLSCI.39B':'PoliSci 39B', 'POLSCI.41':'PoliSci 41', 'POLSCI.C79':'PoliSci C79', 'POLSCI.98':'PoliSci 98',
	'POLSCI.99':'PoliSci 99', 'POLSCI.102':'PoliSci 102', 'POLSCI.103':'PoliSci 103', 'POLSCI.103W':'PoliSci 103W', 'POLSCI.104':'PoliSci 104', 'POLSCI.105':'PoliSci 105', 'POLSCI.106A':'PoliSci 106A', 'POLSCI.109A':'PoliSci 109A', 'POLSCI.109B':'PoliSci 109B',
	'POLSCI.109G':'PoliSci 109G', 'POLSCI.109H':'PoliSci 109H', 'POLSCI.109L':'PoliSci 109L', 'POLSCI.109M':'PoliSci 109M', 'POLSCI.109R':'PoliSci 109R', 'POLSCI.109W':'PoliSci 109W', 'POLSCI.110B':'PoliSci 110B', 'POLSCI.111AC':'PoliSci 111AC', 
	'POLSCI.112A':'PoliSci 112A', 'POLSCI.112B':'PoliSci 112B', 'POLSCI.112C':'PoliSci 112C', 'POLSCI.112D':'PoliSci 112D', 'POLSCI.N113A':'PoliSci N113A', 'POLSCI.114A':'PoliSci 114A', 'POLSCI.116A':'PoliSci 116A', 'POLSCI.116B':'PoliSci 116B', 
	'POLSCI.116C':'PoliSci 116C', 'POLSCI.116D':'PoliSci 116D', 'POLSCI.116E':'PoliSci 116E', 'POLSCI.116F':'PoliSci 116F', 'POLSCI.116G':'PoliSci 116G', 'POLSCI.116H':'PoliSci 116H', 'POLSCI.116J':'PoliSci 116J', 'POLSCI.116K':'PoliSci 116K', 
	'POLSCI.116L':'PoliSci 116L', 'POLSCI.116M':'PoliSci 116M', 'POLSCI.116N':'PoliSci 116N', 'POLSCI.116O':'PoliSci 116O', 'POLSCI.116P':'PoliSci 116P', 'POLSCI.116Q':'PoliSci 116Q', 'POLSCI.116R':'PoliSci 116R', 'POLSCI.116S':'PoliSci 116S', 
	'POLSCI.116T':'PoliSci 116T', 'POLSCI.116U':'PoliSci 116U', 'POLSCI.116V':'PoliSci 116V', 'POLSCI.116W':'PoliSci 116W', 'POLSCI.116X':'PoliSci 116X', 'POLSCI.116Y':'PoliSci 116Y', 'POLSCI.116Z':'PoliSci 116Z', 'POLSCI.118AC':'PoliSci 118AC', 
	'POLSCI.122A':'PoliSci 122A', 'POLSCI.123A':'PoliSci 123A', 'POLSCI.123G':'PoliSci 123G', 'POLSCI.123H':'PoliSci 123H', 'POLSCI.123M':'PoliSci 123M', 'POLSCI.123S':'PoliSci 123S', 'POLSCI.124A':'PoliSci 124A', 'POLSCI.124C':'PoliSci 124C', 
	'POLSCI.126A':'PoliSci 126A', 'POLSCI.128':'PoliSci 128', 'POLSCI.128A':'PoliSci 128A', 'POLSCI.129B':'PoliSci 129B', 'POLSCI.C131A':'PoliSci C131A', 'POLSCI.C135':'PoliSci C135', 'POLSCI.137A':'PoliSci 137A', 'POLSCI.138E':'PoliSci 138E', 
	'POLSCI.138G':'PoliSci 138G', 'POLSCI.139B':'PoliSci 139B', 'POLSCI.C139':'PoliSci C139', 'POLSCI.139D':'PoliSci 139D', 'POLSCI.140E':'PoliSci 140E', 'POLSCI.140F':'PoliSci 140F', 'POLSCI.140R':'PoliSci 140R', 'POLSCI.140S':'PoliSci 140S', 
	'POLSCI.141C':'PoliSci 141C', 'POLSCI.142A':'PoliSci 142A', 'POLSCI.143B':'PoliSci 143B', 'POLSCI.143A':'PoliSci 143A', 'POLSCI.143C':'PoliSci 143C', 'POLSCI.143T':'PoliSci 143T', 'POLSCI.144':'PoliSci 144', 'POLSCI.144B':'PoliSci 144B', 
	'POLSCI.145A':'PoliSci 145A', 'POLSCI.145B':'PoliSci 145B', 'POLSCI.W145A':'PoliSci W145A', 'POLSCI.146A':'PoliSci 146A', 'POLSCI.146D':'PoliSci 146D', 'POLSCI.N146C':'PoliSci N146C', 'POLSCI.147F':'PoliSci 147F', 'POLSCI.147G':'PoliSci 147G', 
	'POLSCI.147T':'PoliSci 147T', 'POLSCI.148A':'PoliSci 148A', 'POLSCI.149B':'PoliSci 149B', 'POLSCI.149C':'PoliSci 149C', 'POLSCI.149E':'PoliSci 149E', 'POLSCI.149F':'PoliSci 149F', 'POLSCI.149I':'PoliSci 149I', 'POLSCI.149J':'PoliSci 149J', 
	'POLSCI.149P':'PoliSci 149P', 'POLSCI.149W':'PoliSci 149W', 'POLSCI.149Y':'PoliSci 149Y', 'POLSCI.149Z':'PoliSci 149Z', 'POLSCI.150':'PoliSci 150', 'POLSCI.157A':'PoliSci 157A', 'POLSCI.157B':'PoliSci 157B', 'POLSCI.161':'PoliSci 161', 
	'POLSCI.164A':'PoliSci 164A', 'POLSCI.N164A':'PoliSci N164A', 'POLSCI.166':'PoliSci 166', 'POLSCI.167AC':'PoliSci 167AC', 'POLSCI.169':'PoliSci 169', 'POLSCI.171':'PoliSci 171', 'POLSCI.173S':'PoliSci 173S', 'POLSCI.175A':'PoliSci 175A', 
	'POLSCI.179':'PoliSci 179', 'POLSCI.181':'PoliSci 181', 'POLSCI.H190A':'PoliSci H190A', 'POLSCI.H190B':'PoliSci H190B', 'POLSCI.191':'PoliSci 191', 'POLSCI.196':'PoliSci 196', 'POLSCI.C196A':'PoliSci C196A', 'POLSCI.C196B':'PoliSci C196B', 
	'POLSCI.C196W':'PoliSci C196W', 'POLSCI.196S':'PoliSci 196S', 'POLSCI.196W':'PoliSci 196W', 'POLSCI.197':'PoliSci 197', 'POLSCI.198':'PoliSci 198', 'POLSCI.199':'PoliSci 199',
	'SOCWEL.10':'SocialWelfare 10', 'SOCWEL.20':'SocialWelfare 20', 'SOCWEL.24':'SocialWelfare 24', 'SOCWEL.97':'SocialWelfare 97', 'SOCWEL.98':'SocialWelfare 98', 'SOCWEL.107':'SocialWelfare 107', 'SOCWEL.110':'SocialWelfare 110', 'SOCWEL.112':'SocialWelfare 112',
	'SOCWEL.114':'SocialWelfare 114', 'SOCWEL.114AC':'SocialWelfare 114AC', 'SOCWEL.116':'SocialWelfare 116', 'SOCWEL.138':'SocialWelfare 138', 'SOCWEL.148':'SocialWelfare 148', 'SOCWEL.150L':'SocialWelfare 150L', 'SOCWEL.152':'SocialWelfare 152', 
	'SOCWEL.174':'SocialWelfare 174', 'SOCWEL.174AC':'SocialWelfare 174AC', 'SOCWEL.175AC':'SocialWelfare 175AC', 'SOCWEL.180':'SocialWelfare 180', 'SOCWEL.H195':'SocialWelfare H195', 'SOCWEL.197':'SocialWelfare 197', 'SOCWEL.198':'SocialWelfare 198', 
	'SOCWEL.199':'SocialWelfare 199',
	'ENVECON.C1':'EEP C1', 'ENVECON.39D':'EEP 39D', 'ENVECON.100':'EEP 100', 'ENVECON.C101':'EEP C101', 'ENVECON.C102':'EEP C102', 'ENVECON.C115':'EEP C115', 'ENVECON.C118':'EEP C118', 'ENVECON.131':'EEP 131', 'ENVECON.140AC':'EEP 140AC', 'ENVECON.142':'EEP 142', 
	'ENVECON.143':'EEP 143', 'ENVECON.145':'EEP 145', 'ENVECON.147':'EEP 147', 'ENVECON.C151':'EEP C151', 'ENVECON.152':'EEP 152', 'ENVECON.153':'EEP 153', 'ENVECON.154':'EEP 154', 'ENVECON.161':'EEP 161', 'ENVECON.162':'EEP 162', 'ENVECON.C175':'EEP C175', 
	'ENVECON.C180':'EEP C180', 'ENVECON.C181':'EEP C181', 'ENVECON.C183':'EEP C183', 'ENVECON.195':'EEP 195', 'ENVECON.196':'EEP 196', 'ENVECON.H196':'EEP H196', 'ENVECON.197':'EEP 197', 'ENVECON.198':'EEP 198', 'ENVECON.199':'EEP 199',
	'SOCIOL.1':'Sociology 1', 'SOCIOL.3AC':'Sociology 3AC', 'SOCIOL.5':'Sociology 5', 'SOCIOL.7':'Sociology 7', 'SOCIOL.98':'Sociology 98', 'SOCIOL.101':'Sociology 101', 'SOCIOL.103':'Sociology 103', 'SOCIOL.107A':'Sociology 107A', 'SOCIOL.107B':'Sociology 107B',
	'SOCIOL.108':'Sociology 108', 'SOCIOL.110':'Sociology 110', 'SOCIOL.111':'Sociology 111', 'SOCIOL.111AC':'Sociology 111AC', 'SOCIOL.111C':'Sociology 111C', 'SOCIOL.111P':'Sociology 111P', 'SOCIOL.C112':'Sociology C112', 'SOCIOL.113':'Sociology 113', 'SOCIOL.113AC':'Sociology 113AC',
	'SOCIOL.114':'Sociology 114', 'SOCIOL.115B':'Sociology 115B', 'SOCIOL.C115':'Sociology C115', 'SOCIOL.116':'Sociology 116', 'SOCIOL.C116G':'Sociology C116G', 'SOCIOL.117':'Sociology 117', 'SOCIOL.119S':'Sociology 119S', 'SOCIOL.120':'Sociology 120', 'SOCIOL.121':'Sociology 121', 
	'SOCIOL.123':'Sociology 123', 'SOCIOL.124':'Sociology 124', 'SOCIOL.C126':'Sociology C126', 'SOCIOL.127':'Sociology 127', 'SOCIOL.130':'Sociology 130', 'SOCIOL.130AC':'Sociology 130AC', 'SOCIOL.131':'Sociology 131', 'SOCIOL.131A':'Sociology 131A', 'SOCIOL.131AC':'Sociology 131AC',
	'SOCIOL.131F':'Sociology 131F', 'SOCIOL.133':'Sociology 133', 'SOCIOL.136':'Sociology 136', 'SOCIOL.137AC':'Sociology 137AC', 'SOCIOL.139':'Sociology 139', 'SOCIOL.140':'Sociology 140', 'SOCIOL.142':'Sociology 142', 'SOCIOL.144':'Sociology 144', 'SOCIOL.145':'Sociology 145', 
	'SOCIOL.145AC':'Sociology 145AC', 'SOCIOL.145L':'Sociology 145L', 'SOCIOL.146':'Sociology 146', 'SOCIOL.146AC':'Sociology 146AC', 'SOCIOL.148':'Sociology 148', 'SOCIOL.150':'Sociology 150', 'SOCIOL.150A':'Sociology 150A', 'SOCIOL.C150A':'Sociology C150A', 'SOCIOL.151':'Sociology 151',
	'SOCIOL.152':'Sociology 152', 'SOCIOL.160':'Sociology 160', 'SOCIOL.165':'Sociology 165', 'SOCIOL.166':'Sociology 166', 'SOCIOL.167':'Sociology 167', 'SOCIOL.C167':'Sociology C167', 'SOCIOL.169':'Sociology 169', 'SOCIOL.169F':'Sociology 169F', 'SOCIOL.180C':'Sociology 180C', 
	'SOCIOL.180E':'Sociology 180E', 'SOCIOL.180I':'Sociology 180I', 'SOCIOL.180P':'Sociology 180P', 'SOCIOL.181':'Sociology 181', 'SOCIOL.182':'Sociology 182', 'SOCIOL.183':'Sociology 183', 'SOCIOL.C184':'Sociology C184', 'SOCIOL.185':'Sociology 185', 'SOCIOL.186':'Sociology 186',
	'SOCIOL.189':'Sociology 189', 'SOCIOL.C189':'Sociology C189', 'SOCIOL.189G':'Sociology 189G', 'SOCIOL.190':'Sociology 190', 'SOCIOL.190AC':'Sociology 190AC', 'SOCIOL.H190A':'Sociology H190A', 'SOCIOL.H190B':'Sociology H190B', 'SOCIOL.191':'Sociology 191', 'SOCIOL.192':'Sociology 192',
	'SOCIOL.194':'Sociology 194', 'SOCIOL.195':'Sociology 195', 'SOCIOL.C196A':'Sociology C196A', 'SOCIOL.C196B':'Sociology C196B', 'SOCIOL.C196W':'Sociology C196W', 'SOCIOL.197':'Sociology 197', 'SOCIOL.198':'Sociology 198', 'SOCIOL.199':'Sociology 199'} 

"""
Determines the number of units each course is through accessing the database of classes and units
For now it just returns 4 for the sake of testing
"""
def units(course):
	return getCourseUnits(course)
	#return 4
"""
handles a simple requirement that a student must take a class
formally known as req but refered to as reqName
the description is an explanation of the general requirement
"""
def basicReq(takenClasses, req, reqName, description):
	if (req in takenClasses):
		return {'reqName':reqName, 'reqCompleted':True, 'reqDescription':description,'courseDone':[reqName], 'courseLeft':[]}
	else:
		return {'reqName':reqName, 'reqCompleted':False, 'reqDescription':description,'courseDone':[], 'courseLeft':[reqName]}
"""
handles a relatively simple requirement known as requirement
that a student must take one of two classes
formally known as req and req1 but refered to as reqName and reqName1
the description is an explanation of the general requirement
"""
def twoChoiceReq(takenClasses, requirement, req, reqName, req1, reqName1, description):
	if (req in takenClasses)and (req1 in takenClasses):
		return {'reqName':requirement, 'reqCompleted':True, 'reqDescription':description,'courseDone':[reqName,reqName1], 'courseLeft':[]}
	elif (req in takenClasses):
		return {'reqName':requirement, 'reqCompleted':True, 'reqDescription':description,'courseDone':[reqName], 'courseLeft':[reqName1]}
	elif (req1 in takenClasses):
		return {'reqName':requirement, 'reqCompleted':True, 'reqDescription':description,'courseDone':[reqName1], 'courseLeft':[reqName]}
	else:
		return {'reqName':requirement, 'reqCompleted':False, 'reqDescription':description,'courseDone':[], 'courseLeft':[reqName, reqName1]}
"""
handles a relatively simple requirement known as requirement
that a student must take two classes
formally known as req and req1 but refered to as reqName and reqName1
the description is an explanation of the general requirement
"""
def twoReq(takenClasses, requirement, req, reqName, req1, reqName1, description):
	if ((req in takenClasses)and (req1 in takenClasses)):
		return {'reqName':requirement, 'reqCompleted':True, 'reqDescription':description,'courseDone':[reqName, reqName1], 'courseLeft':[]}
	elif (req1 in takenClasses):
                return {'reqName':requirement, 'reqCompleted':False, 'reqDescription':description,'courseDone':[reqName1], 'courseLeft':[reqName]}
	elif (req in takenClasses):
		return {'reqName':requirement, 'reqCompleted':False, 'reqDescription':description,'courseDone':[reqName], 'courseLeft':[reqName1]}
	else:
		return {'reqName':requirement, 'reqCompleted':False, 'reqDescription':description,'courseDone':[], 'courseLeft':[reqName, reqName1]}
"""
handles the complex requirement known as requirement
that a student must take one of a large number classes
these requirements are stored in a dictionary, requirements, that maps req to reqName
the description is an explanation of the general requirement
"""
def manyChoiceReq(takenClasses, requirement, requirements, description):
	listOfClassesTaken=[]
	listOfClassesNotTaken=[]
	# iterate over all elements in the dictionary to check if they have been taken or not
	for key in requirements:
		if (key in takenClasses):
			listOfClassesTaken.append(requirements[key])
		else:
			listOfClassesNotTaken.append(requirements[key])
	# No classes on the list were taken
	if (not listOfClassesTaken):
		return {'reqName':requirement, 'reqCompleted':False, 'reqDescription':description,'courseDone':[], 'courseLeft':listOfClassesNotTaken}
	# Some class was taken
	else:
		return {'reqName':requirement, 'reqCompleted':True, 'reqDescription':description,'courseDone':listOfClassesTaken, 'courseLeft':listOfClassesNotTaken}
	return ans
"""
handles the complex requirement known as requirement
that a student must take at least i of a large number classes
these requirements are stored in a dictionary, requirements, that maps req to reqName
the description is an explanation of the general requirement
"""
def doSomeManyChoiceReq(takenClasses, requirement, requirements, description, i):
	listOfClassesTaken=[]
	listOfClassesNotTaken=[]
	# iterate over all elements in the dictionary to check if they have been taken or not
	for key in requirements:
		if (key in takenClasses):
			listOfClassesTaken.append(requirements[key])
		else:
			listOfClassesNotTaken.append(requirements[key])
	# Less than i classes on the list were taken
	if (len( listOfClassesTaken)<i):
		return {'reqName':requirement, 'reqCompleted':False, 'reqDescription':description,'courseDone':listOfClassesTaken, 'courseLeft':listOfClassesNotTaken}
	# At least i classes were taken
	else:
		return {'reqName':requirement, 'reqCompleted':True, 'reqDescription':description,'courseDone':listOfClassesTaken, 'courseLeft':listOfClassesNotTaken}
	return ans

"""
Code to Return all seven breadth requirements
"""
def sevenBreadth(takenClasses):
	alTaken=[]
	alNotTaken=[]
	alConflict=[]
	alDone=False
	for item in artAndLit:
		if (item in takenClasses):
			if(item in biologicalScience) or (item in historicalStudies) or (item in international) or (item in philosophyValues) or (item in physicalScience) or (item in socialBehavioralScience):
				alConflict.append(item)
			else:
				alTaken.append(item)
		else:
			alNotTaken.append(item)
	bsTaken=[]
	bsNotTaken=[]
	bsConflict=[]
	bsDone=False
	for item in biologicalScience:
		if (item in takenClasses):
			if(item in artAndLit) or (item in historicalStudies) or (item in international) or (item in philosophyValues) or (item in physicalScience) or (item in socialBehavioralScience):
				bsConflict.append(item)
			else:
				bsTaken.append(item)
		else:
			bsNotTaken.append(item)
	hsTaken=[]
	hsNotTaken=[]
	hsConflict=[]
	hsDone=False
	for item in historicalStudies:
		if (item in takenClasses):
			if(item in artAndLit) or (item in biologicalScience) or (item in international) or (item in philosophyValues) or (item in physicalScience) or (item in socialBehavioralScience):
				hsConflict.append(item)
			else:
				hsTaken.append(item)
		else:
			hsNotTaken.append(item)
	isTaken=[]
	isNotTaken=[]
	isConflict=[]
	isDone=False
	for item in international:
		if (item in takenClasses):
			if(item in artAndLit) or (item in biologicalScience) or (item in historicalStudies) or (item in philosophyValues) or (item in physicalScience) or (item in socialBehavioralScience):
				isConflict.append(item)
			else:
				isTaken.append(item)
		else:
			isNotTaken.append(item)
	pvTaken=[]
	pvNotTaken=[]
	pvConflict=[]
	pvDone=False
	for item in philosophyValues:
		if (item in takenClasses):
			if(item in artAndLit) or (item in biologicalScience) or (item in historicalStudies) or (item in international) or (item in physicalScience) or (item in socialBehavioralScience):
				pvConflict.append(item)
			else:
				pvTaken.append(item)
		else:
			pvNotTaken.append(item)
	psTaken=[]
	psNotTaken=[]
	psConflict=[]
	psDone=False
	for item in physicalScience:
		if (item in takenClasses):
			if(item in artAndLit) or (item in biologicalScience) or (item in historicalStudies) or (item in international) or (item in philosophyValues) or (item in socialBehavioralScience):
				psConflict.append(item)
			else:
				psTaken.append(item)
		else:
			psNotTaken.append(item)
	sbsTaken=[]
	sbsNotTaken=[]
	sbsConflict=[]
	sbsDone=False
	for item in socialBehavioralScience:
		if (item in takenClasses):
			if(item in artAndLit) or (item in biologicalScience) or (item in historicalStudies) or (item in international) or (item in philosophyValues) or (item in physicalScience):
				sbsConflict.append(item)
			else:
				sbsTaken.append(item)
		else:
			sbsNotTaken.append(item)
	ans=[]
	if alTaken:
		alDone=True
		ans.append({'reqName':'Art and Literature Breadth', 'reqCompleted':True, 'reqDescription':'You must take one art or literature course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/al.html','courseDone':alTaken, 'courseLeft':alNotTaken})
	elif (not alConflict):
		alDone=True
		ans.append({'reqName':'Art and Literature Breadth', 'reqCompleted':False, 'reqDescription':'You must take one art or literature course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/al.html','courseDone':alTaken, 'courseLeft':alNotTaken})
	if bsTaken:
		bsDone=True
		ans.append({'reqName':'Biological Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one biological science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/bs.html','courseDone':bsTaken, 'courseLeft':bsNotTaken})
	elif (not bsConflict):
		bsDone=True
		ans.append({'reqName':'Biological Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one biological science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/bs.html','courseDone':bsTaken, 'courseLeft':bsNotTaken})
	if hsTaken:
		hsDone=True
		ans.append({'reqName':'Historical Studies Breadth', 'reqCompleted':True, 'reqDescription':'You must take one historical studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/hs.html','courseDone':hsTaken, 'courseLeft':hsNotTaken})
	elif (not hsConflict):
		hsDone=True
		ans.append({'reqName':'Historical Studies Breadth', 'reqCompleted':False, 'reqDescription':'You must take one historical studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/hs.html','courseDone':hsTaken, 'courseLeft':hsNotTaken})
	if isTaken:
		isDone=True
		ans.append({'reqName':'International Studies Breadth', 'reqCompleted':True, 'reqDescription':'You must take one internaational studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/is.html','courseDone':isTaken, 'courseLeft':isNotTaken})
	elif (not isConflict):
		isDone=True
		ans.append({'reqName':'International Studies Breadth', 'reqCompleted':False, 'reqDescription':'You must take one internaational studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/is.html','courseDone':isTaken, 'courseLeft':isNotTaken})
	if pvTaken:
		pvDone=True
		ans.append({'reqName':'Philosophy and Values Breadth', 'reqCompleted':True, 'reqDescription':'You must take one philosophy and values course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/pv.html','courseDone':pvTaken, 'courseLeft':pvNotTaken})
	elif (not pvConflict):
		pvDone=True
		ans.append({'reqName':'Philosophy and Values Breadth', 'reqCompleted':False, 'reqDescription':'You must take one philosophy and values course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/pv.html','courseDone':pvTaken, 'courseLeft':pvNotTaken})
	if psTaken:
		psDone=True
		ans.append({'reqName':'Physical Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one physical science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/ps.html','courseDone':psTaken, 'courseLeft':psNotTaken})
	elif (not psConflict):
		psDone=True
		ans.append({'reqName':'Physical Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one physical science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/ps.html','courseDone':psTaken, 'courseLeft':psNotTaken})
	if sbsTaken:
		sbsDone=True
		ans.append({'reqName':'Social and Behavioral Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one social or behavioral science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html','courseDone':sbsTaken, 'courseLeft':sbsNotTaken})
	elif (not sbsConflict):
		sbsDone=True
		ans.append({'reqName':'Social and Behavioral Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one social or behavioral science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html','courseDone':sbsTaken, 'courseLeft':sbsNotTaken})
	for i in range(0,7):
		if (not alDone):
			if (len(alConflict)==1):
				alDone=True
				ans.append({'reqName':'Art and Literature Breadth', 'reqCompleted':True, 'reqDescription':'You must take one art or literature course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/al.html','courseDone':alConflict, 'courseLeft':alNotTaken})
				if (alConflict[0] in bsConflict):
					bsConflict.remove(alConflict[0])
				if (alConflict[0] in hsConflict):
					hsConflict.remove(alConflict[0])
				if (alConflict[0] in isConflict):
					isConflict.remove(alConflict[0])
				if (alConflict[0] in pvConflict):
					pvConflict.remove(alConflict[0])
				if (alConflict[0] in psConflict):
					psConflict.remove(alConflict[0])
				if (alConflict[0] in sbsConflict):
					sbsConflict.remove(alConflict[0])
		if (not bsDone):
			if (len(bsConflict)==1):
				bsDone=True
				ans.append({'reqName':'Biological Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one biological science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/bs.html','courseDone':bsConflict, 'courseLeft':bsNotTaken})
				if (bsConflict[0] in alConflict):
					alConflict.remove(bsConflict[0])
				if (bsConflict[0] in hsConflict):
					hsConflict.remove(bsConflict[0])
				if (bsConflict[0] in isConflict):
					isConflict.remove(bsConflict[0])
				if (bsConflict[0] in pvConflict):
					pvConflict.remove(bsConflict[0])
				if (bsConflict[0] in psConflict):
					psConflict.remove(bsConflict[0])
				if (bsConflict[0] in sbsConflict):
					sbsConflict.remove(bsConflict[0])
			elif(len(bsConflict)==0):
				bsDone=True
				ans.append({'reqName':'Biological Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one biological science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/bs.html','courseDone':bsConflict, 'courseLeft':bsNotTaken})
		if (not hsDone):
			if (len(hsConflict)==1):
				hsDone=True
				ans.append({'reqName':'Historical Studies Breadth', 'reqCompleted':True, 'reqDescription':'You must take one historical studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/hs.html','courseDone':hsConflict, 'courseLeft':hsNotTaken})
				if (hsConflict[0] in alConflict):
					alConflict.remove(hsConflict[0])
				if (hsConflict[0] in bsConflict):
					bsConflict.remove(hsConflict[0])
				if (hsConflict[0] in isConflict):
					isConflict.remove(hsConflict[0])
				if (hsConflict[0] in pvConflict):
					pvConflict.remove(hsConflict[0])
				if (hsConflict[0] in psConflict):
					psConflict.remove(hsConflict[0])
				if (hsConflict[0] in sbsConflict):
					sbsConflict.remove(hsConflict[0])
			elif (len(hsConflict)==0):
				hsDone=True
				ans.append({'reqName':'Historical Studies Breadth', 'reqCompleted':False, 'reqDescription':'You must take one historical studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/hs.html','courseDone':hsConflict, 'courseLeft':hsNotTaken})
		if (not isDone):
			if (len(isConflict)==1):
				isDone=True
				ans.append({'reqName':'International Studies Breadth', 'reqCompleted':True, 'reqDescription':'You must take one internaational studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/is.html','courseDone':isConflict, 'courseLeft':isNotTaken})
				if (isConflict[0] in alConflict):
					alConflict.remove(isConflict[0])
				if (isConflict[0] in bsConflict):
					bsConflict.remove(isConflict[0])
				if (isConflict[0] in hsConflict):
					hsConflict.remove(isConflict[0])
				if (isConflict[0] in pvConflict):
					pvConflict.remove(isConflict[0])
				if (isConflict[0] in psConflict):
					psConflict.remove(isConflict[0])
				if (isConflict[0] in sbsConflict):
					sbsConflict.remove(isConflict[0])
			elif (len(isConflict)==0):
				isDone=True
				ans.append({'reqName':'International Studies Breadth', 'reqCompleted':False, 'reqDescription':'You must take one internaational studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/is.html','courseDone':isConflict, 'courseLeft':isNotTaken})
		if (not pvDone):
			if (len(pvConflict)==1):
				pvDone=True
				ans.append({'reqName':'Philosophy and Values Breadth', 'reqCompleted':True, 'reqDescription':'You must take one philosophy and values course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/pv.html','courseDone':pvConflict, 'courseLeft':pvNotTaken})
				if (pvConflict[0] in alConflict):
					alConflict.remove(pvConflict[0])
				if (pvConflict[0] in bsConflict):
					bsConflict.remove(pvConflict[0])
				if (pvConflict[0] in hsConflict):
					hsConflict.remove(pvConflict[0])
				if (pvConflict[0] in isConflict):
					isConflict.remove(pvConflict[0])
				if (pvConflict[0] in psConflict):
					psConflict.remove(pvConflict[0])
				if (pvConflict[0] in sbsConflict):
					sbsConflict.remove(pvConflict[0])
			elif (len(pvConflict)==0):
				pvDone=True
				ans.append({'reqName':'Philosophy and Values Breadth', 'reqCompleted':False, 'reqDescription':'You must take one philosophy and values course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/pv.html','courseDone':pvConflict, 'courseLeft':pvNotTaken})
		if (not psDone):
			if (len(psConflict)==1):
				psDone=True
				ans.append({'reqName':'Physical Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one physical science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/ps.html','courseDone':psConflict, 'courseLeft':psNotTaken})
				if (psConflict[0] in alConflict):
					alConflict.remove(psConflict[0])
				if (psConflict[0] in bsConflict):
					bsConflict.remove(psConflict[0])
				if (psConflict[0] in hsConflict):
					hsConflict.remove(psConflict[0])
				if (psConflict[0] in isConflict):
					isConflict.remove(psConflict[0])
				if (psConflict[0] in pvConflict):
					pvConflict.remove(psConflict[0])
				if (psConflict[0] in sbsConflict):
					sbsConflict.remove(psConflict[0])
			elif (len(psConflict)==0):
				psDone=True
				ans.append({'reqName':'Physical Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one physical science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/ps.html','courseDone':psConflict, 'courseLeft':psNotTaken})
		if (not sbsDone):
			if (len(sbsConflict)==1):
				sbsDone=True
				ans.append({'reqName':'Social and Behavioral Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one social or behavioral science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html','courseDone':sbsConflict, 'courseLeft':sbsNotTaken})
				if (sbsConflict[0] in alConflict):
					alConflict.remove(sbsConflict[0])
				if (sbsConflict[0] in bsConflict):
					bsConflict.remove(sbsConflict[0])
				if (sbsConflict[0] in hsConflict):
					hsConflict.remove(sbsConflict[0])
				if (sbsConflict[0] in isConflict):
					isConflict.remove(sbsConflict[0])
				if (sbsConflict[0] in pvConflict):
					pvConflict.remove(sbsConflict[0])
				if (sbsConflict[0] in psConflict):
					psConflict.remove(sbsConflict[0])
			elif (len(sbsConflict)==0):
				sbsDone=True
				ans.append({'reqName':'Social and Behavioral Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one social or behavioral science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html','courseDone':sbsTaken, 'courseLeft':sbsNotTaken})
	if(not alDone):
		ans.append({'reqName':'Art and Literature Breadth', 'reqCompleted':True, 'reqDescription':'You must take one art or literature course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/al.html','courseDone':alConflict, 'courseLeft':alNotTaken})
		if (alConflict[0] in bsConflict):
			bsConflict.remove(alConflict[0])
		if (alConflict[0] in hsConflict):
			hsConflict.remove(alConflict[0])
		if (alConflict[0] in isConflict):
			isConflict.remove(alConflict[0])
		if (alConflict[0] in pvConflict):
			pvConflict.remove(alConflict[0])
		if (alConflict[0] in psConflict):
			psConflict.remove(alConflict[0])
		if (alConflict[0] in sbsConflict):
			sbsConflict.remove(alConflict[0])
	for i in range(0,6):
		if (not bsDone):
			if (len(bsConflict)==1):
				bsDone=True
				ans.append({'reqName':'Biological Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one biological science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/bs.html','courseDone':bsConflict, 'courseLeft':bsNotTaken})
				if (bsConflict[0] in hsConflict):
					hsConflict.remove(bsConflict[0])
				if (bsConflict[0] in isConflict):
					isConflict.remove(bsConflict[0])
				if (bsConflict[0] in pvConflict):
					pvConflict.remove(bsConflict[0])
				if (bsConflict[0] in psConflict):
					psConflict.remove(bsConflict[0])
				if (bsConflict[0] in sbsConflict):
					sbsConflict.remove(bsConflict[0])
			elif(len(bsConflict)==0):
				bsDone=True
				ans.append({'reqName':'Biological Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one biological science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/bs.html','courseDone':bsConflict, 'courseLeft':bsNotTaken})
		if (not hsDone):
			if (len(hsConflict)==1):
				hsDone=True
				ans.append({'reqName':'Historical Studies Breadth', 'reqCompleted':True, 'reqDescription':'You must take one historical studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/hs.html','courseDone':hsConflict, 'courseLeft':hsNotTaken})
				if (hsConflict[0] in bsConflict):
					bsConflict.remove(hsConflict[0])
				if (hsConflict[0] in isConflict):
					isConflict.remove(hsConflict[0])
				if (hsConflict[0] in pvConflict):
					pvConflict.remove(hsConflict[0])
				if (hsConflict[0] in psConflict):
					psConflict.remove(hsConflict[0])
				if (hsConflict[0] in sbsConflict):
					sbsConflict.remove(hsConflict[0])
			elif (len(hsConflict)==0):
				hsDone=True
				ans.append({'reqName':'Historical Studies Breadth', 'reqCompleted':False, 'reqDescription':'You must take one historical studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/hs.html','courseDone':hsConflict, 'courseLeft':hsNotTaken})
		if (not isDone):
			if (len(isConflict)==1):
				isDone=True
				ans.append({'reqName':'International Studies Breadth', 'reqCompleted':True, 'reqDescription':'You must take one internaational studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/is.html','courseDone':isConflict, 'courseLeft':isNotTaken})
				if (isConflict[0] in bsConflict):
					bsConflict.remove(isConflict[0])
				if (isConflict[0] in hsConflict):
					hsConflict.remove(isConflict[0])
				if (isConflict[0] in pvConflict):
					pvConflict.remove(isConflict[0])
				if (isConflict[0] in psConflict):
					psConflict.remove(isConflict[0])
				if (isConflict[0] in sbsConflict):
					sbsConflict.remove(isConflict[0])
			elif (len(isConflict)==0):
				isDone=True
				ans.append({'reqName':'International Studies Breadth', 'reqCompleted':False, 'reqDescription':'You must take one internaational studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/is.html','courseDone':isConflict, 'courseLeft':isNotTaken})
		if (not pvDone):
			if (len(pvConflict)==1):
				pvDone=True
				ans.append({'reqName':'Philosophy and Values Breadth', 'reqCompleted':True, 'reqDescription':'You must take one philosophy and values course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/pv.html','courseDone':pvConflict, 'courseLeft':pvNotTaken})
				if (pvConflict[0] in bsConflict):
					bsConflict.remove(pvConflict[0])
				if (pvConflict[0] in hsConflict):
					hsConflict.remove(pvConflict[0])
				if (pvConflict[0] in isConflict):
					isConflict.remove(pvConflict[0])
				if (pvConflict[0] in psConflict):
					psConflict.remove(pvConflict[0])
				if (pvConflict[0] in sbsConflict):
					sbsConflict.remove(pvConflict[0])
			elif (len(pvConflict)==0):
				pvDone=True
				ans.append({'reqName':'Philosophy and Values Breadth', 'reqCompleted':False, 'reqDescription':'You must take one philosophy and values course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/pv.html','courseDone':pvConflict, 'courseLeft':pvNotTaken})
		if (not psDone):
			if (len(psConflict)==1):
				psDone=True
				ans.append({'reqName':'Physical Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one physical science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/ps.html','courseDone':psConflict, 'courseLeft':psNotTaken})
				if (psConflict[0] in bsConflict):
					bsConflict.remove(psConflict[0])
				if (psConflict[0] in hsConflict):
					hsConflict.remove(psConflict[0])
				if (psConflict[0] in isConflict):
					isConflict.remove(psConflict[0])
				if (psConflict[0] in pvConflict):
					pvConflict.remove(psConflict[0])
				if (psConflict[0] in sbsConflict):
					sbsConflict.remove(psConflict[0])
			elif (len(psConflict)==0):
				psDone=True
				ans.append({'reqName':'Physical Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one physical science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/ps.html','courseDone':psConflict, 'courseLeft':psNotTaken})
		if (not sbsDone):
			if (len(sbsConflict)==1):
				sbsDone=True
				ans.append({'reqName':'Social and Behavioral Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one social or behavioral science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html','courseDone':sbsConflict, 'courseLeft':sbsNotTaken})
				if (sbsConflict[0] in bsConflict):
					bsConflict.remove(sbsConflict[0])
				if (sbsConflict[0] in hsConflict):
					hsConflict.remove(sbsConflict[0])
				if (sbsConflict[0] in isConflict):
					isConflict.remove(sbsConflict[0])
				if (sbsConflict[0] in pvConflict):
					pvConflict.remove(sbsConflict[0])
				if (sbsConflict[0] in psConflict):
					psConflict.remove(sbsConflict[0])
			elif (len(sbsConflict)==0):
				sbsDone=True
				ans.append({'reqName':'Social and Behavioral Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one social or behavioral science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html','courseDone':sbsConflict, 'courseLeft':sbsNotTaken})	
	if(not bsDone):
		ans.append({'reqName':'Biological Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one biological science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/bs.html','courseDone':bsConflict, 'courseLeft':bsNotTaken})
		if (bsConflict[0] in hsConflict):
			hsConflict.remove(bsConflict[0])
		if (bsConflict[0] in isConflict):
			isConflict.remove(bsConflict[0])
		if (bsConflict[0] in pvConflict):
			pvConflict.remove(bsConflict[0])
		if (bsConflict[0] in psConflict):
			psConflict.remove(bsConflict[0])
		if (bsConflict[0] in sbsConflict):
			sbsConflict.remove(bsConflict[0])
	for i in range(0,5):
		if (not hsDone):
			if (len(hsConflict)==1):
				hsDone=True
				ans.append({'reqName':'Historical Studies Breadth', 'reqCompleted':True, 'reqDescription':'You must take one historical studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/hs.html','courseDone':hsConflict, 'courseLeft':hsNotTaken})
				if (hsConflict[0] in isConflict):
					isConflict.remove(hsConflict[0])
				if (hsConflict[0] in pvConflict):
					pvConflict.remove(hsConflict[0])
				if (hsConflict[0] in psConflict):
					psConflict.remove(hsConflict[0])
				if (hsConflict[0] in sbsConflict):
					sbsConflict.remove(hsConflict[0])
			elif (len(hsConflict)==0):
				hsDone=True
				ans.append({'reqName':'Historical Studies Breadth', 'reqCompleted':False, 'reqDescription':'You must take one historical studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/hs.html','courseDone':hsConflict, 'courseLeft':hsNotTaken})
		if (not isDone):
			if (len(isConflict)==1):
				isDone=True
				ans.append({'reqName':'International Studies Breadth', 'reqCompleted':True, 'reqDescription':'You must take one internaational studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/is.html','courseDone':isConflict, 'courseLeft':isNotTaken})
				if (isConflict[0] in hsConflict):
					hsConflict.remove(isConflict[0])
				if (isConflict[0] in pvConflict):
					pvConflict.remove(isConflict[0])
				if (isConflict[0] in psConflict):
					psConflict.remove(isConflict[0])
				if (isConflict[0] in sbsConflict):
					sbsConflict.remove(isConflict[0])
			elif (len(isConflict)==0):
				isDone=True
				ans.append({'reqName':'International Studies Breadth', 'reqCompleted':False, 'reqDescription':'You must take one internaational studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/is.html','courseDone':isConflict, 'courseLeft':isNotTaken})
		if (not pvDone):
			if (len(pvConflict)==1):
				pvDone=True
				ans.append({'reqName':'Philosophy and Values Breadth', 'reqCompleted':True, 'reqDescription':'You must take one philosophy and values course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/pv.html','courseDone':pvConflict, 'courseLeft':pvNotTaken})
				if (pvConflict[0] in hsConflict):
					hsConflict.remove(pvConflict[0])
				if (pvConflict[0] in isConflict):
					isConflict.remove(pvConflict[0])
				if (pvConflict[0] in psConflict):
					psConflict.remove(pvConflict[0])
				if (pvConflict[0] in sbsConflict):
					sbsConflict.remove(pvConflict[0])
			elif (len(pvConflict)==0):
				pvDone=True
				ans.append({'reqName':'Philosophy and Values Breadth', 'reqCompleted':False, 'reqDescription':'You must take one philosophy and values course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/pv.html','courseDone':pvConflict, 'courseLeft':pvNotTaken})
		if (not psDone):
			if (len(psConflict)==1):
				psDone=True
				ans.append({'reqName':'Physical Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one physical science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/ps.html','courseDone':psConflict, 'courseLeft':psNotTaken})
				if (psConflict[0] in hsConflict):
					hsConflict.remove(psConflict[0])
				if (psConflict[0] in isConflict):
					isConflict.remove(psConflict[0])
				if (psConflict[0] in pvConflict):
					pvConflict.remove(psConflict[0])
				if (psConflict[0] in sbsConflict):
					sbsConflict.remove(psConflict[0])
			elif (len(psConflict)==0):
				psDone=True
				ans.append({'reqName':'Physical Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one physical science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/ps.html','courseDone':psConflict, 'courseLeft':psNotTaken})
		if (not sbsDone):
			if (len(sbsConflict)==1):
				sbsDone=True
				ans.append({'reqName':'Social and Behavioral Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one social or behavioral science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html','courseDone':sbsConflict, 'courseLeft':sbsNotTaken})
				if (sbsConflict[0] in hsConflict):
					hsConflict.remove(sbsConflict[0])
				if (sbsConflict[0] in isConflict):
					isConflict.remove(sbsConflict[0])
				if (sbsConflict[0] in pvConflict):
					pvConflict.remove(sbsConflict[0])
				if (sbsConflict[0] in psConflict):
					psConflict.remove(sbsConflict[0])
			elif (len(sbsConflict)==0):
				sbsDone=True
				ans.append({'reqName':'Social and Behavioral Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one social or behavioral science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html','courseDone':sbsConflict, 'courseLeft':sbsNotTaken})	
	if(not hsDone):
		ans.append({'reqName':'Historical Studies Breadth', 'reqCompleted':True, 'reqDescription':'You must take one historical studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/hs.html','courseDone':hsConflict, 'courseLeft':hsNotTaken})
		if (hsConflict[0] in isConflict):
			isConflict.remove(hsConflict[0])
		if (hsConflict[0] in pvConflict):
			pvConflict.remove(hsConflict[0])
		if (hsConflict[0] in psConflict):
			psConflict.remove(hsConflict[0])
		if (hsConflict[0] in sbsConflict):
			sbsConflict.remove(hsConflict[0])
	for i in range(0,4):
		if (not isDone):
			if (len(isConflict)==1):
				isDone=True
				ans.append({'reqName':'International Studies Breadth', 'reqCompleted':True, 'reqDescription':'You must take one internaational studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/is.html','courseDone':isConflict, 'courseLeft':isNotTaken})
				if (isConflict[0] in pvConflict):
					pvConflict.remove(isConflict[0])
				if (isConflict[0] in psConflict):
					psConflict.remove(isConflict[0])
				if (isConflict[0] in sbsConflict):
					sbsConflict.remove(isConflict[0])
			elif (len(isConflict)==0):
				isDone=True
				ans.append({'reqName':'International Studies Breadth', 'reqCompleted':False, 'reqDescription':'You must take one internaational studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/is.html','courseDone':isConflict, 'courseLeft':isNotTaken})
		if (not pvDone):
			if (len(pvConflict)==1):
				pvDone=True
				ans.append({'reqName':'Philosophy and Values Breadth', 'reqCompleted':True, 'reqDescription':'You must take one philosophy and values course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/pv.html','courseDone':pvConflict, 'courseLeft':pvNotTaken})
				if (pvConflict[0] in isConflict):
					isConflict.remove(pvConflict[0])
				if (pvConflict[0] in psConflict):
					psConflict.remove(pvConflict[0])
				if (pvConflict[0] in sbsConflict):
					sbsConflict.remove(pvConflict[0])
			elif (len(pvConflict)==0):
				pvDone=True
				ans.append({'reqName':'Philosophy and Values Breadth', 'reqCompleted':False, 'reqDescription':'You must take one philosophy and values course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/pv.html','courseDone':pvConflict, 'courseLeft':pvNotTaken})
		if (not psDone):
			if (len(psConflict)==1):
				psDone=True
				ans.append({'reqName':'Physical Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one physical science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/ps.html','courseDone':psConflict, 'courseLeft':psNotTaken})
				if (psConflict[0] in isConflict):
					isConflict.remove(psConflict[0])
				if (psConflict[0] in pvConflict):
					pvConflict.remove(psConflict[0])
				if (psConflict[0] in sbsConflict):
					sbsConflict.remove(psConflict[0])
			elif (len(psConflict)==0):
				psDone=True
				ans.append({'reqName':'Physical Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one physical science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/ps.html','courseDone':psConflict, 'courseLeft':psNotTaken})
		if (not sbsDone):
			if (len(sbsConflict)==1):
				sbsDone=True
				ans.append({'reqName':'Social and Behavioral Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one social or behavioral science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html','courseDone':sbsConflict, 'courseLeft':sbsNotTaken})
				if (sbsConflict[0] in isConflict):
					isConflict.remove(sbsConflict[0])
				if (sbsConflict[0] in pvConflict):
					pvConflict.remove(sbsConflict[0])
				if (sbsConflict[0] in psConflict):
					psConflict.remove(sbsConflict[0])
			elif (len(sbsConflict)==0):
				sbsDone=True
				ans.append({'reqName':'Social and Behavioral Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one social or behavioral science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html','courseDone':sbsConflict, 'courseLeft':sbsNotTaken})	
	if(not isDone):
		ans.append({'reqName':'International Studies Breadth', 'reqCompleted':True, 'reqDescription':'You must take one internaational studies course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/is.html','courseDone':isConflict, 'courseLeft':isNotTaken})
		if (isConflict[0] in pvConflict):
			pvConflict.remove(isConflict[0])
		if (isConflict[0] in psConflict):
			psConflict.remove(isConflict[0])
		if (isConflict[0] in sbsConflict):
			sbsConflict.remove(isConflict[0])
	for i in range(0,3):
		if (not pvDone):
			if (len(pvConflict)==1):
				pvDone=True
				ans.append({'reqName':'Philosophy and Values Breadth', 'reqCompleted':True, 'reqDescription':'You must take one philosophy and values course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/pv.html','courseDone':pvConflict, 'courseLeft':pvNotTaken})
				if (pvConflict[0] in psConflict):
					psConflict.remove(pvConflict[0])
				if (pvConflict[0] in sbsConflict):
					sbsConflict.remove(pvConflict[0])
			elif (len(pvConflict)==0):
				pvDone=True
				ans.append({'reqName':'Philosophy and Values Breadth', 'reqCompleted':False, 'reqDescription':'You must take one philosophy and values course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/pv.html','courseDone':pvConflict, 'courseLeft':pvNotTaken})
		if (not psDone):
			if (len(psConflict)==1):
				psDone=True
				ans.append({'reqName':'Physical Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one physical science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/ps.html','courseDone':psConflict, 'courseLeft':psNotTaken})
				if (psConflict[0] in pvConflict):
					pvConflict.remove(psConflict[0])
				if (psConflict[0] in sbsConflict):
					sbsConflict.remove(psConflict[0])
			elif (len(psConflict)==0):
				psDone=True
				ans.append({'reqName':'Physical Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one physical science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/ps.html','courseDone':psConflict, 'courseLeft':psNotTaken})
		if (not sbsDone):
			if (len(sbsConflict)==1):
				sbsDone=True
				ans.append({'reqName':'Social and Behavioral Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one social or behavioral science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html','courseDone':sbsConflict, 'courseLeft':sbsNotTaken})
				if (sbsConflict[0] in pvConflict):
					pvConflict.remove(sbsConflict[0])
				if (sbsConflict[0] in psConflict):
					psConflict.remove(sbsConflict[0])
			elif (len(sbsConflict)==0):
				sbsDone=True
				ans.append({'reqName':'Social and Behavioral Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one social or behavioral science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html','courseDone':sbsConflict, 'courseLeft':sbsNotTaken})	
	if(not pvDone):
		ans.append({'reqName':'Philosophy and Values Breadth', 'reqCompleted':True, 'reqDescription':'You must take one philosophy and values course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/pv.html','courseDone':pvConflict, 'courseLeft':pvNotTaken})
		if (pvConflict[0] in psConflict):
			psConflict.remove(pvConflict[0])
		if (pvConflict[0] in sbsConflict):
			sbsConflict.remove(pvConflict[0])
	for i in range(0,2):
		if (not psDone):
			if (len(psConflict)==1):
				psDone=True
				ans.append({'reqName':'Physical Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one physical science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/ps.html','courseDone':psConflict, 'courseLeft':psNotTaken})
				if (psConflict[0] in sbsConflict):
					sbsConflict.remove(psConflict[0])
			elif (len(psConflict)==0):
				psDone=True
				ans.append({'reqName':'Physical Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one physical science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/ps.html','courseDone':psConflict, 'courseLeft':psNotTaken})
		if (not sbsDone):
			if (len(sbsConflict)==1):
				sbsDone=True
				ans.append({'reqName':'Social and Behavioral Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one social or behavioral science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html','courseDone':sbsConflict, 'courseLeft':sbsNotTaken})
				if (sbsConflict[0] in psConflict):
					psConflict.remove(sbsConflict[0])
			elif (len(sbsConflict)==0):
				sbsDone=True
				ans.append({'reqName':'Social and Behavioral Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one social or behavioral science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html','courseDone':sbsConflict, 'courseLeft':sbsNotTaken})	
	if(not psDone):
		ans.append({'reqName':'Physical Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one physical science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/ps.html','courseDone':psConflict, 'courseLeft':psNotTaken})
		if (psConflict[0] in sbsConflict):
			sbsConflict.remove(psConflict[0])
	if (not sbsDone):
		if (len(sbsConflict)==0):
			sbsDone=True
			ans.append({'reqName':'Social and Behavioral Science Breadth', 'reqCompleted':False, 'reqDescription':'You must take one social or behavioral science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html','courseDone':sbsConflict, 'courseLeft':sbsNotTaken})	
		else:
			sbsDone=True
			ans.append({'reqName':'Social and Behavioral Science Breadth', 'reqCompleted':True, 'reqDescription':'You must take one social or behavioral science course. For more info see: http://ls-advise.berkeley.edu/requirement/breadth7/sbs.html','courseDone':sbsConflict, 'courseLeft':sbsNotTaken})	
		
	return ans

def abbreviateMajor(major):
	abr = {'EECS':'Electrical Engineering & Computer Sciences',
	'BIOENG':'Bioengineering', 'CIVENG':'Civil & Environmental Engineering', 'COENG':'Computational Engineering Science',
	'ENENG':'Energy Engineering', 'ENGMS':'Engineering Mathematics & Statistics',
	'ENVENG':'Environmental Engineering Science',
	'ENGP':'Engineering Physics','INDENG':'Industrial Engineering & Operations Research',
	'MATSCI':'Materials Science & Engineering', 'MECENG':'Mechanical Engineering',
	'NUCENG':'Nuclear Engineering', 'BIOMATSCI':'Bioengineering/Materials Science & Engineering',
	'EECSMATSCI':'Materials Science & Engineering/Electrical Engineering & Computer Sciences',
	'EECSNUCENG':'Nuclear Engineering/Electrical Engineering & Computer Sciences',
	'MATMECENG':'Materials Science & Engineering/Mechanical Engineering',
	'MATNUCENG':'Materials Science & Engineering/Nuclear Engineering',
	'MECNUCENG':'Nuclear Engineering/Mechanical Engineering',

	'CRS':'Conservation & Resource Studies', 'ES':'Environmental Sciences',
	'FNR':'Forestry & Natural Resources','GPB': 'Genetics & Plant Biology',
	'MB':'Microbial Biology','MEB':'Molecular & Environmental Biology',
	'MT':'Molecular Toxicology','NSPM':'Nutritional Science (Physiology)', 
	'NSD':'Nutritional Science (Dieletics)', 'SE':'Society & Environment',

	'BSCHEM':'Chemistry B.S.','BACHEM':'Chemistry B.A.',
	'CHEMENG':'Chemical Engineering', 'CHEMBIO':'Chemical Biology',
	'CHEMMATSCI':'Chemical Engineering/Materials Science & Engineering',
	'CHEMNUCENG':'Chemical Engineering/Nuclear Engineering',

	'ARCH':'Architecture', 'LDARCH':'Landscape Architecture',
	'URDES':'Urban Studies', 'SENVDES':'Sustainable Environmental Design',

	'UGBA':'Business Administration',

	'AMERSTD':'American Studies','AENEAA':'Ancient Egyptian & Near Eastern Art & Archaeology',
	'ASIANST': 'Asian Studies', 'COGSCI': 'Cognitive Science', 'DEVSTD':'Development Studies',
	'ISF': 'Interdisciplinary Studies', 'LATAMST':'Latin American Studies', 'LEGALST':'Legal Studies',
	'MEDIAST': 'Media Studies', 'MESTU':'Middle Eastern Studies', 'PACS':'Peace & Conflict Studies',
	'POLECON':'Political Economy','RELIGST':'Religious Studies', 'AFRICAM':'African American Studies',
	'ANTHRO':'Anthropology', 'ASAMDST':'Asian American & Asian Diaspora Studies',
	'CHICANO': 'Chicano Studies','ECON':'Economics', 'EEP':'Environmental Economics & Policy',
	'ETHSTD':'Ethnic Studies', 'GWS':"Gender & Women's Studies", 'GEOG':'Geography', 'HISTORY':'History',
	'LINGUIS':'Linguistics', 'NATAMS':'Native American Studies', 'POLSCI':'Political Science',
	'PSYCH':'Psychology', 'SOCWEL':'Social Welfare', 'SOCIOL':'Sociology', 'ASTRON':'Astronomy',
	'CHEM':'Chemistry', 'COMPSCI':'Computer Science', 'EPS':'Earth & Planetary Science',
	'AMATH':'Mathematics, Applied', 'MATH':'Mathematics', 'OPER':'Operations Research & Management Science',
	'PHYSSCI':'Physical Sciences', 'PHYSICS':'Physics', 'STAT':'Statistics', 'INTEGBI':'Integrative Biology',
	'MCELLBI':'Molecular & Cell Biology', 'PBHLTH':'Public Health', 'HISTART':'Art, History of',
	'ART':'Art, Practice of', 'CELTIC':'Celtic Studies', 'CLASSCIV':'Classical Civilizations',
	'COMLIT':'Comparative Literature','CLASSLANG':'Classical Languages',
	'EALANG':'East Asian Languages & Cultures', 'ENGLISH':'English', 'FILM':'Film & Media',
	'FRENCH':'French', 'GERMAN':'German', 'ITALIAN':'Italian Studies','MUSIC':'Music',
	'NECIV':'Near Eastern Civilizations','PHILOS':'Philosophy', 'RHETOR':'Rhetoric', 'SCANDIN':'Scandinavian',
	'SLAVIC':'Slavic Languages & Literatures', 'SEASN':'South & Southeast Asian Studies',
	'SPANISH':'Spanish & Spanish American', 'DANCE':'Dance & Performance Studies',
	'ASTRO':'Astrophysics','BMBIO':'Biochemistry & Molecular Biology','CDBIO':'Cell & Developmental Biology',
	'CHIN':'Chinese','DUTCH':'Dutch Studies','GGD':'Genetics, Genomics & Development',
	'GREEK':'Greek','HLBI':'Hispanic Languages & Bilingual Issues','ILAL':'Iberian or Latin American Literatures',
	'IMMPATH':'Immunology & Pathology','NEURO':'Neurobiology','THEATER':'Theater & Performance Studies',
	'JAP':'Japanese','LATIN':'Latin','LB':'Luso-Brazilian','NELL':'Near Eastern Languages & Literature'}
	abr = dict (zip(abr.values(),abr.keys()))
	return abr[major.replace(' and ',' & ')]

def abbreviateCollege(college):
	abr = {"College of Engineering":'Engineering',"College of Chemistry":'Chemistry','College of Natural Resources':"NaturalResources",'College of Letters and Science':"LettersAndSciences",'Haas School of Business':"Haas",'College of Environmental Design':"EnvironmentalDesign"}
	return abr[college]

"""
if college is Chemistry then major is in {BSCHEM:'Bachelor of Science Degree in Chemistry',
	CHEMENG:'Chemical Engineering', CHEMBIO:'Chemical Biology', BACHEM:'Bachelor of Arts Degree in Chemistry'
	CHEMMATSCI:'Chemical Engineering and Materials Science and Engineering',
	CHEMNUCENG:'Chemical Engineering and Nuclear Engineering'}
if college is NaturalResources then major is in {}
if college is LettersAndSciences then major is in {AMERSTD:'American Studies'
	ASIANST: 'Asian Studies', COGSCI: 'Cognitive Science', DEVSTD:'Development Studies',
	ISF: 'Interdisciplinary Studies', LATAMST:'Latin American Studies', LEGALST:'Legal Studies',
	MEDIAST: 'Media Studies', MESTU:'Middle Eastern Studies', PACS:'Peace and Conflict Studies',
	POLECON:'Political Economy',RELIGST:'Religious Studies', AFRICAM:'African American Studies',
	ANTHRO:'Anthropology', ASAMDST:'Asian American and Asian Diaspora Studies',
	CHICANO: 'Chicano Studies',ECON:'Economics', ENVECON:'Environmental Economics',
	ETHSTD:'Ethnic Studies', GWS:'Gender & Women's Studies', GEOG:'Geography', HISTORY:'History',
	LINGUIS:'Linguistics', NATAMS:'Native American', POLSCI:'Political Science',
	PSYCH:'Psychology', SOCWEL:'Social Welfare', SOCIOL:'Sociology', ASTRON:'Astronomy',
	CHEM:'Chemistry', COMPSCI:'Computer Science', EPS:'Earth and Planetary Science',
	AMATH:'Applied Mathematics', PMATH:'Pure Mathematics', OPER:'Operations Research and Management',
	PHYSSCI:'Physical Sciences', PHYSICS:'Physics', STAT:'Statistics', INTEGBI:'Integrative Biology',
	MCELLBI:'Molecular and Cell Biology', PBHLTH:'Public Health', HISTART:'History of Art',
	ART:'Practice of Art', CELTIC:'Celtic Studies', CLASSIC:'Classics', COMLIT:'Comparative Literature',
	EALANG:'East Asian Languages and Cultures', ENGLISH:'English', FILM:'Film',
	FRENCH:'French', GERMAN:'German', ITALIAN:'Italian Studies',MUSIC:'Music',
	NESTUD:'Near Eastern Studies',PHILOS:'Philosophy', RHETOR:'Rhetoric', SCANDIN:'Scandinavian',
	SLAVIC:'Slavic Languages and Literatures', SEASN:'South and Southeast Asian Studies',
	SPANISH:'Spanish and Portuguese', THEATER:'Theater, Dance, and Performance Studies'}
if college is Haas then major is in {UGBA:'Undergraduate Business Administration'}
if college is EnvironmentalDesign then major is in {ARCH:'Architecture', CYPLAN:'City and Regional Planning',
	LDARCH:'Landscape Architecture and Environmental Planning', URDES:'Urban Design',
	SENVDES:'Sustainable Environmental Design'}
"""
def remainingRequirements(takenClasses, college, major):
	major = abbreviateMajor(major)
	college = abbreviateCollege(college)
	ans = [];
	# University Requirements: Common for everyone
	#American Cultures
	ac=False
	for item in takenClasses:
		if 'AC' in item:
			ac=True
	if ac:
		ans.append({'reqName':'American Cultures', 'reqCompleted':True, 'reqDescription':"Take at least one course labeled AC",'courseDone':[], 'courseLeft':[]})
	else:
		ans.append({'reqName':'American Cultures', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled AC",'courseDone':[], 'courseLeft':[]})
	#120 units
	unit=0
	for item in takenClasses:
		unit+=units(item)
	if unit>=120:
		ans.append({'reqName':'Unit Requirement', 'reqCompleted':True, 'reqDescription':"Complete at least 120 units",'courseDone':[], 'courseLeft':[]})
	else:
		ans.append({'reqName':'Unit Requirement', 'reqCompleted':False, 'reqDescription':"Complete at least 120 units",'courseDone':[], 'courseLeft':[]})
	#American Institutions and History
	ans.append({'reqName':'American Institutions and History', 'reqCompleted':True, 'reqDescription':"This requirement is usually satisfied before coming to UC Berkeley. See http://registrar.berkeley.edu/?PageID=ahi.html for more information",'courseDone':[], 'courseLeft':[]})
	#Entry Level Writing
	ans.append({'reqName':'Entry Level Writing', 'reqCompleted':True, 'reqDescription':"This requirement is usually satisfied before coming to UC Berkeley but can be fulfilled by taking a placement exam. See http://writing.berkeley.edu/classes-and-awp/awp-exam for more information",'courseDone':[], 'courseLeft':[]})
	#Residency
	ans.append({'reqName':'Residency', 'reqCompleted':True, 'reqDescription':"There are residency requirements placed on students but our program is not capabale of checking if they are fulfilled. See http://ls-advise.berkeley.edu/requirement/summary.html for more information",'courseDone':[], 'courseLeft':[]})
	# College of Engineering
	if(college=='Engineering'):
		# College Requirements
		#Reading and Composition
		OneA=False
		OneB=False
		for item in takenClasses:
			if 'R1A' in item:
				OneA=True
			if 'R1B' in item:
				OneB=True
		if (OneA and OneB):
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':True, 'reqDescription':"Take at least one course labeled R1A and R1B",'courseDone':[], 'courseLeft':[]})
		elif (OneA):
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled R1A and R1B. You have completed R1A",'courseDone':[], 'courseLeft':[]})
		elif (OneB):
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled R1A and R1B. You have completed R1B",'courseDone':[], 'courseLeft':[]})
		else:
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled R1A and R1B",'courseDone':[], 'courseLeft':[]})
		#Electives: Humanities / Social Studies
		#A minimum of six courses from the approved Humanities/Social Sciences (H/SS) lists.
		#At least two of the courses must be upper division (courses numbered 100--196.)
		#At  least two of the courses must be from the same department and at least one of  the two must be upper division. (*Series)
		#No courses offered by an Engineering  department (IEOR, CE, etc.) other than BIOE 100, COMPSCI C79,  ENGIN 125, ENGIN 130AC,  and ME 191AC may be used to complete H/SS requirements.
		ans.append({'reqName':'Electives: Humanities / Social Studies', 'reqCompleted':True, 'reqDescription':"A minimum of six courses from the approved Humanities/Social Sciences (H/SS) lists. At least two of the courses must be upper division (courses numbered 100--196.) At  least two of the courses must be from the same department and at least one of  the two must be upper division.",'courseDone':[], 'courseLeft':[]})
		# Electrical Engineering & Computer Sciences
		if(major=='EECS'):
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Computer Science 70
			ans.append(basicReq(takenClasses, 'COMPSCI.70', 'CS 70', "The sophomore year Discrete Math requirement"))
			#Physics 7C or H7C,Chemistry 1A and 1AL, Chemistry 1B, 3A, 3B , 4A, 4B or 5.Biology 1A/1AL, Biology 1B, Astronomy 7A or B,Molecular and Cell Biology 32/32L
			nat={'PHYSICS.7C':'Physics 7C','CHEM.1A':'Chem 1A','CHEM.1B':'Chem 1B','CHEM.3A':'Chem 3A','CHEM.3B':'Chem 3B','CHEM.4A':'Chem 4A','CHEM.4B':'Chem 4B','CHEM.5':'Chem 5','BIOLOGY.1A':'Bio 1A','BIOLOGY.1B':'Bio 1B','ASTRO.7A':'Astro 7A','ASTRO.7B':'Astro 7B','MCELLBI.32':'MCB 32'}
			ans.append(manyChoiceReq(takenClasses, 'Natural Science', nat, "Requirement of one of Physics 7C or H7C,Chemistry 1A and 1AL, Chemistry 1B, 3A, 3B , 4A, 4B or 5.Biology 1A/1AL, Biology 1B, Astronomy 7A or B,Molecular and Cell Biology 32/32L"))
			#45 units of technical engineering courses comprised of at least 20 units of upper-division EECS courses
			num=0
			for item in takenClasses:
				if((re.search(r'ELENG.1\d\d',item))or((re.search(r'COMPSCI.1\d\d',item)))):
					num+=units(item)
			if (num>=20):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 20 units of upper-division EECS courses",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"At least 20 units of upper-division EECS courses. "+"You have only taken "+str(num),'courseDone':[], 'courseLeft':[]})

			#Not courses numbered 24, 39, 84; BioE 100; CS C79, CS 195, CSH195; Engin 125, 130AC, 140; IEOR 172, IEOR 190 series; IEOR 191; ME 191AC, 190K; 191K
			#15 units of upper division courses in engineering.  Not courses numbered 24, 39, 84; BioE 100; CS C79, CS 195, CS H195, Engin 125; 130 AC, 140, IEOR 172, IEOR 190 series; IEOR 191; and ME 191AC, 190K; 191K.
			num=0
			for item in takenClasses:
				if ((('ENG' in item)or ('COMPSCI' in item)or('MATSCI'in item)or ('NSE' in item))and (not (('ENGLISH' in item)or ('.24' in item)or ('.39' in item)or ('.84' in item)or ('BIOENG.100' in item)or ('COMPSCI.C79' in item)or ('COMPSCI.195' in item)or ('COMPSCI.H195' in item)or ('ENGIN.125' in item)or ('ENGIN.130AC' in item)or ('ENGIN.140' in item)or ('INDENG.172' in item)or ('INDENG.190' in item)or ('INDENG.191' in item)or ('MECENG.191AC' in item)or ('MECENG.190K' in item)or ('MECENG.191K' in item)))):
					num+=units(item)
			if (num>=15):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"15 units of upper division courses in engineering.  Not courses numbered 24, 39, 84; BioE 100; CS C79, CS 195, CS H195, Engin 125; 130 AC, 140, IEOR 172, IEOR 190 series; IEOR 191; and ME 191AC, 190K; 191K.",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"15 units of upper division courses in engineering.  Not courses numbered 24, 39, 84; BioE 100; CS C79, CS 195, CS H195, Engin 125; 130 AC, 140, IEOR 172, IEOR 190 series; IEOR 191; and ME 191AC, 190K; 191K."+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			"""advancement"""
			#EE 20N-Structure and Interpretation of Systems and Signals
			ans.append(basicReq(takenClasses, 'ELENG.20N', 'EE 20N', "The sophomore year Structure and Interpretation of Systems and Signals requirement"))
			#EE 40-Introduction to Microelectronic Circuits
			ans.append(basicReq(takenClasses, 'ELENG.40', 'EE 40',  "The sophomore year Electrical Engineering requirement"))
			#Computer Science 61B, Data Structures
			ans.append(basicReq(takenClasses, 'COMPSCI.61B', 'CS 61B', "The sophomore year Programming Data Structures requirement"))
			#CS 61A-Structure and Interpretation of Computer Programs
			ans.append(basicReq(takenClasses, 'COMPSCI.61A', 'CS 61A', "The freshman year Structure and Interpretation of Computer Programs requirement"))
			#CS 61C-Machine Structures
			ans.append(basicReq(takenClasses, 'COMPSCI.61C','CS 61C', "The junior year Machine Structures requirement"))
			#Ethics Requirement:CS 195, CS H195, ERG 100 or ERG C100, ISF 60 ISF 100D
			ethic={'COMPSCI.195':'CS 195','COMPSCI.H195':'CS H195','ENERES.100':'ERG 100','ENERES.C100':'ERG C100','ISF.100D':'ISF 100D'}
			ans.append(manyChoiceReq(takenClasses, 'Ethics Requirement', ethic, "One required elective with an emphasis on ethics"))
			#Design Requirement:EE C125, C128, 130, 140, 141, 143, C149, 192,CS C149, 150, 160, 162, 164, 169, 184, 186 A course in other engineering departments having substantial engineering design content can be substituted by petition.
			design={'ELENG.C125':'EE C125','ELENG.C128':'EE C128','ELENG.130':'EE 130','ELENG.140':'EE 140','ELENG.141':'EE 141','ELENG.143':'EE 143','ELENG.C149':'EE C149','ELENG.192':'EE 192','COMPSCI.C149':'CS C149','COMPSCI.150':'CS 150','COMPSCI.160':'CS 160','COMPSCI.162':'CS 162','COMPSCI.164':'CS 164','COMPSCI.169':'CS 169','COMPSCI.184':'CS 184','COMPSCI.186':'CS 186'}
			"""advancement"""
			ans.append(manyChoiceReq(takenClasses, 'Design Requirement', design, "One required design class from the list **A course in other engineering departments having substantial engineering design content can be substituted by petition"))
			return ans
		# BioEngineering
		elif(major=='BIOENG'):
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Chemistry 3A and 3AL , or Chem 112A
			if(('CHEM.3A' in takenClasses) and ('CHEM.3AL' in takenClasses)):
				ans.append({'reqName':'Organic Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Organic Chemistry requirement",'courseDone':['Chem 3A', 'Chem 3AL'], 'courseLeft':['Chem 112A']})
			elif('CHEM.112A' in takenClasses):
				ans.append({'reqName':'Organic Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Organic Chemistry requirement",'courseDone':['Chem 112A'], 'courseLeft':['Chem 3A', 'Chem 3AL']})
			else:
				ans.append({'reqName':'Organic Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Organic Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 3A', 'Chem 3AL','Chem 112A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#BioE 10
			ans.append(basicReq(takenClasses, 'BIOENG.10', 'BioE 10', "The freshman year requirement of BioE"))
			#E 7 , Introduction to Applied Computing or CS 61A
			ans.append(twoChoiceReq(takenClasses,"Introduction to Applied Computing", 'ENGIN.7', 'E 7', 'COMPSCI.61A', 'CompSci 61A', "The freshman year Introduction to Applied Computing requirement of either E 7 or CS 61A"))
			#Freshman Seminar: BioE 24 and BioE 25
			ans.append( twoReq(takenClasses,'Freshman Seminar', 'BIOENG.24', 'BioE 24', 'BIOENG.25', 'BioE 25', "The freshman year bioengineering seminar requirement of both BioE 24 and 25"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append( twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Biology 1A & 1AL , General Biology
			ans.append( twoReq(takenClasses,'General Biology', 'BIOLOGY.1A', 'Bio 1A', 'BIOLOGY.1AL', 'Bio 1AL', "The sophomore year biology requirement of both Bio 1A and 1AL"))
			#Engineering/Biology Preparation
			bioprep= {'ENGIN.45':'E 45', 'ELENG.20N':'EE 20N', 'ELENG.40':'EE 40','ELENG.100':'EE 100','CHEM.120B':'Chem 120B','BIOENG.C105B':'BioE C105B','CHEM.C130':'Chem C130','MCELLBI.100A':'MCB 100A', 'CIVENG.C30':'CE C30','MECENG.C85':'ME C85','COMPSCI.61B':'CompSci 61B','COMPSCI.61BL':'CompSci 61BL'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'Engineering/Biology Preparation', bioprep, "Sophomore year engineering or biology preparation requireing two classes from the given list",2))
			#Bioengineering Design Project
			design={'BIOENG.121L':'BioE 121L','BIOENG.140L':'BioE 140L','BIOENG.168L':'BioE 168L','BIOENG.192':'BioE 192','BIOENG.H194':'BioE H194','BIOENG.196':'BioE 196'}
			ans.append(manyChoiceReq(takenClasses, 'Bioengineering Design Project', design, "The senior year requirement of a Bioengineering Design Project or research"))
			#Upper Division Biology Elective
			bioelec={'CHEM.130':'Chem 130desi', 'CHEM.135':'Chem 135', 'INTEGBI.115':'IB 115', 'INTEGBI.127':'IB 127', 'INTEGBI.131':'IB 131', 'INTEGBI.132':'IB 132', 'INTEGBI.135':'IB 135', 'INTEGBI.148':'IB 148', 'INTEGBI.163':'IB 163', 'MCELLBI.C100A':'MCB C100A', 'MCELLBI.100B':'MCB 100B', 'MCELLBI.102':'MCB 102', 'MCELLBI.110':'MCB 110', 'MCELLBI.111':'MCB 111', 'MCELLBI.C112':'MCB C112', 'MCELLBI.130A':'MCB 130A', 'MCELLBI.132':'MCB 132', 'MCELLBI.133L':'MCB 133L', 'MCELLBI.136':'MCB 136', 'MCELLBI.140':'MCB 140', 'MCELLBI.140L':'MCB 140L', 'MCELLBI.C145':'MCB C145', 'MCELLBI.C148':'MCB C148', 'MCELLBI.150':'MCB 150', 'PLANTBI.C112':'PMB C148', 'PLANTBI.C148':'PMB C148', 'MCELLBI.C160':'MCB C160', 'NEUROSC.C160':'NeuroScience C160', 'MCELLBI.160L':'MCB 160L', 'MCELLBI.166':'MCB 166', 'PLANTBI.185':'PMB 185'}
			belec=0
			for key in bioelec:
				if key in takenClasses:
					belec+=1
			ans.append(manyChoiceReq(takenClasses, 'Upper Division Biology Elective', bioelec, "The junior year requirement of an upper division biology elective"))
			#BioE 100 or Humanities / Social Studies course with ethics content
			ethics={'ANTHRO.156B':'Anthro 156B','BIOENG.100':'BioE 100','ENGIN.125':'E 125','ESPM.161':'ESPM 161','ESPM.162':'ESPM 162','LNS.160B':'L&S 160B','PHILOS.2':'Philo 2','PHILOS.104':'Philo 104','PHIMOS.107':'Philo 107','PBHLTH.116':'Public Health 116'}
			ans.append(manyChoiceReq(takenClasses, 'Ethics Requirement', ethics, "The junior year requirement of a course with ethics content"))
			#Bioengineering Fundamentals- 2
			biofund={'BIOENG.101':'BioE 101','BIOENG.102':'BioE 102','BIOENG.104':'BioE 104','BIOENG.110':'BioE 110','BIOENG.116':'BioE 116','BIOENG.131':'BioE 131','BIOENG.150':'BioE 150'}
			fund=0
			for key in biofund:
				if key in takenClasses:
					fund+=1
			if fund>=2:
				ans.append({'reqName':'Bioengineering Fundamentals', 'reqCompleted':True, 'reqDescription':"Two classes from the given list",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Bioengineering Fundamentals', 'reqCompleted':False, 'reqDescription':"Two classes from the given list",'courseDone':[], 'courseLeft':[]})
			#Bioengineering Lab Course
			biolab={'BIOENG.22L':'BioE 22L','BIOENG.101':'BioE 101','BIOENG.115':'BioE 115','BIOENG.121L':'BioE 121L','BIOENG.C136L':'BioE C136L','BIOENG.140L':'BioE 140L','BIOENG.C144L':'BioE C144L','BIOENG.C145L':'BioE C145L','BIOENG.C145M':'BioE C145M','BIOENG.163L':'BioE 163L','BIOENG.168L':'BioE 168L'}
			lab=0
			overlap=('BIOENG.101'in takenClasses)
			simple=('BIOENG.22L'in takenClasses)
			for key in biolab:
				if key in takenClasses:
					lab+=1
			if((not overlap) and (lab>=1))or(overlap and (lab>=2)):
				ans.append({'reqName':'Bioengineering Lab', 'reqCompleted':True, 'reqDescription':"One lab course from the given list",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Bioengineering Lab', 'reqCompleted':False, 'reqDescription':"One lab course from the given list",'courseDone':[], 'courseLeft':[]})
			#Bioengineering Topics-2
			# two off the list but the list includes the fundamentals
			biotopic={'BIOENG.111':'BioE 111','BIOENG.112':'BioE 112','BIOENG.113':'BioE 113','BIOENG.C117':'BioE C117','BIOENG.C118':'BioE C118','BIOENG.C119':'BioE C119','BIOENG.121':'BioE 121','BIOENG.C125':'BioE C125','BIOENG.132':'BioE 132','BIOENG.135':'BioE 135','BIOENG.C144':'BioE C144','BIOENG.C146':'BioE C146','BIOENG.147':'BioE 147','BIOENG.148':'BioE 148','BIOENG.151':'BioE 151','BIOENG.163':'BioE 163','BIOENG.164':'BioE C164','BIOENG.C165':'BioE C165','BIOENG.C181':'BioE C181','BIOENG.190A':'BioE 190A','BIOENG.190B':'BioE 190B','BIOENG.190C':'BioE 190C','BIOENG.190D':'BioE 190D','BIOENG.190E':'BioE 190E','BIOENG.190F':'BioE 190F','BIOENG.190G':'BioE 190G','BIOENG.190H':'BioE 190H'}
			topic=0
			for key in biotopic:
				if key in takenClasses:
					topic+=1
			if (not overlap):
				topic+=fund
				topic+=lab
				topic-=3
			else:
				topic+=fund
				topic+=lab
				topic-=4
			if topic>=2:
				ans.append({'reqName':'Bioengineering Topics', 'reqCompleted':True, 'reqDescription':"Two classes from the given list",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Bioengineering Topics', 'reqCompleted':False, 'reqDescription':"Two classes from the given list",'courseDone':[], 'courseLeft':[]})
			#Engineering Topic-1
			engtopic={'BIOENG.192':'BioE 192' ,'BIOENG.H194':'BioE H194' ,'BIOENG.196':'BioE 196' , 'CHMENG.140':'Chem E 140', 'CHMENG.141':'Chem E 141' ,'CHMENG.150A':'Chem E 150A' , 'CHMENG.150B':'Chem E 150B' , 'CHMENG.170A':'Chem E 170A' , 'CHMENG.170B':'Chem E 170B' , 'CHMENG.170L':'Chem E 170L' , 'CHMENG.171':'Chem E 171' ,'CHMENG.C178':'Chem E C178' , 'CIVENG.C30':'CE C30','MECENG.C85':'ME C85','CIVENG.130N':'CE 130N' ,'COMPSCI.61A':'CS 61A' , 'COMPSCI.61B':'CS 61B' ,'COMPSCI.61BL':'CS 61BL' ,'COMPSCI.170':'CS 170','COMPSCI.186':'CS 186','COMPSCI.191':'CS 191','PHYSICS.C191':'Physics C191' ,'ENGIN.7':'E 7', 'ENGIN.115':'E 115', 'ENGIN.170':'E 170', 'ENGIN.190':'E 190','ELENG.20N':'EE 20N','ELENG.40':'EE 40','ELENG.100':'EE 100','ELENG.105':'EE 105','ELENG.117':'EE 117','ELENG.120':'EE 120','ELENG.126':'EE 126','ELENG.129':'EE 129','ELENG.142':'EE 142','ELENG.143':'EE 143','ELENG.192':'EE 192','INDENG.162':'IEOR 162','MECENG.102B':'ME 102B','MECENG.104':'ME 104','MECENG.106':'ME 106','MECENG.109':'ME 109','MECENG.118':'ME 118','MECENG.119':'ME 119','MECENG.128':'ME 128','MECENG.132':'ME 132','MECENG.133':'ME 133', 'MECENG.167':'ME 167','MECENG.185':'ME 185','MATSCI.102':'MSE 102','MATSCI.104':'MSE 104','MATSCI.111':'MSE 111','MATSCI.113':'MSE 113','MATSCI.151':'MSE 151','NUCENG.101':'NE 101','NUCENG.107':'NE 107', 'NUCENG.170B':'NE 170B'}
			eng=0
			for key in engtopic:
				if key in takenClasses:
					eng+=1
			eng+=topic
			eng-=2
			if eng>=1:
				ans.append({'reqName':'Engineering Topic', 'reqCompleted':True, 'reqDescription':"One class from the given list",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Engineering Topic', 'reqCompleted':False, 'reqDescription':"One class from the given list",'courseDone':[], 'courseLeft':[]})
			#Technical Electives-3
			elec=eng-1
			elec+=(belec-1)
			techelec={'BIOLOGY.1B':'Bio 1B','CHEM.3B':'Chem 3B' , 'CHEM.120A':'Chem 120A','CHEM.120B': 'Chem 120B' ,'CHEM.C130':'Chem C130','MCELLBI.C100A':'MCB C100A','CHEM.130B':'Chem 130B' ,'COMPSCI.70':'CS 70' ,'MATH.55': 'Math 55','MATH.110':'Math 110' ,'MATH.118':'Math 118', 'MATH.127':'Math 127' ,'MATH.128A':'Math 128A' , 'MATH.170':'Math 170' ,  'NUSCTX.121':'NutriSci 121' , 'PHYSICS.7C': 'Physics 7C', 'PHYSICS.110A':'Physics 110A' , 'PHYSICS.112': 'Physics 112','PHYSICS.137A':'Physics 137A' , 'PHYSICS.177':'Physics 177', 'PHYSICS.C191':'Physics C191' , 'PBHLTH.143':'Public Health 143' , 'STAT.133':'Stata 133' ,'STAT.134':'Stats 134', 'INDENG.172':'IEOR 172', 'STAT.135':'Stats 135' , 'STAT.150': 'Stats 150'}
			for key in techelec:
				if key in takenClasses:
					elec+=1
			if elec>=3:
				ans.append({'reqName':'Technical Electives', 'reqCompleted':True, 'reqDescription':"Three classes from the given list",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Electives', 'reqCompleted':False, 'reqDescription':"Three classes from the given list",'courseDone':[], 'courseLeft':[]})
			return ans
		# Civil and Environmental Engineering
		elif(major=='CIVENG'):
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#E 7 - Introduction to Applied Computing
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7', "The sophomore year Introduction to Computer Programming requirement"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Basic Science Breadth Elective (Bio 1B or CE 70)
			ans.append(twoChoiceReq(takenClasses,'Basic Science Breadth Elective', 'BIOLOGY.1B', 'Bio 1B', 'CIVENG.70','CivEng 70', "The freshman year Basic Science Breadth Elective requirement of Bio 1B and CE 70"))
			#CE 92 - Introduction to Civil & Environmental Engineering
			ans.append(basicReq(takenClasses, 'CIVENG.92', 'CivEng 92', "The freshman year Introduction to Civil & Environmental Engineering requirement of CE 92"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Either Chem 1B: General Chemistry, OR Chem 4B General Chemistry and Quantitative Analysis OR Physics 7C: Physics for Scientists & Engineers
			science={'CHEM.1B':'Chem 1B','CHEM.4B':'Chem 4B','PHYSICS.7C':'Physics 7C'}
			ans.append(manyChoiceReq(takenClasses, 'Basic Science', science, "Either Chem 1B: General Chemistry, OR Chem 4B General Chemistry and Quantitative Analysis OR Physics 7C: Physics for Scientists & Engineers"))
			#CE C30/ME C85
			ans.append(twoChoiceReq(takenClasses,'Introduction to Solid Mechanics', 'MECENG.C85', 'MecEng C85','CIVENG.C30','CivEng C30', "The sophomore year Introduction to Solid Mechanics requirement"))
			#CE 60 - Structure & Properties of Civil Engineering Materials
			ans.append(basicReq(takenClasses, 'CIVENG.60', 'CivEng 60', "The sophomore year Structure & Properties of Civil Engineering Materials requirement of CE 60"))
			#Engineering Elective CE 11 or CE 70
			ans.append(twoChoiceReq(takenClasses,'Engineering Sophomore Elective', 'CIVENG.11', 'CivEng 11','CIVENG.70','CivEng 70', "The sophomore year Engineering Sophomore Elective requirement"))
			#CE 93 - Engineering Data Analysis
			ans.append(basicReq(takenClasses, 'CIVENG.93', 'CivEng 93', "The sophomore year Engineering Data Analysis requirement of CE 93"))
			#CE 100 - Elementary Fluid Mechanics
			ans.append(basicReq(takenClasses, 'CIVENG.100', 'CivEng 100', "The junior year Elementary Fluid Mechanics requirement of CE 100"))
			#CE 130N
			ans.append(basicReq(takenClasses, 'CIVENG.130N', 'CivEng 130N', "The junior year Mechanics of Structures requirement of CE 130N"))
			#Engineering Science Electives
			engelec={'ENGIN.115':'E 115','MECENG.40':'MecEng 40','MECENG.104':'MecEng 104'}
			ans.append(manyChoiceReq(takenClasses, 'Engineering Science Elective', engelec, "One off the following list"))
			#Elective Core (four of the following seven): CE 103 - Hydrology (Spring) CE 111 - Environmental Engineering (Fall) CE 120 - Structural Engineering (Spring) CE 155 - Transportation Systems Engineering (Spring) CE 167 - Engineering Project Management (Fall) CE 175 - Geotechnical & Geoenvironmental Engineering (Fall & Spring) CE 191 - Civil & Environmental Systems Analysis (Fall)
			elco={'CIVENG.103':'CivEng 103','CIVENG.111':'CivEng 111','CIVENG.120':'CivEng 120','CIVENG.155':'CivEng 155','CIVENG.167':'CivEng 167','CIVENG.175':'CivEng 175','CIVENG.191':'CivEng 191'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'Elective Core', elco, "Elective Core (four of the following seven): CE 103 - Hydrology, CE 111 - Environmental Engineering, CE 120 - Structural Engineering, CE 155 - Transportation Systems Engineering, CE 167 - Engineering Project Management, CE 175 - Geotechnical & Geoenvironmental Engineering,CE 191 - Civil & Environmental Systems Analysis", 4))
			#CE 192 - Art & Science of Civil & Environmental Engineering Practice
			ans.append(basicReq(takenClasses, 'CIVENG.192', 'CivEng 192', "The senior year Art & Science of Civil & Environmental Engineering Practice requirement of CE 192"))
			#Engineering Electives: 15 additional units of upper-division technically oriented engineering coursework offered in the College of Engineering or in Chemical Engineering. BioE 100; CS 194, 195, C195; E 100, 110, C111, 124, 130AC, 140, 191, 193, 195, 196; EE 194, IEOR 172, 190 series; ME 106; Chem E 185.
			num=0
			notlist={'BIOENG.100', 'COMPSCI.194', 'COMPSCI.195', 'COMPSCI.C195', 'ENGIN.100', 'ENGIN.110', 'ENGIN.C111', 'ENGIN.124', 'ENGIN.130AC', 'ENGIN.140', 'ENGIN.191', 'ENGIN.193', 'ENGIN.195', 'ENGIN.196', 'ELENG.194', 'INDENG.172', 'INDENG.190A','INDENG.190B','INDENG.190C','INDENG.190D','INDENG.190E','INDENG.190F','INDENG.190G', 'MECENG.106', 'CHMENG.185'}
			for item in takenClasses:
				if((re.search(r'ENG.1\d\d',item))or(re.search(r'ENGIN.1\d\d',item))or(re.search(r'COMPSCI.1\d\d',item))or(re.search(r'MATSCI.1\d\d',item)))and (not re.search(r'ENGLISH.1\d\d',item))and (item not in notlist):
					num+=units(item)
			if num>=15:
				ans.append({'reqName':'Engineering Electives', 'reqCompleted':True, 'reqDescription':"Engineering Electives: 15 additional units of upper-division technically oriented engineering coursework offered in the College of Engineering or in Chemical Engineering. BioE 100; CS 194, 195, C195; E 100, 110, C111, 124, 130AC, 140, 191, 193, 195, 196; EE 194, IEOR 172, 190 series; ME 106; Chem E 185",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Engineering Electives', 'reqCompleted':False, 'reqDescription':"Engineering Electives: 15 additional units of upper-division technically oriented engineering coursework offered in the College of Engineering or in Chemical Engineering. BioE 100; CS 194, 195, C195; E 100, 110, C111, 124, 130AC, 140, 191, 193, 195, 196; EE 194, IEOR 172, 190 series; ME 106; Chem E 185",'courseDone':[], 'courseLeft':[]})
			#Design Electives
			deselec={'CIVENG.105':'CivEng 105','CIVENG.112':'CivEng 112','CIVENG.122N':'CivEng 122N','CIVENG.122L':'CivEng 122L','CIVENG.123N':'CivEng 123N','CIVENG.123L':'CivEng 123L','CIVENG.153':'CivEng 153','CIVENG.177':'CivEng 177','CIVENG.180':'CivEng 180','CIVENG.186':'CivEng 186'}
			ans.append(manyChoiceReq(takenClasses, 'Design Elective', deselec, "One of the following"))
			return ans
		# Computational Engineering Science
		elif(major=='COENG'):
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#UCB Chemistry 1A
			ans.append(basicReq(takenClasses, 'CHEM.1A', 'Chem 1A', "The freshman year General Chemistry requirement"))
			#UCB Engineering 10
			ans.append(basicReq(takenClasses, 'ENGIN.10', 'E 10', "The sophomore year Engineering Design and Analysis requirement"))
			#UCB  Engineering 7
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7', "The sophomore year Introduction to Computer Programming requirement"))
			#Three science electives from the following: UCB  Physics 7C; Chemistry 1B; Chemistry 3A/L; Chemistry 3B/L; Biology 1A/L; Biology 1B; Engineering 45
			science={'PHYSICS.7C':'Physics 7C','CHEM.1B':'Chem 1B','CHEM.3A':'Chem 3A','BIOLOGY.1A':'Bio 1A','BIOLOGY.1B':'Bio 1B','ENGIN.45':'E 45','CHEM.3B':'Chem 3B'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'Science Electives', science, "The sophomore year science elective requirement of three classes", 3))
			#One from the following: UCB  Math 55; Statistics 134; Math 110; Computer Science 70
			math={'MATH.55':'Math 55','STAT.134':'Stats 134','MATH.110':'Math 110','COMPSCI.70':'CS 70'}
			ans.append(manyChoiceReq(takenClasses, 'Advanced Math', math, "The sophomore year requirement of one more advanced math class"))
			#UCB  English 1A and 1B
			ans.append(twoReq(takenClasses,'English', 'ENGLISH.1A', 'English 1A','ENGLISH.1B', 'English 1B', "The freshman year English requirement of both English 1A and 1B"))
			#Engin 39B, Introduction to Computational Engineering Science (Freshman Seminar)
			ans.append(basicReq(takenClasses, 'ENGIN.39B', 'E 39B', "The freshman year Introduction to Computational Engineering Science (Freshman Seminar) requirement"))
			#Computer Science 61B, Data Structures
			ans.append(basicReq(takenClasses, 'COMPSCI.61B', 'CS 61B', "The sophomore year Programming Data Structures requirement"))
			#Math 128A, 128B, Numerical Analysis3
			ans.append(twoReq(takenClasses,'Numerical Analysis', 'MATH.128A', 'Math 128A','MATH.128B', 'Math 128B', "The junior year Numerical Analysis requirement of both Math 128A and 128B"))
			#Core Course 1-4: One course from each of four of the following eleven groups:
			#	Bioengineering: Bio Eng 153
			#	Electrical Engineering: El Eng 100, El Eng 120, El Eng 105, El Eng 130
			#	Electromagnetics: EECS 117A, Phys 110A
			#	Engineering Economics: Engin 120
			#	Fluid Mechanics: Mec Eng 106, Chem Eng 150A, Civ Eng 100
			#	Operations Research: Engin 102, Ind Eng 160
			#	Properties of Materials: Engin 45, Mat Sci 102, Mat Sci 111
			#	Quantum Mechanics: Phys 137A
			#	Solid State Electronics: El Eng 130, Phys 141A
			#	Statics/Dynamics: Mec Eng 104, Civ Eng 130, Phys 105
			#	Thermodynamics: Mec Eng 105, Eng 115, Chem Eng 141
			core=0
			coreTaken=[]
			coreNotTaken=[]
			if ('BIOENG.153' in takenClasses):
				core+=1
				coreTaken.append('BioE 153')
			else:
				coreNotTaken.append('BioE 153')
			if ('ENGIN.120' in takenClasses):
				core+=1
				coreTaken.append('E 120')
			else:
				coreNotTaken.append('E 120')
			if ('PHYSICS.137A' in takenClasses):
				core+=1
				coreTaken.append('Physics 137A')
			else:
				coreNotTaken.append('Physics 137A')
			ee={'ELENG.100':'EE 100','ELENG.120':'EE 120','ELENG.105':'EE 105','ELENG.130':'EE 130'}
			eeDone=False
			for key in ee:
				if key in takenClasses:
					eeDone=True
					coreTaken.append(ee[key])
				else:
					coreNotTaken.append(ee[key])
			if eeDone:
				core+=1
			em={'EECS.117A':'EECS 117A','PHYSICS.110A': 'Physics 110A'}
			emDone=False
			for key in em:
				if key in takenClasses:
					emDone=True
					coreTaken.append(em[key])
				else:
					coreNotTaken.append(em[key])
			if emDone:
				core+=1
			fm={'MECENG.106':'Mec Eng 106','CHMENG.150A': 'Chem Eng 150A','CIVENG.100': 'Civ Eng 100'}
			fmDone=False
			for key in fm:
				if key in takenClasses:
					fmDone=True
					coreTaken.append(fm[key])
				else:
					coreNotTaken.append(fm[key])
			if fmDone:
				core+=1
			ore={'ENGIN.102':'E 102','INDENG.160': 'IEOR 160'}
			oreDone=False
			for key in ore:
				if key in takenClasses:
					oreDone=True
					coreTaken.append(ore[key])
				else:
					coreNotTaken.append(ore[key])
			if oreDone:
				core+=1
			pm={'ENGIN.45':'E 45', 'MATSCI.102':'Mat Sci 102','MATSCI.111': 'Mat Sci 111'}
			pmDone=False
			for key in pm:
				if key in takenClasses:
					pmDone=True
					coreTaken.append(pm[key])
				else:
					coreNotTaken.append(pm[key])
			if pmDone:
				core+=1
			ss={'ELENG.130':'EE 130','PHYSICS.141A': 'Physics 141A'}
			ssDone=False
			for key in ss:
				if key in takenClasses:
					ssDone=True
					coreTaken.append(ss[key])
				else:
					coreNotTaken.append(ss[key])
			if ssDone:
				core+=1
			sd={'MECENG.104':'Mec Eng 104','CIVENG.130': 'Civ Eng 130','PHYSICS.105': 'Physics 105'}
			sdDone=False
			for key in sd:
				if key in takenClasses:
					sdDone=True
					coreTaken.append(sd[key])
				else:
					coreNotTaken.append(sd[key])
			if sdDone:
				core+=1
			td={'MECENG.105':'Mec Eng 105','ENGIN.115': 'E 115','CHMENG.141': 'Chem Eng 141'}
			tdDone=False
			for key in td:
				if key in takenClasses:
					tdDone=True
					coreTaken.append(td[key])
				else:
					coreNotTaken.append(td[key])
			if tdDone:
				core+=1
			if core>=4:
				ans.append({'reqName':'Core Course', 'reqCompleted':True, 'reqDescription':"One course from each of four of the following eleven groups:  Bioengineering: Bio Eng 153; Electrical Engineering: El Eng 100, El Eng 120, El Eng 105, El Eng 130; Electromagnetics: EECS 117A, Phys 110A; Engineering Economics: Engin 120; Fluid Mechanics: Mec Eng 106, Chem Eng 150A, Civ Eng 100; Operations Research: Engin 102, Ind Eng 160; Properties of Materials: Engin 45, Mat Sci 102, Mat Sci 111; Quantum Mechanics: Phys 137A; Solid State Electronics: El Eng 130, Phys 141A; Statics/Dynamics: Mec Eng 104, Civ Eng 130, Phys 105; Thermodynamics: Mec Eng 105, Eng 115, Chem Eng 141",'courseDone':coreTaken, 'courseLeft':coreNotTaken})
			else:
				ans.append({'reqName':'Core Course', 'reqCompleted':False, 'reqDescription':"One course from each of four of the following eleven groups:  Bioengineering: Bio Eng 153; Electrical Engineering: El Eng 100, El Eng 120, El Eng 105, El Eng 130; Electromagnetics: EECS 117A, Phys 110A; Engineering Economics: Engin 120; Fluid Mechanics: Mec Eng 106, Chem Eng 150A, Civ Eng 100; Operations Research: Engin 102, Ind Eng 160; Properties of Materials: Engin 45, Mat Sci 102, Mat Sci 111; Quantum Mechanics: Phys 137A; Solid State Electronics: El Eng 130, Phys 141A; Statics/Dynamics: Mec Eng 104, Civ Eng 130, Phys 105; Thermodynamics: Mec Eng 105, Eng 115, Chem Eng 141",'courseDone':coreTaken, 'courseLeft':coreNotTaken})
			#CES Cluster Course 1-4
			#	Optoelectronics, Electromagnetics, and Plasmas: Electrical Engineering 117, 118, 119, 120, 121, 136, 145A; Materials Science 111; Nuclear Engineering 180; Physics 142;	Statistics 134.
			#	Bionuclear Engineering. Electrical Engineering C145B; NuclearEngineering 101, 107, 162, 167.
			#	Radiation Transport. Nuclear Engineering 101, 124, 150, 155, 162, 180.
			#	Thermodynamics and Combustion. Chemical Engineering 141; Engineering 115; Mechanical Engineering 105, 109, 140, 145, 151, 142; Materials Science 115; Physics 112.
			#	Mass and Energy Transport. Chemical Engineering 150A, 150B, 152,157, 171; Mechanical Engineering 106, 107A, 107B, 162, 165, 185;Materials Science 149, 176.
			#	Optimization. Computer Science 170, 172, 174, 188; IndustrialEngineering 131, 160, 161, 162, 166.
			#	Computational Materials Science.Engineering 45;Materials Science 102, 103; Electrical Engineering 131 or MaterialsScience 111 or Physics 141A; Materials Science 112, 113, 116, 117 (orPhysics 141B), 118, 120, 121, 122, 123, 124, 125.
			#	Mechanics. Civil Engineering 130, 131; Engineering 36, C164,Integrative Biology 135; Mechanical Engineering 104, 106, 132, 133,134, 165, 170, 175, 176, 185; Physics 105.
			#	Environmental Transport. Civil Engineering 108, 116, 173; ChemicalEngineering 171; Materials Science 149, 176.
			"""advancement"""
			cluster={'oep':0,'be':0,'rt':0,'tc':0,'met':0,'o':0,'cms':0,'m':0,'et':0}
			oep={'ELENG.117':'EE 117', 'ELENG.118':'EE 118', 'ELENG.119':'EE 119', 'ELENG.120':'EE 120', 'ELENG.121':'EE 121', 'ELENG.136':'EE 136', 'ELENG.145A':'EE 145A', 'MATSCI.111':'MatSci 111', 'NUCENG.180':'NucEng 180','PHYSICS.142':'Physics 142','STAT.134':'Stats 134'}
			be={'ELENG.C145B':'EE C145B','NUCENG.101':'NucEng 101','NUCENG.107':'NucEng 107','NUCENG.162':'NucEng 162','NUCENG.167':'NucEng 167'}
			rt={'NUCENG.101':'NucEng 101','NUCENG.124':'NucEng 124','NUCENG.150':'NucEng 150','NUCENG.155':'NucEng 155','NUCENG.162':'NucEng 162','NUCENG.180':'NucEng 180'}
			tc={'CHMENG.141':'Chem Eng 141', 'ENGIN.115':'E 115','MECENG.105':'MecEng 105','MECENG.109':'MecEng 109','MECENG.140':'MecEng 140','MECENG.145':'MecEng 145','MECENG.151':'MecEng 151','MECENG.142':'MecEng 142', 'MATSCI.115':'MatSci 115','PHYSICS.112':'Physics 112'}
			met={'CHMENG.150A':'ChemEng 150A','CHMENG.150B':'ChemEng 150B','CHMENG.152':'ChemEng 152','CHMENG.157':'ChemEng 157','CHMENG.171':'ChemEng 171','MECENG.106':'MecEng 106','MECENG.107A':'MecEng 107A','MECENG.107B':'MecEng 107B','MECENG.162':'MecEng 162','MECENG.165':'MecEng 165','MECENG.185':'MecEng 185', 'MATSCI.149':'MatSci 149','MATSCI.176':'MatSci 176'}
			o={'COMPSCI.170':'CompSci 170','COMPSCI.172':'CompSci 172','COMPSCI.174':'CompSci 174','COMPSCI.188':'CompSci 188','INDENG.131':'IndEng 131','INDENG.160':'IndEng 160','INDENG.161':'IndEng 161','INDENG.162':'IndEng 162','INDENG.166':'IndEng 166'}
			cms={'ENGIN.45':'E 45','MATSCI.102':'MatSci 102','MATSCI.103':'MatSci 103','ELENG.131':'EE 131', 'MATSCI.111':'MatSci 111', 'PHYSICS.141A':'Physics 141A', 'PHYSICS.141B':'Physics 141B','MATSCI.112':'MatSci 112','MATSCI.113':'MatSci 113','MATSCI.116':'MatSci 116','MATSCI.117':'MatSci 117','MATSCI.118':'MatSci 118','MATSCI.120':'MatSci 120','MATSCI.121':'MatSci 121','MATSCI.122':'MatSci 122','MATSCI.123':'MatSci 123','MATSCI.124':'MatSci 124','MATSCI.125':'MatSci 125'}
			m={'CIVENG.130':'CivEng 130','CIVENG.131':'CivEng 131','ENGIN.36':'E 36','ENGIN.C164':'E C164','INTEGBI.135':'IB 135','PHYSICS.105':'Physics 105','MECENG.104':'MecEng 104', 'MECENG.106':'MecEng 106','MECENG.132':'MecEng 132','MECENG.133':'MecEng 133','MECENG.134':'MecEng 134','MECENG.165':'MecEng 165','MECENG.170':'MecEng 170','MECENG.175':'MecEng 175','MECENG.176':'MecEng 176','MECENG.185':'MecEng 185'}
			et={'CIVENG.108':'CivEng 108','CIVENG.116':'CivEng 116','CIVENG.173':'CivEng 173','CHMENG.171':'ChemE 171','MATSCI.149':'MatSci 149','MATSCI.176':'MatSci 176'}
			clusterTaken=[]
			clusterNotTaken=[]
			for key in oep:
				if (key in takenClasses):
					cluster['oep']=cluster['oep']+1
					clusterTaken.append(oep[key])
				else:
					clusterNotTaken.append(oep[key])
			for key in be:
				if (key in takenClasses):
					cluster['be']=cluster['be']+1
					clusterTaken.append(be[key])
				else:
					clusterNotTaken.append(be[key])
			for key in rt:
				if (key in takenClasses):
					cluster['rt']=cluster['rt']+1
					clusterTaken.append(rt[key])
				else:
					clusterNotTaken.append(rt[key])
			for key in tc:
				if (key in takenClasses):
					cluster['tc']=cluster['tc']+1
					clusterTaken.append(tc[key])
				else:
					clusterNotTaken.append(tc[key])
			for key in met:
				if (key in takenClasses):
					cluster['met']=cluster['met']+1
					clusterTaken.append(met[key])
				else:
					clusterNotTaken.append(met[key])
			for key in o:
				if (key in takenClasses):
					cluster['o']=cluster['o']+1
					clusterTaken.append(o[key])
				else:
					clusterNotTaken.append(o[key])
			for key in cms:
				if (key in takenClasses):
					cluster['cms']=cluster['cms']+1
					clusterTaken.append(cms[key])
				else:
					clusterNotTaken.append(cms[key])
			for key in m:
				if (key in takenClasses):
					cluster['m']=cluster['m']+1
					clusterTaken.append(m[key])
				else:
					clusterNotTaken.append(m[key])
			for key in et:
				if (key in takenClasses):
					cluster['et']=cluster['et']+1
					clusterTaken.append(et[key])
				else:
					clusterNotTaken.append(et[key])
			if (cluster['oep']>=4 or cluster['be']>=4 or cluster['rt']>=4 or cluster['tc']>=4 or cluster['met']>=4 or cluster['o']>=4 or cluster['cms']>=4 or cluster['m']>=4 or cluster['et']>=4 ):
				ans.append({'reqName':'Cluster Courses', 'reqCompleted':True, 'reqDescription':"CES Cluster Course: Each student must complete four courses from one of the given clusters: Optoelectronics, Electromagnetics, and Plasmas: Electrical Engineering 117, 118, 119, 120, 121, 136, 145A; Materials Science 111; Nuclear Engineering 180; Physics 142;Statistics 134. Bionuclear Engineering: Electrical Engineering C145B; Nuclear Engineering 101, 107, 162, 167. Radiation Transport: Nuclear Engineering 101, 124, 150, 155, 162, 180. Thermodynamics and Combustion: Chemical Engineering 141; Engineering 115; Mechanical Engineering 105, 109, 140, 145, 151, 142; Materials Science 115; Physics 112. Mass and Energy Transport: Chemical Engineering 150A, 150B, 152,157, 171; Mechanical Engineering 106, 107A, 107B, 162, 165, 185;Materials Science 149, 176. Optimization: Computer Science 170, 172, 174, 188; Industrial Engineering 131, 160, 161, 162, 166. Computational Materials Science: Engineering 45;Materials Science 102, 103; Electrical Engineering 131 or Materials Science 111 or Physics 141A; Materials Science 112, 113, 116, 117 (or Physics 141B), 118, 120, 121, 122, 123, 124, 125.  Mechanics: Civil Engineering 130, 131; Engineering 36, C164,Integrative Biology 135; Mechanical Engineering 104, 106, 132, 133,134, 165, 170, 175, 176, 185; Physics 105. Environmental Transport: Civil Engineering 108, 116, 173; Chemical Engineering 171; Materials Science 149, 176.**Alternative Cluster courses can be considered by advisors**",'courseDone':clusterTaken, 'courseLeft':clusterNotTaken})
			else:
				ans.append({'reqName':'Cluster Courses', 'reqCompleted':False, 'reqDescription':"CES Cluster Course: Each student must complete four courses from one of the given clusters: Optoelectronics, Electromagnetics, and Plasmas: Electrical Engineering 117, 118, 119, 120, 121, 136, 145A; Materials Science 111; Nuclear Engineering 180; Physics 142;Statistics 134. Bionuclear Engineering: Electrical Engineering C145B; Nuclear Engineering 101, 107, 162, 167. Radiation Transport: Nuclear Engineering 101, 124, 150, 155, 162, 180. Thermodynamics and Combustion: Chemical Engineering 141; Engineering 115; Mechanical Engineering 105, 109, 140, 145, 151, 142; Materials Science 115; Physics 112. Mass and Energy Transport: Chemical Engineering 150A, 150B, 152,157, 171; Mechanical Engineering 106, 107A, 107B, 162, 165, 185;Materials Science 149, 176. Optimization: Computer Science 170, 172, 174, 188; Industrial Engineering 131, 160, 161, 162, 166. Computational Materials Science: Engineering 45;Materials Science 102, 103; Electrical Engineering 131 or Materials Science 111 or Physics 141A; Materials Science 112, 113, 116, 117 (or Physics 141B), 118, 120, 121, 122, 123, 124, 125.  Mechanics: Civil Engineering 130, 131; Engineering 36, C164,Integrative Biology 135; Mechanical Engineering 104, 106, 132, 133,134, 165, 170, 175, 176, 185; Physics 105. Environmental Transport: Civil Engineering 108, 116, 173; Chemical Engineering 171; Materials Science 149, 176.**Alternative Cluster courses can be considered by advisors**",'courseDone':clusterTaken, 'courseLeft':clusterNotTaken})
			#Engineering 170A, 170B, Introduction to Modeling and Simulation
			ans.append(twoReq(takenClasses, 'Introduction to Modeling and Simulation', 'ENGIN.170A', 'E 170A', 'ENGIN.170B', 'E 170B', "Senior year requirement of both Engineering 170A and 170B"))
			#Engin 180A, Computational Engineering Science: Modeling, Simulation
			ans.append(basicReq(takenClasses, 'ENGIN.180A', 'E 180A', "Senior year Computational Engineering Science: Modeling and Simulation requirement of Engineering 180A"))
			#Computational Project Course
			project={'ENGIN.180B':'E 180B','ENGIN.177':'E 177','BIOENG.143':'BioE 143','INDENG.131':'IEOR 131','INDENG.162':'IEOR 162','MECENG.135':'MecEng 135','MECENG.145':'MecEng 145','MECENG.180':'MecEng 180','NUCENG.155':'NucEng 155','MATSCI.215':'MatSci 215'}
			ans.append(manyChoiceReq(takenClasses, 'Computational Project Course', project, "Senior year Project requirement of one course"))
			#Engineering 190, Technical Communication
			ans.append(basicReq(takenClasses, 'ENGIN.190', 'E 190', "Senior year Technical Communication requirement of Engineering 190"))
			return ans
		# Energy Engineering
		elif(major=='ENENG'):
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#E 7 , Introduction to Applied Computing or CS 61A
			ans.append(twoChoiceReq(takenClasses,"Introduction to Applied Computing", 'ENGIN.7', 'E 7', 'COMPSCI.61A', 'CompSci 61A', "The freshman year Introduction to Applied Computing requirement of either E 7 or CS 61A"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Engineering 93-Energy Engineering Seminar
			ans.append(basicReq(takenClasses, 'ENGIN.93', 'E 93', "Part of the freshman year requirement of Engineering 93-Energy Engineering Seminar"))
			#CE C30/ME C85-Introduction to Solid Mechanics
			ans.append(twoChoiceReq(takenClasses,"Introduction to Solid Mechanics", 'CHMENG.C30', 'CE C30', 'MECENG.C85', 'ME C85', "The sophomore year Introduction to Solid Mechanics requirement of either CE C30 or ME C85"))
			#Energy and Resources Group100-Energy and Society (First H/SS course)
			ans.append(basicReq(takenClasses, 'ENERES.100', 'Energy and Society', "Part of the sophomore year requirement of Energy and Resources Group100-Energy and Society"))
			#Engineering Prep Course 1 and 2
			#One must be from List A; the second from list A or B. List A: El Eng 40 (or 100) or Engin 45; List B: Civ Eng 11 or 70, Chem 1B or 3A; El Eng 20N; Physics 7C
			a={'ELENG.40':'EE 40','ELENG.100':'EE 100','ENGIN.45':'E 45'}
			b={'CIVENG.11':'Civ Eng 11','CIVENG.70':'Civ Eng 70','CHEM.1B':'Chem 1B','CHEM.3A':'Chem 3A','ELENG.20N':'EE 20N','PHYSICS.7C':'Physics 7C'}
			takenA=[]
			notTakenA=[]
			for key in a:
				if key in takenClasses:
					takenA.append( a[key])
				else:
					notTakenA.append(a[key])
			takenB=[]
			notTakenB=[]
			for key in b:
				if key in takenClasses:
					takenB.append(b[key])
				else:
					notTakenB.append(b[key])
			if ((len(takenA)>=2)or ((len(takenA)>=1) and (len(takenB)>=1))):
				ans.append({'reqName':'Engineering Prep Course 1 and 2', 'reqCompleted':True, 'reqDescription':"One must be from List A; the second from list A or B. List A: El Eng 40 (or 100) or Engin 45; List B: Civ Eng 11 or 70, Chem 1B or 3A; El Eng 20N; Physics 7C",'courseDone':(takenA+takenB), 'courseLeft':(notTakenA+notTakenB)})
			else:
				ans.append({'reqName':'Engineering Prep Course 1 and 2', 'reqCompleted':False, 'reqDescription':"One must be from List A; the second from list A or B. List A: El Eng 40 (or 100) or Engin 45; List B: Civ Eng 11 or 70, Chem 1B or 3A; El Eng 20N; Physics 7C",'courseDone':(takenA+takenB), 'courseLeft':(notTakenA+notTakenB)})
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Mechanical Engineering 40-Thermodynamics or Engineering 115-Engineering Thermodynamics
			ans.append(twoChoiceReq(takenClasses,"Thermodynamics", 'MECENG.40', 'ME 40', 'ENGIN.115', 'E 115', "The sophomore year Thermodynamics requirement of either ME 40 or E 115"))
			#CE 100-Elementary Fluid Mechanics or ME 106-Fluid Mechanics
			ans.append(twoChoiceReq(takenClasses,"Fluid Mechanics", 'MECENG.106', 'ME 106', 'CHMENG.100', 'CE 100', "The junior year Fluid Mechanics requirement of either ME 106 or CE 100"))
			#Economics Course. Choose one from the following list: Civ Eng 156, ENG 120; Env Econ *147, *C151, *153,*154; ERG C180; *ESPM 102D; *PEIS 101 or an Economics course chosen in consultation with faculty adviser.
			econ={'CIVENG.156':'Civ Eng 156','ENGIN.120':' E 120','ENVECON.147':'Env Econ 147','ENVECON.C151':'Env Econ C151','ENVECON.153':'Env Econ 153','ENVECON.154':'Env Econ 154','ENERES.C180':'ERG C180','ESPM.102D':'ESPM 102D','POLECON.101':'PEIS 101'}
			"""advancement"""
			ans.append(manyChoiceReq(takenClasses, 'Economics Course', econ, "The junior year requirement of an Economics Course **Can be any Economics course chosen in consultation with faculty adviser**"))
			#Elec. Eng. 137A-Introduction to Electric Power Systems
			ans.append(basicReq(takenClasses, 'ELENG.137A', 'EE 137A', "The junior year Introduction to Electric Power Systems requirement"))
			#Math/Stat/Analysis Course. Choose one from the following list: Civ Eng 93, Comp Sci 70, Engin 117, IEOR 172, Math 55 or Stat 134
			math={'CIVENG.93':'Civ Eng 93','COMPSCI.70':'Comp Sci 70','ENGIN.117':'E 117','INDENG.172':'IEOR 172','MATH.55':'Math 55','STAT.134':'Stat 134'}
			ans.append(manyChoiceReq(takenClasses, 'Math/Stat/Analysis Course', math, "The junior year requirement of a Math/Stat/Analysis Course"))
			#ME 109-Heat Transfer
			ans.append(basicReq(takenClasses, 'MECENG.109', 'ME 109', "The junior year Heat Transfer requirement"))
			#MSE 136-Materials in Energy Technologies
			ans.append(basicReq(takenClasses, 'MATSCI.136', 'MSE 136', "The junior year Materials in Energy Technologies requirement"))
			#Nuc Eng 161-Nuclear Power Engineering
			ans.append(basicReq(takenClasses, 'NUCENG.161', 'NucE 161', "The junior year Nuclear Power Engineering requirement"))
			#CE 108-Air Pollutant Emissions and Control or CE 111-Environmental Engineering
			ans.append(twoChoiceReq(takenClasses, 'Environment', 'CHMENG.108', 'CE 108', 'CHMENG.111', 'CE 111',"The senior year Air Pollutant Emissions and Control or Environmental Engineering requirement"))
			#CE 107-Climate Change Mitigation or Geography 142-Climate Dynamics
			ans.append(twoChoiceReq(takenClasses, 'Climate', 'CHMENG.107', 'CE 107', 'GEOG.142', 'Geography 142',"The senior year Climate requirement of one of two classes"))
			#Engineering 194-Research Capstone Course
			ans.append(basicReq(takenClasses, 'ENG.194', 'E 194', "The senior year Research Capstone Course requirement"))
			#Elec. Eng. 134-Fundamentals of Photovoltaic Devices
			ans.append(basicReq(takenClasses, 'ELENG.134', 'EE 134', "The senior year Fundamentals of Photovoltaic Devices requirement"))
			#Sustainability Course. Choose one from the following list: Civ Eng 111, 113N, 115; City & Reg. Planning *119; ERG 101.
			sustain={'CIVENG.111':'CivEng 111','CIVENG.113N':'CivEng 113N','CIVENG.115':'CivEng 115','CYPLAN.119':'City & Reg. Planning 119','ENERES.101':'ERG 101'}
			#Technical elective to be chose in consultation with faculty adviser
			"""advancement"""
			ans.append({'reqName':'Technical elective', 'reqCompleted':True, 'reqDescription':"Can be any agreed upon class with your advisor so we will assume that this requirement is fulfilled because we have no way of checking",'courseDone':[], 'courseLeft':[]})
			return ans
		# Engineering Math and Statistics
		elif(major=='ENGMS'):
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#E 7 , Introduction to Applied Computing or CS 61A
			ans.append(twoChoiceReq(takenClasses,"Introduction to Applied Computing", 'ENGIN.7', 'E 7', 'COMPSCI.61A', 'CompSci 61A', "The freshman year Introduction to Applied Computing requirement of either E 7 or CS 61A"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Two lower division courses in engineering, mathematics, or statistics, chosen in consultation with your faculty advisor; options include CS 61A, CS 61B, CS 61C, CS 70, CE C30/ME C85, E7, E28, E 45, Math 55, but other courses may also be used. Courses used to satisfy the two computer science course requirement may NOT also be for lower division technical electives. They can only be used to complete one requirement.
			tech={'COMPSCI.61A':'CompSci 61A','COMPSCI.61B':'CompSci 61B','COMPSCI.61C':'CompSci 61C','COMPSCI.70':'CompSci 70','CHMENG.C30':'ChemE C30','MECENG.C85':'MecE C85','ENGIN.7':'E 7','ENGIN.28':'E 28','ENGIN.45':'E 45','MATH.55':'Math 55'}
			techTaken=[]
			techNotTaken=[]
			csone=False
			cstwo=('ENGIN.177' in takenClasses)
			for key in tech:
				if (key in takenClasses):
					if ((key in ['COMPSCI.61A','ENGIN.7'])and (not csone)):
						csone=True
						techTaken.append(tech[key]+' (used for Introduction to Applied Computing requirement)')
					elif (key in ['COMPSCI.61B'] and (not cstwo)):
						cstwo=True
						techTaken.append(tech[key]+' (used for Second Computer Science Course requirement)')
					else:
						techTaken.append(tech[key])
				else:
					techNotTaken.append(tech[key])
			"""advancement"""
			if('ENGIN.177' in takenClasses) and ('COMPSCI.61B' in takenClasses):
				techTaken.append('E 177')
			#print len(techTaken)
			if((len(techTaken)>=4)or (((not csone)or (not cstwo))and (len(techTaken)>=3)) or ((not csone) and (not cstwo) and (len(techTaken)>=2))):
				ans.append({'reqName':'Lower Division Technical Electives', 'reqCompleted':True, 'reqDescription':"Part of the freshman and sophmore year Technical elective requirement of two classes **Can be other cclasses agreed upon with advisor**",'courseDone':techTaken, 'courseLeft':techNotTaken})
			else:
				ans.append({'reqName':'Lower Division Technical Electives', 'reqCompleted':False, 'reqDescription':"Part of the freshman and sophmore year Technical elective requirement of two classes **Can be other cclasses agreed upon with advisor**",'courseDone':techTaken, 'courseLeft':techNotTaken})
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Physics 7C-Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Second Computer Science Course (E177-Advanced Programming with MATLAB or CS 61B-Data Sturctures)
			ans.append(twoChoiceReq(takenClasses,'Second Computer Science Course', 'ENGIN.177', 'ME 177', 'COMPSCI.61B', 'CompSci 61B', "The sophomore year computer science requirement of E177 or CS 61B"))
			#Mathematics 110-Linear Algebra
			ans.append(basicReq(takenClasses, 'MATH.100', 'Math 100', "The junior year Linear Algebra requirement"))
			#Mathematics 104-Introduction to Analysis
			ans.append(basicReq(takenClasses, 'MATH.104', 'Math 104', "The junior year Introduction to Analysis requirement"))
			#Mathematics 105-Second course in Analysis or Mathematics 185-Introduction to Theory of Probability
			ans.append(twoChoiceReq(takenClasses,'Mathematics', 'MATH.105', 'Math 105', 'MATH.185', 'Math 185', "The junior year requirement of Math 105 or 185"))
			#Mathematics 128A-Numerical Analysis
			ans.append(basicReq(takenClasses, 'MATH.128A', 'Math 128A', "The junior year Numerical Analysis requirement"))
			#Statistics 134-Concepts of Probability
			ans.append(basicReq(takenClasses, 'STAT.134', 'Stats 134', "The junior year Concepts of Probability requirement"))
			#Technical electives must include 16 units of upper division engineering courses, selected with the help of your faculty adviser in order to provide depth in an area of engineering with high mathematical content--typically, most of these courses will come from a single engineering department, but courses that complement each other from different departments are also permissible. NOTE: IEOR 172 is an alternate course to Statistics 134. Students may not receive credit for both Statistics 134 and IEOR 172. IEOR 172 cannot be used to fulfill engineering unit requirements; it can only be used as a substitution for Stat 134.
			#Three additional upper division technical courses as follows: One in mathematics, one in statistics, and one from either math or statistics from among: Math 105, 113, 118, 123, 125A, 126, 130, 135, 140, 142, 170, 185, 189, and E117; Statistics 135, 150, 151A, 151B, 152, 153, 154, 157, 158.
			math=0
			stats=0
			math={'MATH.105':'Math 105','MATH.113':'Math 113','MATH.118':'Math 118','MATH.123':'Math 123','MATH.125A':'Math 125A','MATH.126':'Math 126','MATH.130':'Math 130','MATH.135':'Math 135','MATH.140':'Math 140','MATH.142':'Math 142','MATH.170':'Math 170','MATH.185':'Math 185','MATH.189':'Math 189','ENGIN.117':'E 117'}
			stats={'STAT.135':'Stats 135','STAT.150':'Stats 150','STAT.151A':'Stats 151A','STAT.151B':'Stats 151B','STAT.152':'Stats 152','STAT.153':'Stats 153','STAT.154':'Stats 154','STAT.157':'Stats 157','STAT.158':'Stats 158'}
			upperTaken=[]
			upperNotTaken=[]
			for key in  math:
				if (key in takenClasses):
					if ((key is 'MATH.105') and ('MATH.185' in takenClasses)):
						math+=1
						upperTaken.append(math[key])
					elif (key is 'MATH.105'):
						upperTaken.append(math[key])
					elif (key is 'MATH.185'):
						upperTaken.append(math[key])
					else:
						math+=1
						upperTaken.append(math[key])
				else:
					upperNotTaken.append(math[key])
			for key in stats:
				if (key in takenClasses):
					stats+=1
					upperTaken.append(stats[key])
				else:
					upperNotTaken.append(stats[key])
			"""advancement"""
			if(math>=1 and stats>=1 and (math>1 or stats>1)):
				ans.append({'reqName':'Upper Division Technical Courses', 'reqCompleted':True, 'reqDescription':"Three additional upper division technical courses as follows: One in mathematics, one in statistics, and one from either math or statistics from among: Math 105, 113, 118, 123, 125A, 126, 130, 135, 140, 142, 170, 185, 189, and E117; Statistics 135, 150, 151A, 151B, 152, 153, 154, 157, 158.",'courseDone':upperTaken, 'courseLeft':upperNotTaken})
			else:
				ans.append({'reqName':'Upper Division Technical Courses', 'reqCompleted':False, 'reqDescription':"Three additional upper division technical courses as follows: One in mathematics, one in statistics, and one from either math or statistics from among: Math 105, 113, 118, 123, 125A, 126, 130, 135, 140, 142, 170, 185, 189, and E117; Statistics 135, 150, 151A, 151B, 152, 153, 154, 157, 158.",'courseDone':upperTaken, 'courseLeft':upperNotTaken})
			return ans
		# Engineering Physics
		elif(major=='ENGP'):
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#E 7 , Introduction to Applied Computing or CS 61A
			ans.append(twoChoiceReq(takenClasses,"Introduction to Applied Computing", 'ENGIN.7', 'E 7', 'COMPSCI.61A', 'CompSci 61A', "The freshman year Introduction to Applied Computing requirement of either E 7 or CS 61A"))
			#Chemistry 1B-General Chemistry or Chemistry 4B-General Chemistry
			ans.append(twoChoiceReq(takenClasses,'General Chemistry', 'CHEM.1B', 'Chem 1B', 'CHEM.4B', 'Chem 4B', "The freshman year requirement of General Chemistry"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Physics 7C-Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Two courses from the following lower division technical electives: Astronomy 7A, 7B; Biology 1A, 1B; CE C30/ME C85; Chemistry 3A; E 45; EE 40 (or 100);
			lower={'ASTRON.7A':'Astronomy 7A','ASTRON.7B':'Astronomy 7B','BIOLOGY.1A':'Biology 1A','BIOLOGY.1B':'Biology 1B','CHMENG.C30':'CE C30','MECENG.C85':'ME C85','CHEM.3SA':'Chemistry 3A','ENGIN.45':'E 45','ELENG.40':'EE 40','ELENG.100':'EE 100'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'Lower Division Technical Electives', lower, "The sophomore year lower division technical elective requirement of two classes", 2))
			#15 units of upper division courses in engineering.  Not courses numbered 24, 39, 84; BioE 100; CS C79, CS 195, CS H195, Engin 125; 130 AC, 140, IEOR 172, IEOR 190 series; IEOR 191; and ME 191AC, 190K; 191K.
			num=0
			for item in takenClasses:
				if ((('ENG' in item)or ('COMPSCI' in item)or('MATSCI'in item)or ('NSE' in item))and (not (('ENGLISH' in item)or ('.24' in item)or ('.39' in item)or ('.84' in item)or ('BIOENG.100' in item)or ('COMPSCI.C79' in item)or ('COMPSCI.195' in item)or ('COMPSCI.H195' in item)or ('ENGIN.125' in item)or ('ENGIN.130AC' in item)or ('ENGIN.140' in item)or ('INDENG.172' in item)or ('INDENG.190' in item)or ('INDENG.191' in item)or ('MECENG.191AC' in item)or ('MECENG.190K' in item)or ('MECENG.191K' in item)))):
					num+=units(item)
			if (num>=15):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"15 units of upper division courses in engineering.  Not courses numbered 24, 39, 84; BioE 100; CS C79, CS 195, CS H195, Engin 125; 130 AC, 140, IEOR 172, IEOR 190 series; IEOR 191; and ME 191AC, 190K; 191K.",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"15 units of upper division courses in engineering.  Not courses numbered 24, 39, 84; BioE 100; CS C79, CS 195, CS H195, Engin 125; 130 AC, 140, IEOR 172, IEOR 190 series; IEOR 191; and ME 191AC, 190K; 191K."+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			"""advancement"""
			#A minimum of 14 units of upper division physics;
			num=0
			for item in takenClasses:
				if(re.match(r'PHYSICS.1\d\d',item)):
					num+=units(item)
			if (num>=14):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"14 units of upper division physics",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"14 units of upper division physics"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			"""advancement"""
			#At least 40 units of approved upper division technical subjects (mathematics, statistics, science, and engineering).
			num=0
			for item in takenClasses:
				if(not re.search(r'POLSCI.1\d\d',item))and((re.search(r'PHYSICS.1\d\d',item))or(re.search(r'ENG.1\d\d',item))or(re.search(r'ENGIN.1\d\d',item))or(re.search(r'MATH.1\d\d',item))or(re.search(r'SCI.1\d\d',item))or(re.search(r'STAT.1\d\d',item))or(re.search(r'CHM.1\d\d',item))or(re.search(r'CHEM.1\d\d',item))or(re.search(r'BIOLOGY.1\d\d',item))or(re.search(r'ASTRON.1\d\d',item))or(re.search(r'BIO.1\d\d',item)) or(re.search(r'BI.1\d\d',item))or (re.search(r'SC.1\d\d',item))):
					num+=units(item)
			if (num>=40):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 40 units of approved upper division technical subjects (mathematics, statistics, science, and engineering)",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"At least 40 units of approved upper division technical subjects (mathematics, statistics, science, and engineering)"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			"""advancement"""
			#E 115-Engineering Thermodynamics or Physics 112-Introduction to Statistical and Thermal Physics
			ans.append(twoChoiceReq(takenClasses,"Thermal Physics", 'ENGIN.115', 'E 115', 'PHYSICS.112', 'Physics 112', "The junior year thermal physics requirement of either E 115 or Physics 112"))
			#Mathematics 104-Introduction to Analysis and Mathematics 185-Introduction to Complex Analysis, or Mathematics 121A and 121B-Mathematical Tools for the Physical Sciences
			math={'MATH.104':'Math 104','MATH.185':'Math 185','MATH.121A':'Math 121A','MATH.121B':'Math 121B'}
			mathTaken=[]
			mathNotTaken=[]
			for key in math:
				if (key in takenClasses):
					mathTaken.append(math[key])
				else:
					mathNotTaken.append(math[key])
			if ((('MATH.104' in takenClasses)and('MATH.185' in takenClasses))or(('MATH.121A' in takenClasses)and('MATH.121B' in takenClasses))):
				ans.append({'reqName':'Mathematics', 'reqCompleted':True, 'reqDescription':"Part of the junior year Mathematics requirement",'courseDone':mathTaken, 'courseLeft':mathNotTaken})
			else:
				ans.append({'reqName':'Mathematics', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':mathTaken, 'courseLeft':mathNotTaken})
			#ME 104-Engineering Mechanics or Physics 105-Analytic Mechanics
			ans.append(twoChoiceReq(takenClasses, 'Mechanics', 'MECENG.104', 'ME 104', 'PHYSICS.105', 'Physics 105', "The junior year Mechanics requirement of either ME 104 or Physics 105"))
			#Physics 137A and 137B-Quantum Mechanic
			ans.append(twoReq(takenClasses, 'Quantum Mechanics', 'PHYSICS.137A', 'Physics 137A', 'PHYSICS.137B', 'Physics 137B', "The junior year Quantum Mechanics requirement of botth Physics 137A and 137B"))
			#EE 143-Microfabrication Technology, or NE 104(6)-Nuclear Instrumentation Lab, or Physics 111A-Modern Physics and Advanced Electrical Lab
			rand={'ELENG.143':'EE 143','NUCENG.104':'NE 104','PHYSICS.111A':'Physics 111A'}
			ans.append(manyChoiceReq(takenClasses, 'Anvanced Lab', rand, "The senior year requirement of EE 143-Microfabrication Technology, or NE 104-Nuclear Instrumentation Lab, or Physics 111A-Modern Physics and Advanced Electrical Lab"))
			#ME 185-Introduction to Continuum Mechanics or ME 106-Fluid Mechanics
			ans.append(twoChoiceReq(takenClasses, 'Advanced Mechanics', 'MECENG.185', 'ME 185', 'MECENG.106', 'ME 106', "The senior year Mechanics requirement of either ME 184 or ME 106"))
			#Students opting to take EE 117 must take either EE 118 (formerly EE 119) or BioE 164. Students opting to take the Physics 110A must take 110B.
			electro={'ELENG.117':'EE 117','ELENG.118':'EE 118','BIOENG.164':'BioE 164','PHYSICS.110A':'Physics 110A','PHYSICS.110B':'Physics 110B'}
			eTaken=[]
			eNotTaken=[]
			for key in electro:
				if (key in takenClasses):
					eTaken.append(electro[key])
				else:
					eNotTaken.append(electro[key])
			if ((('ELENG.117' in takenClasses)and(('ELENG.118' in takenClasses)or('BIOENG.164' in takenClasses)))or(('PHYSICS.110A' in takenClasses)and('PHYSICS.110B' in takenClasses))):
				ans.append({'reqName':'Electromagnetism and Optics', 'reqCompleted':True, 'reqDescription':"The senior year requirement where students select between EE 117 and Physics 110A.Students opting to take EE 117 must take either EE 118 (formerly EE 119) or BioE 164. Students opting to take the Physics 110A must take 110B.",'courseDone':eTaken, 'courseLeft':eNotTaken})
			else:
				ans.append({'reqName':'Electromagnetism and Optics', 'reqCompleted':False, 'reqDescription':"The senior year requirement where students select between EE 117 and Physics 110A.Students opting to take EE 117 must take either EE 118 (formerly EE 119) or BioE 164. Students opting to take the Physics 110A must take 110B.",'courseDone':eTaken, 'courseLeft':eNotTaken})
			#MSE 111-Electric and Magnetic Properties of Materials or Physics 141A-Solid State Physics
			ans.append(twoChoiceReq(takenClasses, 'Material Physics', 'MATSCI.111', 'MSE 111', 'PHYSICS.141A', 'Physics 141A', "The senior year Materials requirement of either MSE 111 or Physics 141A"))
			return ans
		# Industrial Engineering & Operations Research
		elif(major=='INDENG'):
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Chem 1A/1AL
			ans.append(twoReq(takenClasses,'Chemistry', 'CHEM.1A', 'Chem 1A','CHEM.1AL', 'Chem 1AL', "The freshman year Chemistry requirement of Chem 1A and 1AL"))
			#CS (9C, 9F or 9G)
			prog={'COMPSCI.9C':'CS 9C','COMPSCI.9F':'CS 9F','COMPSCI.9G':'CS 9G'}
			ans.append(manyChoiceReq(takenClasses, 'Programming Language', prog, "Requirement of Computer Science 9C,F, or G"))
			#UCB  Engineering 7
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7', "The sophomore year Introduction to Computer Programming requirement"))
			#Engineering Breadth Electives: 9 units (minimum) Must include 9 units of coursework from the approved list: Bioe 102; CE 11, C30, 60, 70, 155; EE 40, 42,100; E 10, 28, 45, 115; MSE 111; ME, 40, C85, 132
			engbre={'BIOENG.102':'BioE 102', 'CIVENG.11':'CivEng 11','CIVENG.C30':'CivEng C30','CIVENG.60':'CivEng 60','CIVENG.70':'CivEng 70','CIVENG.155':'CivEng 155','ELENG.40':'EE 40','ELENG.42':'EE 42','ELENG.100':'EE 100','ENGIN.10':'E 10','ENGIN.28':'E 28','ENGIN.45':'E 45','ENGIN.115':'E 115', 'MATSCI.111':'MatSci 111','MECENG.40':'MecEng 40','MECENG.C85':'MecEng C85','MECENG.132':'MecEng 132'}
			engTaken=[]
			engNotTaken=[]
			num=0
			for key in engbre:
				if key in takenClasses:
					num+=units(key)
					engTaken.append(engbre[key])
				else:
					engNotTaken.append(engbre[key])
			if num>=9:
				ans.append({'reqName':'Engineering Breadth Electives', 'reqCompleted':True, 'reqDescription':"Must include 9 units of coursework from the approved list: Bioe 102; CE 11, C30, 60, 70, 155; EE 40, 42,100; E 10, 28, 45, 115; MSE 111; ME, 40, C85, 132",'courseDone':engTaken, 'courseLeft':engNotTaken})
			else:
				ans.append({'reqName':'Engineering Breadth Electives', 'reqCompleted':False, 'reqDescription':"Must include 9 units of coursework from the approved list: Bioe 102; CE 11, C30, 60, 70, 155; EE 40, 42,100; E 10, 28, 45, 115; MSE 111; ME, 40, C85, 132",'courseDone':engTaken, 'courseLeft':engNotTaken})
			#IEOR Electives : 6 courses from the list below IEOR 115, 130,140, 150, 151, 153, 166, 170, 171
			ieorelec={'INDENG.115':'IEOR 115','INDENG.130':'IEOR 130','INDENG.140':'IEOR 140','INDENG.150':'IEOR 150','INDENG.151':'IEOR 151','INDENG.153':'IEOR 153','INDENG.166':'IEOR 166','INDENG.170':'IEOR 170','INDENG.171':'IEOR 171'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'IEOR Electives', ieorelec,"6 courses from the list below IEOR 115, 130,140, 150, 151, 153, 166, 170, 171", 6))
			#E 120
			ans.append(basicReq(takenClasses, 'ENGIN.120', 'E 120', "The E 120 requirement"))
			#IEOR 172 or Stat 134
			ans.append(twoChoiceReq(takenClasses,'Probability', 'INDENG.172', 'IEOR 172','STAT.134', 'Stats 134', "The Probability requirement of IEOR 172 or Stat 134"))
			#IEOR 131
			ans.append(basicReq(takenClasses, 'INDENG.131', 'IEOR 131', "The IEOR 131 requirement"))
			#IEOR 160
			ans.append(basicReq(takenClasses, 'INDENG.160', 'IEOR 160', "The IEOR 160 requirement"))
			#IEOR 161
			ans.append(basicReq(takenClasses, 'INDENG.161', 'IEOR 161', "The IEOR 161 requirement"))
			#IEOR 162
			ans.append(basicReq(takenClasses, 'INDENG.162', 'IEOR 162', "The IEOR 162 requirement"))
			#IEOR 165
			ans.append(basicReq(takenClasses, 'INDENG.165', 'IEOR 165', "The IEOR 165 requirement"))
			#IEOR 180
			ans.append(basicReq(takenClasses, 'INDENG.165', 'IEOR 165', "The IEOR 165 requirement"))
			return ans
		# Materials Science & Engineering
		elif(major=='MATSCI'):
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#UCB  Engineering 7
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7', "The sophomore year Introduction to Computer Programming requirement"))
			#Chemistry 1B-General Chemistry or Chemistry 4B-General Chemistry
			ans.append(twoChoiceReq(takenClasses,'General Chemistry', 'CHEM.1B', 'Chem 1B', 'CHEM.4B', 'Chem 4B', "The freshman year requirement of General Chemistry"))
			#E 45-Properties of Materials
			ans.append(basicReq(takenClasses, 'ENGIN.45', 'E 45', "The sophomore year Properties of Materials requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append( twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#ME C85-Introduction to Solid Mechanics
			ans.append(basicReq(takenClasses, 'MECENG.C85', 'MecEng C85', "The sophomore year Introduction to Solid Mechanics requirement"))
			#Physics 7C-Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Technical electives must include 24 units of course work of which a minimum of 21 units must be upper division, and The 21 units of upperdivision courses cannot include: BioE 100; CS 195, H195; Engin 125; IEOR 190 series; ME 191AC, 191K.
			num=0
			notlist={'BIOENG.100', 'COMPSCI.195','COMPSCI.H195', 'ENGIN.125',  'INDENG.190A','INDENG.190B','INDENG.190C','INDENG.190D','INDENG.190E','INDENG.190F','INDENG.190G', 'MECENG.191AC', 'MECENG.191K'}
			for item in takenClasses:
				if(not item in notlist) and(not re.search(r'POLSCI.1\d\d',item))and((re.search(r'PHYSICS.1\d\d',item))or(re.search(r'ENG.1\d\d',item))or(re.search(r'ENGIN.1\d\d',item))or(re.search(r'MATH.1\d\d',item))or(re.search(r'SCI.1\d\d',item))or(re.search(r'STAT.1\d\d',item))or(re.search(r'CHM.1\d\d',item))or(re.search(r'CHEM.1\d\d',item))or(re.search(r'BIOLOGY.1\d\d',item))or(re.search(r'ASTRON.1\d\d',item))or(re.search(r'BIO.1\d\d',item)) or(re.search(r'BI.1\d\d',item))or (re.search(r'SC.1\d\d',item))):
					num+=units(item)
			if (num>=21):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"21 units of upperdivision courses cannot include: BioE 100; CS 195, H195; Engin 125; IEOR 190 series; ME 191AC, 191K **Approved by Advisor",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"21 units of upperdivision courses cannot include: BioE 100; CS 195, H195; Engin 125; IEOR 190 series; ME 191AC, 191K **Approved by Advisor"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			"""advancement"""
			#must include at least one (1) MSE 120 series course.
			techtwo={'MATSCI.120':'MatSci 120','MATSCI.121':'MatSci 121','MATSCI.122':'MatSci 122','MATSCI.123':'MatSci 123','MATSCI.125':'MatSci 125'}
			ans.append(manyChoiceReq(takenClasses, 'Technical Elective Two', techtwo, "The senior year Technical Elective requirement of 3 units from the MSE 120 series course"))
			#E 115-Engineering Thermodynamics
			ans.append(basicReq(takenClasses, 'ENGIN.115', 'E 115', "The junior year Engineering Thermodynamics requirement"))
			#MSE 102-Bonding Crystallography and Crystal Defects
			ans.append(basicReq(takenClasses, 'MATSCI.102', 'MatSci 102', "The junior year Bonding Crystallography and Crystal Defects requirement"))
			#MSE 103-Phase Transformation and Kinetics
			ans.append(basicReq(takenClasses, 'MATSCI.103', 'MatSci 103', "The junior year Phase Transformation and Kinetics requirement"))
			#MSE 104-Characterization of Materials
			ans.append(basicReq(takenClasses, 'MATSCI.104', 'MatSci 104', "The junior year Characterization of Materials requirement"))
			#E 117 Methods of Engineering Analysis
			ans.append(basicReq(takenClasses, 'ENGIN.117', 'E 117', "The junior year Methods of Engineering Analysis requirement"))
			#MSE 111-Properties of Electronic Materials
			ans.append(basicReq(takenClasses, 'MATSCI.111', 'MatSci 111', "The senior year Properties of Electronic Materials requirement"))
			#MSE 130-Experimental Materials Science
			ans.append(basicReq(takenClasses, 'MATSCI.130', 'MatSci 130', "The senior year Experimental Materials Science requirement"))
			#MSE 112-Corrosion
			ans.append(basicReq(takenClasses, 'MATSCI.112', 'MatSci 112', "The senior year Corrosion requirement"))
			#MSE 113-Mechanical Behavior of Materials
			ans.append(basicReq(takenClasses, 'MATSCI.113', 'MatSci 113', "The senior year Mechanical Behavior of Materials requirement"))
			#MSE 151-Polymeric Materials
			ans.append(basicReq(takenClasses, 'MATSCI.151', 'MatSci 151', "The senior year Polymeric Materials requirement"))
			return ans
		# Mechanical Engineering
		elif(major=='MECENG'):
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#UCB  Engineering 7
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7', "The sophomore year Introduction to Computer Programming requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#ME C85-Introduction to Solid Mechanics
			ans.append(basicReq(takenClasses, 'MECENG.C85', 'MecEng C85', "The sophomore year Introduction to Solid Mechanics requirement"))
			#UCB Engineering 10
			ans.append(basicReq(takenClasses, 'ENGIN.10', 'E 10', "The sophomore year Engineering Design and Analysis requirement"))
			#E 28-Graphics Communication in Engineering
			ans.append(basicReq(takenClasses, 'ENGIN.28', 'E 28', "The sophomore year Graphics Communication in Engineering requirement"))
			#ME 40-Thermodynamics
			ans.append(basicReq(takenClasses, 'MECENG.40', 'MecEng 40', "The sophomore year Thermodynamics requirement"))
			#EE 40-Introduction to Microelectronic Circuits or EE 100-Electronic Techniques for Engineering
			ans.append(twoChoiceReq(takenClasses, 'Electronics', 'ELENG.40', 'EE 40', 'ELENG.100', 'EE 100', "The sophomore year Electrical Engineering requirement of one of two classes"))
			#ME 104-Engineering Mechanics II (Dynamics)
			ans.append(basicReq(takenClasses, 'MECENG.104', 'MecEng 104', "The junior year Engineering Mechanics II requirement"))
			#ME 106-Fluid Mechanics
			ans.append(basicReq(takenClasses, 'MECENG.106', 'MecEng 106', "The junior year Fluid Mechanics requirement"))
			#ME 108-Introduction to Engineering Materials
			ans.append(basicReq(takenClasses, 'MECENG.108', 'MecEng 108', "The junior year Introduction to Engineering Materials requirement"))
			#ME 109-Heat Transfer
			ans.append(basicReq(takenClasses, 'MECENG.109', 'MecEng 109', "The junior year Heat Transfer requirement"))
			#ME 132-Dynamic Systems and Feedback
			ans.append(basicReq(takenClasses, 'MECENG.132', 'MecEng 132', "The junior year Dynamic Systems and Feedback requirement"))
			#ME 102A-Experimentation and Measurement
			ans.append(basicReq(takenClasses, 'MECENG.102A', 'MecEng 102A', "The senior year Experimentation and Measurement requirement"))
			#ME 102B-Mechanical Engineering Design
			ans.append(basicReq(takenClasses, 'MECENG.102B', 'MecEng 102B', "The senior year Mechanical Engineering Design requirement"))
			#ME 107-Mechanical Engineering Laboratory
			ans.append(basicReq(takenClasses, 'MECENG.107', 'MecEng 107', "The senior year Mechanical Engineering Laboratory requirement"))
			#Tech Elec:15 units from list
			tech={'ENGIN.117':'E 117','MECENG.130':'ME130' ,'MECENG.170':'ME170' ,'ENGIN.128':'E 128','MECENG.131':'ME 131' ,'MECENG.171':'ME 171', 'ENGIN.177':'E 177','MECENG.133':'ME 133','MECENG.173':'ME 173', 'ENGIN.191':'E 191','MECENG.C134':'ME C134','MECENG.175':'ME 175','MECENG.101': 'ME 101','MECENG.135':'ME 135','MECENG.C176':'ME C176' ,'MECENG.110': 'ME 110' ,'MECENG.138':'ME 138' ,'MECENG.C180':'ME C180' , 'MECENG.C115':'ME C115','MECENG.140':'ME 140' , 'MECENG.185':'ME 185', 'MECENG.C117':'ME C117','MECENG.146':'ME 146','MECENG.190A':'ME 190A','MECENG.118': 'ME 118','MECENG.151':'ME 151','MECENG.190L':'ME 190L','MECENG.119': 'ME 119' ,'MECENG.163':'ME 163' ,'MECENG.190M':'ME 190M' ,'MECENG.120':'ME 120' ,'MECENG.164':'ME164','MECENG.190Y':'ME 190Y' , 'MECENG.122': 'ME 122','MECENG.165': 'ME 165', 'MECENG.127':'ME 127','MECENG.167':'ME 167', 'MECENG.128': 'ME 128' ,'MECENG.168':'ME 168'}
			techTaken=[]
			techNotTaken=[]
			num=0
			for key in tech:
				if key in takenClasses:
					num+=units(key)
					techTaken.append(tech[key])
				else:
					techNotTaken.append(tech[key])
			if num>=15:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Must include 15 units of coursework from the approved list of upper-divison ME courses",'courseDone':techTaken, 'courseLeft':techNotTaken})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"Must include 15 units of coursework from the approved list of upper-divison ME courses",'courseDone':techTaken, 'courseLeft':techNotTaken})
			#Tech Elec: 1 design course
			des={'ENGIN.128':'E128','MECENG.101':'ME 101','MECENG.110':'ME 110','MECENG.C117':'ME C117','MECENG.119':'ME 119','MECENG.130':'ME 130','MECENG.135':'ME 135','MECENG.146':'ME 146','MECENG.165':'ME 165','MECENG.C176':'ME C176'}
			ans.append(manyChoiceReq(takenClasses, 'Technical Elective', des, "One design course required from list"))
			#Tech Elec: 1 quant course
			quant={'ENGIN.117':'E 117','ENGIN.177':'E 177','MATH.128A':'MATH 128A','MECENG.120':'ME 120','MECENG.C180':'ME C180'}
			ans.append(manyChoiceReq(takenClasses, 'Technical Elective', quant, "One quant course required from list"))
			#Tech Elec: 18 units total
			lower={'MCELLBI.11':'MCB 11','MCELLBI.32':'MCB 32','STAT.20':'Stats 20','ENGIN.45':'E 45','CIVENG.70':'CE 70','ASTRO.7A':'Astro 7A','BIOLOGY.1A': 'Bio 1A', 'BIOLOGY.1B': 'Bio 1B', 'CHEM.1B': 'Chem 1B', 'CHEM.5': 'Chem 5'}
			for key in lower:
				if key in takenClasses:
					num+=units(key)
					techTaken.append(lower[key])
				else:
					techNotTaken.append(lower[key])
			if num>=18:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Must include 18 units of coursework from the approved list",'courseDone':techTaken, 'courseLeft':techNotTaken})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"Must include 18 units of coursework from the approved list",'courseDone':techTaken, 'courseLeft':techNotTaken})
			return ans
		# Nuclear Engineering
		elif(major=='NUCENG'):
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#E 7 , Introduction to Applied Computing
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7',  "The freshman year Introduction to Applied Computing requirement of E 7"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#UCB Engineering 10
			ans.append(basicReq(takenClasses, 'ENGIN.10', 'E 10', "The sophomore year Engineering Design and Analysis requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#EE 40-Introduction to Microelectronic Circuits or EE 100-Electronic Techniques for Engineering
			ans.append(twoChoiceReq(takenClasses, 'Electronics', 'ELENG.40', 'EE 40', 'ELENG.100', 'EE 100', "The sophomore year Electrical Engineering requirement of one of two classes"))
			#Physics 7C-Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The sophomore year Physics for Scientists and Engineers requirement"))
			#E 45-Properties of Materials
			ans.append(basicReq(takenClasses, 'ENGIN.45', 'E 45', "The sophomore year Properties of Materials requirement"))
			#E 115-Engineering Thermodynamics
			ans.append(basicReq(takenClasses, 'ENGIN.115', 'E 115', "The junior year Engineering Thermodynamics requirement"))
			#E 117
			ans.append(basicReq(takenClasses, 'ENGIN.117', 'E 117', "The junior year Methods of Engineering Analysis requirement"))
			#NE 101-Nuclear Reactions and Radiation
			ans.append(basicReq(takenClasses, 'NUCENG.101', 'NucEng 101', "The junior year Nuclear Reactions and Radiation requirement"))
			#NE 150-Nuclear Reactor Theory
			ans.append(basicReq(takenClasses, 'NUCENG.150', 'NucEng 150', "The junior year Nuclear Reactor Theory requirement"))
			#NE 104-Radiation Detection Lab
			ans.append(basicReq(takenClasses, 'NUCENG.104', 'NucEng 104', "The junior year Radiation Detection Lab requirement"))
			#NE 170-Nuclear Engineering Design
			ans.append(basicReq(takenClasses, 'NUCENG.170', 'NucEng 170', "The senior year Nuclear Engineering Design requirement"))
			#32 technical elective units must include at least 17 units of upper division Nuc. Eng.Courses.
			nereq={'NUCENG.101','NUCENG.104','NUCENG.150','NUCENG.170'}
			num=0
			for item in takenClasses:
				if((re.search(r'NUCENG.1\d\d',item))and(not item in nereq)):
					num+=units(item)
			if (num>=17):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 17 units of upper division NE courses",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"At least 17 units of upper division NE courses"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			#Remaining technical elective units must be fulfilled by taking upper division courses in engineering and science, but cannot include BioE 100, E110, 124, 140, 193 or 195.
			num=0
			notlist={'BIOENG.100', 'ENGIN.140','ENGIN.124','ENGIN.193', 'ENGIN.195' }
			for item in takenClasses:
				if(not item in notlist) and(not re.search(r'POLSCI.1\d\d',item))and((re.search(r'PHYSICS.1\d\d',item))or(re.search(r'ENG.1\d\d',item))or(re.search(r'ENGIN.1\d\d',item))or(re.search(r'MATH.1\d\d',item))or(re.search(r'SCI.1\d\d',item))or(re.search(r'STAT.1\d\d',item))or(re.search(r'CHM.1\d\d',item))or(re.search(r'CHEM.1\d\d',item))or(re.search(r'BIOLOGY.1\d\d',item))or(re.search(r'ASTRON.1\d\d',item))or(re.search(r'BIO.1\d\d',item)) or(re.search(r'BI.1\d\d',item))or (re.search(r'SC.1\d\d',item))):
					num+=units(item)
			if (num>=32):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"32 units of upperdivision courses cannot include: BioE 100, E110, 124, 140, 193 or 195 **Approved by Advisor",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"32 units of upperdivision courses cannot include:  BioE 100, E110, 124, 140, 193 or 195 **Approved by Advisor"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			"""advancement"""
			return ans
		# Bioengineering and Materials Science & Engineering
		elif(major=='BIOMATSCI'):
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Chemistry 3A and 3AL , or Chem 112A
			if(('CHEM.3A' in takenClasses) and ('CHEM.3AL' in takenClasses)):
				ans.append({'reqName':'Organic Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Organic Chemistry requirement",'courseDone':['Chem 3A', 'Chem 3AL'], 'courseLeft':['Chem 112A']})
			elif('CHEM.112A' in takenClasses):
				ans.append({'reqName':'Organic Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Organic Chemistry requirement",'courseDone':['Chem 112A'], 'courseLeft':['Chem 3A', 'Chem 3AL']})
			else:
				ans.append({'reqName':'Organic Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Organic Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 3A', 'Chem 3AL','Chem 112A']})
			#E 7 , Introduction to Applied Computing
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7',  "The freshman year Introduction to Applied Computing requirement of E 7"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#BioE 10
			ans.append(basicReq(takenClasses, 'BIOENG.10', 'BioE 10', "The freshman year requirement of BioE"))
			#Freshman Seminar: BioE 24
			ans.append(basicReq(takenClasses, 'BIOENG.24', 'BioE 24',  "The freshman year bioengineering seminar requirement of BioE 24"))
			#Biology 1A & 1AL , General Biology
			ans.append(twoReq(takenClasses,'General Biology', 'BIOLOGY.1A', 'Bio 1A', 'BIOLOGY.1AL', 'Bio 1AL', "The sophomore year biology requirement of both Bio 1A and 1AL"))
			#E 45-Properties of Materials
			ans.append(basicReq(takenClasses, 'ENGIN.45', 'E 45', "The sophomore year Properties of Materials requirement"))
			#EE 40-Introduction to Microelectronic Circuits or EE 100-Electronic Techniques for Engineering
			ans.append(twoChoiceReq(takenClasses, 'Electronics', 'ELENG.40', 'EE 40', 'ELENG.100', 'EE 100', "The sophomore year Electrical Engineering requirement of one of two classes"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#BioE 102-Biomechanics
			ans.append(basicReq(takenClasses, 'BIOENG.102', 'BioE 102', "The junior year Biomechanics requirement"))
			#BioE 104-Biological Transport Phenomena
			ans.append(basicReq(takenClasses, 'BIOENG.104', 'BioE 104', "The junior year Biological Transport Phenomena requirement"))
			#Chemistry 120B-Physical Chemistry OR E115
			ans.append(twoChoiceReq(takenClasses, 'Chemistry', 'CHEM.120B', 'Chem 120B', 'ENGIN.115', 'E 115', "The junior year Physical Chemistry requirement of Chem 120B or E 115"))
			#BioE110-Biomedical Physiology for Engineers or BioE 113-Stem Cells and Technologies
			ans.append(twoChoiceReq(takenClasses, 'Biomedical Technology', 'BIOENG.110', 'BioE 110', 'BIOENG.113', 'BioE 113', "The junior year Biomedical Technology requirement of BioE 110 or 113"))
			#Molecular and Cell Biology C100A Biophysical Chemistry OR MCB 102 - Survey of the Principles of Biochemistry and Molecular Biology
			ans.append(twoChoiceReq(takenClasses, 'Biochemistry', 'MCELLBI.C100A', 'MCB C100A', 'MCELLBI.102', 'MCB 102', "The junior year Biochemistry requirement of MCB C100A or 102"))
			#MSE 102-Bonding Crystallography and Crystal Defects
			ans.append(basicReq(takenClasses, 'MATSCI.102', 'MatSci 102', "The junior year Bonding Crystallography and Crystal Defects requirement"))
			#MSE 104-Characterization of Materials
			ans.append(basicReq(takenClasses, 'MATSCI.104', 'MatSci 104', "The junior year Characterization of Materials requirement"))
			#BioE 115-Cell Biology Lab for Engineers OR MSE 130-Experimental Materials Science
			ans.append(twoChoiceReq(takenClasses, 'Labs', 'BIOENG.115', 'BioE 115', 'MATSCI.130', 'MatSci 130', "The senior year Lab requirement of BioE 115 or MatSci 130"))
			#BioE 116-Cell and Tissue Engineering, BioE C117-Structural Aspects of Biomaterials or BioE 111-Functional Biomaterials
			biomat={'BIOENG.116':'BioE 116','BIOENG.C117':'BioE C117','BIOENG.111':'BioE 111'}
			ans.append(manyChoiceReq(takenClasses, 'BioMaterials', biomat, "The senior year BioMaterials requirement of one class"))
			#BioE C118-Biological Performance of Materials
			ans.append(basicReq(takenClasses, 'BIOENG.C118', 'BioE C118', "The senior year Biological Performance of Materials requirement"))
			#MSE 111-Properties of Electronic Materials,MSE 112-Corrosion, OR MSE 113-Mechanical Behavior of Engineering Materials, BioE 121-Introduction to Micro and Nanobiotechnology: BioMEMS OR BioE 150-Introduction to Bionanoscience and Bionanotechnology
			matsci={'MATSCI.111':'MatSci 111','MATSCI.112':'MatSci 112','MATSCI.113':'MatSci 113'}
			ans.append(manyChoiceReq(takenClasses, 'Materials', matsci, "The senior year Materials requirement of one class"))
			ans.append(twoChoiceReq(takenClasses, 'Nanoteachnology', 'BIOENG.121', 'BioE 121', 'BIOENG.150', 'BioE 150', "The senior year Lab requirement of BioE 121 or BioE 150"))
			#MSE 151-Polymeric Materials
			ans.append(basicReq(takenClasses, 'MATSCI.151', 'MatSci 151', "The senior year Polymeric Materials requirement"))
			#Bioengineering Design Project or Research: BioE 121L, 140L, 168L, 192, H194, 196.
			biodes={'BIOENG.121L':'BioE 121L','BIOENG.140L':'BioE 140L','BIOENG.168L':'BioE 168L','BIOENG.192':'BioE 192','BIOENG.H194':'BioE H194','BIOENG.196':'BioE 196'}
			ans.append(manyChoiceReq(takenClasses, 'Bioengineering Design Project or Research', biodes, "The senior year Bioengineering Design Project or Research requirement of one class"))
			#Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement
			if ('MATSCI.111' in takenClasses) and (('MATSCI.112'in takenClasses) or ('MATSCI.113'in takenClasses)):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['MATSCI.111'], 'courseLeft':[]})
			elif('MATSCI.112' in takenClasses) and (('MATSCI.111'in takenClasses) or ('MATSCI.113'in takenClasses)):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['MATSCI.112'], 'courseLeft':[]})
			elif('MATSCI.113' in takenClasses) and (('MATSCI.111'in takenClasses) or ('MATSCI.112'in takenClasses)):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['MATSCI.113'], 'courseLeft':[]})
			elif('MATSCI.103' in takenClasses):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['MATSCI.103'], 'courseLeft':[]})
			elif ('BIOENG.111' in takenClasses) and (('BIOENG.116'in takenClasses) or ('BIOENG.C117'in takenClasses)):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['BIOENG.111'], 'courseLeft':[]})
			elif('BIOENG.116' in takenClasses) and (('BIOENG.111'in takenClasses) or ('BIOENG.C117'in takenClasses)):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['BIOENG.116'], 'courseLeft':[]})
			elif('BIOENG.C117' in takenClasses) and (('BIOENG.111'in takenClasses) or ('BIOENG.116'in takenClasses)):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['BIOENG.C117'], 'courseLeft':[]})
			elif('BIOENG.121' in takenClasses) and('BIOENG.150' in takenClasses):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['BIOENG.121'], 'courseLeft':[]})
			elif('BIOENG.H194' in takenClasses) and(('BIOENG.121L' in takenClasses)or('BIOENG.140L' in takenClasses)or('BIOENG.168L' in takenClasses)or('BIOENG.192' in takenClasses)or('BIOENG.196' in takenClasses)):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['BIOENG.H194'], 'courseLeft':[]})
			elif('BIOENG.113' in takenClasses):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':['BIOENG.113'], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"Choose course from the Technical Electives List. BIOE 111*, 113*, 116*, C117*, 121*, H194*; MSE 103*, 111*, 112* or 113*. Cannot be a course you have taken to fulfill another requirement",'courseDone':[], 'courseLeft':['BioE 111','BioE 113','BioE 116','BioE C117','BioE 121', 'BioE H194','MatSci 103','MatSci 111', 'MatSci 112', 'MatSci 113']})
			return ans
		# Electrical Engineering & Computer Sciences and Materials Science & Engineering
		elif(major=='EECSMATSCI'):
			#E 7 , Introduction to Applied Computing or CS 61A
			ans.append(twoChoiceReq(takenClasses,"Introduction to Applied Computing", 'ENGIN.7', 'E 7', 'COMPSCI.61A', 'CompSci 61A', "The freshman year Introduction to Applied Computing requirement of either E 7 or CS 61A"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Computer Science 61B, Data Structures
			ans.append(basicReq(takenClasses, 'COMPSCI.61B', 'CS 61B', "The sophomore year Programming Data Structures requirement"))
			#E 45-Properties of Materials
			ans.append(basicReq(takenClasses, 'ENGIN.45', 'E 45', "The sophomore year Properties of Materials requirement"))
			#EE 40-Introduction to Microelectronic Circuits
			ans.append(basicReq(takenClasses, 'ELENG.40', 'EE 40',  "The sophomore year Electrical Engineering requirement"))
			#CS 61C-Machine Structures or EE 20N-Structure and Interpretation of Systems and Signals
			ans.append(twoChoiceReq(takenClasses, 'Systems','ELENG.20N', 'EE 20N', 'COMPSCI.61C','CS 61C', "The junior year Systems requirement of EE 20N or CS 61C"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Physics 7C-Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append( twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#E 115-Engineering Thermodynamics or Physics 112-Statistical and Thermal Physics
			ans.append(twoChoiceReq(takenClasses, 'Thermal Physics', 'ENGIN.115', 'E 115', 'TPHYSICS.112', 'Physics 115', "The junior year Thermal Physics requirement of E 115 or Physics 112"))
			#EE 105-Macroelectronic Devices and Circuits
			ans.append(basicReq(takenClasses, 'ELENG.105', 'EE 105', "The senior year Macroelectronic Devices and Circuits requirement"))
			#EE 126-Probability and Random Processes, Statistics 25-Introduction to Probability and Statistics for Engineers, or Statistics 134-Concepts of Probability
			probs={'ELENG.126':'EE 126','STAT.25':'Stats 25','STAT.134':'Stats 134'}
			ans.append(manyChoiceReq(takenClasses, 'Probability', probs , "The junior year Probability requirement of one of the given classes"))
			#MSE 102-Bonding Crystallography and Crystal Defects
			ans.append(basicReq(takenClasses, 'MATSCI.102', 'MatSci 102', "The junior year Bonding Crystallography and Crystal Defects requirement"))
			#MSE 103-Phase Transformation and Kinetics
			ans.append(basicReq(takenClasses, 'MATSCI.103', 'MatSci 103', "The junior year Phase Transformation and Kinetics requirement"))
			#MSE 104-Characterization of Materials
			ans.append(basicReq(takenClasses, 'MATSCI.104', 'MatSci 104', "The junior year Characterization of Materials requirement"))
			#Physics 137A-Quantum Mechanics
			ans.append(basicReq(takenClasses, 'PHYSICS.137A', 'Physics 137A', "The junior year Quantum Mechanics requirement"))
			#EE 117-Electromagnetic Fields and Waves
			ans.append(basicReq(takenClasses, 'ELENG.117', 'EE 117', "The senior year Electromagnetic Fields and Waves requirement"))
			#EE 140-Linear Integrated Circuits or EE 141-Digital Integrated Circuits
			ans.append(twoChoiceReq(takenClasses, 'Integrated Circuits', 'ELENG.140', 'EE 140', 'ELENG.141', 'EE 141', "The senior year Integrated Circuits requirement of EE 140 or 141"))
			#MSE 111-Properties of Electronic Materials
			ans.append(basicReq(takenClasses, 'MATSCI.111', 'MatSci 111', "The senior year Properties of Electronic Materials requirement"))
			#MSE 130-Experimental Materials Science
			ans.append(basicReq(takenClasses, 'MATSCI.130', 'MatSci 130', "The senior year Experimental Materials Science requirement"))
			#Physics 141A-Solid State Physics
			ans.append(basicReq(takenClasses, 'PHYSICS.141A', 'Physics 141A', "The senior year Solid State Physics requirement of Physics 141A"))
			#Technical electives must include two courses: one course from the following: CS 150; EE 119, 143; and at least three 3 units from the MSE 120 series courses(Not 124,126,127,128,129).
			techone={'COMPSCI.150':'CS 150','ELENG.119':'EE 119','ELENG.143':'EE 143'}
			#all MSE 120 series course are 3+ units
			techtwo={'MATSCI.120':'MatSci 120','MATSCI.121':'MatSci 121','MATSCI.122':'MatSci 122','MATSCI.123':'MatSci 123','MATSCI.125':'MatSci 125'}
			ans.append(manyChoiceReq(takenClasses, 'Technical Elective One', techone, "The senior year Technical Elective requirement of CS 150, EE 119, or EE 143"))
			ans.append(manyChoiceReq(takenClasses, 'Technical Elective Two', techtwo, "The senior year Technical Elective requirement of 3 units from the MSE 120 series course"))
			return ans
		# Electrical Engineering & Computer Sciences and Nuclear Engineering
		elif(major=='EECSNUCENG'):
			#Chemistry 1A and 1AL-General Chemistry or Chemistry 4A-General Chemistry and Quantitative Analysis
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#NE 92-Issues in Nuclear Science and Technology
			ans.append(basicReq(takenClasses, 'NUCENG.92', 'NucEng 92', "The freshman year Issues in Nuclear Science and Technology requirement"))
			#CS 61A-Structure and Interpretation of Computer Programs
			ans.append(basicReq(takenClasses, 'COMPSCI.61A', 'CS 61A', "The freshman year Structure and Interpretation of Computer Programs requirement"))
			#CS 61B-Data Structures
			ans.append(basicReq(takenClasses, 'COMPSCI.61B', 'CS 61B', "The freshman year Data Structures requirement"))
			#E 45-Properties of Materials
			ans.append(basicReq(takenClasses, 'ENGIN.45', 'E 45', "The sophomore year Properties of Materials requirement"))
			#EE 40-Introduction to Microelectronic Circuits
			ans.append(basicReq(takenClasses, 'ELENG.40', 'EE 40',  "The sophomore year Electrical Engineering requirement"))
			#EE 20N-Structure and Interpretation of Systems and Signals
			ans.append(basicReq(takenClasses, 'ELENG.20N', 'EE 20N', "The sophomore year Structure and Interpretation of Systems and Signals requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append( twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Physics 7C-Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The sophomore year Physics for Scientists and Engineers requirement"))
			#E 115-Engineering Thermodynamics
			ans.append(basicReq(takenClasses, 'ENGIN.115', 'E 115', "The junior year Engineering Thermodynamics requirement"))
			#EE 120-Signals and Systems
			ans.append(basicReq(takenClasses, 'ELENG.120', 'EE 120', "The junior year Signals and Systems requirement"))
			#EE 126-Probability and Random Processes, Statistics 25-Introduction to Probability and Statistics for Engineers, or Statistics 134-Concepts of Probability
			probs={'ELENG.126':'EE 126','STAT.25':'Stats 25','STAT.134':'Stats 134'}
			ans.append(manyChoiceReq(takenClasses, 'Probability', probs , "The junior year Probability requirement of one of the given classes"))
			#NE 101-Nuclear Reactions and Radiation
			ans.append(basicReq(takenClasses, 'NUCENG.101', 'NucEng 101', "The junior year Nuclear Reactions and Radiation requirement"))
			#NE 150-Nuclear Reactor Theory
			ans.append(basicReq(takenClasses, 'NUCENG.150', 'NucEng 150', "The junior year Nuclear Reactor Theory requirement"))
			#NE 104-Radiation Detection Lab
			ans.append(basicReq(takenClasses, 'NUCENG.104', 'NucEng 104', "The junior year Radiation Detection Lab requirement"))
			#EE 105-Macroelectronic Devices and Circuits
			ans.append(basicReq(takenClasses, 'ELENG.105', 'EE 105', "The senior year Macroelectronic Devices and Circuits requirement"))
			#EE 117-Electromagnetic Fields and Waves
			ans.append(basicReq(takenClasses, 'ELENG.117', 'EE 117', "The senior year Electromagnetic Fields and Waves requirement"))
			#NE 170A-Nuclear Engineering Design
			ans.append(basicReq(takenClasses, 'NUCENG.170A', 'NucEng 170A', "The senior year Nuclear Engineering Design requirement"))
			#Technical Electives:
			#At least 9 units of upper-division nuclear engineering courses from NE 107, 162, 120, 124, 155, 161, 167, 175, 155, 107, 130, 180
			techne={'NUCENG.107':'NucEng 107','NUCENG.162':'NucEng 162','NUCENG.120':'NucEng 120','NUCENG.124':'NucEng 124','NUCENG.155':'NucEng 155','NUCENG.161':'NucEng 161','NUCENG.167':'NucEng 167','NUCENG.175':'NucEng 175','NUCENG.155':'NucEng 155','NUCENG.107':'NucEng 107','NUCENG.130':'NucEng 130','NUCENG.180':'NucEng 180'}
			num=0
			neTaken=[]
			neNotTaken=[]
			for key in techne:
				if key in takenClasses:
					neTaken.append(techne[key])
					num+=units(key)
				else:
					neNotTaken.append(techne[key])
			if num>=9:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 9 units of upper-division nuclear engineering courses from NE 107, 162, 120, 124, 155, 161, 167, 175, 155, 107, 130, 180",'courseDone':neTaken, 'courseLeft':neNotTaken})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"At least 9 units of upper-division nuclear engineering courses from NE 107, 162, 120, 124, 155, 161, 167, 175, 155, 107, 130, 180."+"You have only taken"+str(num),'courseDone':neTaken, 'courseLeft':neNotTaken})
			#At least 8 units of upper division El Eng courses from  EE 118, 119, 239, 130, 131, 140, 141, 143,113, 114, 128, 134, 137A, 137B
			techee={'ELEN.118':'EE 118','ELEN.119':'EE 119','ELEN.239':'EE 239','ELEN.130':'EE 130','ELEN.131':'EE 131','ELEN.140':'EE 140','ELEN.141':'EE 141','ELEN.143':'EE 143','ELEN.113':'EE 113','ELEN.114':'EE 114','ELEN.128':'EE 128','ELEN.134':'EE 134','ELEN.137A':'EE 137A','ELEN.137B':'EE 137B'}
			num=0
			eeTaken=[]
			eeNotTaken=[]
			for key in techee:
				if key in takenClasses:
					eeTaken.append(techee[key])
					num+=units(key)
				else:
					eeNotTaken.append(techee[key])
			if num>=8:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 8 units of upper division El Eng courses from  EE 118, 119, 239, 130, 131, 140, 141, 143,113, 114, 128, 134, 137A, 137B",'courseDone':neTaken, 'courseLeft':neNotTaken})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"At least 8 units of upper division El Eng courses from  EE 118, 119, 239, 130, 131, 140, 141, 143,113, 114, 128, 134, 137A, 137B"+"You have only taken"+str(num),'courseDone':neTaken, 'courseLeft':neNotTaken})
			return ans
		# Materials Science & Engineering and Mechanical Engineering
		elif(major=='MATMECENG'):
			#Chemistry 1A and 1AL-General Chemistry or Chemistry 4A-General Chemistry and Quantitative Analysis
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#E 7 , Introduction to Applied Computing
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7',  "The freshman year Introduction to Applied Computing requirement of E 7"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#UCB Engineering 10
			ans.append(basicReq(takenClasses, 'ENGIN.10', 'E 10', "The sophomore year Engineering Design and Analysis requirement"))
			#E 45-Properties of Materials
			ans.append(basicReq(takenClasses, 'ENGIN.45', 'E 45', "The sophomore year Properties of Materials requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append( twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#ME 40-Thermodynamics
			ans.append(basicReq(takenClasses, 'MECENG.40', 'MecEng 40', "The sophomore year Thermodynamics requirement"))
			#ME C85-Introduction to Solid Mechanics
			ans.append(basicReq(takenClasses, 'MECENG.C85', 'MecEng C85', "The sophomore year Introduction to Solid Mechanics requirement"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#EE 40-Introduction to Microelectronic Circuits or EE 100-Electronic Techniques for Engineering
			ans.append(twoChoiceReq(takenClasses, 'Electronics', 'ELENG.40', 'EE 40', 'ELENG.100', 'EE 100', "The sophomore year Electrical Engineering requirement of one of two classes"))
			#ME 104-Engineering Mechanics II (Dynamics)
			ans.append(basicReq(takenClasses, 'MECENG.104', 'MecEng 104', "The junior year Engineering Mechanics II requirement"))
			#ME 106-Fluid Mechanics
			ans.append(basicReq(takenClasses, 'MECENG.106', 'MecEng 106', "The junior year Fluid Mechanics requirement"))
			#ME 108-Introduction to Engineering Materials
			ans.append(basicReq(takenClasses, 'MECENG.108', 'MecEng 108', "The junior year Introduction to Engineering Materials requirement"))
			#ME 109-Heat Transfer
			ans.append(basicReq(takenClasses, 'MECENG.109', 'MecEng 109', "The junior year Heat Transfer requirement"))
			#ME 132-Dynamic Systems and Feedback
			ans.append(basicReq(takenClasses, 'MECENG.132', 'MecEng 132', "The junior year Dynamic Systems and Feedback requirement"))
			#MSE 102-Bonding Crystallography and Crystal Defects
			ans.append(basicReq(takenClasses, 'MATSCI.102', 'MatSci 102', "The junior year Bonding Crystallography and Crystal Defects requirement"))
			#MSE 103-Phase Transformation and Kinetics
			ans.append(basicReq(takenClasses, 'MATSCI.103', 'MatSci 103', "The junior year Phase Transformation and Kinetics requirement"))
			#MSE 104-Characterization of Materials
			ans.append(basicReq(takenClasses, 'MATSCI.104', 'MatSci 104', "The junior year Characterization of Materials requirement"))
			#ME 102A-Experimentation and Measurement
			ans.append(basicReq(takenClasses, 'MECENG.102A', 'MecEng 102A', "The senior year Experimentation and Measurement requirement"))
			#ME 102B-Mechanical Engineering Design
			ans.append(basicReq(takenClasses, 'MECENG.102B', 'MecEng 102B', "The senior year Mechanical Engineering Design requirement"))
			#ME 107-Mechanical Engineering Laboratory
			ans.append(basicReq(takenClasses, 'MECENG.107', 'MecEng 107', "The senior year Mechanical Engineering Laboratory requirement"))
			#MSE 112-Corrosion
			ans.append(basicReq(takenClasses, 'MATSCI.112', 'MatSci 112', "The senior year Corrosion requirement"))
			#MSE 130-Experimental Materials Science
			ans.append(basicReq(takenClasses, 'MATSCI.130', 'MatSci 130', "The senior year Experimental Materials Science requirement"))
			#A total of 12 upper division technical elective units are required.
			num=0
			req={'MECENG.104','MECENG.106','MECENG.107','MECENG.108','MECENG.109', 'MECENG.132', 'MECENG.102A','MECENG.102B','MATSCI.102','MATSCI.103','MATSCI.104','MATSCI.112','MATSCI.130'}
			for item in takenClasses:
				if(not item in req) and(not re.search(r'POLSCI.1\d\d',item))and((re.search(r'PHYSICS.1\d\d',item))or(re.search(r'ENG.1\d\d',item))or(re.search(r'ENGIN.1\d\d',item))or(re.search(r'MATH.1\d\d',item))or(re.search(r'SCI.1\d\d',item))or(re.search(r'STAT.1\d\d',item))or(re.search(r'CHM.1\d\d',item))or(re.search(r'CHEM.1\d\d',item))or(re.search(r'BIOLOGY.1\d\d',item))or(re.search(r'ASTRON.1\d\d',item))or(re.search(r'BIO.1\d\d',item)) or(re.search(r'BI.1\d\d',item))or (re.search(r'SC.1\d\d',item))):
					num+=units(item)
			if (num>=12):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 12 units of approved upper division technical subjects (mathematics, statistics, science, and engineering)",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"At least 12 units of approved upper division technical subjects (mathematics, statistics, science, and engineering)"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			"""advancement"""
			#These must include 6 units of upper-division Mechanical Engineering courses, one of which must be from the following list: ME 101,110,C117,119,128,130,135,146,165,C176 or Engin 128.
			mereq={'MECENG.104','MECENG.106','MECENG.107','MECENG.108','MECENG.109', 'MECENG.132', 'MECENG.102A','MECENG.102B'}
			metech={'MECENG.101':'MecEng 101','MECENG.110':'MecEng 110','MECENG.C117':'MecEng C117','MECENG.119':'MecEng 119','MECENG.128':'MecEng 128','MECENG.130':'MecEng 130','MECENG.135':'MecEng 135','MECENG.146':'MecEng 146','MECENG.165':'MecEng 165','MECENG.C176':'MecEng C176','ENGIN.128':'E 128'}
			ans.append(manyChoiceReq(takenClasses, 'Technical Elective', metech, "Technical electives must include one class from the list"))
			num=0
			for item in takenClasses:
				if((re.search(r'MECENG.1\d\d',item))and(not item in mereq)):
					num+=units(item)
			if (num>=6):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 6 units of upper-division Mechanical Engineering courses",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"6 units of upper-division Mechanical Engineering courses"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			#In addition, 3 units must be from the MSE 120 series.
			me120={'MATSCI.120':'MatSci 120','MATSCI.121':'MatSci 121','MATSCI.122':'MatSci 122','MATSCI.123':'MatSci 123','MATSCI.125':'MatSci 125'}
			ans.append(manyChoiceReq(takenClasses, 'Technical Elective', me120, "3 units of the technical electives must be from the MSE 120 series"))
			#ME 108-Introduction to Engineering Materials or MSE 113-Mechanical Behavior of Engineering Materials
			ans.append(twoChoiceReq(takenClasses,'Materials', 'MECENG.108', 'MecEng 108','MATSCI.113','MatSci 113', "The junior year Materials requirement of ME 108 or MSE 113"))
			#E 28-Graphics Communication in Engineering
			ans.append(basicReq(takenClasses, 'ENGIN.28', 'E 28', "The sophomore year Graphics Communication in Engineering requirement"))
			return ans
		# Materials Science & Engineering and Nuclear Engineering
		elif(major=='MATNUCENG'):
			#Chemistry 1A and 1AL-General Chemistry or Chemistry 4A-General Chemistry and Quantitative Analysis
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#E 7 , Introduction to Applied Computing
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7',  "The freshman year Introduction to Applied Computing requirement of E 7"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#NE 92-Issues in Nuclear Science and Technology
			ans.append(basicReq(takenClasses, 'NUCENG.92', 'NucEng 92', "The freshman year Issues in Nuclear Science and Technology requirement"))
			#E 45-Properties of Materials
			ans.append(basicReq(takenClasses, 'ENGIN.45', 'E 45', "The sophomore year Properties of Materials requirement"))
			#EE 40-Introduction to Microelectronic Circuits or EE 100-Electronic Techniques for Engineering
			ans.append(twoChoiceReq(takenClasses, 'Electronics', 'ELENG.40', 'EE 40', 'ELENG.100', 'EE 100', "The sophomore year Electrical Engineering requirement of one of two classes"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#ME C85-Introduction to Solid Mechanics
			ans.append(basicReq(takenClasses, 'MECENG.C85', 'MecEng C85', "The sophomore year Introduction to Solid Mechanics requirement"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Physics 7C-Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The sophomore year Physics for Scientists and Engineers requirement"))
			#NE 101-Nuclear Reactions and Radiation
			ans.append(basicReq(takenClasses, 'NUCENG.101', 'NucEng 101', "The junior year Nuclear Reactions and Radiation requirement"))
			#NE 150-Nuclear Reactor Theory
			ans.append(basicReq(takenClasses, 'NUCENG.150', 'NucEng 150', "The junior year Nuclear Reactor Theory requirement"))
			#NE 104-Radiation Detection Lab
			ans.append(basicReq(takenClasses, 'NUCENG.104', 'NucEng 104', "The junior year Radiation Detection Lab requirement"))
			#E 115-Engineering Thermodynamics
			ans.append(basicReq(takenClasses, 'ENGIN.115', 'E 115', "The junior year Engineering Thermodynamics requirement"))
			#MSE 102-Bonding Crystallography and Crystal Defects
			ans.append(basicReq(takenClasses, 'MATSCI.102', 'MatSci 102', "The junior year Bonding Crystallography and Crystal Defects requirement"))
			#MSE 103-Phase Transformation and Kinetics
			ans.append(basicReq(takenClasses, 'MATSCI.103', 'MatSci 103', "The junior year Phase Transformation and Kinetics requirement"))
			#MSE 104-Characterization of Materials
			ans.append(basicReq(takenClasses, 'MATSCI.104', 'MatSci 104', "The junior year Characterization of Materials requirement"))
			#Technical electives must include at least 9 units of upper division NE courses and at least 3 units from the MSE 120 series courses.
			nereq={'NUCENG.101','NUCENG.104','NUCENG.150','NUCENG.120','NUCENG.170A'}
			num=0
			for item in takenClasses:
				if((re.search(r'NUCENG.1\d\d',item))and(not item in nereq)):
					num+=units(item)
			if (num>=9):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 9 units of upper division NE courses",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"At least 9 units of upper division NE courses"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			me120={'MATSCI.120':'MatSci 120','MATSCI.121':'MatSci 121','MATSCI.122':'MatSci 122','MATSCI.123':'MatSci 123','MATSCI.125':'MatSci 125'}
			ans.append(manyChoiceReq(takenClasses, 'Technical Elective', me120, "3 units of the technical electives must be from the MSE 120 series"))
			#MSE 111-Properties of Electronic Materials
			ans.append(basicReq(takenClasses, 'MATSCI.111', 'MatSci 111', "The senior year Properties of Electronic Materials requirement"))
			#MSE 112-Corrosion
			ans.append(basicReq(takenClasses, 'MATSCI.112', 'MatSci 112', "The senior year Corrosion requirement"))
			#MSE 113-Mechanical Behavior of Materials
			ans.append(basicReq(takenClasses, 'MATSCI.113', 'MatSci 113', "The senior year Mechanical Behavior of Materials requirement"))
			#MSE 130-Experimental Materials Science
			ans.append(basicReq(takenClasses, 'MATSCI.130', 'MatSci 130', "The senior year Experimental Materials Science requirement"))
			#NE 120-Nuclear Materials
			ans.append(basicReq(takenClasses, 'NUCENG.120', 'NucEng 120', "The senior year Nuclear Materials requirement"))
			#NE 170A-Nuclear Engineering Design
			ans.append(basicReq(takenClasses, 'NUCENG.170A', 'NucEng 170A', "The senior year Nuclear Engineering Design requirement"))
			return ans
		# Mechanical Engineering and Nuclear Engineering
		elif(major=='MECNUCENG'):
			#Chemistry 1A and 1AL-General Chemistry or Chemistry 4A-General Chemistry and Quantitative Analysis
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Engineering 10-Engineering Design and Analysis or Nuclear Engineering 92-Issues in Nuclear Science and Technology
			ans.append(twoChoiceReq(takenClasses,'Design', 'ENGIN.10', 'E 10','NUCENG.92','NucEng 92', "The freshman year requirement of E 10 or NucEng 92"))
			#E 7 , Introduction to Applied Computing
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7',  "The freshman year Introduction to Applied Computing requirement of E 7"))
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#E 28-Graphics Communication and Engineering
			ans.append(basicReq(takenClasses, 'ENGIN.28', 'E 28', "The sophomore year Graphics Communication and Engineering requirement of E 28"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#ME 40-Thermodynamics
			ans.append(basicReq(takenClasses, 'MECENG.40', 'MecEng 40', "The sophomore year Thermodynamics requirement"))
			#ME C85-Introduction to Solid Mechanics
			ans.append(basicReq(takenClasses, 'MECENG.C85', 'MecEng C85', "The sophomore year Introduction to Solid Mechanics requirement"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Physics 7C-Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The sophomore year Physics for Scientists and Engineers requirement"))
			#EE 40-Introduction to Microelectronic Circuits or EE 100-Electronic Techniques for Engineering
			ans.append(twoChoiceReq(takenClasses, 'Electronics', 'ELENG.40', 'EE 40', 'ELENG.100', 'EE 100', "The junior year Electrical Engineering requirement of one of two classes"))
			#ME 104-Engineering Mechanics II (Dynamics)
			ans.append(basicReq(takenClasses, 'MECENG.104', 'MecEng 104', "The junior year Engineering Mechanics II requirement"))
			#ME 106-Fluid Mechanics
			ans.append(basicReq(takenClasses, 'MECENG.106', 'MecEng 106', "The junior year Fluid Mechanics requirement"))
			#ME 108-Introduction to Engineering Materials
			ans.append(basicReq(takenClasses, 'MECENG.108', 'MecEng 108', "The junior year Introduction to Engineering Materials requirement"))
			#ME 109-Heat Transfer
			ans.append(basicReq(takenClasses, 'MECENG.109', 'MecEng 109', "The junior year Heat Transfer requirement"))
			#ME 132-Dynamic Systems and Feedback
			ans.append(basicReq(takenClasses, 'MECENG.132', 'MecEng 132', "The junior year Dynamic Systems and Feedback requirement"))
			#NE 101-Nuclear Reactions and Radiation
			ans.append(basicReq(takenClasses, 'NUCENG.101', 'NucEng 101', "The junior year Nuclear Reactions and Radiation requirement"))
			#NE 150-Nuclear Reactor Theory
			ans.append(basicReq(takenClasses, 'NUCENG.150', 'NucEng 150', "The junior year Nuclear Reactor Theory requirement"))
			#ME 102A-Experimentation and Measurement
			ans.append(basicReq(takenClasses, 'MECENG.102A', 'MecEng 102A', "The senior year Experimentation and Measurement requirement"))
			#ME 102B-Mechanical Engineering Design
			ans.append(basicReq(takenClasses, 'MECENG.102B', 'MecEng 102B', "The senior year 102B-Mechanical Engineering Design requirement"))
			#ME 107-Mechanical Engineering Laboratory
			ans.append(basicReq(takenClasses, 'MECENG.107', 'MecEng 107', "The senior year Mechanical Engineering Laboratory requirement"))
			#NE 104-Radiation Detection Lab
			ans.append(basicReq(takenClasses, 'NUCENG.104', 'NucEng 104', "The senior year Radiation Detection Lab requirement"))
			#NE 170A-Nuclear Engineering Design
			ans.append(basicReq(takenClasses, 'NUCENG.170A', 'NucEng 170A', "The senior year Nuclear Engineering Design requirement"))
			#Technical elective units include at least 6 units of upper-division elective Mechanical Engineering courses and
			#6 units of upper division Nuclear Engineering courses
			#Not ME(104,106,108,109,132,102A,102B,107) NE(101,150,104,170A)
			nereq={'NUCENG.101','NUCENG.104','NUCENG.150','NUCENG.170A'}
			num=0
			for item in takenClasses:
				if((re.search(r'NUCENG.1\d\d',item))and(not item in nereq)):
					num+=units(item)
			if (num>=6):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 6 units of upper division NE courses",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"At least 6 units of upper division NE courses"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})
			mereq={'MECENG.104','MECENG.106','MECENG.107','MECENG.108','MECENG.109', 'MECENG.132', 'MECENG.102A','MECENG.102B'}
			num=0
			for item in takenClasses:
				if((re.search(r'MECENG.1\d\d',item))and(not item in mereq)):
					num+=units(item)
			if (num>=6):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':"At least 6 units of upper-division Mechanical Engineering courses",'courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':"6 units of upper-division Mechanical Engineering courses"+"You have only taken"+str(num),'courseDone':[], 'courseLeft':[]})

			return ans
		# Environmental Engineering Science
		elif(major=='ENVENG'):
			#Math 1A
			ans.append(basicReq(takenClasses, 'MATH.1A', 'Math 1A', "Part of the freshman year Calculus requirement of Math 1A"))
			#Math 1B
			ans.append(basicReq(takenClasses, 'MATH.1B', 'Math 1B', "Part of the freshman year Calculus requirement of Math 1B"))
			#Physics 7A
			ans.append(basicReq(takenClasses, 'PHYSICS.7A', 'Physics 7A', "The freshman year Physics for Scientists and Engineers requirement"))
			#Math 53 -54 , Multivariable Calculus, Linear Algebra, Diff. Eqns.
			ans.append(twoReq(takenClasses,'Multivariable Calculus, Linear Algebra, Differential Equations', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', "The sophomore year mathematics requirement of both Math 53 and 54"))
			#Physics 7B , Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7B', 'Physics 7B', "The sophomore year Physics for Scientists and Engineers requirement"))
			#Chemistry 1A and 1AL or 4A
			if(('CHEM.1A' in takenClasses) and ('CHEM.1AL' in takenClasses)):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 1A', 'Chem 1AL'], 'courseLeft':['Chem 4A']})
			elif('CHEM.4A' in takenClasses):
				ans.append({'reqName':'Chemistry', 'reqCompleted':True, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':['Chem 4A'], 'courseLeft':['Chem 1A', 'Chem 1AL']})
			else:
				ans.append({'reqName':'Chemistry', 'reqCompleted':False, 'reqDescription':"Part of the freshman year Chemistry requirement",'courseDone':[], 'courseLeft':['Chem 1A', 'Chem 1AL','Chem 4A']})
			#E 7 , Introduction to Applied Computing
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7', "The freshman year Introduction to Applied Computing requirement of E 7"))
			#Engineering Elective CE 11
			ans.append(basicReq(takenClasses, 'CIVENG.11', 'CivEng 11',"The sophomore year requirement of CE 11"))
			#CE C30/ME C85-Introduction to Solid Mechanics
			ans.append(twoChoiceReq(takenClasses,"Introduction to Solid Mechanics", 'CHMENG.C30', 'CE C30', 'MECENG.C85', 'ME C85', "The sophomore year Introduction to Solid Mechanics requirement of either CE C30 or ME C85"))
			#Complete three courses from the following list: Biology 1A/1AL; Biology 1b; Chemistry 1B; 3A/3AL, 4B; Physics 7C; Earth and Planetary Science 50. Note: Approved scores on Biology AP, IB or A-Level Exams can satisfy 2 of the 3 basic science electives.
			science={'BIOLOGY.1A':'Bio 1A','Biology.1B':'Bio 1B','CHEM.1B':'Chem 1B','CHEM.3A':'Chem 3A','CHEM.4B':'Chem 4B','PHYSICS.7C':'Physics 7C','EPS.50':'EPS 50'}
			ans.append(doSomeManyChoiceReq(takenClasses,'Basic Science Electives',science,"You must complete 3 of the classes in the following list",3))
			#Fluid Mechanics: CE 100, ME 106, or Chem E 150A
			fluid={'CIVENG.100':'CE 100', 'MECENG.106':'ME 106','CHMENG.150A':'ChemE 150A'}
			ans.append(manyChoiceReq(takenClasses,'Fluid Mechanics',fluid,"You must complete one of the following three choices of fluid mechanics courses"))
			#Thermodynamics: ME 40, E 115, or ChemE 141
			thermo={'ENGIN.115':'E 115', 'MECENG.40':'ME 40','CHMENG.141':'ChemE 141'}
			ans.append(manyChoiceReq(takenClasses,'Thermodynamics',thermo,"You must complete one of the following three choices of thermodynamics courses"))
			#CE 111-Environmental Engineering
			ans.append(basicReq(takenClasses,'CHMENG.111', 'CE 111',"The senior year Air Pollutant Emissions and Control or Environmental Engineering requirement"))
			#CE 103-Hydrology or CE 115-Water Chemistry
			ans.append(twoChoiceReq(takenClasses,'Hydrology','CIVENG.103','CE 103','CIVENG.115','CE 115',"You are reqquired to take one of the two following Hydrology courses"))
			#Math/Computing Elective: any one of E 117, E177; Math 104, 110, 126, 128A, 170, 185; Stat 133, 134
			compute={'ENGIN.117':'E 117','MATH.104':'Math 104','MATH.110':'Math 110','MATH.126':'Math 126','MATH.128A':'Math 128A','MATH.170':'Math 170','MATH.185':'Math 185','STAT.133':'Stats 133','STAT.134':'Stats 134'}
			ans.append(manyChoiceReq(takenClasses,'Math/Computing Elective',compute,"You must complete one of the following choices of math or computing courses"))
			#The 12 units of cluster courses are in addition to engineering and science courses used to fulfill other requirements of the program. See approved cluster course list for options.
			#Air Pollution and Climate Change: Architecture 140; BioE C181; CE C106, 107, 108; EE 134, 137A; MSE 136; ME 109, 140, 146; NE 161
			#Biotechnology: BioE C181; ChemE 140, 142, 170A, 170B, 170L; CE 112, 114; MCB C112 and C112L, 113, C116; Plant and Microbial Biology 120, 120L, 122, 180
			#Ecosystems and Ecological Engineering: CE 113, 114; ESPM C103, C104; Integrative Biology C149, 151, 151L, 152, 153, 153LF, 154
			#Environmental Fluid Mechanics: CE 101, 103, 105, 173; Earth and Planetary Science 117, C129
			#Geoengineering:CE 171, 172, 173, 175, 176, C178, 281; Earth and Planetary Science 117
			#Water Quality : CE 112, 113, 114, 115, C116, 173; Integrative Biology 152; ESPM 120.
			cluster={'ARCH.140':'Architecture 140','BIOENG.C181':'BioE C181','CIVENG.C106':'CE C106','CIVENG.107':'CE 107','CIVENG.108':'CE 108',
				'ELENG.134':'EE 134','ELENG.137A':'EE 137A','MATSCI.136':'MSE 136','MECENG.109':'ME 109','MECENG.140':'ME 140','MECENG.146':'ME 146',
				'NUCENG.161':'NE 161','CHMENG.140':'ChemE 140','CHMENG.142':'ChemE 142','CHMENG.170A':'ChemE 170A','CHMENG.170B':'ChemE 170B','CHMENG.170L':'ChemE 170L',
				'CIVENG.112':'CE 112','CIVENG.114':'CE 114','ESPM.C103':'ESPM C103','ESPM.C104':'ESPM C104','MCELLBI.C112':'MCB C112','MCELLBI.113':'MCB 113','MCELLBI.C116':'MCB C116',
				'PLANTBI.120':'Plant and Microbial Biology 120','PLANTBI.120L':'Plant and Microbial Biology 120L','PLANTBI.122':'Plant and Microbial Biology 122','PLANTBI.180':'Plant and Microbial Biology 180',
				'CIVENG.113':'CE 113','INTEGBI.C149':'IB C149','INTEGBI.151':'IB 151','INTEGBI.151L':'IB 151L','INTEGBI.152':'IB 152','INTEGBI.153':'IB 153','INTEGBI.153LF':'IB 153LF','INTEGBI.154':'IB 154',
				'CIVENG.101':'CE 101','CIVENG.103':'CE 103','CIVENG.105':'CE 105','CIVENG.173':'CE 173','CIVENG.171':'CE 171','CIVENG.172':'CE 172','CIVENG.175':'CE 175','CIVENG.176':'CE 176','CIVENG.C178':'CE C178',
				'CIVENG.281':'CE 281','CIVENG.115':'CE 115','CIVENG.C116':'CE C116','EPS.117':'EPS 117','EPS.C129':'EPS C129','ESPM.120':'ESPM 120'}
			c=0
			takenCluster=[]
			notTakenCluster=[]
			for key in cluster:
				if key in takenClasses:
					takenCluster.append(cluster[key])
					c+=units(key)
				else:
					notTakenCluster.append(cluster[key])
			if c>=12:
				ans.append({'reqName':'Cluster Electives', 'reqCompleted':True, 'reqDescription':"A required 12 units of cluster electives",'courseDone':takenCluster, 'courseLeft':notTakenCluster})
			else:
				ans.append({'reqName':'Cluster Electives', 'reqCompleted':False, 'reqDescription':"A required 12 units of cluster electives. You have completed "+str(c),'courseDone':takenCluster, 'courseLeft':notTakenCluster})
			#See Advanced Science Course Sequence. Choose one of the sequences of eight to 10 units:
			#Chemistry 112A, 112B, Organic Chemistry
			#Chemistry 120A, 120B, 125
			#Earth and Planetary Science 101, 108, 116, 117, 124, C146
			#Earth and Planetary Science C180, C181, C182; Geography 142
			#ESPM 102A, C103, 111, 112, 120, C128, 131
			#MCB 102, 112/112L
			takenSequence=[]
			notTakenSequence=[]
			sequence={'CHEM.112A':'Chem 112A','CHEM.112B':'Chem 112B','CHEM.120A':'Chem 120A','CHEM.120B':'Chem 120B','CHEM.125':'Chem 125',
				'EPS.101':'EPS 101','EPS.108':'EPS 108','EPS.116':'EPS 116','EPS.117':'EPS 117','EPS.124':'EPS 124','EPS.C146':'EPS C146','EPS.C180':'EPS C180','EPS.C181':'EPS C181','EPS.C182':'EPS C182',
				'GEOG.142':'Geography 142','ESPM.102A':'ESPM 102A','ESPM.C103':'ESPM C103','ESPM.111':'ESPM 111','ESPM.112':'ESPM 112','ESPM.120':'ESPM 120','ESPM.C128':'ESPM C128','ESPM.131':'ESPM 131',
				'MCELLBI.102':'MCB 102','MCELLBI.112':'MCB 112','MCELLBI.112L':'MCB 112L'}
			for key in sequence:
				if key in takenClasses:
					takenSequence.append(sequence[key])
				else:
					notTakenSequence.append(sequence[key])
			tempA={'EPS.101':'EPS 101','EPS.108':'EPS 108','EPS.116':'EPS 116','EPS.117':'EPS 117','EPS.124':'EPS 124','EPS.C146':'EPS C146'}
			unitA=0
			tempB={'EPS.C180':'EPS C180','EPS.C181':'EPS C181','EPS.C182':'EPS C182','GEOG.142':'Geography 142'}
			unitB=0
			tempC={'ESPM.102A':'ESPM 102A','ESPM.C103':'ESPM C103','ESPM.111':'ESPM 111','ESPM.112':'ESPM 112','ESPM.120':'ESPM 120','ESPM.C128':'ESPM C128','ESPM.131':'ESPM 131'}
			unitC=0
			for key in tempA:
				if key in takenClasses:
					unitA+=units(key)
			for key in tempB:
				if key in takenClasses:
					unitB+=units(key)
			for key in tempC:
				if key in takenClasses:
					unitC+=units(key)
			if ((unitA>=8)or(unitB>=8)or(unitC>=8)or(('CHEM.120A' in takenClasses)and('CHEM.120B' in takenClasses)and('CHEM.125' in takenClasses))or(('CHEM.112A' in takenClasses)and('CHEM.112B' in takenClasses))or(('MCELLBI.102' in takenClasses)and('MCELLBI.112' in takenClasses)and('MCELLBI.112L' in takenClasses))):
				ans.append({'reqName':'Advanced Science Course Sequence', 'reqCompleted':True, 'reqDescription':"Choose classes from one of the sequences for a total of eight to 10 units:Chemistry 112A, 112B; Chemistry 120A, 120B, 125;Earth and Planetary Science 101, 108, 116, 117, 124, C146;Earth and Planetary Science C180, C181, C182; Geography 142;ESPM 102A, C103, 111, 112, 120, C128, 131;MCB 102, 112/112L",'courseDone':takenSequence, 'courseLeft':notTakenSequence})
			else:
				ans.append({'reqName':'Advanced Science Course Sequence', 'reqCompleted':False, 'reqDescription':"Choose classes from one of the sequences for a total of eight to 10 units:Chemistry 112A, 112B; Chemistry 120A, 120B, 125;Earth and Planetary Science 101, 108, 116, 117, 124, C146;Earth and Planetary Science C180, C181, C182; Geography 142;ESPM 102A, C103, 111, 112, 120, C128, 131;MCB 102, 112/112L",'courseDone':takenCluster, 'courseLeft':notTakenSequence})
			return ans
		#Should not occur but in the case that the major given does not match
		else:
			raise MyError(major+"is not a valid major at UC Berkeley College of Engineering")

	# College of Chemistry
	if (college=='Chemistry'):
		# College Requirements
		# complete two or more humanities and social science courses from the Breadth Requirement Course List: Group II (Humanities and Social Sciences)
		hss=0
		classesCompleted=[]
		classesNotCompleted=[]
		#all specific allowed classes
		electives={'AFRICAM.4A':'AfricanAmerican 4A','AFRICAM.4B':'AfricanAmerican 4B','AFRICAM.5B':'AfricanAmerican 5B','AFRICAM.5A':'AfricanAmerican 5A','AFRICAM.7A':'AfricanAmerican 7A',
			'AFRICAM.7B':'AfricanAmerican 7B','AFRICAM.8A':'AfricanAmerican 8A','AFRICAM.8B':'AfricanAmerican 8B','AFRICAM.9A':'AfricanAmerican 9A','AFRICAM.9B':'AfricanAmerican 9B',
			'AFRICAM.10A':'AfricanAmerican 10A','AFRICAM.10B':'AfricanAmerican 10B','AFRICAM.11A':'AfricanAmerican 11A','AFRICAM.11B':'AfricanAmerican 11B','AFRICAM.13A':'AfricanAmerican 13B',
			'AFRICAM.14A':'AfricanAmerican 14A','AFRICAM.15A':'AfricanAmerican 15A','AFRICAM.14B':'AfricanAmerican 14B','AFRICAM.19A':'AfricanAmerican 19A','AFRICAM.19B':'AfricanAmerican 19B',
			'AFRICAM.27AC':'AfricanAmerican 27AC','AFRICAM.28AC':'AfricanAmerican 28AC','AFRICAM.30A':'AfricanAmerican 30A','AFRICAM.30B':'AfricanAmerican 30B','AFRICAM.31A':'AfricanAmerican 31A',
			'AFRICAM.31B':'AfricanAmerican 31B','AFRICAM.100':'AfricanAmerican 100','AFRICAM.101':'AfricanAmerican 101','AFRICAM.107':'AfricanAmerican 107','AFRICAM.109':'AfricanAmerican 109',
			'AFRICAM.111':'AfricanAmerican 111','AFRICAM.112A':'AfricanAmerican 112A','AFRICAM.112B':'AfricanAmerican 112B','AFRICAM.114':'AfricanAmerican 114','AFRICAM.115':'AfricanAmerican 115',
			'AFRICAM.116':'AfricanAmerican 116','AFRICAM.117':'AfricanAmerican 117','AFRICAM.118':'AfricanAmerican 118','AFRICAM.119':'AfricanAmerican 119','AFRICAM.121':'AfricanAmerican 121',
			'AFRICAM.122':'AfricanAmerican 122','AFRICAM.123':'AfricanAmerican 123','AFRICAM.124':'AfricanAmerican 124','AFRICAM.125':'AfricanAmerican 125','AFRICAM.131':'AfricanAmerican 131',
			'AFRICAM.132':'AfricanAmerican 132','AFRICAM.133':'AfricanAmerican 133','AFRICAM.134':'AfricanAmerican 134','AFRICAM.137':'AfricanAmerican 137','AFRICAM.138':'AfricanAmerican 138',
			'AFRICAM.139':'AfricanAmerican 139','AFRICAM.140':'AfricanAmerican 140','AFRICAM.142A':'AfricanAmerican 142A','AFRICAM.142B':'AfricanAmerican 142B','AFRICAM.143A':'AfricanAmerican 143A',
			'AFRICAM.143B':'AfricanAmerican 143B','AFRICAM.151B':'AfricanAmerican 151B','AFRICAM.152F':'AfricanAmerican 152F','AFRICAM.153C':'AfricanAmerican 153C','AFRICAM.155':'AfricanAmerican 155',
			'AFRICAM.156AC':'AfricanAmerican 156AC','AFRICAM.158A':'AfricanAmerican 158A','AFRICAM.158B':'AfricanAmerican 158B','AFRICAM.159':'AfricanAmerican 159','AFRICAM.173AC':'AfricanAmerican 173AC',
			'AFRICAM.C178':'AfricanAmerican C178','AFRICAM.190AC':'AfricanAmerican 190AC','AMERSTD.10':'AmericanStudies 10','AMERSTD.C10':'AmericanStudies C10','AMERSTD.10AC':'AmericanStudies 10AC','AMERSTD.101':'AmericanStudies 101',
			'AMERSTD.101AC':'AmericanStudies 101AC','AMERSTD.102':'AmericanStudies 102','AMERSTD.110':'AmericanStudies 110','AMERSTD.H110':'AmericanStudies H110','AMERSTD.C111A':'AmericanStudies C111A',
			'AMERSTD.C111B':'AmericanStudies C111B','AMERSTD.C111C':'AmericanStudies C111C','AMERSTD.C111D':'AmericanStudies C111D','AMERSTD.C111E':'AmericanStudies C111E','AMERSTD.C111F':'AmericanStudies C111F',
			'AMERSTD.C112A':'AmericanStudies C112A','AMERSTD.C112B':'AmericanStudies C112B','AMERSTD.C112C':'AmericanStudies C112C','AMERSTD.C112D':'AmericanStudies C112D','AMERSTD.C112E':'AmericanStudies C112E',
			'AMERSTD.C112F':'AmericanStudies C112F','AMERSTD.C134':'AmericanStudies C134','AMERSTD.139AC':'AmericanStudies 139AC','AMERSTD.C152':'AmericanStudies C152','AMERSTD.C171':'AmericanStudies C171',
			'AMERSTD.C172':'AmericanStudies C172','AMERSTD.C174':'AmericanStudies C174','AMERSTD.178AC':'AmericanStudies 178AC','AMERSTD.179AC':'AmericanStudies 179AC','AMERSTD.189':'AmericanStudies 189',
			'ANTHRO.2':'Antro 2','ANTHRO.2AC':'Antro 2AC','ANTHRO.3':'Antro 3','ANTHRO.3AC':'Antro 3AC','ANTHRO.111':'Antro 111','ANTHRO.114':'Antro 114','ANTHRO.115':'Antro 115','ANTHRO.119':'Antro 119',
			'ANTHRO.121A':'Antro 121A','ANTHRO.121B':'Antro 121B','ANTHRO.121C':'Antro 121C','ANTHRO.121AC':'Antro 121AC','ANTHRO.122':'Antro 122','ANTHRO.122A':'Antro 122A','ANTHRO.122B':'Antro 122B',
			'ANTHRO.122C':'Antro 122C','ANTHRO.122D':'Antro 122D','ANTHRO.122E':'Antro 122E','ANTHRO.122F':'Antro 122F','ANTHRO.122G':'Antro 122G','ANTHRO.124A':'Antro 124A','ANTHRO.123A':'Antro 123A',
			'ANTHRO.123B':'Antro 123B','ANTHRO.123C':'Antro 123C','ANTHRO.123D':'Antro 123D','ANTHRO.123E':'Antro 123E','ANTHRO.123F':'Antro 123F','ANTHRO.124AC':'Antro 124AC','ANTHRO.C125A':'Antro C125A',
			'ANTHRO.C125B':'Antro C125B','ANTHRO.128A':'Antro 128A','ANTHRO.128B':'Antro 128B','ANTHRO.128C':'Antro 128C','ANTHRO.128D':'Antro 128D','ANTHRO.128E':'Antro 128E','ANTHRO.128F':'Antro 128F',
			'ANTHRO.128G':'Antro 128G','ANTHRO.128H':'Antro 128H','ANTHRO.128I':'Antro 128I','ANTHRO.128J':'Antro 128J','ANTHRO.128K':'Antro 128K','ANTHRO.128L':'Antro 128L','ANTHRO.128M':'Antro 128M',
			'ANTHRO.129A':'Antro 129A','ANTHRO.129B':'Antro 129B','ANTHRO.129C':'Antro 129C','ANTHRO.129D':'Antro 129D','ANTHRO.129E':'Antro 129E','ANTHRO.129F':'Antro 129F','ANTHRO.135B':'Antro 135B',
			'ANTHRO.136':'Antro 136','ANTHRO.137':'Antro 137','ANTHRO.138':'Antro 138','ANTHRO.139':'Antro 139','ANTHRO.140':'Antro 140','ANTHRO.141':'Antro 141','ANTHRO.142':'Antro 142','ANTHRO.C146':'Antro C146',
			'ANTHRO.147':'Antro 147','ANTHRO.148':'Antro 148','ANTHRO.149':'Antro 149','ANTHRO.150':'Antro 150','ANTHRO.152':'Antro 152','ANTHRO.155':'Antro 155','ANTHRO.156':'Antro 156','ANTHRO.157':'Antro 157',
			'ANTHRO.158':'Antro 158','ANTHRO.160AC':'Antro 160AC','ANTHRO.161':'Antro 161','ANTHRO.162':'Antro 162','ANTHRO.166':'Antro 166','ANTHRO.169B':'Antro 169B','ANTHRO.169C':'Antro 169C','ANTHRO.170':'Antro 170',
			'ANTHRO.171':'Antro 171','ANTHRO.172AC':'Antro 172AC','ANTHRO.174AC':'Antro 174AC','ANTHRO.179':'Antro 179','ANTHRO.180':'Antro 180','ANTHRO.181':'Antro 181','ANTHRO.183':'Antro 183','ANTHRO.184':'Antro 184','ANTHRO.189':'Antro 189',
			'ARABIC.1A':'Arabic 1A','ARABIC.1B':'Arabic 1B','ARABIC.15B':'Arabic 15B','ARABIC.20A':'Arabic 20A','ARABIC.20B':'Arabic 20B','ARABIC.100A':'Arabic 100A','ARABIC.100B':'Arabic 100B','ARABIC.104B':'Arabic 104B',
			'ARABIC.105B':'Arabic 105B','ARABIC.108':'Arabic 108','ARABIC.111A':'Arabic 111B','ARABIC.190A':'Arabic 190A','ARABIC.190B':'Arabic 190B','ARABIC.190C':'Arabic 190C','ARABIC.190D':'Arabic 190D','ARABIC.190E':'Arabic 19E',
			'ARABIC.190F':'Arabic 190F','ARABIC.190G':'Arabic 190G','ARABIC.190H':'Arabic 190H','ARABIC.190I':'Arabic 190I','ARABIC.190J':'Arabic 190J','ARABIC.190K':'Arabic 190K',
			'ARCH.110AC':'Arch 110AC','ARCH.119':'Arch 119','ARCH.130':'Arch 130','ARCH.133':'Arch 133','ARCH.136':'Arch 136','ARCH.139':'Arch 139','ARCH.170A':'Arch 170A','ARCH.170B':'Arch 170B','ARCH.173':'Arch 173',
			'ARCH.C174':'Arch C174','ARCH.175':'Arch 175','ARCH.176':'Arch 176','ARCH.178':'Arch 178','ARCH.179':'Arch 179',
			'ASAMST.20A':'AsianAmerican 20A','ASAMST.20B':'AsianAmerican 20B','ASAMST.20C':'AsianAmerican 20C','ASAMST.121':'AsianAmerican 121','ASAMST.127':'AsianAmerican 127','ASAMST.128AC':'AsianAmerican 128AC',
			'ASAMST.131':'AsianAmerican 131','ASAMST.132AC':'AsianAmerican 132AC','ASAMST.138':'AsianAmerican 138','ASAMST.141':'AsianAmerican 141','ASAMST.143':'AsianAmerican 143','ASAMST.144':'AsianAmerican 144',
			'ASAMST.145':'AsianAmerican 145','ASAMST.146':'AsianAmerican 146','ASAMST.150':'AsianAmerican 150','ASAMST.151':'AsianAmerican 151','ASAMST.165':'AsianAmerican 165','ASAMST.171':'AsianAmerican 171',
			'ASAMST.172':'AsianAmerican 172','ASAMST.173':'AsianAmerican 173','ASAMST.175':'AsianAmerican 175','ASAMST.176':'AsianAmerican 176','ASAMST.177':'AsianAmerican 177','ASAMST.179':'AsianAmerican 179',
			'ASAMST.181':'AsianAmerican 181','ASAMST.183':'AsianAmerican 183','ASAMST.190':'AsianAmerican 190','ASAMST.190AC':'AsianAmerican 190AC',
			'ASIANST.10':'AsianStudies 10','ASIANST.150':'AsianStudies 150',
			'BUDDSTD.50':'Buddhist 50','BUDDSTD.C50':'Buddhist C50','BUDDSTD.114':'Buddhist 114','BUDDSTD.C114':'Buddhist C114','BUDDSTD.C115':'Buddhist C115','BUDDSTD.C120':'Buddhist C120','BUDDSTD.C126':'Buddhist C126',
			'BUDDSTD.C128':'Buddhist C128','BUDDSTD.C130':'Buddhist C130','BUDDSTD.C135':'Buddhist C135','BUDDSTD.C140':'Buddhist C140','BUDDSTD.154':'Buddhist 154','BUDDSTD.C154':'Buddhist C154','BUDDSTD.C174':'Buddhist C174','BUDDSTD.190':'Buddhist 190',
			'UGBA.C5':'Bussiness C5','UGBA.10':'Bussiness 10','UGBA.39AC':'Bussiness 39AC','UGBA.100':'Bussiness 100','UGBA.101A':'Bussiness 101A','UGBA.101B':'Bussiness 101B','UGBA.105':'Bussiness 105','UGBA.107':'Bussiness 107',
			'UGBA.118':'Bussiness 118','UGBA.156AC':'Bussiness 156AC','UGBA.170':'Bussiness 170','UGBA.C172':'Bussiness C172','UGBA.175':'Bussiness 175','UGBA.178':'Bussiness 178','UGBA.184':'Bussiness 184',
			'CATALAN.101':'Catalan 101',
			'CELTIC.15':'Celtic 15','CELTIC.16':'Celtic 16','CELTIC.70':'Celtic 70','CELTIC.85':'Celtic 85','CELTIC.86':'Celtic 86','CELTIC.102A':'Celtic 102A','CELTIC.102B':'Celtic 102B','CELTIC.105A':'Celtic 105A','CELTIC.119A':'Celtic 119A',
			'CELTIC.119B':'Celtic 119B','CELTIC.125':'Celtic 125','CELTIC.128':'Celtic 128','CELTIC.129':'Celtic 129','CELTIC.138':'Celtic 138','CELTIC.139':'Celtic 139','CELTIC.144A':'Celtic 144A','CELTIC.144B':'Celtic 144B','CELTIC.145A':'Celtic 145A',
			'CELTIC.145B':'Celtic 145B','CELTIC.146A':'Celtic 146A','CELTIC.146B':'Celtic 146B','CELTIC.161':'Celtic 161','CELTIC.C168':'Celtic C168','CELTIC.170':'Celtic 170','CELTIC.171':'Celtic 171','CELTIC.173':'Celtic 173',
			'CHICANO.20':'Chicano 20','CHICANO.40':'Chicano 40','CHICANO.50':'Chicano 50','CHICANO.70':'Chicano 70','CHICANO.110':'Chicano 110','CHICANO.130':'Chicano 130','CHICANO.133':'Chicano 133','CHICANO.135A':'Chicano 135A','CHICANO.135B':'Chicano 135B',
			'CHICANO.135C':'Chicano 135C','CHICANO.141':'Chicano 141','CHICANO.142':'Chicano 142','CHICANO.143':'Chicano 143','CHICANO.150B':'Chicano 150B','CHICANO.159':'Chicano 159','CHICANO.161':'Chicano 161','CHICANO.C161':'Chicano C161','CHICANO.162':'Chicano 162',
			'CHICANO.163':'Chicano 163','CHICANO.165':'Chicano 165','CHICANO.172':'Chicano 172','CHICANO.174':'Chicano 174','CHICANO.176':'Chicano 176','CHICANO.179':'Chicano 179','CHICANO.180':'Chicano 180',
			'CHINESE.1A':'Chinese 1A','CHINESE.1B':'Chinese 1B','CHINESE.7A':'Chinese 7A','CHINESE.7B':'Chinese 7B','CHINESE.10A':'Chinese 10A','CHINESE.10B':'Chinese 10B','CHINESE.100A':'Chinese 100A','CHINESE.100B':'Chinese 100B','CHINESE.101':'Chinese 101',
			'CHINESE.102':'Chinese 102','CHINESE.110A':'Chinese 110A','CHINESE.110B':'Chinese 110B','CHINESE.111':'Chinese 111','CHINESE.112':'Chinese 112','CHINESE.120':'Chinese 120','CHINESE.122':'Chinese 122','CHINESE.130':'Chinese 130','CHINESE.134':'Chinese 134',
			'CHINESE.136':'Chinese 136','CHINESE.C140':'Chinese C140','CHINESE.153':'Chinese 153','CHINESE.155':'Chinese 155','CHINESE.156':'Chinese 156','CHINESE.157':'Chinese 157','CHINESE.158':'Chinese 158','CHINESE.159':'Chinese 159','CHINESE.161':'Chinese 161',
			'CHINESE.165':'Chinese 165','CHINESE.180':'Chinese 180','CHINESE.181':'Chinese 181','CHINESE.183':'Chinese 183','CHINESE.186':'Chinese 186','CHINESE.187':'Chinese 187','CHINESE.188':'Chinese 188','CHINESE.189':'Chinese 189',
			'CYPLAN.110':'CityPlanning 110','CYPLAN.111':'CityPlanning 111','CYPLAN.113A':'CityPlanning 113A','CYPLAN.113B':'CityPlanning 113B','CYPLAN.114':'CityPlanning 114','CYPLAN.115':'CityPlanning 115',
			'CYPLAN.116':'CityPlanning 116','CYPLAN.118AC':'CityPlanning 118AC','CYPLAN.119':'CityPlanning 119','CYPLAN.120':'CityPlanning 120','CYPLAN.C139':'CityPlanning C139','CYPLAN.140':'CityPlanning 140',
			'CIVENG.C154':'CivEng C154','CIVENG.167':'CivEng 167',
			'CLASSIC.10A':'Classics 10A','CLASSIC.10B':'Classics 10B','CLASSIC.17A':'Classics 17A','CLASSIC.17B':'Classics 17B','CLASSIC.28':'Classics 28','CLASSIC.29':'Classics 29','CLASSIC.34':'Classics 34','CLASSIC.35':'Classics 35',
			'CLASSIC.36':'Classics 36','CLASSIC.100A':'Classics 100A','CLASSIC.100B':'Classics 100B','CLASSIC.110':'Classics 110','CLASSIC.124':'Classics 124','CLASSIC.121':'Classics 121','CLASSIC.130':'Classics 130','CLASSIC.R44':'Classics R44',
			'CLASSIC.161':'Classics 161','CLASSIC.163':'Classics 163','CLASSIC.170A':'Classics 170A','CLASSIC.170B':'Classics 170B','CLASSIC.170C':'Classics 170C','CLASSIC.170D':'Classics 170D','CLASSIC.175A':'Classics 175A',
			'CLASSIC.175B':'Classics 175B','CLASSIC.175C':'Classics 175C','CLASSIC.175D':'Classics 175D','CLASSIC.175E':'Classics 175E','CLASSIC.175F':'Classics 175F','CLASSIC.175G':'Classics 175G','CLASSIC.180':'Classics 180',
			'COGSCI.1':'CogSci 1','COGSCI.C100':'CogSci C100','COGSCI.C101':'CogSci C101','COGSCI.C102':'CogSci C102','COGSCI.C103':'CogSci C103','COGSCI.C104':'CogSci C104','COGSCI.C110':'CogSci C110','COGSCI.C124':'CogSci C124','COGSCI.C142':'CogSci C142','COGSCI.C147':'CogSci C147',
			'COLWRIT.25AC':'CollegeWriting 25AC','COLWRIT.50AC':'CollegeWriting 50AC','COLWRIT.108':'CollegeWriting 108','COLWRIT.110':'CollegeWriting 110','COLWRIT.150AC':'CollegeWriting 150AC','COLWRIT.180':'CollegeWriting 180','COLWRIT.192AC':'CollegeWriting 192AC',
			'COMPSCI.10':'CompSci 10','COMPSCI.C79':'CompSci C79',
			'DEMOG.5':'Demography 5','DEMOG.110':'Demography 110','DEMOG.C126':'Demography C126','DEMOG.145AC':'Demography 145AC','DEMOG.160':'Demography 160','DEMOG.C164':'Demography C164','DEMOG.C165':'Demography C165','DEMOG.C175':'Demography C175',
			'DUTCH.1':'Dutch 1','DUTCH.2':'Dutch 2','DUTCH.10':'Dutch 10','DUTCH.39A':'Dutch 39A','DUTCH.100':'Dutch 100','DUTCH.107':'Dutch 107','DUTCH.110':'Dutch 110','DUTCH.125':'Dutch 125','DUTCH.140':'Dutch 140','DUTCH.C164':'Dutch C164',
			'DUTCH.166':'Dutch 166','DUTCH.170':'Dutch 170','DUTCH.C170':'Dutch C170','DUTCH.171AC':'Dutch 171AC','DUTCH.173':'Dutch 173','DUTCH.174':'Dutch 174','DUTCH.176':'Dutch 176','DUTCH.C178':'Dutch C178','DUTCH.179':'Dutch 179','DUTCH.C179':'Dutch C179',
			'EALANG.C50':'EastAsianLanguages C50','EALANG.101':'EastAsianLanguages 101','EALANG.103':'EastAsianLanguages 103','EALANG.104':'EastAsianLanguages 104','EALANG.105':'EastAsianLanguages 105','EALANG.106':'EastAsianLanguages 106','EALANG.107':'EastAsianLanguages 107','EALANG.109':'EastAsianLanguages 109',
			'EALANG.C120':'EastAsianLanguages C120','EALANG.C126':'EastAsianLanguages C126','EALANG.C128':'EastAsianLanguages C128','EALANG.C130':'EastAsianLanguages C130','EALANG.C135':'EastAsianLanguages C135','EALANG.180':'EastAsianLanguages 180','EALANG.181':'EastAsianLanguages 181',
			'EAEURST.1A':'EastEuropean 1A','EAEURST.1B':'EastEuropean 1B','EAEURST.2A':'EastEuropean 2A','EAEURST.2B':'EastEuropean 2B','EAEURST.100':'EastEuropean 100','EAEURST.102A':'EastEuropean 102A','EAEURST.102B':'EastEuropean 102B',
			'EDUC.30AC':'Educ 30AC','EDUC.40AC':'Educ 40AC','EDUC.52':'Educ 52','EDUC.75AC':'Educ 75AC','EDUC.112':'Educ 112','EDUC.114A':'Educ 114A','EDUC.130':'Educ 130',
			'EDUC.140AC':'Educ 140AC','EDUC.142':'Educ 142','EDUC.143':'Educ 143','EDUC.C145':'Educ C145','EDUC.180':'Educ 180','EDUC.C181':'Educ C181','EDUC.182AC':'Educ 182AC',
			'EDUC.183':'Educ 183','EDUC.184':'Educ 184','EDUC.185':'Educ 185','EDUC.186AC':'Educ 186AC','EDUC.189':'Educ 189','EDUC.190':'Educ 190','EDUC.190B':'Educ 190B',
			'ENERES.C100':'ERG C100','ENERES.102':'ERG 102','ENERES.170':'ERG 170','ENERES.175':'ERG 175','ENERES.C180':'ERG C180','ENERES.190':'ERG 190',
			'ENGIN.120':'E 120','ENGIN.125':'E 125',
			'ENVDES.1':'EnvironDesign 1','ENVDES.4A':'EnvironDesign 4A','ENVDES.4B':'EnvironDesign 4B','ENVDES.4C':'EnvironDesign 4C','ENVDES.10':'EnvironDesign 10','ENVDES.100':'EnvironDesign 100',
			'ENVDES.101A':'EnvironDesign 101A','ENVDES.101B':'EnvironDesign 101B','ENVDES.C169A':'EnvironDesign C169A','ENVDES.C169B':'EnvironDesign C169B','ENVDES.170':'EnvironDesign 170',
			'ENVDES.C1':'EnvironDesign C1','ENVDES.100':'EnvironDesign 100','ENVDES.C101':'EnvironDesign C101','ENVDES.C102':'EnvironDesign C102','ENVDES.C118':'EnvironDesign C118','ENVDES.140AC':'EnvironDesign 140AC','ENVDES.141':'EnvironDesign 141',
			'ENVDES.142':'EnvironDesign 142','ENVDES.143':'EnvironDesign 143','ENVDES.145':'EnvironDesign 145','ENVDES.147':'EnvironDesign 147','ENVDES.C151':'EnvironDesign C151','ENVDES.152':'EnvironDesign 152','ENVDES.153':'EnvironDesign 153',
			'ENVDES.154':'EnvironDesign 154','ENVDES.161':'EnvironDesign 161','ENVDES.162':'EnvironDesign 162','ENVDES.C175':'EnvironDesign C175','ENVDES.C180':'EnvironDesign C180','ENVDES.C181':'EnvironDesign C181','ENVDES.C183':'EnvironDesign C183',
			'ESPM.C10':'ESPM C10','ESPM.C11':'ESPM C11','ESPM.C12':'ESPM C12','ESPM.50AC':'ESPM 50AC','ESPM.60':'ESPM 60','ESPM.78A':'ESPM 78A','ESPM.100':'ESPM 100','ESPM.102C':'ESPM 102C','ESPM.102D':'ESPM 102D','ESPM.118':'ESPM 118','ESPM.151':'ESPM 151',
			'ESPM.155':'ESPM 155','ESPM.C159':'ESPM C159','ESPM.160AC':'ESPM 160AC','ESPM.161':'ESPM 161','ESPM.162':'ESPM 162','ESPM.163AC':'ESPM 163AC','ESPM.165':'ESPM 165','ESPM.166':'ESPM 166','ESPM.C167':'ESPM C167','ESPM.168':'ESPM 168',
			'ESPM.169':'ESPM 169','ESPM.182':'ESPM 182','ESPM.183':'ESPM 183','ESPM.C183':'ESPM C183','ESPM.184':'ESPM 184','ESPM.186':'ESPM 186','ESPM.188':'ESPM 188','ESPM.190':'ESPM 190','ESPM.C191':'ESPM C191','ESPM.C193B':'ESPM C193B',
			'ENVSCI.10':'EnvSci 10',
			'ETHSTD.10AC':'EthnicStudies 10AC','ETHSTD.10B':'EthnicStudies 10B','ETHSTD.11AC':'EthnicStudies 11AC','ETHSTD.20AC':'EthnicStudies 20AC','ETHSTD.21AC':'EthnicStudies 21AC','ETHSTD.41AC':'EthnicStudies 41AC','ETHSTD.C73AC':'EthnicStudies C73AC','ETHSTD.100':'EthnicStudies 100','ETHSTD.101A':'EthnicStudies 101A',
			'ETHSTD.101B':'EthnicStudies 101B','ETHSTD.103':'EthnicStudies 103','ETHSTD.122AC':'EthnicStudies 122AC','ETHSTD.126':'EthnicStudies 126','ETHSTD.130':'EthnicStudies 130','ETHSTD.135':'EthnicStudies 135','ETHSTD.136':'EthnicStudies 136','ETHSTD.141':'EthnicStudies 141','ETHSTD.144AC':'EthnicStudies 144AC',
			'ETHSTD.147':'EthnicStudies 147','ETHSTD.150':'EthnicStudies 150','ETHSTD.159AC':'EthnicStudies 159AC','ETHSTD.174':'EthnicStudies 174','ETHSTD.175':'EthnicStudies 175','ETHSTD.190':'EthnicStudies 190','ETHSTD.190AC':'EthnicStudies 190AC','ETHSTD.195':'EthnicStudies 195',
			'EURAST.1A':'EurAsianStudies 1A','EURAST.1B':'EurAsianStudies 1B','EURAST.101A':'EurAsianStudies 101A','EURAST.101B':'EurAsianStudies 101B','EURAST.102A':'EurAsianStudies 102A','EURAST.102B':'EurAsianStudies 102B',
			'FILM.25A':'Film 25A','FILM.25B':'Film 25B','FILM.26':'Film 26','FILM.50':'Film 50','FILM.100':'Film 100','FILM.108':'Film 108','FILM.128':'Film 128','FILM.129':'Film 129','FILM.140':'Film 140',
			'GEOG.4':'Geography 4','GEOG.10':'Geography 10','GEOG.20':'Geography 20','GEOG.30':'Geography 30','GEOG.31':'Geography 31','GEOG.C32':'Geography C32','GEOG.35':'Geography 35','GEOG.37':'Geography 37',
			'GEOG.51':'Geography 51','GEOG.C55':'Geography C55','GEOG.70AC':'Geography 70AC','GEOG.109':'Geography 109','GEOG.C110':'Geography C110','GEOG.C112':'Geography C112','GEOG.123':'Geography 123','GEOG.125':'Geography 125',
			'GEOG.130':'Geography 130','GEOG.137':'Geography 137','GEOG.138':'Geography 138','GEOG.C157':'Geography C157','GEOG.159AC':'Geography 159AC','GEOG.C160A':'Geography C160A','GEOG.C160B':'Geography B160B','GEOG.163':'Geography 163',
			'GEOG.164':'Geography 164','GEOG.165':'Geography 165','GEOG.172':'Geography 172','GEOG.173A':'Geography 173A','GEOG.181':'Geography 181',
			'GPP.105':'GPP 105','GPP.115':'GPP 155',
			'GREEK.1':'Greek 1','GREEK.2':'Greek 2','GREEK.10':'Greek 10','GREEK.40':'Greek 40','GREEK.100':'Greek 100','GREEK.101':'Greek 101','GREEK.102':'Greek 102','GREEK.105':'Greek 105',
			'GREEK.115':'Greek 115','GREEK.116':'Greek 116','GREEK.117':'Greek 117','GREEK.120':'Greek 120','GREEK.121':'Greek 121','GREEK.122':'Greek 122','GREEK.123':'Greek 123','GREEK.125':'Greek 125',
			'HMEDSCI.C133':'HealthMedical C133',
			'INDENG.170':'IndEng 170','INDENG.191':'IndEng 191',
			'INFO.W10':'Information W10','INFO.C103':'Information C103','INFO.146':'Information 146','INFO.C167':'Information C167','INFO.181':'Information 181',
			'INTEGBI.34AC':'IB 34AC',
			'JEWISH.39A':'Jewish 39A','JEWISH.101':'Jewish 101',
			'JOURN.100':'Journalism 100','JOURN.C101':'Journalism C101','JOURN.102AC':'Journalism 102AC','JOURN.C103':'Journalism C103','JOURN.141':'Journalism 141','JOURN.C141':'Journalism C141',
			'LDARCH.110':'LandscapeArchitecture 110','LDARCH.111':'LandscapeArchitecture 111','LDARCH.121':'LandscapeArchitecture 121','LDARCH.130':'LandscapeArchitecture 130','LDARCH.138':'LandscapeArchitecture 138','LDARCH.138AC':'LandscapeArchitecture 138AC','LDARCH.140':'LandscapeArchitecture 140','LDARCH.141AC':'LandscapeArchitecture 141AC','LDARCH.170':'LandscapeArchitecture 170','LDARCH.C171':'LandscapeArchitecture C171',
			'L&S.5':'L&S 5','L&S.C5':'L&S C5','L&S.20':'L&S 20','L&S.40':'L&S 40','L&S.C40T':'L&S C40T','L&S.60':'L&S 60','L&S.C60T':'L&S C60T','L&S.C60U':'L&S C60U','L&S.C101':'L&S C101','L&S.105':'L&S 105',
			'L&S.120':'L&S 120','L&S.121':'L&S 121','L&S.122':'L&S 122','L&S.140':'L&S 140','L&S.C140V':'L&S C140V','L&S.150':'L&S 150','L&S.C150T':'L&S C150T','L&S.160':'L&S 160','L&S.C160T':'L&S C160T',
			'L&S.C160V':'L&S C160V','L&S.170AC':'L&S 170AC','L&S.180':'L&S 180','L&S.180AC':'L&S 180AC','L&S.C180T':'L&S C180T','L&S.C180U':'L&S C180U','L&S.C180V':'L&S C180V',
			'LINGUIS.1A':'Linguistics 1A','LINGUIS.1B':'Linguistics 1B','LINGUIS.C1B':'Linguistics C1B','LINGUIS.C3B':'Linguistics C3B','LINGUIS.5':'Linguistics 5','LINGUIS.11':'Linguistics 11','LINGUIS.16':'Linguistics 16','LINGUIS.22':'Linguistics 22',
			'LINGUIS.23':'Linguistics 23','LINGUIS.C30B':'Linguistics C30B','LINGUIS.40':'Linguistics 40','LINGUIS.51':'Linguistics 51','LINGUIS.55AC':'Linguistics 55AC','LINGUIS.100':'Linguistics 100','LINGUIS.C104':'Linguistics C104','LINGUIS.105':'Linguistics 105',
			'LINGUIS.106':'Linguistics 106','LINGUIS.110':'Linguistics 110','LINGUIS.113':'Linguistics 113','LINGUIS.115':'Linguistics 115','LINGUIS.120':'Linguistics 120','LINGUIS.121':'Linguistics 121','LINGUIS.122':'Linguistics 122','LINGUIS.123':'Linguistics 123',
			'LINGUIS.124':'Linguistics 124','LINGUIS.127':'Linguistics 127','LINGUIS.128':'Linguistics 128','LINGUIS.130':'Linguistics 130','LINGUIS.131':'Linguistics 131','LINGUIS.C139':'Linguistics C139','LINGUIS.C142':'Linguistics C142','LINGUIS.146':'Linguistics 146',
			'LINGUIS.C147':'Linguistics C147','LINGUIS.150':'Linguistics 150','LINGUIS.151':'Linguistics 151','LINGUIS.152':'Linguistics 152','LINGUIS.155AC':'Linguistics 155AC','LINGUIS.170':'Linguistics 170','LINGUIS.175':'Linguistics 175','LINGUIS.181':'Linguistics 181',
			'MATH.160':'Math 160',
			'MEDST.150':'Medieval 150',
			'MESTU.20':'MiddleEastern 20','MESTU.102':'MiddleEastern 102','MESTU.109':'MiddleEastern 109','MESTU.150':'MiddleEastern 150',
			'MILAFF.20':'MilitaryAffairs 20','MILAFF.145A':'MilitaryAffairs 145A','MILAFF.145B':'MilitaryAffairs 145B','MILAFF.154':'MilitaryAffairs 154',
			'MUSIC.26AC':'Music 26AC','MUSIC.27':'Music 27','MUSIC.73':'Music 73','MUSIC.75':'Music 75','MUSIC.76':'Music 76','MUSIC.77':'Music 77','MUSIC.128':'Music 128','MUSIC.130B':'Music 130B','MUSIC.132':'Music 132','MUSIC.133C':'Music 133C',
			'MUSIC.134A':'Music 134A','MUSIC.134B':'Music 134B','MUSIC.135A':'Music 135A','MUSIC.136':'Music 136','MUSIC.137AC':'Music 137AC','MUSIC.139':'Music 139','MUSIC.171D':'Music 171D','MUSIC.172A':'Music 172A','MUSIC.174C':'Music 174C',
			'MUSIC.128A':'Music 128A','MUSIC.128B':'Music 128B','MUSIC.128C':'Music 128C','MUSIC.128D':'Music 128D','MUSIC.128E':'Music 128E','MUSIC.128F':'Music 128F','MUSIC.128G':'Music 128G','MUSIC.128H':'Music 128H','MUSIC.128I':'Music 128I','MUSIC.128J':'Music 128J',
			'MUSIC.128K':'Music 128K','MUSIC.128L':'Music 128L','MUSIC.128M':'Music 128M','MUSIC.128N':'Music 128N','MUSIC.128O':'Music 128O','MUSIC.128P':'Music 128P','MUSIC.128Q':'Music 128Q','MUSIC.128R':'Music 128R','MUSIC.128S':'Music 128S','MUSIC.128T':'Music 128T',
			'NAVSSCI.2':'NavalScience 2','NAVSSCI.3':'NavalScience 3',
			'NWMEDIA.150AC':'NWMEDIA 150AC',
			'NUSCTX.104':'NutriSci 104','NUSCTX.135':'NutriSci 135','NUSCTX.C159':'NutriSci C159','NUSCTX.166':'NutriSci 166',
			'ART.23AC':'Art 23AC','ART.119':'Art 119','ART.162':'Art 162','ART.164':'Art 164','ART.C179':'Art C179',
			'PSYCH.1':'Psychology 1','PSYCH.2':'Psychology 2','PSYCH.14':'Psychology 14','PSYCH.39AC':'Psychology 39AC','PSYCH.C105':'Psychology C105','PSYCH.106':'Psychology 106','PSYCH.107':'Psychology 107','PSYCH.109':'Psychology 109',
			'PSYCH.C120':'Psychology C120','PSYCH.121':'Psychology 121','PSYCH.122':'Psychology 122','PSYCH.C124':'Psychology C124','PSYCH.C129':'Psychology C129','PSYCH.130':'Psychology 130','PSYCH.131':'Psychology 131','PSYCH.133':'Psychology 133',
			'PSYCH.140':'Psychology 140','PSYCH.141':'Psychology 141','PSYCH.146':'Psychology 146','PSYCH.148':'Psychology 148','PSYCH.150':'Psychology 150','PSYCH.156':'Psychology 156','PSYCH.160':'Psychology 160','PSYCH.162':'Psychology 162',
			'PSYCH.C162':'Psychology C162','PSYCH.164':'Psychology 164','PSYCH.165':'Psychology 165','PSYCH.166':'Psychology 166','PSYCH.167':'Psychology 167','PSYCH.168':'Psychology 168','PSYCH.180':'Psychology 180',
			'PBHLTH.14':'PublicHealth 14','PBHLTH.103':'PublicHealth 103','PBHLTH.105':'PublicHealth 105','PBHLTH.107':'PublicHealth 107','PBHLTH.112':'PublicHealth 112','PBHLTH.113':'PublicHealth 113','PBHLTH.114':'PublicHealth 114','PBHLTH.116':'PublicHealth 116','PBHLTH.126':'PublicHealth 126',
			'PBHLTH.130AC':'PublicHealth 130AC','PBHLTH.131AC':'PublicHealth 131AC','PBHLTH.150D':'PublicHealth 150D','PBHLTH.150E':'PublicHealth 150E','PBHLTH.C155':'PublicHealth C155','PBHLTH.C160':'PublicHealth C160','PBHLTH.180':'PublicHealth 180','PBHLTH.181':'PublicHealth 181','PBHLTH.183':'PublicHealth 183',
			'STAT.C79':'Stats C79',
			'THEATER.25AC':'TDPS 25AC','THEATER.52AC':'TDPS 52AC','THEATER.26':'TDPS 26','THEATER.C107':'TDPS C107','THEATER.C108':'TDPS C108','THEATER.119':'TDPS 119','THEATER.121':'TDPS 121','THEATER.122':'TDPS 122','THEATER.125':'TDPS 125',
			'THEATER.126':'TDPS 126','THEATER.C131B':'TDPS C131B','THEATER.145':'TDPS 145','THEATER.151A':'TDPS 151A','THEATER.151B':'TDPS 151B','THEATER.153B':'TDPS 153B','THEATER.C183A':'TDPS C183A','THEATER.C183B':'TDPS C183B','THEATER.187':'TDPS 187',
			'UGIS.110':'UGIS 110','UGIS.112':'UGIS 112','UGIS.120':'UGIS 120','UGIS.C133':'UGIS C133','UGIS.C136':'UGIS C136','UGIS.C155':'UGIS C155','UGIS.160':'UGIS 160','UGIS.161':'UGIS 161','UGIS.165':'UGIS 165',
			'UGIS.166':'UGIS 166','UGIS.167':'UGIS 167','UGIS.171':'UGIS 171','UGIS.172':'UGIS 172','UGIS.173':'UGIS 173','UGIS.174':'UGIS 174','UGIS.175':'UGIS 175','UGIS.176':'UGIS 176','UGIS.177':'UGIS 177',
			'UGIS.168':'UGIS 168','UGIS.169':'UGIS 169','UGIS.170':'UGIS 170','UGIS.187':'UGIS 187','UGIS.162A':'UGIS 162A','UGIS.162B':'UGIS 162B','UGIS.162C':'UGIS 162C','UGIS.162D':'UGIS 162D','UGIS.162E':'UGIS 162E','UGIS.162F':'UGIS 162F',
			'UGIS.162G':'UGIS 162G','UGIS.162H':'UGIS 162H','UGIS.162I':'UGIS 162I','UGIS.162J':'UGIS 162J','UGIS.162K':'UGIS 162K','UGIS.162L':'UGIS 162L','UGIS.162M':'UGIS 162M','UGIS.162N':'UGIS 162N','UGIS.162O':'UGIS 162O','UGIS.162P':'UGIS 162P'}
		temp=manyChoiceReq(takenClasses, '', electives, '')
		hss+=(len (temp['courseDone']))
		classesCompleted+=(temp['courseDone'])
		classesNotCompleted+=(temp['courseLeft'])
		#departments where all classes are acceptable
		depts=['BENGLA','CUNEIF','DEVSTD','EGYPT','FILIPN','HEBREW','HINURD','ISF','IAS','IRANIAN','JAPAN','KHMER','KOREAN','LATAMST','LATIN','LGBT','MALAY/I','PACS','PERSIAN','PORTUG',
			'PUBPOL','PUNJABI','RELIGST','SEASIAN','SANSKR','SEMITIC','SOCWEL','TAMIL','TAGALG','TELUGU','THAI','TIBETAN','TURKISH','VIETNMS','YIDDISH']
		for item in takenClasses:
			for i in depts:
				if (i in item):
					hss+=1
					classesCompleted.append(item.replace('.',' '))
		for item in depts:
			classesNotCompleted.append('All '+item+' classes')
		#departments where most classes are taken
		exceptSPANISH=['SPANISH.R1A','SPANISH.R1B']
		for item in takenClasses:
			if ('SPANISH' in item) and (not (item in exceptSPANISH)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptRHETOR=['RHETOR.R1A','RHETOR.R1B','RHETOR.10','RHETOR.30']
		for item in takenClasses:
			if ('RHETOR' in item) and (not (item in exceptRHETOR)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptSCANDIN=['SCANDIN.R5A','SCANDIN.R5B']
		for item in takenClasses:
			if ('SCANDIN' in item) and (not (item in exceptSCANDIN)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptSLAVIC=['SLAVIC.R5A','SLAVIC.R5B']
		for item in takenClasses:
			if ('SLAVIC' in item) and (not (item in exceptSLAVIC)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptSOCIOL=['SOCIOL.106','SOCIOL.107B','SOCIOL.C196W']
		for item in takenClasses:
			if ('SOCIOL' in item) and (not (item in exceptSOCIOL)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptSSEAST=['SSEAST.R5A','SSEAST.R5B']
		for item in takenClasses:
			if ('SSEAST' in item) and (not (item in exceptSSEAST)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptSASIAN=['SASIAN.R5A','SASIAN.R5B']
		for item in takenClasses:
			if ('SASIAN' in item) and (not (item in exceptSASIAN)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptPHILOS=['PHILOS.R1B','PHILOS.12A','PHILOS.12B']
		for item in takenClasses:
			if ('PHILOS' in item) and (not (item in exceptPHILOS)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptPOLECON=['POLECON.C196W']
		for item in takenClasses:
			if ('POLECON' in item) and (not (item in exceptPOLECON)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptPOLSCI=['POLSCI.3','POLSCI.133','POLSCI.C196W']
		for item in takenClasses:
			if ('POLSCI' in item) and (not (item in exceptPOLSCI)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptNESTUD=['NESTUD.R1A','NESTUD.R1B']
		for item in takenClasses:
			if ('NESTUD' in item) and (not (item in exceptNESTUD)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptNATAMST=['NATAMST.R1A','NATAMST.R1B']
		for item in takenClasses:
			if ('NATAMST' in item) and (not (item in exceptNATAMST)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptMEDIAST=['MEDIAST.C196W']
		for item in takenClasses:
			if ('MEDIAST' in item) and (not (item in exceptMEDIAST)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptLEGALST=['LEGALST.R1A','LEGALST.R1B']
		for item in takenClasses:
			if ('LEGALST' in item) and (not (item in exceptLEGALST)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptITALIAN=['ITALIAN.R5A','ITALIAN.R5B']
		for item in takenClasses:
			if ('ITALIAN' in item) and (not (item in exceptITALIAN)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptHISTORY=['HISTORY.R1A','HISTORY.R1B','HISTORY.C196W']
		for item in takenClasses:
			if ('HISTORY' in item) and (not (item in exceptHISTORY)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptHISTART=['HISTART.R1B','HISTART.C196W']
		for item in takenClasses:
			if ('HISTART' in item) and (not (item in exceptHISTART)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptGERMAN=['GERMAN.5A','GERMAN.5B']
		for item in takenClasses:
			if ('GERMAN' in item) and (not (item in exceptGERMAN)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptGWS=['GWS.R1B','GWS.C196W','GWS.197']
		for item in takenClasses:
			if ('GWS' in item) and (not (item in exceptGWS)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptFRENCH=['FRENCH.R1A','FRENCH.R1B']
		for item in takenClasses:
			if ('FRENCH' in item) and (not (item in exceptFRENCH)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptENGLISH=['ENGLISH.R1A','ENGLISH.R1B','ENGLISH.R50']
		for item in takenClasses:
			if ('ENGLISH' in item) and (not (item in exceptENGLISH)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptECON=['ECON.C103']
		for item in takenClasses:
			if ('ECON' in item) and (not (item in exceptECON)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptCOMLIT=['COMLIT.H1A','COMLIT.H1B','COMLIT.R1A','COMLIT.R1B','COMLIT.R2A','COMLIT.R2B','COMLIT.R3A','COMLIT.R3B']
		for item in takenClasses:
			if ('COMLIT' in item) and (not (item in exceptCOMLIT)):
				hss+=1
				classesCompleted.append(item.replace('.',' '))
		exceptions=['All Rhetoric Classes except R1A,R1B,R10,R30','All Scandinavian Classes except R5A, R5B','All Slavic Classes except R5A, R5B','All Sociology Classes except 106,107B,C196W',
			'All South and SouthEast Asian Classes except except R5A, R5B','All South Asian Classes except except R5A, R5B','All Philosophy Classes except R1B,12A,12B', 'All Polital Econ Classes except C196W',
			'All Politcal Science Classes except 3,133,C196W','All Near Eastern Studies Classes except R1A,R1B','All Native American Studies Classes except R1A,R1B', 'All Media Studies Classes except C196W',
			'All Legal Studies Classes except R1A,R1B', 'All Italian Classes except R5A,R5B','All History Classes except R1A,R1B,C196W','All History of Art Classes except R1B,C196W',
			'All German Classes except 5A,5B','All GWS Classes except R1B,C196W,197','All French Classes except R1A,R1B','All English Classes except R1A,R1B,R50','All Econ Classes except C103',
			'All Comparative Literature Classes except H1A,H1B,R1A,R1B,R2A,R2B,R3A,R3B']
		classesNotCompleted+=exceptions
		if('AEROSPC.2A' in takenClasses) and ('AEROSPC.2B' in takenClasses):
			hss+=2
			classesCompleted.append('AeroSpace 2A')
			classesCompleted.append('AeroSpace 2B')
		else:
			classesNotCompleted.append('AeroSpace 2A')
			classesNotCompleted.append('AeroSpace 2B')
		if(hss>=2):
			ans.append({'reqName':'HSS Breadth', 'reqCompleted':True, 'reqDescription':'The Humanities and Social Sciencces Breadth requirement of at least two courses','courseDone':classesCompleted, 'courseLeft':classesNotCompleted})
		else:
			ans.append({'reqName':'HSS Breadth', 'reqCompleted':False, 'reqDescription':'The Humanities and Social Sciencces Breadth requirement of at least two courses','courseDone':classesCompleted, 'courseLeft':classesNotCompleted})				
		#Freshman Seminar.  Chemistry 96
		ans.append(basicReq(takenClasses, 'CHEM.96', 'Chem 96', 'Required Freshman Seminar'))
		#Chemistry.  4A, 4B, 112A, 112B
		ans.append(twoReq(takenClasses, 'General Chemistry', 'CHEM.4A', 'Chem 4A', 'CHEM.4B', 'Chem 4A', 'Basic Chemistry Requirements'))
		ans.append(twoReq(takenClasses, 'Organic Chemistry', 'CHEM.112A', 'Chem 112A', 'CHEM.112B', 'Chem 112B', 'Basic Chemistry Requirements'))
		#Mathematics.  1A, 1B, 53, 54
		ans.append(twoReq(takenClasses, 'Basic Calculus', 'MATH.1A', 'Math 1A', 'MATH.1B', 'Math 1B', 'Basic Math Requirements'))
		ans.append(twoReq(takenClasses, 'Basic Math', 'MATH.53', 'Math 53', 'MATH.54', 'Math 54', 'Basic Math Requirements'))
		#Physics.  7A, 7B (Physics 8A, 8B is allowed)
		temp1=twoReq(takenClasses, '', 'PHYSICS.7A', 'Physics 7A', 'PHYSICS.7B', 'Physics 7A', '')
		temp2=twoReq(takenClasses, '', 'PHYSICS.8A', 'Physics 8A', 'PHYSICS.8B', 'Physics 8A', '')
		if (temp1['reqCompleted'] or temp2['reqCompleted']):
			ans.append({'reqName':'Basic Physics', 'reqCompleted':True, 'reqDescription':'Basic Physics of either 7A and 7B or 8A and 8B','courseDone':temp1['courseDone']+temp2['courseDone'], 'courseLeft':temp1['courseLeft']+temp2['courseLeft']})
		else:
			ans.append({'reqName':'Basic Physics', 'reqCompleted':False, 'reqDescription':'Basic Physics of either 7A and 7B or 8A and 8B','courseDone':temp1['courseDone']+temp2['courseDone'], 'courseLeft':temp1['courseLeft']+temp2['courseLeft']})
		#Reading and Composition
		OneA=False
		OneB=False
		for item in takenClasses:
			if 'R1A' in item:
				OneA=True
			if 'R1B' in item:
				OneB=True
		if (OneA and OneB):
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':True, 'reqDescription':"Take at least one course labeled R1A and R1B",'courseDone':[], 'courseLeft':[]})
		elif (OneA):
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled R1A and R1B. You have completed R1A",'courseDone':[], 'courseLeft':[]})
		elif (OneB):
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled R1A and R1B. You have completed R1B",'courseDone':[], 'courseLeft':[]})
		else:
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled R1A and R1B",'courseDone':[], 'courseLeft':[]})
		#just here because it is used by several different majors
		allied={'ASTRON.C162':'Astro C162', 'BIOENG.100':'BioEng 100','BIOENG.104':'BioEng 104','BIOENG.C105B':'BioEng C105B','BIOENG.111':'BioEng 111',
			'BIOENG.112':'BioEng 112','BIOENG.C112':'BioEng C112','BIOENG.115':'BioEng 115','BIOENG.116':'BioEng 116','BIOENG.C117':'BioEng C117',
			'BIOENG.C118':'BioEng C118','BIOENG.C119':'BioEng C119','BIOENG.121':'BioEng 121','BIOENG.131':'BioEng 131','BIOENG.132':'BioEng 132',
			'BIOENG.C141':'BioEng C141','BIOENG.143':'BioEng 143','BIOENG.C144':'BioEng C144','BIOENG.C144L':'BioEng C144L','BIOENG.147':'BioEng 147',
			'BIOENG.150':'BioEng 150','BIOENG.151':'BioEng 151','BIOENG.163':'BioEng 163','BIOENG.174':'BioEng 174','BIOENG.C181':'BioEng C181',
			'CHMENG.140':'ChemEng 140','CHMENG.141':'ChemEng 141','CHMENG.142':'ChemEng 142','CHMENG.150A':'ChemEng 150A','CHMENG.150B':'ChemEng 150B','CHMENG.154':'ChemEng 154',
			'CHMENG.160':'ChemEng 160','CHMENG.162':'ChemEng 162','CHMENG.170A':'ChemEng 170A','CHMENG.170B':'ChemEng 170B','CHMENG.C170L':'ChemEng C170L','CHMENG.171':'ChemEng 171',
			'CHMENG.176':'ChemEng 176','CHMENG.C178':'ChemEng C178','CHMENG.179':'ChemEng 179','CHMENG.180':'ChemEng 180','CHMENG.185':'ChemEng 185','CHMENG.H194':'ChemEng H194',
			'CHMENG.195':'ChemEng 195','CHMENG.C195A':'ChemEng C195A','CHMENG.196':'ChemEng 196','CHEM.100':'Chem 100','CHEM.103':'Chem 103','CHEM.105':'Chem 105','CHEM.108':'Chem 108',
			'CHEM.C110L':'Chem C110L','CHEM.113':'Chem 113','CHEM.114':'Chem 114','CHEM.115':'Chem 115','CHEM.122':'Chem 122','CHEM.C130':'Chem C130','CHEM.130B':'Chem 130B','CHEM.135':'Chem 135',
			'CHEM.C138':'Chem C138','CHEM.143':'Chem 143','CHEM.146':'Chem 146','CHEM.C150':'Chem C150','CHEM.C170L':'Chem C170L','CHEM.C178':'Chem C178','CHEM.C182':'Chem C182','CHEM.C191':'Chem C191',
			'CHEM.192':'Chem 192','CHEM.H194':'Chem H194','CHEM.195':'Chem 195','CHEM.196':'Chem 196','CIVENG.C106':'CivEng C106','CIVENG.108':'CivEng 108','CIVENG.111':'CivEng 111','CIVENG.112':'CivEng 112',
			'CIVENG.114':'CivEng 114','CIVENG.115':'CivEng 115','CIVENG.C116':'CivEng C116','CIVENG.C133':'CivEng C133','COMPSCI.160':'CS 160','COMPSCI.162':'CS 162','COMPSCI.164':'CS 164','COMPSCI.170':'CS 170',
			'COMPSCI.174':'CS 174','COMPSCI.184':'CS 184','COMPSCI.C191':'CS C191','EPS.103':'EPS 103','EPS.105':'EPS 105','EPS.111':'EPS 111','EPS.C129':'EPS C129','EPS.131':'EPS 131','EPS.C162':'EPS C162',
			'EPS.C180':'EPS C180','EPS.C183':'EPS C183','EPS.C182':'EPS C182','EPS.185':'EPS 185', 'ECON.C103':'Econ C103', 'EDUC.223B':'Educ 223B','EDUC.224A':'Educ 224A','ELENG.100':'EE 100',
			'ENERES.102':'ERG 102','ENGIN.117':'E 117','ENGIN.128':'E 128','ENVSCI.119':'EnvSci 119','ENVSCI.120':'EnvSci 120','ENVSCI.C128':'EnvSci C128','ENVSCI.C129':'EnvSci C129','ENVSCI.C138':'EnvSci C138',
			'ENVSCI.C148':'EnvSci C148','ENVSCI.C180':'EnvSci C180','INTEGBI.106A':'IB 106A','INTEGBI.115':'IB 115','MATSCI.102':'MSE 102','MATSCI.103':'MSE 103','MATSCI.104':'MSE 104','MATSCI.111':'MSE 111','MATSCI.112':'MSE 112','MATSCI.113':'MSE 113',
			'MATSCI.117':'MSE 117','MATSCI.C118':'MSE C118','MATSCI.120':'MSE 120','MATSCI.121':'MSE 121','MATSCI.122':'MSE 122','MATSCI.123':'MSE 123','MATSCI.125':'MSE 125','MATSCI.130':'MSE 130','MATSCI.140':'MSE 140','MATSCI.151':'MSE 151',
			'MATH.C103':'Math C103','MATH.104':'Math 104','MATH.H104':'Math H104','MATH.105':'Math 105','MATH.110':'Math 110','MATH.H110':'Math H110','MATH.113':'Math 113','MATH.H113':'Math H113','MATH.114':'Math 114','MATH.115':'Math 115','MATH.121A':'Math 121A','MATH.121B':'Math 121B','MATH.123':'Math 123','MATH.125A':'Math 125A',
			'MATH.126':'Math 126','MATH.128A':'Math 128A','MATH.128B':'Math 128B','MATH.130':'Math 130','MATH.135':'Math 135','MATH.136':'Math 136','MATH.140':'Math 140','MATH.142':'Math 142','MATH.170':'Math 170','MATH.185':'Math 185','MATH.H185':'Math H185','MATH.187':'Math 187','MATH.189':'Math 189',
			'MECENG.C105B':'ME C105B','MECENG.107':'ME 107','MECENG.C115':'ME C115','MECENG.C117':'ME C117','MECENG.118':'ME 118','MECENG.C124':'ME C124','MECENG.C176':'ME C176','MECENG.C180':'ME C180',
			'MCELLBI.C100A':'MCB C100A','MCELLBI.102':'MCB 102','MCELLBI.C103':'MCB C103','MCELLBI.104':'MCB 104','MCELLBI.110':'MCB 110','MCELLBI.C110L':'MCB C110L','MCELLBI.111':'MCB 111','MCELLBI.C112':'MCB C112','MCELLBI.C112L':'MCB C112L','MCELLBI.113':'MCB 113','MCELLBI.C114':'MCB C114',
			'MCELLBI.115':'MCB 115','MCELLBI.C116':'MCB C116','MCELLBI.118':'MCB 118','MCELLBI.130A':'MCB 130A','MCELLBI.130L':'MCB 130L','MCELLBI.133L':'MCB 133L','MCELLBI.140':'MCB 140','MCELLBI.140L':'MCB 140L','MCELLBI.141':'MCB 141','MCELLBI.143':'MCB 143','MCELLBI.C148':'MCB C148',
			'MCELLBI.150':'MCB 150','MCELLBI.150L':'MCB 150L','MCELLBI.C160':'MCB C160','MCELLBI.160L':'MCB 160L','MCELLBI.167':'MCB 167','NUCENG.101':'NucEng 101','NUCENG.104':'NucEng 104','NUCENG.107':'NucEng 107','NUCENG.120':'NucEng 120',
			'NUCENG.124':'NucEng 124','NUCENG.130':'NucEng 130','NUCENG.150':'NucEng 150','NUCENG.161':'NucEng 161','NUCENG.162':'NucEng 162','NUCENG.170A':'NucEng 170A','NUCENG.170B':'NucEng 170B','NUCENG.180':'NucEng 180',
			'NUSCTX.103':'NutriSci 103','NUSCTX.108A':'NutriSci 108A','NUSCTX.110':'NutriSci 110','NUSCTX.C112':'NutriSci C112','NUSCTX.115':'NutriSci 115','NUSCTX.C119':'NutriSci C119','NUSCTX.120':'NutriSci 120','NUSCTX.150':'NutriSci 150','NUSCTX.160':'NutriSci 160','NUSCTX.171':'NutriSci 171',
			'PHYSICS.7C':'Physics 7C','PHYSICS.105':'Physics 105','PHYSICS.110A':'Physics 110A','PHYSICS.110B':'Physics 110B','PHYSICS.112':'Physics 112','PHYSICS.130':'Physics 130','PHYSICS.137B':'Physics 137B','PHYSICS.138':'Physics 138','PHYSICS.141A':'Physics 141A','PHYSICS.141B':'Physics 141B','PHYSICS.C191':'Physics C191',
			'PLANTBI.C103':'PlantBio C103','PLANTBI.C112':'PlantBio C112','PLANTBI.C112L':'PlantBio C112L','PLANTBI.C114':'PlantBio C114','PLANTBI.C116':'PlantBio C116','PLANTBI.120':'PlantBio 120','PLANTBI.120L':'PlantBio 120L','PLANTBI.122':'PlantBio 122','PLANTBI.C124':'PlantBio C124','PLANTBI.135':'PlantBio 135',
			'PLANTBI.135L':'PlantBio 135L','PLANTBI.C144':'PlantBio C144','PLANTBI.C144L':'PlantBio C144L','PLANTBI.C148':'PlantBio C148','PLANTBI.150':'PlantBio 150','PLANTBI.150L':'PlantBio 150L','PLANTBI.160':'PlantBio 160','PLANTBI.160L':'PlantBio 160L','PLANTBI.170':'PlantBio 170','PLANTBI.180':'PlantBio 180',
			'PBHLTH.C102':'PublicHealth C102','PBHLTH.142':'PublicHealth 142','PBHLTH.C143':'PublicHealth C143','PBHLTH.162A':'PublicHealth 162A','PBHLTH.162L':'PublicHealth 162L','PBHLTH.C170B':'PublicHealth C170B','PBHLTH.172':'PublicHealth 172','PBHLTH.C172':'PublicHealth C172',
			'STAT.134':'Stat 134','STAT.135':'Stat 135','STAT.C141':'Stat C141','STAT.C143':'Stat C143'}
		# Bachelor of Science Degree in Chemistry
		if(major=='BSCHEM'):
			#Chemistry. 104A, 104B, 120A, 120B, 125 and one of the following choices: 105, 108, 115, or 146. (Chemistry C182 may be substituted for 125.)
			ans.append(twoReq(takenClasses, 'InOrganic Chemistry', 'CHEM.104A', 'Chem 104A', 'CHEM.104B', 'Chem 104B', 'Requirement of both Chem 104A and 104B'))
			ans.append(twoReq(takenClasses, 'Physical Chemistry', 'CHEM.120A', 'Chem 120A', 'CHEM.120B', 'Chem 120B', 'Requirement of both Chem 120A and 120B'))
			ans.append(twoChoiceReq(takenClasses, 'Physical Chemistry', 'CHEM.125', 'Chem 125', 'CHEM.C182', 'Chem C182', 'Its suggested that you complete Chemistry 125 but C182 is acceptable'))
			#total at least 15 units including chem and allied:
			elecUnits=0
			chemReqs=['CHEM.4A','CHEM.4B','CHEM.112A','CHEM.112B','CHEM.104A','CHEM.104B','CHEM.120A','CHEM.120B','CHEM.125','CHEM.C182']
			elecTaken=[]
			elecNotTaken=[]
			for item in takenClasses:
				if (('CHEM' in item) and (not(item in chemReqs))):
					elecUnits+=units(item)
					elecTaken.append(item.replace('.',' '))
			elecNotTaken.append('Any additional Chem Class (not 4A/B,112A/B,104A/B,120A/B,125,C182)')
			#One additional lecture course (or laboratory/lecture course) in chemistry
			if elecUnits>=0:
				ans.append({'reqName':'Chem Elective', 'reqCompleted':True, 'reqDescription':'You must take at least one Chemistry Lecture Course in addition to requirements','courseDone':elecTaken, 'courseLeft':elecNotTaken})
			else:
				ans.append({'reqName':'Chem Elective', 'reqCompleted':False, 'reqDescription':'You must take at least one Chemistry Lecture Course in addition to requirements','courseDone':elecTaken, 'courseLeft':elecNotTaken})
			for key in allied:
				if (key in takenClasses):
					elecUnits+=units(item)
					elecTaken.append(allied[key])
				else:
					elecNotTaken.append(allied[key])
			if(elecUnits>=15):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':'You must take at least 15 units of electives either in Chemistry or included in the Allied Classes List','courseDone':elecTaken, 'courseLeft':['Any additional Chem Class (not 4A/B,112A/B,104A/B,120A/B,125,C182)']})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':'You must take at least 15 units of electives either in Chemistry or included in the Allied Classes List','courseDone':[], 'courseLeft':['Any additional Chem Class (not 4A/B,112A/B,104A/B,120A/B,125,C182)']})
			return ans
		# Chemical Engineering and Materials Science and Engineering
		elif(major=='CHEMMATSCI'):
			#Eng 7, Introduction to Computer Programming for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7', "The Introduction to Computer Programming requirement"))
			#Physics 7C, Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The Physics for Scientists and Engineers requirement"))
			#Chem Eng 140, Introduction to Chemical Process Analysis
			ans.append(basicReq(takenClasses, 'CHMENG.140', 'ChemEng 140', "The Introduction to Chemical Process Analysis requirement"))
			#Chem Eng 141, Chemical Engineering Thermodynamics
			ans.append(basicReq(takenClasses, 'CHMENG.141', 'ChemEng 141', "The Chemical Engineering Thermodynamics requirement"))
			#Chem Eng 150A, Transport Processes
			ans.append(basicReq(takenClasses, 'CHMENG.150A', 'ChemEng 150A', "The Transport Processes requirement"))
			#EE 100, Electronic Techniques for Engineering
			ans.append(basicReq(takenClasses, 'ELENG.100', 'EE 100', "The Electronic Techniques for Engineering requirement"))
			#Eng 45, Properties of Materials
			ans.append(basicReq(takenClasses, 'ENGIN.45', 'E 45', "The Properties of Materials requirement"))
			#Mat Sci 102, Bonding, Crystallography,and Crystal Defects
			ans.append(basicReq(takenClasses, 'MATSCI.102', 'MatSci 102', "The Bonding, Crystallography,and Crystal Defects requirement"))
			#Mat Sci 103, Phase Transformations and Kinetics
			ans.append(basicReq(takenClasses, 'MATSCI.103', 'MatSci 103', "The Phase Transformations and Kinetics requirement"))
			#Mat Sci Electives must include one course from Mat Sci 104, 111, 112, 113, 117, C118, or 151;
			elecOne={'MATSCI.104':'MatSci 104', 'MATSCI.111':'MatSci 111', 'MATSCI.112':'MatSci 112', 'MATSCI.113':'MatSci 113', 'MATSCI.117':'MatSci 117', 'MATSCI.C118':'MatSci C118', 'MATSCI.151':'MatSci 151'}
			ans.append(manyChoiceReq(takenClasses, 'Material Science Elective One', elecOne, 'Mat Sci Electives must include one course from Mat Sci 104, 111, 112, 113, 117, C118, or 151'))
			#one course from Mat Sci 121, 122, 123, or 125.
			elecTwo={'MATSCI.121':'MatSci 121', 'MATSCI.122':'MatSci 122', 'MATSCI.123':'MatSci 123', 'MATSCI.125':'MatSci 125'}
			ans.append(manyChoiceReq(takenClasses, 'Material Science Elective Two', elecTwo, 'Mat Sci Electives must include one course from Mat Sci 104, 111, 112, 113, 117, C118, or 151'))
			#Chemistry 120A, Physical Chemistry or Physics 137A,Quantum Mechanics
			ans.append(twoChoiceReq(takenClasses,'Physics', 'CHEM.120A', 'Chem 120A','PHYSICS.137A','Physics 137A', "The Physical Chemistry or Quantum Mechanics requirement"))
			#Chem Eng 142, Chemical Kinetics and Reaction Engineering
			ans.append(basicReq(takenClasses, 'MATSCI.103', 'MatSci 103', "The Phase Transformations and Kinetics requirement"))
			#Chem Eng 150B, Transport and Separation Processes
			ans.append(basicReq(takenClasses, 'CHMENG.150B', 'ChemEng 150B', "The Transport and Separation Processes requirement"))
			#Chem Eng 185, Technical Communication
			ans.append(basicReq(takenClasses, 'CHMENG.185', 'ChemEng 185', "The Technical Communication requirement"))
			#Mat Sci 120, Materials Production
			ans.append(basicReq(takenClasses, 'MATSCI.120', 'MatSci 120', "The Materials Production requirement"))
			#Mat Sci 130, Experimental Materials Science
			ans.append(basicReq(takenClasses, 'MATSCI.130', 'MatSci 130', "The Experimental Materials Science requirement"))
			#Chem Eng 154, Chemical Engineering Laboratory
			ans.append(basicReq(takenClasses, 'CHMENG.154', 'ChemEng 154', "The Chemical Engineering Laboratory requirement"))
			#Chem Eng 160, Chemical Process Design
			ans.append(basicReq(takenClasses, 'CHMENG.160', 'ChemEng 160', "The Chemical Process Design requirement"))
			#Chem Eng 162, Dynamics and Control of Chemical Processes
			ans.append(basicReq(takenClasses, 'CHMENG.162', 'ChemEng 162', "The Dynamics and Control of Chemical Processes requirement"))
			return ans
		# Chemical Engineering and Nuclear Engineering
		elif(major=='CHEMNUCENG'):
			#Eng 7, Introduction to Computer Programming for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7', "The Introduction to Computer Programming requirement"))
			#Physics 7C, Physics for Scientists and Engineers
			ans.append(basicReq(takenClasses, 'PHYSICS.7C', 'Physics 7C', "The Physics for Scientists and Engineers requirement"))
			#Chem Eng 140, Introduction to Chemical Process Analysis
			ans.append(basicReq(takenClasses, 'CHMENG.140', 'ChemEng 140', "The Introduction to Chemical Process Analysis requirement"))
			#Chem Eng 141, Chemical Engineering Thermodynamics
			ans.append(basicReq(takenClasses, 'CHMENG.141', 'ChemEng 141', "The Chemical Engineering Thermodynamics requirement"))
			#Chem Eng 150A, Transport Processes
			ans.append(basicReq(takenClasses, 'CHMENG.150A', 'ChemEng 150A', "The Transport Processes requirement"))
			#EE 100, Electronic Techniques for Engineering
			ans.append(basicReq(takenClasses, 'ELENG.100', 'EE 100', "The Electronic Techniques for Engineering requirement"))
			#Eng 117, Methods of Engineering Analysis
			ans.append(basicReq(takenClasses, 'ENGIN.117', 'E 117', "The Methods of Engineering Analysis requirement"))
			#Nuc Eng 101, Nuclear Reactions and Radiation
			ans.append(basicReq(takenClasses, 'NUCENG.101', 'NucEng 101', "The Nuclear Reactions and Radiation requirement"))
			#Nuc Eng 104, Radiation Detection and Nuclear Instrumentation Lab
			ans.append(basicReq(takenClasses, 'NUCENG.104', 'NucEng 104', "The Radiation Detection and Nuclear Instrumentation Lab requirement"))
			#Nuc Eng 150, Nuclear Reactor Theory
			ans.append(basicReq(takenClasses, 'NUCENG.150', 'NucEng 150', "The Nuclear Reactor Theory requirement"))
			#Chem Eng 142, Chemical Kinetics and Reaction Engineering
			ans.append(basicReq(takenClasses, 'MATSCI.103', 'MatSci 103', "The Phase Transformations and Kinetics requirement"))
			#Chem Eng 150B, Transport and Separation Processes
			ans.append(basicReq(takenClasses, 'CHMENG.150B', 'ChemEng 150B', "The Transport and Separation Processes requirement"))
			#Chem Eng 185, Technical Communication
			ans.append(basicReq(takenClasses, 'CHMENG.185', 'ChemEng 185', "The Technical Communication requirement"))
			#Nuc Eng Electives: Students select nine units of upper division Nuc Eng courses, including
			#at least two courses selected from Nuc Eng 120, 124, or 161.
			celec={'NUCENG.120':'NucEng 120', 'NUCENG.124':'NucEng 124', 'NUCENG.161':'NucEng 161'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'Nuclear Engineering Elective', celec, 'At least two courses selected from Nuc Eng 120, 124, or 161', 2))
			#Chemistry 120A, Physical Chemistry or Physics 137A,Quantum Mechanics
			ans.append(twoChoiceReq(takenClasses, 'CHEM.120A', 'Chem 120A','PHYSICS.137A','Physics 137A', "The Physical Chemistry or Quantum Mechanics requirement"))
			#Chem Eng 154, Chemical Engineering Laboratory
			ans.append(basicReq(takenClasses, 'CHMENG.154', 'ChemEng 154', "The Chemical Engineering Laboratory requirement"))
			#Chem Eng 160, Chemical Process Design
			ans.append(basicReq(takenClasses, 'CHMENG.160', 'ChemEng 160', "The Chemical Process Design requirement"))
			#Chem Eng 162, Dynamics and Control of Chemical Processes
			ans.append(basicReq(takenClasses, 'CHMENG.162', 'ChemEng 162', "The Dynamics and Control of Chemical Processes requirement"))
			return ans
		# Chemical Engineering
		elif(major=='CHEMENG'):
			#CBE. 40, 140, 141, 150A
			ans.append(basicReq(takenClasses, 'CHMENG.40', 'CBE 40', 'Required general chemical and biomolecuular engineering course'))
			ans.append(basicReq(takenClasses, 'CHMENG.140', 'CBE 140', 'Required general chemical and biomolecuular engineering course'))
			ans.append(basicReq(takenClasses, 'CHMENG.141', 'CBE 141', 'Required general chemical and biomolecuular engineering course'))
			ans.append(basicReq(takenClasses, 'CHMENG.150A', 'CBE 150A', 'Required general chemical and biomolecuular engineering course'))
			#Engineering. Engineering 7 (W7 ok)
			ans.append(basicReq(takenClasses, 'ENGIN.7', 'E 7', 'Required general engineering course'))
			#Biology. 1A 
			ans.append(basicReq(takenClasses, 'BIOLOGY.1A', 'Bio 1A', 'Required general biology course'))
			#Chemistry. 120A, or Physics 137A.
			ans.append( twoChoiceReq(takenClasses,'Physical Chemistry', 'CHEM.120A', 'Chem 120A', 'PHYSICS.137A', 'Physics 137A', 'Required class of either Chemistry 120A or Physics 137A'))
			#CBE. 142, 150B, 154, 160, 162, 185.
			ans.append(basicReq(takenClasses, 'CHMENG.142', 'CBE 142', 'Required general chemical and biomolecuular engineering course'))
			ans.append(basicReq(takenClasses, 'CHMENG.150B', 'CBE 150B', 'Required general chemical and biomolecuular engineering course'))
			ans.append(basicReq(takenClasses, 'CHMENG.154', 'CBE 154', 'Required general chemical and biomolecuular engineering course'))
			ans.append(basicReq(takenClasses, 'CHMENG.160', 'CBE 160', 'Required general chemical and biomolecuular engineering course'))
			ans.append(basicReq(takenClasses, 'CHMENG.162', 'CBE 162', 'Required general chemical and biomolecuular engineering course'))
			ans.append(basicReq(takenClasses, 'CHMENG.185', 'CBE 185', 'Required general chemical and biomolecuular engineering course'))
			#Engineering. 45.
			ans.append(basicReq(takenClasses, 'ENGIN.45', 'E 45', 'Required general engineering course'))
			#Electrical Engineering. 40.
			ans.append(basicReq(takenClasses, 'ELENG.40', 'EE 40', 'Required general electrical engineering course'))
			#Option 1
			optionOne=False
			#3 units of CBE electives (CBE 196 may not be used as a CBE elective);
			#170A,170B,C170L,171,176,C178,179,180,H194,
			cbeElec={'CHMENG.170A':'CBE 170A','CHMENG.170B':'CBE 170B','CHMENG.C170L':'CBE C170L','CHMENG.171':'CBE 171','CHMENG.176':'CBE 176','CHMENG.C178':'CBE C178','CHMENG.179':'CBE 179','CHMENG.180':'CBE 180','CHMENG.H194':'CBE H194'}
			cbeUnits=0
			cbeTaken=[]
			cbeNotTaken=[]
			for key in cbeElec:
				if key in takenClasses:
					cbeUnits+=units(key)
					cbeTaken.append(cbeElec[key])
				else:
					cbeNotTaken.append(cbeElec[key])
			#6 units of engineering selected from the following: 
			#Bioengineering 100, 104, C105B, 110, 111, 112, C112, C117, 121, C125, 132, C136L, 143, C144, C144L, 147, 150, 151, 163, C165, C181
			#CBE 170A, 170B, C170L, 171, 176, C178, 179, 180, H194, C195A (C195A may be repeated for credit when the topic changes), 196
			#Chemistry C138
			#Civil and Environmental Engineering 103, 105, 107, 114, 115, 120, 130N, 131, C133, 175, 176, 180, 186, 193
			#Computer Science C149
			#Electrical Engineering 105, C125, 130, 134, 143, C145B, C145O, 147, C149
			#Engineering 117, 120
			#Industrial Engineering and Operations Research 160, 162
			#Materials Science and Engineering 112, 113, 120, 121, 122, 123, 136, 140, 151
			#Mechanical Engineering 102A, 102B, 104, C105B, 106, 107, 108, 109, 110, C115, C117, 119, 122, 127, 131, 135, 140, 142, 146, 151, 166, 171, C177L, C180, 185
			#Nuclear Engineering 101, 124
			#Plant and Microbial Biology C124, C144, C144L
			engin={'BIOENG.100':'BioEng 100','BIOENG.104':'BioEng 104','BIOENG.C105B':'BioEng C105B','BIOENG.110':'BioEng 110','BIOENG.111':'BioEng 111','BIOENG.112':'BioEng 112','BIOENG.C112':'BioEng C112',
				'BIOENG.C117':'BioEng C117','BIOENG.121':'BioEng 121','BIOENG.C125':'BioEng C125','BIOENG.132':'BioEng 132','BIOENG.C136L':'BioEng C136L','BIOENG.143':'BioEng 143','BIOENG.C144':'BioEng C144',
				'BIOENG.C144L':'BioEng C144L','BIOENG.147':'BioEng 147','BIOENG.150':'BioEng 150','BIOENG.151':'BioEng 151','BIOENG.163':'BioEng 163','BIOENG.C165':'BioEng C165','BIOENG.C181':'BioEng C181',
				'CHEM.C138':'Chem C138',
				'CIVENG.103':'CivEng 103','CIVENG.105':'CivEng 105','CIVENG.107':'CivEng 107','CIVENG.114':'CivEng 114','CIVENG.115':'CivEng 115','CIVENG.120':'CivEng 120','CIVENG.130N':'CivEng 130N','CIVENG.131':'CivEng 131',
				'CIVENG.C133':'CivEng C133','CIVENG.175':'CivEng 175','CIVENG.176':'CivEng 176','CIVENG.180':'CivEng 180','CIVENG.186':'CivEng 186','CIVENG.193':'CivEng 193',
				'COMPSCI.C149':'CompSci C149',
				'ELENG.105':'EE 105','ELENG.C125':'EE C125','ELENG.130':'EE 130','ELENG.134':'EE 134','ELENG.143':'EE 143','ELENG.C145B':'EE C145B','ELENG.C145O':'EE C145O','ELENG.147':'EE 147','ELENG.C149':'EE C149',
				'ENGIN.117':'E 117','ENGIN.120':'E 120',
				'INDENG.160':'IndEng 160','INDENG.162':'IndEng 162',
				'MATSCI.112':'MatSci 112','MATSCI.113':'MatSci 113','MATSCI.120':'MatSci 120','MATSCI.121':'MatSci 121','MATSCI.122':'MatSci 122','MATSCI.123':'MatSci 123','MATSCI.136':'MatSci 136','MECENG.140':'ME 140','MECENG.151':'ME 151',
				'MECENG.102A':'ME 102A','MECENG.102B':'ME 102B','MECENG.104':'ME 104','MECENG.C105B':'ME C105B','MECENG.106':'ME 106','MECENG.107':'ME 107','MECENG.108':'ME 108','MECENG.109':'ME 109','MECENG.110':'ME 110',
				'MECENG.C115':'ME C115','MECENG.C117':'ME C117','MECENG.119':'ME 119','MECENG.122':'ME 122','MECENG.127':'ME 127','MECENG.131':'ME 131','MECENG.135':'ME 135','MECENG.140':'ME 140',
				'MECENG.142':'ME 142','MECENG.146':'ME 146','MECENG.151':'ME 151','MECENG.166':'ME 166','MECENG.171':'ME 171','MECENG.C177L':'ME C177L','MECENG.C180':'ME C180','MECENG.185':'ME 185',
				'NUCENG.101':'NucEng 101','NUCENG.124':'NucEng 124',
				'PLANTBI.C124':'PMB C124','PLANTBI.C144':'PMB C144','PLANTBI.C144L':'PMB C144L'}
			eTaken=[]
			eNotTaken=[]
			eUnit=0
			for key in engin:
				if key in takenClasses:
					eUnit+=units(key)
					eTaken.append(engin[key])
				else:
					eNotTaken.append(engin[key])
			#3 units of science elective selected from the list of Physical and Biological Science Electives		
			#Anthropology 1, C100, C103, 107, C131, 132, 134, 135
			#Astronomy 3, 7A, 7B, 10, C10, C12, C162
			#Biology 1B
			#Chemistry 103, 104A, 104B, 105, 108, 112B, 113, 114, 115, 120B, 122, 125, C130, 135, 143, 146, C150, C182, C191, 192, H194, 196
			#Civil and Environmental Engineering C106, C116
			#Cognitive Science C102, C110, C126, C127
			#Computer Science C182
			#Earth and Planetary Science 3, 8, C12, 20, C20, 50, 80, C82, 100A, 103, 105, 108, 117, C129, 130, C141, C146, C162, C171, C180, 181, C182, 185
			#Energy and Resources Group 102
			#English C77
			#Environmental Science, Policy, and Management 2, 4, 15, C10, C11, C12, 40, 42, 44, 100, 102A, 102B, 102C, C103, 106, C107, 108A, 108B, 109, 110, 112, 113, 114, 115B, 117, 118, 119, 120, C128, C129, C130, 131, 134, 137, C138, 140, 142, 144, 145, 146, 148, C149, 152, 172, 174, C180, 181, 185, 186, 187
			#Environmental Sciences 10, 125
			#Geography 1, 35, 40, C82, C136, 137, 140A, C141, 143, 144, C145, 148, 171
			#Integrative Biology 31, 32, 41, C82, C101, C101L, 102, 102LF, 103, 103LF, 104, 104LF, 106, 106A, C107, C107L, 115, 117, 117L, 118, 123A, 123AL, 131, 135, 137, C139, C142L, C143A, C143B, 144, 148, C149, 151, 152, 153, 154, 154L, 155, C156, 157L, 158LF, 159, 161, 162, 164, 165, 168, 168L, 169, 174, 174LF, 183, 183L, 184, 184L, C185L, 187
			#Letters and Science C30U, C30V, C30W, C70T, C70U, C70W, C70Y
			#Linguistics C109
			#Materials Science and Engineering C150
			#Molecular and Cell Biology 32, 41, 50, C61, C62, 64, C100A, 100B, 102, C103, 104, 111, C112, 113, C114, 115, C116, 130A, 132, 133L, 135A, 135E, 136, 140, 140L, 141, 143, C148, 150, C160, 160L, 163, 166, 167
			#Nutritional Science and Toxicology 10, 11, 106, 107, 108A, 110, C112, C119, 120, 150, 160, 171
			#Physics 7C, C21, 105, 110A, 110B, 112, 129, 130, 132, 137B, 138, 141A, 177
			#Plant and Microbial Biology 10, 40, C102, C102L, C103, C107, C107L, 110, 110L, C112, C114, C116, 120, 120L, 122, 135, C148, 150, 160, 170, 180
			#Psychology 110, 111, C112, C113, 114, 115A, C115B, C116, 117, 119, 122, C126, C127, C129
			#Public Health C102, 162A, C170B, 172, C172
			#Undergraduate and Interdisciplinary Studies C12
			scienceTaken=[]
			scienceNotTaken=[]
			scienceUnits=0
			scienceElec={'ANTRO.1':'Anthro 1','ANTRO.C100':'Anthro C100','ANTRO.C103':'Anthro C103','ANTRO.107':'Anthro 107','ANTRO.C131':'Anthro C131','ANTRO.132':'Anthro 132','ANTRO.134':'Anthro 134','ANTRO.135':'Anthro 135',
				'ASTRON.3':'Astro 3','ASTRON.7A':'Astro 7A','ASTRON.7B':'Astro 7B','ASTRON.10':'Astro 10','ASTRON.C10':'Astro C10','ASTRON.C12':'Astro C12','ASTRON.C162':'Astro C162',
				'BIOLOGY.1B':'Bio 1B',
				'CHEM.103':'Chem 103','CHEM.104A':'Chem 104A','CHEM.104B':'Chem 104B','CHEM.105':'Chem 105','CHEM.108':'Chem 108','CHEM.112B':'Chem 112B','CHEM.113':'Chem 113','CHEM.114':'Chem 114','CHEM.115':'Chem 115','CHEM.120B':'Chem 120B',
				'CHEM.122':'Chem 122','CHEM.125':'Chem 125','CHEM.C130':'Chem C130','CHEM.135':'Chem 135','CHEM.143':'Chem 143','CHEM.146':'Chem 146','CHEM.C150':'Chem C150','CHEM.C182':'Chem C182','CHEM.C191':'Chem C191','CHEM.192':'Chem 192',
				'CHEM.H194':'Chem H194','CHEM.196':'Chem 196',
				'CIVENG.C106':'CivEng C106','CIVENG.C116':'CivEng C116',
				'COGSCI.C102':'CogSci C102','COGSCI.C110':'CogSci C110','COGSCI.C126':'CogSci C126','COGSCI.C127':'CogSci C127',
				'COMPSCI.C182':'CompSci C182',
				'EPS.3':'EPS 3','EPS.8':'EPS 8','EPS.C12':'EPS C12','EPS.20':'EPS 20','EPS.C20':'EPS C20','EPS.50':'EPS 50','EPS.80':'EPS 80','EPS.C82':'EPS C82','EPS.100A':'EPS 100A',
				'EPS.103':'EPS 103','EPS.105':'EPS 105','EPS.108':'EPS 108','EPS.117':'EPS 117','EPS.C129':'EPS C129','EPS.130':'EPS 130','EPS.C141':'EPS C141','EPS.C146':'EPS C146','EPS.C162':'EPS C162',
				'EPS.C171':'EPS C171','EPS.C180':'EPS C180','EPS.181':'EPS 181','EPS.C182':'EPS C182','EPS.185':'EPS 185',
				'ENERES.102':'ERG 102',
				'ENGLISH.C77':'English C77',
				'ESPM.2':'ESPM 2','ESPM.4':'ESPM 4','ESPM.15':'ESPM 15','ESPM.C10':'ESPM C10','ESPM.C11':'ESPM C11','ESPM.C12':'ESPM C12','ESPM.40':'ESPM 40','ESPM.42':'ESPM 42','ESPM.44':'ESPM 44','ESPM.100':'ESPM 100',
				'ESPM.102A':'ESPM 102A','ESPM.102B':'ESPM 102B','ESPM.102C':'ESPM 102C','ESPM.C103':'ESPM C103','ESPM.106':'ESPM 106','ESPM.C107':'ESPM C107','ESPM.108A':'ESPM 108A','ESPM.108B':'ESPM 108B','ESPM.109':'ESPM 109','ESPM.110':'ESPM 110',
				'ESPM.112':'ESPM 112','ESPM.113':'ESPM 113','ESPM.114':'ESPM 114','ESPM.115B':'ESPM 115B','ESPM.117':'ESPM 117','ESPM.118':'ESPM 118','ESPM.119':'ESPM 119','ESPM.120':'ESPM 120','ESPM.C128':'ESPM C128','ESPM.C129':'ESPM C129',
				'ESPM.C130':'ESPM C130','ESPM.131':'ESPM 131','ESPM.134':'ESPM 134','ESPM.137':'ESPM 137','ESPM.C138':'ESPM C138','ESPM.140':'ESPM 140','ESPM.142':'ESPM 142','ESPM.144':'ESPM 144','ESPM.145':'ESPM 145','ESPM.146':'ESPM 146',
				'ESPM.148':'ESPM 148','ESPM.C149':'ESPM C149','ESPM.152':'ESPM 152','ESPM.172':'ESPM 172','ESPM.174':'ESPM 174','ESPM.C180':'ESPM C180','ESPM.181':'ESPM 181','ESPM.185':'ESPM 185','ESPM.186':'ESPM 186','ESPM.187':'ESPM 187',
				'ENVSCI.10':'EnvSci 10','ENVSCI.125':'EnvSci 125',
				'GEOG.1':'Geog 1','GEOG.35':'Geog 35','GEOG.40':'Geog 40','GEOG.C82':'Geog C82','GEOG.C136':'Geog C136','GEOG.137':'Geog 137','GEOG.140A':'Geog 140A',
				'GEOG.C141':'Geog C141','GEOG.143':'Geog 143','GEOG.144':'Geog 144','GEOG.C145':'Geog C145','GEOG.148':'Geog 148','GEOG.171':'Geog 171',
				'INTEGBI.31':'IB 31','INTEGBI.32':'IB 32','INTEGBI.41':'IB 41','INTEGBI.C82':'IB C82','INTEGBI.C101':'IB C101','INTEGBI.C101L':'IB C101L','INTEGBI.102':'IB 102','INTEGBI.102LF':'IB 102LF','INTEGBI.103':'IB 103','INTEGBI.103LF':'IB 103LF',
				'INTEGBI.104':'IB 104','INTEGBI.104LF':'IB 104LF','INTEGBI.106':'IB 106','INTEGBI.106A':'IB 106A','INTEGBI.C107':'IB C107','INTEGBI.C107L':'IB C107L','INTEGBI.115':'IB 115','INTEGBI.117':'IB 117','INTEGBI.117L':'IB 117L','INTEGBI.118':'IB 118',
				'INTEGBI.123A':'IB 123A','INTEGBI.123AL':'IB 123AL','INTEGBI.131':'IB 131','INTEGBI.135':'IB 135','INTEGBI.137':'IB 137','INTEGBI.C139':'IB C139','INTEGBI.C142L':'IB C142L','INTEGBI.C143A':'IB C143A','INTEGBI.C143B':'IB C143B','INTEGBI.144':'IB 144',
				'INTEGBI.148':'IB 148','INTEGBI.C149':'IB C149','INTEGBI.151':'IB 151','INTEGBI.152':'IB 152','INTEGBI.153':'IB 153','INTEGBI.154':'IB 154','INTEGBI.154L':'IB 154L','INTEGBI.155':'IB 155','INTEGBI.C156':'IB C156','INTEGBI.157L':'IB 157L',
				'INTEGBI.158LF':'IB 158LF','INTEGBI.159':'IB 159','INTEGBI.161':'IB 161','INTEGBI.162':'IB 162','INTEGBI.164':'IB 164','INTEGBI.165':'IB 165','INTEGBI.168':'IB 168','INTEGBI.168L':'IB 168L','INTEGBI.169':'IB 169','INTEGBI.174':'IB 174',
				'INTEGBI.174LF':'IB 174LF','INTEGBI.183':'IB 183','INTEGBI.183L':'IB 183L','INTEGBI.184':'IB 184','INTEGBI.184L':'IB 184:','INTEGBI.C185L':'IB C185L','INTEGBI.187':'IB 187',
				'L&S.C30U':'L&S C30U','L&S.C30V':'L&S C30V','L&S.C30W':'L&S C30W','L&S.C70T':'L&S C70T','L&S.C70U':'L&S C70U','L&S.C70W':'L&S C70W','L&S.C70Y':'L&S C70Y',
				'LINGUIS.C109':'Ling C109',
				'MATSCI.C150':'MatSci C150',
				'MCELLBI.32':'MCB 32','MCELLBI.41':'MCB 41','MCELLBI.50':'MCB 50','MCELLBI.C61':'MCB C61','MCELLBI.C62':'MCB C62','MCELLBI.64':'MCB 64','MCELLBI.C100A':'MCB C100A','MCELLBI.100B':'MCB 100B','MCELLBI.102':'MCB 102',
				'MCELLBI.C103':'MCB C103','MCELLBI.104':'MCB 104','MCELLBI.111':'MCB 111','MCELLBI.C112':'MCB C112','MCELLBI.113':'MCB 113','MCELLBI.C114':'MCB C114','MCELLBI.115':'MCB 115','MCELLBI.C116':'MCB C116','MCELLBI.130A':'MCB 130A',
				'MCELLBI.132':'MCB 132','MCELLBI.133L':'MCB 133L','MCELLBI.135A':'MCB 135A','MCELLBI.135E':'MCB 135E','MCELLBI.136':'MCB 136','MCELLBI.140':'MCB 140','MCELLBI.140L':'MCB 140L','MCELLBI.141':'MCB 141',
				'MCELLBI.143':'MCB 143','MCELLBI.C148':'MCB C148','MCELLBI.150':'MCB 150','MCELLBI.C160':'MCB C160','MCELLBI.160L':'MCB 160L','MCELLBI.163':'MCB 163','MCELLBI.166':'MCB 166','MCELLBI.167':'MCB 167',
				'NUSCTX.10':'NutriSci 10','NUSCTX.11':'NutriSci 11','NUSCTX.106':'NutriSci 106','NUSCTX.107':'NutriSci 107','NUSCTX.108A':'NutriSci 108A','NUSCTX.110':'NutriSci 110',
				'NUSCTX.C112':'NutriSci C112','NUSCTX.C119':'NutriSci C119','NUSCTX.120':'NutriSci 120','NUSCTX.150':'NutriSci 150','NUSCTX.160':'NutriSci 160','NUSCTX.171':'NutriSci 171',
				'PHYSICS.7C':'Physics 7C','PHYSICS.C21':'Physics C21','PHYSICS.105':'Physics 105','PHYSICS.110A':'Physics 110A','PHYSICS.110B':'Physics 110B','PHYSICS.112':'Physics 112','PHYSICS.129':'Physics 129',
				'PHYSICS.130':'Physics 130','PHYSICS.132':'Physics 132','PHYSICS.137B':'Physics 137B','PHYSICS.138':'Physics 138','PHYSICS.141A':'Physics 141A','PHYSICS.177':'Physics 177',
				'PLANTBI.10':'PMB 10','PLANTBI.40':'PMB 40','PLANTBI.C102':'PMB C102','PLANTBI.C102L':'PMB C102L','PLANTBI.C103':'PMB C103','PLANTBI.C107':'PMB C107','PLANTBI.C107L':'PMB C107L',
				'PLANTBI.110':'PMB 110','PLANTBI.110L':'PMB 110L','PLANTBI.C112':'PMB C112','PLANTBI.C114':'PMB C114','PLANTBI.C116':'PMB C116','PLANTBI.120':'PMB 120','PLANTBI.120L':'PMB 120L',
				'PLANTBI.122':'PMB 122','PLANTBI.135':'PMB 135','PLANTBI.C148':'PMB C148','PLANTBI.150':'PMB 150','PLANTBI.160':'PMB 160','PLANTBI.170':'PMB 170','PLANTBI.180':'PMB 180',
				'PSYCH.110':'Psych 110','PSYCH.111':'Psych 111','PSYCH.C112':'Psych C112','PSYCH.C113':'Psych C113','PSYCH.114':'Psych 114','PSYCH.115A':'Psych 115A','PSYCH.C115B':'Psych C115B',
				'PSYCH.C116':'Psych C116','PSYCH.117':'Psych 117','PSYCH.119':'Psych 119','PSYCH.122':'Psych 122','PSYCH.C126':'Psych C126','PSYCH.C127':'Psych C127','PSYCH.C129':'Psych C129',
				'PBHLTH.C102':'PublicHealth C102','PBHLTH.162A':'PublicHealth 162A','PBHLTH.C170B':'PublicHealth C170B','PBHLTH.172':'PublicHealth 172','PBHLTH.C172':'PublicHealth C172',
				'UGIS.C12':'UGIS C12'}
			for key in scienceElec:
				if key in takenClasses:
					scienceUnits+=units(key)
					scienceTaken.append(scienceElec[key])
				else:
					scienceNotTaken.append(scienceElec[key])
			if (eUnit>=6 and cbeUnits>=3 and scienceUnits>=3):
				optionOne=True
			#Option 2: Concentrations
			#Biotechnology:Chemistry 112B or Molecular and Cell Biology C112;CBE 170A, *170B, and *C170L
			optionTwo=(('CHEM.112B'in takenClasses)or ('MCELLBI.C112'in takenClasses))and ('CHMENG.170A'in takenClasses) and ('CHMENG.170B'in takenClasses) and ('CHMENG.C170L'in takenClasses)
			#Chemical Processing: Chemistry 104A or 112B; 6 units of CBE electives chosen from the following: 170A, 170B, C170L, 171, 176, C178, 179, 180, H194 (up to 3 units);
			#3 units of engineering selected from the following: Civil and Environmental Engineering C30, 111, 114, 173; Materials Science and Engineering 111, 112, 113, C118, 120, 121, 122, 123; Mechanical Engineering 140, 151
			engineer={'CIVENG.C30':'CivEng C30','CIVENG.111':'CivEng 111','CIVENG.114':'CivEng 114','CIVENG.173':'CivEng 173',
				'MATSCI.111':'MatSci 111','MATSCI.112':'MatSci 112','MATSCI.113':'MatSci 113','MATSCI.C118':'MatSci C118','MATSCI.120':'MatSci 120','MATSCI.121':'MatSci 121','MATSCI.122':'MatSci 122','MATSCI.123':'MatSci 123',
				'MECENG.140':'ME 140','MECENG.151':'ME 151'}
			engineerUnits=0
			for key in engineer:
				if key in takenClasses:
					engineerUnits+=units(key)
			optionThree=(('CHEM.104A'in takenClasses)or ('CHEM.112B'in takenClasses))and (cbeUnits>=6)and (engineerUnits>=3)
			#Environmental Technology:Chemistry 112B or 104A; CBE 170A; 
			#6 units chosen from the following: CBE 176; Civil and Environmental Engineering 108, 111, 113N, C116, 173; Mechanical Engineering 140
			environTechUnits=0
			environTech={'CHMENG.176':'CBE 176','CIVENG.108':'CivEng 108','CIVENG.111':'CivEng 111','CIVENG.113N':'CivEng 113N','CIVENG.C116':'CivEng C116','CIVENG.173':'CivEng 173','MECENG.140':'ME 140'}
			for key in environTech:
				if key in takenClasses:
					environTechUnits+=units(key)
			optionFour=(('CHEM.104A'in takenClasses)or ('CHEM.112B'in takenClasses))and ('CHMENG.170A'in takenClasses) and ('MECENG.140'in takenClasses) and (environTechUnits>=6)
			#Materials Science and Technology: One of Chemistry 104A, 108, or 112B;3 units of CBE elective selected from the following: 176, C178, 179;
			#6 units chosen from the following: Civil and Environmental Engineering C30; Electrical Engineering 130, 143; Materials Science and Engineering 102, 103, 111, 112, 120, 121, 122, 123, 125; Mechanical Engineering 122, 127
			matTech={'CIVENG.C30':'CivEng C30','ELENG.130':'EE 130','ELENG.143':'EE 143','MATSCI.102':'MatSci 102','MATSCI.103':'MatSci 103','MATSCI.111':'MatSci 111','MATSCI.112':'MatSci 112','MATSCI.120':'MatSci 120','MATSCI.121':'MatSci 121','MATSCI.122':'MatSci 122','MATSCI.123':'MatSci 123','MATSCI.125':'MatSci 125','MECENG.122':'ME 122','MECENG.127':'ME 127'}
			matTechUnits=0
			for key in matTech:
				if key in takenClasses:
					matTechUnits+=units(key)
			optionFive=(('CHEM.104A'in takenClasses)or ('CHEM.112B'in takenClasses)or ('CHEM.108'in takenClasses)) and (cbeUnits>=3)and (matTechUnits>=6)
			#Applied Physical Science:6 units of chemistry or physics courses selected from the list of Physical and Biological Science Electives;3 units of CBE elective (CBE 196 may not be used as a CBE elective);3 units of engineering electives selected from the list of Engineering Electives
			optionSix=(scienceUnits>=6)and (cbeUnits>=3)and (eUnit>=3)
			if (optionOne or optionTwo or optionThree or optionFour or optionFive or optionSix):
				ans.append({'reqName':'Concentration', 'reqCompleted':True, 'reqDescription':'You must complete one concentration as outlined on http://chemistry.berkeley.edu/student_info/undergrad_info/degree_programs/cheme_major/upper_division_courses.php','courseDone':scienceTaken+eTaken+cbeTaken, 'courseLeft':scienceNotTaken+eNotTaken+cbeNotTaken})
			else:
				ans.append({'reqName':'Concentration', 'reqCompleted':False, 'reqDescription':'You must complete one concentration as outlined on http://chemistry.berkeley.edu/student_info/undergrad_info/degree_programs/cheme_major/upper_division_courses.php','courseDone':scienceTaken+eTaken+cbeTaken, 'courseLeft':scienceNotTaken+eNotTaken+cbeNotTaken})
			return ans
		# Chemical Biology
		elif(major=='CHEMBIO'):
			#Biology.  1A and 1AL
			ans.append(twoReq(takenClasses, 'Basic Biology', 'BIOLOGY.1A', 'Bio 1A','BIOLOGY.1AL', 'Bio 1AL', 'Basic Biology requirement of both Bio 1A and Bio 1AL'))
			#Chemistry. 103, C110L, 120A, 120B, 135
			ans.append(basicReq(takenClasses, 'CHEM.103', 'Chem 103', 'Basic Chemistry requirement of Chem 103'))
			ans.append(basicReq(takenClasses, 'CHEM.C110L', 'Chem C110L', 'Basic Chemistry requirement of Chem C110L'))
			ans.append(basicReq(takenClasses, 'CHEM.120A', 'Chem 120A', 'Basic Chemistry requirement of Chem 120A'))
			ans.append(basicReq(takenClasses, 'CHEM.120B', 'Chem 120B', 'Basic Chemistry requirement of Chem 120B'))
			ans.append(basicReq(takenClasses, 'CHEM.135', 'Chem 135', 'Basic Chemistry requirement of Chem 135'))
			#Chemistry. one of the following choices: 105, 125, C170L, or C182.
			chemElec={'CHEM.105':'Chem 105','CHEM.125':'Chem 125','CHEM.C170L':'Chem C170L','CHEM.C182':'Chem C182'}
			ans.append(manyChoiceReq(takenClasses, 'Advanced Chemistry', chemElec, 'The requirement of one of the following choices: Chemistry 105, 125, C170L, or C182'))
			#Molecular and Cell Biology. 110.
			ans.append(basicReq(takenClasses, 'MCELLBI.110', 'MCB 110', 'Advanced Biology requirement of MCB 110'))
			#Seven Units of Upper Division Chemistry and Allied Subjects. In addition to the requirements listed above, the following must be completed to total at least seven units:
			elecUnits=0
			chemReqs=['CHEM.4A','CHEM.4B','CHEM.112A','CHEM.112B','CHEM.104A','CHEM.104B','CHEM.120A','CHEM.120B','CHEM.125','CHEM.C182']
			elecTaken=[]
			elecNotTaken=[]
			for item in takenClasses:
				if (('CHEM' in item) and (not(item in chemReqs))):
					elecUnits+=units(item)
					elecTaken.append(item.replace('.',' '))
			elecNotTaken.append('Any additional Chem Class (not 4A/B,112A/B,104A/B,120A/B,125,C182)')
			for key in allied:
				if (key in takenClasses):
					elecUnits+=units(item)
					elecTaken.append(allied[key])
				else:
					elecNotTaken.append(allied[key])
			if(elecUnits>=7):
				ans.append({'reqName':'Technical Elective', 'reqCompleted':True, 'reqDescription':'You must take at least 7 units of electives either in Chemistry or included in the Allied Classes List','courseDone':elecTaken, 'courseLeft':['Any additional Chem Class (not 4A/B,112A/B,104A/B,120A/B,125,C182)']})
			else:
				ans.append({'reqName':'Technical Elective', 'reqCompleted':False, 'reqDescription':'You must take at least 7 units of electives either in Chemistry or included in the Allied Classes List','courseDone':[], 'courseLeft':['Any additional Chem Class (not 4A/B,112A/B,104A/B,120A/B,125,C182)']})
			return ans
		# Bachelor of Arts Degree in Chemistry
		elif(major=='BACHEM'):
			#Chemistry. 104A, 104B (103 and 135 may be taken in place of 104A, 104B), 120A, 120B, and a choice of one of 105, 108, 115, 125, C170L, or C182.
			temp1=twoReq(takenClasses, '', 'CHEM.104A', 'Chem 104A', 'CHEM.104B', 'Chem 104B', '')
			temp2=twoReq(takenClasses, '', 'CHEM.103', 'Chem 103', 'CHEM.135', 'Chem 135', '')
			if (temp1['reqCompleted'] or temp2['reqCompleted']):
				ans.append({'reqName':'Basic Chemistry', 'reqCompleted':True, 'reqDescription':'Either Chem 104A and 104B or 103 and 135','courseDone':temp1['courseDone']+temp2['courseDone'], 'courseLeft':temp1['courseLeft']+temp2['courseLeft']})
			else:
				ans.append({'reqName':'Basic Chemistry', 'reqCompleted':False, 'reqDescription':'Either Chem 104A and 104B or 103 and 135','courseDone':temp1['courseDone']+temp2['courseDone'], 'courseLeft':temp1['courseLeft']+temp2['courseLeft']})
			ans.append(twoReq(takenClasses, 'Physical Chemistry', 'CHEM.120A', 'Chem 120A', 'CHEM.120B', 'Chem 120B', 'Required Chemistry 120A and 120B'))
			chem={'CHEM.105':'Chem 105','CHEM.108':'Chem 108','CHEM.115':'Chem 115','CHEM.125':'Chem 125','CHEM.C170L':'Chem C170L','CHEM.C182':'Chem C182'}
			ans.append(manyChoiceReq(takenClasses, 'Chem Elective', chem, 'You must complete your choice of Chem 105, 108, 115, 125, C170L, or C182'))
			return ans
		# Chemical Engineering and Materials Science and Engineering
		elif(major=='CHEMMATSCI'):
			#to be changed
			return ans
		# Chemical Engineering and Nuclear Engineering
		elif(major=='CHEMNUCENG'):
			#to be changed
			return ans
		#Should not occur but in the case that the major given does not match
		else:
			raise MyError(major+"is not a valid major at UC Berkeley College of Engineering")
	# College of Natural Resources
	elif (college=='NaturalResources'):
		# College Requirements		
		#Two courses in Reading & Composition (8 units): R1A and R1B
		#Reading and Composition
		OneA=False
		OneB=False
		for item in takenClasses:
			if 'R1A' in item:
				OneA=True
			if 'R1B' in item:
				OneB=True
		if (OneA and OneB):
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':True, 'reqDescription':"Take at least one course labeled R1A and R1B",'courseDone':[], 'courseLeft':[]})
		elif (OneA):
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled R1A and R1B. You have completed R1A",'courseDone':[], 'courseLeft':[]})
		elif (OneB):
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled R1A and R1B. You have completed R1B",'courseDone':[], 'courseLeft':[]})
		else:
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled R1A and R1B",'courseDone':[], 'courseLeft':[]})
		# 15 upper division units must be in the College of Natural Resources (EEP, ES, ESPM, NST, PMB, ERG)
		upperUnits=0
		upperDone=[]
		for item in takenClasses:
				if((re.search(r'ENVECON.1\d\d',item)) or (re.search(r'ENVSCI.1\d\d',item)) or (re.search(r'ESPM.1\d\d',item)) or (re.search(r'NUSCTX.1\d\d',item)) or (re.search(r'PLANTBI.1\d\d',item)) or (re.search(r'ENERES.1\d\d',item))):
					upperDone.append(item.replace('.',' '))
					upperUnits+=units(item)
		if (upperUnits>=15):
			ans.append({'reqName':'CNR', 'reqCompleted':True, 'reqDescription':"Take at least 15 upper division units in the College of Natural Resources (EEP, ES, ESPM, NST, PMB, ERG)",'courseDone':[], 'courseLeft':[]})
		else:
			ans.append({'reqName':'CNR', 'reqCompleted':False, 'reqDescription':"Take at least 15 upper division units in the College of Natural Resources (EEP, ES, ESPM, NST, PMB, ERG)",'courseDone':[], 'courseLeft':[]})		
		# Conservation and Resource Studies
		if (major=='CRS'):
			#ESPM Environmental Sci Core: 1 from ESPM 2, ESPM 6, ESPM C10 (L&S C30V), or ESPM 15 (formerly ES 10)
			core={'ESPM.2':'ESPM 2', 'ESPM.6':'ESPM 6', 'ESPM.C10':'ESPM C10', 'ESPM.15':'ESPM 15','L&S.C30V':'L&S C30V'}
			ans.append(manyChoiceReq(takenClasses, 'ESPM Environmental Science Core', core, 'For the ESPM Environmental Sci Core you must complete one from ESPM 2, ESPM 6, ESPM C10 (L&S C30V), or ESPM 15'))
			#ESPM Social Science Core: 1 course from ESPM C11 (L&S C30U), ESPM C12, ESPM 50AC or ESPM 60
			socialcore={'ESPM.50AC':'ESPM 50AC', 'ESPM.C12':'ESPM C12', 'ESPM.C11':'ESPM C11', 'ESPM.60':'ESPM 60','L&S.C30U':'L&S C30U'}
			ans.append(manyChoiceReq(takenClasses, 'ESPM Social Science Core', socialcore, 'For the ESPM Social Science Core you must complete one from ESPM C11 (L&S C30U), ESPM C12, ESPM 50AC or ESPM 60'))
			#One course in General Biology with lab from the following list: Biology 1A: Molecular & Cellular Biology, Biology 1B: Plants/Ecology/Evolution, or Biology 11: Introduction to the Science of Living Organisms.
			genbio={'BIOLOGY.1A':'Bio 1A','BIOLOGY.1B':'Bio 1B','BIOLOGY.11':'Bio 11'}
			ans.append(manyChoiceReq(takenClasses, 'General Biology', genbio, 'You must take one general biology class out of 1A, 1B, and 11'))
			#Breadth
			temp=sevenBreadth(takenClasses)
			one=False
			oneTaken=[]
			oneNotTaken=[]
			two=False
			twoTaken=[]
			twoNotTaken=[]
			three=False
			threeTaken=[]
			threeNotTaken=[]
			for item in temp:
				if item['reqName'] in ['International Studies Breadth','Social and Behavioral Science Breadth'] :
					one= one or item['reqCompleted']
					oneTaken= oneTaken + item['courseDone']
					oneNotTaken= oneNotTaken + item['courseLeft']
				elif item['reqName'] is 'Physical Science Breadth':
					two= two or item['reqCompleted']
					twoTaken= twoTaken + item['courseDone']
					twoNotTaken= twoNotTaken + item['courseLeft']
				elif item['reqName'] in ['Art and Literature Breadth','Historical Studies Breadth','Philosophy and Values Breadth'] :
					three= three or item['reqCompleted']
					threeTaken= threeTaken + item['courseDone']
					threeNotTaken= threeNotTaken + item['courseLeft']
			#One course (3-4 units) in Social & Behavioral Sciences or International Studies
				if one:
					ans.append({'reqName':'Social & Behavioral Sciences or International Studies Breadth', 'reqCompleted':True, 'reqDescription':'You must take one social & behavioral sciences or international studies course. For more info see: http://http://ls-advise.berkeley.edu/requirement/7breadth.html','courseDone':oneTaken, 'courseLeft':oneNotTaken})
				else:
					ans.append({'reqName':'Social & Behavioral Sciences or International Studies Breadth', 'reqCompleted':False, 'reqDescription':'You must take one social & behavioral sciences or international studies course. For more info see: http://http://ls-advise.berkeley.edu/requirement/7breadth.html','courseDone':[], 'courseLeft':oneNotTaken})
			#One course (3-4 units) in Physical Sciences
				if two:
					ans.append({'reqName':'Physical Sciences Breadth', 'reqCompleted':True, 'reqDescription':'You must take one physical sciences course. For more info see: http://http://ls-advise.berkeley.edu/requirement/7breadth.html','courseDone':twoTaken, 'courseLeft':twoNotTaken})
				else:
					ans.append({'reqName':'Physical Sciences Breadth', 'reqCompleted':False, 'reqDescription':'You must take one physical sciences course. For more info see: http://http://ls-advise.berkeley.edu/requirement/7breadth.html','courseDone':[], 'courseLeft':twoNotTaken})
			#One course (3-4 units) in Arts & Literature, Historical Studies, or Philosophy & Values
				if three:
					ans.append({'reqName':'Arts & Literature, Historical Studies, or Philosophy & Values Breadth', 'reqCompleted':True, 'reqDescription':'You must take one Arts & Literature, Historical Studies, or Philosophy & Values course. For more info see: http://http://ls-advise.berkeley.edu/requirement/7breadth.html','courseDone':threeTaken, 'courseLeft':threeNotTaken})
				else:
					ans.append({'reqName':'Arts & Literature, Historical Studies, or Philosophy & Values Breadth', 'reqCompleted':False, 'reqDescription':'You must take one Arts & Literature, Historical Studies, or Philosophy & Values course. For more info see: http://http://ls-advise.berkeley.edu/requirement/7breadth.html','courseDone':[], 'courseLeft':threeNotTaken})
			#One Calculus or Statistics course: Math 16A, 16B, 1A or 1B; Statistics 2, 20, 25, 131A, or PH 142A.
			math={'MATH.16A':'Math 16A','MATH.16B':'Math 16B','MATH.1A':'Math 1A','MATH.1B':'Math 1B','STAT.2':'Stats 2','STAT.20':'Stats 20','STAT.25':'Stats 25','STAT.131A':'Stats 131A','PBHLTH.142A':'Public Health 142A'}
			ans.append(manyChoiceReq(takenClasses, 'General Math', math, 'You must take One Calculus or Statistics course: Math 16A, 16B, 1A or 1B; Statistics 2, 20, 25, 131A, or PH 142AOne Calculus or Statistics course: Math 16A, 16B, 1A or 1B; Statistics 2, 20, 25, 131A, or PH 142A'))
			#ESPM 90: Introduction to the CRS Major. Students design Area of Interest statement and declare the major in this class. This course should be taken spring of sophomore year or fall of junior year.
			ans.append(basicReq(takenClasses, 'ESPM.90', 'ESPM 90', "Introduction to the CRS Major. Students design Area of Interest statement and declare the major in this class.This course should be taken spring of sophomore year or fall of junior year."))
			#Two Preparatory Courses to the Area of Interest
			ans.append({'reqName':'Preparatory Courses to the Area of Interest', 'reqCompleted':True, 'reqDescription':'You must take Two Preparatory Courses to the Area of Interest. However, there is no standard set of courses so we must assume you have done this','courseDone':[], 'courseLeft':[]})
			#ESPM 100 (Fall only) Environmental Problem Solving (4)
			ans.append(basicReq(takenClasses, 'ESPM.100', 'ESPM 100', "Environmental Problem Solving"))
			#ESPM 194A: Senior Seminar in Conservation & Resource Studies (2)
			ans.append(basicReq(takenClasses, 'ESPM.194A', 'ESPM 194A', "Senior Seminar in Conservation & Resource Studies"))
			#Eight student-designed Area of Interest Classes (Completely Unspecified)
			ans.append({'reqName':'Area of Interest', 'reqCompleted':True, 'reqDescription':'You must take Eight student-designed Area of Interest Classes. However, there is no standard set of courses so we must assume you have done this','courseDone':[], 'courseLeft':[]})
			return ans
		# Environmental Sciences
		elif(major=='ES'):
			#3 options:
			#Math 1A, Math 1B, Chem 1A and 1AL, Chem 3A and 3AL , Physics 7A, Physics 7B, [Biology 1A and 1AL,  Biology 1B OR  Biology 11 and 11L, 1 course from: IB 153, 154; ESPM 102A, 111, 113, 114, 115B, 116B ]  
			#Math 16A or Math 1A, Math 16B or Math 1B, Chem 1A and 1AL, Chem 3A and 3AL, Biology 1A and 1AL , Biology 1B, Physics 8A 
			#Math 16A or Math 1A, Math 16B or Math 1B, Chem 1A and 1AL, Chem 3A and 3AL OR Chem 1B, [Biology 1A and 1AL,  Biology 1B OR  Biology 11 and 11L, 1 course from: IB 153, 154; ESPM 102A, 111, 113, 114, 115B, 116B ], Physics 8A 
			
			#ESPM Environmental Sci Core: 1 from ESPM 2, ESPM 6, ESPM C10 (L&S C30V), or ESPM 15 (formerly ES 10)
			#ESPM Social Science Core: 1 course from ESPM C11 (L&S C30U), ESPM C12, ESPM 50AC or ESPM 60
			#Environmental Economics Environmental Economics & Policy (EEP) C1 / Economics C3
			#1 course (3-4 units) in Arts & Literature, Historical Studies, or Philosophy & Values
			#1 course (3-4 units) in Social & Behavioral Sciences or Intl Studies
			#Statistics: Statistics 131A (fall/spring), Public Health 141 (summer), Public Health 142 (fall), or ESPM 173 (spring)
			#Intro to Methods of Environmental Science ESPM 100ES [Must be taken spring of junior year]
			#Sr. Research Seminar (1st half)ESPM 175A and 175L [Must be taken fall of senior year
			#Sr. Research Seminar (2nd half)ESPM 175B and 175L [Must be taken spring of senior year]
			#Environmental Modeling ERG 102 (spring), ESPM C104/EEP C115 (fall), or ESPM C183/EEP C183 (spring)
			#Human Environment Interactions: ESPM 102D, ESPM 151, ESPM 155, ESPM 160AC/History 120AC, ESPM 161, ESPM 162, ESPM 163AC/Sociology 137AC, ESPM 166, ESPM C167/Public Health C160, ESPM 168, ESPM 169, ESPM 186; EEP C101/Econ C125, 131, EEP 140AC, EEP 153, EEP 162, C180; ERG 170, ERG 175; Geography 130, 138; Anthropology 137
			#Elective in Area of Concentration(3-4 units) See http://environmentalsciences.berkeley.edu/ES%20Electives.pdf
			#Additional ES Elective (2-4 units) May be selected from any area of concentration: http://environmentalsciences.berkeley.edu/ES%20Electives.pdf


			return ans
		# Forestry and Natural Resources
		elif(major=='FNR'):
			#ESPM Environmental Sci Core: 1 from ESPM 2, ESPM 6, ESPM C10 (L&S C30V), or ESPM 15 (formerly ES 10)
			core={'ESPM.2':'ESPM 2', 'ESPM.6':'ESPM 6', 'ESPM.C10':'ESPM C10', 'ESPM.15':'ESPM 15','L&S.C30V':'L&S C30V'}
			ans.append(manyChoiceReq(takenClasses, 'ESPM Environmental Science Core', core, 'For the ESPM Environmental Sci Core you must complete one from ESPM 2, ESPM 6, ESPM C10 (L&S C30V), or ESPM 15'))
			#ESPM Social Science Core: 1 course from ESPM C11 (L&S C30U), ESPM C12, ESPM 50AC or ESPM 60
			socialcore={'ESPM.50AC':'ESPM 50AC', 'ESPM.C12':'ESPM C12', 'ESPM.C11':'ESPM C11', 'ESPM.60':'ESPM 60','L&S.C30U':'L&S C30U'}
			ans.append(manyChoiceReq(takenClasses, 'ESPM Social Science Core', socialcore, 'For the ESPM Social Science Core you must complete one from ESPM C11 (L&S C30U), ESPM C12, ESPM 50AC or ESPM 60'))
			#Breadth
			temp=sevenBreadth(takenClasses)
			one=False
			oneTaken=[]
			oneNotTaken=[]
			two=False
			twoTaken=[]
			twoNotTaken=[]
			three=False
			threeTaken=[]
			threeNotTaken=[]
			for item in temp:
				if item['reqName'] in ['International Studies Breadth','Social and Behavioral Science Breadth'] :
					one= one or item['reqCompleted']
					oneTaken= oneTaken + item['courseDone']
					oneNotTaken= oneNotTaken + item['courseLeft']
				elif item['reqName'] is 'Physical Science Breadth':
					two= two or item['reqCompleted']
					twoTaken= twoTaken + item['courseDone']
					twoNotTaken= twoNotTaken + item['courseLeft']
				elif item['reqName'] in ['Art and Literature Breadth','Historical Studies Breadth','Philosophy and Values Breadth'] :
					three= three or item['reqCompleted']
					threeTaken= threeTaken + item['courseDone']
					threeNotTaken= threeNotTaken + item['courseLeft']
			#One course (3-4 units) in Social & Behavioral Sciences or International Studies
				if one:
					ans.append({'reqName':'Social & Behavioral Sciences or International Studies Breadth', 'reqCompleted':True, 'reqDescription':'You must take one social & behavioral sciences or international studies course. For more info see: http://http://ls-advise.berkeley.edu/requirement/7breadth.html','courseDone':oneTaken, 'courseLeft':oneNotTaken})
				else:
					ans.append({'reqName':'Social & Behavioral Sciences or International Studies Breadth', 'reqCompleted':False, 'reqDescription':'You must take one social & behavioral sciences or international studies course. For more info see: http://http://ls-advise.berkeley.edu/requirement/7breadth.html','courseDone':[], 'courseLeft':oneNotTaken})
			#One course (3-4 units) in Arts & Literature, Historical Studies, or Philosophy & Values
				if three:
					ans.append({'reqName':'Arts & Literature, Historical Studies, or Philosophy & Values Breadth', 'reqCompleted':True, 'reqDescription':'You must take one Arts & Literature, Historical Studies, or Philosophy & Values course. For more info see: http://http://ls-advise.berkeley.edu/requirement/7breadth.html','courseDone':threeTaken, 'courseLeft':threeNotTaken})
				else:
					ans.append({'reqName':'Arts & Literature, Historical Studies, or Philosophy & Values Breadth', 'reqCompleted':False, 'reqDescription':'You must take one Arts & Literature, Historical Studies, or Philosophy & Values course. For more info see: http://http://ls-advise.berkeley.edu/requirement/7breadth.html','courseDone':[], 'courseLeft':threeNotTaken})
			#Chemistry (4 units): Chem 1A/1AL; Biology (4 units): Biology 1B; Calculus (6-8 units): Math 16A-B or Math 1A-B; Statistics (4 units): Stat 2 or 20; Economics (4 units): EEP C1 (rec), Econ 1 or 2; Physical Science (4 units): EPS 50, Geog 1 or 40
				#or Physical Science: One course from Physical Sciences; Biology (3-4 units): Biology 1B or 11; Mathematics (3-4 units): Math 16A, 1A, or 32; Statistics (4 units): Stat 2, 20, Poli Sci 3 or Soc 5; Economics (3-4 units): EEP C1 (rec), Econ 1 or 2, or UGBA 10
			#ESPM 105A: Sierra Nevada Ecology (4),ESPM 105B: Forest Measurements (1), ESPM 105C: Silviculture and Utilization (3), ESPM 105D: Forest Management and Assessment (3), or ESPM C107: Biology & Geomorphology of Tropical Islands
			field={'ESPM.105A':'ESPM 105A','ESPM.105B':'ESPM.105B','ESPM.105C':'ESPM.105C','ESPM.105D':'ESPM 105D','ESPM.C107':'ESPM C107'}
			ans.append(manyChoiceReq(takenClasses, 'Field Study', field, "One field study course from the list below"))
			#ESPM 102A: Terrestrial Resource Ecology (4) F
			ans.append(basicReq(takenClasses, 'ESPM.102A', 'ESPM 102A', "The Terrestrial Resource Ecology requirement"))
			#ESPM 102B/L: Natural Resource Sampling (2/2) F
			ans.append(basicReq(takenClasses, 'ESPM.102B', 'ESPM 102B', "The Natural Resource Sampling requirement"))
			ans.append(basicReq(takenClasses, 'ESPM.102BL', 'ESPM 102BL', "The Natural Resource Sampling Lab requirement"))
			#ESPM 72: Geographic Information Systems (3) Sp
			ans.append(basicReq(takenClasses, 'ESPM.72', 'ESPM 72', "The Geographic Information Systems requirement"))
			#ESPM 102C: Resource Management (4) 
			ans.append(basicReq(takenClasses, 'ESPM.102C', 'ESPM 102C', "The Resource Management requirement"))
			#ESPM 102D: Resource & Environ Policy (4) Sp
			ans.append(basicReq(takenClasses, 'ESPM.102D', 'ESPM 102D', "The Resource & Environ Policy requirement"))
			#PROFESSIONAL FORESTRY SPECIALIZATION:ESPM 108A: Trees-Taxonomy, Growth & Structures (3) F; ESPM 134: Fire, Insects, and Diseases in Forest Ecosystems (3) Sp;ESPM 182: Forest Operations Management (3) F;ESPM 183: Forest Ecosystem Management (4) Sp;ESPM 185: Applied Forest Ecology (4) F;Plus one additional course from one of the following subject categories: PE or MM.
				#or Two courses each from both the E and the PE subject categories, plus one additional course from each of the following: MM and MP.
				#or one from each category plus two from anywhere: Ecology (E) Physical Environment (PE) Monitoring & Measurement (MM) Management (MP)
			e={'ESPM.C103':'ESPM C103','ESPM.106':'ESPM 106','ESPM.108A':'ESPM 108A','ESPM.108B':'ESPM 108B','ESPM.111':'ESPM 111','ESPM.112':'ESPM 112','ESPM.113':'ESPM 113','ESPM.114':'ESPM 114', 'ESPM.115B':'ESPM 115B','ESPM.115C':'ESPM 115C', 'ESPM.116B':'ESPM 116B','ESPM.116C':'ESPM 116C', 'ESPM.116A':'ESPM 116A', 'ESPM.134':'ESPM 134', 'ESPM.135':'ESPM 135', 'ESPM.187':'ESPM 187', 'INTEGBI.102':'INTEGBI 102', 'INTEGBI.102LF':'INTEGBI 102LF', 'INTEGBI.153':'INTEGBI 153', 'INTEGBI.154':'INTEGBI 154', 'INTEGBI.157LF':'INTEGBI 157LF'}
			pe={'ESPM.120':'ESPM 120','ESPM.121':'ESPM 121', 'ESPM.C128':'ESPM C128','ESPM.C129':'ESPM C129', 'EPS.117':'EPS 117', 'GEOG.140A':'GEOG 140A' }
			mm={'ESPM.172':'ESPM 172', 'ESPM.174':'ESPM 174', 'ANTHRO.169A':'ANTH 169A', 'ANTHRO.169B':'ANTH 169B', 'ARCH.110':'ARCH 110', 'EPS.C120':'EPS C120', 'GEOG.187':'GEOG 187', 'LDARCH.110':'LD ARCH 110','LDARCH.C188':'LD ARCH C188' }
			mp={'ESPM.155':'ESPM 155','ESPM.165':'ESPM 165','ESPM.168':'ESPM 168','ESPM.169':'ESPM 169','ESPM.181A':'ESPM 181A','ESPM.182':'ESPM 182','ESPM.183':'ESPM 183','ESPM.184':'ESPM 184','ESPM.185':'ESPM 185','ESPM.186':'ESPM 186','ESPM.188':'ESPM 188','CYPLAN.112A':'CY PLAN 112A'}
			enum=0
			penum=0
			mmnum=0
			mpnum=0
			pfsTaken=[]
			pfsNotTaken=[]
			for item in e:
				if item in takenClasses:
					enum=enum+1
					pfsTaken.append(e[item])
				else:
					pfsNotTaken.append(e[item])
			for item in pe:
				if item in takenClasses:
					penum=penum+1
					pfsTaken.append(pe[item])
				else:
					pfsNotTaken.append(pe[item])
			for item in mm:
				if item in takenClasses:
					mmnum=mmnum+1
					pfsTaken.append(mm[item])
				else:
					pfsNotTaken.append(mm[item])
			for item in mp:
				if item in takenClasses:
					mpnum=mpnum+1
					pfsTaken.append(mp[item])
				else:
					pfsNotTaken.append(mp[item])
			if (enum>=2) and (penum>=2) and (mmnum>=1) and (mpnum>=1):
				ans.append({'reqName':'PROFESSIONAL FORESTRY SPECIALIZATION', 'reqCompleted':True, 'reqDescription':'Specialization through Two courses each from both the E and the PE subject categories, plus one additional course from each of the following: MM and MP','courseDone':pfsTaken, 'courseLeft':pfsNotTaken})
			elif (enum>=1) and (penum>=1) and (mmnum>=1) and (mpnum>=1) and (enum+penum+mmnum+mpnum>=6):
				ans.append({'reqName':'PROFESSIONAL FORESTRY SPECIALIZATION', 'reqCompleted':True, 'reqDescription':'Specialization through one from each category plus two from anywhere: Ecology (E) Physical Environment (PE) Monitoring & Measurement (MM) Management (MP)','courseDone':pfsTaken, 'courseLeft':pfsNotTaken})
			elif ('ESPM.108A' in takenClasses) and ('ESPM.134' in takenClasses) and ('ESPM.180' in takenClasses) and ('ESPM.183' in takenClasses) and ('ESPM.185' in takenClasses) and ((penum>=1) or (mmnum>=1)):
				ans.append({'reqName':'PROFESSIONAL FORESTRY SPECIALIZATION', 'reqCompleted':True, 'reqDescription':'Specialization through ESPM 108A: Trees-Taxonomy, Growth & Structures (3) F; ESPM 134: Fire, Insects, and Diseases in Forest Ecosystems (3) Sp;ESPM 182: Forest Operations Management (3) F;ESPM 183: Forest Ecosystem Management (4) Sp;ESPM 185: Applied Forest Ecology (4) F;Plus one additional course from one of the following subject categories: PE or MM.','courseDone':pfsTaken, 'courseLeft':pfsNotTaken})
			else:
				ans.append({'reqName':'PROFESSIONAL FORESTRY SPECIALIZATION', 'reqCompleted':False, 'reqDescription':'Three options (ESPM 108A: Trees-Taxonomy, Growth & Structures (3) F; ESPM 134: Fire, Insects, and Diseases in Forest Ecosystems (3) Sp;ESPM 182: Forest Operations Management (3) F;ESPM 183: Forest Ecosystem Management (4) Sp;ESPM 185: Applied Forest Ecology (4) F;Plus one additional course from one of the following subject categories: PE or MM.) or (Two courses each from both the E and the PE subject categories, plus one additional course from each of the following: MM and MP.) or (one from each category plus two from anywhere: Ecology (E) Physical Environment (PE) Monitoring & Measurement (MM) Management (MP))','courseDone':pfsTaken, 'courseLeft':pfsNotTaken})
			return ans
		#Genetics and Plant Biology
		elif(major=='GPB'):
			#Math 16A/1A: Calculus I [3-4]
			ans.append(twoChoiceReq(takenClasses, 'Calculus I', 'MATH.16A', 'Math 16A', 'MATH.1A', 'Math 1A', 'You must take an Intro Calculus course either math 16A or 1A'))
			#Math 16B/1B: Calculus II [3-4]
			ans.append(twoChoiceReq(takenClasses, 'Calculus II', 'MATH.16B', 'Math 16B', 'MATH.1B', 'Math 1B', 'You must take an Intermediate Calculus course either math 16B or 1B'))
			#Stat 2, 20, 131A: Probability & Statistics [4]
			prob={'STAT.2':'Stats 2','STAT.20':'Stats 20','STAT.131A':'Stats 131A'}
			ans.append(manyChoiceReq(takenClasses, 'Probability & Statistics', prob, 'The Probability & Statistics requirement of one of Stat 2, 20, 131A'))
			#Chem 1A/L: General Chemistry [4]
			ans.append(twoReq(takenClasses,'General Chemistry', 'CHEM.1A', 'Chem 1A', 'CHEM.1AL', 'Chem 1AL', "The General Chemistry requirement"))
			#Chem 3A/L: Organic Chemistry I [5]
			ans.append(twoReq(takenClasses,'Organic Chemistry I', 'CHEM.3A', 'Chem 3A', 'CHEM.3AL', 'Chem 3AL', "The Organic Chemistry I requirement"))
			#Chem 3B/L: Organic Chemistry II [5]
			ans.append(twoReq(takenClasses,'Organic Chemistry II', 'CHEM.3B', 'Chem 3B', 'CHEM.3BL', 'Chem 3BL', "The Organic Chemistry II requirement"))
			#Bio 1A/L: General Biology [5]
			ans.append(twoReq(takenClasses,'General Biology', 'BIOLOGY.1A', 'Bio 1A', 'BIOLOGY.1AL', 'Bio 1AL', "The General Biology requirement"))
			#Bio 1B: General Biology [4]
			ans.append(basicReq(takenClasses, 'BIOLOGY.1B', 'Bio 1B', 'The General Biology requirement'))
			#15 units of coursework taken from L&S breadth list,excluding biological and physical science courses
			breadthTaken=[]
			bnum=0
			breadthNotTaken=[]
			for item in socialBehavioralScience:
				if (item in takenClasses) and (not(socialBehavioralScience[item] in breadthTaken)):
					breadthTaken.append(socialBehavioralScience[item])
					bnum=bnum+units()
				else:
					breadthNotTaken.append(socialBehavioralScience[item])
			for item in philosophyValues:
				if (item in takenClasses) and (not(philosophyValues[item] in breadthTaken)):
					breadthTaken.append(philosophyValues[item])
					bnum=bnum+units()
				else:
					breadthNotTaken.append(philosophyValues[item])
			for item in international:
				if (item in takenClasses) and (not(international[item] in breadthTaken)):
					breadthTaken.append(international[item])
					bnum=bnum+units()
				else:
					breadthNotTaken.append(international[item])
			for item in historicalStudies:
				if (item in takenClasses) and (not(historicalStudies[item] in breadthTaken)):
					breadthTaken.append(historicalStudies[item])
					bnum=bnum+units()
				else:
					breadthNotTaken.append(historicalStudies[item])
			for item in artAndLit:
				if (item in takenClasses) and (not(artAndLit[item] in breadthTaken)):
					breadthTaken.append(artAndLit[item])
					bnum=bnum+units()
				else:
					breadthNotTaken.append(artAndLit[item])
			if (bnum>=15):
				ans.append( {'reqName':'Breadth', 'reqCompleted':True, 'reqDescription':'15 units of coursework taken from L&S breadth list,excluding biological and physical science courses','courseDone':breadthTaken, 'courseLeft':breadthNotTaken})
			else:
				ans.append( {'reqName':'Breadth', 'reqCompleted':False, 'reqDescription':'15 units of coursework taken from L&S breadth list,excluding biological and physical science courses','courseDone':breadthTaken, 'courseLeft':breadthNotTaken})
			#Physics 8A: Introductory Physics [4]
			ans.append(basicReq(takenClasses, 'PHYSICS.8A', 'Physics 8A', 'The Introductory Physics requirement'))
			# PMB 101L: Experimental Plant Biology Lab [3]
			ans.append(basicReq(takenClasses, 'PLANTBI.101L', 'PMB 101L', 'The Experimental Plant Biology Lab requirement'))
			#PMB C107L: Principles of Plant Morphology and Lab [5]
			ans.append(basicReq(takenClasses, 'PLANTBI.C107L', 'PMB C107L', 'The Principles of Plant Morphology and Lab requirement'))
			#PMB 135: Physiology and Biochemistry of Plants [3]
			ans.append(basicReq(takenClasses, 'PLANTBI.135', 'PMB 135', 'The Physiology and Biochemistry of Plants requirement'))
			#PMB 150: Plant Cell Biology [3]
			ans.append(basicReq(takenClasses, 'PLANTBI.150', 'PMB 150', 'The Plant Cell Biology requirement'))
			#PMB 160: Plant Molecular Genetics [3]
			ans.append(basicReq(takenClasses, 'PLANTBI.160', 'PMB 160', 'The  requirement'))
			#Choose any five courses for a minimum of 15 units from the Plant Biology Tracks below                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
			tracks={'BIOENG.131':'BioE 131', 'BIOENG.143':'BioE 143', 'ESPM.108A':'ESPM 108A', 'ESPM.108B':'ESPM 108B', 'ESPM.131':'ESPM 131', 'ESPM.149':'ESPM 149', 'ESPM.152':'ESPM 152', 'ESPM.162':'ESPM 162', 'INTEGBI.102LF':'IB 102LF', 'INTEGBI.117':'IB 117','INTEGBI.117L':'IB 117L', 'INTEGBI.151':'IB 151', 'INTEGBI.154':'IB 154', 'INTEGBI.157':'IB 157', 'INTEGBI.160':'IB 160', 'INTEGBI.161':'IB 161', 'INTEGBI.162':'IB 162', 'INTEGBI.163':'IB 163', 'INTEGBI.168L':'IB 168L', 'INTEGBI.181':'IB 181', 'MCELLBI.102':'MCB 102', 'MCELLBI.130A':'MCB 130A', 'PLANTBI.110':'PMB 110', 'PLANTBI.110L':'PMB 110L','PLANTBI.113':'PMB 113', 'PLANTBI.120':'PMB 120','PLANTBI.120L':'PMB 120L', 'PLANTBI.122':'PMB 122', 'PLANTBI.142':'PMB 142', 'PLANTBI.165':'PMB 165', 'PLANTBI.170':'PMB 170', 'PLANTBI.180':'PMB 180', 'PLANTBI.185':'PMB 185', 'PLANTBI.C102L':'PMB C102L', 'PLANTBI.C103':'PMB C103', 'PLANTBI.C112':'PMB C112', 'PLANTBI.C112L':'PMB C112L', 'PLANTBI.C114':'PMB C114', 'PLANTBI.C116':'PMB C116', 'PLANTBI.C124':'PMB C124', 'PLANTBI.C134':'PMB C134', 'PLANTBI.C144':'PMB C144','PLANTBI.C144L':'PMB C144L',  'PLANTBI.C148':'PMB C148', 'PLANTBI.H196':'PMB H196','PLANTBI.199':'PMB 199', 'STAT.143':'Stat C143'}
			classes=0
			tracknum=0
			trackTaken=[]
			trackNotTaken=[]
			for item in tracks:
				if item in takenClasses:
					classes=classes+1
					tracknum=tracknum+units(item)
					trackTaken.append(tracks[item])
				else:
					trackNotTaken.append(tracks[item])
			if (tracknum>=15) and (classes>=5):
				ans.append( {'reqName':'Plant Biology Tracks', 'reqCompleted':True, 'reqDescription':'Choose any five courses for a minimum of 15 units from the Plant Biology Tracks below','courseDone':trackTaken, 'courseLeft':trackNotTaken})
			else:
				ans.append( {'reqName':'Plant Biology Tracks', 'reqCompleted':False, 'reqDescription':'Choose any five courses for a minimum of 15 units from the Plant Biology Tracks below','courseDone':trackTaken, 'courseLeft':trackNotTaken})
			return ans
		#Microbial Biology
		elif(major=='MB'):
			#ESPM Environmental Sci Core: 1 from ESPM 2, ESPM 6, ESPM C10 (L&S C30V), or ESPM 15 (formerly ES 10)
			#ESPM Social Science Core: 1 course from ESPM C11 (L&S C30U), ESPM C12, ESPM 50AC or ESPM 60
			#One course in General Biology with lab from the following list: Biology 1A: Molecular & Cellular Biology, Biology 1B: Plants/Ecology/Evolution, or Biology 11: Introduction to the Science of Living Organisms. NOTE: Biology 1B is recommended.
			#One course (3-4 units) in Social & Behavioral Sciences or International Studies chosen from the "Seven Breadth" listing: http://ls-advise.berkeley.edu/requirements/lsreq.html#7breadth
			#One course (3-4 units) in Physical Sciences chosen from the "Seven Breadth" listing: http://ls-advise.berkeley.edu/requirements/lsreq.html#7breadth
			#One course (3-4 units) in Arts & Literature, Historical Studies, or Philosophy & Values chosen from the "Seven Breadth" listing: http://ls-advise.berkeley.edu/requirements/lsreq.html#7breadth.
			#One Calculus or Statistics course: Math 16A, 16B, 1A or 1B; Statistics 2, 20, 25, 131A, or PH 142A.
			#ESPM 90: Introduction to the CRS Major. Students design Area of Interest statement and declare the major in this class.
			#Two Preparatory Courses to the Area of Interest (6-8 units), chosen in consultation with advisor
			#ESPM 100 (Fall only) Environmental Problem Solving (4)
			#ESPM 194A: Senior Seminar in Conservation & Resource Studies
			#Eight student-designed Area of Interest Classes (for a minimum of 24 units)

			return ans
		#Molecular Environmental Biology
		elif(major=='MEB'):
			#ESPM Environmental Science Core: 1 course from ES 10, ESPM 2, 6, C10 (L&S C30V), or 15 
			#ESPM Social Science Core: 1 course from ESPM C11 (L&S C30U), C12 (ENG C77), 50AC or 60
			#One course (3-4 units) in Arts & Literature, Historical Studies, or Philosophy & Values
			#One course (3-4 units) in Social & Behavioral Sciences or International Studies
			#Chemistry 1A (4 units) effective Summer 2011: Chem 1A (3 units) & Chem 1AL (1 unit) 
			# Chemistry 3A and lab (5 units) 
			# Chemistry 3B and lab (5 units)
			#Biology 1A and lab (5 units) and 
			#Biology 1B (4 units) NOTE: Bio 1B may be taken prior to Bio 1A. 
			#Math 16A (or 1A)  
			#Math 16B (or 1B) Math 16B/1B may be replaced by Statistics 2, 20, 25, PH 142A or Stat 131A.
			#Physics 8A: 4 units
			#Biological Core: select one course from each of the seven categories below
			"""here"""


			return ans
		#Molecular Toxicology
		elif(major=='MT'):
			#14 additional units of course work in American Cultures, Arts & Literature, Historical Studies, International Studies, Philosophy & Values, Social & Behavioral Sciences, or Foreign Language
			humanity=0
			for item in takenClasses:
				if 'AC' in item:
					humanity+=units(item)
			humanityCourses=artAndLit
			for item in historicalStudies:
				if item not in humanityCourses:
					humanityCourses.append(item)
			for item in international:
				if item not in humanityCourses:
					humanityCourses.append(item)
			for item in philosophyValues:
				if item not in humanityCourses:
					humanityCourses.append(item)
			for item in physicalScience:
				if item not in humanityCourses:
					humanityCourses.append(item)
			for item in socialBehavioralScience:
				if item not in humanityCourses:
					humanityCourses.append(item)
			for item in humanityCourses:
				if ('AC' not in item) and (item in takenClasses):
					humanity+=units(item)
			if(humanity>=14):
				ans.append({'reqName':'Humanities Courses', 'reqCompleted':True, 'reqDescription':'14 additional units of course work in American Cultures, Arts & Literature, Historical Studies, International Studies, Philosophy & Values, Social & Behavioral Sciences, or Foreign Language','courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Humanities Courses', 'reqCompleted':False, 'reqDescription':'14 additional units of course work in American Cultures, Arts & Literature, Historical Studies, International Studies, Philosophy & Values, Social & Behavioral Sciences, or Foreign Language','courseDone':[], 'courseLeft':[]})
			#Math 16A and Math 16B and Stats 2 (Intro to Statistics)(10) OR  Math 1A and Stats 2 (8) OR Math 10A and Math 10B (8)
			if (('MATH.16A'in takenClasses)and ('MATH.16B'in takenClasses)and ('STAT.2'in takenClasses)) or (('MATH.1A'in takenClasses)and ('STAT.2'in takenClasses)) or (('MATH.10A'in takenClasses)and ('MATH.10B'in takenClasses)):
				ans.append({'reqName':'Math Courses', 'reqCompleted':True, 'reqDescription':'Math 16A and Math 16B and Stats 2 (Intro to Statistics)(10) OR  Math 1A and Stats 2 (8) OR Math 10A and Math 10B (8)','courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Math Courses', 'reqCompleted':False, 'reqDescription':'Math 16A and Math 16B and Stats 2 (Intro to Statistics)(10) OR  Math 1A and Stats 2 (8) OR Math 10A and Math 10B (8)','courseDone':[], 'courseLeft':[]})
			#Chemistry 1A (4 units) effective Summer 2011: Chem 1A (3 units) & Chem 1AL (1 unit) 
			ans.append(twoReq(takenClasses,'Chemistry', 'CHEM.1A', 'Chem 1A','CHEM.1AL', 'Chem 1AL', "The freshman year Chemistry requirement of Chem 1A and 1AL"))
			# Chemistry 3A and lab (5 units)
			ans.append(twoReq(takenClasses,'Chemistry', 'CHEM.3A', 'Chem 3A','CHEM.3AL', 'Chem 3AL', "The freshman year Chemistry requirement of Chem 3A and 3AL"))
			# Chemistry 3B and lab (5 units)
			ans.append(twoReq(takenClasses,'Chemistry', 'CHEM.3B', 'Chem 3B','CHEM.3BL', 'Chem 3BL', "The freshman year Chemistry requirement of Chem 3B and 3BL"))
			#Physics 8A: 4 units
			ans.append(basicReq(takenClasses,'PHYSICS.8A', 'Physics 8A', 'Requirement of PHYSICS 8A'))
			#NST 11, Introduction to Toxicology (3)(SP)
			ans.append(basicReq(takenClasses,'NUSCTX.11', 'NutriSci 11', 'Requirement of NutriSci 11'))
			#MCB 32, Human Physiology and  MCB 32L, Human Physiology Lab (2)(F) (IB 132/132L is also acceptable)
			temp1=twoReq(takenClasses,'', 'MCELLBI.32', 'MCB 32','MCELLBI.32L', 'MCB 32L','')
			temp2=twoReq(takenClasses,'', 'INTEGBI.132', 'IB 132','INTEGBI.132L', 'IB 132L','')
			if (temp1['reqCompleted']):
				ans.append({'reqName':'Human Physiology', 'reqCompleted':True, 'reqDescription':'Requirement of MCB 32, Human Physiology and MCB 32L, Human Physiology Lab','courseDone':['MCB 32','MCB 32L'], 'courseLeft':[]})
			elif (temp1['reqCompleted']):
				ans.append({'reqName':'Human Physiology', 'reqCompleted':True, 'reqDescription':'Requirement of IB 132/132L','courseDone':['IB 132','IB 132L'], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Human Physiology', 'reqCompleted':False, 'reqDescription':'Requirement of MCB 32, Human Physiology and  MCB 32L, Human Physiology Lab (2)(F) (IB 132/132L is also acceptable)','courseDone':temp1['courseDone']+temp2['courseDone'], 'courseLeft':temp1['courseLeft']+temp2['courseLeft']})
			#Bio 1A, General Biology and Bio 1AL, General Biology Lab (2)(F,SP)
			ans.append( twoReq(takenClasses,'General Biology', 'BIOLOGY.1A', 'Bio 1A', 'BIOLOGY.1AL', 'Bio 1AL', "The sophomore year biology requirement of both Bio 1A and 1AL"))
			#MCB 102 Biochemistry &Molecular Biology (4)(F,SP)
			ans.append(basicReq(takenClasses,'MCELLBI.102', 'MCB 102', 'Requirement of MCB 102 Biochemistry & Molecular Biology'))
			#MCB 104 Genetics (4)(F,SP) or IB 141 (3, offered Summer Session only)
			ans.append(twoChoiceReq(takenClasses,'Genetics', 'MCELLBI.104', 'MCB 104', 'INTEGBI.141', 'IB 141', 'Requirement of MCB 104 Genetics (4)(F,SP) or IB 141 (3, offered Summer Session only)'))
			#PMB/MCB C112 General Microbiology (4) (F) OR PH 162A Public Health Microbiology (3) (F)
			micro={'PLANTBI.C112':'PMB C112','MCELLBI.C112':'MCB C112','PBHLTH.162A':'Public Health 162A'}
			ans.append(manyChoiceReq(takenClasses, 'Microbiology', micro, "Requirement of PMB/MCB C112 General Microbiology (4) (F) OR PH 162A Public Health Microbiology (3) (F)"))
			#Microbiology Lab PMB/MCB C112L(F,SP) (2) OR PH 162L (1) (F)*
			microl={'PLANTBI.C112L':'PMB C112L','MCELLBI.C112L':'MCB C112L','PBHLTH.162L':'Public Health 162L'}
			ans.append(manyChoiceReq(takenClasses, 'Microbiology Lab', microl, "Requirement of PMB/MCB C112L General Microbiology Lab(F,SP) (2) OR PH 162L (1)"))
			#NST 110 Toxicology (4) (F)
			ans.append(basicReq(takenClasses,'NUSCTX.110', 'NutriSci 110', 'Requirement of NutriSci 110 Toxicology'))
			#NST 121 Computational Toxicology (3) (SP)
			ans.append(basicReq(takenClasses,'NUSCTX.121', 'NutriSci 121', 'Requirement of NutriSci 121 Computational Toxicology'))
			#NST 171 Nutrition and Toxicology Laboratory (4) (F)
			ans.append(basicReq(takenClasses,'NUSCTX.171', 'NutriSci 171', 'Requirement of NutriSci 171 Nutrition and Toxicology Laboratory'))
			#NST 193 Introduction to Research in Toxicology (1)(SP)
			ans.append(basicReq(takenClasses,'NUSCTX.193', 'NutriSci 193', 'Requirement of NutriSci 193 Introduction to Research in Toxicology'))
			#36 total units including above requirements:Approved Electives List:Civ Eng 114 Environmental Microbiology (3), Civ Eng 115 Water Chemistry (3), 
			#ESPM 100 Environmental Problem Solving (4), ESPM 119 Chemical Ecology (2), ESPM 126 Environmental Soil Chemistry (3), ESPM 162 Bioethics (4), 
			#ESPM C180 Air Pollution (3), IB 117 Medical Ethnobotany (2), IB 131 Human Anatomy (3),, IB 152 Environmental Toxicology (4), 
			#NST 103 Nutrient Function and Metabolism (3)(F), NST C114/ESPM C148 Pesticide Chemistry & Toxicology (3)(SP), NST C115 Principles of Drug Action (2)(SP), 
			#NST 160 Metabolic Bases of Human Health & Diseases (4)(SP), NST H196 Honors Research (4), NST 199 Independent Study Research (1-4), 
			#PH 150A Introduction to Epidemiology & Human Disease (3), PH 150B Introduction to Environmental Health (3), PH 170B Toxicology (3), 
			#UGIS 192C Research Biological Sciences (1-4), Any other Approved NS-PM Elective Courses, Other IB, MCB, and PMB lecture or lab courses also accepted
			upperdiv=['MCELLBI.104','MCELLBI.102','PLANTBI.C112','MCELLBI.C112','PBHLTH.162A','PLANTBI.C112L','MCELLBI.C112L','PBHLTH.162L','NUSCTX.110','NUSCTX.121','NUSCTX.171','NUSCTX.193']
			upperdivunits=0
			for item in upperdiv:
				if (item in takenClasses):
					upperdivunits+=units(item)
			approvedElec={'CIVENG.114':'CivEng 114','CIVENG.115':'CivEng 115','ESPM.100':'ESPM 100','ESPM.119':'ESPM 119','ESPM.126':'ESPM 126','ESPM.C148':'ESPM C148','ESPM.162':'ESPM 162','ESPM.C180':'ESPM C180',
				'INTEGBI.117':'IB 117','INTEGBI.131':'IB 131','INTEGBI.152':'IB 152','NUSCTX.103':'NutriSci 103','NUSCTX.C114':'NutriSci C114','NUSCTX.C115':'NutriSci C115','NUSCTX.160':'NutriSci 160','NUSCTX.H196':'NutriSci H196','NUSCTX.199':'NutriSci 199',
				'PBHLTH.150A':'PublicHealth 150A','PBHLTH.150B':'PublicHealth 150B','PBHLTH.170B':'PublicHealth 170B','UGIS.192C':'UGIS 192C'}
			approvedElecUnits=0
			approvedElecTaken=[]
			approvedElecLeft=[]
			for item in approvedElec:
				if (item in takenClasses):
					approvedElecUnits+=units(item)
					approvedElecTaken.append(approvedElec[item])
				else:
					approvedElecLeft.append(approvedElec[item])
			if(approvedElecUnits+upperdivunits>=36):
				ans.append({'reqName':'Approved Elective', 'reqCompleted':True, 'reqDescription':'36 total units including above requirements and classes from the Approved Electives List as well as  Any other Approved NS-PM Elective Courses, Other IB, MCB, and PMB lecture or lab courses also accepted','courseDone':approvedElecTaken, 'courseLeft':approvedElecLeft})
			else:
				ans.append({'reqName':'Approved Elective', 'reqCompleted':False, 'reqDescription':'36 total units including above requirements and classes from the Approved Electives List as well as  Any other Approved NS-PM Elective Courses, Other IB, MCB, and PMB lecture or lab courses also accepted','courseDone':approvedElecTaken, 'courseLeft':approvedElecLeft})
			return ans
		#Nutritional Science: Physiology & Metabolism
		elif(major=='NSPM'):
			#14 additional units of course work in American Cultures, Arts & Literature, Historical Studies, International Studies, Philosophy & Values, Social & Behavioral Sciences, or Foreign Language
			humanity=0
			for item in takenClasses:
				if 'AC' in item:
					humanity+=units(item)
			humanityCourses=artAndLit
			for item in historicalStudies:
				if item not in humanityCourses:
					humanityCourses.append(item)
			for item in international:
				if item not in humanityCourses:
					humanityCourses.append(item)
			for item in philosophyValues:
				if item not in humanityCourses:
					humanityCourses.append(item)
			for item in physicalScience:
				if item not in humanityCourses:
					humanityCourses.append(item)
			for item in socialBehavioralScience:
				if item not in humanityCourses:
					humanityCourses.append(item)
			for item in humanityCourses:
				if ('AC' not in item) and (item in takenClasses):
					humanity+=units(item)
			if(humanity>=14):
				ans.append({'reqName':'Humanities Courses', 'reqCompleted':True, 'reqDescription':'14 additional units of course work in American Cultures, Arts & Literature, Historical Studies, International Studies, Philosophy & Values, Social & Behavioral Sciences, or Foreign Language','courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Humanities Courses', 'reqCompleted':False, 'reqDescription':'14 additional units of course work in American Cultures, Arts & Literature, Historical Studies, International Studies, Philosophy & Values, Social & Behavioral Sciences, or Foreign Language','courseDone':[], 'courseLeft':[]})
			#Math 16A and Math 16B and Stats 2 (Intro to Statistics)(10) OR  Math 1A and Stats 2 (8) OR Math 10A and Math 10B (8)
			if (('MATH.16A'in takenClasses)and ('MATH.16B'in takenClasses)and ('STAT.2'in takenClasses)) or (('MATH.1A'in takenClasses)and ('STAT.2'in takenClasses)) or (('MATH.10A'in takenClasses)and ('MATH.10B'in takenClasses)):
				ans.append({'reqName':'Math Courses', 'reqCompleted':True, 'reqDescription':'Math 16A and Math 16B and Stats 2 (Intro to Statistics)(10) OR  Math 1A and Stats 2 (8) OR Math 10A and Math 10B (8)','courseDone':[], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Math Courses', 'reqCompleted':False, 'reqDescription':'Math 16A and Math 16B and Stats 2 (Intro to Statistics)(10) OR  Math 1A and Stats 2 (8) OR Math 10A and Math 10B (8)','courseDone':[], 'courseLeft':[]})
			#Chemistry 1A (4 units) effective Summer 2011: Chem 1A (3 units) & Chem 1AL (1 unit) 
			ans.append(twoReq(takenClasses,'Chemistry', 'CHEM.1A', 'Chem 1A','CHEM.1AL', 'Chem 1AL', "The freshman year Chemistry requirement of Chem 1A and 1AL"))
			# Chemistry 3A and lab (5 units)
			ans.append(twoReq(takenClasses,'Chemistry', 'CHEM.3A', 'Chem 3A','CHEM.3AL', 'Chem 3AL', "The freshman year Chemistry requirement of Chem 3A and 3AL"))
			# Chemistry 3B and lab (5 units)
			ans.append(twoReq(takenClasses,'Chemistry', 'CHEM.3B', 'Chem 3B','CHEM.3BL', 'Chem 3BL', "The freshman year Chemistry requirement of Chem 3B and 3BL"))
			#Physics 8A: 4 units
			ans.append(basicReq(takenClasses,'PHYSICS.8A', 'Physics 8A', 'Requirement of PHYSICS 8A'))
			#NST 10, Intro to Human Nutrition (3)(F,SP)
			ans.append(basicReq(takenClasses,'NUSCTX.10', 'NutriSci 10', 'Requirement of NutriSci 10'))
			#MCB 32, Human Physiology and  MCB 32L, Human Physiology Lab (2)(F) (IB 132/132L is also acceptable)
			temp1=twoReq(takenClasses,'', 'MCELLBI.32', 'MCB 32','MCELLBI.32L', 'MCB 32L','')
			temp2=twoReq(takenClasses,'', 'INTEGBI.132', 'IB 132','INTEGBI.132L', 'IB 132L','')
			if (temp1['reqCompleted']):
				ans.append({'reqName':'Human Physiology', 'reqCompleted':True, 'reqDescription':'Requirement of MCB 32, Human Physiology and MCB 32L, Human Physiology Lab','courseDone':['MCB 32','MCB 32L'], 'courseLeft':[]})
			elif (temp1['reqCompleted']):
				ans.append({'reqName':'Human Physiology', 'reqCompleted':True, 'reqDescription':'Requirement of IB 132/132L','courseDone':['IB 132','IB 132L'], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Human Physiology', 'reqCompleted':False, 'reqDescription':'Requirement of MCB 32, Human Physiology and  MCB 32L, Human Physiology Lab (2)(F) (IB 132/132L is also acceptable)','courseDone':temp1['courseDone']+temp2['courseDone'], 'courseLeft':temp1['courseLeft']+temp2['courseLeft']})
			#Bio 1A, General Biology (3)(F,SP)  Bio 1AL, General Biology Lab (2)(F,SP)
			ans.append( twoReq(takenClasses,'General Biology', 'BIOLOGY.1A', 'Bio 1A', 'BIOLOGY.1AL', 'Bio 1AL', "The sophomore year biology requirement of both Bio 1A and 1AL"))
			#MCB 102 Principles of Biochemistry & Molecular Biology (4) (F,SP)
			ans.append(basicReq(takenClasses,'MCELLBI.102', 'MCB 102', 'Requirement of MCB 102 Principles of Biochemistry & Molecular Biology'))
			#NST 103 Nutrient Function & Metabolism (3)(F)
			ans.append(basicReq(takenClasses,'NUSCTX.103', 'NutriSci 103', 'Requirement of NutriSci 103 Nutrient Function & Metabolism'))
			#NST 160 Metabolic Bases of Human Health and Diseases (4)(SP)
			ans.append(basicReq(takenClasses,'NUSCTX.160', 'NutriSci 160', 'Requirement of NutriSci 160 Metabolic Bases of Human Health and Diseases'))
			#NST 170 Experimental Nutrition Laboratory (4)(SP)
			ans.append(basicReq(takenClasses,'NUSCTX.170', 'NutriSci 170', 'Requirement of NutriSci 170 Experimental Nutrition Laboratory'))
			#NST 190 Introduction to Research in Nutritional Science (1)(F,SP)
			ans.append(basicReq(takenClasses,'NUSCTX.190', 'NutriSci 190', 'Requirement of NutriSci 190 Introduction to Research in Nutritional Science'))
			#Approved Electives List (20 Units Required):
			elec={'NUSCTX.104':'NST 104', 'NUSCTX.108A':'NST 108A', 'NUSCTX.110':'NST 110' , 'NUSCTX.C114':'NST C114', 'NUSCTX.115':'NST 115', 'NUSCTX.161A':'NST 161A', 'NUSCTX.161B':'NST 161B' , 'NUSCTX.166':'NST 166', 'NUSCTX.193':'NST 193', 'NUSCTX.H196':'NST H196' , 'NUSCTX.199':'NST 199' , 'PBHLTH.C103':'PMB C103', 'PBHLTH.C112':'PMB C112' , 'PBHLTH.162A':'PMB 162A' , 'PBHLTH.C114':'PMB C114' , 'INTEGBI.117':'IB 117', 'INTEGBI.123':'IB 123', 'INTEGBI.128':'IB 128', 'INTEGBI.131':'IB 131', 'INTEGBI.140':'IB 140' , 'MCELLBI.104':'MCB 104' , 'MCELLBI.130A':'MCB 130A' , 'MCELLBI.132':'MCB 132', 'MCELLBI.135A':'MCB 135A','MCELLBI.135B':'MCB 135B','MCELLBI.135C':'MCB 135C','MCELLBI.135D':'MCB 135D','MCELLBI.135E':'MCB 135E','MCELLBI.135F':'MCB 135F','MCELLBI.135G':'MCB 135G','MCELLBI.135H':'MCB 135H','MCELLBI.135I':'MCB 135I','MCELLBI.135J':'MCB 135J','MCELLBI.135K':'MCB 135K','MCELLBI.135L':'MCB 135L','MCELLBI.135M':'MCB 135M','MCELLBI.135N':'MCB 135N','MCELLBI.135O':'MCB 135O','MCELLBI.135P':'MCB 135P','MCELLBI.135Q':'MCB 135Q','MCELLBI.135R':'MCB 135R','MCELLBI.135S':'MCB 135S','MCELLBI.135T':'MCB 135T','MCELLBI.135U':'MCB 135U','MCELLBI.135V':'MCB 135V','PBHLTH.170B':'PH 170B','UGIS.192C':'UGIS 192C'}
			#up to 10 units of Dietetic courses: NST 104, NST 108A, NST 161A, NST 161B, and NST 166.
			dietic={'NUSCTX.104':'NST 104', 'NUSCTX.108A':'NST 108A', 'NUSCTX.161A':'NST 161A', 'NUSCTX.161B':'NST 161B', 'NUSCTX.166':'NST 166'}
			dunit=0
			eunit=0
			aeTaken=[]
			aeLeft=[]
			for item in dietic:
				if item in takenClasses:
					dunit+=units(item)
			for item in elec:
				if item in takenClasses:
					eunit+=units(item)
					aeTaken.append(elec[item])
				else:
					aeLeft.append(elec[item])
			if (dunit>=10):
				eunit=eunit-dunit+10
			if eunit>=20:
				ans.append({'reqName':'Electives', 'reqCompleted':True, 'reqDescription':'Approved Electives List (20 Units Required) and only up to 10 units of Dietetic courses','courseDone':aeTaken, 'courseLeft':aeLeft})
			else:
				ans.append({'reqName':'Electives', 'reqCompleted':False, 'reqDescription':'Approved Electives List (20 Units Required) and only up to 10 units of Dietetic courses','courseDone':aeTaken, 'courseLeft':aeLeft})
			return ans
		#Nutritional Science: Dietetics
		elif(major=='NSD'):
			#Econ 1, or 2, or 3
			#Anthro 3, Psych 1 or 2, Soc 3
			#5 additional units of humanities and social science course work
			#Math 16A and .Stats 2 or Math 1A and .Stats 2  or .Math 10A and .Math 10B 
			#Chem 1A, General Chemistry and Chem 1AL General Chemistry 
			#Chem 3A, Organic Chemistry and Chem 3AL, Organic Chemistry Lab 
			#Chem 3B, Organic Chemistry (3) . Chem 3BL, Organic Chemistry Lab
			#NST 10, Intro to Human Nutrition
			#MCB 32, Human Physiology and MCB 32L, Human Physiology Lab (IB 132/132L is also acceptable)
			#Bio 1A, General Biology and Bio 1AL, General Biology Lab
			#MCB 102, Principles of Biochem. & Molecular Biology
			#NST 161A, Medical Nutrition Therapy 
			#NST 103, Nutrient Function & Metabolism
			#NST 161B, Applica. Medical Nutrition Therapy 
			#NST 104, Human Food Practices 
			#NST 166, Nutrition in the Community 
			#NST 108A, Intro & App of Food Science 
			#NST 192, Junior Seminar in Dietetics 
			#NST 108B, App of Food Science Lab 
			#NST 194, Senior Seminar in Dietetics 
			#NST 135, Food Systems Org & Management
			#PH 162A, Public Health 
			#NST 145, Nutrition Education & Counseling 
			#UGBA 102A, Intro to Financial Accounting
			#NST 160, Metabolic Bases of Human Health and Diseases 
			#UGBA 105, Intro to Organizational Behavior  

			return ans
		#Society and Environment
		elif(major=='SE'):
			#ESPM Environmental Science Core: 1 course from ES 10, ESPM 2, 6, C10 (L&S C30V), or 15 (cannot overlap with breadth)
			#ESPM Social Science Core: 1 course from ESPM C11 (L&S C30U), C12 (ENG C77), 50AC or 60 (cannot overlap with breadth)
			#Social & Behavioral Sciences (3-4 units)
			#International Studies (3-4 units)
			#Physical Sciences (3-4 units)
			#Arts & Literature, Historical Studies, or Philosophy & Values (3-4 units)
			#Biological Science (3-4 units)
			#One Math or Statistics course: Math 1A, 10A, 16A, Statistics 2, 20, PH 140 or 142A.
			#One Economics course: EEP 1 (Econ C3), Econ 1 or Econ 2 (The Econ course may count as the Soc & Behav. req.)
			#One course in Environmental or Political Economics: POL SCI 126A or 139B; GEOG C110, C112, or 156; DEV STD C100; ECON C125; ENVECON 100, C101, 131, 140AC, 153, 161, or C180; ERG C180; ISF C101; PEIS 100 or 101; GPP 115/IAS 115; PUB POL C103
			#Capstone Presentation. ESPM 194B (1-2) Research or poster presentation (Final semester of the senior year)
			#Seven courses from the Area of Concentration requirement
			
			return ans
		#Environmental Economics and Policy
		elif(major=='EEP'):
			#Seven-Course Breadth of Knowledge (one course from each of the following categories)
			#Principles of Micro-Economics:EEP 1, ECON 1, ECON 2 or ECON 3
			#Two Semesters of Calculus: MATH 1A & 1B or MATH 16A & 16B
			#Statistics: STAT 20, 21, or 25
			#Intermediate Micro-Economics: EEP 100 (or ECON 100A or 101A)
			#Environmental or Natural Resource Economics: EEP C101 or EEP C102
			#Quantitative Methods: EEP C115 or EEP C118
			#At least 5 courses to form an Area of Concentration: 3 of these must be upper-division EEP courses
			#A total of at least 5 upper division EEP courses (not 195-199)
			
			
			return ans
		#Should not occur but in the case that the major given does not match
		else:
			raise MyError(major+"is not a valid major at UC Berkeley College of Engineering")
	# College of Letters and Sciences
	elif (college=='LettersAndSciences'):
		# College Requirements
		if (major=='COMPSCI'):
			
			return ans
		else:
			ans.append({'reqName':'I am sorry this major is not yet supported', 'reqCompleted':False, 'reqDescription':'','courseDone':[], 'courseLeft':[]})
			return ans
	# Haas School of Business
	elif (college=='Haas'):
		#no need for college requirements because there is only one major
		# Undergraduate Business Administration
		if (major=='UGBA'):
			#7 Breadth Requirements
			ans=ans+sevenBreadth(takenClasses)
			#100 Business Communications 2
			ans.append(basicReq(takenClasses, 'UGBA.100', 'UGBA 100', 'Requirement to take UGBA 100, Business Communications'))
			#101A Microeconomic Analysis for Business Decisions 3 (ECON 100A;ECON 101A;EEP 100;IAS 106)
			micro={'UGBA.101A':'UGBA 101A','ECON.100A':'Econ 100A','ECON.101A':'Econ 101A','ENVECON.100':'EEP 100','IAS.106':'IAS 106'}
			ans.append(manyChoiceReq(takenClasses, 'Microeconomic Analysis', micro, 'Requirement of UGBA 101A,ECON 100A,ECON 101A,EEP 100,or IAS 106'))
			#101B Macroeconomic Analysis for Business Decisions 3 (ECON 100B;ECON 101B;IAS 107)
			macro={'UGBA.101B':'UGBA 101B','ECON.100B':'Econ 100B','ECON.100B':'Econ 101B','IAS.107':'IAS 107'}
			ans.append(manyChoiceReq(takenClasses, 'Macroeconomic Analysis', macro, 'Requirement of UGBA 101B,ECON 100B,ECON 101B,IAS 107'))
			#102A Introduction to Financial Accounting 3
			ans.append(basicReq(takenClasses, 'UGBA.102A', 'UGBA 102A', 'Requirement to take UGBA 102A,Introduction to Financial Accounting'))
			#102B Introduction to Managerial Accounting 3
			ans.append(basicReq(takenClasses, 'UGBA.102B', 'UGBA 102B', 'Requirement to take UGBA 102B, Introduction to Managerial Accounting'))
			#103 Introduction to Finance 4
			ans.append(basicReq(takenClasses, 'UGBA.103', 'UGBA 103', 'Requirement to take UGBA 103, Introduction to Finance'))
			#104 Analytic Decision Modeling Using Spreadsheets 3
			ans.append(basicReq(takenClasses, 'UGBA.104', 'UGBA 104', 'Requirement to take UGBA 104, Analytic Decision Modeling Using Spreadsheets'))
			#105 Introduction to Organizational Behavior 3
			ans.append(basicReq(takenClasses, 'UGBA.105', 'UGBA 105', 'Requirement to take UGBA 105, Introduction to Organizational Behavior'))
			#106 Marketing 3
			ans.append(basicReq(takenClasses, 'UGBA.106', 'UGBA 106', 'Requirement to take UGBA 106, Marketing'))
			#107 The Social, Political, and Ethical Environment of Business 3
			ans.append(basicReq(takenClasses, 'UGBA.107', 'UGBA 107', 'Requirement to take UGBA 107, The Social, Political, and Ethical Environment of Business'))
			#38 Upper-Division Business Units* Includes previous classes
			elec={'UGBA.100':'UGBA 100','UGBA.101A':'UGBA 101A','UGBA.101B':'UGBA 101B','UGBA.102A':'UGBA 102A','UGBA.102B':'UGBA 102B','UGBA.103':'UGBA 103','UGBA.104':'UGBA 104','UGBA.105':'UGBA 105',
				'UGBA.106':'UGBA 106','UGBA.107':'UGBA 107','UGBA.113':'UGBA 113','UGBA.115':'UGBA 115','UGBA.117':'UGBA 117','UGBA.118':'UGBA 118','UGBA.119':'UGBA 119','UGBA.120A':'UGBA 120A',
				'UGBA.120B':'UGBA 120B','UGBA.121':'UGBA 121','UGBA.122':'UGBA 122','UGBA.126':'UGBA 126','UGBA.127':'UGBA 127','UGBA.128':'UGBA 128','UGBA.131':'UGBA 131','UGBA.132':'UGBA 132',
				'UGBA.133':'UGBA 133','UGBA.136F':'UGBA 136F','UGBA.137':'UGBA 137','UGBA.141':'UGBA 141','UGBA.143':'UGBA 143','UGBA.147':'UGBA 147','UGBA.151':'UGBA 151','UGBA.152':'UGBA 152','UGBA.155':'UGBA 155','UGBA.156AC':'UGBA 156AC',
				'UGBA.157':'UGBA 157','UGBA.160':'UGBA 160','UGBA.161':'UGBA 161','UGBA.162':'UGBA 162','UGBA.165':'UGBA 165','UGBA.167':'UGBA 167','UGBA.170':'UGBA 170','UGBA.C172':'UGBA C172','UGBA.175':'UGBA 175','UGBA.177':'UGBA 177',
				'UGBA.178':'UGBA 178','UGBA.180':'UGBA 180','UGBA.183':'UGBA 183','UGBA.184':'UGBA 184','UGBA.187':'UGBA 187','UGBA.190T':'UGBA 190T','UGBA.191C':'UGBA 191C','UGBA.192A':'UGBA 192A','UGBA.192N':'UGBA 192N','UGBA.192P':'UGBA 192P',
				'UGBA.192T':'UGBA 192T','UGBA.195A':'UGBA 195A','UGBA.195P':'UGBA 195P','UGBA.195S':'UGBA 195S','UGBA.195T':'UGBA 195T','UGBA.196':'UGBA 196','UGBA.198':'UGBA 198','UGBA.199':'UGBA 199'}
			elecUnits=0
			elecDone=[]
			elecNotDone=[]
			for item in elec:
				if item in takenClasses:
					elecUnits+=units(item)
					elecDone.append(elec[item])
				else:
					elecNotDone.append(elec[item])
			if (elecUnits>=38):
				ans.append({'reqName':'Upper Division Business', 'reqCompleted':True, 'reqDescription':'Required 38 upper division business units','courseDone':elecDone, 'courseLeft':elecNotDone})
			else:
				ans.append({'reqName':'Upper Division Business', 'reqCompleted':False, 'reqDescription':'Required 38 upper division business units','courseDone':elecDone, 'courseLeft':elecNotDone})
			return ans
		#Should not occur but in the case that the major given does not match
		else:
			raise MyError(major+"is not a valid major at UC Berkeley Haas School of Business")
	# College of Environmental Design
	elif (college=='EnvironmentalDesign'):
		# College Requirements
		#R1A and R1B
		OneA=False
		OneB=False
		for item in takenClasses:
			if 'R1A' in item:
				OneA=True
			if 'R1B' in item:
				OneB=True
		if (OneA and OneB):
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':True, 'reqDescription':"Take at least one course labeled R1A and R1B",'courseDone':[], 'courseLeft':[]})
		elif (OneA):
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled R1A and R1B. You have completed R1A",'courseDone':[], 'courseLeft':[]})
		elif (OneB):
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled R1A and R1B. You have completed R1B",'courseDone':[], 'courseLeft':[]})
		else:
			ans.append({'reqName':'Reading and Composition', 'reqCompleted':False, 'reqDescription':"Take at least one course labeled R1A and R1B",'courseDone':[], 'courseLeft':[]})
		#Seven Course Breadth Requirement
		ans=ans+sevenBreadth(takenClasses)
		#Architecture
		if(major=='ARCH'):
			#ENV DES 1 People and Environmental Design
			ans.append(basicReq(takenClasses, 'ENVDES.1', 'EnvDesign 1', 'Requirement of ENV DES 1 People and Environmental Design'))
			#ENV DES 4A Design and Activism, 4B Global Cities, 4C Future Ecologies (complete 2 of 3)
			envFour={'ENVDES.4A':'EnvDesign 4A','ENVDES.4B':'EnvDesign 4B','ENVDES.4C':'EnvDesign 4C'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'Environmental Design 4', envFour, 'Requirement of 2 of 4A Design and Activism, 4B Global Cities, 4C Future Ecologies', 2))
			#Upper Division College of Environmental Design Courses Outside of Architecture (3 courses total): courses in Environmental Design, Visual Studies, Landscape Architecture, and City and Regional Planning
			upperDone=[]
			upperClasses=0
			for item in takenClasses:
				if((re.search(r'ENVDES.1\d\d',item)) or (re.search(r'VISSTD.1\d\d',item)) or (re.search(r'LDARCH.1\d\d',item)) or (re.search(r'CYPLAN.1\d\d',item))):
					upperDone.append(item.replace('.',' '))
					upperClasses+=1
			if upperClasses>=3:
				ans.append({'reqName':'College of Environmental Design Courses', 'reqCompleted':True, 'reqDescription':"Take at least 3 upper division courses in the College of Environmental Design but not Architecture(Environmental Design, Visual Studies, Landscape Architecture, and City and Regional Planning)",'courseDone':upperDone, 'courseLeft':['Any Environmental Design','Any Visual Studies','Any Landscape Architecture','Any City and Regional Planning']})
			else:
				ans.append({'reqName':'College of Environmental Design Courses', 'reqCompleted':False, 'reqDescription':"Take at least 3 upper division courses in the College of Environmental Design but not Architecture(Environmental Design, Visual Studies, Landscape Architecture, and City and Regional Planning)",'courseDone':upperDone, 'courseLeft':['Any Environmental Design','Any Visual Studies','Any Landscape Architecture','Any City and Regional Planning']})
			#ENV DES 11A Introduction to Visual Representation and Drawing
			ans.append(basicReq(takenClasses, 'ENVDES.11A', 'EnvDesign 11A', 'Requirement of ENV DES 11A Introduction to Visual Representation and Drawing'))
			#ENV DES 11B Introduction to Design
			ans.append(basicReq(takenClasses, 'ENVDES.11B', 'EnvDesign 11B', 'Requirement of ENV DES 11B, Introduction to Design'))
			#MATH 16A or Math 1A
			ans.append(twoChoiceReq(takenClasses, 'Basic Calculus', 'MATH.16A', 'Math 16A', 'MATH.1A', 'Math.1A', 'Requirement of MATH 16A or Math 1A'))
			#PHYSICS 8A or 7A
			ans.append(twoChoiceReq(takenClasses, 'Basic Physics', 'PHYSICS.7A', 'Physics 7A', 'PHYSICS.8A', 'Physics 8A', 'Requirement of PHYSICS 8A or 7A'))
			#ARCH 100A Fundamentals of Architectural Design
			ans.append(basicReq(takenClasses, 'ARCH.100A', 'Architecture 100A', 'Requirement of ARCH 100A, Fundamentals of Architectural Design'))
			#ARCH 100B Fundamentals of Architectural Design
			ans.append(basicReq(takenClasses, 'ARCH.100B', 'Architecture 100B', 'Requirement of ARCH 100B, Fundamentals of Architectural Design'))
			#ARCH 170A An Historical Survey of Architecture and Urbanism (Part 1) and
			ans.append(basicReq(takenClasses, 'ARCH.170A', 'Architecture 170A', 'Requirement of ARCH 170A, An Historical Survey of Architecture and Urbanism'))
			#ARCH 170B An Historical Survey of Architecture and Urbanism (Part 2) plus
			ans.append(basicReq(takenClasses, 'ARCH.170B', 'Architecture 170B', 'Requirement of ARCH 170B, An Historical Survey of Architecture and Urbanism'))
			#Either ARCH 110AC The Social and Cultural Basis of Design or ARCH 130 Introduction to Design Theories and Methods
			ans.append(twoChoiceReq(takenClasses, 'Design Theories' ,'ARCH.110AC' , 'Arch 110AC', 'ARCH.130', 'Arch 130', 'Requirement of either ARCH 110AC The Social and Cultural Basis of Design or ARCH 130 Introduction to Design Theories and Methods'))
			#Either ARCH 140 Energy and Environment or ARCH 160 Introduction to Construction
			ans.append(twoChoiceReq(takenClasses, 'Architecture', 'ARCH.140', 'Arch 140', 'ARCH.160', 'Arch 160', 'Requirement of either ARCH 140 Energy and Environment or ARCH 160 Introduction to Construction '))
			#Senior Year Project Track [ ARCH 102A Capstone Preparation Seminar, ARCH 102B Capstone Project, Capstone Electives. Choose three from list that will be provided each year by the instructors] 
			#OR Senior Year Studio Track [ ARCH 100C Architectural Design, ARCH 100D Architectural Design, ARCH 140 Energy and Environment or ARCH 160 Introduction to Construction, ARCH 150 Introduction to Structures]
			trackTwo= (('ARCH.100C'in takenClasses)and('ARCH.100D'in takenClasses)and ('ARCH.150'in takenClasses) and ('ARCH.140'in takenClasses) and ('ARCH.160'in takenClasses))
			trackOne= (('ARCH.102A'in takenClasses)and ('ARCH.102B'in takenClasses))
			trackDone=[]
			trackNotDone=[]
			tracks={'ARCH.100C':'Arch 100C','ARCH.100D':'Arch 100D','ARCH.140':'Arch 140','ARCH.150':'Arch 150','ARCH.160':'Arch 160','ARCH.102A':'Arch 102A','ARCH.102B':'Arch 102B'}
			for key in tracks:
				if key in takenClasses:
					trackDone.append(tracks[key])
				else:
					trackNotDone.append(tracks[key])
			if trackTwo:
				ans.append({'reqName':'Studio Track', 'reqCompleted':True, 'reqDescription':'Choose either project or studio track. Studio Track requirements:ARCH 100C Architectural Design, ARCH 100D Architectural Design, ARCH 140 Energy and Environment or ARCH 160 Introduction to Construction, ARCH 150 Introduction to Structures','courseDone':['Arch 100C','Arch 100D','Arch 140','Arch 150','Arch 160'], 'courseLeft':[]})
			elif trackOne:
				ans.append({'reqName':'Project Track', 'reqCompleted':True, 'reqDescription':'Choose either project or studio track. Project Track requirements:ARCH 102A Capstone Preparation Seminar, ARCH 102B Capstone Project, Three Capstone Electives from list that will be provided each year','courseDone':['Arch 102A','Arch 102B','Yearly Electives'], 'courseLeft':[]})
			else:
				ans.append({'reqName':'Senior Year', 'reqCompleted':False, 'reqDescription':'Choose either project or studio track. Studio Track requirements:ARCH 100C Architectural Design, ARCH 100D Architectural Design, ARCH 140 Energy and Environment or ARCH 160 Introduction to Construction, ARCH 150 Introduction to Structures. Project Track: ARCH 102A Capstone Preparation Seminar, ARCH 102B Capstone Project, Three Capstone Electives from list that will be provided each year','courseDone':trackDone, 'courseLeft':trackNotDone})
			return ans		
		#Landscape Architecture
		elif(major=='LDARCH'):
			#ENV DES 1 People and Environmental Design
			ans.append(basicReq(takenClasses, 'ENVDES.1', 'EnvDesign 1', 'Requirement of ENV DES 1 People and Environmental Design'))
			#ENV DES 4A Design and Activism, 4B Global Cities, 4C Future Ecologies (complete 2 of 3)
			envFour={'ENVDES.4A':'EnvDesign 4A','ENVDES.4B':'EnvDesign 4B','ENVDES.4C':'EnvDesign 4C'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'Environmental Design 4', envFour, 'Requirement of 2 of 4A Design and Activism, 4B Global Cities, 4C Future Ecologies', 2))
			#Upper Division College of Environmental Design Courses Outside of Landscape Architecture (3 courses total): courses in Environmental Design, Visual Studies, Architecture, and City and Regional Planning
			upperDone=[]
			upperClasses=0
			for item in takenClasses:
				if((re.search(r'ENVDES.1\d\d',item)) or (re.search(r'VISSTD.1\d\d',item)) or (re.search(r'ARCH.1\d\d',item)) or (re.search(r'CYPLAN.1\d\d',item))):
					upperDone.append(item.replace('.',' '))
					upperClasses+=1
			if upperClasses>=3:
				ans.append({'reqName':'College of Environmental Design Courses', 'reqCompleted':True, 'reqDescription':"Take at least 3 upper division courses in the College of Environmental Design but not Landscape Architecture(Environmental Design, Visual Studies, Architecture, and City and Regional Planning)",'courseDone':upperDone, 'courseLeft':['Any Environmental Design','Any Visual Studies','Any Architecture','Any City and Regional Planning']})
			else:
				ans.append({'reqName':'College of Environmental Design Courses', 'reqCompleted':False, 'reqDescription':"Take at least 3 upper division courses in the College of Environmental Design but not Landscape Architecture(Environmental Design, Visual Studies, Architecture, and City and Regional Planning)",'courseDone':upperDone, 'courseLeft':['Any Environmental Design','Any Visual Studies','Any Architecture','Any City and Regional Planning']})
			#ENV DES 11A Introduction to Visual Representation and Drawing
			ans.append(basicReq(takenClasses, 'ENVDES.11A', 'EnvDesign 11A', 'Requirement of ENV DES 11A, Introduction to Visual Representation and Drawing'))
			#ENV DES 11B Introduction to Design
			ans.append(basicReq(takenClasses, 'ENVDES.11B', 'EnvDesign 11B', 'Requirement of ENV DES 11B, Introduction to Design'))
			#Physical Science (course also completes Physical Science breadth requirement)
			physical={'EPS.50':'EPS 50','EPS.80':'EPS 80','ENVSCI.10':'ES 10','PHYSICS.7A':'Physics 7A','PHYSICS.8A':'Physics 8A','PHYSICS.10':'Physics 10','PHYSICS.C10':'Physics C10','L&S.C70V':'L&S C70V'}
			ans.append(manyChoiceReq(takenClasses, 'Physical Science Elective', physical, 'You must choice one of the following elective courses'))
			#Biological Science (course also completes Biological Science breadth requirement)
			biological={'BIOLOGY.1B':'Biology 1B' ,'BIOLOGY.11':'Biology 11' ,'PLANTBI.40':'PLANTBI 40' ,'ESPM.2':'ESPM 2','ESPM.6':'ESPM 6','ESPM 101A':'ESPM 101A','LDARCH.12':'LD ARCH 12'}
			ans.append(manyChoiceReq(takenClasses, 'Biological Science Elective', biological, 'You must choice one of the following elective courses'))
			#LD ARCH 101 (5) Fundamentals of Landscape Design (Topographic Form and Design)
			ans.append(basicReq(takenClasses, 'LDARCH.101', 'LandscapeArchitecture 101', 'Requirement of Landscape Architecture 101, Fundamentals of Landscape Design'))
			#LD ARCH 102 (5) Case Studies in Landscape Design (Design Development Studio)
			ans.append(basicReq(takenClasses, 'LDARCH.102', 'LandscapeArchitecture 102', 'Requirement of Landscape Architecture 102, Case Studies in Landscape Design'))
			#LD ARCH 103 (5) Energy, Fantasy, and Form
			ans.append(basicReq(takenClasses, 'LDARCH.103', 'LandscapeArchitecture 103', 'Requirement of Landscape Architecture 103, Energy, Fantasy, and Form'))
			#LD ARCH 110 (4) Ecological Analysis
			ans.append(basicReq(takenClasses, 'LDARCH.110', 'LandscapeArchitecture 110', 'Requirement of Landscape Architecture 110, Ecological Analysis'))
			#LD ARCH 112 (4) Landscape Plants: Identification and Use
			ans.append(basicReq(takenClasses, 'LDARCH.112', 'LandscapeArchitecture 112', 'Requirement of Landscape Architecture 112, Landscape Plants: Identification and Use'))
			#LD ARCH 120 (3) Topographic Form and Design Technology
			ans.append(basicReq(takenClasses, 'LDARCH.120', 'LandscapeArchitecture 120', 'Requirement of Landscape Architecture 120, Topographic Form and Design Technology'))
			#LD ARCH 121 (4) Design in Detail: Introduction to Landscape Materials and Construction
			ans.append(basicReq(takenClasses, 'LDARCH.121', 'LandscapeArchitecture 121', 'Requirement of Landscape Architecture 121,  Design in Detail: Introduction to Landscape Materials and Construction'))
			#LD ARCH 134A (3) Drawing Workshop I
			ans.append(basicReq(takenClasses, 'LDARCH.134A', 'LandscapeArchitecture 134A', 'Requirement of Landscape Architecture 134A, Drawing Workshop'))
			#LD ARCH 134B (3) Drawing Workshop II
			ans.append(basicReq(takenClasses, 'LDARCH.134B', 'LandscapeArchitecture 134B', 'Requirement of Landscape Architecture 134B, Drawing Workshop II'))
			#LD ARCH 135 (3) The Art of Landscape Drawing
			ans.append(basicReq(takenClasses, 'LDARCH.135', 'LandscapeArchitecture 135', 'Requirement of Landscape Architecture 135, The Art of Landscape Drawing'))
			#LD ARCH 170 (3) History and Literature of Landscape Architecture
			ans.append(basicReq(takenClasses, 'LDARCH.170', 'LandscapeArchitecture 170', 'Requirement of Landscape Architecture 170, History and Literature of Landscape Architecture'))
			return ans
		#Urban Studies
		elif(major=='URDES'):
			#ENV DES 1 People and Environmental Design
			ans.append(basicReq(takenClasses, 'ENVDES.1', 'EnvDesign 1', 'Requirement of ENV DES 1 People and Environmental Design'))
			#ENV DES 4A Design and Activism, 4B Global Cities, 4C Future Ecologies (complete 2 of 3)
			envFour={'ENVDES.4A':'EnvDesign 4A','ENVDES.4B':'EnvDesign 4B','ENVDES.4C':'EnvDesign 4C'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'Environmental Design 4', envFour, 'Requirement of 2 of 4A Design and Activism, 4B Global Cities, 4C Future Ecologies', 2))
			#Upper Division College of Environmental Design Courses Outside of City Planning (3 courses total): courses in Environmental Design, Visual Studies, Landscape Architecture, and Architecture
			upperDone=[]
			upperClasses=0
			for item in takenClasses:
				if((re.search(r'ENVDES.1\d\d',item)) or (re.search(r'VISSTD.1\d\d',item)) or (re.search(r'LDARCH.1\d\d',item)) or (re.search(r'ARCH.1\d\d',item))):
					upperDone.append(item.replace('.',' '))
					upperClasses+=1
			if upperClasses>=3:
				ans.append({'reqName':'College of Environmental Design Courses', 'reqCompleted':True, 'reqDescription':"Take at least 3 upper division courses in the College of Environmental Design but not City Planning(Environmental Design, Visual Studies, Landscape Architecture, and Architecture)",'courseDone':upperDone, 'courseLeft':['Any Environmental Design','Any Visual Studies','Any Landscape Architecture','Any City and Regional Planning']})
			else:
				ans.append({'reqName':'College of Environmental Design Courses', 'reqCompleted':False, 'reqDescription':"Take at least 3 upper division courses in the College of Environmental Design but not City Planning(Environmental Design, Visual Studies, Landscape Architecture, and Architecture)",'courseDone':upperDone, 'courseLeft':['Any Environmental Design','Any Visual Studies','Any Landscape Architecture','Any City and Regional Planning']})
			#Economics: ECON 1 or 2 Intro to Economics or ECON C3 Intro to Environmental Economics & Policy (also completes the SBS breadth requirement).
			econ={'ECON.1':'Econ 1','ECON.2':'Econ 2','ECON.C3':'Econ C3'}
			ans.append(manyChoiceReq(takenClasses, 'Economics', econ, 'Requirement of one economics course from ECON 1 or 2 Intro to Economics or ECON C3 Intro to Environmental Economics & Policy'))
			#Calculus: MATH 16A or MATH 1A
			ans.append(twoChoiceReq(takenClasses, 'Basic Calculus', 'MATH.16A', 'Math 16A', 'MATH.1A', 'Math.1A', 'Requirement of MATH 16A or Math 1A'))
			#Statistics: STAT 2, STAT 20, STAT 21, STAT 25, or STAT 131A
			stat={'STAT.2':'Stats 2','STAT.20':'Stats 20','STAT.21':'Stats 21','STAT.25':'Stats 25','STAT.131A':'Stats 131A'}
			ans.append(manyChoiceReq(takenClasses, 'Statistics', stat, 'Requirement of one statistics course from STAT 2, STAT 20, STAT 21, STAT 25, or STAT 131A'))
			#choose two of the following list:
			lower={'ENVDES.11A':'ENVDES 11A','ENVDES.11B':'ENVDES 11B','ENVDES.C169A':'ENVDES C169A','ENVDES.C169B':'ENVDES C169B','ENVDES.170':'ENVDES 170','ARCH.110AC':'ARCH 110AC','ARCH.111':'ARCH 111','ARCH.130':'ARCH 130','ARCH.170A':'ARCH 170A','ARCH.170B':'ARCH 170B','CYPLAN.111':'CY PLAN 111','CYPLAN.116':'CY PLAN 116','CYPLAN.140':'CY PLAN 140','LDARCH.170':'LDARCH 170'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'Lower Division Electives', lower, 'Choose two lower division Environmental Design courses from the list', 2))
			#ENV DES 100: The City: Theories and Methods of Urban Studies (4) (SP)
			ans.append(basicReq(takenClasses, 'ENVDES.100', 'EnvDesign 100', 'Requirement of ENVDES 100, The City: Theories and Methods of Urban Studies'))
			#CY PLAN 110: Introduction to City Planning (4) (FA, SP, SU)
			ans.append(basicReq(takenClasses, 'CYPLAN.110', 'CityPlanning 110', 'Requirement of CY PLAN 110, Introduction to City Planning'))
			#Choose four from the following:
			upper={'CYPLAN.111':'CYPLAN 111','CYPLAN.113A':'CYPLAN 113A','CYPLAN.113B':'CYPLAN 113B','CYPLAN.114':'CYPLAN 114','CYPLAN.115':'CYPLAN 115','CYPLAN.116':'CYPLAN 116','CYPLAN.118AC':'CYPLAN 118AC','CYPLAN.119':'CYPLAN 119','CYPLAN.120':'CYPLAN 120','CYPLAN.C139':'CYPLAN C139','CYPLAN.140':'CYPLAN 140','CYPLAN.190':'CYPLAN 190'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'Upper Division Electives', upper, 'Choose four upper division Environmental Design courses from the list', 4))
			#three Urban Studies related courses outside CED from the following list of courses. 
			outside={'AFRICAM.107': 'AFRICAM 107','AMERSTD.102':'AMERSTD 102','ANTHRO.139':'ANTHRO 139','ANTHRO.C146':'ANTHRO C146', 'ANTHRO.157':'ANTHRO 157', 'ANTHRO.189':'ANTHRO 189', 'ASAMST.150':'ASAMST 150', 'CIVENG.156':'CIV ENG 156', 'CIVENG.167':'CIV ENG 167','DEMOG.C126':'DEMOG C126','SOCIOL.C126':'Sociol C126',
				'DEMOG.145AC':'DEMOG 145AC', 'DEVSTD.C100':'DEV STD C100','ECON.115':'ECON 115','ECON.C102':'ECON C102','ECON.121':'ECON 121', 'ECON.C125':'ECON C125','ECON.131':'ECON 131','ECON.C171':'ECON C171','ECON.174':'ECON 174','EDUC.186':'EDUC 186AC' ,'ENERES.C100':'ENERES C100','ENERES.101':'ENERES 101', 
				'ENERES.151':'ENERES 151','ENERES.170':'ENERES 170','ENVECON.C101':'ENVECON C101', 'ENVECON.151':'ENVECON 151', 'ESPM.102D':'ESPM 102D', 'ESPM.155':'ESPM 155', 'ESPM.160AC':'ESPM 160AC', 'ESPM.161':'ESPM 161', 'ESPM.163AC':'ESPM 163AC','ESPM.165':'ESPM 165','ESPM.168':'ESPM 168','ESPM.169':'ESPM 169',
				'ETHSTD.159AC':'ETH STD 159AC','GEOG.110':'GEOG 110','GEOG.111':'GEOG 111','GEOG.123':'GEOG 123', 'GEOG.125':'GEOG 125', 'GEOG.130':'GEOG 130', 'GEOG.C152':'GEOG C152', 'GEOG.159AC':'GEOG 159AC', 'GEOG.164':'GEOG 164','GEOG.170':'GEOG 170', 'GEOG.181':'GEOG 181','GEOG.C188':'GEOG C188',
				'HISTORY.120AC':'HISTORY 120AC','HISTORY.134':'HISTORY 134','HISTORY.134A':'HISTORY134A','HISTORY.C139B':'HISTORY C139B','HISTORY.160':'HISTORY 160','HISTORY.C176':'HISTORY C176', 'IAS.115':'IAS 115','IAS.C145':'IAS C145','LGLSTDS.182':'LGL STDS 182','NUSCTX.166':'NUSCTX 166','PACS.127':'PACS 127',
				'PACS.149':'PACS 149','POLSCI.114A':'POL SCI 114A','POLSCI.138F':'POL SCI 138F', 'POLSCI.139D':'POL SCI 139D','POLSCI.181':'POL SCI 181','POLECON.100':'POLECON 100','POLECON.101':'POLECON 101','PBHLTH.131AC':'PUB HLTH 131AC','PBHLTH.150B':'PUB HLTH 150B', 'PUBPOL.103':'PUB POL 103', 'PUBPOL.156':'PUB POL 156',
				'PUBPOL.184':'PUB POL 184','SOCIOL.110':'SOCIOL 110','SOCIOL.124':'SOCIOL 124','SOCIOL.130':'SOCIOL 130','SOCIOL.130AC':'SOCIOL 130AC', 'SOCIOL.136':'SOCIOL 136','SOCIOL.137AC':'SOCIOL 137AC','SOCIOL.145':'SOCIOL 145','SOCIOL.127':'SOCIOL 127','SOCIOL.180I':'SOCIOL 180I','SOCIOL.186':'SOCIOL 186','UGBA.105':'UGBA 105',
				'UGBA.180':'UGBA 180', 'UGBA.192P':'UGBA 192P','UGBA.195S':'UGBA 195S' }
			ans.append(doSomeManyChoiceReq(takenClasses, 'Urban Studies Elective', outside, 'Requirement of three Urban Studies related courses outside CED from the following list of courses', 3))
			#At least one of the three courses must have international content			
			international={'ANTHRO.139':'ANTHRO 139','DEVSTD.C100':'DEV STD C100','ECON.115':'ECON 115','EDUC.186AC':'EDUC 186AC' ,'ESPM.165':'ESPM 165','ESPM.169':'ESPM 169','GEOG.110':'GEOG 110','GEOG.111':'GEOG 111','GEOG.123':'GEOG 123', 'GEOG.130':'GEOG 130', 'GEOG.C152':'GEOG C152', 'GEOG.159AC':'GEOG 159AC', 'GEOG.164':'GEOG 164',
				'HISTORY.134':'HISTORY 134','HISTORY.134A':'HISTORY134A','HISTORY.160':'HISTORY 160','HISTORY.C176':'HISTORY C176', 'IAS.115':'IAS 115','IAS.C145':'IAS C145','PACS.127':'PACS 127', 'PACS.149':'PACS 149','POLECON.100':'POLECON 100','POLECON.101':'POLECON 101','SOCIOL.127':'SOCIOL 127','SOCIOL.180I':'SOCIOL 180I','UGBA.195S':'UGBA 195S'}
			ans.append(manyChoiceReq(takenClasses, 'International Urban Studies Elective', international, 'One of the previous Urban Studies Electives must have International content'))
			#complete TWO of the following four capstone experiences: Thesis: ENV DES 195B, Planning Studio: CY PLAN 116, Research Studio: CY PLAN 190, Field experience/internship CY PLAN 197
			capstone={'ENVDES.195B':'EnvDesign 195B','CYPLAN.116':'CityPlanning 116','CYPLAN.190':'CityPlanning 190','CYPLAN.197':'CityPlanning 197'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'Capstone Experience', capstone, 'Requirement to complete TWO of the following four capstone experiences: Thesis: ENV DES 195B, Planning Studio: CY PLAN 116, Research Studio: CY PLAN 190, Field experience/internship CY PLAN 197', 2))
			return ans
		#Sustainable Environmental Design
		elif(major=='SENVDES'):
			#ENV DES 1 People and Environmental Design
			ans.append(basicReq(takenClasses, 'ENVDES.1', 'EnvDesign 1', 'Requirement of ENV DES 1 People and Environmental Design'))
			#ENV DES 4A Design and Activism, 4B Global Cities, 4C Future Ecologies (complete 2 of 3)
			envFour={'ENVDES.4A':'EnvDesign 4A','ENVDES.4B':'EnvDesign 4B','ENVDES.4C':'EnvDesign 4C'}
			ans.append(doSomeManyChoiceReq(takenClasses, 'Environmental Design 4', envFour, 'Requirement of 2 of 4A Design and Activism, 4B Global Cities, 4C Future Ecologies', 2))
			#LD ARCH 12: Environmental Science for Sustainable Development
			ans.append(basicReq(takenClasses, 'LDARCH.12', 'LandscapeArchitecture 12', 'Requirement of Landscape Architecture 12, Environmental Science for Sustainable Development'))
			#MATH 16A or 1A: Analytic Geometry and Calculus
			ans.append(twoChoiceReq(takenClasses, 'Basic Calculus', 'MATH.16A', 'Math 16A', 'MATH.1A', 'Math.1A', 'Requirement of MATH 16A or Math 1A'))
			#STAT 2 or higher: Introduction to Statistics
			statDone=[]
			for item in takenClasses:
				if ('STAT.' in item) and (not (item is 'STAT.1')):
					statDone.append(item.replace('STAT.', 'Stats '))
			if statDone:
				ans.append({'reqName':'Statistics', 'reqCompleted':True, 'reqDescription':'Requirement of one statistics class numbered two or higher','courseDone':statDone, 'courseLeft':[]})
			else:
				ans.append({'reqName':'Statistics', 'reqCompleted':False, 'reqDescription':'Requirement of one statistics class numbered two or higher','courseDone':[], 'courseLeft':['Stats 2+']})
			#PHYSICS 8A or 7A
			ans.append(twoChoiceReq(takenClasses, 'Basic Physics', 'PHYSICS.7A', 'Physics 7A', 'PHYSICS.8A', 'Physics 8A', 'Requirement of PHYSICS 8A or 7A'))
			#Economics: ECON 1 or 2 Intro to Economics or ECON C3 Intro to Environmental Economics & Policy (also completes the SBS breadth requirement).
			econ={'ECON.1':'Econ 1','ECON.2':'Econ 2','ECON.C3':'Econ C3'}
			ans.append(manyChoiceReq(takenClasses, 'Economics', econ, 'Requirement of one economics course from ECON 1 or 2 Intro to Economics or ECON C3 Intro to Environmental Economics & Policy'))
			#ENV DES 100: The City: Theories and Methods of Urban Studies (4) (SP)
			ans.append(basicReq(takenClasses, 'ENVDES.100', 'EnvDesign 100', 'Requirement of ENVDES 100, The City: Theories and Methods of Urban Studies'))
			#ENV DES 102: Critical Approaches to Sustainable Urbanism & Design (FL)
			ans.append(basicReq(takenClasses, 'ENVDES.102', 'EnvDesign 102', 'Requirement of ENV DES 102, Critical Approaches to Sustainable Urbanism & Design'))
			#ENV DES 106: Sustainable Environmental Design Workshop (SP)
			ans.append(basicReq(takenClasses, 'ENVDES.106', 'EnvDesign 106', 'Requirement of ENV DES 106, Sustainable Environmental Design Workshop'))
			#ARCH 140: Energy and Environment (SP)
			ans.append(basicReq(takenClasses, 'ARCH.140', 'Architecture 140', 'Requirement of ARCH 140, Energy and Environment'))
			#ARCH 242: Sustainability Colloquium; must take for 2 units (FL)
			ans.append(basicReq(takenClasses, 'ARCH.242', 'Architecture 242', 'Requirement of ARCH 242, Sustainability Colloquium'))
			#CY PLAN 119: Planning for Sustainability (FL)
			ans.append(basicReq(takenClasses, 'CYPLAN.119', 'CityPlanning 119', 'Requirement of CY PLAN 119, Planning for Sustainability'))
			#LD ARCH 110 (4) Ecological Analysis
			ans.append(basicReq(takenClasses, 'LDARCH.110', 'LandscapeArchitecture 110', 'Requirement of Landscape Architecture 110, Ecological Analysis'))
			#LD ARCH 130: Sustainable Cities & Landscapes (SP)
			ans.append(basicReq(takenClasses, 'LDARCH.130', 'LandscapeArchitecture 130', 'Requirement of Landscape Architecture 130, Sustainable Cities & Landscapes'))
			#LD ARCH /GEOG C188: Geographic Information Systems (FL)
			ans.append(twoChoiceReq(takenClasses, 'Geographic Information Systems', 'GEOG.C188','Geography C188', 'LDARCH.C188', 'LandscapeArchitecture C188', 'Requirement of LD ARCH/GEOG C188, Geographic Information Systems'))
			#4 courses from each of the following 4 areas or 2 courses from 2 areas for specializations.
			#Economics, Business and Policy
			business={'MBA.107':'BUS ADM 107','MBA.180':'BUS ADM 180','CYPLAN.113A':'CY PLAN 113A','CYPLAN.113B':'CY PLAN 113B','CYPLAN.115':'CY PLAN 115','IAS.115':'IAS 115','GPP.115':'GPP 115','ENVECON.100':'ENVECON 100',
				'ENVECON.C175':'ENVECON C175','ENERES.151':'ENERES 151','ENERES.190':'ENERES 190','ESPM.60':'ESPM 60','ESPM.166':'ESPM 166','ESPM.168':'ESPM 168','ESPM.169':'ESPM 169','ESPM.C193A':'ESPM C193A', 'EDUC.C193A':'EDU C193A','PUBPOL.182':'PUB POL 182'}
			#Society, Culture and Ethics
			culture={'ANTHRO.137':'ANTHRO 137','ARCH,110AC':'ARCH 110AC','ARCH.133':'ARCH 133','CYPLAN.118AC':'CY PLAN 118AC','ENERES.100':'ENERES 100','ENERES.101':'ENERES 101', 'ESPM.148':'ESPM 148','ESPM.151':'ESPM 151','ESPM.161':'ESPM 161','ESPM.163AC':'ESPM 163AC',
				'ESPM.C167':'ESPM C167','PBHLTH.C160':'PUBHEAL C160','ESPM.155':'ESPM 155','LDARCH.140':'LD ARCH 140','LDARCH.141AC':'LD ARCH 141AC','SOCIOL.123':'SOCIOL 123','SOCIOL.128':'SOCIOL 128' }
			#Resources and Environmental Management
			management={'ENERES.102':'ENERES 102','EPS.170AC':'EPS 170AC','ESPM.50AC':'ESPM 50AC','ESPM.102D':'ESPM 102D','ESPM.102C':'ESPM 102C','ESPM.117':'ESPM 117','INTEGBI.152':'IB 152' }
			#Design and Technology
			design={'ARCH.105':'ARCH 105','ARCH.122':'ARCH 122','ARCH.130':'ARCH 130','ARCH.242':'ARCH 242','ARCH.149':'ARCH 149','ARCH.160':'ARCH 160','CYPLAN.C111':'CY PLAN C111','ARCH.C111':'ARCH C111',
				'CYPLAN.C114':'CY PLAN C114', 'CIVENFG.154':'CEE 154', 'CYPLAN.116':'CY PLAN 116','CYPLAN.140':'CY PLAN 140','ENERES.175':'ENERES 175','ENVDES.11A':'ENV DES 11A','ENVDES.11B':'ENV DES 11B','GEOG.125':'GEOG 125','INFO.146':'INFO 146'}
			temp1=manyChoiceReq(takenClasses, '', business, '')
			temp2=manyChoiceReq(takenClasses, '', culture, '')
			temp3=manyChoiceReq(takenClasses, '', management, '')
			temp4=manyChoiceReq(takenClasses, '', design, '')
			t1=len(temp1['courseDone'])
			t2=len(temp2['courseDone'])
			t3=len(temp3['courseDone'])
			t4=len(temp4['courseDone'])
			twos=0
			if t1>=2:
				twos+=1
			if t2>=2:
				twos+=1
			if t3>=2:
				twos+=1
			if t4>=2:
				twos+=1
			if(twos>=2)or(t1>0 and t2>0 and t3>0 and t4>0):
				ans.append({'reqName':'Concentrations', 'reqCompleted':True, 'reqDescription':'4 courses each from one of 4 areas or 2 courses from 2 areas for specializations','courseDone':temp1['courseDone']+temp2['courseDone']+temp3['courseDone']+temp4['courseDone'], 'courseLeft':temp1['courseLeft']+temp2['courseLeft']+temp3['courseLeft']+temp4['courseLeft']})
			else:
				ans.append({'reqName':'Concentrations', 'reqCompleted':False, 'reqDescription':'4 courses each from one of 4 areas or 2 courses from 2 areas for specializations','courseDone':temp1['courseDone']+temp2['courseDone']+temp3['courseDone']+temp4['courseDone'], 'courseLeft':temp1['courseLeft']+temp2['courseLeft']+temp3['courseLeft']+temp4['courseLeft']})
			return ans			
		#Should not occur but in the case that the major given does not match
		else:
			raise MyError(major+"is not a valid major at UC Berkeley Haas School of Business")
		return ans
	# Should not occur but in the case that the college given does not match
	else:
		raise MyError(college+'is not a valid college at UC Berkeley')
	return ans

