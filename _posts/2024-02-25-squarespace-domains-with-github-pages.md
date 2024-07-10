---
layout: post
title: Custom Squarespace Domains with GitHub Pages
category: computer
---
Github Pages will host anyone's website for free, as long as it is statically generated (ie you aren't doing any fancy backend stuff like interacting with databases).

By default, the site will be hosted at `<github-username>.github.io`. For example, my website (the site you're on now) is hosted at [tristan-white.github.io](https://tristan-white.github.io).

But if you enter that in your search bar, you'll be sent to this site and see `tristanwhite.me` in the URL bar. The reason for this is that I've set up my github pages site to use a custom domain that was registered through Squarespace. 

## Steps to use Squarespace Domain with Github Pages
1. Change the name of you github account to `<username>.github.io`
2. Make a few changes in Settings > Pages section of your repo
	- Under **Build and deployment > Source** select "Deploy from a branch"
	- Under **Build and deployment > Branch** select "master" and "/ root"
	- Under **Build and deployment > Custom Domain** enter the domain name you registered with Squarespace.
3. Login to your Domains Dashboard on squarespace.com and click on the domain you have registered
4. Add DNS records
	- Go to the place to edit DNS records. At the time of this writing, there is a little button on the top right corner that says "Edit DNS"
	- Add a CNAME record with Host set to "www" and Data set to `<github-username>.github.io`
	- Add 4 A records exactly as shown in the picture.

![DNS Records for this website](./assets/images/squarespace-domain/records.png)

Your done! It may take time for the records to propagate so it's possible that it could take up to 72 hours for everything to take effect.
