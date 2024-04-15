#!/bin/bash
. /usr/share/beakerlib/beakerlib.sh || exit 1

rlJournalStart
	rlPhaseStartSetup
		rlRun "pushd data" 0 "Move to the data directory"
		rlRun "set -o pipefail"
	rlPhaseEnd

# Checks for good and full are identical
for type in good; do
	rlPhaseStartTest "Check ${type} plans"
		rlRun -s "tmt lint plans --disable-check C000 --disable-check C001 /${type}" 0 "Check plan lint"
		rlAssertNotGrep "^warn:" $rlRun_LOG -E
		rlRun -s "tmt plans show /${type}" 0 "Get all /${type} plans"
		# Check schemas
#		rlAssertNotGrep "warn: .* is not valid under any of the given schemas" $rlRun_LOG -E
		# Check for any failing messages
		rlAssertNotGrep "fail:" $rlRun_LOG -E
		# Other catch all
#		rlAssertNotGrep "warn:" $rlRun_LOG
	rlPhaseEnd
done

	rlPhaseStartCleanup
		rlRun 'popd'
	rlPhaseEnd
rlJournalEnd
