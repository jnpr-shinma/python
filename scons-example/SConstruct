env = Environment()
if ARGUMENTS.get('VERBOSE') != '1':
    env['CCCOMSTR'] = "Compiling $TARGET"
    env['LINKCOMSTR'] = "Linking $TARGET"
env.Program('hello.c')