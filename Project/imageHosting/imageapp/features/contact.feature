Feature: User is at contact page
		 I am a user who need assistance with ImageSpace
		 I can contact the ImageSpace owner
	
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
		And I should see header "See you later. Login anytime you wish"
		
	
		