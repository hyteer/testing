from locust import HttpLocust, TaskSet, events, task
import random, traceback

counter = 0

counter_start = 0
counter_case = 0

master_counter_start = 0
master_counter_case = 0

counter_success = 0
total_errors = 0


def on_request_success(request_type, name, response_time, response_length):
    print 'Type: %s, Name: %s, Time: %fms, Response Length: %d' % \
            (request_type, name, response_time, response_length)

def on_request_failure(request_type, name, response_time, exception):
    print 'Type: %s, Name: %s, Time: %fms, Reason: %r' % \
            (request_type, name, response_time, exception)

def on_locust_error(locust_instance, exception, tb):
    print "%r, %s, %s" % (locust_instance, exception, "".join(traceback.format_tb(tb)))

def on_hatch_complete(user_count):
    print "Haha, Locust have generate %d users" % user_count

def on_quitting():
    print "Locust is quiting"

def on_locust_start_hatching():
    print "YT, start hatching..."

def on_locust_stop_hatching():
    print "YT, stop hatching..."

events.request_success += on_request_success
events.request_failure += on_request_failure
events.locust_error += on_locust_error
events.hatch_complete += on_hatch_complete
events.quitting += on_quitting
events.locust_start_hatching += on_locust_start_hatching
events.locust_stop_hatching += on_locust_stop_hatching


class UserTask(TaskSet):

# Counters

    def count_total(self):
        global counter
        counter += 1

    def count_success(self):
        global counter_success
        counter_success += 1


# Tasks to be tested...

    @task(5)
    def job1(self):
        with self.client.get('/', catch_response = True) as r:
            self.count_total()
            if random.choice([0, 1]):
                r.success()
                self.count_success()
            else:
                r.failure('0')
    '''
    @task(1)
    def job2(self):
        raise Exception("Mars Loo's test")
    '''



class User(HttpLocust):
    task_set = UserTask
    min_wait = 3000
    max_wait = 5000
    host = 'http://www.baidu.com'