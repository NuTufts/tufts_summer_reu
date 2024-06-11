This file provides instructions for logging into the cluster and setting up our standard cluster environment.

## Logging Into the Cluster and Storage Areas

Open a terminal on your computer and run the following command to connect to the cluster.

(Note: in the following, everytime you see `<username>` this is a placeholder indicating where your Tufts username should go.)

```
ssh -XY <username>@login.pax.tufts.edu
```

You should see a prompt that looks like the following:
```
<username>@login-prod-02 ~]
```

If you type in `pwd`, your present working directory should show up. This is your home folder.
```
/cluster/home/twongj01
```

In this location, you have a very limited amount of disk space. You should put your working files and data files in our group's storage area. This is:

```
/cluster/tufts/wongjiradlabnu/
```

If you run `ls /cluster/tufts/wongjiradlabnu/` you should get a list of directories. You should see a folder with your name. This is where you code and files should go.

## Starting an interactive job

When you first log in, you will be on one of the designated 'log in nodes'. You are not suppose to run any kind of data intensive job here. Instead, you need to start an interactive job which will transport you to one of the worker nodes on the cluster.

To do this, run:

```
srun --pty --mem-per-cpu 8000 --time 8:00:00 bash
```

What this command did was 
* start a job using the slurm job system `srun`,
* once the job is launched, make a terminal connection, `--pty`
* ask for 8 GB of memory for the job (`--mem-per-cpu 8000`),
* and give the job a maximum run time of 8 hours

When you run it, you will see something like this,
```
srun: job 4781777 queued and waiting for resources
srun: job 4781777 has been allocated resources
[<username>@d1cmp006 ~]$ 
```
In this instance, I got assigned to a computer in the cluster named, `d1cmp006`.

Tip: if you cannot remember the exact command, you can search your terminal history. To do so, hit CTRL+R, in the terminal, it'll give you a `(reverse-i-search):` prompt. 
In it, type run `srun`. The most recent command you typed with that keyword will show up. 
* You can hit CRTL+R again to go to the next instance.
* CRTL+C will get you out of the prompt.
* ENTER will accept the command.

## Starting a container

To build or run our code, you need to be inside a container environment.  [Containers explained in a 4 minute video with an overdone introduction](https://www.youtube.com/watch?v=pR-cGS6IGvI)

First, we need to activate the container system.

```
module load singularity/3.5.3
```

Then we can start our container.

```
singularity shell --bind /cluster/tufts/:/cluster/tufts/ /cluster/tufts/wongjiradlabnu//larbys/larbys-container/singularity_minkowskiengine_u20.04.cu111.torch1.9.0_comput8.sif 
```

This command 
* started a container and provided you with an interactive shell `shell`
* it binded the cluster directories,  `--bind /cluster/tufts/:/cluster/tufts/`, so you can see the folders inside the cluster.

When you run the command, you'll see the following prompt:
```
Singularity>
```
Within it type, `bash`, to start a bash shell.

Now you are 'inside' the container. You'll have the core set of libraries we use to run our analysis code.

For example, in this particular container, we have ROOT installed at:

```
/usr/local/root
```

To setup shell environment variables so that you can use ROOT, run
```
source /usr/local/root/bin/thisroot.sh
```

Now you can use ROOT. For example, to go into the ROOT iterpreter, run: `root -b`
```
$ root -b
   ------------------------------------------------------------------
  | Welcome to ROOT 6.24/02                        https://root.cern |
  | (c) 1995-2021, The ROOT Team; conception: R. Brun, F. Rademakers |
  | Built for linuxx8664gcc on Jun 28 2021, 09:28:51                 |
  | From tags/v6-24-02@v6-24-02                                      |
  | With                                                             |
  | Try '.help', '.demo', '.license', '.credits', '.quit'/'.q'       |
   ------------------------------------------------------------------

root [0] 
```
Note: if things take a moment to load, don't fret.  Often, the compute node is caching data stored on the network drive locally -- or something.

To exit out of the container, run:
`exit`

You'll drop back into the default Singularity shell. Just type exit again, to drop out of the container.


