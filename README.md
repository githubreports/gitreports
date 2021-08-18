# gitreports

Script to get the User Details , Repository details and languages identified in GIT 

How To Use:

Clone the repo and run the below command

python gitreport.py --organisation org name --authkey gitauthkey

<pre>
usage: gitreport.py [-h] --organisation ORGANISATION --authkey AUTHKEY

optional arguments:
  -h, --help            show this help message and exit
  --organisation ORGANISATION
                        organisation
  --authkey AUTHKEY     git hub auth key
</pre>

Sample CSV Ouput File Content:

<pre>
login;name;email;repos;languages

kiran007;Kiran Reddy;kiran.yerram139@gmail.com;python_project,myrepo;java,python,go
<pre>
