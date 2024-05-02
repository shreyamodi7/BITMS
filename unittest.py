class Fan:
    def __init__(self,survey_id,name,report_id):
        self.survey_id=survey_id
        self.name = name
        self.report_id = report_id
        #self.appoint=appoint

class fandata:
    def __init__(self):
        self.fans = {}

    def create(self, survey_id, name,report_id):
        if survey_id in self.fans:
            raise ValueError("survey ID already exists")
        self.fans[survey_id] = Fan(survey_id,name,report_id)

    def read(self, survey_id):
        if survey_id not in self.fans:
            raise ValueError("survey ID does not exist")
        return self.fans[survey_id]

    def update(self, survey_id, name=None, report_id=None):
        if survey_id not in self.fans:
            raise ValueError("survey ID does not exist")
        fans = self.fans[survey_id]
        if name:
            fans.name = name
        if report_id:
            fans.report_id = report_id

    def delete(self, survey_id):
        if survey_id not in self.fans:
            raise ValueError("survey ID does not exist")
        del self.fans[survey_id]
    
    def conduct_fan_surveys(self,survey_id,name,report_id):
        if survey_id not in self.fans:
            raise ValueError("survey ID does not exist")
        return self.fans[survey_id]
        if name:
            fans.name = name
        if progress_data:
            fans.report_id = report_id
            
    def generate_fan_engagement_reports(self,report_id):
        if report_id not in self.fans:
            raise ValueError("Report ID does not exist")
        return self.fans[report_id]

# Unit tests
import unittest

class TestFanDatabase(unittest.TestCase):
    def setUp(self):
        self.db = fandata()
        self.db.create(1000, "fan-one", "win")
        self.db.create(1001, "fan-two", "lose")

    def test_create(self):
        self.db.create(1002, "fan-three","win" )
        self.assertIn(1002, self.db.fans)

    def test_read(self):
        athlete = self.db.read(1000)
        self.assertEqual(athlete.name, "fan-one","win")

    def test_update(self):
        self.db.update(1000, name="fans",report_id="lose")
        athlete = self.db.read(1000)
        self.assertEqual(athlete.name, "fans")

    def test_delete(self):
        self.db.delete(1000)
        self.assertNotIn(1000, self.db.fans)
    
    def test_conduct_fan_surveys(self):
        self.db.conduct_fan_surveys(1001,name="fan-two",report_id=None)
        fans=self.db.read(1001)
        self.assertEqual(fans.name, "fan-two")
        
    def test_generate_fan_engagement_reports(self):
        fans=self.db.generate_fan_engagement_reports(1001)
        self.assertEqual(fans.name, "fan-two")
        


if __name__ == '__main__':
    unittest.main(verbosity=8)

