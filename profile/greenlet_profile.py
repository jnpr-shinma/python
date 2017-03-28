import GreenletProfiler
from gevent_logic import launch

GreenletProfiler.start()

launch()

GreenletProfiler.stop()
stats = GreenletProfiler.get_func_stats()
# stats.print_all()
stats.save('callgrind.greenletprofile', type='callgrind')
