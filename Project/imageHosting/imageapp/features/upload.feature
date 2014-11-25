Feature: User is at Upload page
		 I am an existing user
		 I am able to upload a new photo
	
	Scenario: User uploads a new photo
		Given that I want a new photo
		And I select a photo
		Then I should see the file name 
		And when I click "Submit" I should see "Uploaded successfully. Visit home page to see the change."
		
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
	
	