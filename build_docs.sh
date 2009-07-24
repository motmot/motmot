#!/bin/bash

# abort on error
set -o errexit

VIRTUALENVDIR=PYtest

# activate new virutal environment
source $VIRTUALENVDIR/bin/activate

# check for expected permissions on X server
python -c 'import os; assert os.path.exists("/etc/X2.hosts")'
python -c 'fd = open("/etc/X2.hosts",mode="r"); assert "localhost\n" in fd.readlines()'

# run X server
Xvfb :2 &
# get PID
XVFBPID=$!
echo "Xvfb running in process $XVFBPID"

echo "checking that Xvfb process is running"
sleep 1
python -c "import os; assert os.path.exists(\"/proc/$XVFBPID\")"
echo "PID $XVFBPID seems OK, will continue with building docs"


cd doc

set +o errexit
DISPLAY=":2" ./clean-build-and-upload.sh
RESULT=$?
set -o errexit

# Kill the X server
kill $XVFBPID
wait $XVFBPID

# exit with test results
exit $RESULT

