Feature: User is at home page
		 I am an image space user
		 I can access multiple pages 
	
	Scenario: New user
		Given that I am a new user
		Then I see "Welcome to your album.... Oops! It's empty...Upload photo"
		When I click "Upload photo" 
		I should see "/upload/"

	Scenario: Existing user
		Given that I am an existing user
		Then I should see all of my uploaded pictures

	Scenario: User clicks on "edit" on a photo
		Given that I want to edit a photo
		And I click edit
		Then I should see an adjustment bar that enhances the brightness
		
	Scenario: User clicks on "contact us"
		Given that I need to contact the owner of imageSpace
		Then I should see "/contact/"
	
	Scenario: User clicks on "home"
		Given that I want to go to the home page
		Then I should see "/home/"
	
	Scenario: User clicks on "upload"
		Given that I want to upload a new photo
		Then I should see "/upload/"
	
	Scenario: User clicks on Setting
		Given that I want to change my profile pictures
		Then I should see "/settings/"
	
	Scenario: User clicks logout
		Given that I am done using imageSpace
		Then I should see "/logout/"


