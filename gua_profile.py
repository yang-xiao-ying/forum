import app
from routes.index import profile
import cProfile
from pstats import Stats


def profile_request(path, cookie, f):
    a = app.configured_app()
    pr = cProfile.Profile()
    headers = {'Cookie': cookie}

    with a.test_request_context(path, headers=headers):
        pr.enable()
        f()

        pr.disable()

    pr.create_stats()
    s = Stats(pr).sort_stats('cumulative')
    s.dump_stats('miao_profile.pstat')

    s.print_stats('.*web19.*')


if __name__ == '__main__':
    path = '/profile'
    cookie = 'session=eyJ1c2VyX2lkIjoyfQ.XWPM5g.3acfbweSNyouMk7BM91Zq-jdy-Y'
    profile_request(path, cookie, profile)
