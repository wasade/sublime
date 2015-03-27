# sublime
Easy job submission to Torque-based clusters

Sublime is a light helper script for submitting jobs to a cluster. `sub`
automatically keeps track of what was run, important file locations, preserves
virtualenv, and switches to your current working directory. For instance, to
submit a job that calls the command hostname, just use:

    $ sub hostname

Additionally, you can specify the name of the job:

    $ sub -n testjob hostname

Walltime and queue is also available:

    $ sub -q friendlyq -m 2 -w 12:34:56 hostname

If submitting a command that also takes arguments, a POSIX separator must be
used to indicate the the split. For instance:

    $ sub -n testjob -- grep -i -n export ~/.bash_profile

## Practical example

In the example below, we're going to submit a simple job in a new directory,
and then show the files created and the contents of notes.

    $ workon some-virtualenv
    $ mkdir sub-testing
    $ cd sub-testing/
    $ ls
    total 0
    $ sub hostname
    Success! This job is named sub_jxwLOz with job id 112730.
    $ cat sub.notes
    time=10:01:49 on 27 Mar 2015
    id=sub_jxwLOz
    job_id=112730
    cmd=echo "cd `pwd`; source ~/.bash_profile;workon some-virtualenv; hostname" | qsub -o sub.oe -e sub.oe -N sub_jxwLOz -q route -l nodes=1:ppn=1
    resub=/Users/mcdonadt/bin/sub hostname
    expected_stdout=/Users/mcdonadt/sub-testing/sub.oe/sub_jxwLOz.o112730
    expected_stderr=/Users/mcdonadt/sub-testing/sub.oe/sub_jxwLOz.e112730

    $ ls sub.oe
    total 2.0K
    -rw-------+ 1 mcdonadt knightlab 0 Mar 27 10:01 sub_jxwLOz.e112730
    -rw-------+ 1 mcdonadt knightlab 8 Mar 27 10:01 sub_jxwLOz.o112730

## Running multiple commands in a job

It is possible to build up a list of commands to execute within a single job
as well. By using `--prime`, you can build up a list of commands. These
commands are stored in a file within the current working directory. The
commands can then be submitted by issuing a `--purge`. The `--purge` will
create a PBS script, store it under the sub.primed/ directory, and submit the
script to the cluster. The script includes a wait command at the end to ensure
that all executed commands complete.

### Running commands in serial

Below is an example that will run 3 commands serially:

    $ sub --prime -- hostname
    $ sub --prime -- uname -a
    $ sub --prime -- date
    $ sub --purge -q route -w 12:34:56

### Running commands in parallel

Below is the same example as the serial commands, except that we're adding an
ampersand (`&`) to the end of each command. Note that the command needs to be
encased in quotes. We're also indicating that our resource request needs 3
processors.

    $ sub --prime -- "hostname &"
    $ sub --prime -- "uname -a &"
    $ sub --prime -- "date &"
    $ sub --purge -p 3 -q route -w 12:34:56
