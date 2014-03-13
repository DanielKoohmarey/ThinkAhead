## Import the python xUnit framework
from django.test import TestCase
from darsplus.requirementscode import *

class TestRequirements(unittest.TestCase):
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
		
class TestUniversity(unittest.TestCase):
	def testAC1(self):
		ans= remainingRequirements([], 'Engineering', 'EECS')
		self.assertTrue( not ans[0]['reqCompleted'])
	def testAC2(self):
		ans= remainingRequirements(['GWS.100AC'], 'Engineering', 'EECS')
		self.assertTrue( ans[0]['reqCompleted'])
	def testAC3(self):
		ans= remainingRequirements(['ELENG.40','GWS.100AC'], 'Engineering', 'EECS')
		self.assertTrue( ans[0]['reqCompleted'])
	def testUnits1(self):
		ans= remainingRequirements([], 'Engineering', 'EECS')
		self.assertTrue( not ans[1]['reqCompleted'])
	def testUnits1(self):
		ans= remainingRequirements(['ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20','ELENG.20'], 'Engineering', 'EECS')
		self.assertTrue(ans[1]['reqCompleted'])

class TestEngineering(unittest.TestCase):
	def testReadComp1(self):
		ans= remainingRequirements([], 'Engineering', 'EECS')
		self.assertTrue( not ans[5]['reqCompleted'])
	def testReadComp2(self):
		ans= remainingRequirements(['ENGLISH.R1A'], 'Engineering', 'EECS')
		self.assertTrue( not ans[5]['reqCompleted'])
		self.assertIn('You have completed R1A',ans[5]['reqDescription'])
	def testReadComp3(self):
		ans= remainingRequirements(['ENGLISH.R1B'], 'Engineering', 'EECS')
		self.assertTrue( not ans[5]['reqCompleted'])
		self.assertIn('You have completed R1B',ans[5]['reqDescription'])
	def testReadComp4(self):
		ans= remainingRequirements(['ENGLISH.R1B','ENGLISH.R1A'], 'Engineering', 'EECS')
		self.assertTrue(ans[5]['reqCompleted'])
	def testEECS1(self):
		ans= remainingRequirements([], 'Engineering', 'EECS')
		self.assertEqual(23,len(ans))
	def testEECS2(self):
		ans= remainingRequirements([], 'Engineering', 'EECS')
		self.assertTrue( not ans[14]['reqCompleted'])
		self.assertIn('You have only taken 0',ans[14]['reqDescription'])
	def testEECS3(self):
		ans= remainingRequirements(['ELENG.40','ELENG.40','ELENG.40','COMPSCI.61A','COMPSCI.61A','COMPSCI.61A'], 'Engineering', 'EECS')
		self.assertTrue(not ans[14]['reqCompleted'])
		self.assertIn('You have only taken 0',ans[14]['reqDescription'])
	def testEECS4(self):
		ans= remainingRequirements(['ELENG.140','ELENG.140','ELENG.140','COMPSCI.161A','COMPSCI.161A','COMPSCI.161A'], 'Engineering', 'EECS')
		self.assertTrue(ans[14]['reqCompleted'])
	def testBIOENG1(self):
		ans= remainingRequirements([], 'Engineering', 'BIOENG')
		self.assertEqual(5+2+20,len(ans))
	def testBIOENG2(self):
		ans= remainingRequirements([], 'Engineering', 'BIOENG')
		self.assertTrue(not ans[9]['reqCompleted'])
	def testBIOENG3(self):
		ans= remainingRequirements(['CHEM.1A'], 'Engineering', 'BIOENG')
		self.assertTrue(not ans[9]['reqCompleted'])
	def testBIOENG4(self):
		ans= remainingRequirements(['CHEM.1AL'], 'Engineering', 'BIOENG')
		self.assertTrue(not ans[9]['reqCompleted'])
	def testBIOENG5(self):
		ans= remainingRequirements(['CHEM.1AL', 'CHEM.1A'], 'Engineering', 'BIOENG')
		self.assertTrue(ans[9]['reqCompleted'])
	def testBIOENG6(self):
		ans= remainingRequirements(['CHEM.4A'], 'Engineering', 'BIOENG')
		self.assertTrue(ans[9]['reqCompleted'])
	def testBIOENG7(self):
		ans= remainingRequirements([], 'Engineering', 'BIOENG')
		self.assertTrue(not ans[10]['reqCompleted'])
	def testBIOENG8(self):
		ans= remainingRequirements(['CHEM.3A'], 'Engineering', 'BIOENG')
		self.assertTrue(not ans[10]['reqCompleted'])
	def testBIOENG9(self):
		ans= remainingRequirements(['CHEM.3AL'], 'Engineering', 'BIOENG')
		self.assertTrue(not ans[10]['reqCompleted'])
	def testBIOENG10(self):
		ans= remainingRequirements(['CHEM.3AL', 'CHEM.3A'], 'Engineering', 'BIOENG')
		self.assertTrue(ans[10]['reqCompleted'])
	def testBIOENG11(self):
		ans= remainingRequirements(['CHEM.112A'], 'Engineering', 'BIOENG')
		self.assertTrue(ans[10]['reqCompleted'])
	def testCIVENG1(self):
		ans= remainingRequirements([], 'Engineering', 'CIVENG')
		self.assertEqual(5+2+21,len(ans))
	def testCOENG1(self):
		ans= remainingRequirements([], 'Engineering', 'COENG')
		self.assertEqual(5+2+20,len(ans))
	def testCOENG2(self):
		ans= remainingRequirements(['BIOENG.153', 'ELENG.100','PHYSICS.110A','ENGIN.120'], 'Engineering', 'COENG')
		self.assertTrue(ans[21]['reqCompleted'])
	def testCOENG3(self):
		ans= remainingRequirements(['BIOENG.153', 'ELENG.100','PHYSICS.110A'], 'Engineering', 'COENG')
		self.assertTrue(not ans[21]['reqCompleted'])
	def testCOENG4(self):
		ans= remainingRequirements(['BIOENG.153', 'ELENG.100','PHYSICS.110A','ELENG.120'], 'Engineering', 'COENG')
		self.assertTrue(not ans[21]['reqCompleted'])
	def testENENG1(self):
		ans= remainingRequirements([], 'Engineering', 'ENENG')
		self.assertEqual(5+2+24,len(ans))
	def testENENG2(self):
		ans= remainingRequirements(['CIVENG.11','CIVENG.70'], 'Engineering', 'ENENG')
		self.assertTrue(not ans[15]['reqCompleted'])
	def testENENG3(self):
		ans= remainingRequirements(['ELENG.40','CIVENG.70'], 'Engineering', 'ENENG')
		self.assertTrue(ans[15]['reqCompleted'])
	def testENENG4(self):
		ans= remainingRequirements(['ELENG.40','ENGIN.45'], 'Engineering', 'ENENG')
		self.assertTrue(ans[15]['reqCompleted'])
	def testENGMS1(self):
		ans= remainingRequirements([], 'Engineering', 'ENGMS')
		self.assertEqual(5+2+16,len(ans))
	def testENGMS2(self):
		ans= remainingRequirements(['COMPSCI.61A','ENGIN.7','ENGIN.177','COMPSCI.61B'], 'Engineering', 'ENGMS')
		self.assertTrue(ans[12]['reqCompleted'])
	def testENGMS3(self):
		ans= remainingRequirements(['COMPSCI.61A','ENGIN.7','COMPSCI.61B'], 'Engineering', 'ENGMS')
		self.assertTrue(not ans[12]['reqCompleted'])
	def testENGMS4(self):
		ans= remainingRequirements(['COMPSCI.61A','ENGIN.177','COMPSCI.61B'], 'Engineering', 'ENGMS')
		self.assertTrue(not ans[12]['reqCompleted'])
	def testENGMS5(self):
		ans= remainingRequirements(['COMPSCI.61C','COMPSCI.70'], 'Engineering', 'ENGMS')
		self.assertTrue(ans[12]['reqCompleted'])
	def testENGP1(self):
		ans= remainingRequirements([], 'Engineering', 'ENGP')
		self.assertEqual(5+2+21,len(ans))
	def testINDENG1(self):
		ans= remainingRequirements([], 'Engineering', 'INDENG')
		self.assertEqual(5+2+18,len(ans))
	def testMATSCI1(self):
		ans= remainingRequirements([], 'Engineering', 'MATSCI')
		self.assertEqual(5+2+23,len(ans))
	def testMECENG1(self):
		ans= remainingRequirements([], 'Engineering', 'MECENG')
		self.assertEqual(5+2+24,len(ans))
	def testNUCENG1(self):
		ans= remainingRequirements([], 'Engineering', 'NUCENG')
		self.assertEqual(5+2+19,len(ans))
	def testBIOMATSCI1(self):
		ans= remainingRequirements([], 'Engineering', 'BIOMATSCI')
		self.assertEqual(5+2+28,len(ans))
	def testEECSMATSCI1(self):
		ans= remainingRequirements([], 'Engineering', 'EECSMATSCI')
		self.assertEqual(5+2+26,len(ans))
	def testEECSNUCENG1(self):
		ans= remainingRequirements([], 'Engineering', 'EECSNUCENG')
		self.assertEqual(5+2+24,len(ans))
	def testMATNUCENG1(self):
		ans= remainingRequirements([], 'Engineering', 'MATNUCENG')
		self.assertEqual(5+2+27,len(ans))
	def testMECNUCENG1(self):
		ans= remainingRequirements([], 'Engineering', 'MECNUCENG')
		self.assertEqual(5+2+27,len(ans))
	def testMATMECENG1(self):
		ans= remainingRequirements([], 'Engineering', 'MATMECENG')
		self.assertEqual(5+2+31,len(ans))


class TestChem(unittest.TestCase):
	def testBSCHEM1(self):
		self.assertEqual(1,1)
