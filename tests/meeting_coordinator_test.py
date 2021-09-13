from meeting_coordinator import MeetingCoordinator
import datetime
import unittest


class TestSum(unittest.TestCase):
    sample_data = [
        {
            'name': 'Betty',
            'meetings': [
                {
                    'startTime': '2021-03-10T08:55:39+00:00',
                    'endTime': '2021-03-10T09:15:39+00:00',
                    'subject': 'Meeting 1'
                },
                {
                    'startTime': '2021-03-10T09:55:39+00:00',
                    'endTime': '2021-03-10T10:15:39+00:00',
                    'subject': 'Meeting 2'
                },
                {
                    'startTime': '2021-03-10T11:55:39+00:00',
                    'endTime': '2021-03-10T12:15:39+00:00',
                    'subject': 'Meeting 3'
                }
            ]
        },
        {
            'name': 'John',
            'meetings': [
                {
                    'startTime': '2021-03-10T08:15:39+00:00',
                    'endTime': '2021-03-10T09:55:39+00:00',
                    'subject': 'Meeting a'
                },
                {
                    'startTime': '2021-03-10T10:15:39+00:00',
                    'endTime': '2021-03-10T10:55:39+00:00',
                    'subject': 'Meeting b'
                },
                {
                    'startTime': '2021-03-10T11:15:39+00:00',
                    'endTime': '2021-03-10T12:55:39+00:00',
                    'subject': 'Meeting c'
                }
            ]
        }
    ]
    meeting_coordinator = MeetingCoordinator(sample_data)

    def test_get_all_meetings(self):
        result = [(datetime.datetime(2021, 3, 10, 8, 55, 38, tzinfo=datetime.timezone.utc),
                   datetime.datetime(2021, 3, 10, 9, 15, 40, tzinfo=datetime.timezone.utc)), (
                      datetime.datetime(2021, 3, 10, 9, 55, 38, tzinfo=datetime.timezone.utc),
                      datetime.datetime(2021, 3, 10, 10, 15, 40, tzinfo=datetime.timezone.utc)), (
                      datetime.datetime(2021, 3, 10, 11, 55, 38, tzinfo=datetime.timezone.utc),
                      datetime.datetime(2021, 3, 10, 12, 15, 40, tzinfo=datetime.timezone.utc)), (
                      datetime.datetime(2021, 3, 10, 8, 15, 38, tzinfo=datetime.timezone.utc),
                      datetime.datetime(2021, 3, 10, 9, 55, 40, tzinfo=datetime.timezone.utc)), (
                      datetime.datetime(2021, 3, 10, 10, 15, 38, tzinfo=datetime.timezone.utc),
                      datetime.datetime(2021, 3, 10, 10, 55, 40, tzinfo=datetime.timezone.utc)), (
                      datetime.datetime(2021, 3, 10, 11, 15, 38, tzinfo=datetime.timezone.utc),
                      datetime.datetime(2021, 3, 10, 12, 55, 40, tzinfo=datetime.timezone.utc))]

        self.assertEqual(self.meeting_coordinator.all_meetings, result)

    def test_calculate_availability_times(self):
        result = [{'endTime': datetime.datetime(2021, 3, 10, 8, 15, 38, tzinfo=datetime.timezone.utc),
                   'startTime': datetime.datetime(2021, 3, 10, 0, 0, tzinfo=datetime.timezone.utc)},
                  {'endTime': datetime.datetime(2021, 3, 10, 11, 15, 38, tzinfo=datetime.timezone.utc),
                   'startTime': datetime.datetime(2021, 3, 10, 10, 55, 40, tzinfo=datetime.timezone.utc)},
                  {'endTime': datetime.datetime(2021, 3, 10, 23, 59, 59, tzinfo=datetime.timezone.utc),
                   'startTime': datetime.datetime(2021, 3, 10, 12, 55, 40, tzinfo=datetime.timezone.utc)}]
        self.assertEqual(self.meeting_coordinator.available_times, result)


if __name__ == '__main__':
    unittest.main()
