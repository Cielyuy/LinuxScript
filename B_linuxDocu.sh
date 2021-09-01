#!/bin/bash
#SBATCH -J test1
#SBATCH -p cpu
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48







hostlist= echo `env |grep RMS_HOSTLIST|awk -F "=" '{print $2}'` | tr "," "\n" > hostlist





/home/ztc184212120/ansysInstall/v192/fluent/bin/fluent  -g  3d  -t48 -cnf=$hostlist   -mpi=intel -i J_M500_85_3850.jou >wenwen.txt

/home/ztc184212120/ansysInstall/v192/fluent/bin/fluent -g 3d -t48 -cnf=$hostlist -mpi=intel -i J_M500_85_3800.jou >miaomiao.txt
