from datetime import datetime, time, timezone
from utilities import Utilities
import ciso8601


class MeetingCoordinator:
    def __init__(self, scheduled_meetings):
        self.scheduled_meetings = scheduled_meetings
        self.all_meetings_in_timestamps = {}
        self.get_all_meetings()
        self.available_times = None
        self.calculate_availability_times()

    def get_all_meetings(self):
        """
        This method goes over every person in the list of people and extracts all the meeting they have into a list of
        dictionaries that are made of the date the meetings are on and a tuple of timestamps that mark the start and end
        of the meeting, and save it to the class argument 'all_meetings_in_timestamps'.
        :return:
        """
        for person in self.scheduled_meetings:
            for meeting in person['meetings']:
                start_time = ciso8601.parse_datetime(meeting['startTime'])
                end_time = ciso8601.parse_datetime(meeting['endTime'])
                meeting_date = start_time.replace(hour=0, minute=0, second=0, microsecond=0)
                if meeting_date not in self.all_meetings_in_timestamps:
                    self.all_meetings_in_timestamps[meeting_date] = []
                self.all_meetings_in_timestamps[meeting_date].append(
                    (int(start_time.timestamp()), int(end_time.timestamp())))

    def calculate_availability_times(self):
        """
        This method go over each date in the 'all_meetings_in_timestamps' dictionary, and gets the starting and ending
         seconds and create the main time range to subtract the meetings time from.
        :return:
        """
        for meeting_date in self.all_meetings_in_timestamps:
            start_second = int(datetime.combine(meeting_date, time.min).replace(tzinfo=timezone.utc).timestamp())
            end_second = int(datetime.combine(meeting_date, time.max).replace(tzinfo=timezone.utc).timestamp())
            ranges_timestamp = Utilities.multi_range_diff([(start_second, end_second)],
                                                          self.all_meetings_in_timestamps[meeting_date])
            self.available_times = [{'startTime': datetime.utcfromtimestamp(meeting_availability[0]),
                                     'endTime': datetime.utcfromtimestamp(meeting_availability[1])} for
                                    meeting_availability in ranges_timestamp]
