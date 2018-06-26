class TempTracker(object):

    # Implement methods to track the max, min, mean, and mode
    def __init__(self):
        self.temps = [0] * 111
        self.num_temps = 0
        self.min = 111
        self.max = -1
        self.total = 0
        self.mean = None
        self.max_freq = 0
        self.mode = None


    def insert(self, temp):
        if temp < 0 or temp > 110:
            raise Exception
        self.temps[temp] += 1
        self.num_temps += 1
        if temp < self.min:
            self.min = temp
        if temp > self.max:
            self.max = temp
        self.total += temp
        self.mean = self.total / float(self.num_temps)
        if self.temps[temp] > self.max_freq:
            self.max_freq = self.temps[temp]
            self.mode = temp


    def get_max(self):
        max = self.max
        if max == -1:
            max = None
        return max

    def get_min(self):
        min = self.min
        if min == 111:
            min = None
        return min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode


# Tests
tracker = TempTracker()

tracker.insert(50)
print("after inserting 50, max is, "+str(tracker.get_max()))
print("after inserting 50, min is, "+str(tracker.get_min()))
print("after inserting 50, mean is, "+str(tracker.get_mean()))
print("after inserting 50, mode is, "+str(tracker.get_mode()))

tracker.insert(80)
print("after inserting 80, max is, "+str(tracker.get_max()))
print("after inserting 80, min is, "+str(tracker.get_min()))
print("after inserting 80, mean is, "+str(tracker.get_mean()))
print("after inserting 80, mode is, "+str(tracker.get_mode()))

tracker.insert(80)
print("after inserting 80, max is, "+str(tracker.get_max()))
print("after inserting 80, min is, "+str(tracker.get_min()))
print("after inserting 80, mean is, "+str(tracker.get_mean()))
print("after inserting 80, mode is, "+str(tracker.get_mode()))

tracker.insert(30)
print("after inserting 30, max is, "+str(tracker.get_max()))
print("after inserting 30, min is, "+str(tracker.get_min()))
print("after inserting 30, mean is, "+str(tracker.get_mean()))
print("after inserting 30, mode is, "+str(tracker.get_mode()))