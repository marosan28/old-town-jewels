# old-town-jewels
# About
Old Town Jewels is an online jewellery store built using the Django web framework. It was developed as a part of a Fullstack course with Code Institute.

The store offers a wide variety of beautiful and unique jewellery pieces, including rings, earrings, necklaces, and more. Customers can browse the store's inventory, add items to their cart, and complete their purchase securely through the website.

Old Town Jewels is designed to be user-friendly and easy to navigate. The store features a clean and modern design, with high-quality product photos and detailed product descriptions to help customers make informed purchasing decisions.

Whether you're looking for a special piece of jewellery for yourself or a gift for someone else, Old Town Jewels has something for everyone. We hope you enjoy shopping with us!


[View the live project here](https://old-town-jewels.herokuapp.com/ "Link to deployed site - Old Town Jewels")


# Table of Contents

[User Experience](#user-experience)

- [Strategy](#strategy)

- [User Stories](#user-stories)

- [Scope](#scope)

- [Structure](#structure)
    - [Design](#design)
        - [Wireframes](#wireframes)
        - [Color Schema](#color-schema)
        - [Model Schema](#model-schema)

- [Marketing Strategies](#marketing-strategies)

- [Features](#features)

- [Technologies Used](#technologies-used)

- [Testing](#Testing)

- [Bugs Found](#bugs-found)

- [Deployment](#deployment)

- [Credit](#credit)

- [Acknowledgments](#Acknowledgments)


# User experience

At Old Town Jewels, our goal is to provide an enjoyable and seamless shopping experience for both our customers and the store owner. To achieve this, we have implemented the following strategies:

# Strategy
## For Customer
1. Easy navigation: We have designed the store's layout and menu to be intuitive and easy to use, so customers can easily find  what they are looking for.

2. Clear product descriptions: We have provided detailed descriptions of each product, including information on materials, sizing, and care instructions. This helps customers make informed purchasing decisions.

3. Secure checkout: We have implemented secure payment methods and encrypted data transmission to protect our customers' personal and financial information.

### What's New

4. User Profiles: Added User profiles for customers where they can modify their personal information, date of birth, name, email and also change a password.

5. Reviews: Added reviews on each product where customers can rate the product themselves and see the average rating of each product. Users are allowed to modify/delete their c omments.

6. User emails: Users are now getting emails after each completed order with their order summary, price and payment method.

## For Owner 
1. Easy inventory management: We have provided tools for the owner to easily add, update, and delete products from the store's inventory.

2. Detailed sales reports: The owner can access reports on sales data, including total revenue.

3. Track payments: The owner can track payments on the admin dashboard and print a csv file of each order if desired.

By following these strategies, we hope to create a positive user experience for our customers and encourage them to shop with us again in the future.

# User Stories
As the superuser of Old Town Jewels, I want to be able to:

1. **Add and manage products**: I want to be able to easily add new products to the store's inventory, as well as update and delete existing products.

2. **View and analyze sales data**: I want to be able to access detailed reports on sales data, including total revenue and popular products.

3. **Manage user accounts**: I want to be able to add, update, and delete user accounts, including customer and employee accounts.

4. **Manage orders**: I want to be able to view and manage orders, including marking orders as shipped and canceling orders if necessary.

5. **Create and manage coupons**: I want to be able to create and manage coupons, including setting expiration dates and usage limits, and track their usage.


By being able to perform these tasks, I can effectively manage and maintain the Old Town Jewels store.

As a shopper at Old Town Jewels, I want to be able to:

1. **Easily browse and search for products**: I want to be able to easily browse through the store's inventory and use section filters to find specific products.

2. **View detailed product information**: I want to be able to see photos of the products and read detailed descriptions, including information on materials, sizing, and care instructions.

3. **Add items to my cart and complete my purchase**: I want to be able to easily add items to my cart and complete my purchase securely through the website.

4. **Apply coupons to my order**: I want to be able to enter a coupon code at checkout and have the discount applied to my order.

### What's New

5. **Log in and see my profile**: I want to be able to log in to the website, visit my profile and modify personal details.

6. **Leave a review on the product, or check ratings of a product**: I want to be able to comment on a product, rate it and edit/delete the review. I want to see the average reviews of the selected product to help me bring a decision about buying.

7. **Receive an email after purchase**: I want to receive an email after completing a purchase with my order summary, payment method, the amount I paid.

By being able to perform these tasks, I can easily shop and make purchases at Old Town Jewels.


# Scope

# User Story 1: Easily browse and search for products
Customers can easily browse through the store's inventory and use search filters to find specific products.

# User Story 2: View detailed product information
Customers can view high-quality photos of the products and read detailed descriptions, including information on materials, sizing, and care instructions.

# User Story 3: Add items to my cart and complete my purchase
Customers can easily add items to their cart and complete their purchase securely through the website.

# User Story 4: Apply coupons to my order
Customers have the option to apply coupons to their orders at checkout by entering a coupon code.

### What's new
# User Story 5: User Profiles
Customers can log in and view their profile. Customers are allowed to modify personal information including a password reset on the profile. 

# User Story 6: Password Reset
Customers can request a password reset and get an email with a link for a password change in case of a forgotten password. 

# User Story 7: Reviews
Customers are allowed to leave reviews on all products with a star rating, modify the reviews/delete accordingly. Customers are allowed to see the average rating of each product to help them make a decision before making a purchase.

# User Story 8: Delivery
Customers are allowed to add a delivery charge on their order. 

# User Story 8: Payment Information
Customers are getting a detailed overview of their purchase after successfull payments. All information is also forwareded onto the email address provided earlier in the checkout. 

# Superuser

# User Story 5: Add and manage products
As the superuser of the store, I can easily add and manage products.

# User Story 6: View and analyze sales data
As the superuser of the store, I can view and analyze sales data, including total revenue and popular products.

# User Story 7: Manage user accounts
As the superuser of the store, I can manage user accounts, including customer and employee accounts. 

# User Story 8: View and analyze sales data
As the superuser of the store, I can access detailed reports on sales data, including total revenue and popular products.

# User Story 9: Manage user accounts
As the superuser of the store, I can add, update, and delete user accounts, .

# User Story 10: Manage orders
As the superuser of the store, I can view and manage orders, including marking orders as shipped and canceling orders if necessary.

# User Story 11: Create and manage coupons
As the superuser of the store, I can create and manage coupons, including setting expiration dates and usage limits, and track their usage.

By providing these features, Old Town Jewels aims to create a positive shopping experience for both customers and the store owner.


# Structure

This project is structured with a homepage with the website's logo and a message that greets the user with a clear navigation bar at the top of the page where the user can login or sign up. When logging in user is allowed to request a email password reset in case of a forgotten password.
After the User logs in he is able to visit his profile section and make modifications of his personal information, customer is also allowed to change his password while being logged in. Customers can inspect products and see average reviews on product details helping them make a decision while shopping. Customers are also allowed to leave their own comments and ratings below each product. Old Town Jewels shop enables clients to browse products, add them to the cart, apply discount codes, go through the checkout process and pay with a credit a card. After successfull payment has been made, customers are greeted with a message containing their order information, payment method, last 4 digits of the card they used on checkout, payment ID, date of purchase. The information is also forwarded to their emails. Additionally fully functional 404 error page has been added. 

**The website is made of the following apps**:

1. MyShop
2. Users
3. Cart
4. Coupons
5. Orders
6. Payment
7. Shop
8. Delivery

## Design
In addition to the visually appealing and user-friendly design, the website was also built with functionality in mind. The navigation menu was strategically placed to make it easy for users to find the products they are looking for. The search bar is prominently displayed to allow users to quickly search for specific products.

To ensure a seamless user experience, the website was designed to be responsive, meaning that it can adapt to different screen sizes and devices, including desktops, laptops, tablets, and mobile phones. This was achieved through the use of fluid grids and flexible images, which allow the website to adjust to different screen sizes without sacrificing its overall design and functionality.

To maintain a cohesive appearance throughout the site, a limited color palette was used, with careful consideration given to the colors chosen. This helps to ensure that the site looks professional and visually appealing, without overwhelming the user with too many colors and distracting elements.

Overall, the website was designed with the user in mind, with the goal of creating a pleasant and intuitive shopping experience. The combination of a visually appealing design, user-friendly navigation, and responsive layout helps to achieve this goal, making the website an effective tool for selling products online.









- ## Color Schema
![App Screenshot](static/images/color-palete.png)
The colors #111111, #444444, and #333333 are shades of gray, with #111111 being the darkest and #333333 being the lightest. These colors give a sense of professionalism and sophistication, and can be used as a background or text color to create a clean and simple layout.

#ffc0cb is a shade of pink, which is often associated with warmth, playfulness, and femininity. It can be used as an accent color to add a pop of color to the layout without overwhelming the design.

#ffffff is pure white, which can be used as a background color to create a clean and modern look. It can also be used as a text color for areas where high contrast is needed, such as on dark backgrounds.

Overall, using these colors I achieved a simple and clean layout that allows the products to be the focal point.

- ## Model Schema
Our application uses two different databases: SQLite for local development and Postgres for the deployed app on Heroku. SQLite is a lightweight, file-based database that is easy to set up and use for development purposes. Postgres is a more powerful and feature-rich relational database that is well suited for production environments.

For local development, we use SQLite as the database. SQLite is included in Python's standard library and requires no additional setup.

For the deployed app on Heroku, we use Postgres as the database. Postgres is a powerful, open-source relational database that is well suited for production environments. It offers robust data integrity and security features, as well as advanced performance and scalability.

We have created a separate data model for each of the databases, which defines the tables, fields, and relationships used in the application. The data model for SQLite is designed for local development and is optimized for ease of use and rapid development. The data model for Postgres is designed for production and is optimized for performance, scalability, and data integrity.

To set up the databases, you will need to install SQLite and Postgres on your local machine and configure the appropriate settings in the application's configuration file. Once the databases are set up, you can use any SQL client to interact with the databases, such as the SQLite command-line tool or pgAdmin for Postgres.

Keep in mind that SQLite is file-based while Postgres is server-based, so you will have to configure the appropriate settings in the application's configuration file to connect the app to the right database depending on the environment, local or production.

Please note that the SQLite database will be created automatically when you run the application for the first time in local environment and the Postgres database should be created manually in Heroku before you deploy your app.

**Product Models**
- **orders app**
The **Order** model has a one-to-many relationship with the **OrderItem** model, as defined by the ForeignKey field in the **OrderItem** model that references the **Order model**. The **Order** model also has a foreign key relationship with the **Coupon** model, which is a one-to-many relationship where one coupon can be used in multiple orders. The **Order** model has a get_total_cost_before_discount method that sums the cost of all associated **OrderItem** objects and a get_discount method that calculates a discount based on the discount field and the total cost before discount. The **Order** model also has a method get_stripe_url that returns a Stripe URL based on the stripe_id field. The **OrderItem** model has a one-to-one relationship with the **Product model**, as defined by the ForeignKey field in the **OrderItem** model that references the **Product model**, and it also has a method get_cost that calculates the cost of the item by multiplying the price and quantity fields.
- **shop app**
The **Category** model has a one-to-many relationship with the **Product model**, as defined by the ForeignKey field in the **Product** model that references the **Category model**. This means that one category can have multiple products associated with it. The **Category** model has a get_absolute_url method that returns the URL of a page that displays all products of that category. The **Product** model has a name, slug, image, description, price, available, created, and updated fields and a get_absolute_url method that returns the URL of the product detail page. Additionally, the **Product** model has a Meta class that contains the indexes, ordering and other metainformation about the model.

**DeliveryOption model**: This model represents the delivery options available for the products. It has a name field that specifies the name of the delivery option, and a price field that specifies the delivery price. The price is stored as a decimal number with a maximum of 6 digits and 2 decimal places.

**Profile model**: This model represents the user profile. It has a one-to-one relationship with the built-in User model in Django, as specified by the OneToOneField. The profile contains additional information about the user, such as their date of birth and alternate contact information. It has a get_absolute_url method that returns the URL of the user's profile detail page.

**Review model**: This model represents the product reviews submitted by users. It has a foreign key relationship with the Product model, as defined by the ForeignKey field that references the Product model. It also has a foreign key relationship with the built-in User model in Django, as specified by the ForeignKey field that references the AUTH_USER_MODEL. The model includes a body field that contains the review text, a rating field that specifies the rating given by the user, and created and updated fields that record the date and time the review was created or last updated. The active field is a Boolean field that indicates whether the review is currently active or not. The Review model also has a Meta class that specifies the ordering and indexing options for the model.

# Marketing Strategies

In order to drive more traffic to the website and attract potential customers, the following marketing strategies have been employed:

1. Social Media Marketing: Three major social media platforms (Facebook, Instagram, Twitter) have been utilized to reach out to a wider audience and increase brand awareness. Regular posts, promotions, and interactive content have been shared to engage with the followers.

2. Search Engine Optimization (SEO): The website has been optimized for search engines to improve its visibility and ranking. This includes the implementation of a sitemap.xml file and robots.txt file, as well as the use of relevant keywords in the website's content and meta description.

3. Email Marketing: An email list has been created to send out newsletters, promotions, and other relevant updates to the subscribers.

By implementing these marketing strategies, the website aims to attract more customers and increase sales.

1. **Social Media Marketing** 

[Facebook](https://www.facebook.com/people/Old-Town-Jewels/100089850577128// "Facebook Link")
On Facebook, a business page for Old Town Jewels is created and used to showcase our products, 
share promotions and discounts, and interact with our customers.

[Instagram](https://www.instagram.com/ot__jewels/ "Instagram Link")
On Instagram, we plan to create a visually appealing account that highlights our products, showcases our brand, 
and shares customer reviews and testimonials.

[Twitter](https://twitter.com/old_townjewels "Twitter Link")
On Twitter, we plan to use Twitter to share updates about new products, promotions, and events, as well as respond to customer inquiries and feedback.

2. **SEO** 

**Keyword research**: To determine the most relevant and high-traffic keywords for this website
I made a list of important topics based on the type of the website and targeted users and researched related search terms. I used a keyword research tool
[Ahrefs](https://ahrefs.com/keywords-explorer)

**Technical SEO**: Technical optimizations I made to improve the crawlability and indexability of this site
Adding a sitemap.xml and robots.txt file and ensuring the site is mobile-friendly, using bootstrap for layouts and testing responsivness with Google Responsive Tools.

A website's essential pages are listed in an XML sitemap file so that Google can easily identify and crawl them individually. Additionally, it aids in the structure-understanding of search engines. The discovery of content is sped up with a sitemap. All the URLs on website that a search engine crawler may visit are specified in a robots.txt file. The rules are assigned to bots by stating their user-agent (the search engine bot) followed by directives (the rules). I have allowed all search engines to crawl this entire site. Thereafore my block looks like this:

```
User-agent: *
Allow: /
```

Meta tag in the HTML code, is used to provide a brief description of the website that may be displayed in search results
```
meta name="description" 
```

**Analytics and tracking** : In the future the plan to track and measure the success of SEO efforts, Google Analytics service will be set up. Google Analytics includes features that can help users identify trends and patterns in how visitors engage with their websites. Features enable data collection, analysis, monitoring, visualization, reporting and integration with other applications. 

**Continuous improvement**: Regular reexamination of ongoing SEO efforts is of big importance. Strategies should be continually monitored and updated  based on changing search algorithms and user behavior.

3. **Email Marketing**

Users are able to easily subscribe to the monthly newsletter at the bottom of the site. 

# Features



# Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks - Libraries - Programs Used
- [Django](https://www.djangoproject.com/)
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [ElephantSQL](https://www.elephantsql.com/)
- [Heroku](https://dashboard.heroku.com/login)
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")
- [Celery](https://docs.celeryq.dev/en/stable/)
- [RabbitMQ](https://www.rabbitmq.com/)

# Testing

## Index – Table of Contents

* [Manual Testing](#manual-testing) 
* [User Stories Testing](#user-stories-testing)
* [Responsiveness Testing](#responsiveness-testing)
* [HTML Testing](#html-testing)
* [CSS Testing](#css-testing)
* [Lighthouse Testing](#lighthouse-testing)


## Manual Testing

|  Test Label                                   | Action         | Expected Outcome                                          | Test Outcome  |
|-----------------------------------------------|----------------|-----------------------------------------------------------|---------------|
|    Register Button                            | Page load      |  Visible on homepage                                      | PASS          |
|    Login button in navigation bar             | Page load      |  Visible on homepage                                      | PASS          |
|    Login functionality                        | User input     |  Successful login redirects to homepage                   | PASS          |
|    Logout functionality                       | User input     |  Successful logs out and redirects to homepage            | PASS          |
|    User greeting in navbar                    | User input     |  Correctly displays "Hello, [username]"	                 | PASS          |
|    Shop link                                  | User input     |  Opens shop products                                      | PASS          |
|    Categories                                 | User input     |  Displays refined categories                              | PASS          |
|    Product details                            | User input     |  Displays product details on the page                     | PASS          |
|    Quantity                                   | User input     |  User can select the quantity and update susccessfully    | PASS          |
|    Add to cart button                         | User input     |  Product successfully updates the cart                    | PASS          |
|    Checkout                                   | User input     |  Product successfully updates the cart                    | PASS          |
|    Apply a coupon                             | User input     |  Coupon applies successfully to the cart                  | PASS          |
|    Continue Shopping Button                   | User input     |  Redirects to products categories                         | PASS          |
|    Checkout button                            | User input     |  Correctly displays form after clicking                   | PASS          |
|    Pay now button                             | User input     |  Correctly displays form after clicking                   | PASS          |

## Responsivness Testing

The app has been tested in Chrome with developer tools and showed to be fully responsive.

## HTML Testing


| HTML document             | Result | Issues found                                                            | Fixes made                                                                  |
|---------------------------|--------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| base.html                 | Fail   |1. Stray start tag <script>.                                             |1. Checked for script closed tags and invisible characters and whitespaces   |
| index.html                | Pass   |                                                                         |                                                                             |
| login.html                | Fail   |1. Unclosed element div                                                  |1. Close div element                                                         |
| logout.html               | Pass   |                                                                         |                                                                             |
| register.html             | Pass   |                                                                         |                                                                             |
| detail.html               | Fail   |1. Element div not allowed as child of element ul in this context.       |1. Wrap div element in li element                                            |
| list.html                 | Pass   |                                                                         |                                                                             |
| newsletter.html           | Pass   |                                                                         |                                                                             |
| cart/detail.html          | Fail   |1. Element div not allowed as child of element button in this context.   |1. Remove a element                                                          |
| payment-successfull.html  | Pass   |                                                                         |
| payment-unsuccessfull.html| Pass   |                                                                         |

# CSS Testing 

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

# Lighthouse Testing 

Desktop Testing with Google Lightouse
![App Screenshot](static/images/features/lighthouse-desktop.png)

Mobile Testing with Google Lighthouse
![App Screenshot](static/images/features/lighthouse-mobile.png)

## Bugs Found

### Criterion 1.2
- **Issue:** Insufficient feedback is relayed to the user in the event of successful and failed payment attempts. Confirmation e-mails are not sent on successful purchases.
- **Status:** Fixed

## Changes Made
### Criterion 1.2
- Added payment information on the payment_completed page after a successful payment.

![App Screenshot](static/images/features/payment-confirmed.png)

- Improved feedback to users on payment attempts by displaying relevant information such as payment method, transaction ID, and date. 

- Added email functionality using SMTP to send confirmation emails to users on successful purchases.

# Deployment

## Deploying-on-Heroku

To deploy this project on Heroku, the following steps were taken:

1. Create a new app on Heroku and choose a name and location for it.
2. In the Resources tab, add a Postgres database to the app by selecting the "Heroku Postgres" option under add-ons.
3. In the Settings tab, reveal the Config Vars and copy the url next to DATABASE_URL.
4. In the project's GitPod workspace, create an env.py file and add the DATABASE_URL and SECRET_KEY values to it.
5. Update the project's settings.py file to import the env file and add the SECRET_KEY and DATABASE_URL file paths.
6. Update the Config Vars with the Cloudinary URL, and also update the settings.py file with this URL.
7. In the settings.py file, add Cloudinary to the INSTALLED_APPS list, and add values for STATICFILE_STORAGE, STATICFILES_DIRS,   
   STATIC_ROOT, MEDIA_URL, DEFAULT_FILE_STORAGE, and TEMPLATES_DIR.
8. Update the DIRS in TEMPLATES with the TEMPLATES_DIR value, and update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost'].
9. Create media, storage, and templates directories in the main project directory, and add a Procfile with the following content: "web: gunicorn project-name.wsgi".
10. Log in to Heroku using the terminal and run the command "heroku git:remote -a your_app_name_here" to link the app to the GitPod workspace.
11. To deploy new versions of the app, run the command "git push heroku main" in the terminal

## Forking the Repository

1. Make sure you have a GitHub account. If you don't have one, you can create an account by going to https://github.com and following the prompts.
2. Go to the GitHub page for the repository you want to fork.
3. In the top right corner of the page, click the "Fork" button. This will create a copy of the repository in your account.
4. You can then clone the repository to your local machine by following the steps in the "Creating a clone" section above, replacing USERNAME with your own GitHub username and REPOSITORY with the name of the repository.
5. Once you have a copy of the repository on your local machine, you can make changes to it and commit those changes back to your fork on GitHub. You can also create a pull request to submit your changes to the original repository for review.

It's generally a good idea to keep your fork up to date with the original repository by regularly syncing your fork with the upstream repository. To do this, you can add the original repository as an upstream repository and then use the git pull command to sync your fork with the upstream repository.

## Creating a clone

1. Make sure you have Git installed on your local machine. You can check if you have it installed by running the command git --version in your terminal.
2. Navigate to the directory where you want to create a copy of the repository.
3. Run the command git clone https://github.com/USERNAME/REPOSITORY.git, replacing USERNAME with the username of the repository owner and REPOSITORY with the name of the repository. In this specific case (https://github.com/marosan28/old-town-jewels.git) This will create a copy of the repository in a new directory with the same name as the repository.
4. Change into the new directory by running the command cd REPOSITORY, replacing REPOSITORY with the name of the repository.
5. Run the command git branch to see a list of available branches in the repository.
6. To switch to a specific branch, run the command git checkout BRANCHNAME, replacing BRANCHNAME with the name of the branch you want to switch to.



# Credits

## Content 

For finding website content I was using [Google](https://www.google.com)

## Media
For creating the website logo I used [Canva](https://www.canva.com/hr_hr/)

# Acknowledgments

- Special thanks to Antonio Mele the creator of the book Django 4 By Example - Fourth Edition 
- Python crash course book by Eric Matthes
- Slack community
- Tutor support
