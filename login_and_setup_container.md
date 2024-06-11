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

Tip: if you cannot remember the exact command, you can search your terminal history. To do so, hit CTRL+R, in the terminal, it'll give you a `(reverse-i-search):` prompt. 
In it, type run `srun`. The most recent command you typed with that keyword will show up. 
* You can hit CRTL+R again to go to the next instance.
* CRTL+C will get you out of the prompt.
* ENTER will accept the command.






