2/18/2023: Reminders to myself about how this works.

The github repo djohn89.com.source contains the source files that generate the github repo znoop333.github.io, which is hosted by GitHub Pages on the domain name djohn89.com (gandhi.net DNS).

To update the files:

Install Anaconda and create the env from conda-create.txt to install Pelican. Read the docs at https://docs.getpelican.com/en/latest/quickstart.html

Clone repos https://github.com/znoop333/djohn89.com.source and https://github.com/znoop333/znoop333.github.io into My Documents

Clone https://github.com/getpelican-themes/pelican-blueidea into My Documents. Edit the theme as needed

In djohn89.com.source, edit or create new files in source/

Run pelrun.bat from Anaconda using djohn89_com env

Run publish-locally.sh to copy output/* into ../znoop333.github.io

Commit the changes to znoop333.github.io, push back to GitHub

Wait for GitHub Pages to update the CDN.


The very old files (in websockets/ and science/) are not generated from Pelican. They are static content in znoop333.github.io only, which is referenced by the links in the headers MENUITEMS from the pelican configuration file, pelicanconf.py

Historical note: migrate-wordpress-to-pelican.py is not needed since the migration off Wordpress in 2018. What it did was to reformat the HTML from Wordpress into files that Pelican could process in djohn89.com.source/source/ . Since Wordpress had PHP vulnerabilities and cost $5/month, and Pelican was static content and free, switching to GitHub Pages was an easy decision. See also: migration-to-github-pages.html
