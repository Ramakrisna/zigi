from datetime import timedelta
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

        self._get_all_meetings()
        if self.all_meetings:
            self._get_first_and_last_days_in_range()
            self._calculate_availability_times()
        else:
            print('No meetings were provided, all dates are open')

    def _get_all_meetings(self):
        """
        This method goes over every person in the list of people and extracts all the meetings they have into a list of
        tuples of datetimes that mark the start and end of each meeting, and save it to the class argument
        'all_meetings_in_timestamps'.
        """
        self.all_meetings = [(ciso8601.parse_datetime(meeting['startTime']),
                              ciso8601.parse_datetime(meeting['endTime'])) for person in
                             self.scheduled_meetings for meeting in person['meetings']]

    def _get_first_and_last_days_in_range(self):
        """
        This method gets the beginning of the first day and end of the last day of the range.
        """
        all_times = list(itertools.chain.from_iterable(self.all_meetings))
        first_day = min(all_times)
        last_day = max(all_times)
        self.starting_day = first_day.replace(hour=0, minute=0, second=0)
        self.ending_day = last_day.replace(hour=23, minute=59, second=59)

    def _calculate_availability_times(self):
        """
        This method goes over each date in the 'all_meetings' list, subtracts all the meeting times and then inputs it
        into the 'available_times' argument.
        """
        filtered_meetings_ranges = Utilities.filter_and_organize_ranges(self.all_meetings)
        ranges = Utilities.filter_sub_ranges_from_whole_range((self.starting_day, self.ending_day),
                                                              filtered_meetings_ranges)
        self.available_times = [{'startTime': meeting_availability[0], 'endTime': meeting_availability[1]} for
                                meeting_availability in ranges]
