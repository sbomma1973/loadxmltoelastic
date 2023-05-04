loadfromxml/config.yml                                                                              000755  000765  000024  00000000616 14424571712 017061  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         request_url: "https://sdsfeeder.isd.lacounty.gov/FeederFiles/bos-sop-supdocs---xml-prod---oracle.xml"
url: "https://test-4f3018.es.us-central1.gcp.cloud.es.io"
cloud_id: "Workshop_ML:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyQ0Y2U0N2YwYjJlZGM0NzBiYWE2Y2ZkY2Q4MjQ5Mjg1OCQ4YWNiYTRmN2RhODE0N2E4YWM3ZmMxN2MxOThmNGVkMw=="
username: "elastic"
password: "BnJBH5vptVtudn0tMZhfAuZy"
index_name: "test_index"                                                                                                                  loadfromxml/loadXMLtoElastic.py                                                                     000644  000765  000024  00000003566 14424571664 020625  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         #loadxmlto elastic reads multiline xml from an url response
#built for a customer to insert documents into elastic directly from an Url scrape
#Satish Bomma
#05.03.2023


import requests
from datetime import datetime
import json
import yaml
import logging
import xmltodict
import xml.etree.ElementTree as ET
from elasticsearch import Elasticsearch

#date time setup for the script
log = logging.getLogger("ProcessLog")
log.info('Setting Datetime:')

now = datetime.now();
dt_string = now.strftime("%m%d%Y %H:%M:%S")
logging.info('Executing Ingest Script:', dt_string)

#functions
def read_from_file():
    with open('config.yml') as f:
        data = yaml.load (f, Loader=yaml.FullLoader)
        return data

#function to execute search


def call_get (url):
    print ("call url", url)
    response12 = requests.get(url)
    return response12.text



# Main function to get executed to process rest of the files
if __name__ == '__main__':
    log = logging.getLogger("scriptlog")
    log.info('Setting Datetime:')

    #read config from yaml file.
    data=read_from_file()
    username = data['username']
    password = data['password']
    url = data['url']
    cloud_id1 = data['cloud_id']
    request_url= data['request_url']
    index_name=data['index_name']

    log.info("username:",username)
    log.info ("username:", username)
    log.info ("password:", password)
    log.info ("url:", url)



    es=Elasticsearch(cloud_id=cloud_id1,basic_auth=(username,password))
    print (es.info())

    response1 = call_get(request_url)
    ida=0
    root = ET.fromstring(response1)
    for doc1 in root.findall('document'):
        doc_xml = ET.tostring(doc1)
        python_dict=xmltodict.parse(doc_xml)
        json_string=json.dumps(python_dict)
        ida = ida+1
        print (ida)

        resp = es.index(index=index_name,id=ida,document=json_string)
        print ("-resp-", resp)


    exit(1)


                                                                                                                                          loadfromxml/loadfromxml                                                                             000644  000765  000024  00000002000 14424575163 017326  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         loadfromxml/loadxmltoelastic/                                                                       000755  000765  000024  00000000000 14424573166 020440  5                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         loadfromxml/loadxmltoelastic/.git/                                                                  000755  000765  000024  00000000000 14424573166 021301  5                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         loadfromxml/loadxmltoelastic/.git/config                                                            000644  000765  000024  00000000211 14424573166 022463  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         [core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
                                                                                                                                                                                                                                                                                                                                                                                       loadfromxml/loadxmltoelastic/.git/objects/                                                          000755  000765  000024  00000000000 14424573166 022732  5                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         loadfromxml/loadxmltoelastic/.git/HEAD                                                              000644  000765  000024  00000000027 14424573166 021724  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         ref: refs/heads/master
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         loadfromxml/loadxmltoelastic/.git/info/                                                             000755  000765  000024  00000000000 14424573166 022234  5                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         loadfromxml/loadxmltoelastic/.git/description                                                       000644  000765  000024  00000000111 14424573166 023540  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         Unnamed repository; edit this file 'description' to name the repository.
                                                                                                                                                                                                                                                                                                                                                                                                                                                       loadfromxml/loadxmltoelastic/.git/hooks/                                                            000755  000765  000024  00000000000 14424573166 022424  5                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         loadfromxml/loadxmltoelastic/.git/refs/                                                             000755  000765  000024  00000000000 14424573166 022240  5                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         loadfromxml/loadxmltoelastic/.git/branches/                                                         000755  000765  000024  00000000000 14424573166 023066  5                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         loadfromxml/loadxmltoelastic/.git/refs/heads/                                                       000755  000765  000024  00000000000 14424573166 023324  5                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         loadfromxml/loadxmltoelastic/.git/refs/tags/                                                        000755  000765  000024  00000000000 14424573166 023176  5                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         loadfromxml/loadxmltoelastic/.git/hooks/commit-msg.sample                                           000755  000765  000024  00000001600 14424573166 025703  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         #!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines.

test "" = "$(grep '^Signed-off-by: ' "$1" |
	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
	echo >&2 Duplicate Signed-off-by lines.
	exit 1
}
                                                                                                                                loadfromxml/loadxmltoelastic/.git/hooks/pre-rebase.sample                                           000755  000765  000024  00000011442 14424573166 025661  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         #!/bin/sh
#
# Copyright (c) 2006, 2008 Junio C Hamano
#
# The "pre-rebase" hook is run just before "git rebase" starts doing
# its job, and can prevent the command from running by exiting with
# non-zero status.
#
# The hook is called with the following parameters:
#
# $1 -- the upstream the series was forked from.
# $2 -- the branch being rebased (or empty when rebasing the current branch).
#
# This sample shows how to prevent topic branches that are already
# merged to 'next' branch from getting rebased, because allowing it
# would result in rebasing already published history.

publish=next
basebranch="$1"
if test "$#" = 2
then
	topic="refs/heads/$2"
else
	topic=`git symbolic-ref HEAD` ||
	exit 0 ;# we do not interrupt rebasing detached HEAD
fi

case "$topic" in
refs/heads/??/*)
	;;
*)
	exit 0 ;# we do not interrupt others.
	;;
esac

# Now we are dealing with a topic branch being rebased
# on top of master.  Is it OK to rebase it?

# Does the topic really exist?
git show-ref -q "$topic" || {
	echo >&2 "No such branch $topic"
	exit 1
}

# Is topic fully merged to master?
not_in_master=`git rev-list --pretty=oneline ^master "$topic"`
if test -z "$not_in_master"
then
	echo >&2 "$topic is fully merged to master; better remove it."
	exit 1 ;# we could allow it, but there is no point.
fi

# Is topic ever merged to next?  If so you should not be rebasing it.
only_next_1=`git rev-list ^master "^$topic" ${publish} | sort`
only_next_2=`git rev-list ^master           ${publish} | sort`
if test "$only_next_1" = "$only_next_2"
then
	not_in_topic=`git rev-list "^$topic" master`
	if test -z "$not_in_topic"
	then
		echo >&2 "$topic is already up to date with master"
		exit 1 ;# we could allow it, but there is no point.
	else
		exit 0
	fi
else
	not_in_next=`git rev-list --pretty=oneline ^${publish} "$topic"`
	/usr/bin/perl -e '
		my $topic = $ARGV[0];
		my $msg = "* $topic has commits already merged to public branch:\n";
		my (%not_in_next) = map {
			/^([0-9a-f]+) /;
			($1 => 1);
		} split(/\n/, $ARGV[1]);
		for my $elem (map {
				/^([0-9a-f]+) (.*)$/;
				[$1 => $2];
			} split(/\n/, $ARGV[2])) {
			if (!exists $not_in_next{$elem->[0]}) {
				if ($msg) {
					print STDERR $msg;
					undef $msg;
				}
				print STDERR " $elem->[1]\n";
			}
		}
	' "$topic" "$not_in_next" "$not_in_master"
	exit 1
fi

<<\DOC_END

This sample hook safeguards topic branches that have been
published from being rewound.

The workflow assumed here is:

 * Once a topic branch forks from "master", "master" is never
   merged into it again (either directly or indirectly).

 * Once a topic branch is fully cooked and merged into "master",
   it is deleted.  If you need to build on top of it to correct
   earlier mistakes, a new topic branch is created by forking at
   the tip of the "master".  This is not strictly necessary, but
   it makes it easier to keep your history simple.

 * Whenever you need to test or publish your changes to topic
   branches, merge them into "next" branch.

The script, being an example, hardcodes the publish branch name
to be "next", but it is trivial to make it configurable via
$GIT_DIR/config mechanism.

With this workflow, you would want to know:

(1) ... if a topic branch has ever been merged to "next".  Young
    topic branches can have stupid mistakes you would rather
    clean up before publishing, and things that have not been
    merged into other branches can be easily rebased without
    affecting other people.  But once it is published, you would
    not want to rewind it.

(2) ... if a topic branch has been fully merged to "master".
    Then you can delete it.  More importantly, you should not
    build on top of it -- other people may already want to
    change things related to the topic as patches against your
    "master", so if you need further changes, it is better to
    fork the topic (perhaps with the same name) afresh from the
    tip of "master".

Let's look at this example:

		   o---o---o---o---o---o---o---o---o---o "next"
		  /       /           /           /
		 /   a---a---b A     /           /
		/   /               /           /
	       /   /   c---c---c---c B         /
	      /   /   /             \         /
	     /   /   /   b---b C     \       /
	    /   /   /   /             \     /
    ---o---o---o---o---o---o---o---o---o---o---o "master"


A, B and C are topic branches.

 * A has one fix since it was merged up to "next".

 * B has finished.  It has been fully merged up to "master" and "next",
   and is ready to be deleted.

 * C has not merged to "next" at all.

We would want to allow C to be rebased, refuse A, and encourage
B to be deleted.

To compute (1):

	git rev-list ^master ^topic next
	git rev-list ^master        next

	if these match, topic has not merged in next at all.

To compute (2):

	git rev-list master..topic

	if this is empty, it is fully merged to "master".

DOC_END
                                                                                                                                                                                                                              loadfromxml/loadxmltoelastic/.git/hooks/pre-commit.sample                                           000755  000765  000024  00000003146 14424573166 025712  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         #!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

if git rev-parse --verify HEAD >/dev/null 2>&1
then
	against=HEAD
else
	# Initial commit: diff against an empty tree object
	against=$(git hash-object -t tree /dev/null)
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.
if [ "$allownonascii" != "true" ] &&
	# Note that the use of brackets around a tr range is ok here, (it's
	# even required, for portability to Solaris 10's /usr/bin/tr), since
	# the square bracket bytes happen to fall in the designated range.
	test $(git diff --cached --name-only --diff-filter=A -z $against |
	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
then
	cat <<\EOF
Error: Attempt to add a non-ASCII file name.

This can cause problems if you want to work with people on other platforms.

To be portable it is advisable to rename the file.

If you know what you are doing you can disable this check using:

  git config hooks.allownonascii true
EOF
	exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --
                                                                                                                                                                                                                                                                                                                                                                                                                          loadfromxml/loadxmltoelastic/.git/hooks/applypatch-msg.sample                                       000755  000765  000024  00000000736 14424573166 026571  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         #!/bin/sh
#
# An example hook script to check the commit log message taken by
# applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.  The hook is
# allowed to edit the commit message file.
#
# To enable this hook, rename this file to "applypatch-msg".

. git-sh-setup
commitmsg="$(git rev-parse --git-path hooks/commit-msg)"
test -x "$commitmsg" && exec "$commitmsg" ${1+"$@"}
:
                                  loadfromxml/loadxmltoelastic/.git/hooks/fsmonitor-watchman.sample                                   000755  000765  000024  00000006377 14424573166 027467  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         #!/usr/bin/perl

use strict;
use warnings;
use IPC::Open2;

# An example hook script to integrate Watchman
# (https://facebook.github.io/watchman/) with git to speed up detecting
# new and modified files.
#
# The hook is passed a version (currently 1) and a time in nanoseconds
# formatted as a string and outputs to stdout all files that have been
# modified since the given time. Paths must be relative to the root of
# the working tree and separated by a single NUL.
#
# To enable this hook, rename this file to "query-watchman" and set
# 'git config core.fsmonitor .git/hooks/query-watchman'
#
my ($version, $time) = @ARGV;

# Check the hook interface version

if ($version == 1) {
	# convert nanoseconds to seconds
	$time = int $time / 1000000000;
} else {
	die "Unsupported query-fsmonitor hook version '$version'.\n" .
	    "Falling back to scanning...\n";
}

my $git_work_tree;
if ($^O =~ 'msys' || $^O =~ 'cygwin') {
	$git_work_tree = Win32::GetCwd();
	$git_work_tree =~ tr/\\/\//;
} else {
	require Cwd;
	$git_work_tree = Cwd::cwd();
}

my $retry = 1;

launch_watchman();

sub launch_watchman {

	my $pid = open2(\*CHLD_OUT, \*CHLD_IN, 'watchman -j --no-pretty')
	    or die "open2() failed: $!\n" .
	    "Falling back to scanning...\n";

	# In the query expression below we're asking for names of files that
	# changed since $time but were not transient (ie created after
	# $time but no longer exist).
	#
	# To accomplish this, we're using the "since" generator to use the
	# recency index to select candidate nodes and "fields" to limit the
	# output to file names only. Then we're using the "expression" term to
	# further constrain the results.
	#
	# The category of transient files that we want to ignore will have a
	# creation clock (cclock) newer than $time_t value and will also not
	# currently exist.

	my $query = <<"	END";
		["query", "$git_work_tree", {
			"since": $time,
			"fields": ["name"],
			"expression": ["not", ["allof", ["since", $time, "cclock"], ["not", "exists"]]]
		}]
	END

	print CHLD_IN $query;
	close CHLD_IN;
	my $response = do {local $/; <CHLD_OUT>};

	die "Watchman: command returned no output.\n" .
	    "Falling back to scanning...\n" if $response eq "";
	die "Watchman: command returned invalid output: $response\n" .
	    "Falling back to scanning...\n" unless $response =~ /^\{/;

	my $json_pkg;
	eval {
		require JSON::XS;
		$json_pkg = "JSON::XS";
		1;
	} or do {
		require JSON::PP;
		$json_pkg = "JSON::PP";
	};

	my $o = $json_pkg->new->utf8->decode($response);

	if ($retry > 0 and $o->{error} and $o->{error} =~ m/unable to resolve root .* directory (.*) is not watched/) {
		print STDERR "Adding '$git_work_tree' to watchman's watch list.\n";
		$retry--;
		qx/watchman watch "$git_work_tree"/;
		die "Failed to make watchman watch '$git_work_tree'.\n" .
		    "Falling back to scanning...\n" if $? != 0;

		# Watchman will always return all files on the first query so
		# return the fast "everything is dirty" flag to git and do the
		# Watchman query just to get it over with now so we won't pay
		# the cost in git to look up each individual file.
		print "/\0";
		eval { launch_watchman() };
		exit 0;
	}

	die "Watchman: $o->{error}.\n" .
	    "Falling back to scanning...\n" if $o->{error};

	binmode STDOUT, ":utf8";
	local $, = "\0";
	print @{$o->{files}};
}
                                                                                                                                                                                                                                                                 loadfromxml/loadxmltoelastic/.git/hooks/pre-receive.sample                                          000755  000765  000024  00000001040 14424573166 026033  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         #!/bin/sh
#
# An example hook script to make use of push options.
# The example simply echoes all push options that start with 'echoback='
# and rejects all pushes when the "reject" push option is used.
#
# To enable this hook, rename this file to "pre-receive".

if test -n "$GIT_PUSH_OPTION_COUNT"
then
	i=0
	while test "$i" -lt "$GIT_PUSH_OPTION_COUNT"
	do
		eval "value=\$GIT_PUSH_OPTION_$i"
		case "$value" in
		echoback=*)
			echo "echo from the pre-receive-hook: ${value#*=}" >&2
			;;
		reject)
			exit 1
		esac
		i=$((i + 1))
	done
fi
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                loadfromxml/loadxmltoelastic/.git/hooks/prepare-commit-msg.sample                                   000755  000765  000024  00000002724 14424573166 027347  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         #!/bin/sh
#
# An example hook script to prepare the commit log message.
# Called by "git commit" with the name of the file that has the
# commit message, followed by the description of the commit
# message's source.  The hook's purpose is to edit the commit
# message file.  If the hook fails with a non-zero status,
# the commit is aborted.
#
# To enable this hook, rename this file to "prepare-commit-msg".

# This hook includes three examples. The first one removes the
# "# Please enter the commit message..." help message.
#
# The second includes the output of "git diff --name-status -r"
# into the message, just before the "git status" output.  It is
# commented because it doesn't cope with --amend or with squashed
# commits.
#
# The third example adds a Signed-off-by line to the message, that can
# still be edited.  This is rarely a good idea.

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

/usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"

# case "$COMMIT_SOURCE,$SHA1" in
#  ,|template,)
#    /usr/bin/perl -i.bak -pe '
#       print "\n" . `git diff --cached --name-status -r`
# 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
#  *) ;;
# esac

# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# if test -z "$COMMIT_SOURCE"
# then
#   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# fi
                                            loadfromxml/loadxmltoelastic/.git/hooks/post-update.sample                                          000755  000765  000024  00000000275 14424573166 026103  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         #!/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info
                                                                                                                                                                                                                                                                                                                                   loadfromxml/loadxmltoelastic/.git/hooks/pre-applypatch.sample                                       000755  000765  000024  00000000650 14424573166 026564  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         #!/bin/sh
#
# An example hook script to verify what is about to be committed
# by applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-applypatch".

. git-sh-setup
precommit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$precommit" && exec "$precommit" ${1+"$@"}
:
                                                                                        loadfromxml/loadxmltoelastic/.git/hooks/pre-push.sample                                             000755  000765  000024  00000002504 14424573166 025376  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         #!/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local sha1> <remote ref> <remote sha1>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

z40=0000000000000000000000000000000000000000

while read local_ref local_sha remote_ref remote_sha
do
	if [ "$local_sha" = $z40 ]
	then
		# Handle delete
		:
	else
		if [ "$remote_sha" = $z40 ]
		then
			# New branch, examine all commits
			range="$local_sha"
		else
			# Update to existing branch, examine new commits
			range="$remote_sha..$local_sha"
		fi

		# Check for WIP commit
		commit=`git rev-list -n 1 --grep '^WIP' "$range"`
		if [ -n "$commit" ]
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0
                                                                                                                                                                                            loadfromxml/loadxmltoelastic/.git/hooks/update.sample                                               000755  000765  000024  00000007032 14424573166 025116  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         #!/bin/sh
#
# An example hook script to block unannotated tags from entering.
# Called by "git receive-pack" with arguments: refname sha1-old sha1-new
#
# To enable this hook, rename this file to "update".
#
# Config
# ------
# hooks.allowunannotated
#   This boolean sets whether unannotated tags will be allowed into the
#   repository.  By default they won't be.
# hooks.allowdeletetag
#   This boolean sets whether deleting tags will be allowed in the
#   repository.  By default they won't be.
# hooks.allowmodifytag
#   This boolean sets whether a tag may be modified after creation. By default
#   it won't be.
# hooks.allowdeletebranch
#   This boolean sets whether deleting branches will be allowed in the
#   repository.  By default they won't be.
# hooks.denycreatebranch
#   This boolean sets whether remotely creating branches will be denied
#   in the repository.  By default this is allowed.
#

# --- Command line
refname="$1"
oldrev="$2"
newrev="$3"

# --- Safety check
if [ -z "$GIT_DIR" ]; then
	echo "Don't run this script from the command line." >&2
	echo " (if you want, you could supply GIT_DIR then run" >&2
	echo "  $0 <ref> <oldrev> <newrev>)" >&2
	exit 1
fi

if [ -z "$refname" -o -z "$oldrev" -o -z "$newrev" ]; then
	echo "usage: $0 <ref> <oldrev> <newrev>" >&2
	exit 1
fi

# --- Config
allowunannotated=$(git config --bool hooks.allowunannotated)
allowdeletebranch=$(git config --bool hooks.allowdeletebranch)
denycreatebranch=$(git config --bool hooks.denycreatebranch)
allowdeletetag=$(git config --bool hooks.allowdeletetag)
allowmodifytag=$(git config --bool hooks.allowmodifytag)

# check for no description
projectdesc=$(sed -e '1q' "$GIT_DIR/description")
case "$projectdesc" in
"Unnamed repository"* | "")
	echo "*** Project description file hasn't been set" >&2
	exit 1
	;;
esac

# --- Check types
# if $newrev is 0000...0000, it's a commit to delete a ref.
zero="0000000000000000000000000000000000000000"
if [ "$newrev" = "$zero" ]; then
	newrev_type=delete
else
	newrev_type=$(git cat-file -t $newrev)
fi

case "$refname","$newrev_type" in
	refs/tags/*,commit)
		# un-annotated tag
		short_refname=${refname##refs/tags/}
		if [ "$allowunannotated" != "true" ]; then
			echo "*** The un-annotated tag, $short_refname, is not allowed in this repository" >&2
			echo "*** Use 'git tag [ -a | -s ]' for tags you want to propagate." >&2
			exit 1
		fi
		;;
	refs/tags/*,delete)
		# delete tag
		if [ "$allowdeletetag" != "true" ]; then
			echo "*** Deleting a tag is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/tags/*,tag)
		# annotated tag
		if [ "$allowmodifytag" != "true" ] && git rev-parse $refname > /dev/null 2>&1
		then
			echo "*** Tag '$refname' already exists." >&2
			echo "*** Modifying a tag is not allowed in this repository." >&2
			exit 1
		fi
		;;
	refs/heads/*,commit)
		# branch
		if [ "$oldrev" = "$zero" -a "$denycreatebranch" = "true" ]; then
			echo "*** Creating a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/heads/*,delete)
		# delete branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/remotes/*,commit)
		# tracking branch
		;;
	refs/remotes/*,delete)
		# delete tracking branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a tracking branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	*)
		# Anything else (is there anything else?)
		echo "*** Update hook: unknown type of update to ref $refname of type $newrev_type" >&2
		exit 1
		;;
esac

# --- Finished
exit 0
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      loadfromxml/loadxmltoelastic/.git/info/exclude                                                      000644  000765  000024  00000000372 14424573166 023612  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         # git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~
.DS_Store
                                                                                                                                                                                                                                                                      loadfromxml/loadxmltoelastic/.git/objects/pack/                                                     000755  000765  000024  00000000000 14424573166 023650  5                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         loadfromxml/loadxmltoelastic/.git/objects/info/                                                     000755  000765  000024  00000000000 14424573166 023665  5                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         loadfromxml/pythonProject1/                                                                         000755  000765  000024  00000000000 14424517567 020024  5                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         loadfromxml/pythonProject1/main.py                                                                  000644  000765  000024  00000001007 14424517567 021320  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         # This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         loadfromxml/pythonProject1/.idea/                                                                   000755  000765  000024  00000000000 14424517613 020774  5                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         loadfromxml/pythonProject1/.idea/aws.xml                                                            000644  000765  000024  00000000446 14424517526 022317  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         <?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="accountSettings">
    <option name="activeRegion" value="us-east-1" />
    <option name="recentlyUsedRegions">
      <list>
        <option value="us-east-1" />
      </list>
    </option>
  </component>
</project>                                                                                                                                                                                                                          loadfromxml/pythonProject1/.idea/inspectionProfiles/                                                000755  000765  000024  00000000000 14424517613 024653  5                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         loadfromxml/pythonProject1/.idea/pythonProject1.iml                                                 000644  000765  000024  00000000434 14424517613 024431  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         <?xml version="1.0" encoding="UTF-8"?>
<module type="PYTHON_MODULE" version="4">
  <component name="NewModuleRootManager">
    <content url="file://$MODULE_DIR$" />
    <orderEntry type="inheritedJdk" />
    <orderEntry type="sourceFolder" forTests="false" />
  </component>
</module>                                                                                                                                                                                                                                    loadfromxml/pythonProject1/.idea/.gitignore                                                         000644  000765  000024  00000000057 14424517541 022766  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         # Default ignored files
/shelf/
/workspace.xml
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 loadfromxml/pythonProject1/.idea/workspace.xml                                                      000644  000765  000024  00000002141 14424517613 023512  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         <?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="RunManager">
    <configuration name="main" type="PythonConfigurationType" factoryName="Python" nameIsGenerated="true">
      <module name="pythonProject1" />
      <option name="INTERPRETER_OPTIONS" value="" />
      <option name="PARENT_ENVS" value="true" />
      <envs>
        <env name="PYTHONUNBUFFERED" value="1" />
      </envs>
      <option name="SDK_HOME" value="" />
      <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$" />
      <option name="IS_MODULE_SDK" value="true" />
      <option name="ADD_CONTENT_ROOTS" value="true" />
      <option name="ADD_SOURCE_ROOTS" value="true" />
      <option name="SCRIPT_NAME" value="$PROJECT_DIR$/main.py" />
      <option name="PARAMETERS" value="" />
      <option name="SHOW_COMMAND_LINE" value="false" />
      <option name="EMULATE_TERMINAL" value="false" />
      <option name="MODULE_MODE" value="false" />
      <option name="REDIRECT_INPUT" value="false" />
      <option name="INPUT_FILE" value="" />
      <method v="2" />
    </configuration>
  </component>
</project>                                                                                                                                                                                                                                                                                                                                                                                                                               loadfromxml/pythonProject1/.idea/modules.xml                                                        000644  000765  000024  00000000430 14424517613 023163  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         <?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ProjectModuleManager">
    <modules>
      <module fileurl="file://$PROJECT_DIR$/.idea/pythonProject1.iml" filepath="$PROJECT_DIR$/.idea/pythonProject1.iml" />
    </modules>
  </component>
</project>                                                                                                                                                                                                                                        loadfromxml/pythonProject1/.idea/inspectionProfiles/profiles_settings.xml                           000644  000765  000024  00000000256 14424517613 031143  0                                                                                                    ustar 00satishbomma                     staff                           000000  000000                                                                                                                                                                         <component name="InspectionProjectProfileManager">
  <settings>
    <option name="USE_PROJECT_PROFILE" value="false" />
    <version value="1.0" />
  </settings>
</component>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  