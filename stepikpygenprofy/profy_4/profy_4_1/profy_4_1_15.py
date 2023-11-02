import sys

[sys.stdout.write(line) for line in sys.stdin if not line.lstrip().startswith('#')]
