# Header File: data.py
# Analytical Module.
# History:
# Date    Programmer   - Description
# ---------- ---------- ----------------------------
# 05/04/2021     Ricardo Josue Colindres      - Created
from datetime import datetime


class Data:

    #! ******************************** Properties *******************************

    def __init__(self, data_list, habit_data):

        self.data_list = data_list
        self.habit_name = habit_data[0]
        self.habit_frequency = habit_data[1]

        # Remove habit name, frecuency, and today's observations if not completed yet.
        # Today's observation is removed because the 24-hour period
        # to complete the habit is not over yet
        self.streaks = []
        if len(self.data_list) > 2:
            if self.data_list[-1][1] == 0:
                self.streaks = data_list[2:-1]
            else:
                self.streaks = data_list[2:]

        if not self.streaks:
            self.streaks_len = len(self.streaks)
        self.now = datetime.now()
        self.current_year = self.now.strftime("%Y")
        self.current_week = self.now.strftime("%V")
        self.habit_data = habit_data
        self.habit_days = habit_data[2]

        # Last day observed in Data (name)
        if len(self.streaks) > 0:
            self.last_day_observed = (
                self.current_year + ' ' + str(self.streaks[-1][0]))
            self.last_day_observed = datetime.strptime(
                self.last_day_observed, '%Y %j')
            self.last_day_observed = self.last_day_observed.strftime('%A')
            self.last_day_number = self.streaks[-1][0]
        else:
            self.last_day_observed = None
            self.last_day_number = None

        # Last day observed in Data (number)

        # Number of days observed in Data
        self.number_days = len(data_list[2:])

    #! ******************************** Methods *******************************

    def active_streak(self):
        ''' This method analysis the object's properties: self.streaks, self.frequency, 
        and self.habit_days. Each list within self.streaks must contain two elements. 
        Index 0 of each list should contain the day of the year the habit was observed. 
        If the habit was NOT completed index 1 will reflet 0 and if completed a 1. 
        The method iterates backwards and breaks when a sub-list reflects a day 
        that the habit was NOT completed. The method also analyses the number of complete
        week in which the streak has remained perfect. The habit must have been completed
        the number of times defiend in the fequency parameter for the week to count.  
        Then method returns a tuple with two values: The first value is the number of days \
        the habit has been continously completed starting at last day the habit has currently 
        been observed and considering the pre-defined frequency. The  the number of weeks the habit has have a perfect streak. '''

        current_streak = 0
        num_weeks = 0
        observed_day = None
        next_day = self.last_day_observed
        next_day_idx = None
        previous_day = self.last_day_number
        weeks_observed = []

        if len(self.streaks) == 0:
            current_streak = 0
            num_weeks = 0

        else:
            # no possible streak in data
            no_possible_streak = False
            if self.streaks[-1][1] == 0:
                no_possible_streak = True

            # calculate streak and perfect weeks
            if no_possible_streak == False:

                for v in reversed(self.streaks):
                    completion_status = v[1]
                    observed_time = self.current_year + ' ' + str(v[0])
                    observed_time = datetime.strptime(observed_time, '%Y %j')
                    observed_day = observed_time.strftime('%A')
                    observed_week = int(observed_time.strftime('%V'))

                    # prevent data gap of 7 days as false reading
                    time_gap = previous_day - v[0]

                    if time_gap <= 7:
                        if completion_status == 1:
                            if observed_day == next_day:
                                next_day_idx = self.habit_days.index(
                                    observed_day)
                                if next_day_idx != 0:
                                    next_day_idx -= 1
                                    next_day = self.habit_days[next_day_idx]
                                    current_streak += 1
                                    weeks_observed.append(observed_week)
                                    previous_day = v[0]

                                else:
                                    next_day = self.habit_days[-1]
                                    current_streak += 1
                                    weeks_observed.append(observed_week)
                                    previous_day = v[0]
                            else:
                                break
                        else:
                            break
                    else:
                        break

                    # Check and correct if streak goes beyond a single year
                    if v[0] == 1:
                        self.current_year = str(int(self.current_year) - 1)

                # Check if last and first week observed have the same number
                # data points as the frequency parameter.
                last_week = weeks_observed[0]
                first_week = weeks_observed[-1]

                if weeks_observed.count(last_week) == self.habit_frequency:
                    last_week += 1

                if weeks_observed.count(first_week) != self.habit_frequency:
                    first_week += 1

                num_weeks = last_week - first_week

                if num_weeks < 0:
                    num_weeks = 0

        # Reset year (in case it was changed)
        self.current_year = self.now.strftime("%Y")
        return (current_streak, num_weeks)

    def probability(self):
        '''
        This methods return a tuple with two values. The first is a string
        with the most likely days for the habit completion and the second 
        is a string with least likely days for the habit's completion.
        '''

        mapped_day = {'Monday': 'Mon', 'Tuesday': 'Tue', 'Wednesday': 'Wed',
                      'Thursday': 'Thu', 'Friday': 'Fri', 'Saturday': 'Sat',
                      'Sunday': 'Sun'}

        # Get all days the habit was completed and
        # all day the habit was not completed
        none_days_observed = []
        for d in self.streaks:
            observed_time = self.current_year + ' ' + str(d[0])
            observed_time = datetime.strptime(observed_time, '%Y %j')
            observed_day = observed_time.strftime('%A')

            if d[1] == 0:
                none_days_observed.append(observed_day)

            # Check and correct if streak goes beyond a single year
            if d[0] == 1:
                self.current_year = str(int(self.current_year) - 1)

        # Get less likely days for the habit's completion
        none_days_probability = []
        highest_none_probability = 0
        runs = 0
        for h in self.habit_days:
            probability = none_days_observed.count(h)
            if runs == 0:
                highest_none_probability = probability
            else:
                if probability > highest_none_probability:
                    highest_none_probability = probability

            none_days_probability.append((h, probability))
            runs += 1

        # Define and Format Lowest Posible Days
        if highest_none_probability != 0:
            lowest_probable_days = [x[0]
                                    for x in none_days_probability if x[1] == highest_none_probability]
            if len(lowest_probable_days) == 1:
                lowest_probable_days = lowest_probable_days[0]
            else:
                lowest_probable_days = [newday for day in lowest_probable_days
                                        for oldday, newday in mapped_day.items() if oldday == day]
                lowest_probable_days = ', '.join(lowest_probable_days)

        else:
            lowest_probable_days = None

        # Get most likely days for the habit's completion

        lowest_none_probability = 0
        runs = 0

        for x in none_days_probability:
            if runs == 0:
                lowest_none_probability = x[1]
            else:
                if lowest_none_probability > x[1]:
                    lowest_none_probability = x[1]

        # Define and Format Highest Posible Days
        higest_probable_days = [x[0]
                                for x in none_days_probability if x[1] == lowest_none_probability]

        if len(higest_probable_days) == 1:
            higest_probable_days = higest_probable_days[0]
        else:
            higest_probable_days = [newday for day in higest_probable_days
                                    for oldday, newday in mapped_day.items() if oldday == day]
            higest_probable_days = ', '.join(higest_probable_days)

        # Reset year (in case it was changed)
        self.current_year = self.now.strftime("%Y")
        return (higest_probable_days, lowest_probable_days)


class General:

    #! ******************************** Properties *******************************

    def __init__(self, user_habits):
        self.user_habits = user_habits

    #! ******************************** Methods *******************************

    def highest_lowest(self):
        '''This method return the highest and lowest observed streaks in user_habits '''

        highest_observed_value = 0
        highest_observed_name = ''
        lowest_observed_value = 0
        lowest_observed_name = ''
        runs = 0

        for habit in self.user_habits:

            if runs == 0:
                highest_observed_value = habit[4]
                lowest_observed_value = habit[4]
                highest_observed_name = habit[0]
                lowest_observed_name = habit[0]
            else:
                if highest_observed_value < habit[4]:
                    highest_observed_value = habit[4]
                    highest_observed_name = habit[0]

                if lowest_observed_value > habit[4]:
                    lowest_observed_value = habit[4]
                    lowest_observed_name = habit[0]

            runs += 1

        return ((highest_observed_name, highest_observed_value), (lowest_observed_name, lowest_observed_value))


class ClockedSession:

    #! ******************************** Properties *******************************

    def __init__(self, session_id, sessions_data):
        self.session_id = session_id
        self.sessions_data = sessions_data
        self.data_for_analisis = None
        for d in self.sessions_data:
            if d[0] == self.session_id:
                self.data_for_analisis = d[1:]
                break

    #! ******************************** Methods *******************************

    def listed_data(self):
        ''' This method returns a lists of all fields to display for any
        specific clocked session'''

        habits_in_session = []
        time_elpsed = 0

        for moment in self.data_for_analisis:
            if not habits_in_session:
                if moment[0] == 1:
                    habits_in_session.append([moment[3], moment[2], 1, 1])
                else:
                    habits_in_session.append([moment[3], moment[2], 1, 0])
            else:
                does_exist = False
                for i in habits_in_session:
                    if i[0] == moment[3]:
                        does_exist = True
                        if moment[0] == 1:
                            i[2] += 1
                            i[3] += 1
                        else:
                            i[2] += 1
                        break
                if does_exist == False:
                    if moment[0] == 1:
                        habits_in_session.append([moment[3], moment[2], 1, 1])
                    else:
                        habits_in_session.append([moment[3], moment[2], 1, 0])

            if moment[1] > time_elpsed:
                time_elpsed = moment[1]

        time_elpsed = int(time_elpsed / 60)
        time_elpsed = str(time_elpsed) + 'min.'

        for his in habits_in_session:
            his[1] = int(his[1] / 60)
            his[1] = str(his[1]) + 'min.'
            his.insert(2, time_elpsed)

        return habits_in_session
