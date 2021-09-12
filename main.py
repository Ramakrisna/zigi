from meeting_coordinator import MeetingCoordinator

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
print(meeting_coordinator.available_times)
