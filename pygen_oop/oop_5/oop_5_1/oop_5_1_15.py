class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, program_name: str = 'GenerationPy', environment: str = 'release', loglevel: str = 'verbose',
                 version: str = '1.0.0'):
        self.program_name, self.environment, self.loglevel, self.version = program_name, environment, loglevel, version
