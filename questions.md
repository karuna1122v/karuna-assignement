# Questions

1. How do the following components get deployed in your current work environment,
from brain to production?
    a. Application code
    b. Configuration
    c. Infrastructure
Ans:
  a.  Once feature request created in the ticketing tool developer review the ticket then creates the feature branch in the repo. Once development done and raise the pull request from feature branch to main release branch.
   When pull request created in the jenkins multibranch pipeline creates PR pipeline and execute. As part of this pipeline execution it will execute below stages:
    stages:
       checkout (Multibrach pipeline checkout by default)
       build
       unit testing
       code coverage
       Code Quality check
       SAST
       SCA
   All above stages executed in the pipeline with quality gate condition. Once pipeline success update pipeline status in the bitbucket. Also reviwers need to review the code. Once done merge button enabled to developer to merge the code. 
On commit of code into main branch pipeline execute automatically and execute on integrated code all aabove quaility stages and below.
    Image Creation
    Image push to Artifactory
    Image tag updates in gitops configuration (Argocd gitops) [Dev env always we latest tag with hash no change and higher envs always specific tag pattern eg: timestampcommitid
    Deployement stage (Validate deployment status)
 Some of the microservice have  test cases where wil execute.
 QA team validate changes in the QA environment. Once signed off same images promoted to higher environments.

b. Configurations
    We maintain congifurations in gitops configutaions namespace(env) wise and also in another project all the properties maintaining in the config server/

C. Infrastructure.
   Currently we have onpremise redhat machines. Infra team provision those based on need. But we plan to migrate GCP and Terafform to use infra automation.

2. In your opinion, what is the purpose of an incident post-mortem?
 Ans:  Discuss together(Required teams and members) details of the incident. Why it happend,impact and how can avoid in the future. Give trust to client will try reduce the impacts in the future.
3. How do you handle (and feel about) making changes (code/schema/network/etc.) in
your current environment? How do you know the changes you made did not break
anything?
    Analyze the changes
    Work with depedent teams to take support (Db,Infra teams etc)
    Discuss in the cab meetings.
    Deploy or make changes in the lower environmentsa and validate changes. Avoild manual changes any cost.
    Promote to higher enviroments.
4. Let's say you have a directory that contains other directories, that contain
database files, that have these characteristics:

```bash
$ du -sh /data/
960G   /data/
$ find . -type d | wc -l
920
$ find . -type f | wc -l
353260
```
* What are 3 methods to copy this entire directory structure from one server to
another?
  ans:  scp,rsync,cp
* What are any methods to speed up this transfer?
  ans:  compress the file
        Limit background processes
* How can you measure the resource usage of any of these different methods of
transfer?
Ans: Disk read write spped during the trsafter or if file transfter monitoing tool available.
