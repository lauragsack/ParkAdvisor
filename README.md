# ParkAdvisor

## :evergreen_tree: ParkAdvisor :evergreen_tree:
![Yosemite](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRebMjMHDksQyxxfX9yuc-Pa8yp52pKPX8lZaef57ZR7t1HmLzM&usqp=CAU)

### About This App
ParkAdviser is an app made for users to explore US National Parks. Users can add reviews to share and rate their park experiences. 

#### Checkit it out
Start exploring parks [here!](https://park-advisor.herokuapp.com/)
username: greatoutdoors
password: iloventlparks!

### User Stories

##### Site Page Load
* When a user visits park-advisor.herokuapp.com, a user will see these components:
* Homepage
* Header
* Navbar
* Footer
* From the homepage, an unauthenticated user can navigate to:
    * Explore Parks
    * About Us
    * Login
    * Signup
* From the homepage, an authenticated user can navigate to:
    * Explore Parks
    * About Us
    * My Reviews
    * Logout

##### Explore Parks
* If a user navigates to "Explore Parks", display a gallery of National Park cards
* If a user clicks "More Details", redirect the user to a park detail page
* On the park detail page, display the park's information, a "Add a Review" button, and users reviews for that park
* If a user clicks "Add a Review", redirect the user to a review form
* When the user clicks "Submit!", save the review and display it on the park detail page
* If the authenticated user is the same user that created the review, display "Update Review" and "Edit Review" buttons on the review card
* If a user clicks "Update Review", redirect the user to the review form and save when the user clicks "Submit!"
* If a user clicks "Delete Review", delete the review and remove it from the park detail page
* Display review category, subject, and likes on the review card
* Display a heart shaped button on the review card to enable users to like the review
* If the user clicks the heart button, increase review likes by 1.

##### My Reviews
* If a user navigates to "My Reviews", display a gallery of their reviews
* If a user clicks "More Details", redirect the user to a park detail page
* On each review card, add an "Edit" and "Delete" button
* If a user clicks "Edit", redirect the user to the review form and save when the user clicks "Submit!"
* If a user clicks "Delete Review", delete the review and remove it from the park detail page

### Wireframes
![Wireframes](https://i.imgur.com/megqFnh.png)
![Wireframes](https://i.imgur.com/pLnwa3U.png)

### ERD
![ERD](https://i.imgur.com/vpUG1EA.png)

##### References
These sources helped make ParkAdvisor a reality:
* https://unsplash.com/
* https://docs.djangoproject.com/en/3.0/
* https://getbootstrap.com/
* https://fontawesome.com/
* https://getbootstrap.com/docs/3.3/components/
* https://fonts.google.com/
* https://api.jquery.com/
* https://www.nps.gov/subjects/developer/api-documentation.htm
* https://www.npmjs.com/package/popper
