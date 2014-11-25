Feature: User is at settings page
		 I am an existing user
		 I am able to upload a new profile picture
	
	Scenario: User uploads a new profile photo
		Given that I want a new photo
		And I select a photo
		Then I should see the file name 
		And when I click "Submit" I should see the new photo in an icon
		
	Scenario: User uploads no file
		Given that I click "Submit"
		Then I should see header "This field is required"
		
	Scenario: User clicks on "contact us"
		Given that I need to contact the owner of imageSpace
		Then I should see "/contact/"
	
	Scenario: User clicks on "home"
		Given that I want to go to the home page
		Then I should see "/home/"
	
	Scenario: User clicks on "upload"
		Given that I want to upload a new photo
		Then I should see "/upload/"
	
	Scenario: User clicks on "Setting"
		Given that I want to change my profile pictures
		Then I should see "/settings/"
	
	Scenario: User clicks "logout"
		Given that I am done using imageSpace
		Then I should see "/logout/"
		
	
		