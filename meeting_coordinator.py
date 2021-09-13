from datetime import datetime, timedelta
from utilities import Utilities
import ciso8601
import itertools


class MeetingCoordinator:
    def __init__(self, scheduled_meetings):
        self.scheduled_meetings = scheduled_meetings
        self.all_meetings = []
        self.available_times = None
        self.starting_day = None
        self.ending_day = None

        self.get_all_meetings()
        self.get_first_and_last_days_in_range()
        self.calculate_availability_times()

    def get_all_meetings(self):
        """
        This method goes over every person in the list of people and extracts all the meetings they have into a list of
        tuples of datetimes that mark the start and end of each meeting, and save it to the class argument
        'all_meetings_in_timestamps'.
        """
        self.all_meetings = [(ciso8601.parse_datetime(meeting['startTime']) - timedelta(seconds=1),
                              ciso8601.parse_datetime(meeting['endTime']) + timedelta(seconds=1)) for person in
                             self.scheduled_meetings for meeting in person['meetings']]

    def get_first_and_last_days_in_range(self):
        """
        This method gets the beginning of the first day and end of the last day of the range.
        """
        all_times = list(itertools.chain.from_iterable(self.all_meetings))
        first_day = min(all_times)
        last_day = max(all_times)
        self.starting_day = first_day.replace(hour=0, minute=0, second=0)
        self.ending_day = last_day.replace(hour=23, minute=59, second=59)

    def calculate_availability_times(self):
        """
        This method goes over each date in the 'all_meetings' list, subtracts all the meeting times and then inputs it
        into the 'available_times' argument.
        """
        ranges = Utilities.multi_range_diff([(self.starting_day, self.ending_day)],
                                            self.all_meetings)
        self.available_times = [{'startTime': datetime.utcfromtimestamp(meeting_availability[0]),
                                 'endTime': datetime.utcfromtimestamp(meeting_availability[1])} for
                                meeting_availability in ranges]
