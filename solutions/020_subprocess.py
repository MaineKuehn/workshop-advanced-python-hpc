import subprocess

cat = subprocess.Popen(['cat', __file__], stdout=subprocess.PIPE)
counter = subprocess.Popen(['wc', '-l'], stdin=cat.stdout)

for process in (cat, counter):
    if process.wait() != 0:
        raise RuntimeError('process %r exited with %d' % (' '.join(process.args), process.wait()))
