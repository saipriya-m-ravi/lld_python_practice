"""
Lesson 4.3 - Singleton (and why it's usually the wrong tool)

Part A (worked): a classic Singleton via __new__.
Part B (TODO): prove the hidden-coupling danger.
Part C (TODO): refactor to plain constructor injection (DIP style),
                and prove the danger is gone.
"""


# ------------------------------------------------------------------
# PART A -- worked example
# ------------------------------------------------------------------

class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._settings = {}
        return cls._instance

    def set(self, key, value):
        self._settings[key] = value

    def get(self, key):
        return self._settings.get(key)


# ------------------------------------------------------------------
# PART B -- TODO: demonstrate the hidden-coupling problem
#
# Write two functions that never call each other and never share a
# parameter, yet secretly communicate through ConfigManager:
#
def configure_for_module_a():
    ConfigManager().set("timeout", 30)

def read_in_module_b():
    return ConfigManager().get("timeout")
#
# In __main__ (below), call configure_for_module_a(), then call
# read_in_module_b() and print the result. Notice: read_in_module_b's
# SIGNATURE gives you zero indication it depends on anything having
# run before it. That invisibility is exactly what your notes mean by
# "Singletons hide dependencies."
# ------------------------------------------------------------------


# ------------------------------------------------------------------
# PART C -- TODO: refactor away from Singleton
#
# 1. Define a plain Config class -- NO __new__ override, NO _instance,
#    just a normal class with __init__(self): self._settings = {} and
#    the same set()/get() methods as ConfigManager.
#
# 2. Rewrite the two functions to take the config as an explicit
#    parameter instead of reaching for a global:
#       def configure(config: Config):
#           config.set("timeout", 30)
#       def read(config: Config):
#           return config.get("timeout")
#
# 3. In __main__, create ONE Config() instance and pass it to both --
#    same "single shared instance" behavior as the Singleton gave you,
#    but now the dependency is VISIBLE in every function signature.
#
# 4. Prove the real benefit: create a SECOND, completely independent
#    Config() instance and show it does NOT have "timeout" set --
#    (with ConfigManager, there is no way to get a second independent
#    instance at all -- that's exactly the testing problem your notes
#    describe: tests can't isolate themselves from each other).
class Config:
    def __init__(self):
        self._settings = {}
    
    def set(self, key, value):
        self._settings[key] = value

    def get(self, key):
        return self._settings.get(key)

def configure(config: Config):
    config.set("timeout", 30)

def read(config: Config):
    return config.get("timeout")
# ------------------------------------------------------------------


if __name__ == "__main__":
    # Part A demo -- prove it's really a singleton
    c1 = ConfigManager()
    c2 = ConfigManager()
    print("c1 is c2:", c1 is c2)
    c1.set("env", "production")
    print("read via c2:", c2.get("env"))   # set via c1, read via c2 -- same object

    configure_for_module_a()
    print(read_in_module_b())
    # TODO: Part B -- call configure_for_module_a(), then read_in_module_b(), print result

    c11 = Config()
    c12 = Config()
    configure(c11)
    print(read(c11))
    print(read(c12))
    print()
    # TODO: Part C -- build the Config-based version and prove independence
