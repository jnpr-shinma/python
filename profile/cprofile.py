import lsprofcalltree
import cProfile
from gevent_logic import launch


profile = cProfile.Profile()
profile.enable()
launch()
profile.disable()
stats = lsprofcalltree.KCacheGrind(profile)
stats.output(open('callgrind.profile', 'w'))