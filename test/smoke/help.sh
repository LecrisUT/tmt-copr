#!/bin/bash
. /usr/share/beakerlib/beakerlib.sh || exit 1

rlJournalStart
	rlPhaseStartTest "Check plugin help messages"
		rlRun -s "tmt run discover --how copr --help" 0 "Check discover help message"
	rlPhaseEnd
rlJournalEnd
