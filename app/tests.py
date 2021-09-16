from django.http import response
from django.shortcuts import render
from django.test import SimpleTestCase

# Create your tests here.

class TestNearHundred(SimpleTestCase):
    def test_nearhundred90(self):
        response = self.client.get("/near-hundred/90")
        self.assertContains(response, "True!")

    def test_nearhundred50(self):
        response = self.client.get("/near-hundred/50")
        self.assertContains(response, "False!")

    def test_nearhundred190(self):
        response = self.client.get("/near-hundred/190")
        self.assertContains(response, "True!")


class TestStringExplosion(SimpleTestCase):
    def test_strplode_code(self):
        response = self.client.get("/string-splosion/code")
        self.assertContains(response, "ccocodcode")

    def test_strplode_taco(self):
        response = self.client.get("/string-splosion/taco")
        self.assertContains(response, "ttatactaco")
    
    def test_strplode_takeguchi(self):
        response = self.client.get('/string-splosion/takeguchi')
        self.assertContains(response, "ttataktaketakegtakegutakeguctakeguchtakeguchi")


class TestCatDog(SimpleTestCase):
    def test_catdog_catdog(self):
        response = self.client.get("/cat-dog/catdog")
        self.assertContains(response, "True")
    
    def test_catdog_catcatdog(self):
        response = self.client.get("/cat-dog/catcatdog")
        self.assertContains(response, "False")

    def test_catdog_catcatcatdogdogdog(self):
        response = self.client.get("/cat-dog/catcatcatdogdogdog")
        self.assertContains(response, "True")


class TestLoneSum(SimpleTestCase):
    def test_lonesum_123(self):
        response = self.client.get("/lone-sum/1/2/3")
        self.assertContains(response, "6")
    
    def test_lonesum_777(self):
        response = self.client.get("/lone-sum/7/7/7")
        self.assertContains(response, "0")

    def test_lonesum_696(self):
        response = self.client.get("/lone-sum/6/9/6")
        self.assertContains(response, "9")