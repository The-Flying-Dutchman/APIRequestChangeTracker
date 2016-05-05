from tracker import *
from tracker.views.login_view import *
from tracker.services.crawler import request_update_thread

if __name__ == '__main__':
    app.run()
    # request_update_thread.start()
    # request_update_thread.join()

