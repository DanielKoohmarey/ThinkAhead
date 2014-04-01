## Import the python xUnit framework
from django.test import TestCase
from darsplus.requirementscode import *

class TestRequirements(TestCase):
	def testBasicReq1(self):
		ans=basicReq([],'ELENG.20','EE 20',"Engineering class")
		self.assertTrue(type(ans) is dict)
		self.assertEqual(5, len(ans))
	def testBasicReq2(self):
		ans=basicReq([],'ELENG.20','EE 20',"Engineering class")
		self.assertEqual([],ans['courseDone'])
		self.assertEqual(['EE 20'],ans['courseLeft'])
		self.assertTrue( not ans['reqCompleted'])
		self.assertEqual('EE 20',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testBasicReq3(self):
		ans=basicReq(['ELENG.20','ELENG.40'],'ELENG.20','EE 20',"Engineering class")
		self.assertEqual(['EE 20'],ans['courseDone'])
		self.assertEqual([],ans['courseLeft'])
		self.assertTrue(ans['reqCompleted'])
		self.assertEqual('EE 20',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testUnits1(self):
		self.assertEqual(4,units('COMPSCI.61B'))
	def testUnits2(self):
		self.assertEqual(3,units('MATSCI.120'))
	def testTwoReq1(self):
		ans=twoReq([],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertTrue(type(ans) is dict)
		self.assertEqual(5, len(ans))
	def testTwoReq2(self):
		ans=twoReq([],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertEqual([],ans['courseDone'])
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertIn('EE 40',ans['courseLeft'])
		self.assertTrue( not ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testTwoReq3(self):
		ans=twoReq(['ELENG.20','ELENG.40'],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertEqual([],ans['courseLeft'])
		self.assertIn('EE 20',ans['courseDone'])
		self.assertIn('EE 40',ans['courseDone'])
		self.assertTrue(ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testTwoReq4(self):
		ans=twoReq(['ELENG.20'],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertIn('EE 20',ans['courseDone'])
		self.assertIn('EE 40',ans['courseLeft'])
		self.assertTrue(not ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testTwoChoiceReq1(self):
		ans=twoChoiceReq([],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertTrue(type(ans) is dict)
		self.assertEqual(5, len(ans))
	def testTwoChoiceReq2(self):
		ans=twoChoiceReq(['ELENG.20'],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertIn('EE 20',ans['courseDone'])
		self.assertIn('EE 40',ans['courseLeft'])
		self.assertTrue(ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testTwoChoiceReq3(self):
		ans=twoChoiceReq(['ELENG.40'],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertIn('EE 40',ans['courseDone'])
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertTrue(ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testTwoChoiceReq4(self):
		ans=twoChoiceReq(['ELENG.40','ELENG.20'],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertIn('EE 40',ans['courseDone'])
		self.assertIn('EE 20',ans['courseDone'])
		self.assertTrue(ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testTwoChoiceReq5(self):
		ans=twoChoiceReq([],'Electronics','ELENG.20','EE 20','ELENG.40','EE 40',"Engineering class")
		self.assertIn('EE 40',ans['courseLeft'])
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertTrue(not ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testManyChoiceReq1(self):
		listelec={'ELENG.20':'EE 20','ELENG.40':'EE 40','ELENG.100':'EE 100'}
		ans=manyChoiceReq([],'Electronics',listelec,"Engineering class")
		self.assertTrue(type(ans) is dict)
		self.assertEqual(5, len(ans))
	def testManyChoiceReq2(self):
		listelec={'ELENG.20':'EE 20','ELENG.40':'EE 40','ELENG.100':'EE 100'}
		ans=manyChoiceReq(['ELENG.40'],'Electronics',listelec,"Engineering class")
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertIn('EE 100',ans['courseLeft'])
		self.assertIn('EE 40',ans['courseDone'])
		self.assertTrue(ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testManyChoiceReq3(self):
		listelec={'ELENG.20':'EE 20','ELENG.40':'EE 40','ELENG.100':'EE 100'}
		ans=manyChoiceReq(['ELENG.40','ELENG.100'],'Electronics',listelec,"Engineering class")
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertIn('EE 100',ans['courseDone'])
		self.assertIn('EE 40',ans['courseDone'])
		self.assertTrue(ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testManyChoiceReq4(self):
		listelec={'ELENG.20':'EE 20','ELENG.40':'EE 40','ELENG.100':'EE 100'}
		ans=manyChoiceReq([],'Electronics',listelec,"Engineering class")
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertIn('EE 100',ans['courseLeft'])
		self.assertIn('EE 40',ans['courseLeft'])
		self.assertTrue(not ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testDoSomeManyChoiceReq1(self):
		listelec={'ELENG.20':'EE 20','ELENG.40':'EE 40','ELENG.100':'EE 100'}
		ans=doSomeManyChoiceReq([],'Electronics',listelec,"Engineering class",2)
		self.assertTrue(type(ans) is dict)
		self.assertEqual(5, len(ans))
	def testDoSomeManyChoiceReq2(self):
		listelec={'ELENG.20':'EE 20','ELENG.40':'EE 40','ELENG.100':'EE 100'}
		ans=doSomeManyChoiceReq(['ELENG.40'],'Electronics',listelec,"Engineering class",2)
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertIn('EE 100',ans['courseLeft'])
		self.assertIn('EE 40',ans['courseDone'])
		self.assertTrue(not ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testDoSomeManyChoiceReq3(self):
		listelec={'ELENG.20':'EE 20','ELENG.40':'EE 40','ELENG.100':'EE 100'}
		ans=doSomeManyChoiceReq(['ELENG.40','ELENG.100'],'Electronics',listelec,"Engineering class",2)
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertIn('EE 100',ans['courseDone'])
		self.assertIn('EE 40',ans['courseDone'])
		self.assertTrue(ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])
	def testDoSomeManyChoiceReq4(self):
		listelec={'ELENG.20':'EE 20','ELENG.40':'EE 40','ELENG.100':'EE 100'}
		ans=doSomeManyChoiceReq([],'Electronics',listelec,"Engineering class",2)
		self.assertIn('EE 20',ans['courseLeft'])
		self.assertIn('EE 100',ans['courseLeft'])
		self.assertIn('EE 40',ans['courseLeft'])
		self.assertTrue(not ans['reqCompleted'])
		self.assertEqual('Electronics',ans['reqName'])
		self.assertEqual("Engineering class",ans['reqDescription'])

class TestUniversity(TestCase):
	def testAC1(self):
		ans= remainingRequirements([], "College of Engineering", 'Electrical Engineering & Computer Sciences')
		self.assertTrue( not ans[0]['reqCompleted'])
	def testAC2(self):
		ans= remainingRequirements(['GWS.100AC'], "College of Engineering", 'Electrical Engineering & Computer Sciences')
		self.assertTrue( ans[0]['reqCompleted'])
	def testAC3(self):
		ans= remainingRequirements(['ELENG.40','GWS.100AC'], "College of Engineering", 'Electrical Engineering & Computer Sciences')
		self.assertTrue( ans[0]['reqCompleted'])
	def testUnits1(self):
		ans= remainingRequirements([], "College of Engineering", 'Electrical Engineering & Computer Sciences')
		self.assertTrue( not ans[1]['reqCompleted'])
	def testUnits1(self):
		ans= remainingRequirements(['ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20'], "College of Engineering", 'Electrical Engineering & Computer Sciences')
		self.assertTrue(ans[1]['reqCompleted'])

class TestEngineering(TestCase):
	def testReadComp1(self):
		ans= remainingRequirements([], "College of Engineering", 'Electrical Engineering & Computer Sciences')
		self.assertTrue( not ans[5]['reqCompleted'])
	def testReadComp2(self):
		ans= remainingRequirements(['ENGLISH.R1A'], "College of Engineering", 'Electrical Engineering & Computer Sciences')
		self.assertTrue( not ans[5]['reqCompleted'])
		self.assertIn('You have completed R1A',ans[5]['reqDescription'])
	def testReadComp3(self):
		ans= remainingRequirements(['ENGLISH.R1B'], "College of Engineering", 'Electrical Engineering & Computer Sciences')
		self.assertTrue( not ans[5]['reqCompleted'])
		self.assertIn('You have completed R1B',ans[5]['reqDescription'])
	def testReadComp4(self):
		ans= remainingRequirements(['ENGLISH.R1B','ENGLISH.R1A'], "College of Engineering", 'Electrical Engineering & Computer Sciences')
		self.assertTrue(ans[5]['reqCompleted'])
	def testEECS1(self):
		ans= remainingRequirements([], "College of Engineering", 'Electrical Engineering & Computer Sciences')
		self.assertEqual(23,len(ans))
	def testEECS2(self):
		ans= remainingRequirements([], "College of Engineering", 'Electrical Engineering & Computer Sciences')
		self.assertTrue( not ans[14]['reqCompleted'])
		self.assertIn('You have only taken 0',ans[14]['reqDescription'])
	def testEECS3(self):
		ans= remainingRequirements(['ELENG.40','ELENG.40','ELENG.40','COMPSCI.61A','COMPSCI.61A','COMPSCI.61A'], "College of Engineering", 'Electrical Engineering & Computer Sciences')
		self.assertTrue(not ans[14]['reqCompleted'])
		self.assertIn('You have only taken 0',ans[14]['reqDescription'])
	def testEECS4(self):
		ans= remainingRequirements(['ELENG.140','ELENG.140','ELENG.140','COMPSCI.170','COMPSCI.170','COMPSCI.170'], "College of Engineering", 'Electrical Engineering & Computer Sciences')
		self.assertTrue(ans[14]['reqCompleted'])
	def testBIOENG1(self):
		ans= remainingRequirements([], "College of Engineering", 'Bioengineering')
		self.assertEqual(5+2+20,len(ans))
	def testBIOENG2(self):
		ans= remainingRequirements([], "College of Engineering", 'Bioengineering')
		self.assertTrue(not ans[9]['reqCompleted'])
	def testBIOENG3(self):
		ans= remainingRequirements(['CHEM.1A'], "College of Engineering", 'Bioengineering')
		self.assertTrue(not ans[9]['reqCompleted'])
	def testBIOENG4(self):
		ans= remainingRequirements(['CHEM.1AL'], "College of Engineering", 'Bioengineering')
		self.assertTrue(not ans[9]['reqCompleted'])
	def testBIOENG5(self):
		ans= remainingRequirements(['CHEM.1AL', 'CHEM.1A'], "College of Engineering", 'Bioengineering')
		self.assertTrue(ans[9]['reqCompleted'])
	def testBIOENG6(self):
		ans= remainingRequirements(['CHEM.4A'], "College of Engineering", 'Bioengineering')
		self.assertTrue(ans[9]['reqCompleted'])
	def testBIOENG7(self):
		ans= remainingRequirements([], "College of Engineering", 'Bioengineering')
		self.assertTrue(not ans[10]['reqCompleted'])
	def testBIOENG8(self):
		ans= remainingRequirements(['CHEM.3A'], "College of Engineering", 'Bioengineering')
		self.assertTrue(not ans[10]['reqCompleted'])
	def testBIOENG9(self):
		ans= remainingRequirements(['CHEM.3AL'], "College of Engineering", 'Bioengineering')
		self.assertTrue(not ans[10]['reqCompleted'])
	def testBIOENG10(self):
		ans= remainingRequirements(['CHEM.3AL', 'CHEM.3A'], "College of Engineering", 'Bioengineering')
		self.assertTrue(ans[10]['reqCompleted'])
	def testBIOENG11(self):
		ans= remainingRequirements(['CHEM.112A'], "College of Engineering", 'Bioengineering')
		self.assertTrue(ans[10]['reqCompleted'])
	def testCIVENG1(self):
		ans= remainingRequirements([], "College of Engineering", 'Civil and Environmental Engineering')
		self.assertEqual(5+2+21,len(ans))
	def testCOENG1(self):
		ans= remainingRequirements([], "College of Engineering", 'Computational Engineering Science')
		self.assertEqual(5+2+20,len(ans))
	def testCOENG2(self):
		ans= remainingRequirements(['BIOENG.153', 'ELENG.100','PHYSICS.110A','ENGIN.120'], "College of Engineering", 'Computational Engineering Science')
		self.assertTrue(ans[21]['reqCompleted'])
	def testCOENG3(self):
		ans= remainingRequirements(['BIOENG.153', 'ELENG.100','PHYSICS.110A'], "College of Engineering", 'Computational Engineering Science')
		self.assertTrue(not ans[21]['reqCompleted'])
	def testCOENG4(self):
		ans= remainingRequirements(['BIOENG.153', 'ELENG.100','PHYSICS.110A','ELENG.120'], "College of Engineering", 'Computational Engineering Science')
		self.assertTrue(not ans[21]['reqCompleted'])
	def testENENG1(self):
		ans= remainingRequirements([], "College of Engineering", 'Energy Engineering')
		self.assertEqual(5+2+24,len(ans))
	def testENENG2(self):
		ans= remainingRequirements(['CIVENG.11','CIVENG.70'], "College of Engineering", 'Energy Engineering')
		self.assertTrue(not ans[15]['reqCompleted'])
	def testENENG3(self):
		ans= remainingRequirements(['ELENG.40','CIVENG.70'], "College of Engineering", 'Energy Engineering')
		self.assertTrue(ans[15]['reqCompleted'])
	def testENENG4(self):
		ans= remainingRequirements(['ELENG.40','ENGIN.45'], "College of Engineering", 'Energy Engineering')
		self.assertTrue(ans[15]['reqCompleted'])
	def testENGMS1(self):
		ans= remainingRequirements([], "College of Engineering", 'Engineering Mathematics & Statistics')
		self.assertEqual(5+2+16,len(ans))
	def testENGMS2(self):
		ans= remainingRequirements(['COMPSCI.61A','ENGIN.7','ENGIN.177','COMPSCI.61B'], "College of Engineering", 'Engineering Mathematics & Statistics')
		self.assertTrue(ans[12]['reqCompleted'])
	def testENGMS3(self):
		ans= remainingRequirements(['COMPSCI.61A','ENGIN.7','COMPSCI.61B'], "College of Engineering", 'Engineering Mathematics & Statistics')
		self.assertTrue(not ans[12]['reqCompleted'])
	def testENGMS4(self):
		ans= remainingRequirements(['COMPSCI.61A','ENGIN.177','COMPSCI.61B'], "College of Engineering", 'Engineering Mathematics & Statistics')
		self.assertTrue(not ans[12]['reqCompleted'])
	def testENGMS5(self):
		ans= remainingRequirements(['COMPSCI.61C','COMPSCI.70'], "College of Engineering", 'Engineering Mathematics & Statistics')
		self.assertTrue(ans[12]['reqCompleted'])
	def testENGP1(self):
		ans= remainingRequirements([], "College of Engineering", 'Engineering Physics')
		self.assertEqual(5+2+21,len(ans))
	def testINDENG1(self):
		ans= remainingRequirements([], "College of Engineering", 'Industrial Engineering & Operations Research')
		self.assertEqual(5+2+18,len(ans))
	def testMATSCI1(self):
		ans= remainingRequirements([], "College of Engineering", 'Materials Science & Engineering')
		self.assertEqual(5+2+23,len(ans))
	def testMECENG1(self):
		ans= remainingRequirements([],"College of Engineering", 'Mechanical Engineering')
		self.assertEqual(5+2+24,len(ans))
	def testNUCENG1(self):
		ans= remainingRequirements([], "College of Engineering", 'Nuclear Engineering')
		self.assertEqual(5+2+19,len(ans))
	def testBIOMATSCI1(self):
		ans= remainingRequirements([], "College of Engineering", 'Bioengineering/Materials Science & Engineering')
		self.assertEqual(5+2+28,len(ans))
	def testEECSMATSCI1(self):
		ans= remainingRequirements([], "College of Engineering", 'Materials Science & Engineering/Electrical Engineering & Computer Sciences')
		self.assertEqual(5+2+26,len(ans))
	def testEECSNUCENG1(self):
		ans= remainingRequirements([], "College of Engineering", 'Nuclear Engineering/Electrical Engineering & Computer Sciences')
		self.assertEqual(5+2+24,len(ans))
	def testMATNUCENG1(self):
		ans= remainingRequirements([], "College of Engineering", 'Materials Science & Engineering/Nuclear Engineering')
		self.assertEqual(5+2+27,len(ans))
	def testMECNUCENG1(self):
		ans= remainingRequirements([], "College of Engineering", 'Nuclear Engineering/Mechanical Engineering')
		self.assertEqual(5+2+27,len(ans))
	def testMATMECENG1(self):
		ans= remainingRequirements([], "College of Engineering", 'Materials Science & Engineering/Mechanical Engineering')
		self.assertEqual(5+2+31,len(ans))
    	def testENVENG1(self):
		ans= remainingRequirements([], "College of Engineering", 'Environmental Engineering Science')
		self.assertEqual(24,len(ans))
	def testENVENG2(self):
		ans= remainingRequirements(['ARCH.140', 'BIOENG.C181'], "College of Engineering", 'Environmental Engineering Science')
		self.assertTrue( not ans[22]['reqCompleted'])
		self.assertIn('You have completed ',ans[22]['reqDescription'])
	def testENVENG3(self):
		ans= remainingRequirements(['ARCH.140', 'BIOENG.C181','CHMENG.140','CHMENG.142'], "College of Engineering", 'Environmental Engineering Science')
		self.assertTrue( ans[22]['reqCompleted'])
	def testENVENG4(self):
		ans= remainingRequirements(['CHEM.112A','CHEM.112B'], "College of Engineering", 'Environmental Engineering Science')
		self.assertTrue( ans[23]['reqCompleted'])
	def testENVENG5(self):
		ans= remainingRequirements(['EPS.101','EPS.108','EPS.116'], "College of Engineering", 'Environmental Engineering Science')
		self.assertTrue( ans[23]['reqCompleted'])
	def testENVENG6(self):
		ans= remainingRequirements(['EPS.101','EPS.C180','ESPM.102A'], "College of Engineering", 'Environmental Engineering Science')
		self.assertTrue(not ans[23]['reqCompleted'])

class TestChem(TestCase):
	def testBSCHEM1(self):
		ans= remainingRequirements([], "College of Chemistry", 'B.S. Chemistry')
		self.assertEqual(5+8+5,len(ans))
	def testBACHEM1(self):
		ans= remainingRequirements([], "College of Chemistry", 'B.A. Chemistry')
		self.assertEqual(5+8+3,len(ans))
	def testCHEMENG1(self):
		ans= remainingRequirements([], "College of Chemistry", 'Chemical Engineering')
		self.assertEqual(5+8+16,len(ans))
	def testCHEMBIO1(self):
		ans= remainingRequirements([], "College of Chemistry", 'Chemical Biology')
		self.assertEqual(5+8+9,len(ans))
	def testCHEMMATSCI1(self):
		ans= remainingRequirements([], "College of Chemistry", 'Chemical Engineering/Materials Science & Engineering')
		#to be changed
		self.assertEqual(5+8,len(ans))
	def testCHEMNUCENG1(self):
		ans= remainingRequirements([], "College of Chemistry", 'Chemical Engineering/Nuclear Engineering')
		#to be changed
		self.assertEqual(5+8,len(ans))

class TestEnvironmentalDesign(TestCase):
	def testARCH1(self):
		ans= remainingRequirements([], "College of Environmental Design", 'Architecture')
		self.assertEqual(5+8+14,len(ans))
	def testLDARCH1(self):
		ans= remainingRequirements([], "College of Environmental Design", 'Landscape Architecture')
		self.assertEqual(5+8+18,len(ans))
	def testURDES1(self):
		ans= remainingRequirements([], "College of Environmental Design", 'Urban Studies')
		self.assertEqual(5+8+13,len(ans))
	def testSENVDES1(self):
		ans= remainingRequirements([], "College of Environmental Design", 'Sustainable Environmental Design')
		self.assertEqual(5+8+17,len(ans))

class TestHaas(TestCase):
	def testUGBA1(self):
		ans= remainingRequirements([], "Haas School of Business", 'Business Administration')
		self.assertEqual(5+18,len(ans))

class TestNaturalResources(TestCase):
	def testSE1(self):
		self.assertEqual(1,1)

class TestBreadth(TestCase):
	def testBreadth1(self):
		self.assertEqual(7,len(sevenBreadth([])))
	def testBreadth2(self):
		temp=sevenBreadth([])
		self.assertTrue(not (temp[0]['reqCompleted']))
		self.assertTrue(not (temp[1]['reqCompleted']))
		self.assertTrue(not (temp[2]['reqCompleted']))
		self.assertTrue(not (temp[3]['reqCompleted']))
		self.assertTrue(not (temp[4]['reqCompleted']))
		self.assertTrue(not (temp[5]['reqCompleted']))
		self.assertTrue(not (temp[6]['reqCompleted']))
	def testBreadth3(self):
		temp=sevenBreadth(['AFRICAM.4A'])
		for i in range(7):
			if ('Art' in temp[i]['reqName']):
				self.assertTrue (temp[i]['reqCompleted'])
			else:
				self.assertTrue(not (temp[i]['reqCompleted']))
	def testBreadth4(self):
		temp=sevenBreadth(['AFRICAM.4A','AFRICAM.5A'])
		for i in range(7):
			if ('Art' in temp[i]['reqName'] )or('Historical' in temp[i]['reqName'] ):
				self.assertTrue (temp[i]['reqCompleted'])
			else:
				self.assertTrue(not (temp[i]['reqCompleted']))
	def testBreadth5(self):
		temp=sevenBreadth(['AFRICAM.4A','AFRICAM.5A','ANTHRO.1','AFRICAM.4B','BUDDHST.39A','ANTHRO.131','AFRICAM.5B'])
		for i in range(7):
			self.assertTrue (temp[i]['reqCompleted'])
