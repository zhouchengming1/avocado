#!/usr/bin/python

from avocado import test
from avocado.core import job
from avocado.core import exceptions


class FailTest(test.Test):

    """
    Functional test for avocado. Straight up fail the test.
    """

    def runTest(self):
        """
        Should fail.
        """
        raise exceptions.TestFail('This test is supposed to fail')


if __name__ == "__main__":
    job.main()
