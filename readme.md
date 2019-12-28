RNMC Hunt
========================================

Overview
----------------------------------------

The foundations of a 'kickstarter' website based on a 'Product Hunt' clone. A place where you can post your products or ideas so that people can check them out and vote for them.

Everything revolves around Function-based views using Django for Backend and HTML, a little of Javascript and Bootstrap for the Front-End. I focus entirely on Backend, so sorry if the Front makes your eyes bleed.

This is a very simple and basic project, which I put together just to practice, following Nick Walter's proposed exercise at his ['Django 2.2 & Python, The Ultimate Web Development Bootcamp'](https://www.udemy.com/course/the-ultimate-beginners-guide-to-django-django-2-python-web-dev-website/) course at Udemy. Awesome lessons and outstanding teacher, definitely learnt lots from him.

There is a bug I could not figure out in the entity-relationship model whenever you up or downvote a product, which leads to a wonky behavior on the buttons stylings. I will try to look for them up later. Not considering that, the main functionality of the website is intact.

As for my other projects, please feel free to go to [my GitHub page](https://github.com/RenzoMurinaCadierno) to check them out. I am still on my learning tracks, so you will see new projects frequently. I tend to specialize in Python and Javascript, and whatever I upload is normally related to web, game and app developing, or Python scripting for multiple purposes.

Instructions
------------------------------------------

Just like a Product Hunt website.

As a **user** you can:

- Navigate to the main item route by clicking on their names or images on the main page. You will be redirected to the post page, where you can check who Posted it, when they did so, and the description as well as the image.

As an **registered user** you can:

- Create a post for your product/service/idea using the "+" icon in the navbar.
- Once the post is created, it will be published on the main page. From there onwards, people can see it from the main page, access it, and vote for it.
- Vote for posts on the home page or on its main page. Once Upvoted, you can click again to downvote it. Only one vote per user per post is allowed.

What I learned from this project
------------------------------------------
This is a new section I will try to put together from now on each time I upload something new, since I do not tend to 'finish' a project without having learnt at least a little more than before.

- How to keep track of user 'likes', and to restrict them to once per post per user.
- How to use hidden forms whenever we deal with GET requests linked to 'a' tags or buttons by converting them to POST and submitting them to those hidden forms. This helps with browser compatibility, since some of them trigger GET requests by default when rendering the site for the first time.
- How to install, link to a project, visualize and use PostgresSQL in a simple way.
- How to add flat icons to the website.
- How to ask for several table fields related by ManyToMany and ForeignKey relationships when querying for data.
- How NOT to hit the database. I tried to query the DB on models.py and templates, thing that is normally not intended in this framework.
- How NOT to use for loops on template tags. I was tempted to call for something like {% break %} too many times along the development, but Django's model is not supposed to do so. That logic is always handled in views.

### Thank you for reading and for taking your time to check this project out! ###
